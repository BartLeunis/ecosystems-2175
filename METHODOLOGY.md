# Methodology Overview: Ecosystems 2175 Monte Carlo Simulation

This document outlines the methodology for the Monte Carlo simulation in `ecosystems-2175`, projecting cascading biodiversity loss across eight key ecosystems from 2025 to 2175 under no-intervention scenarios (Low, Mid, High). Developed as a citizen science effort by Bart Leunis, it aims to inform tipping point research with accessible, reproducible code.

## Model Structure
- **Type**: Monte Carlo simulation with 100,000 iterations per scenario.
- **Timeframe**: 2025–2175, in 10-year steps (15 time points).
- **Ecosystems Modeled**: 8 (Amazon Rainforest, Coral Reefs, Arctic Sea Ice, Boreal Forests, Savanna Grasslands, Wetlands, Oceans, Temperate Forests), covering ~70% of global biodiversity.
- **Output**: Annual loss fractions (0–1) per ecosystem, weighted total biodiversity loss, and visualizations.

### Simulation Steps
1. **Base Loss**: Annual ecosystem-specific loss rates drawn from a normal distribution (`stats.norm`) with scenario-specific means and a standard deviation of 0.01.
2. **Nuclear Risk**: Annual nuclear event probability (0.01) compounds over 150 years, triggering a 25% loss increase scaled by time progression.
3. **Cascading Effects**: If an ecosystem’s mean loss exceeds 50%, it amplifies linked ecosystems’ losses via predefined multipliers.
4. **Aggregation**: Losses capped at 100% per ecosystem; total biodiversity loss weighted by ecosystem species contributions.

## Key Parameters and Assumptions

### Ecosystems and Base Loss Rates
Annual loss rates (`base_loss_means`) reflect climate, nuclear, and human stressors without mitigation:

| Ecosystem           | Low  | Mid  | High | Source/Justification                                      |
|---------------------|------|------|------|-----------------------------------------------------------|
| Amazon Rainforest   | 0.03 | 0.06 | 0.09 | IPCC AR6 WGII Ch. 2: Deforestation, warming rates         |
| Coral Reefs         | 0.04 | 0.08 | 0.12 | IPCC AR6 WGII Ch. 3: Bleaching, acidification            |
| Arctic Sea Ice      | 0.03 | 0.06 | 0.09 | IPCC AR6 WGII Ch. 3: Melting under warming scenarios     |
| Boreal Forests      | 0.02 | 0.04 | 0.06 | IPCC AR6 WGII Ch. 5: Fires, permafrost thaw              |
| Savanna Grasslands  | 0.02 | 0.04 | 0.06 | WWF Living Planet: Drought, land use change              |
| Wetlands            | 0.02 | 0.05 | 0.07 | IPCC AR6 WGII Ch. 4: Drainage, sea level rise            |
| Oceans (Pelagic)    | 0.03 | 0.06 | 0.09 | IPCC AR6 WGII Ch. 3: Warming, acidification              |
| Temperate Forests   | 0.01 | 0.03 | 0.05 | IPCC AR6 WGII Ch. 5: Drought, fires (slower than tropics)|

- **Assumption**: Rates are cumulative, compounding annually; variability (σ = 0.01) reflects uncertainty in climate impacts.
- **High Scenario**: Represents unmitigated 4–6°C warming plus nuclear risk.

### Species Weights
Weights estimate each ecosystem’s contribution to global biodiversity (~10M species estimated, per Mora et al., 2011):

| Ecosystem           | Weight | Justification                                      |
|---------------------|--------|----------------------------------------------------|
| Amazon Rainforest   | 0.125  | ~1.25M species (WWF, IPCC), ~12.5% of total        |
| Coral Reefs         | 0.07   | ~700K species (25% marine, Fisher et al., 2015)    |
| Arctic Sea Ice      | 0.0075 | ~75K species (low diversity, CAFF 2013)            |
| Boreal Forests      | 0.065  | ~650K species (IPCC WGII Ch. 5)                    |
| Savanna Grasslands  | 0.06   | ~600K species (WWF Living Planet)                  |
| Wetlands            | 0.08   | ~800K species (Ramsar, IPCC WGII Ch. 4)            |
| Oceans (Pelagic)    | 0.20   | ~2M species (15–20%, Mora et al., 2011)            |
| Temperate Forests   | 0.10   | ~1M species (5–10%, IPCC WGII Ch. 5)               |

- **Total**: 0.7075 (~70% of biodiversity modeled).
- **Assumption**: Unmodeled ecosystems (e.g., deserts, tundra) contribute the remaining ~30%; weights are approximate, based on species richness estimates.

