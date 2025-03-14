import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import json

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

# Add transformation baselines (rough estimates, refine with refs)
transform_baselines = {
    'Amazon Rainforest': 0.25,  # Savanna-like
    'Coral Reefs': 0.15,        # Algae-dominated
    'Arctic Sea Ice': 0.35,     # Open water
    'Boreal Forests': 0.40,     # Shrubland
    'Savanna Grasslands': 0.60, # Degraded but stable
    'Wetlands': 0.30,           # Drained marsh
    'Oceans': 0.40,             # Warmer, less diverse
    'Temperate Forests': 0.50   # Drier woodland
}
# Transformation mappings (ecosystem → new state)
transform_targets = {
    'Amazon Rainforest': 'Savanna Grasslands',  # Rainforest to steppe
    'Coral Reefs': 'Oceans',                    # Reefs to algae-dominated sea
    'Arctic Sea Ice': 'Oceans',                 # Ice to open water
    'Boreal Forests': 'Savanna Grasslands',     # Taiga to shrubland
    'Savanna Grasslands': None,                 # Already transformed-like
    'Wetlands': 'Savanna Grasslands',           # Drained to dryland
    'Oceans': None,                             # Stays oceanic, just warmer
    'Temperate Forests': 'Savanna Grasslands'   # Forest to woodland
}

# Final degraded baselines
final_baselines = {
    'Amazon Rainforest': 0.10, 'Coral Reefs': 0.05, 'Arctic Sea Ice': 0.20,
    'Boreal Forests': 0.20, 'Savanna Grasslands': 0.40, 'Wetlands': 0.15,
    'Oceans': 0.25, 'Temperate Forests': 0.30
}
# Save ecosystems and transform_baselines to config.json
config = {
    'ecosystems': ecosystems,
    'transform_baselines': transform_baselines
}
config_path = os.path.join(DATA_DIR, 'config.json')
with open(config_path, 'w') as f:
    json.dump(config, f)

print(f"Config saved to: {config_path}")

def run_ecosystem_simulation(scenario):
    loss_dict = {eco: np.zeros((n_iter, len(years))) for eco in ecosystems}
    transformed = {eco: np.zeros(n_iter, dtype=bool) for eco in ecosystems}
    for t, year in enumerate(years):
        for eco in ecosystems:
            # Check transformation using ecosystem's specific threshold
            if t > 0:
                transformed[eco] = loss_dict[eco][:, t-1] >= transform_baselines[eco]
            # Determine target ecosystem and mean loss
            target_eco = transform_targets[eco]
            # Apply target loss rate only to transformed simulations
            current_means = np.full(n_iter, base_loss_means[eco][scenario])
            if target_eco:
                transformed_mask = transformed[eco]
                current_means[transformed_mask] = base_loss_means[target_eco][scenario]
            annual_loss = stats.norm(loc=current_means, scale=base_loss_std).rvs()
            loss_dict[eco][:, t] = loss_dict[eco][:, t-1] + annual_loss if t > 0 else annual_loss
            # Apply nuclear effect
            if t > 0 and np.any(nuclear_occurs):
                nuclear_effect = nuclear_occurs * nuclear_loss * (t / len(years))
                loss_dict[eco][:, t] += nuclear_effect
            # Apply cascade effects
            for source_eco, targets in cascade_effects.items():
                if eco in targets:
                    source_losses = loss_dict[source_eco][:, t]
                    multiplier = targets[eco]
                    # Check if source ecosystem has transformed in each simulation
                    source_transformed = source_losses >= transform_baselines[source_eco]
                    reduced_multiplier = multiplier * 0.8
                    # Apply reduced multiplier where source is transformed
                    cascade_multipliers = np.where(source_transformed, reduced_multiplier, multiplier)
                    loss_dict[eco][:, t] *= cascade_multipliers
            # Cap losses at ecosystem's maximum allowed loss
            max_loss = 1.0 - final_baselines[eco]
            loss_dict[eco][:, t] = np.minimum(loss_dict[eco][:, t], max_loss)
    return loss_dict


results = {scenario: run_ecosystem_simulation(scenario) for scenario in ['Low', 'Mid', 'High']}

species_weights = {
    'Amazon Rainforest': 0.125, 'Coral Reefs': 0.07, 'Arctic Sea Ice': 0.0075,
    'Boreal Forests': 0.065, 'Savanna Grasslands': 0.06, 'Wetlands': 0.08,
    'Oceans': 0.20, 'Temperate Forests': 0.10
}

