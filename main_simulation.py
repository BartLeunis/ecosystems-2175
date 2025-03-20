# main_simulation.py
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import copy
from archive_ignored.ecosystem_parameters import ecosystems, ecosystem_areas, biodiversity_density_ratios, initial_biodiversity
from archive_ignored.simulation_parameters import final_baselines, original_consensus_loss, adjusted_loss_potentials, transform_targets, cascade_effects, logistic_params

# Define model parameters
years = np.arange(2025, 2176, 5)
n_iter = 1000
logistic_std = 0.02
shock_annual_prob = 0.05
shock_magnitude = {'positive': -0.03, 'negative': 0.03}
shock_targets = ['Amazon Rainforest', 'Congo Rainforest', 'Southeast Asian Rainforest', 'Coral Reefs', 'Atlantic Ocean', 'Pacific Ocean', 'Southern Ocean', 'Arctic Sea Ice']

# Define the loss function (renamed to reflect exponential form)
def exponential_loss(t, eco, scenario, include_cascades):
    time_span = t - 2025
    k = logistic_params[eco]['k'][scenario]
    if not include_cascades:
        L_max = original_consensus_loss[eco]['2175'] / 100.0
    else:
        L_max = min(1.0 - final_baselines[eco], adjusted_loss_potentials[eco]['2175'] / 100.0)
    raw_loss = L_max * (1 - np.exp(-k * time_span))
    return np.clip(raw_loss, 0, L_max)

