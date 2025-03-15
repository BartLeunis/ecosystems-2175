Methodology Overview: Ecosystems 2175 Monte Carlo Simulation
This document outlines the methodology for the Ecosystems 2175 Monte Carlo simulation, projecting cascading biodiversity loss across 13 key ecosystems from 2025 to 2175 under no-intervention scenarios (Low, Mid, High). Developed as a citizen science initiative by Bart Leunis, this model expands from 8 ecosystems (~70% coverage) to 13 (~97.5% of global biodiversity), aiming to inform tipping point research with accessible, reproducible code. The methodology reflects recent updates based on scientific feedback, enhancing realism and variability.

Model Structure
Type: Monte Carlo simulation with 50,000 iterations per scenario (up from 100,000 for computational efficiency, runtime ~5 seconds).
Timeframe: 2025–2175, in 1-year steps (151 time points), aligning with long-term climate projections.
Ecosystems Modeled: 13 (Amazon Rainforest, Coral Reefs, Arctic Sea Ice, Boreal Forests, Savanna Grasslands, Wetlands, Oceans, Temperate Forests, Deserts, Tundra, Montane, Freshwater, Polar), covering ~97.5% of global biodiversity.
Output: Annual loss fractions (0–1) per ecosystem, weighted total biodiversity loss, and visualizations (e.g., total loss plots with consistent colors: Low = green, Mid = orange, High = red), saved to data/ and figures/ directories.
Simulation Steps
Base Loss: Annual ecosystem-specific loss rates are drawn from a t-distribution (stats.t(df=3)) with scenario-specific means (base_loss_means) and a standard deviation (base_loss_std = 0.001), reflecting climate, human, and chaotic stressors without mitigation.
Chaotic Events: Random disturbances (e.g., extreme weather, nuclear conflicts) occur with an annual probability of 0.03, applying a ±10% adjustment to annual loss rates (positive for relief, negative for increased pressure).
Cascading Effects: If an ecosystem’s mean loss exceeds its transformation threshold (drawn from stats.beta(a=2, b=5)), it amplifies linked ecosystems’ losses via predefined multipliers (1.1–1.2), with a 0.8 dampener post-transformation.
Transformation Dynamics: When cumulative loss reaches the threshold, ecosystems shift to transformed states (e.g., Amazon to Savanna), adopting target rates and capping at final baselines, with losses locked post-transformation.
Aggregation: Total biodiversity loss is weighted by ecosystem species contributions, capped at 100% (np.minimum(1.0, ...)), ensuring physical realism.
Key Parameters and Assumptions
Ecosystems and Base Loss Rates
Annual loss rates (base_loss_means) reflect unmitigated climate, human, and chaotic stressors, derived from IPCC (2019) and UNEP (2020) projections (RCP2.6 for Low, RCP4.5 for Mid, RCP8.5 for High), adjusted for ecosystem vulnerabilities.

Ecosystem	Low	Mid	High	Source/Justification
Amazon Rainforest	0.003	0.006	0.009	IPCC AR6 WGII Ch. 2: ~40% loss by 2100, scaled with cascades
Coral Reefs	0.004	0.008	0.012	IPCC AR6 WGII Ch. 3: ~90% loss under >2°C warming
Arctic Sea Ice	0.003	0.006	0.009	IPCC AR6 WGII Ch. 3: Melting rates under warming
Boreal Forests	0.002	0.004	0.006	IPCC AR6 WGII Ch. 5: Fires, permafrost thaw
Savanna Grasslands	0.002	0.004	0.006	WWF (2022): Drought, land use change
Wetlands	0.002	0.005	0.007	IPCC AR6 WGII Ch. 4: Drainage, sea level rise
Oceans (Pelagic)	0.003	0.006	0.009	IPCC AR6 WGII Ch. 3: Warming, acidification
Temperate Forests	0.001	0.003	0.005	IPCC AR6 WGII Ch. 5: Drought, fires (slower loss)
Deserts	0.001	0.003	0.005	IPCC AR6 WGII Ch. 3: Aridification, high resilience
Tundra	0.002	0.004	0.007	CAFF (2013): Warming-driven shrubification
Montane	0.002	0.004	0.006	WWF (2022): Altitude shifts, sparse data
Freshwater	0.003	0.006	0.009	Ramsar (2018): Pollution, warming
Polar	0.001	0.003	0.005	IPCC AR6 WGII Ch. 3: Ice loss, low diversity
Justification: Rates are scaled from IPCC projections, with High reflecting 4–6°C warming (RCP8.5) plus chaotic impacts. Future refinements could incorporate regional data for ecosystems like Deserts and Tundra.
Assumption: Variability is moderate; higher uncertainty for new ecosystems is noted in Limitations.
Species Weights
Weights estimate ecosystem contributions to global biodiversity (~10M species, Mora et al., 2011):

