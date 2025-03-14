import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Dynamically set BASE_DIR to the root of the repository
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(BASE_DIR, 'data')
FIGURES_DIR = os.path.join(BASE_DIR, 'figures')

print(f"BASE_DIR: {BASE_DIR}")
print(f"DATA_DIR: {DATA_DIR}")
print(f"FIGURES_DIR: {FIGURES_DIR}")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(FIGURES_DIR, exist_ok=True)

ecosystems = [
    'Amazon Rainforest', 'Coral Reefs', 'Arctic Sea Ice', 'Boreal Forests',
    'Savanna Grasslands', 'Wetlands', 'Oceans', 'Temperate Forests',
    'Deserts', 'Tundra', 'Montane', 'Freshwater', 'Polar'
]
transform_threshold = 0.5
transform_targets = {
    'Amazon Rainforest': 'Savanna Grasslands', 'Coral Reefs': 'Oceans',
    'Arctic Sea Ice': 'Oceans', 'Boreal Forests': 'Savanna Grasslands',
    'Savanna Grasslands': None, 'Wetlands': 'Savanna Grasslands',
    'Oceans': None, 'Temperate Forests': 'Savanna Grasslands',
    'Deserts': None, 'Tundra': 'Savanna Grasslands',
    'Montane': 'Savanna Grasslands', 'Freshwater': 'Wetlands', 'Polar': 'Oceans'
}
species_weights = {
    'Amazon Rainforest': 0.125, 'Coral Reefs': 0.07, 'Arctic Sea Ice': 0.0075,
    'Boreal Forests': 0.065, 'Savanna Grasslands': 0.06, 'Wetlands': 0.08,
    'Oceans': 0.20, 'Temperate Forests': 0.10, 'Deserts': 0.05, 'Tundra': 0.02,
    'Montane': 0.08, 'Freshwater': 0.10, 'Polar': 0.01
}

# Load simulation results and shock logs
results_no_shock_path = os.path.join(DATA_DIR, 'ecosystem_cascade_results_no_shock.csv')
results_with_shock_path = os.path.join(DATA_DIR, 'ecosystem_cascade_results_with_shock.csv')
shock_log_path = os.path.join(DATA_DIR, 'shock_log_high.csv')
df_no_shock = pd.read_csv(results_no_shock_path)
df_with_shock = pd.read_csv(results_with_shock_path)
shock_log = pd.read_csv(shock_log_path)

sns.set(style="whitegrid")

# --- Plot 1: Shock vs. No-Shock Overlay with CI ---
plt.figure(figsize=(12, 8))
years = np.unique(df_no_shock['Year'])  # Should be 15 (2025–2175, step 10)
for scenario in ['High']:
    no_shock_mean = df_no_shock[df_no_shock['Scenario'] == scenario].groupby('Year')['Loss'].mean() * 100
    no_shock_ci_low = df_no_shock[df_no_shock['Scenario'] == scenario].groupby('Year')['Loss'].quantile(0.025) * 100
    no_shock_ci_high = df_no_shock[df_no_shock['Scenario'] == scenario].groupby('Year')['Loss'].quantile(0.975) * 100
    with_shock_mean = df_with_shock[df_with_shock['Scenario'] == scenario].groupby('Year')['Loss'].mean() * 100
    with_shock_ci_low = df_with_shock[df_with_shock['Scenario'] == scenario].groupby('Year')['Loss'].quantile(0.025) * 100
    with_shock_ci_high = df_with_shock[df_with_shock['Scenario'] == scenario].groupby('Year')['Loss'].quantile(0.975) * 100
    
    plt.plot(years, no_shock_mean, label=f'{scenario} (No Shock)', linestyle='--', color='gray', linewidth=2)
    plt.fill_between(years, no_shock_ci_low, no_shock_ci_high, color='gray', alpha=0.2)
    plt.plot(years, with_shock_mean, label=f'{scenario} (With Shock)', linestyle='-', color='blue', linewidth=2)
    plt.fill_between(years, with_shock_ci_low, with_shock_ci_high, color='lightblue', alpha=0.3)

