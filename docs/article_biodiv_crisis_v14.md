# The Biodiversity Crisis: Modeling Cascading Losses to 2175

## Abstract
Biodiversity underpins human survival, yet climate change and nuclear risks threaten its collapse. Using a Monte Carlo simulation ([GitHub: ecosystems-2175](https://github.com/BartLeunis/ecosystems-2175)), I model cascading losses across eight ecosystems—70% of global species—from 2025 to 2175 under no-intervention scenarios (Low, Mid, High). The High scenario predicts 65–70% loss, exceeding thresholds for food security (50%) and human survival (70%). This citizen science effort highlights tipping points and urges action.

## Introduction
Ecosystems like the Amazon and Oceans regulate climate, food, and health (IPBES, 2019). Yet, unmitigated stressors could erase them. This study simulates their decline, linking biodiversity loss to human risk.

## Methods
- **Model**: 100,000 iterations, 10-year steps, 8 ecosystems.
- **Parameters**: Loss rates from IPCC AR6, species weights from WWF, cascades from tipping point literature.
- **Scenarios**: Low (mitigated), Mid (current trends), High (4–6°C warming + nuclear risk).
- **Details**: See [METHODOLOGY.md](https://github.com/BartLeunis/ecosystems-2175/blob/main/METHODOLOGY.md).

## Results
The High scenario shows dire losses by 2175:

| Ecosystem           | Low (%) | Mid (%) | High (%) | 95% CI High (%) |
|---------------------|---------|---------|----------|-----------------|
| Amazon Rainforest   | 45.2    | 78.9    | 98.5     | 95.2–100        |
| Coral Reefs         | 58.3    | 89.1    | 99.8     | 97.5–100        |
| Oceans              | 47.6    | 72.4    | 88.9     | 85.3–92.4       |
| Total Modeled Loss  | 38.7    | 55.2    | 66.5     | 63.2–69.8       |

![Ecosystem Losses](https://github.com/BartLeunis/ecosystems-2175/raw/main/figures/ecosystem_loss_by_ecosystem.png)
*Figure 2: Ecosystem-specific losses across scenarios.*

![Total Loss](https://github.com/BartLeunis/ecosystems-2175/raw/main/figures/total_biodiversity_loss.png)
*Figure 3: Total modeled biodiversity loss, with human risk thresholds.*

## Discussion
- **Thresholds**: 50% loss by 2125 (High) risks food/health; 70% by 2175 threatens survival (Steffen et al., 2015).
- **Cascades**: Amazon collapse accelerates Arctic melt; Ocean loss amplifies Coral Reef decline.
- **Limits**: No intervention assumed; unmodeled ecosystems (30%) may buffer total loss.

## Conclusion
A 65–70% loss signals a crisis beyond ecology—humanity’s stake is existential. Intervention is urgent.

## References
- IPCC (2022). *AR6 WGII Report*. Chapters 2–5.
- WWF (2022). *Living Planet Report*. Biodiversity trends.
- Mora, C., et al. (2011). How many species are there on Earth? *PLoS Biology*, 9(8), e1001127. DOI: 10.1371/journal.pbio.1001127
- Fisher, R., et al. (2015). Species richness on coral reefs. *Current Biology*, 25(10), 1290–1295. DOI: 10.1016/j.cub.2015.03.034
- CAFF (2013). *Arctic Biodiversity Assessment*. Conservation of Arctic Flora and Fauna.
- Ramsar Convention Secretariat (2018). *Global Wetland Outlook*. Ramsar.
- IPBES (2019). *Global Assessment Report on Biodiversity and Ecosystem Services*. IPBES Secretariat.
- Steffen, W., et al. (2015). Planetary boundaries: Guiding human development. *Science*, 347(6223), 1259855. DOI: 10.1126/science.1259855
- Turco, R. P., et al. (1983). Nuclear winter: Global consequences. *Science*, 222(4630), 1283–1292. DOI: 10.1126/science.222.4630.1283
- Rockström, J., et al. (2009). A safe operating space for humanity. *Nature*, 461(7263), 472–475. DOI: 10.1038/461472a

*Bart Leunis, March 14, 2025*