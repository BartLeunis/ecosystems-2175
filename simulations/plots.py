import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import json

# Dynamically set BASE_DIR to the root of the repository
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(BASE_DIR, 'data')
FIGURES_DIR = os.path.join(BASE_DIR, 'figures')

# Debugging: Print paths to verify
print(f"BASE_DIR: {BASE_DIR}")
print(f"DATA_DIR: {DATA_DIR}")
print(f"FIGURES_DIR: {FIGURES_DIR}")

# Create directories if they don't exist
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(FIGURES_DIR, exist_ok=True)

# Load ecosystems and transform_baselines from config.json
config_path = os.path.join(DATA_DIR, 'config.json')
with open(config_path, 'r') as f:
    config = json.load(f)
ecosystems = config['ecosystems']
transform_baselines = config['transform_baselines']

# Load simulation results
results_path = os.path.join(DATA_DIR, 'ecosystem_cascade_results.csv')
df = pd.read_csv(results_path)

# Set style
sns.set(style="whitegrid")

# --- Scenario Comparison (Matplotlib) ---
plt.figure(figsize=(18, 12))
for i, eco in enumerate(ecosystems, 1):
    plt.subplot(3, 3, i)
    for scenario in ['Low', 'Mid', 'High']:
        eco_df = df[(df['Ecosystem'] == eco) & (df['Scenario'] == scenario)]
        sns.lineplot(x='Year', y='Loss', data=eco_df, label=scenario, linewidth=2)
    
    # Add transformation threshold line
    transform_year = df[(df['Ecosystem'] == eco) & (df['Loss'] >= transform_baselines[eco])]['Year'].min()
    plt.axvline(x=transform_year, color='red', linestyle='--', alpha=0.5, label='Transformation Threshold')
    
    plt.title(eco, fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('% Loss of Ecosystem Function', fontsize=12)
    plt.legend(title='Scenario', fontsize=10)
plt.suptitle('Projected Ecosystem Loss by Ecosystem and Scenario (2025–2175)', fontsize=16, y=1.02)
plt.tight_layout()
plt.savefig(os.path.join(FIGURES_DIR, 'scenario_comparison_by_ecosystem.png'), dpi=300, bbox_inches='tight')
plt.close()

# --- Highlight Transformations (Matplotlib) ---
plt.figure(figsize=(15, 10))
g = sns.FacetGrid(df, col='Ecosystem', hue='Scenario', col_wrap=4, height=3, aspect=1.5)
g.map(sns.lineplot, 'Year', 'Loss', linewidth=2, marker='o')

# Add transformation thresholds
for ax, eco in zip(g.axes.flat, ecosystems):
    transform_year = df[(df['Ecosystem'] == eco) & (df['Loss'] >= transform_baselines[eco])]['Year'].min()
    ax.axvline(x=transform_year, color='red', linestyle='--', alpha=0.5, label='Transformation Threshold')

g.add_legend(title='Scenario', title_fontsize=12, fontsize=10)
g.set_axis_labels('Year', '% Loss of Ecosystem Function', fontsize=10)
g.set_titles('{col_name}', size=12)
g.fig.suptitle('Projected Ecosystem Loss with Transformation Thresholds (2025–2175)', fontsize=16, y=1.05)
plt.savefig(os.path.join(FIGURES_DIR, 'ecosystem_loss_with_transformations.png'), dpi=300, bbox_inches='tight')
plt.close()

# --- Total Loss Plot with Thresholds (Matplotlib) ---
plt.figure(figsize=(12, 8))
for scenario in ['Low', 'Mid', 'High']:
    scenario_df = df[df['Scenario'] == scenario]
    total_loss = scenario_df.groupby('Year')['Loss'].mean() * 100  # Mean across ecosystems, weighted in cascade
    sns.lineplot(x=total_loss.index, y=total_loss, label=f'{scenario} Scenario', linewidth=2)

plt.title('Projected Biodiversity Loss in Modeled Ecosystems (2025–2175, No Intervention)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('% Biodiversity Loss (Modeled Ecosystems)', fontsize=12)
plt.legend(title='Scenario', fontsize=10)
plt.savefig(os.path.join(FIGURES_DIR, 'total_biodiversity_loss.png'), dpi=300, bbox_inches='tight')
plt.close()

print(f"Graphs saved to '{FIGURES_DIR}'")