import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure correct file paths from repo root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
FIGURES_DIR = os.path.join(BASE_DIR, 'figures')

np.random.seed(42)
n_iter = 100000
years = np.arange(2025, 2176, 10)
ecosystems = ['Amazon Rainforest', 'Coral Reefs', 'Arctic Sea Ice', 
              'Boreal Forests', 'Savanna Grasslands', 'Wetlands', 
              'Oceans', 'Temperate Forests']

base_loss_means = {
    'Amazon Rainforest': {'Low': 0.03, 'Mid': 0.06, 'High': 0.09},
    'Coral Reefs': {'Low': 0.04, 'Mid': 0.08, 'High': 0.12},
    'Arctic Sea Ice': {'Low': 0.03, 'Mid': 0.06, 'High': 0.09},
    'Boreal Forests': {'Low': 0.02, 'Mid': 0.04, 'High': 0.06},
    'Savanna Grasslands': {'Low': 0.02, 'Mid': 0.04, 'High': 0.06},
    'Wetlands': {'Low': 0.02, 'Mid': 0.05, 'High': 0.07},
    'Oceans': {'Low': 0.03, 'Mid': 0.06, 'High': 0.09},
    'Temperate Forests': {'Low': 0.01, 'Mid': 0.03, 'High': 0.05}
}
base_loss_std = 0.01

cascade_effects = {
    'Amazon Rainforest': {'Arctic Sea Ice': 1.2, 'Coral Reefs': 1.1, 'Wetlands': 1.1},
    'Coral Reefs': {'Wetlands': 1.2, 'Savanna Grasslands': 1.1, 'Oceans': 1.1},
    'Arctic Sea Ice': {'Amazon Rainforest': 1.1, 'Boreal Forests': 1.2, 'Coral Reefs': 1.1, 'Oceans': 1.1},
    'Boreal Forests': {'Arctic Sea Ice': 1.1, 'Wetlands': 1.1, 'Temperate Forests': 1.1},
    'Savanna Grasslands': {'Wetlands': 1.1},
    'Wetlands': {'Savanna Grasslands': 1.1, 'Temperate Forests': 1.1},
    'Oceans': {'Coral Reefs': 1.2, 'Arctic Sea Ice': 1.1},
    'Temperate Forests': {'Boreal Forests': 1.1, 'Wetlands': 1.1}
}

nuclear_annual_risk = 0.01
nuclear_years = 150
nuclear_prob = 1 - np.exp(-nuclear_annual_risk * nuclear_years)
nuclear_occurs = np.random.binomial(1, nuclear_prob, n_iter)
nuclear_loss = 0.25

def run_ecosystem_simulation(scenario):
    loss_dict = {eco: np.zeros((n_iter, len(years))) for eco in ecosystems}
    for t, year in enumerate(years):
        for eco in ecosystems:
            mean_loss = base_loss_means[eco][scenario]
            annual_loss = stats.norm(loc=mean_loss, scale=base_loss_std).rvs(n_iter)
            loss_dict[eco][:, t] = loss_dict[eco][:, t-1] + annual_loss if t > 0 else annual_loss
            if t > 0 and np.any(nuclear_occurs):
                nuclear_effect = nuclear_occurs * nuclear_loss * (t / len(years))
                loss_dict[eco][:, t] += nuclear_effect
            for source_eco, targets in cascade_effects.items():
                if source_eco != eco and eco in targets and np.mean(loss_dict[source_eco][:, t]) > 0.5:
                    loss_dict[eco][:, t] *= targets[eco]
            loss_dict[eco][:, t] = np.minimum(loss_dict[eco][:, t], 1.0)
    return loss_dict

results = {scenario: run_ecosystem_simulation(scenario) for scenario in ['Low', 'Mid', 'High']}

species_weights = {
    'Amazon Rainforest': 0.125, 'Coral Reefs': 0.07, 'Arctic Sea Ice': 0.0075,
    'Boreal Forests': 0.065, 'Savanna Grasslands': 0.06, 'Wetlands': 0.08,
    'Oceans': 0.20, 'Temperate Forests': 0.10
}
total_loss = {scenario: np.zeros((n_iter, len(years))) for scenario in ['Low', 'Mid', 'High']}
for scenario in results:
    for t in range(len(years)):
        total_loss[scenario][:, t] = sum(results[scenario][eco][:, t] * species_weights[eco] 
                                        for eco in ecosystems)

for scenario in ['Low', 'Mid', 'High']:
    total_mean_2175 = np.mean(total_loss[scenario][:, -1]) * 100
    total_ci_2175 = np.percentile(total_loss[scenario][:, -1], [2.5, 97.5]) * 100
    global_mean_2175 = total_mean_2175 * 0.7075  # Modeled contribution
    global_ci_2175 = total_ci_2175 * 0.7075
    print(f"Total Modeled Loss 2175: {total_mean_2175:.1f}%, 95% CI = {total_ci_2175[0]:.1f}–{total_ci_2175[1]:.1f}%")
    print(f"Est. Global Loss 2175: {global_mean_2175:.1f}%, 95% CI = {global_ci_2175[0]:.1f}–{global_ci_2175[1]:.1f}% (modeled 70% only)")
    mean_2125 = np.mean(total_loss[scenario][:, -6]) * 100
    global_2125 = mean_2125 * 0.7075
    if global_2125 > 50:
        print(f"WARNING: {global_2125:.1f}% global loss by 2125 exceeds 50% - risks to food/health.")
    if global_mean_2175 > 70:
        print(f"WARNING: {global_mean_2175:.1f}% global loss by 2175 exceeds 70% - survival threat.")
        
plt.figure(figsize=(12, 8))
sns.set(style="whitegrid")
for scenario in ['Low', 'Mid', 'High']:
    mean_loss = np.mean(total_loss[scenario], axis=0) * 100
    plt.plot(years, mean_loss, label=f'{scenario} Scenario', linewidth=2)
plt.axhline(y=50, color='orange', linestyle='--', label='50% Threshold (Food/Health Risks)')
plt.axhline(y=70, color='red', linestyle='--', label='70% Threshold (Survival Threat)')
plt.title('Projected Biodiversity Loss in Modeled Ecosystems (2025–2175, No Intervention)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('% Biodiversity Loss (Modeled Ecosystems)', fontsize=12)
plt.legend(title='Scenario', fontsize=10)
os.makedirs(FIGURES_DIR, exist_ok=True)
plt.savefig(os.path.join(FIGURES_DIR, 'total_biodiversity_loss.png'), dpi=300, bbox_inches='tight')
plt.close()

all_data = []
for scenario in ['Low', 'Mid', 'High']:
    for eco in ecosystems:
        loss_flat = results[scenario][eco].ravel()
        all_data.append(pd.DataFrame({
            'Ecosystem': eco,
            'Scenario': scenario,
            'Loss': loss_flat,
            'Year': np.tile(years, n_iter)
        }))
results_df = pd.concat(all_data, ignore_index=True)
print(f"DataFrame rows: {len(results_df)} (expected: {n_iter * len(years) * len(ecosystems) * 3})")
os.makedirs(DATA_DIR, exist_ok=True)
results_df.to_csv(os.path.join(DATA_DIR, 'ecosystem_cascade_results.csv'), index=False)
print(f"Results saved to '{os.path.join(DATA_DIR, 'ecosystem_cascade_results.csv')}'")