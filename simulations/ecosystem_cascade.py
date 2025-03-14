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
n_iter = 100000
years = np.arange(2025, 2176, 10)
ecosystems = ['Amazon Rainforest', 'Coral Reefs', 'Arctic Sea Ice', 'Boreal Forests',
              'Savanna Grasslands', 'Wetlands', 'Oceans', 'Temperate Forests',
              'Deserts', 'Tundra', 'Montane', 'Freshwater', 'Polar']

base_loss_means = {
    'Amazon Rainforest': {'Low': 0.03, 'Mid': 0.06, 'High': 0.09},
    'Coral Reefs': {'Low': 0.04, 'Mid': 0.08, 'High': 0.12},
    'Arctic Sea Ice': {'Low': 0.03, 'Mid': 0.06, 'High': 0.09},
    'Boreal Forests': {'Low': 0.02, 'Mid': 0.04, 'High': 0.06},
    'Savanna Grasslands': {'Low': 0.02, 'Mid': 0.04, 'High': 0.06},
    'Wetlands': {'Low': 0.02, 'Mid': 0.05, 'High': 0.07},
    'Oceans': {'Low': 0.03, 'Mid': 0.06, 'High': 0.09},
    'Temperate Forests': {'Low': 0.01, 'Mid': 0.03, 'High': 0.05},
    'Deserts': {'Low': 0.01, 'Mid': 0.03, 'High': 0.05},  # IPCC AR6 Ch. 3
    'Tundra': {'Low': 0.02, 'Mid': 0.04, 'High': 0.07},   # CAFF 2013
    'Montane': {'Low': 0.02, 'Mid': 0.04, 'High': 0.06},  # WWF 2022
    'Freshwater': {'Low': 0.03, 'Mid': 0.06, 'High': 0.09},  # Ramsar 2018
    'Polar': {'Low': 0.01, 'Mid': 0.03, 'High': 0.05}     # IPCC AR6
}
base_loss_std = 0.01  # Higher uncertainty for new ecosystems noted in METHODOLOGY

cascade_effects = {
    'Amazon Rainforest': {'Arctic Sea Ice': 1.2, 'Coral Reefs': 1.1, 'Wetlands': 1.1},
    'Coral Reefs': {'Wetlands': 1.2, 'Savanna Grasslands': 1.1, 'Oceans': 1.1},
    'Arctic Sea Ice': {'Amazon Rainforest': 1.1, 'Boreal Forests': 1.2, 'Oceans': 1.1},
    'Boreal Forests': {'Arctic Sea Ice': 1.1, 'Wetlands': 1.1, 'Temperate Forests': 1.1},
    'Savanna Grasslands': {'Wetlands': 1.1},
    'Wetlands': {'Savanna Grasslands': 1.1, 'Temperate Forests': 1.1},
    'Oceans': {'Coral Reefs': 1.2, 'Arctic Sea Ice': 1.1},
    'Temperate Forests': {'Boreal Forests': 1.1, 'Wetlands': 1.1},
    'Deserts': {'Savanna Grasslands': 1.1},  # Aridification spill
    'Tundra': {'Arctic Sea Ice': 1.1, 'Boreal Forests': 1.1},
    'Montane': {'Temperate Forests': 1.1},
    'Freshwater': {'Wetlands': 1.2, 'Oceans': 1.1},
    'Polar': {'Arctic Sea Ice': 1.1}
}

nuclear_annual_risk = 0.01
nuclear_years = 150
nuclear_prob = 1 - np.exp(-nuclear_annual_risk * nuclear_years)
nuclear_occurs = np.random.binomial(1, nuclear_prob, n_iter)
nuclear_loss = 0.25

transform_threshold = 0.5
transform_targets = {
    'Amazon Rainforest': 'Savanna Grasslands', 'Coral Reefs': 'Oceans',
    'Arctic Sea Ice': 'Oceans', 'Boreal Forests': 'Savanna Grasslands',
    'Savanna Grasslands': None, 'Wetlands': 'Savanna Grasslands',
    'Oceans': None, 'Temperate Forests': 'Savanna Grasslands',
    'Deserts': None, 'Tundra': 'Savanna Grasslands',  # Shrubification
    'Montane': 'Savanna Grasslands', 'Freshwater': 'Wetlands', 'Polar': 'Oceans'
}
final_baselines = {
    'Amazon Rainforest': 0.10, 'Coral Reefs': 0.05, 'Arctic Sea Ice': 0.20,
    'Boreal Forests': 0.20, 'Savanna Grasslands': 0.40, 'Wetlands': 0.15,
    'Oceans': 0.25, 'Temperate Forests': 0.30, 'Deserts': 0.50,  # Resilient
    'Tundra': 0.30, 'Montane': 0.40, 'Freshwater': 0.20, 'Polar': 0.40
}