plt.axhline(y=50, color='orange', linestyle='--', label='50% Threshold')
plt.axhline(y=70, color='red', linestyle='--', label='70% Threshold')
plt.title('High Scenario Biodiversity Loss: Shock vs. No-Shock with 95% CI (2025–2175)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('% Total Biodiversity Loss', fontsize=12)
plt.legend(title='Scenario', fontsize=10, loc='upper left')
plt.savefig(os.path.join(FIGURES_DIR, 'shock_vs_no_shock_overlay_with_ci.png'), dpi=300, bbox_inches='tight')
plt.close()

# --- Plot 2: Ecosystem Breakdown with Transformation Flags ---
plt.figure(figsize=(14, 8))
high_shock_2175 = df_with_shock[(df_with_shock['Scenario'] == 'High') & (df_with_shock['Year'] == 2175)]
mean_losses = high_shock_2175.groupby('Ecosystem')['Loss'].mean() * 100
ci_low = high_shock_2175.groupby('Ecosystem')['Loss'].quantile(0.025) * 100
ci_high = high_shock_2175.groupby('Ecosystem')['Loss'].quantile(0.975) * 100
transformed = mean_losses >= (transform_threshold * 100)

lower_errors = np.maximum(mean_losses - ci_low, 0)
upper_errors = ci_high - mean_losses
errors = [lower_errors, upper_errors]

bars = plt.bar(mean_losses.index, mean_losses, yerr=errors, capsize=5, color='skyblue', edgecolor='black')
for bar, is_transformed in zip(bars, transformed):
    if is_transformed:
        bar.set_hatch('//')

plt.axhline(y=50, color='orange', linestyle='--', label='50% Threshold')
plt.axhline(y=90, color='red', linestyle='--', label='90% Near-Collapse')
plt.title('Ecosystem Loss in High Scenario with Shocks (2175)', fontsize=16)
plt.xlabel('Ecosystem', fontsize=12)
plt.ylabel('% Loss of Ecosystem Function', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.legend(fontsize=10)
plt.tight_layout()
plt.savefig(os.path.join(FIGURES_DIR, 'ecosystem_breakdown_2175_high_shock.png'), dpi=300, bbox_inches='tight')
plt.close()

# --- Plot 3: Shock Impact with Weighted Loss and Exact Shocks ---
plt.figure(figsize=(14, 8))
sample_runs = 5
high_shock_df = df_with_shock[df_with_shock['Scenario'] == 'High']
n_years = len(years)  # 15
n_ecosystems = len(ecosystems)  # 13
rows_per_run = n_years * n_ecosystems
total_runs = len(high_shock_df) // rows_per_run
run_ids = np.random.choice(total_runs, sample_runs, replace=False)

for run_id in run_ids:
    start_idx = run_id * rows_per_run
    end_idx = (run_id + 1) * rows_per_run
    run_data = high_shock_df.iloc[start_idx:end_idx]
    if len(run_data) == rows_per_run:
        # Weighted total loss per year
        weighted_loss = np.zeros(n_years)
        for i, year in enumerate(years):
            year_data = run_data[run_data['Year'] == year]
            weighted_loss[i] = sum(year_data[year_data['Ecosystem'] == eco]['Loss'].mean() * species_weights[eco]
                                  for eco in ecosystems) * 100
        plt.plot(years, weighted_loss, label=f'Run {run_id}', alpha=0.7, linewidth=1.5)
        
        # Exact shock years from log
        run_shocks = shock_log[shock_log['iteration'] == run_id]
        for _, shock in run_shocks.iterrows():
            color = 'green' if shock['type'] == 'positive' else 'purple'
            plt.axvline(x=shock['year'], color=color, linestyle='--', alpha=0.5)

plt.axhline(y=50, color='orange', linestyle='--', label='50% Threshold')
plt.axhline(y=70, color='red', linestyle='--', label='70% Threshold')
plt.title('Shock Impacts on Weighted Total Loss (High Scenario, Sample Runs)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('% Total Biodiversity Loss (Weighted)', fontsize=12)
plt.legend(title='Sample Runs', fontsize=10, loc='upper left')
plt.savefig(os.path.join(FIGURES_DIR, 'shock_impact_sample_runs_weighted.png'), dpi=300, bbox_inches='tight')
plt.close()

print(f"Graphs saved to '{FIGURES_DIR}'")