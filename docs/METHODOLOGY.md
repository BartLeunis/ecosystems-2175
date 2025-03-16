# Methodology Document

## Overview
This document outlines the methodology for simulating the loss of ecosystem function across 13 global ecosystems (Amazon Rainforest, Coral Reefs, Arctic Sea Ice, Boreal Forests, Savanna Grasslands, Wetlands, Oceans, Temperate Forests, Deserts, Tundra, Montane, Freshwater, and Polar) from 2025 to 2175. The model integrates base loss rates, transformation dynamics, cascade effects, and stochastic shocks to estimate biodiversity loss under Low, Mid, and High climate scenarios, with and without shock events. The primary output is the percentage loss of ecosystem function, weighted by species diversity, to assess global biodiversity impacts.

## Objectives
- Quantify the progressive loss of ecosystem function over 150 years (2025–2175).
- Model the transformation of ecosystems (e.g., Amazon Rainforest to Savanna Grasslands) and its impact on biodiversity.
- Account for cascade effects and stochastic shocks to reflect ecological interdependencies and climate variability.
- Provide total biodiversity loss estimates with 95% confidence intervals (CI) to inform risk thresholds (50% for food/health risks, 70% for survival threats).

## Methodology

### 1. Ecosystem Definition and Baseline Data
- **Ecosystems**: 13 distinct ecosystems are modeled, each with a baseline fraction remaining in 2175 (`final_baselines`), representing the minimum expected ecosystem extent under climate change.
  - Example: Amazon Rainforest (0.05), Coral Reefs (0.01), Savanna Grasslands (0.40).
- **Species Weights**: Each ecosystem is assigned a weight based on approximate biodiversity contribution (e.g., Amazon Rainforest: 0.25, Coral Reefs: 0.15, Oceans: 0.20), summing to 1.0. These are proxies for species richness and ecological importance, subject to refinement with empirical data.
- **Data Sources**: Baseline assumptions are informed by IPCC AR6 reports, Nobre et al. (2016) for Amazon deforestation, and Hoegh-Guldberg et al. (2018) for coral bleaching projections.

### 2. Loss Simulation
- **Time Frame**: Annual time steps from 2025 to 2175 (150 years), with 10,000 iterations for statistical robustness.
- **Base Loss Rates**: Each ecosystem has scenario-specific annual loss rates drawn from a t-distribution (df=3) with means and standard deviations:
  - Low: 0.001–0.006, Mid: 0.003–0.012, High: 0.005–0.04 (e.g., Amazon Rainforest: 0.005 High).
  - Standard deviation: 0.001 across all ecosystems.
- **Cumulative Loss**: Loss accumulates annually, capped at `1.0 - final_baselines` to reflect maximum feasible loss (e.g., 95% for Amazon Rainforest).

### 3. Transformation Dynamics
- **Transformation Targets**: Certain ecosystems transform into others when lost (e.g., Amazon Rainforest → Savanna Grasslands, Coral Reefs → Oceans), reflecting ecological succession or degradation.
- **Biodiversity Density Ratios**: Transformation offsets are scaled by ratios of species density (e.g., Amazon Rainforest: 1.0, Savanna Grasslands: 0.128), reducing the biodiversity gain in the target ecosystem.
- **Time-Based Cutoff**: Offsets are applied only while the source ecosystem has not reached its maximum loss (`1.0 - final_baselines`). Once fully transformed (e.g., Amazon at 95% by 2100), the target ecosystem (e.g., Savanna Grasslands) accumulates loss at its own base rate, adjusted by cascades and shocks.
- **Implementation**: The offset is subtracted from the target ecosystem’s loss, clipped to [0, 1], ensuring no negative loss.

### 4. Cascade Effects
- **Interdependencies**: Loss in one ecosystem amplifies loss in connected ecosystems via multipliers (e.g., Amazon Rainforest → Wetlands: 1.05, Coral Reefs → Oceans: 1.1).
- **Application**: Cascades are applied annually after base loss and transformation, ensuring cumulative amplification without exceeding maximum loss.

### 5. Stochastic Shocks
- **Probability**: 2% annual chance of a shock event, affecting all ecosystems.
- **Magnitude**: ±0.05 for most ecosystems, ±0.15 for Coral Reefs and Arctic Sea Ice to reflect higher vulnerability.
- **Type**: Randomly positive (recovery) or negative (exacerbation), logged for analysis.
- **Impact**: Shocks adjust the annual loss rate, integrated into the cumulative loss.

### 6. Total Biodiversity Loss
- **Weighted Aggregation**: Total loss is the sum of each ecosystem’s loss multiplied by its species weight, capped at 100%.
- **Confidence Intervals**: 95% CI calculated using the 2.5th and 97.5th percentiles across iterations.
- **Thresholds**: 50% triggers food/health risk warnings, 70% triggers survival threat warnings.

### 7. Visualization
- **Total Loss Plot**: Line graph with shaded 95% CI, comparing No Shock vs. With Shock across Low (green), Mid (orange), and High (red) scenarios, saved as `total_biodiversity_loss_with_shocks.png`.
- **Ecosystem Breakdown**: Bar chart for 2175 High With-Shocks scenario, with hatched bars indicating transformed ecosystems, saved as `ecosystem_breakdown_2175_high_shock.png`.
- **Ecosystem-Specific Trajectories**: 4x4 grid of line graphs, each showing loss over time (2025–2175) per ecosystem across scenarios, with 95% CI and 50%/90% thresholds, saved as `ecosystem_specific_loss_trajectories.png`.

### 8. Validation and Assumptions
- **Validation**: Model outputs are cross-checked with literature (e.g., 70–90% coral loss by 2100, 40–50% Amazon loss by 2100). Discrepancies (e.g., 99% coral loss by 2050) suggest tuning opportunities.
- **Assumptions**:
  - Linear base loss rates with stochastic variation.
  - Transformation offsets cease at maximum source loss, ignoring partial overlaps.
  - No recovery mechanisms (future enhancement).
  - Species weights are approximate, pending empirical refinement.

### 9. Limitations
- **Simplifications**: Ignores adaptation, policy interventions, or non-climate stressors (e.g., pollution).
- **Data Gaps**: Biodiversity density ratios and weights lack precise global data.
- **Sensitivity**: High sensitivity to base rates and cascade multipliers; small changes can shift outcomes significantly.

### 10. Future Enhancements
- Incorporate recovery probabilities post-shock.
- Refine species weights with IUCN or biomass data.
- Add overlapping transformation losses for smoother transitions.
- Increase shock variability (e.g., 1% chance of 50% loss).

## Implementation
- **Language**: Python 3.x with NumPy, SciPy, Pandas, Matplotlib, and Seaborn.
- **Directory Structure**:
  - `data/`: Stores CSV outputs (e.g., `ecosystem_cascade_results_with_shock.csv`).
  - `figures/`: Stores PNG plots (e.g., `total_biodiversity_loss_with_shocks.png`).
- **Random Seed**: 42 for reproducibility.
- **Output**: Debug logs, CSV files, and PNG visualizations.

## Contributors
- Developed with assistance from Grok 3 (xAI), iteratively refined with user feedback.

## Version History
- **v1.0**: Initial model with base losses and cascades.
- **v2.0**: Added transformation offsets and shocks.
- **v3.0**: Implemented time-based transformation cutoff (March 2025), adjusted base rates, and enhanced visualizations.