### Cascade Effects
Multipliers apply when a source ecosystem’s loss exceeds 50%:

| Source Ecosystem    | Target Ecosystem      | Multiplier | Justification                       |
|---------------------|-----------------------|------------|-------------------------------------|
| Amazon Rainforest   | Arctic Sea Ice        | 1.2        | Carbon sink loss accelerates melt  |
|                     | Coral Reefs           | 1.1        | CO2 uptake decline                 |
|                     | Wetlands              | 1.1        | Hydrological disruption            |
| Coral Reefs         | Wetlands              | 1.2        | Coastal protection loss            |
|                     | Savanna Grasslands    | 1.1        | Nutrient flow disruption           |
|                     | Oceans                | 1.1        | Marine food web collapse           |
| Arctic Sea Ice      | Amazon Rainforest     | 1.1        | Albedo feedback                    |
|                     | Boreal Forests        | 1.2        | Permafrost-carbon link             |
|                     | Coral Reefs           | 1.1        | Ocean circulation shift            |
|                     | Oceans                | 1.1        | Polar ecosystem collapse           |
| Boreal Forests      | Arctic Sea Ice        | 1.1        | Carbon release                     |
|                     | Wetlands              | 1.1        | Methane emissions                  |
|                     | Temperate Forests     | 1.1        | Climate overlap                    |
| Savanna Grasslands  | Wetlands              | 1.1        | Water cycle disruption             |
| Wetlands            | Savanna Grasslands    | 1.1        | Soil fertility decline             |
|                     | Temperate Forests     | 1.1        | Hydrological support loss          |
| Oceans              | Coral Reefs           | 1.2        | Acidification synergy              |
|                     | Arctic Sea Ice        | 1.1        | Warming feedback                   |
| Temperate Forests   | Boreal Forests        | 1.1        | Fire-climate linkage               |
|                     | Wetlands              | 1.1        | Water retention loss               |

- **Assumption**: Multipliers (1.1–1.2) reflect moderate to strong feedbacks, grounded in IPCC tipping point literature.

### Nuclear Risk
- **Annual Probability**: 0.01 (1% chance/year, speculative based on Cold War peak risks).
- **Cumulative**: Over 150 years, ~78% chance of occurrence (1 - e^(-0.01 × 150)).
- **Impact**: 25% loss increase, scaled by time (t/15), simulating ecosystem shock.
- **Source**: Inspired by nuclear winter studies (e.g., Turco et al., 1983), adjusted for long-term ecological harm.

### Human Survival Thresholds
- **50% Loss**: Food security and health risks (e.g., pollination collapse, IPBES 2019).
- **70% Loss**: Critical collapse threatening human survival (e.g., fisheries, climate regulation fail; Steffen et al., 2015).
- **Assumption**: Thresholds apply to modeled ~70% of biodiversity; total global loss would be lower but still catastrophic.

## Outputs
- **CSV**: `data/ecosystem_cascade_results.csv` (~1.3GB, 36M rows: 100K × 15 × 8 × 3).
- **Plots**: 
  - `figures/total_biodiversity_loss.png`: Total loss with 50%/70% thresholds.
  - `figures/ecosystem_loss_by_ecosystem.png`: Per-ecosystem trajectories.
  - `figures/ecosystem_loss_by_scenario.png`: Per-scenario trends.

## Limitations
- **No Intervention**: Assumes no mitigation—real-world efforts could lower losses.
- **Simplified Cascades**: Multipliers are uniform; actual feedbacks vary spatially.
- **Data Gaps**: Weights and rates are estimates; unmodeled ecosystems (e.g., deserts) omitted due to sparse data.
- **Nuclear Risk**: Highly speculative—serves as a stress test.

## References
- IPCC AR6 WGII (2022): Chapters 2–5, ecosystem-specific climate impacts.
- WWF Living Planet Report (2022): Species richness and loss trends.
- Mora et al. (2011): "How Many Species Are There on Earth?" *PLoS Biology*.
- Fisher et al. (2015): Coral reef biodiversity, *Current Biology*.
- CAFF (2013): Arctic biodiversity assessment.
- Ramsar Convention: Wetland species estimates.
- IPBES (2019): Global Assessment Report on Biodiversity.
- Steffen et al. (2015): "Planetary Boundaries," *Science*.
- Turco et al. (1983): Nuclear winter ecological impacts, *Science*.
- Rockström et al. (2009): "A Safe Operating Space for Humanity," *Nature*.

## Usage
Run `simulations/ecosystem_cascade.py` to generate data, then `simulations/graph_plots.py` for visuals. See `README.md` for setup.

*Last updated: March 14, 2025*