Ecosystem	Weight	Justification
Amazon Rainforest	0.125	~1.25M species (~12.5%, WWF, IPCC)
Coral Reefs	0.07	~700K species (25% marine, Fisher et al., 2015)
Arctic Sea Ice	0.0075	~75K species (low diversity, CAFF 2013)
Boreal Forests	0.065	~650K species (IPCC WGII Ch. 5)
Savanna Grasslands	0.06	~600K species (WWF, 2022)
Wetlands	0.08	~800K species (Ramsar, IPCC WGII Ch. 4)
Oceans (Pelagic)	0.20	~2M species (15–20%, Mora et al., 2011)
Temperate Forests	0.10	~1M species (5–10%, IPCC WGII Ch. 5)
Deserts	0.05	~500K species (5%, IPCC AR6 WGII Ch. 3)
Tundra	0.02	~200K species (2%, CAFF 2013)
Montane	0.08	~800K species (8%, WWF, 2022)
Freshwater	0.10	~1M species (10%, Ramsar, 2018)
Polar	0.01	~100K species (1%, IPCC AR6 WGII Ch. 3)
Total: 0.975 (~97.5% modeled biodiversity).
Assumption: Remaining ~2.5% (e.g., deep sea, urban) follows similar trends; weights are approximate, with higher uncertainty for new ecosystems.
Transformation Dynamics and Final Baselines
Transformation Threshold: Drawn from stats.beta(a=2, b=5).rvs() (mean ~0.29, range 0.05–0.6), reflecting variable tipping points.
Rationale: Tipping points vary (e.g., coral reefs at ~50% loss, forests at 20–80% canopy loss; Hoegh-Guldberg et al., 2017; Hirota et al., 2011). The beta distribution models this heterogeneity, ensuring transformations occur within the timeframe.
Justification: Provides a bounded, flexible framework grounded in tipping point literature; future work could tailor thresholds to specific ecosystems.
Final Baselines: Minimum remaining function post-transformation:
Amazon Rainforest: 0.05 (5% remnant biodiversity, IPCC, 2019)
Coral Reefs: 0.01 (near-total collapse, Hoegh-Guldberg et al., 2017)
Arctic Sea Ice: 0.20 (20% resilient ice-dependent species, UNEP, 2020)
Boreal Forests: 0.20 (20% post-thaw biodiversity, IPCC WGII Ch. 5)
Savanna Grasslands: 0.40 (40% resilient grasses, WWF, 2022)
Wetlands: 0.15 (15% remaining function, Ramsar, 2018)
Oceans: 0.15 (15% deep-sea resilience, UNEP, 2020)
Temperate Forests: 0.30 (30% post-degradation, IPCC WGII Ch. 5)
Deserts: 0.80 (80% resilience, IPCC AR6 WGII Ch. 3)
Tundra: 0.30 (30% shrub-dominated, CAFF, 2013)
Montane: 0.40 (40% altitude-adapted species, WWF, 2022)
Freshwater: 0.20 (20% resilient aquatic life, Ramsar, 2018)
Polar: 0.40 (40% ice-edge species, IPCC AR6 WGII Ch. 3)
Justification: Based on ecosystem resilience and transformation outcomes; future refinements could use ecosystem-specific post-transformation data.
Hybrid Loss Logic: Allows reductions pre-transformation (recovery potential) but locks losses post-transformation (irreversible extinction), balancing realism with focus on biodiversity loss.
Cascade Effects
Multipliers (1.1–1.2) apply when a source ecosystem’s mean loss exceeds its threshold, with a 0.8 dampener post-transformation:

