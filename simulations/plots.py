import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Dynamically set BASE_DIR to the root of the repository
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(BASE_DIR, 'data')
FIGURES_DIR = os.path.join(BASE_DIR, 'figures')

# Debugging: Print paths to verify
print(f"BASE_DIR: {BASE_DIR}")
print(f"DATA_DIR: {DATA_DIR}")
print(f"FIGURES_DIR: {FIGURES_DIR}")

# Create directories if they don’t exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(FIGURES_DIR, exist_ok=True)

# Define ecosystems inline (from ecosystem_cascade.py)
ecosystems = [
    'Amazon Rainforest', 'Coral Reefs', 'Arctic Sea Ice', 'Boreal Forests',
    'Savanna Grasslands', 'Wetlands', 'Oceans', 'Temperate Forests',
    'Deserts', 'Tundra', 'Montane', 'Freshwater', 'Polar'
]
transform_threshold = 0.5

# Load simulation results
results_no_shock_path = os.path.join(DATA_DIR, 'ecosystem_cascade_results_no_shock.csv')
results_with_shock_path = os.path.join(DATA_DIR, 'ecosystem_cascade_results_with_shock.csv')
df_no_shock = pd.read_csv(results_no_shock_path)
df_with_shock = pd.read_csv(results_with_shock_path)

# Set style
sns.set(style="whitegrid")

# --- Plot 1: Shock vs. No-Shock Overlay ---
plt.figure(figsize=(12, 8))
years = np.unique(df_no_shock['Year'])
for scenario in ['Low', 'Mid', 'High']:
    no_shock_mean = df_no_shock[df_no_shock['Scenario'] == scenario].groupby('Year')['Loss'].mean() * 100
    with_shock_mean = df_with_shock[df_with_shock['Scenario'] == scenario].groupby('Year')['Loss'].mean() * 100
    plt.plot(years, no_shock_mean, label=f'{scenario} (No Shock)', linestyle='--', linewidth=2)
    plt.plot(years, with_shock_mean, label=f'{scenario} (With Shock)', linestyle='-', linewidth=2)

plt.axhline(y=50, color='orange', linestyle='--', label='50% Threshold (Food/Health Risks)')
plt.axhline(y=70, color='red', linestyle='--', label='70% Threshold (Survival Threat)')
plt.title('Biodiversity Loss: Shock vs. No-Shock Scenarios (2025–2175)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('% Total Biodiversity Loss', fontsize=12)
plt.legend(title='Scenario', fontsize=10, loc='upper left')
plt.savefig(os.path.join(FIGURES_DIR, 'shock_vs_no_shock_overlay.png'), dpi=300, bbox_inches='tight')
plt.close()

# --- Plot 2: Ecosystem Breakdown (Bar Chart, High Scenario with Shocks) ---
plt.figure(figsize=(14, 8))
high_shock_2175 = df_with_shock[(df_with_shock['Scenario'] == 'High') & (df_with_shock['Year'] == 2175)]
mean_losses = high_shock_2175.groupby('Ecosystem')['Loss'].mean() * 100
ci_low = high_shock_2175.groupby('Ecosystem')['Loss'].quantile(0.025) * 100
ci_high = high_shock_2175.groupby('Ecosystem')['Loss'].quantile(0.975) * 100

# Fix error bars: ensure non-negative distances
lower_errors = np.maximum(mean_losses - ci_low, 0)
upper_errors = ci_high - mean_losses
errors = [lower_errors, upper_errors]

plt.bar(mean_losses.index, mean_losses, yerr=errors, capsize=5, color='skyblue', edgecolor='black')
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

# --- Plot 3: Shock Impact (Sample Runs with Vertical Lines) ---
plt.figure(figsize=(14, 8))
sample_runs = 5  # Show 5 random iterations
high_shock_df = df_with_shock[df_with_shock['Scenario'] == 'High']

# Group by iteration (assuming 15 years per run, 13 ecosystems)
n_years = len(np.unique(high_shock_df['Year']))  # Should be 15
n_ecosystems = len(ecosystems)  # 13
rows_per_run = n_years * n_ecosystems
total_runs = len(high_shock_df) // rows_per_run
run_ids = np.random.choice(total_runs, sample_runs, replace=False)

for run_id in run_ids:
    start_idx = run_id * rows_per_run
    end_idx = (run_id + 1) * rows_per_run
    run_data = high_shock_df.iloc[start_idx:end_idx]
    if len(run_data) == rows_per_run:  # Ensure full run data
        total_loss = run_data.groupby('Year')['Loss'].mean() * 100
        plt.plot(years, total_loss, label=f'Run {run_id}', alpha=0.7, linewidth=1.5)
        
        # Detect shock years (significant jumps or drops)
        loss_diff = np.diff(total_loss)
        shock_years = years[1:][(loss_diff > 3) | (loss_diff < -2)]
        for shock_year in shock_years:
            plt.axvline(x=shock_year, color='gray', linestyle='--', alpha=0.5)

plt.axhline(y=50, color='orange', linestyle='--', label='50% Threshold')
plt.axhline(y=70, color='red', linestyle='--', label='70% Threshold')
plt.title('Shock Impacts on Total Loss (High Scenario, Sample Runs)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('% Total Biodiversity Loss', fontsize=12)
plt.legend(title='Sample Runs', fontsize=10, loc='upper left')
plt.savefig(os.path.join(FIGURES_DIR, 'shock_impact_sample_runs.png'), dpi=300, bbox_inches='tight')
plt.close()

print(f"Graphs saved to '{FIGURES_DIR}'")