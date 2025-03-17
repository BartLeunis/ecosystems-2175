from stressor_templates import *
import copy

aquatic_kelp_forests_south_american_stressors = {
    "Overfishing": copy.deepcopy(overfishing_template),
    "Sea Urchin Harvesting": {},
    "Climate Change": copy.deepcopy(climate_change_template),
}

# --- Overfishing ---
aquatic_kelp_forests_south_american_stressors["Overfishing"]["Metric"] = 'Abundance of key urchin predators (e.g., certain fish species, sea stars); sea urchin density; kelp cover.'
aquatic_kelp_forests_south_american_stressors["Overfishing"]["Data Sources"] = ['Fisheries data (often limited).', 'Underwater surveys.', 'Research publications.', '**Impact on Area:** Potential for urchin barren formation.', '**Impact on Biodiversity:**', 'Loss of kelp forest habitat.', 'Reduced biodiversity.', '**Influenced By (Stressors):**', 'Overfishing of Urchin Predators.', 'Demand for Seafood.', '**Influences (Stressors):**', 'Kelp Forest Cover.', '**Logic Description:** Overfishing of predators can lead to increased urchin grazing and kelp forest loss.  This is a *potential* threat, and the specific predators and dynamics may differ from the Northern Hemisphere.']
aquatic_kelp_forests_south_american_stressors["Overfishing"]["Impact on Area"] = 'Potential for urchin barren formation.'
aquatic_kelp_forests_south_american_stressors["Overfishing"]["Impact on Biodiversity"] = 'Loss of kelp forest habitat.\nReduced biodiversity.\n**Influenced By (Stressors):**\nOverfishing of Urchin Predators.\nDemand for Seafood.\n**Influences (Stressors):**\nKelp Forest Cover.\n**Logic Description:** Overfishing of predators can lead to increased urchin grazing and kelp forest loss.  This is a *potential* threat, and the specific predators and dynamics may differ from the Northern Hemisphere.'
aquatic_kelp_forests_south_american_stressors["Overfishing"]["Influenced By"] = ['Overfishing of Urchin Predators.', 'Demand for Seafood.', '**Influences (Stressors):**', 'Kelp Forest Cover.', '**Logic Description:** Overfishing of predators can lead to increased urchin grazing and kelp forest loss.  This is a *potential* threat, and the specific predators and dynamics may differ from the Northern Hemisphere.']
aquatic_kelp_forests_south_american_stressors["Overfishing"]["Influences"] = ['Kelp Forest Cover.', '**Logic Description:** Overfishing of predators can lead to increased urchin grazing and kelp forest loss.  This is a *potential* threat, and the specific predators and dynamics may differ from the Northern Hemisphere.']
aquatic_kelp_forests_south_american_stressors["Overfishing"]["Logic Description"] = '---'

# --- Sea Urchin Harvesting ---
aquatic_kelp_forests_south_american_stressors["Sea Urchin Harvesting"]["Data Sources"] = ['* Fisheries data', '**Impact on Area:** Potential for kelp forest expansion (if urchins are heavily harvested).', '**Impact on Biodiversity**:', '* Can be positive or negative.', '**Influenced By (Stressors):**', '* Demand for urchin roe (uni).', '**Influences (Stressors):**', '* Urchin populations', '* Kelp cover.', '**Logic Description**: In some areas, sea urchins are harvested for their roe (uni). This can have *complex* effects on kelp forests. It *could* reduce grazing pressure, but it also removes a component of the ecosystem.']
aquatic_kelp_forests_south_american_stressors["Sea Urchin Harvesting"]["Impact on Area"] = 'Potential for kelp forest expansion (if urchins are heavily harvested).'
aquatic_kelp_forests_south_american_stressors["Sea Urchin Harvesting"]["Influenced By"] = ['* Demand for urchin roe (uni).', '**Influences (Stressors):**', '* Urchin populations', '* Kelp cover.', '**Logic Description**: In some areas, sea urchins are harvested for their roe (uni). This can have *complex* effects on kelp forests. It *could* reduce grazing pressure, but it also removes a component of the ecosystem.']
aquatic_kelp_forests_south_american_stressors["Sea Urchin Harvesting"]["Influences"] = ['* Urchin populations', '* Kelp cover.', '**Logic Description**: In some areas, sea urchins are harvested for their roe (uni). This can have *complex* effects on kelp forests. It *could* reduce grazing pressure, but it also removes a component of the ecosystem.']

# --- Climate Change ---
aquatic_kelp_forests_south_american_stressors["Climate Change"]["Metric"] = 'Sea surface temperature (SST) (°C); ocean acidification (pH).'
aquatic_kelp_forests_south_american_stressors["Climate Change"]["Data Sources"] = ['Climate models.', 'Oceanographic data.', '**Impact on Area:**  Potential changes in kelp distribution and growth.', '**Impact on Biodiversity:**', '* Impacts to be determined', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', '**Logic Description:**  The impacts of climate change on South American kelp forests are still being researched, but warming waters and acidification are potential threats.']
aquatic_kelp_forests_south_american_stressors["Climate Change"]["Impact on Area"] = 'Potential changes in kelp distribution and growth.'
aquatic_kelp_forests_south_american_stressors["Climate Change"]["Impact on Biodiversity"] = '* Impacts to be determined\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\n**Influences (Stressors):**\n**Logic Description:**  The impacts of climate change on South American kelp forests are still being researched, but warming waters and acidification are potential threats.'
aquatic_kelp_forests_south_american_stressors["Climate Change"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', '**Logic Description:**  The impacts of climate change on South American kelp forests are still being researched, but warming waters and acidification are potential threats.']
aquatic_kelp_forests_south_american_stressors["Climate Change"]["Influences"] = ['**Logic Description:**  The impacts of climate change on South American kelp forests are still being researched, but warming waters and acidification are potential threats.']
aquatic_kelp_forests_south_american_stressors["Climate Change"]["Logic Description"] = '---'

