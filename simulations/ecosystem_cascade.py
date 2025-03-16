import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
FIGURES_DIR = os.path.join(BASE_DIR, 'figures')

np.random.seed(42)
n_iter = 50000
years = np.arange(2025, 2176, 1)
ecosystems = ['Amazon Rainforest', 'Coral Reefs', 'Arctic Sea Ice', 'Boreal Forests',
              'Savanna Grasslands', 'Wetlands', 'Oceans', 'Temperate Forests',
              'Deserts', 'Tundra', 'Montane', 'Freshwater', 'Polar']

base_loss_means = {
    'Amazon Rainforest': {'Low': 0.003, 'Mid': 0.005, 'High': 0.005},
    'Coral Reefs': {'Low': 0.006, 'Mid': 0.008, 'High': 0.015},
    'Arctic Sea Ice': {'Low': 0.004, 'Mid': 0.008, 'High': 0.04},
    'Boreal Forests': {'Low': 0.002, 'Mid': 0.004, 'High': 0.006},
    'Savanna Grasslands': {'Low': 0.002, 'Mid': 0.004, 'High': 0.005},
    'Wetlands': {'Low': 0.002, 'Mid': 0.005, 'High': 0.007},
    'Oceans': {'Low': 0.003, 'Mid': 0.006, 'High': 0.009},
    'Temperate Forests': {'Low': 0.001, 'Mid': 0.003, 'High': 0.005},
    'Deserts': {'Low': 0.001, 'Mid': 0.003, 'High': 0.005},
    'Tundra': {'Low': 0.002, 'Mid': 0.004, 'High': 0.007},
    'Montane': {'Low': 0.002, 'Mid': 0.004, 'High': 0.006},
    'Freshwater': {'Low': 0.003, 'Mid': 0.006, 'High': 0.009},
    'Polar': {'Low': 0.001, 'Mid': 0.003, 'High': 0.005}
}
base_loss_std = 0.001

cascade_effects = {
    'Amazon Rainforest': {'Arctic Sea Ice': 1.05, 'Coral Reefs': 1.05, 'Wetlands': 1.05},
    'Coral Reefs': {'Wetlands': 1.2, 'Savanna Grasslands': 1.05, 'Oceans': 1.1},
    'Arctic Sea Ice': {'Amazon Rainforest': 1.05, 'Boreal Forests': 1.2, 'Oceans': 1.1},
    'Boreal Forests': {'Arctic Sea Ice': 1.1, 'Wetlands': 1.1, 'Temperate Forests': 1.1},
    'Savanna Grasslands': {'Wetlands': 1.05},
    'Wetlands': {'Savanna Grasslands': 1.05, 'Temperate Forests': 1.1},
    'Oceans': {'Coral Reefs': 1.1, 'Arctic Sea Ice': 1.1},
    'Temperate Forests': {'Boreal Forests': 1.1, 'Wetlands': 1.1},
    'Deserts': {'Savanna Grasslands': 1.05},
    'Tundra': {'Arctic Sea Ice': 1.1, 'Boreal Forests': 1.1},
    'Montane': {'Temperate Forests': 1.1},
    'Freshwater': {'Wetlands': 1.2, 'Oceans': 1.1},
    'Polar': {'Arctic Sea Ice': 1.1}
}

shock_annual_prob = 0.02
shock_magnitude = {'positive': -0.05, 'negative': 0.05}
shock_targets = ecosystems