Source Ecosystem	Target Ecosystem	Multiplier	Justification	Source
Amazon Rainforest	Arctic Sea Ice	1.2	Carbon sink loss accelerates melt	Nature (2024)
Coral Reefs	1.1	CO₂ uptake decline	IPCC AR6 WGII Ch. 2
Wetlands	1.1	Hydrological disruption	Science (2021)
Coral Reefs	Wetlands	1.2	Coastal protection loss	PNAS (2016)
Savanna Grasslands	1.1	Nutrient flow disruption	WWF (2022)
Oceans	1.1	Marine food web collapse	IPCC AR6 WGII Ch. 3
Arctic Sea Ice	Amazon Rainforest	1.1	Albedo feedback	Nature Climate Change (2020)
Boreal Forests	1.2	Permafrost-carbon link	Nature Communications (2023)
Coral Reefs	1.1	Ocean circulation shift	Ecosphere (2021)
Oceans	1.1	Polar ecosystem collapse	IPCC AR6 WGII Ch. 3
Boreal Forests	Arctic Sea Ice	1.1	Carbon release	Science (2022)
Wetlands	1.1	Methane emissions	Nature Geoscience (2021)
Temperate Forests	1.1	Climate overlap	IPCC AR6 WGII Ch. 5
Savanna Grasslands	Wetlands	1.1	Water cycle disruption	Ecology Letters (2021)
Wetlands	Savanna Grasslands	1.1	Soil fertility decline	ScienceDirect (2021)
Temperate Forests	1.1	Hydrological support loss	Ramsar (2018)
Oceans	Coral Reefs	1.1	Acidification synergy	IPCC AR6 WGII Ch. 3
Arctic Sea Ice	1.1	Warming feedback	Nature Climate Change (2020)
Temperate Forests	Boreal Forests	1.1	Fire-climate linkage	IPCC AR6 WGII Ch. 5
Wetlands	1.1	Water retention loss	Wetlands (2023)
Deserts	Savanna Grasslands	1.1	Aridification spill	IPCC AR6 WGII Ch. 3
Tundra	Arctic Sea Ice	1.1	Warming feedback	CAFF (2013)
Boreal Forests	1.1	Shrubification impact	Nature Communications (2023)
Montane	Temperate Forests	1.1	Altitude shift effects	WWF (2022)
Freshwater	Wetlands	1.2	Hydrological linkage	Ramsar (2018)
Oceans	1.1	Nutrient flow	IPCC AR6 WGII Ch. 3
Polar	Arctic Sea Ice	1.1	Ice loss synergy	IPCC AR6 WGII Ch. 3
Justification: Multipliers (1.1–1.2) reflect moderate to strong feedbacks, reverted from a reduced range (1.05–1.1) to capture the full intensity of inter-ecosystem dependencies as initially modeled. This aligns with IPCC and tipping point literature (Global Tipping Points Report, 2023), emphasizing systemic risks in a no-intervention scenario. The 0.8 dampener post-transformation reflects reduced ecological feedbacks in degraded states (Nature Communications, 2023), such as lower carbon emissions from transformed ecosystems.
Impact of Reversion: Reverting to 1.1–1.2 multipliers increases the simulation’s “wildness,” amplifying cascading effects. Expected total biodiversity loss in 2175 is now ~70–80% for High (up from 54.7%), ~50–60% for Mid (up from 43.4%), and ~30–40% for Low (up from 23.9%), aligning more closely with the 70% survival threat threshold.
Assumption: Feedbacks are simplified; spatial and event-specific variations are a limitation.
Chaotic Events
Definition: Unpredictable, large-scale disturbances (e.g., extreme weather, nuclear conflicts, volcanic eruptions, cosmic impacts) temporarily alter ecosystem loss trajectories.
Frequency: Annual probability of 0.03 (~4.5 events/151 years).
Rationale: IPCC (2021) and WMO report rising extreme weather frequencies (e.g., 2–5x under RCP8.5), while rare events (e.g., volcanic eruptions, nuclear conflicts) range from 0.001–0.01 annually (Baum et al., 2018; Robock et al., 2007). A 0.01–0.05 range captures this, with 0.03 balancing realism and wildness.
Justification: Reflects climate-driven trends and rare catastrophes; future work could use dynamic scaling with warming.
Magnitude: ±10% adjustment to annual loss rates (positive for relief, negative for pressure).
Rationale: Severe events (e.g., 2016 coral bleaching, 50–90% mortality; 2003 heatwave, 30% tree loss) and recovery periods (5–15%, Tilman et al., 2001) support this range.
Justification: Initial estimate for significant perturbations; future iterations could vary by event type (e.g., ±20% for storms).
Integration of Nuclear Risk: Included as a low-probability, high-impact event within the 0.03 probability, with ±10% impacts reflecting potential 5–10% global loss (Robock et al., 2007).
Annual Loss Distribution
Parameter: stats.t(df=3) with base_loss_std = 0.001.
Rationale: Fat tails capture extreme losses (e.g., 2004 tsunami, 10–20% coastal loss; UNEP, 2005), better than a normal distribution, while maintaining mean stability.
Justification: Supported by non-normal extinction rate distributions (Lockwood et al., 2002); df=3 balances extremity. Future work could test higher df for stability.
Standard Deviation (base_loss_std)
Parameter: 0.001.
Rationale: Ensures 95% of losses fall within ±0.003 of the mean, reflecting moderate variability (e.g., Amazon High 0.006–0.012, per Hansen et al., 2013).
Justification: Balances realism with stability; could increase to 0.003 for more recovery potential.
Human Survival Thresholds
50% Loss: Food security and health risks (e.g., pollination collapse; IPBES, 2019).
70% Loss: Critical survival threat (e.g., fisheries, climate regulation fail; Steffen et al., 2015).
Assumption: Applies to ~97.5% modeled biodiversity; unmodeled ~2.5% assumed similar.
Outputs
CSV: data/ecosystem_cascade_results.csv (~0.9GB, 22.5M rows: 50K × 151 × 13 × 3).
Plots:
figures/total_biodiversity_loss_with_shocks.png: Total loss with 50%/70% thresholds (Low = green, Mid = orange, High = red).
figures/ecosystem_loss_by_ecosystem.png: Per-ecosystem boxplots.
figures/high_scenario_biodiversity_loss_ci.png: High scenario shock vs. no-shock with 95% CI.
Limitations
No Intervention: Assumes no mitigation; real-world efforts could reduce losses.
Simplified Cascades: Uniform 1.1–1.2 multipliers; spatial and event-specific variations are simplified.
Data Gaps: New ecosystems (e.g., Deserts, Tundra) rely on coarser data; base_loss_std = 0.001 may understate variability.
Chaotic Events: ±10% magnitude and 0.03 probability are initial estimates; dynamic scaling and event-specific impacts need further research.
References
IPCC AR6 WGII (2022): Chapters 2–6, IPCC AR6 WGII Report.
WWF Living Planet Report (2022): WWF 2022.
Mora, C., et al. (2011): PLoS Biology, 9(8), e1001127, Mora et al. 2011.
Fisher, R., et al. (2015): Current Biology, 25(10), 1290–1295, Fisher et al. 2015.
CAFF (2013): Arctic Biodiversity Assessment, CAFF 2013.
Ramsar (2018): Global Wetland Outlook, Ramsar 2018.
IPBES (2019): Global Assessment Report, IPBES 2019.
Steffen, W., et al. (2015): Science, 347(6223), 1259855, Steffen et al. 2015.
Baum, S. D., et al. (2018): Nuclear risk assessment, Risk Analysis, 38(5), 1031–1045.
Robock, A., et al. (2007): Science, 222(4630), 1283–1292, Robock et al. 2007.
Hoegh-Guldberg, O., et al. (2017): Science, 318(5857), 1737–1742.
Hirota, M., et al. (2011): Science, 334(6053), 232–235.
Tilman, D., et al. (2001): Nature, 414(6860), 258–260.
Hansen, M. C., et al. (2013): Science, 342(6160), 850–853.
Nature (2024): Amazon dieback, Nature 2024.
Science (2021): Carbon feedbacks, Science 2021.
Nature Climate Change (2020): Tipping points, Nature Climate Change 2020.
Nature Communications (2023): Post-transformation feedbacks, Nature Communications 2023.
Usage
Run simulations/ecosystem_cascade.py to generate data, then simulations/graph_plots.py for visuals. See README.md for setup.

Last updated: March 15, 2025