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

# Inspect the DataFrame structure for debugging
print("No-Shock DataFrame columns:", df_no_shock.columns)
print("With-Shock DataFrame columns:", df_with_shock.columns)
print("Sample of No-Shock DataFrame:\n", df_no_shock.head())

sns.set(style="whitegrid")

# --- Plot 1: Total Biodiversity Loss by Scenario with Shock vs. No-Shock and 95% CI ---
plt.figure(figsize=(12, 8))
years = np.unique(df_no_shock['Year'])  # Should be 2025 to 2175 (151 years)
color_map = {'Low': 'green', 'Mid': 'orange', 'High': 'red'}

# Compute total biodiversity loss for each iteration and year
def compute_total_biodiversity_loss(df, scenario):
    # Filter by scenario
    df_scen = df[df['Scenario'] == scenario]
    # Group by RunID and Year, then pivot to get Loss per Ecosystem
    grouped = df_scen.groupby(['RunID', 'Year', 'Ecosystem'])['Loss'].mean().reset_index()
    pivoted = grouped.pivot(index=['RunID', 'Year'], columns='Ecosystem', values='Loss')
    # Ensure all ecosystems are present
    for eco in ecosystems:
        if eco not in pivoted.columns:
            pivoted[eco] = 0.0
    # Compute weighted total loss for each RunID and Year
    total_loss = np.zeros((len(np.unique(df_scen['RunID'])), len(years)))
    for run_idx, run_id in enumerate(np.unique(df_scen['RunID'])):
        for year_idx, year in enumerate(years):
            row = pivoted.loc[(run_id, year)] if (run_id, year) in pivoted.index else pd.Series(0.0, index=ecosystems)
            total_loss[run_idx, year_idx] = np.sum(row * pd.Series(species_weights)) * 100
    # Compute mean and CI
    mean_loss = np.mean(total_loss, axis=0)
    ci_low = np.percentile(total_loss, 2.5, axis=0)
    ci_high = np.percentile(total_loss, 97.5, axis=0)
    return mean_loss, ci_low, ci_high

for scenario in ['Low', 'Mid', 'High']:
    # No-Shock
    mean_loss_no, ci_low_no, ci_high_no = compute_total_biodiversity_loss(df_no_shock, scenario)
    plt.plot(years, mean_loss_no, label=f'{scenario} (No Shock)', linestyle='--', color=color_map[scenario], linewidth=2)
    plt.fill_between(years, ci_low_no, ci_high_no, color=color_map[scenario], alpha=0.2)

    # With-Shock
    mean_loss_with, ci_low_with, ci_high_with = compute_total_biodiversity_loss(df_with_shock, scenario)
    plt.plot(years, mean_loss_with, label=f'{scenario} (With Shock)', linestyle='-', color=color_map[scenario], linewidth=2)
    plt.fill_between(years, ci_low_with, ci_high_with, color=color_map[scenario], alpha=0.2)

plt.axhline(y=50, color='yellow', linestyle='--', label='50% Threshold')
plt.axhline(y=70, color='purple', linestyle='--', label='70% Threshold')
plt.title('Total Biodiversity Loss by Scenario: Shock vs. No-Shock with 95% CI (2025–2175)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('% Total Biodiversity Loss', fontsize=12)
plt.legend(title='Scenario', fontsize=10, loc='upper left')
plt.savefig(os.path.join(FIGURES_DIR, 'total_biodiversity_loss_with_shocks.png'), dpi=300, bbox_inches='tight')
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

# --- Plot 3: Shock Impact with Weighted Loss and Exact Shocks ---
plt.figure(figsize=(14, 8))
sample_runs = 5
high_shock_df = df_with_shock[df_with_shock['Scenario'] == 'High']
n_years = len(np.unique(high_shock_df['Year']))  # 151 years
n_ecosystems = len(ecosystems)  # 13
rows_per_run = n_years * n_ecosystems
total_runs = len(high_shock_df) // rows_per_run
run_ids = np.random.choice(total_runs, sample_runs, replace=False)

for run_id in run_ids:
    run_data = high_shock_df[high_shock_df['RunID'] == run_id]
    if len(run_data) == rows_per_run:
        # Weighted total loss per year
        weighted_loss = np.zeros(n_years)
        year_indices = np.unique(run_data['Year'].values)
        for i, year in enumerate(year_indices):
            year_data = run_data[run_data['Year'] == year]
            weighted_loss[i] = np.sum([year_data[year_data['Ecosystem'] == eco]['Loss'].mean() * species_weights[eco] for eco in ecosystems]) * 100
        plt.plot(year_indices, weighted_loss, label=f'Run {run_id}', alpha=0.7, linewidth=1.5)
        
        # Exact shock years from log
        run_shocks = shock_log[shock_log['iteration'] == run_id]
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

print(f"Graphs saved to '{FIGURES_DIR}'")