transform_targets = {
    'Amazon Rainforest': 'Savanna Grasslands', 'Coral Reefs': 'Oceans',
    'Arctic Sea Ice': 'Oceans', 'Boreal Forests': 'Savanna Grasslands',
    'Savanna Grasslands': None, 'Wetlands': 'Savanna Grasslands',
    'Oceans': None, 'Temperate Forests': 'Savanna Grasslands',
    'Deserts': None, 'Tundra': 'Savanna Grasslands',
    'Montane': 'Savanna Grasslands', 'Freshwater': 'Wetlands', 'Polar': 'Oceans'
}
final_baselines = {
    'Amazon Rainforest': 0.05, 'Coral Reefs': 0.01, 'Arctic Sea Ice': 0.20,
    'Boreal Forests': 0.05, 'Savanna Grasslands': 0.40, 'Wetlands': 0.05,
    'Oceans': 0.15, 'Temperate Forests': 0.30, 'Deserts': 0.80,
    'Tundra': 0.30, 'Montane': 0.40, 'Freshwater': 0.20, 'Polar': 0.40
}
species_weights = {
    'Amazon Rainforest': 0.25, 'Coral Reefs': 0.15, 'Arctic Sea Ice': 0.0075,
    'Boreal Forests': 0.065, 'Savanna Grasslands': 0.06, 'Wetlands': 0.08,
    'Oceans': 0.20, 'Temperate Forests': 0.10, 'Deserts': 0.05, 'Tundra': 0.02,
    'Montane': 0.08, 'Freshwater': 0.10, 'Polar': 0.01
}

biodiversity_density_ratios = {
    'Amazon Rainforest': 1.0, 'Savanna Grasslands': 0.128, 'Coral Reefs': 0.5,
    'Arctic Sea Ice': 0.05, 'Boreal Forests': 0.3, 'Wetlands': 0.4,
    'Oceans': 0.2, 'Temperate Forests': 0.25, 'Deserts': 0.02,
    'Tundra': 0.05, 'Montane': 0.3, 'Freshwater': 0.35, 'Polar': 0.03
}

def run_ecosystem_simulation(scenario, include_shocks=False):
    loss_dict = {eco: np.zeros((n_iter, len(years))) for eco in ecosystems}
    transformed_fraction = {eco: np.zeros((n_iter, len(years))) for eco in ecosystems}
    # Track when each ecosystem is fully transformed (per iteration)
    fully_transformed = {eco: np.zeros(n_iter, dtype=bool) for eco in ecosystems}
    shock_events = np.random.binomial(1, shock_annual_prob, size=(n_iter, len(years))) if include_shocks else np.zeros((n_iter, len(years)))
    shock_types = np.random.choice(['positive', 'negative'], size=(n_iter, len(years))) if include_shocks else np.full((n_iter, len(years)), 'none')
    shock_log = []
    debug_logs = []

    for t, year in enumerate(years):
        for eco in ecosystems:
            mean_loss = base_loss_means[eco][scenario]
            shock_adjust = 0
            if include_shocks and eco in shock_targets:
                shock_magnitude_adjusted = shock_magnitude.copy()
                if eco in ['Coral Reefs', 'Arctic Sea Ice']:
                    shock_magnitude_adjusted = {'positive': -0.15, 'negative': 0.15}
                shock_adjust = np.where(shock_events[:, t],
                                      np.where(shock_types[:, t] == 'positive', shock_magnitude_adjusted['positive'],
                                               shock_magnitude_adjusted['negative']),
                                      0)
            adjusted_mean_loss = mean_loss + shock_adjust
            annual_loss = stats.t(df=3, loc=adjusted_mean_loss, scale=base_loss_std).rvs(n_iter)
            annual_loss = np.maximum(0, annual_loss)

            if t > 0:
                loss_dict[eco][:, t] = loss_dict[eco][:, t-1] + annual_loss
            else:
                loss_dict[eco][:, t] = annual_loss

            max_loss = 1.0 - final_baselines[eco]
            loss_dict[eco][:, t] = np.minimum(loss_dict[eco][:, t], max_loss)

            # Update fully transformed status (per iteration)
            fully_transformed[eco] = loss_dict[eco][:, t] >= max_loss

            target_eco = transform_targets[eco]
            if target_eco and not np.all(fully_transformed[eco]):
                # Only apply transformation if the ecosystem is not fully transformed
                transformed_fraction[eco][:, t] = loss_dict[eco][:, t]
                transformed_amount = transformed_fraction[eco][:, t] * (1.0 - final_baselines[eco])
                bio_density_ratio = biodiversity_density_ratios[target_eco] / biodiversity_density_ratios[eco]
                scaled_transformed_amount = transformed_amount * bio_density_ratio
                # Apply offset only to iterations where eco is not fully transformed
                mask = ~fully_transformed[eco]
                loss_dict[target_eco][mask, t] -= scaled_transformed_amount[mask]
                loss_dict[target_eco][:, t] = np.clip(loss_dict[target_eco][:, t], 0, 1)

        for eco in ecosystems:
            for source_eco, targets in cascade_effects.items():
                if eco in targets:
                    for i in range(n_iter):
                        source_loss = loss_dict[source_eco][i, t]
                        multiplier = targets[eco]
                        if source_loss > 0:
                            loss_dict[eco][i, t] *= multiplier

            max_loss = 1.0 - final_baselines[eco]
            loss_dict[eco][:, t] = np.minimum(loss_dict[eco][:, t], max_loss)

        if include_shocks and eco in shock_targets:
            for i in range(n_iter):
                if shock_events[i, t]:
                    shock_log.append({'iteration': i, 'year': year, 'type': shock_types[i, t], 'ecosystem': eco})

    key_years = [2025, 2050, 2100, 2175]
    for year in key_years:
        t = np.where(years == year)[0][0]
        for eco in ['Coral Reefs', 'Arctic Sea Ice', 'Amazon Rainforest', 'Savanna Grasslands']:
            mean_loss = np.mean(loss_dict[eco][:, t]) * 100
            debug_logs.append(f"Year {year}, {eco}: Mean Loss = {mean_loss:.1f}%")

    for log in debug_logs:
        print(log)

    return loss_dict, shock_log