total_loss = {scenario: np.zeros((n_iter, len(years))) for scenario in ['Low', 'Mid', 'High']}


for scenario in ['Low', 'Mid', 'High']:
    for t in range(len(years)):
        # Weighted sum across ecosystems
        total_loss[scenario][:, t] = sum(
            results[scenario][eco][:, t] * species_weights[eco] 
            for eco in ecosystems
        )

for scenario in ['Low', 'Mid', 'High']:
    # Convert modeled loss to global scale (70% coverage)
    global_loss = total_loss[scenario] * 0.7075  # 70% coverage factor
    
    # Calculate thresholds for comparison
    threshold_50_global = 50  # Absolute 50% of global biodiversity
    threshold_70_global = 70  # Absolute 70% of global biodiversity
for scenario in ['Low', 'Mid', 'High']:
    print(f"\n---- {scenario} Scenario Results ----")
    
    # Ecosystem-specific results
    for eco in ecosystems:
        mean_loss_2175 = np.mean(results[scenario][eco][:, -1]) * 100
        ci_2175 = np.percentile(results[scenario][eco][:, -1], [2.5, 97.5]) * 100
        print(f"{eco}: Net Loss 2175 = {mean_loss_2175:.1f}%, 95% CI = {ci_2175[0]:.1f}–{ci_2175[1]:.1f}%")
    
    # Total/global results
    total_mean_2175 = np.mean(total_loss[scenario][:, -1]) * 100
    total_ci_2175 = np.percentile(total_loss[scenario][:, -1], [2.5, 97.5]) * 100
    
    # Global biodiversity impact (modeled portion only)
    global_mean_2175 = total_mean_2175 * 0.7075
    global_ci_2175 = total_ci_2175 * 0.7075
    
    print(f"\nModeled Ecosystems Loss (70% Coverage): {total_mean_2175:.1f}%, 95% CI = {total_ci_2175[0]:.1f}–{total_ci_2175[1]:.1f}%")
    print(f"Projected Global Impact: {global_mean_2175:.1f}%, 95% CI = {global_ci_2175[0]:.1f}–{global_ci_2175[1]:.1f}%")

    # Threshold checks (using global scale)
    if global_mean_2175 > 50:
        print(f"WARNING: Projected {global_mean_2175:.1f}% projected global loss exceeds 50% threshold - food/health systems at risk.")
    if global_mean_2175 > 70:
        print(f"CRITICAL: Projected {global_mean_2175:.1f}% projected global loss exceeds 70% threshold - survival-level risks.")

    # Threshold checks (adjusted for 70% coverage)
    threshold_50_global = 50 / 0.7075  #≈ 70.7% of modeled loss = 50% of global
    threshold_70_global = 70 / 0.7075  #≈ 98.9% of modeled loss = 70% of global

    if global_mean_2175 > threshold_50_global:
        print(f"WARNING: Modeled ecosystems loss {global_mean_2175:.1f}% ({global_mean_2175*0.7075:.1f}% global) exceeds 50% threshold.")
    if global_mean_2175 > threshold_70_global:
        print(f"WARNING: Modeled ecosystems loss {global_mean_2175:.1f}% ({global_mean_2175*0.7075:.1f}% global) exceeds 70% threshold.")

# Plot projected global impact (scaled to 100% biodiversity)
plt.figure(figsize=(12, 8))
for scenario in ['Low', 'Mid', 'High']:
    global_loss = np.mean(total_loss[scenario], axis=0) * 100 * 0.7075
    plt.plot(years, global_loss, label=f'{scenario} Scenario', linewidth=2)

plt.axhline(y=50, color='orange', linestyle='--', label='50% Threshold (Food/Health Risks)')
plt.axhline(y=70, color='red', linestyle='--', label='70% Threshold (Survival Threat)')
plt.title('Projected Global Biodiversity Loss (2025–2175, No Intervention)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('% Projected Global Biodiversity Loss', fontsize=12)
plt.legend(title='Scenario', fontsize=10)
os.makedirs(FIGURES_DIR, exist_ok=True)
plt.savefig(os.path.join(FIGURES_DIR, 'projected_global_biodiversity_loss.png'), dpi=300, bbox_inches='tight')
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