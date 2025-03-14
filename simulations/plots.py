import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Ensure correct file paths from repo root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
FIGURES_DIR = os.path.join(BASE_DIR, 'figures')

# Load data
df = pd.read_csv(os.path.join(DATA_DIR, 'ecosystem_cascade_results.csv'))

sns.set(style="whitegrid")

# Version 1: Ecosystem Plots (All Scenarios)
plt.figure(figsize=(15, 10))
g1 = sns.FacetGrid(df, col='Ecosystem', hue='Scenario', col_wrap=4, height=3, aspect=1.5)
g1.map(sns.lineplot, 'Year', 'Loss', linewidth=2, marker='o')
g1.add_legend(title='Scenario', title_fontsize=12, fontsize=10)
g1.set_axis_labels('Year', '% Loss of Ecosystem Function', fontsize=10)
g1.set_titles('{col_name}', size=12)
g1.fig.suptitle('Projected Ecosystem Loss by Ecosystem (2025–2175, No Intervention)', fontsize=16, y=1.05)
os.makedirs(FIGURES_DIR, exist_ok=True)
plt.savefig(os.path.join(FIGURES_DIR, 'ecosystem_loss_by_ecosystem.png'), dpi=300, bbox_inches='tight')
plt.close()

# Version 2: Scenario Plots (All Ecosystems)
plt.figure(figsize=(15, 10))
g2 = sns.FacetGrid(df, col='Scenario', hue='Ecosystem', col_wrap=3, height=4, aspect=1.2)
g2.map(sns.lineplot, 'Year', 'Loss', linewidth=2, marker='o')
g2.add_legend(title='Ecosystem', title_fontsize=12, fontsize=10, bbox_to_anchor=(1.05, 1), loc='upper left')
g2.set_axis_labels('Year', '% Loss of Ecosystem Function', fontsize=10)
g2.set_titles('{col_name} Scenario', size=12)
g2.fig.suptitle('Projected Ecosystem Loss by Scenario (2025–2175, No Intervention)', fontsize=16, y=1.05)
plt.savefig(os.path.join(FIGURES_DIR, 'ecosystem_loss_by_scenario.png'), dpi=300, bbox_inches='tight')
plt.close()

# Total Loss Plot with Thresholds
plt.figure(figsize=(12, 8))
for scenario in ['Low', 'Mid', 'High']:
    scenario_df = df[df['Scenario'] == scenario]
    total_loss = scenario_df.groupby('Year')['Loss'].mean() * 100  # Mean across ecosystems, weighted in cascade
    sns.lineplot(x=total_loss.index, y=total_loss, label=f'{scenario} Scenario', linewidth=2)
plt.axhline(y=50, color='orange', linestyle='--', label='50% Threshold (Food/Health Risks)')
plt.axhline(y=70, color='red', linestyle='--', label='70% Threshold (Survival Threat)')
plt.title('Projected Biodiversity Loss in Modeled Ecosystems (2025–2175, No Intervention)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('% Biodiversity Loss (Modeled Ecosystems)', fontsize=12)
plt.legend(title='Scenario', fontsize=10)
plt.savefig(os.path.join(FIGURES_DIR, 'total_biodiversity_loss.png'), dpi=300, bbox_inches='tight')
plt.close()

print(f"Graphs saved to '{FIGURES_DIR}'")