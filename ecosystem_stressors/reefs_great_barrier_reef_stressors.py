from stressor_templates import *
import copy

reefs_great_barrier_reef_stressors = {
    "Ocean Warming": {},
    "Ocean Acidification": {},
    "Water Pollution": copy.deepcopy(pollution_template),
    "Crown-of-Thorns Starfish (COTS) Outbreaks": {},
    "Tropical Cyclones": {},
    "Overfishing": copy.deepcopy(overfishing_template),
}

# --- Ocean Warming ---
reefs_great_barrier_reef_stressors["Ocean Warming"]["Metric"] = 'Sea surface temperature (SST) (°C); frequency and severity of marine heatwaves; Degree Heating Weeks (DHW).'
reefs_great_barrier_reef_stressors["Ocean Warming"]["Data Sources"] = ['Australian Institute of Marine Science (AIMS) Long-Term Monitoring Program.', 'Great Barrier Reef Marine Park Authority (GBRMPA) reports.', 'NOAA Coral Reef Watch.', 'Bureau of Meteorology (Australia) data.', '**Impact on Area:** Coral bleaching; reduced coral growth rates.', '**Impact on Biodiversity:**', 'Coral mortality (severe and frequent bleaching events).', 'Shifts in coral species composition.', 'Impacts on fish and invertebrate communities.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Coral Bleaching.', 'Disease Outbreaks.', '**Logic Description:** Ocean warming is the *most significant* threat to the GBR, causing widespread and increasingly frequent coral bleaching events.']
reefs_great_barrier_reef_stressors["Ocean Warming"]["Impact on Area"] = 'Coral bleaching; reduced coral growth rates.'
reefs_great_barrier_reef_stressors["Ocean Warming"]["Impact on Biodiversity"] = 'Coral mortality (severe and frequent bleaching events).\nShifts in coral species composition.\nImpacts on fish and invertebrate communities.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\n**Influences (Stressors):**\nCoral Bleaching.\nDisease Outbreaks.\n**Logic Description:** Ocean warming is the *most significant* threat to the GBR, causing widespread and increasingly frequent coral bleaching events.'
reefs_great_barrier_reef_stressors["Ocean Warming"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Coral Bleaching.', 'Disease Outbreaks.', '**Logic Description:** Ocean warming is the *most significant* threat to the GBR, causing widespread and increasingly frequent coral bleaching events.']
reefs_great_barrier_reef_stressors["Ocean Warming"]["Influences"] = ['Coral Bleaching.', 'Disease Outbreaks.', '**Logic Description:** Ocean warming is the *most significant* threat to the GBR, causing widespread and increasingly frequent coral bleaching events.']
reefs_great_barrier_reef_stressors["Ocean Warming"]["Logic Description"] = ''

# --- Ocean Acidification ---
reefs_great_barrier_reef_stressors["Ocean Acidification"]["Metric"] = 'Ocean pH; aragonite saturation state (Ωar).'
reefs_great_barrier_reef_stressors["Ocean Acidification"]["Data Sources"] = ['AIMS monitoring data.', 'Research publications.', '**Impact on Area:** Reduced calcification rates.', '**Impact on Biodiversity:**', 'Slower coral growth.', 'Weaker coral skeletons.', '**Influenced By (Stressors):**', 'Increased Atmospheric CO2.', '**Influences (Stressors):**', 'Coral growth and survival.', '**Logic Description:** Ocean acidification reduces the ability of corals to build their skeletons.']
reefs_great_barrier_reef_stressors["Ocean Acidification"]["Impact on Area"] = 'Reduced calcification rates.'
reefs_great_barrier_reef_stressors["Ocean Acidification"]["Impact on Biodiversity"] = 'Slower coral growth.\nWeaker coral skeletons.\n**Influenced By (Stressors):**\nIncreased Atmospheric CO2.\n**Influences (Stressors):**\nCoral growth and survival.\n**Logic Description:** Ocean acidification reduces the ability of corals to build their skeletons.'
reefs_great_barrier_reef_stressors["Ocean Acidification"]["Influenced By"] = ['Increased Atmospheric CO2.', '**Influences (Stressors):**', 'Coral growth and survival.', '**Logic Description:** Ocean acidification reduces the ability of corals to build their skeletons.']
reefs_great_barrier_reef_stressors["Ocean Acidification"]["Influences"] = ['Coral growth and survival.', '**Logic Description:** Ocean acidification reduces the ability of corals to build their skeletons.']
reefs_great_barrier_reef_stressors["Ocean Acidification"]["Logic Description"] = ''

# --- Water Pollution ---
reefs_great_barrier_reef_stressors["Water Pollution"]["Metric"] = 'Concentrations of nutrients (nitrogen, phosphorus), sediments, and pesticides in coastal waters.'
reefs_great_barrier_reef_stressors["Water Pollution"]["Data Sources"] = ['Queensland Government water quality monitoring programs.', 'AIMS monitoring data.', 'Research publications.', '**Impact on Area:** Reduced water quality; increased turbidity.', '**Impact on Biodiversity:**', 'Algal overgrowth.', 'Reduced light penetration.', 'Direct harm to corals and other organisms.', '* Exacerbates Crown-of-thorns Starfish outbreaks', '**Influenced By (Stressors):**', 'Agricultural Runoff (sugarcane and cattle grazing are major sources).', 'Coastal Development.', '**Influences (Stressors):**', 'Crown-of-Thorns Starfish Outbreaks.', 'Coral Bleaching (reduces resilience).', '**Logic Description:** Runoff from agriculture and coastal development carries nutrients, sediments, and pollutants into coastal waters, degrading water quality and impacting coral health.  This is a *major* and well-documented stressor on the GBR.']
reefs_great_barrier_reef_stressors["Water Pollution"]["Impact on Area"] = 'Reduced water quality; increased turbidity.'
reefs_great_barrier_reef_stressors["Water Pollution"]["Impact on Biodiversity"] = 'Algal overgrowth.\nReduced light penetration.\nDirect harm to corals and other organisms.\n* Exacerbates Crown-of-thorns Starfish outbreaks\n**Influenced By (Stressors):**\nAgricultural Runoff (sugarcane and cattle grazing are major sources).\nCoastal Development.\n**Influences (Stressors):**\nCrown-of-Thorns Starfish Outbreaks.\nCoral Bleaching (reduces resilience).\n**Logic Description:** Runoff from agriculture and coastal development carries nutrients, sediments, and pollutants into coastal waters, degrading water quality and impacting coral health.  This is a *major* and well-documented stressor on the GBR.'
reefs_great_barrier_reef_stressors["Water Pollution"]["Influenced By"] = ['Agricultural Runoff (sugarcane and cattle grazing are major sources).', 'Coastal Development.', '**Influences (Stressors):**', 'Crown-of-Thorns Starfish Outbreaks.', 'Coral Bleaching (reduces resilience).', '**Logic Description:** Runoff from agriculture and coastal development carries nutrients, sediments, and pollutants into coastal waters, degrading water quality and impacting coral health.  This is a *major* and well-documented stressor on the GBR.']
reefs_great_barrier_reef_stressors["Water Pollution"]["Influences"] = ['Crown-of-Thorns Starfish Outbreaks.', 'Coral Bleaching (reduces resilience).', '**Logic Description:** Runoff from agriculture and coastal development carries nutrients, sediments, and pollutants into coastal waters, degrading water quality and impacting coral health.  This is a *major* and well-documented stressor on the GBR.']
reefs_great_barrier_reef_stressors["Water Pollution"]["Logic Description"] = ''

# --- Crown-of-Thorns Starfish (COTS) Outbreaks ---
reefs_great_barrier_reef_stressors["Crown-of-Thorns Starfish (COTS) Outbreaks"]["Metric"] = 'Density of COTS (number per hectare).'
reefs_great_barrier_reef_stressors["Crown-of-Thorns Starfish (COTS) Outbreaks"]["Data Sources"] = ['AIMS Long-Term Monitoring Program.', 'GBRMPA reports.', '**Impact on Area:** Direct predation on corals.', '**Impact on Biodiversity:**', 'Significant coral mortality during outbreaks.', 'Changes in reef structure.', '**Influenced By (Stressors):**', 'Nutrient Enrichment (from land runoff - promotes larval survival).', 'Overfishing (removal of COTS predators - less well-established).', '**Influences (Stressors):**', 'Coral Cover.', '**Logic Description:** Outbreaks of crown-of-thorns starfish (COTS), a coral-eating starfish, are a major cause of coral decline on the GBR.  These outbreaks are thought to be linked to nutrient enrichment from land runoff.']
reefs_great_barrier_reef_stressors["Crown-of-Thorns Starfish (COTS) Outbreaks"]["Impact on Area"] = 'Direct predation on corals.'
reefs_great_barrier_reef_stressors["Crown-of-Thorns Starfish (COTS) Outbreaks"]["Impact on Biodiversity"] = 'Significant coral mortality during outbreaks.\nChanges in reef structure.\n**Influenced By (Stressors):**\nNutrient Enrichment (from land runoff - promotes larval survival).\nOverfishing (removal of COTS predators - less well-established).\n**Influences (Stressors):**\nCoral Cover.\n**Logic Description:** Outbreaks of crown-of-thorns starfish (COTS), a coral-eating starfish, are a major cause of coral decline on the GBR.  These outbreaks are thought to be linked to nutrient enrichment from land runoff.'
reefs_great_barrier_reef_stressors["Crown-of-Thorns Starfish (COTS) Outbreaks"]["Influenced By"] = ['Nutrient Enrichment (from land runoff - promotes larval survival).', 'Overfishing (removal of COTS predators - less well-established).', '**Influences (Stressors):**', 'Coral Cover.', '**Logic Description:** Outbreaks of crown-of-thorns starfish (COTS), a coral-eating starfish, are a major cause of coral decline on the GBR.  These outbreaks are thought to be linked to nutrient enrichment from land runoff.']
reefs_great_barrier_reef_stressors["Crown-of-Thorns Starfish (COTS) Outbreaks"]["Influences"] = ['Coral Cover.', '**Logic Description:** Outbreaks of crown-of-thorns starfish (COTS), a coral-eating starfish, are a major cause of coral decline on the GBR.  These outbreaks are thought to be linked to nutrient enrichment from land runoff.']
reefs_great_barrier_reef_stressors["Crown-of-Thorns Starfish (COTS) Outbreaks"]["Logic Description"] = ''

# --- Tropical Cyclones ---
reefs_great_barrier_reef_stressors["Tropical Cyclones"]["Metric"] = 'Frequency and intensity of tropical cyclones (categories 3-5).'
reefs_great_barrier_reef_stressors["Tropical Cyclones"]["Data Sources"] = ['* Bureau of Meteorology (Australia) data', '* Historical records.', '**Impact on Area:** Physical damage of coral reefs', '**Impact on Biodiversity:**', '* Coral Mortality', '* Loss of Reef Structure', '**Influenced By (Stressors):**', '* Climate change', '* Sea Surface Temperature', '**Influences (Stressors):**', '* Reef Structure', '**Logic Description:** Strong cyclones can cause significant physical damage to the reef structure.']
reefs_great_barrier_reef_stressors["Tropical Cyclones"]["Impact on Area"] = 'Physical damage of coral reefs'
reefs_great_barrier_reef_stressors["Tropical Cyclones"]["Impact on Biodiversity"] = '* Coral Mortality\n* Loss of Reef Structure\n**Influenced By (Stressors):**\n* Climate change\n* Sea Surface Temperature\n**Influences (Stressors):**\n* Reef Structure\n**Logic Description:** Strong cyclones can cause significant physical damage to the reef structure.'
reefs_great_barrier_reef_stressors["Tropical Cyclones"]["Influenced By"] = ['* Climate change', '* Sea Surface Temperature', '**Influences (Stressors):**', '* Reef Structure', '**Logic Description:** Strong cyclones can cause significant physical damage to the reef structure.']
reefs_great_barrier_reef_stressors["Tropical Cyclones"]["Influences"] = ['* Reef Structure', '**Logic Description:** Strong cyclones can cause significant physical damage to the reef structure.']
reefs_great_barrier_reef_stressors["Tropical Cyclones"]["Logic Description"] = ''

# --- Overfishing ---
reefs_great_barrier_reef_stressors["Overfishing"]["Data Sources"] = ['* Fisheries data', '* Underwater surveys', '**Impact on Area:** N/A', '**Impact on Biodiversity:**', '* Loss of species, trophic structure', '**Influenced By (Stressors):**', '* Fishing pressure.', '**Influences (Stressors):**', '* Food web.', "**Logic Description:** Overfishing can impact, although it's more regulated here than other areas."]
reefs_great_barrier_reef_stressors["Overfishing"]["Impact on Area"] = 'N/A'
reefs_great_barrier_reef_stressors["Overfishing"]["Impact on Biodiversity"] = "* Loss of species, trophic structure\n**Influenced By (Stressors):**\n* Fishing pressure.\n**Influences (Stressors):**\n* Food web.\n**Logic Description:** Overfishing can impact, although it's more regulated here than other areas."
reefs_great_barrier_reef_stressors["Overfishing"]["Influenced By"] = ['* Fishing pressure.', '**Influences (Stressors):**', '* Food web.', "**Logic Description:** Overfishing can impact, although it's more regulated here than other areas."]
reefs_great_barrier_reef_stressors["Overfishing"]["Influences"] = ['* Food web.', "**Logic Description:** Overfishing can impact, although it's more regulated here than other areas."]
reefs_great_barrier_reef_stressors["Overfishing"]["Logic Description"] = ''

