# Ecosystems 2175: Biodiversity Loss Simulation

A Monte Carlo simulation projecting cascading biodiversity loss across eight ecosystems from 2025–2175 under no-intervention scenarios. Built as a citizen science project by Bart Leunis.

## Setup
- **Requirements**: Python 3.13, `numpy`, `scipy`, `pandas`, `matplotlib`, `seaborn`.
- Install: `pip install -r requirements.txt` (create this file if needed).

## Running the Simulation
1. **Generate Data**:
   ```bash
   cd simulations
   python3 ecosystem_cascade_test.py
Outputs: data/ecosystem_cascade_results.csv (~1.3GB, not stored in repo due to size).
Note: Uses fixed seed (42) for reproducibility—rerun to regenerate identical data.

2. **Plot Results**:
    ```bash
    python3 graph_plots.py

    Outputs: figures/ with three PNGs (total loss, by ecosystem, by scenario).

## Methodology
See METHODOLOGY.md for assumptions, parameters, and references.

## Notes
data/ecosystem_cascade_results.csv is in .gitignore—too large for GitHub. Reproduce it locally with the above command.
Covers ~70% of biodiversity; High scenario shows 65–70% loss, exceeding human survival thresholds (50%, 70%).
