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
    'Amazon Rainforest': {'Low': 0.003, 'Mid': 0.006, 'High': 0.009},
    'Coral Reefs': {'Low': 0.004, 'Mid': 0.008, 'High': 0.012},
    'Arctic Sea Ice': {'Low': 0.003, 'Mid': 0.006, 'High': 0.009},
    'Boreal Forests': {'Low': 0.002, 'Mid': 0.004, 'High': 0.006},
    'Savanna Grasslands': {'Low': 0.002, 'Mid': 0.004, 'High': 0.006},
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
    'Amazon Rainforest': {'Arctic Sea Ice': 1.2, 'Coral Reefs': 1.1, 'Wetlands': 1.1},
    'Coral Reefs': {'Wetlands': 1.2, 'Savanna Grasslands': 1.1, 'Oceans': 1.1},
    'Arctic Sea Ice': {'Amazon Rainforest': 1.1, 'Boreal Forests': 1.2, 'Oceans': 1.1},
    'Boreal Forests': {'Arctic Sea Ice': 1.1, 'Wetlands': 1.1, 'Temperate Forests': 1.1},
    'Savanna Grasslands': {'Wetlands': 1.1},
    'Wetlands': {'Savanna Grasslands': 1.1, 'Temperate Forests': 1.1},
    'Oceans': {'Coral Reefs': 1.1, 'Arctic Sea Ice': 1.1},
    'Temperate Forests': {'Boreal Forests': 1.1, 'Wetlands': 1.1},
    'Deserts': {'Savanna Grasslands': 1.1},
    'Tundra': {'Arctic Sea Ice': 1.1, 'Boreal Forests': 1.1},
    'Montane': {'Temperate Forests': 1.1},
    'Freshwater': {'Wetlands': 1.2, 'Oceans': 1.1},
    'Polar': {'Arctic Sea Ice': 1.1}
}

# Boosted shock parameters
shock_annual_prob = 0.03  # 4-5 shocks per run
shock_magnitude = {'positive': -0.1, 'negative': 0.1}  # ±10% loss rate adjustment
shock_targets = ecosystems  # Shocks hit all

transform_threshold = stats.beta(a=2, b=5).rvs()  # 0-1 scale
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
    'Amazon Rainforest': 0.125, 'Coral Reefs': 0.07, 'Arctic Sea Ice': 0.0075,
    'Boreal Forests': 0.065, 'Savanna Grasslands': 0.06, 'Wetlands': 0.08,
    'Oceans': 0.20, 'Temperate Forests': 0.10, 'Deserts': 0.05, 'Tundra': 0.02,
    'Montane': 0.08, 'Freshwater': 0.10, 'Polar': 0.01
}