# Run simulations
results_no_shock = {scenario: run_ecosystem_simulation(scenario, include_shocks=False)[0] for scenario in ['Low', 'Mid', 'High']}
results_with_shock, shock_logs = {}, {}
for scenario in ['Low', 'Mid', 'High']:
    results_with_shock[scenario], shock_logs[scenario] = run_ecosystem_simulation(scenario, include_shocks=True)

# Calculate total loss
total_loss_no_shock = {scenario: np.zeros((n_iter, len(years))) for scenario in ['Low', 'Mid', 'High']}
total_loss_with_shock = {scenario: np.zeros((n_iter, len(years))) for scenario in ['Low', 'Mid', 'High']}

for scenario in results_no_shock:
    for t in range(len(years)):
        total_loss_no_shock[scenario][:, t] = np.minimum(1.0, sum(results_no_shock[scenario][eco][:, t] * species_weights[eco]
                                                 for eco in ecosystems))
        total_loss_with_shock[scenario][:, t] = np.minimum(1.0, sum(results_with_shock[scenario][eco][:, t] * species_weights[eco]
                                                   for eco in ecosystems))

# Print results
for scenario in ['Low', 'Mid', 'High']:
    print(f"\n--- {scenario.upper()} SCENARIO (NO SHOCKS) ---")
    total_mean_2175 = np.mean(total_loss_no_shock[scenario][:, -1]) * 100
    total_ci_2175 = np.percentile(total_loss_no_shock[scenario][:, -1], [2.5, 97.5]) * 100
    print(f"Total Loss 2175: {total_mean_2175:.1f}%, 95% CI = {total_ci_2175[0]:.1f}–{total_ci_2175[1]:.1f}%")
    mean_2125 = np.mean(total_loss_no_shock[scenario][:, 100]) * 100
    print(f"Total Loss 2125: {mean_2125:.1f}%")
    if mean_2125 > 50:
        print(f"WARNING: {mean_2125:.1f}% loss by 2125 exceeds 50% - food/health risks.")
    if total_mean_2175 > 70:
        print(f"WARNING: {total_mean_2175:.1f}% loss by 2175 exceeds 70% - survival threat.")

    print(f"\n--- {scenario.upper()} SCENARIO (WITH SHOCKS) ---")
    total_mean_2175 = np.mean(total_loss_with_shock[scenario][:, -1]) * 100
    total_ci_2175 = np.percentile(total_loss_with_shock[scenario][:, -1], [2.5, 97.5]) * 100
    print(f"Total Loss 2175: {total_mean_2175:.1f}%, 95% CI = {total_ci_2175[0]:.1f}–{total_ci_2175[1]:.1f}%")
    mean_2125 = np.mean(total_loss_with_shock[scenario][:, 100]) * 100
    print(f"Total Loss 2125: {mean_2125:.1f}%")
    if mean_2125 > 50:
        print(f"WARNING: {mean_2125:.1f}% loss by 2125 exceeds 50% - food/health risks.")
    if total_mean_2175 > 70:
        print(f"WARNING: {total_mean_2175:.1f}% loss by 2175 exceeds 70% - survival threat.")