def run_ecosystem_simulation(scenario, include_shocks=False, include_cascades=False, include_transfers=False, simulation_label=""):
    biodiversity_dict = {eco: np.zeros((n_iter, len(years))) for eco in ecosystems}
    loss_dict = {eco: np.zeros((n_iter, len(years))) for eco in ecosystems}
    transformed_biodiversity = {eco: np.zeros((n_iter, len(years))) for eco in ecosystems} if include_transfers else {}
    fully_transformed = {eco: np.zeros(n_iter, dtype=bool) for eco in ecosystems}
    shock_events = np.zeros((n_iter, len(years))) if not include_shocks else np.random.binomial(1, shock_annual_prob, size=(n_iter, len(years)))
    shock_types = np.full((n_iter, len(years)), 'none') if not include_shocks else np.random.choice(['positive', 'negative'], size=(n_iter, len(years)))
    shock_log = []
    debug_logs = []
    cascade_log = []
    transform_log = [] if include_transfers else []

    transfer_rate = 0.3  # 30% of lost area transferred per 5-year step; remaining 90% assumed degraded; conservative estimate based on slow transformation rates

    # Initialize biodiversity at t=0
    for eco in ecosystems:
        biodiversity_dict[eco][:, 0] = initial_biodiversity[eco]
        if include_transfers:
            transformed_biodiversity[eco][:, 0] = 0  # Initialize transformed biodiversity

    for t, year in enumerate(years):
        for eco in ecosystems:
            if not include_cascades:
                L_max = original_consensus_loss[eco]['2175'] / 100.0
            else:
                L_max = min(1.0 - final_baselines[eco], adjusted_loss_potentials[eco]['2175'] / 100.0)
            mean_loss = exponential_loss(year, eco, scenario, include_cascades)
            annual_variation = stats.norm(loc=0, scale=logistic_std).rvs(n_iter)
            adjusted_loss = mean_loss + annual_variation
            shock_adjust = 0
            if include_shocks and eco in shock_targets and year >= 2030:
                for i in range(n_iter):
                    if shock_events[i, t]:
                        shock_adjust = shock_magnitude[shock_types[i, t]]
                        shock_log.append({'iteration': i, 'year': year, 'type': shock_types[i, t], 'ecosystem': eco})
            adjusted_loss += shock_adjust
            loss_dict[eco][:, t] = np.clip(adjusted_loss, 0, 1.0)
            if not include_cascades:
                loss_dict[eco][:, t] = np.minimum(loss_dict[eco][:, t], original_consensus_loss[eco]['2175'] / 100.0)
            else:
                loss_dict[eco][:, t] = np.minimum(loss_dict[eco][:, t], adjusted_loss_potentials[eco]['2175'] / 100.0)
            fully_transformed[eco] = loss_dict[eco][:, t] >= L_max

            # Handle transfers: Add biodiversity to target and degrade transformed biodiversity
            if include_transfers and t > 0:
                target_eco = transform_targets[eco]
                if target_eco and not np.all(fully_transformed[eco]):
                    # Calculate transferred area from loss increment
                    current_loss = loss_dict[eco][:, t]
                    previous_loss = loss_dict[eco][:, t-1] if t > 1 else np.zeros(n_iter)
                    loss_increment = np.maximum(current_loss - previous_loss, 0)
                    source_area = ecosystem_areas[eco]
                    transferred_area = transfer_rate * loss_increment * source_area
                    target_density = biodiversity_density_ratios[target_eco]
                    biodiversity_increase = transferred_area * target_density

                    # Add to target's transformed biodiversity and total biodiversity
                    transformed_biodiversity[target_eco][:, t] = transformed_biodiversity[target_eco][:, t-1] + biodiversity_increase
                    transform_log.append(f"Year {year}, Source {eco}, Target {target_eco}, Transferred Area {np.mean(transferred_area):.4f}, Biodiversity Increase {np.mean(biodiversity_increase):.4f}")

                    # Degrade the target's transformed biodiversity based on target's loss rate
                    current_target_loss = loss_dict[target_eco][:, t]
                    previous_target_loss = loss_dict[target_eco][:, t-1] if t > 1 else np.zeros(n_iter)
                    degradation_rate = np.maximum(current_target_loss - previous_target_loss, 0) / (1 - previous_target_loss + 1e-10)
                    transformed_biodiversity[target_eco][:, t] -= transformed_biodiversity[target_eco][:, t] * degradation_rate
                    transformed_biodiversity[target_eco][:, t] = np.maximum(transformed_biodiversity[target_eco][:, t], 0)

        # Apply cascade effects
        if include_cascades:
            for eco in ecosystems:
                initial_loss = loss_dict[eco][:, t].copy()  # Store initial loss
                for source_eco, targets in cascade_effects.items():
                    if eco in targets and loss_dict[source_eco][:, t].mean() > 0.03:
                        for i in range(n_iter):
                            source_loss = loss_dict[source_eco][i, t]
                            multiplier = targets[eco]
                            if source_loss > 0:
                                new_loss = initial_loss[i] * multiplier
                                loss_dict[eco][i, t] = min(new_loss, adjusted_loss_potentials[eco]['2175'] / 100.0)
                                cascade_log.append(f"Year {year}, Target {eco}, Source {source_eco}, Multiplier {multiplier:.2f}, Loss {loss_dict[eco][i, t]:.2f}")
                # Apply auto-cascade for specific ecosystems with tipping points
                if eco == 'Amazon Rainforest' and initial_loss.mean() > 0.20:
                    for i in range(n_iter):
                        multiplier = cascade_effects[eco][eco]
                        new_loss = initial_loss[i] * multiplier
                        loss_dict[eco][i, t] = min(new_loss, adjusted_loss_potentials[eco]['2175'] / 100.0)
                        cascade_log.append(f"Year {year}, Target {eco}, Source {eco}, Multiplier {multiplier:.2f}, Loss {loss_dict[eco][i, t]:.2f}")
                elif eco == 'Congo Rainforest' and initial_loss.mean() > 0.20:
                    for i in range(n_iter):
                        multiplier = cascade_effects[eco][eco]
                        new_loss = initial_loss[i] * multiplier
                        loss_dict[eco][i, t] = min(new_loss, adjusted_loss_potentials[eco]['2175'] / 100.0)
                        cascade_log.append(f"Year {year}, Target {eco}, Source {eco}, Multiplier {multiplier:.2f}, Loss {loss_dict[eco][i, t]:.2f}")
                elif eco == 'Coral Reefs' and initial_loss.mean() > 0.50:
                    for i in range(n_iter):
                        multiplier = cascade_effects[eco][eco]
                        new_loss = initial_loss[i] * multiplier
                        loss_dict[eco][i, t] = min(new_loss, adjusted_loss_potentials[eco]['2175'] / 100.0)
                        cascade_log.append(f"Year {year}, Target {eco}, Source {eco}, Multiplier {multiplier:.2f}, Loss {loss_dict[eco][i, t]:.2f}")
                elif eco == 'Arctic Sea Ice' and initial_loss.mean() > 0.50:
                    for i in range(n_iter):
                        multiplier = cascade_effects[eco][eco]
                        new_loss = initial_loss[i] * multiplier
                        loss_dict[eco][i, t] = min(new_loss, adjusted_loss_potentials[eco]['2175'] / 100.0)
                        cascade_log.append(f"Year {year}, Target {eco}, Source {eco}, Multiplier {multiplier:.2f}, Loss {loss_dict[eco][i, t]:.2f}")
                elif eco == 'Boreal Forests' and initial_loss.mean() > 0.20:
                    for i in range(n_iter):
                        multiplier = cascade_effects[eco][eco]
                        new_loss = initial_loss[i] * multiplier
                        loss_dict[eco][i, t] = min(new_loss, adjusted_loss_potentials[eco]['2175'] / 100.0)
                        cascade_log.append(f"Year {year}, Target {eco}, Source {eco}, Multiplier {multiplier:.2f}, Loss {loss_dict[eco][i, t]:.2f}")
                    for eco in ecosystems:
                        for source_eco, targets in cascade_effects.items():
                            if eco in targets and loss_dict[source_eco][:, t].mean() > 0.03:
                                for i in range(n_iter):
                                    source_loss = loss_dict[source_eco][i, t]
                                    multiplier = targets[eco]
                                    if source_loss > 0:
                                        new_loss = loss_dict[eco][i, t] * multiplier
                                        loss_dict[eco][i, t] = min(new_loss, adjusted_loss_potentials[eco]['2175'] / 100.0)
                                        cascade_log.append(f"Year {year}, Target {eco}, Source {source_eco}, Multiplier {multiplier:.2f}, Loss {loss_dict[eco][i, t]:.2f}")
                        # Apply auto-cascade for specific ecosystems with tipping points
                        if eco == 'Amazon Rainforest' and loss_dict[eco][:, t].mean() > 0.20:
                            for i in range(n_iter):
                                multiplier = cascade_effects[eco][eco]
                                new_loss = loss_dict[eco][i, t] * multiplier
                                loss_dict[eco][i, t] = min(new_loss, adjusted_loss_potentials[eco]['2175'] / 100.0)
                                cascade_log.append(f"Year {year}, Target {eco}, Source {eco}, Multiplier {multiplier:.2f}, Loss {loss_dict[eco][i, t]:.2f}")
                        elif eco == 'Congo Rainforest' and loss_dict[eco][:, t].mean() > 0.20:
                            for i in range(n_iter):
                                multiplier = cascade_effects[eco][eco]
                                new_loss = loss_dict[eco][i, t] * multiplier
                                loss_dict[eco][i, t] = min(new_loss, adjusted_loss_potentials[eco]['2175'] / 100.0)
                                cascade_log.append(f"Year {year}, Target {eco}, Source {eco}, Multiplier {multiplier:.2f}, Loss {loss_dict[eco][i, t]:.2f}")
                        elif eco == 'Coral Reefs' and loss_dict[eco][:, t].mean() > 0.50:
                            for i in range(n_iter):
                                multiplier = cascade_effects[eco][eco]
                                new_loss = loss_dict[eco][i, t] * multiplier
                                loss_dict[eco][i, t] = min(new_loss, adjusted_loss_potentials[eco]['2175'] / 100.0)
                                cascade_log.append(f"Year {year}, Target {eco}, Source {eco}, Multiplier {multiplier:.2f}, Loss {loss_dict[eco][i, t]:.2f}")
                        elif eco == 'Arctic Sea Ice' and loss_dict[eco][:, t].mean() > 0.50:
                            for i in range(n_iter):
                                multiplier = cascade_effects[eco][eco]
                                new_loss = loss_dict[eco][i, t] * multiplier
                                loss_dict[eco][i, t] = min(new_loss, adjusted_loss_potentials[eco]['2175'] / 100.0)
                                cascade_log.append(f"Year {year}, Target {eco}, Source {eco}, Multiplier {multiplier:.2f}, Loss {loss_dict[eco][i, t]:.2f}")
                        elif eco == 'Boreal Forests' and loss_dict[eco][:, t].mean() > 0.20:
                            for i in range(n_iter):
                                multiplier = cascade_effects[eco][eco]
                                new_loss = loss_dict[eco][i, t] * multiplier
                                loss_dict[eco][i, t] = min(new_loss, adjusted_loss_potentials[eco]['2175'] / 100.0)
                                cascade_log.append(f"Year {year}, Target {eco}, Source {eco}, Multiplier {multiplier:.2f}, Loss {loss_dict[eco][i, t]:.2f}")
                            for eco in ecosystems:
                                for source_eco, targets in cascade_effects.items():
                                    if eco in targets and loss_dict[source_eco][:, t].mean() > 0.03:
                                        for i in range(n_iter):
                                            source_loss = loss_dict[source_eco][i, t]
                                            multiplier = targets[eco]
                                            if source_loss > 0:
                                                new_loss = loss_dict[eco][i, t] * multiplier
                                                loss_dict[eco][i, t] = min(new_loss, adjusted_loss_potentials[eco]['2175'] / 100.0)
                                                cascade_log.append(f"Year {year}, Target {eco}, Source {source_eco}, Multiplier {multiplier:.2f}, Loss {loss_dict[eco][i, t]:.2f}")
                                if eco == 'Amazon Rainforest' and loss_dict[eco][:, t].mean() > 0.20:
                                    for i in range(n_iter):
                                        multiplier = cascade_effects['Amazon Rainforest']['Amazon Rainforest']
                                        new_loss = loss_dict[eco][i, t] * multiplier
                                        loss_dict[eco][i, t] = min(new_loss, adjusted_loss_potentials[eco]['2175'] / 100.0)
                                        cascade_log.append(f"Year {year}, Target {eco}, Source {eco}, Multiplier {multiplier:.2f}, Loss {loss_dict[eco][i, t]:.2f}")

        # Ensure monotonic increase in loss
        if t > 0:
            for eco in ecosystems:
                loss_dict[eco][:, t] = np.maximum(loss_dict[eco][:, t], loss_dict[eco][:, t-1])

        # Update biodiversity once per time step, after all adjustments
        for eco in ecosystems:
            if t > 0:
                # Apply loss to the ecosystem's native biodiversity
                biodiversity_dict[eco][:, t] = biodiversity_dict[eco][:, t-1] * (1 - loss_dict[eco][:, t])
                # Add any transformed biodiversity (from transfers where eco is the target)
                if include_transfers:
                    biodiversity_dict[eco][:, t] += transformed_biodiversity[eco][:, t]
                # Ensure biodiversity doesn't go negative
                biodiversity_dict[eco][:, t] = np.maximum(biodiversity_dict[eco][:, t], 0)

    # Debug logging
    key_years = [2025, 2050, 2100, 2175]
    for year in key_years:
        t = np.where(years == year)[0][0]
        for eco in ecosystems:
            mean_loss = np.mean(loss_dict[eco][:, t]) * 100
            mean_biodiversity = np.mean(biodiversity_dict[eco][:, t])
            mean_transformed = np.mean(transformed_biodiversity[eco][:, t]) if include_transfers else 0
            debug_logs.append(f"{simulation_label} Year {year}, {eco}: Mean Loss = {mean_loss:.1f}%, Biodiversity = {mean_biodiversity:.4f}, Transformed Biodiversity = {mean_transformed:.4f}")

    if include_cascades:
        for log in cascade_log[:10]:
            print(log)
        with open('cascade_log.txt', 'w') as f:
            for log in cascade_log:
                f.write(log + '\n')
    if include_transfers:
        for log in transform_log[:10]:
            print(log)
        with open('transform_log.txt', 'w') as f:
            for log in transform_log:
                f.write(log + '\n')

    return biodiversity_dict, loss_dict, shock_log, debug_logs