def run_ecosystem_simulation(scenario):
    loss_dict = {eco: np.zeros((n_iter, len(years))) for eco in ecosystems}
    transformed = {eco: np.zeros(n_iter, dtype=bool) for eco in ecosystems}
    for t, year in enumerate(years):
        for eco in ecosystems:
            if t > 0:
                transformed[eco] = loss_dict[eco][:, t-1] >= transform_threshold
            target_eco = transform_targets[eco]
            mean_loss = (base_loss_means[eco][scenario] if not np.any(transformed[eco])
                         else (base_loss_means[target_eco][scenario] if target_eco else base_loss_means[eco][scenario]))
            annual_loss = stats.norm(loc=mean_loss, scale=base_loss_std).rvs(n_iter)
            loss_dict[eco][:, t] = loss_dict[eco][:, t-1] + annual_loss if t > 0 else annual_loss
            if t > 0 and np.any(nuclear_occurs):
                nuclear_effect = nuclear_occurs * nuclear_loss * (t / len(years))
                loss_dict[eco][:, t] += nuclear_effect
            for source_eco, targets in cascade_effects.items():
                if eco in targets:
                    source_mean = np.mean(loss_dict[source_eco][:, t])
                    multiplier = targets[eco]
                    if transformed[source_eco].any() and source_mean > transform_threshold:
                        multiplier *= 0.8
                    if source_mean > transform_threshold:
                        loss_dict[eco][:, t] *= multiplier
            max_loss = 1.0 - final_baselines[eco]
            loss_dict[eco][:, t] = np.minimum(loss_dict[eco][:, t], max_loss)
    return loss_dict

results = {scenario: run_ecosystem_simulation(scenario) for scenario in ['Low', 'Mid', 'High']}

species_weights = {
    'Amazon Rainforest': 0.125, 'Coral Reefs': 0.07, 'Arctic Sea Ice': 0.0075,
    'Boreal Forests': 0.065, 'Savanna Grasslands': 0.06, 'Wetlands': 0.08,
    'Oceans': 0.20, 'Temperate Forests': 0.10, 'Deserts': 0.05, 'Tundra': 0.02,
    'Montane': 0.08, 'Freshwater': 0.10, 'Polar': 0.01
}

total_loss = {scenario: np.zeros((n_iter, len(years))) for scenario in ['Low', 'Mid', 'High']}
for scenario in results:
    for t in range(len(years)):
        total_loss[scenario][:, t] = sum(results[scenario][eco][:, t] * species_weights[eco] 
                                        for eco in ecosystems)

for scenario in ['Low', 'Mid', 'High']:
    print(f"\n--- {scenario.upper()} SCENARIO (NO INTERVENTION) ---")
    for eco in ecosystems:
        mean_loss_2175 = np.mean(results[scenario][eco][:, -1]) * 100
        ci_2175 = np.percentile(results[scenario][eco][:, -1], [2.5, 97.5]) * 100
        print(f"{eco}: Net Loss 2175 = {mean_loss_2175:.1f}%, 95% CI = {ci_2175[0]:.1f}–{ci_2175[1]:.1f}%")
    total_mean_2175 = np.mean(total_loss[scenario][:, -1]) * 100
    total_ci_2175 = np.percentile(total_loss[scenario][:, -1], [2.5, 97.5]) * 100
    print(f"Total Loss 2175: {total_mean_2175:.1f}%, 95% CI = {total_ci_2175[0]:.1f}–{total_ci_2175[1]:.1f}%")
    mean_2125 = np.mean(total_loss[scenario][:, -6]) * 100
    if mean_2125 > 50:
        print(f"WARNING: {mean_2125:.1f}% loss by 2125 exceeds 50% - food/health risks.")
    if total_mean_2175 > 70:
        print(f"WARNING: {total_mean_2175:.1f}% loss by 2175 exceeds 70% - survival threat.")

plt.figure(figsize=(12, 8))
sns.set(style="whitegrid")
for scenario in ['Low', 'Mid', 'High']:
    total_loss_mean = np.mean(total_loss[scenario], axis=0) * 100
    plt.plot(years, total_loss_mean, label=f'{scenario} Scenario', linewidth=2)
plt.axhline(y=50, color='orange', linestyle='--', label='50% Threshold (Food/Health Risks)')
plt.axhline(y=70, color='red', linestyle='--', label='70% Threshold (Survival Threat)')
plt.title('Total Biodiversity Loss (2025–2175, No Intervention)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('% Total Biodiversity Loss', fontsize=12)
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
os.makedirs(DATA_DIR, exist_ok=True)
results_df.to_csv(os.path.join(DATA_DIR, 'ecosystem_cascade_results.csv'), index=False)
print(f"Results saved to '{os.path.join(DATA_DIR, 'ecosystem_cascade_results.csv')}'")