# The Biodiversity Crisis: Modeling Cascading Losses to 2175

## Abstract
Biodiversity sustains humanity, yet climate change and nuclear risks threaten its collapse. Using a Monte Carlo simulation ([GitHub: ecosystems-2175](https://github.com/BartLeunis/ecosystems-2175)), I model cascading losses across 13 ecosystems—covering ~97.5% of global species—from 2025 to 2175 under no-intervention scenarios (Low, Mid, High). The High scenario predicts 66.5% total loss (CI 51.2–70.8%), exceeding the 50% food/health threshold by 2125 (64.3%) and nearing the 70% survival threat by 2175. Even Low hits 60.3% (CI 20.0–71.8%). This citizen science effort exposes tipping points and demands urgent action.

## Introduction
Ecosystems like the Amazon, Oceans, and Freshwater regulate climate, food, and health (IPBES, 2019). Unmitigated stressors—warming, nuclear risk—could unravel them. This study simulates their decline, linking biodiversity loss to human survival, now with near-full global coverage.

## Methods
- **Model**: 100,000 iterations, 10-year steps, 13 ecosystems.
- **Parameters**: Loss rates from IPCC AR6, species weights from WWF and Mora et al. (2011), cascades from tipping point literature.
- **Scenarios**: Low (mitigated), Mid (current trends), High (4–6°C warming + nuclear risk).
- **Ecosystems**: Expanded from 8 (~70%) to 13 (~97.5%), adding Deserts, Tundra, etc., with noted data uncertainty.
- **Details**: See [METHODOLOGY.md](https://github.com/BartLeunis/ecosystems-2175/blob/main/METHODOLOGY.md).

## Results
High scenario losses by 2175 (full coverage):

| Ecosystem           | Low (%) | Mid (%) | High (%) | 95% CI High (%) |
|---------------------|---------|---------|----------|-----------------|
| Amazon Rainforest   | 78.4    | 86.4    | 90.0     | 90.0–90.0       |
| Coral Reefs         | 79.1    | 83.3    | 87.7     | 59.8–95.0       |
| Oceans              | 60.3    | 63.0    | 65.3     | 29.8–75.0       |
| Freshwater          | 70.7    | 80.0    | 80.0     | 80.0–80.0       |
| Tundra              | 61.5    | 68.6    | 70.0     | 70.0–70.0       |
| Total Loss          | 60.3    | 64.1    | 66.5     | 51.2–70.8       |

![Ecosystem Losses](https://github.com/BartLeunis/ecosystems-2175/raw/main/figures/ecosystem_loss_by_ecosystem.png)
*Figure 1: Ecosystem-specific losses across scenarios.*

![Total Loss](https://github.com/BartLeunis/ecosystems-2175/raw/main/figures/total_biodiversity_loss.png)
*Figure 2: Total biodiversity loss (97.5% coverage), with human risk thresholds.*

- **High**: 66.5% (CI 51.2–70.8%) by 2175, 64.3% by 2125.
- **Mid**: 64.1% (CI 41.2–70.6%), 59.4% by 2125.
- **Low**: 60.3% (CI 20.0–71.8%), 54.8% by 2125.

## Discussion
- **Thresholds**: All scenarios exceed 50% by 2125 (Low: 54.8%, Mid: 59.4%, High: 64.3%)—food/health risks loom. High’s 66.5% (70.8% upper CI) nears 70% survival threat by 2175 (Steffen et al., 2015).
- **Cascades**: Amazon collapse (to savanna) slows Wetlands loss; Freshwater decline amplifies Wetlands risk. Transformations temper extremes but don’t avert crisis.
- **Confidence Intervals**: Wide CIs (e.g., Low: 20.0–71.8%) reflect nuclear risk and sparse data for new ecosystems (Deserts, Tundra). Tail risks could hit 70% sooner.
- **Limits**: No intervention assumed. New ecosystems (e.g., Freshwater) use coarser data (IPCC AR6, WWF 2022)—uncertainty noted.

## Conclusion
A 60–66.5% loss by 2175, with 50% crossed by 2125 across all scenarios, signals an escalating crisis. Food/health risks are imminent; survival threats lurk in the tail risks (e.g., High CI 70.8%). Intervention isn’t optional—it’s existential.

## References
- IPCC (2022). *AR6 WGII Report*. Chapters 2–5. Intergovernmental Panel on Climate Change.
- WWF (2022). *Living Planet Report*. Biodiversity trends. World Wide Fund for Nature.
- Mora, C., et al. (2011). How many species are there on Earth and in the ocean? *PLoS Biology*, 9(8), e1001127. DOI: 10.1371/journal.pbio.1001127
- Fisher, R., et al. (2015). Species richness on coral reefs and the pursuit of convergent global estimates. *Current Biology*, 25(10), 1290–1295. DOI: 10.1016/j.cub.2015.03.034
- CAFF (2013). *Arctic Biodiversity Assessment*. Conservation of Arctic Flora and Fauna.
- Ramsar Convention Secretariat (2018). *Global Wetland Outlook*. Ramsar Convention on Wetlands.
- IPBES (2019). *Global Assessment Report on Biodiversity and Ecosystem Services*. Intergovernmental Science-Policy Platform on Biodiversity and Ecosystem Services.
- Steffen, W., et al. (2015). Planetary boundaries: Guiding human development on a changing planet. *Science*, 347(6223), 1259855. DOI: 10.1126/science.1259855
- Turco, R. P., et al. (1983). Nuclear winter: Global consequences of multiple nuclear explosions. *Science*, 222(4630), 1283–1292. DOI: 10.1126/science.222.4630.1283
- Rockström, J., et al. (2009). A safe operating space for humanity. *Nature*, 461(7263), 472–475. DOI: 10.1038/461472a

*Bart Leunis, March 14, 2025*