# Run simulations
print("Running Baseline Simulation (Mid)...")
biodiversity_dict_baseline, loss_dict_baseline, shock_log_baseline, debug_logs_baseline = run_ecosystem_simulation('Mid', include_shocks=False, include_cascades=False, include_transfers=False, simulation_label="Baseline")
for log in debug_logs_baseline:
    print(log)

print("\nRunning Cascades-Only Simulation...")
biodiversity_dict_cascades, loss_dict_cascades, shock_log_cascades, debug_logs_cascades = run_ecosystem_simulation('Mid', include_shocks=False, include_cascades=True, include_transfers=False, simulation_label="Cascades-Only")
for log in debug_logs_cascades:
    print(log)

print("\nRunning Cascades+Transfers Simulation...")
biodiversity_dict_cascades_transfers, loss_dict_cascades_transfers, shock_log_cascades_transfers, debug_logs_cascades_transfers = run_ecosystem_simulation('Mid', include_shocks=False, include_cascades=True, include_transfers=True, simulation_label="Cascades+Transfers")
for log in debug_logs_cascades_transfers:
    print(log)

# Calculate mean biodiversity and losses
mean_biodiversity_baseline = {eco: np.mean(biodiversity_dict_baseline[eco], axis=0) for eco in ecosystems}
mean_biodiversity_cascades = {eco: np.mean(biodiversity_dict_cascades[eco], axis=0) for eco in ecosystems}
mean_biodiversity_cascades_transfers = {eco: np.mean(biodiversity_dict_cascades_transfers[eco], axis=0) for eco in ecosystems}
mean_losses_baseline = {eco: np.mean(loss_dict_baseline[eco], axis=0) * 100 for eco in ecosystems}
mean_losses_cascades = {eco: np.mean(loss_dict_cascades[eco], axis=0) * 100 for eco in ecosystems}
mean_losses_cascades_transfers = {eco: np.mean(loss_dict_cascades_transfers[eco], axis=0) * 100 for eco in ecosystems}