# --- Plot 1: Total Biodiversity Loss by Scenario with Shock vs. No-Shock and 95% CI ---
plt.figure(figsize=(12, 8))
sns.set(style="whitegrid")

color_map = {'Low': 'green', 'Mid': 'orange', 'High': 'red'}

for scenario in ['Low', 'Mid', 'High']:
    total_loss_mean_no = np.mean(total_loss_no_shock[scenario], axis=0) * 100
    total_loss_ci_no = np.percentile(total_loss_no_shock[scenario], [2.5, 97.5], axis=0) * 100
    plt.plot(years, total_loss_mean_no, label=f'{scenario} (No Shock)', linestyle='--', color=color_map[scenario], linewidth=2)
    plt.fill_between(years, total_loss_ci_no[0], total_loss_ci_no[1], color=color_map[scenario], alpha=0.2)

    total_loss_mean = np.mean(total_loss_with_shock[scenario], axis=0) * 100
    total_loss_ci = np.percentile(total_loss_with_shock[scenario], [2.5, 97.5], axis=0) * 100
    plt.plot(years, total_loss_mean, label=f'{scenario} (With Shock)', linestyle='-', color=color_map[scenario], linewidth=2)
    plt.fill_between(years, total_loss_ci[0], total_loss_ci[1], color=color_map[scenario], alpha=0.2)