def run_ecosystem_simulation(scenario, include_shocks=False):
    loss_dict = {eco: np.zeros((n_iter, len(years))) for eco in ecosystems}
    transformed = {eco: np.zeros(n_iter, dtype=bool) for eco in ecosystems}
    shock_events = np.random.binomial(1, shock_annual_prob, size=(n_iter, len(years))) if include_shocks else np.zeros((n_iter, len(years)))
    shock_types = np.random.choice(['positive', 'negative'], size=(n_iter, len(years))) if include_shocks else np.full((n_iter, len(years)), 'none')
    shock_log = []

    for t, year in enumerate(years):
        for eco in ecosystems:
            if t > 0:
                transformed[eco] = loss_dict[eco][:, t-1] >= transform_threshold
            target_eco = transform_targets[eco]
            mean_loss = (base_loss_means[eco][scenario] if not np.any(transformed[eco])
                         else (base_loss_means[target_eco][scenario] if target_eco else base_loss_means[eco][scenario]))
            
            # Apply boosted shocks to target ecosystems
            shock_adjust = 0
            if include_shocks and eco in shock_targets:
                shock_adjust = np.where(shock_events[:, t], 
                                      np.where(shock_types[:, t] == 'positive', shock_magnitude['positive'], shock_magnitude['negative']), 
                                      0)
            adjusted_mean_loss = np.clip(mean_loss + shock_adjust, 0, 0.15)
            
            annual_loss = stats.t(df=3, loc=adjusted_mean_loss, scale=base_loss_std).rvs(n_iter)
            if t > 0:
                transformed[eco] = loss_dict[eco][:, t-1] >= transform_threshold
                loss_dict[eco][:, t] = np.where(transformed[eco],
                                               np.maximum(loss_dict[eco][:, t-1], loss_dict[eco][:, t-1] + annual_loss),
                                               loss_dict[eco][:, t-1] + annual_loss)
            else:
                loss_dict[eco][:, t] = annual_loss
            
            # Cap before cascades
            max_loss = 1.0 - final_baselines[eco]
            loss_dict[eco][:, t] = np.minimum(loss_dict[eco][:, t], max_loss)
            
            # Apply cascades
            for source_eco, targets in cascade_effects.items():
                if eco in targets:
                    source_mean = np.mean(loss_dict[source_eco][:, t])
                    multiplier = targets[eco]
                    if transformed[source_eco].any() and source_mean > transform_threshold:
                        multiplier *= 0.8
                    if source_mean > transform_threshold:
                        loss_dict[eco][:, t] *= multiplier
            
            # Reapply cap after cascades
            loss_dict[eco][:, t] = np.minimum(loss_dict[eco][:, t], max_loss)
            
            # Log shocks for target ecosystems
            if include_shocks and eco in shock_targets:
                for i in range(n_iter):
                    if shock_events[i, t]:
                        shock_log.append({'iteration': i, 'year': year, 'type': shock_types[i, t], 'ecosystem': eco})
    
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
    
    
# Plot total loss with shocks
plt.figure(figsize=(12, 8))
sns.set(style="whitegrid")

# Define color mapping for scenarios
color_map = {
    'Low': 'green',
    'Mid': 'orange',
    'High': 'red'
}

for scenario in ['Low', 'Mid', 'High']:
    # Plot no-shocks (dashed lines)
    total_loss_mean_no = np.mean(total_loss_no_shock[scenario], axis=0) * 100
    plt.plot(years, total_loss_mean_no, label=f'{scenario} (No Shocks)', linestyle='--', color=color_map[scenario])
    
    # Plot with-shocks (solid lines)
    total_loss_mean = np.mean(total_loss_with_shock[scenario], axis=0) * 100
    plt.plot(years, total_loss_mean, label=f'{scenario} Scenario (w/ Shocks)', linewidth=2, color=color_map[scenario])

plt.axhline(y=50, color='yellow', linestyle='--', label='50% Threshold (Food/Health Risks)')
plt.axhline(y=70, color='red', linestyle='--', label='70% Threshold (Survival Threat)')
plt.title('Total Biodiversity Loss with Boosted Shocks (2025–2175, No Intervention)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('% Total Biodiversity Loss', fontsize=12)
plt.legend(title='Scenario', fontsize=10)
os.makedirs(FIGURES_DIR, exist_ok=True)
plt.savefig(os.path.join(FIGURES_DIR, 'total_biodiversity_loss_with_shocks.png'), dpi=300, bbox_inches='tight')
plt.close()

# Save results
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

# Save shock logs
for scenario in ['Low', 'Mid', 'High']:
    shock_df = pd.DataFrame(shock_logs[scenario])
    shock_df.to_csv(os.path.join(DATA_DIR, f'shock_log_{scenario.lower()}.csv'), index=False)

print(f"Results saved to '{os.path.join(DATA_DIR, 'ecosystem_cascade_results_no_shock.csv')}' and '{os.path.join(DATA_DIR, 'ecosystem_cascade_results_with_shock.csv')}'")
print(f"Shock logs saved to '{os.path.join(DATA_DIR, 'shock_log_high.csv')}' (and Low/Mid)")