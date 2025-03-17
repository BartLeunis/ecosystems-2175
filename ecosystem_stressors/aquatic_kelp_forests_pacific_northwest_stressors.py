from stressor_templates import *
import copy

aquatic_kelp_forests_pacific_northwest_stressors = {
    "Ocean Warming": {},
    "Sea Urchin Grazing / "Urchin Barrens"": {},
    "Water Pollution": copy.deepcopy(pollution_template),
}

# --- Ocean Warming ---
aquatic_kelp_forests_pacific_northwest_stressors["Ocean Warming"]["Metric"] = 'Sea surface temperature (SST) (°C); frequency and severity of marine heatwaves.'
aquatic_kelp_forests_pacific_northwest_stressors["Ocean Warming"]["Data Sources"] = ['Satellite data.', 'In-situ temperature loggers.', 'Climate models.', '* NOAA', '* Fisheries and Oceans Canada', '**Impact on Area:** Reduced kelp growth and survival; potential for die-offs.', '**Impact on Biodiversity:**', 'Loss of habitat.', 'Changes in community structure.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Sea Urchin Grazing (indirectly).', '**Logic Description:**  Rising ocean temperatures, especially marine heatwaves, stress kelp.']
aquatic_kelp_forests_pacific_northwest_stressors["Ocean Warming"]["Impact on Area"] = 'Reduced kelp growth and survival; potential for die-offs.'
aquatic_kelp_forests_pacific_northwest_stressors["Ocean Warming"]["Impact on Biodiversity"] = 'Loss of habitat.\nChanges in community structure.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\n**Influences (Stressors):**\nSea Urchin Grazing (indirectly).\n**Logic Description:**  Rising ocean temperatures, especially marine heatwaves, stress kelp.'
aquatic_kelp_forests_pacific_northwest_stressors["Ocean Warming"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Sea Urchin Grazing (indirectly).', '**Logic Description:**  Rising ocean temperatures, especially marine heatwaves, stress kelp.']
aquatic_kelp_forests_pacific_northwest_stressors["Ocean Warming"]["Influences"] = ['Sea Urchin Grazing (indirectly).', '**Logic Description:**  Rising ocean temperatures, especially marine heatwaves, stress kelp.']
aquatic_kelp_forests_pacific_northwest_stressors["Ocean Warming"]["Logic Description"] = '---'
aquatic_kelp_forests_pacific_northwest_stressors["Ocean Warming"]["Impact Function"] = "impact_ocean_warming_aquatic_kelp_forests_pacific_northwest"

# --- Sea Urchin Grazing / "Urchin Barrens" ---
aquatic_kelp_forests_pacific_northwest_stressors["Sea Urchin Grazing / "Urchin Barrens""]["Metric"] = 'Sea urchin density; kelp cover; sea otter abundance.'
aquatic_kelp_forests_pacific_northwest_stressors["Sea Urchin Grazing / "Urchin Barrens""]["Data Sources"] = ['Underwater surveys.', 'Research studies.', '* Government monitoring', '**Impact on Area:** Conversion of kelp forests to urchin barrens.', '**Impact on Biodiversity:**', 'Dramatic reduction in biodiversity.', 'Loss of habitat.', '**Influenced By (Stressors):**', 'Sea Otter Abundance: Sea otters are key predators.  Where otters are present and healthy, urchin populations are generally controlled. Where otters are absent or reduced, urchin barrens can form.', 'Overfishing of Other Urchin Predators.', '**Influences (Stressors):**', 'Kelp Forest Cover.', '**Logic Description:** The sea otter/urchin/kelp dynamic is crucial. While sea otter populations are generally healthier in the Pacific Northwest than in parts of California, localized urchin barrens can still occur.']
aquatic_kelp_forests_pacific_northwest_stressors["Sea Urchin Grazing / "Urchin Barrens""]["Impact on Area"] = 'Conversion of kelp forests to urchin barrens.'
aquatic_kelp_forests_pacific_northwest_stressors["Sea Urchin Grazing / "Urchin Barrens""]["Impact on Biodiversity"] = 'Dramatic reduction in biodiversity.\nLoss of habitat.\n**Influenced By (Stressors):**\nSea Otter Abundance: Sea otters are key predators.  Where otters are present and healthy, urchin populations are generally controlled. Where otters are absent or reduced, urchin barrens can form.\nOverfishing of Other Urchin Predators.\n**Influences (Stressors):**\nKelp Forest Cover.\n**Logic Description:** The sea otter/urchin/kelp dynamic is crucial. While sea otter populations are generally healthier in the Pacific Northwest than in parts of California, localized urchin barrens can still occur.'
aquatic_kelp_forests_pacific_northwest_stressors["Sea Urchin Grazing / "Urchin Barrens""]["Influenced By"] = ['Sea Otter Abundance: Sea otters are key predators.  Where otters are present and healthy, urchin populations are generally controlled. Where otters are absent or reduced, urchin barrens can form.', 'Overfishing of Other Urchin Predators.', '**Influences (Stressors):**', 'Kelp Forest Cover.', '**Logic Description:** The sea otter/urchin/kelp dynamic is crucial. While sea otter populations are generally healthier in the Pacific Northwest than in parts of California, localized urchin barrens can still occur.']
aquatic_kelp_forests_pacific_northwest_stressors["Sea Urchin Grazing / "Urchin Barrens""]["Influences"] = ['Kelp Forest Cover.', '**Logic Description:** The sea otter/urchin/kelp dynamic is crucial. While sea otter populations are generally healthier in the Pacific Northwest than in parts of California, localized urchin barrens can still occur.']
aquatic_kelp_forests_pacific_northwest_stressors["Sea Urchin Grazing / "Urchin Barrens""]["Logic Description"] = '---'
aquatic_kelp_forests_pacific_northwest_stressors["Sea Urchin Grazing / "Urchin Barrens""]["Impact Function"] = "impact_sea_urchin_grazing_/_"urchin_barrens"_aquatic_kelp_forests_pacific_northwest"

# --- Water Pollution ---
aquatic_kelp_forests_pacific_northwest_stressors["Water Pollution"]["Metric"] = 'Concentrations of pollutants (nutrients, sediments, etc.).'
aquatic_kelp_forests_pacific_northwest_stressors["Water Pollution"]["Data Sources"] = ['* Water Quality monitoring', '* Research studies', '**Impact on Area:** Reduced water quality', '**Impact on Biodiversity:**', '* Can harm kelp and other organisms.', '**Influenced By (Stressors):**', '* Runoff', '* Industrial discharge', '**Influences (Stressors):**', '* Kelp health', '* Water clarity', '**Logic Description:** Pollution from various sources.']
aquatic_kelp_forests_pacific_northwest_stressors["Water Pollution"]["Impact on Area"] = 'Reduced water quality'
aquatic_kelp_forests_pacific_northwest_stressors["Water Pollution"]["Impact on Biodiversity"] = '* Can harm kelp and other organisms.\n**Influenced By (Stressors):**\n* Runoff\n* Industrial discharge\n**Influences (Stressors):**\n* Kelp health\n* Water clarity\n**Logic Description:** Pollution from various sources.'
aquatic_kelp_forests_pacific_northwest_stressors["Water Pollution"]["Influenced By"] = ['* Runoff', '* Industrial discharge', '**Influences (Stressors):**', '* Kelp health', '* Water clarity', '**Logic Description:** Pollution from various sources.']
aquatic_kelp_forests_pacific_northwest_stressors["Water Pollution"]["Influences"] = ['* Kelp health', '* Water clarity', '**Logic Description:** Pollution from various sources.']
aquatic_kelp_forests_pacific_northwest_stressors["Water Pollution"]["Logic Description"] = '---'
aquatic_kelp_forests_pacific_northwest_stressors["Water Pollution"]["Impact Function"] = "impact_water_pollution_aquatic_kelp_forests_pacific_northwest"