plt.axhline(y=50, color='yellow', linestyle='--', label='50% Threshold (Food/Health Risks)')
plt.axhline(y=70, color='purple', linestyle='--', label='70% Threshold (Survival Threat)')
plt.title('Total Biodiversity Loss by Scenario: Shock vs. No-Shock with 95% CI (2025–2175)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('% Total Biodiversity Loss', fontsize=12)
plt.legend(title='Scenario', fontsize=10, loc='upper left')
os.makedirs(FIGURES_DIR, exist_ok=True)
plt.savefig(os.path.join(FIGURES_DIR, 'total_biodiversity_loss_with_shocks.png'), dpi=300, bbox_inches='tight')
plt.close()

# --- Plot 2: Ecosystem Breakdown with Transformation Flags (High With-Shocks, 2175) ---
plt.figure(figsize=(14, 8))
sns.set(style="whitegrid")

scenario = 'High'
year_idx = -1
mean_losses = np.zeros(len(ecosystems))
ci_low = np.zeros(len(ecosystems))
ci_high = np.zeros(len(ecosystems))

for eco_idx, eco in enumerate(ecosystems):
    losses = results_with_shock[scenario][eco][:, year_idx] * 100
    mean_losses[eco_idx] = np.mean(losses)
    ci_low[eco_idx], ci_high[eco_idx] = np.percentile(losses, [2.5, 97.5])
    ci_low[eco_idx] = max(0, ci_low[eco_idx])
    ci_high[eco_idx] = max(mean_losses[eco_idx], ci_high[eco_idx])

transformed = np.zeros(len(ecosystems), dtype=bool)
for eco_idx, eco in enumerate(ecosystems):
    transformed[eco_idx] = results_with_shock[scenario][eco][:, year_idx].mean() > 0

lower_errors = mean_losses - ci_low
lower_errors = np.maximum(0, lower_errors)
upper_errors = ci_high - mean_losses
upper_errors = np.maximum(0, upper_errors)
errors = np.array([lower_errors, upper_errors])

bars = plt.bar(ecosystems, mean_losses, yerr=errors, capsize=5, color='skyblue', edgecolor='black')
for bar, is_transformed in zip(bars, transformed):
    if is_transformed:
        bar.set_hatch('//')

plt.axhline(y=50, color='yellow', linestyle='--', label='50% Threshold')
plt.axhline(y=90, color='purple', linestyle='--', label='90% Near-Collapse')
plt.title('Ecosystem Loss in High Scenario with Shocks (2175)', fontsize=16)
plt.xlabel('Ecosystem', fontsize=12)
plt.ylabel('% Loss of Ecosystem Function', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.legend(fontsize=10)
plt.tight_layout()
plt.savefig(os.path.join(FIGURES_DIR, 'ecosystem_breakdown_2175_high_shock.png'), dpi=300, bbox_inches='tight')
plt.close()

# --- Plot 3: Shock Impact with Weighted Total Loss (Sample Runs, High With-Shocks) ---
plt.figure(figsize=(14, 8))
sns.set(style="whitegrid")

sample_runs = 5
scenario = 'High'
run_ids = np.random.choice(n_iter, sample_runs, replace=False)

for run_id in run_ids:
    weighted_loss = total_loss_with_shock[scenario][run_id] * 100
    plt.plot(years, weighted_loss, label=f'Run {run_id}', alpha=0.7, linewidth=1.5)

    shock_df = pd.DataFrame(shock_logs[scenario])
    if not shock_df.empty and 'iteration' in shock_df.columns:
        run_shocks = shock_df[shock_df['iteration'] == run_id]
        for _, shock in run_shocks.iterrows():
            color = 'green' if shock['type'] == 'positive' else 'purple'
            plt.axvline(x=shock['year'], color=color, linestyle='--', alpha=0.5)

plt.axhline(y=50, color='yellow', linestyle='--', label='50% Threshold')
plt.axhline(y=70, color='purple', linestyle='--', label='70% Threshold')
plt.title('Shock Impacts on Weighted Total Loss (High Scenario, Sample Runs)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('% Total Biodiversity Loss (Weighted)', fontsize=12)
plt.legend(title='Sample Runs', fontsize=10, loc='upper left')
plt.savefig(os.path.join(FIGURES_DIR, 'shock_impact_sample_runs_weighted.png'), dpi=300, bbox_inches='tight')
plt.close()

# --- Plot 4: Ecosystem-Specific Loss Trajectories in 4x4 Grid ---
plt.figure(figsize=(20, 20))
sns.set(style="whitegrid")

# Define colors and linestyles
color_map = {'Low': 'green', 'Mid': 'orange', 'High': 'red'}
linestyles = {'No Shock': '--', 'With Shock': '-'}

# 4x4 grid (16 subplots)
for idx, eco in enumerate(ecosystems + [None] * 3):  # Pad with None for 16 slots
    row = idx // 4
    col = idx % 4
    plt.subplot(4, 4, idx + 1)
    
    if eco is None:
        plt.axis('off')  # Skip empty subplots
        continue
    
    # Plot for each scenario
    for scenario in ['Low', 'Mid', 'High']:
        # No Shock
        mean_loss_no = np.mean(results_no_shock[scenario][eco], axis=0) * 100
        ci_no = np.percentile(results_no_shock[scenario][eco], [2.5, 97.5], axis=0) * 100
        plt.plot(years, mean_loss_no, label=f'{scenario} (No Shock)', linestyle=linestyles['No Shock'],
                 color=color_map[scenario], linewidth=2, alpha=0.7)
        plt.fill_between(years, ci_no[0], ci_no[1], color=color_map[scenario], alpha=0.2)
        
        # With Shock
        mean_loss_with = np.mean(results_with_shock[scenario][eco], axis=0) * 100
        ci_with = np.percentile(results_with_shock[scenario][eco], [2.5, 97.5], axis=0) * 100
        plt.plot(years, mean_loss_with, label=f'{scenario} (With Shock)', linestyle=linestyles['With Shock'],
                 color=color_map[scenario], linewidth=2, alpha=0.7)
        plt.fill_between(years, ci_with[0], ci_with[1], color=color_map[scenario], alpha=0.2)

    # Threshold lines
    plt.axhline(y=50, color='yellow', linestyle='--', label='50% Threshold', alpha=0.5)
    plt.axhline(y=90, color='purple', linestyle='--', label='90% Near-Collapse', alpha=0.5)

    # Customize each subplot
    plt.title(f'{eco} Loss', fontsize=10)
    plt.xlabel('Year', fontsize=8)
    plt.ylabel('% Loss', fontsize=8)
    plt.ylim(0, 100)
    plt.grid(True, alpha=0.3)
    if col == 0:
        plt.ylabel('% Loss of Ecosystem Function', fontsize=8)
    if row == 3:
        plt.xlabel('Year', fontsize=8)
    if idx == 0:  # Only show legend on first plot to avoid clutter
        plt.legend(title='Scenario', fontsize=6, loc='upper left', bbox_to_anchor=(1.05, 1), borderaxespad=0.)

plt.suptitle('Ecosystem-Specific Loss Trajectories (2025–2175)', fontsize=16)
plt.tight_layout(rect=[0, 0, 0.9, 0.95])  # Adjust layout to accommodate legend
os.makedirs(FIGURES_DIR, exist_ok=True)
plt.savefig(os.path.join(FIGURES_DIR, 'ecosystem_specific_loss_trajectories.png'), dpi=300, bbox_inches='tight')
plt.close()

# Save ecosystem-level results
all_data_no_shock = []
all_data_with_shock = []
for scenario in ['Low', 'Mid', 'High']:
    for eco in ecosystems:
        loss_flat_no_shock = results_no_shock[scenario][eco].ravel()
        loss_flat_with_shock = results_with_shock[scenario][eco].ravel()
        all_data_no_shock.append(pd.DataFrame({
            'Ecosystem': eco,
            'Scenario': scenario,
            'Loss': loss_flat_no_shock,
            'Year': np.tile(years, n_iter)
        }))
        all_data_with_shock.append(pd.DataFrame({
            'Ecosystem': eco,
            'Scenario': scenario,
            'Loss': loss_flat_with_shock,
            'Year': np.tile(years, n_iter)
        }))

results_df_no_shock = pd.concat(all_data_no_shock, ignore_index=True)
results_df_with_shock = pd.concat(all_data_with_shock, ignore_index=True)

os.makedirs(DATA_DIR, exist_ok=True)
results_df_no_shock.to_csv(os.path.join(DATA_DIR, 'ecosystem_cascade_results_no_shock.csv'), index=False)
results_df_with_shock.to_csv(os.path.join(DATA_DIR, 'ecosystem_cascade_results_with_shock.csv'), index=False)

for scenario in ['Low', 'Mid', 'High']:
    shock_df = pd.DataFrame(shock_logs[scenario])
    shock_df.to_csv(os.path.join(DATA_DIR, f'shock_log_{scenario.lower()}.csv'), index=False)

print(f"Results saved to '{os.path.join(DATA_DIR, 'ecosystem_cascade_results_no_shock.csv')}' and '{os.path.join(DATA_DIR, 'ecosystem_cascade_results_with_shock.csv')}'")
print(f"Shock logs saved to '{os.path.join(DATA_DIR, 'shock_log_high.csv')}' (and Low/Mid)")
print(f"Plots saved to '{FIGURES_DIR}'")