# Plotting (add summary plot)
consensus_years = [2025, 2050, 2100, 2175]
consensus_data = {eco: [0 if year == 2025 else original_consensus_loss[eco][str(year)] / 100.0 for year in consensus_years] for eco in ecosystems}

n_rows = 7
n_cols = 6
fig, axes = plt.subplots(n_rows, n_cols, figsize=(24, 28), sharex=True, sharey=True)
axes = axes.flatten()

for idx, eco in enumerate(ecosystems):
    ax = axes[idx]
    print(f"\nPlotting ecosystem: {eco} (Index {idx})")
    
    # Plot consensus loss percentages
    consensus_data_eco = [consensus_data[eco][t] * 100 for t in range(len(consensus_years))]
    ax.plot(consensus_years, consensus_data_eco, label='Consensus Loss (%)', color='black', linestyle='--')

    # Plot simulated loss for each scenario
    if eco in mean_losses_baseline:
        ax.plot(years, mean_losses_baseline[eco], label='Baseline Loss (%)', color='blue', linestyle='-.')
    if eco in mean_losses_cascades:
        ax.plot(years, mean_losses_cascades[eco], label='Cascades Loss (%)', color='green', linestyle='-.')
    if eco in mean_losses_cascades_transfers:
        ax.plot(years, mean_losses_cascades_transfers[eco], label='Cascades+Transfers Loss (%)', color='red', linestyle='-.')
    
    # Plot biodiversity for each scenario
    if eco in mean_biodiversity_baseline:
        ax.plot(years, mean_biodiversity_baseline[eco], label='Baseline Biodiversity', color='blue')
    if eco in mean_biodiversity_cascades:
        ax.plot(years, mean_biodiversity_cascades[eco], label='Cascades Biodiversity', color='green')
    if eco in mean_biodiversity_cascades_transfers:
        ax.plot(years, mean_biodiversity_cascades_transfers[eco], label='Cascades+Transfers Biodiversity', color='red')

    ax.set_title(eco)
    ax.set_xlabel('Year')
    ax.set_ylabel('Biodiversity (Relative Units) / Loss (%)')
    ax.set_ylim(0, max(max(initial_biodiversity.values()) * 1.2, 100))  # Adjust y-limit to accommodate loss percentages
    ax.grid(True)
    if idx == 0:
        ax.legend()

for idx in range(len(ecosystems), len(axes)):
    fig.delaxes(axes[idx])

# Add summary plot for loss comparison
fig_summary, ax_summary = plt.subplots(figsize=(10, 6))
for eco in ecosystems:
    consensus_data_eco = [consensus_data[eco][t] * 100 for t in range(len(consensus_years))]
    ax_summary.plot(consensus_years, consensus_data_eco, label=f'Consensus {eco}', color='gray', alpha=0.3, linestyle='--')
    if eco in mean_losses_cascades_transfers:
        ax_summary.plot(years, mean_losses_cascades_transfers[eco], label=f'Simulated {eco}', alpha=0.5)
ax_summary.set_title('Simulated vs Consensus Loss Across Ecosystems')
ax_summary.set_xlabel('Year')
ax_summary.set_ylabel('Loss (%)')
ax_summary.set_ylim(0, 100)
ax_summary.grid(True)
ax_summary.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('loss_comparison_summary.png')

plt.tight_layout()
plt.savefig('biodiversity_and_loss_trajectories_by_ecosystem.png')
plt.show()