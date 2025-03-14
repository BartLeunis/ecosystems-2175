import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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

# Define ecosystems and transformation threshold inline (from ecosystem_cascade.py)
ecosystems = [
    'Amazon Rainforest', 'Coral Reefs', 'Arctic Sea Ice', 'Boreal Forests',
    'Savanna Grasslands', 'Wetlands', 'Oceans', 'Temperate Forests',
    'Deserts', 'Tundra', 'Montane', 'Freshwater', 'Polar'
]
transform_threshold = 0.5  # Matches model’s transformation trigger

# Load simulation results
results_path = os.path.join(DATA_DIR, 'ecosystem_cascade_results.csv')
df = pd.read_csv(results_path)

# Set style
sns.set(style="whitegrid")

# --- Scenario Comparison by Ecosystem (Matplotlib) ---
plt.figure(figsize=(20, 15))  # Increased size for 13 ecosystems
for i, eco in enumerate(ecosystems, 1):
    plt.subplot(4, 4, i)  # Adjusted to 4x4 grid (16 slots, 13 used)
    for scenario in ['Low', 'Mid', 'High']:
        eco_df = df[(df['Ecosystem'] == eco) & (df['Scenario'] == scenario)]
        sns.lineplot(x='Year', y='Loss', data=eco_df, label=scenario, linewidth=2)
    
    # Add transformation threshold line (first year loss ≥ 0.5)
    transform_year = df[(df['Ecosystem'] == eco) & (df['Loss'] >= transform_threshold)]['Year'].min()
    if pd.notna(transform_year):  # Only plot if threshold crossed
        plt.axvline(x=transform_year, color='red', linestyle='--', alpha=0.5, label='Transform Threshold')
    
    plt.title(eco, fontsize=12)
    plt.xlabel('Year', fontsize=10)
    plt.ylabel('% Loss', fontsize=10)
    plt.legend(title='Scenario', fontsize=8)
plt.suptitle('Projected Ecosystem Loss by Ecosystem and Scenario (2025–2175)', fontsize=16, y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(FIGURES_DIR, 'scenario_comparison_by_ecosystem.png'), dpi=300, bbox_inches='tight')
plt.close()

# --- Highlight Transformations (Seaborn FacetGrid) ---
plt.figure(figsize=(15, 12))  # Adjusted for readability
g = sns.FacetGrid(df, col='Ecosystem', hue='Scenario', col_wrap=4, height=3, aspect=1.5)
g.map(sns.lineplot, 'Year', 'Loss', linewidth=2, marker='o')

# Add transformation thresholds
for ax, eco in zip(g.axes.flat, ecosystems):
    transform_year = df[(df['Ecosystem'] == eco) & (df['Loss'] >= transform_threshold)]['Year'].min()
    if pd.notna(transform_year):
        ax.axvline(x=transform_year, color='red', linestyle='--', alpha=0.5, label='Transform Threshold')

g.add_legend(title='Scenario', title_fontsize=12, fontsize=10)
g.set_axis_labels('Year', '% Loss of Ecosystem Function', fontsize=10)
g.set_titles('{col_name}', size=12)
g.fig.suptitle('Projected Ecosystem Loss with Transformation Thresholds (2025–2175)', fontsize=16, y=1.05)
plt.savefig(os.path.join(FIGURES_DIR, 'ecosystem_loss_with_transformations.png'), dpi=300, bbox_inches='tight')
plt.close()

print(f"Graphs saved to '{FIGURES_DIR}'")