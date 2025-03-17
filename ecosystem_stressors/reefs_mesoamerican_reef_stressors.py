from stressor_templates import *
import copy

reefs_mesoamerican_reef_stressors = {
    "Overfishing": copy.deepcopy(overfishing_template),
    "Coastal Development": {},
    "Water Pollution": copy.deepcopy(pollution_template),
    "Climate Change": copy.deepcopy(climate_change_template),
    "Invasive Species": copy.deepcopy(invasive_species_template),
}

# --- Overfishing ---
reefs_mesoamerican_reef_stressors["Overfishing"]["Metric"] = 'Fish biomass, size structure, and abundance of key species (e.g., groupers, snappers, parrotfish).'
reefs_mesoamerican_reef_stressors["Overfishing"]["Data Sources"] = ['Fisheries data (often limited and unreliable).', 'Underwater surveys (conducted by research organizations and conservation groups).', 'Research publications.', '**Impact on Area:** Not directly applicable, but affects ecosystem structure.', '**Impact on Biodiversity:**', 'Decline of important fish species.', 'Disruption of the food web (e.g., loss of herbivores can lead to algal overgrowth).', 'Loss of top predators.', '**Influenced By (Stressors):**', 'High Fishing Pressure: Due to local dependence on fishing and tourism.', 'Weak Enforcement of Fisheries Regulations.', 'Lack of Alternative Livelihoods.', '**Influences (Stressors):**', 'Algal Overgrowth (if herbivores are removed).', 'Coral Reef Health.', '**Logic Description:** Overfishing is a major problem in the Mesoamerican Reef, depleting populations of important fish species and disrupting the food web.']
reefs_mesoamerican_reef_stressors["Overfishing"]["Impact on Area"] = 'Not directly applicable, but affects ecosystem structure.'
reefs_mesoamerican_reef_stressors["Overfishing"]["Impact on Biodiversity"] = 'Decline of important fish species.\nDisruption of the food web (e.g., loss of herbivores can lead to algal overgrowth).\nLoss of top predators.\n**Influenced By (Stressors):**\nHigh Fishing Pressure: Due to local dependence on fishing and tourism.\nWeak Enforcement of Fisheries Regulations.\nLack of Alternative Livelihoods.\n**Influences (Stressors):**\nAlgal Overgrowth (if herbivores are removed).\nCoral Reef Health.\n**Logic Description:** Overfishing is a major problem in the Mesoamerican Reef, depleting populations of important fish species and disrupting the food web.'
reefs_mesoamerican_reef_stressors["Overfishing"]["Influenced By"] = ['High Fishing Pressure: Due to local dependence on fishing and tourism.', 'Weak Enforcement of Fisheries Regulations.', 'Lack of Alternative Livelihoods.', '**Influences (Stressors):**', 'Algal Overgrowth (if herbivores are removed).', 'Coral Reef Health.', '**Logic Description:** Overfishing is a major problem in the Mesoamerican Reef, depleting populations of important fish species and disrupting the food web.']
reefs_mesoamerican_reef_stressors["Overfishing"]["Influences"] = ['Algal Overgrowth (if herbivores are removed).', 'Coral Reef Health.', '**Logic Description:** Overfishing is a major problem in the Mesoamerican Reef, depleting populations of important fish species and disrupting the food web.']
reefs_mesoamerican_reef_stressors["Overfishing"]["Logic Description"] = '---'

# --- Coastal Development ---
reefs_mesoamerican_reef_stressors["Coastal Development"]["Metric"] = 'Area of coastline developed (km or ha); tourism intensity (number of visitors); infrastructure development (e.g., hotels, marinas).'
reefs_mesoamerican_reef_stressors["Coastal Development"]["Data Sources"] = ['Government statistics (tourism, construction).', 'Remote sensing data.', 'Reports from conservation organizations.', '**Impact on Area:** Habitat loss (mangroves, seagrass beds); increased sedimentation and pollution.', '**Impact on Biodiversity:**', 'Loss of critical habitats (nursery grounds for fish).', 'Reduced water quality.', 'Physical damage to reefs (from anchors, construction).', '**Influenced By (Stressors):**', 'Tourism Development: Rapid growth in tourism in some areas.', 'Population Growth: Increased demand for housing and infrastructure.', 'Government Policies: Land-use planning and zoning.', '**Influences (Stressors):**', 'Water Quality.', 'Sedimentation.', 'Habitat Loss.', '**Logic Description:** Rapid coastal development, driven by tourism and population growth, is leading to habitat loss, increased sedimentation, and pollution, impacting coral reefs.']
reefs_mesoamerican_reef_stressors["Coastal Development"]["Impact on Area"] = 'Habitat loss (mangroves, seagrass beds); increased sedimentation and pollution.'
reefs_mesoamerican_reef_stressors["Coastal Development"]["Impact on Biodiversity"] = 'Loss of critical habitats (nursery grounds for fish).\nReduced water quality.\nPhysical damage to reefs (from anchors, construction).\n**Influenced By (Stressors):**\nTourism Development: Rapid growth in tourism in some areas.\nPopulation Growth: Increased demand for housing and infrastructure.\nGovernment Policies: Land-use planning and zoning.\n**Influences (Stressors):**\nWater Quality.\nSedimentation.\nHabitat Loss.\n**Logic Description:** Rapid coastal development, driven by tourism and population growth, is leading to habitat loss, increased sedimentation, and pollution, impacting coral reefs.'
reefs_mesoamerican_reef_stressors["Coastal Development"]["Influenced By"] = ['Tourism Development: Rapid growth in tourism in some areas.', 'Population Growth: Increased demand for housing and infrastructure.', 'Government Policies: Land-use planning and zoning.', '**Influences (Stressors):**', 'Water Quality.', 'Sedimentation.', 'Habitat Loss.', '**Logic Description:** Rapid coastal development, driven by tourism and population growth, is leading to habitat loss, increased sedimentation, and pollution, impacting coral reefs.']
reefs_mesoamerican_reef_stressors["Coastal Development"]["Influences"] = ['Water Quality.', 'Sedimentation.', 'Habitat Loss.', '**Logic Description:** Rapid coastal development, driven by tourism and population growth, is leading to habitat loss, increased sedimentation, and pollution, impacting coral reefs.']
reefs_mesoamerican_reef_stressors["Coastal Development"]["Logic Description"] = '---'

# --- Water Pollution ---
reefs_mesoamerican_reef_stressors["Water Pollution"]["Metric"] = 'Concentrations of nutrients (nitrogen, phosphorus), sediments, and pesticides in coastal waters.'
reefs_mesoamerican_reef_stressors["Water Pollution"]["Data Sources"] = ['Water quality monitoring programs (often limited).', 'Research studies.', '**Impact on Area:** Reduced water quality.', '**Impact on Biodiversity:**', 'Algal overgrowth, smothering corals.', 'Reduced light penetration.', 'Direct harm to corals and other organisms.', '**Influenced By (Stressors):**', 'Agricultural Runoff: Fertilizers and pesticides from agriculture.', 'Deforestation: Increased sediment runoff.', 'Urban Runoff: Sewage and stormwater.', 'Inadequate Wastewater Treatment.', '**Influences (Stressors):**', 'Coral Reef Health.', 'Algal Blooms.', '**Logic Description:** Runoff from agriculture, deforestation, and urban areas carries pollutants (nutrients, sediments, pesticides) into coastal waters, degrading water quality and impacting coral reefs.']
reefs_mesoamerican_reef_stressors["Water Pollution"]["Impact on Area"] = 'Reduced water quality.'
reefs_mesoamerican_reef_stressors["Water Pollution"]["Impact on Biodiversity"] = 'Algal overgrowth, smothering corals.\nReduced light penetration.\nDirect harm to corals and other organisms.\n**Influenced By (Stressors):**\nAgricultural Runoff: Fertilizers and pesticides from agriculture.\nDeforestation: Increased sediment runoff.\nUrban Runoff: Sewage and stormwater.\nInadequate Wastewater Treatment.\n**Influences (Stressors):**\nCoral Reef Health.\nAlgal Blooms.\n**Logic Description:** Runoff from agriculture, deforestation, and urban areas carries pollutants (nutrients, sediments, pesticides) into coastal waters, degrading water quality and impacting coral reefs.'
reefs_mesoamerican_reef_stressors["Water Pollution"]["Influenced By"] = ['Agricultural Runoff: Fertilizers and pesticides from agriculture.', 'Deforestation: Increased sediment runoff.', 'Urban Runoff: Sewage and stormwater.', 'Inadequate Wastewater Treatment.', '**Influences (Stressors):**', 'Coral Reef Health.', 'Algal Blooms.', '**Logic Description:** Runoff from agriculture, deforestation, and urban areas carries pollutants (nutrients, sediments, pesticides) into coastal waters, degrading water quality and impacting coral reefs.']
reefs_mesoamerican_reef_stressors["Water Pollution"]["Influences"] = ['Coral Reef Health.', 'Algal Blooms.', '**Logic Description:** Runoff from agriculture, deforestation, and urban areas carries pollutants (nutrients, sediments, pesticides) into coastal waters, degrading water quality and impacting coral reefs.']
reefs_mesoamerican_reef_stressors["Water Pollution"]["Logic Description"] = '---'

# --- Climate Change ---
reefs_mesoamerican_reef_stressors["Climate Change"]["Metric"] = 'SST, Ocean Acidification, storm intensity.'
reefs_mesoamerican_reef_stressors["Climate Change"]["Data Sources"] = ['* Climate models.', '* Oceanographic data.', '**Impact on Area:** Coral Bleaching', '**Impact on Biodiversity:**', '* Coral mortality.', '* Shifts in species', '* Acidification impacts.', '**Influenced By (Stressors):**', '* Global GHG emissions', '**Influences (Stressors):**', '* Coral Bleaching', '* Ocean Acidification', '* Storm intensity', '**Logic Description:**  Warming waters, acidification, and potentially stronger storms impact.']
reefs_mesoamerican_reef_stressors["Climate Change"]["Impact on Area"] = 'Coral Bleaching'
reefs_mesoamerican_reef_stressors["Climate Change"]["Impact on Biodiversity"] = '* Coral mortality.\n* Shifts in species\n* Acidification impacts.\n**Influenced By (Stressors):**\n* Global GHG emissions\n**Influences (Stressors):**\n* Coral Bleaching\n* Ocean Acidification\n* Storm intensity\n**Logic Description:**  Warming waters, acidification, and potentially stronger storms impact.'
reefs_mesoamerican_reef_stressors["Climate Change"]["Influenced By"] = ['* Global GHG emissions', '**Influences (Stressors):**', '* Coral Bleaching', '* Ocean Acidification', '* Storm intensity', '**Logic Description:**  Warming waters, acidification, and potentially stronger storms impact.']
reefs_mesoamerican_reef_stressors["Climate Change"]["Influences"] = ['* Coral Bleaching', '* Ocean Acidification', '* Storm intensity', '**Logic Description:**  Warming waters, acidification, and potentially stronger storms impact.']
reefs_mesoamerican_reef_stressors["Climate Change"]["Logic Description"] = '---'

# --- Invasive Species ---
reefs_mesoamerican_reef_stressors["Invasive Species"]["Metric"] = 'Abundance and distribution of lionfish (and other invasive species, if relevant).'
reefs_mesoamerican_reef_stressors["Invasive Species"]["Data Sources"] = ['Underwater surveys.', 'Research studies.', 'Lionfish removal programs.', '**Impact on Area:**  Indirect - affects the native fish populations.', '**Impact on Biodiversity:**', 'Predation on native fish and invertebrates.', 'Competition with native predators.', '**Influenced By (Stressors):**', 'Introduction through the aquarium trade (likely initial introduction).', 'Lack of Natural Predators: In the Caribbean.', '**Influences (Stressors):**', 'Native Fish Populations.', '**Logic Description:** The invasive lionfish, a voracious predator with no natural predators in the Atlantic/Caribbean, is a major threat to reef fish populations in the Mesoamerican Reef.']
reefs_mesoamerican_reef_stressors["Invasive Species"]["Impact on Area"] = 'Indirect - affects the native fish populations.'
reefs_mesoamerican_reef_stressors["Invasive Species"]["Impact on Biodiversity"] = 'Predation on native fish and invertebrates.\nCompetition with native predators.\n**Influenced By (Stressors):**\nIntroduction through the aquarium trade (likely initial introduction).\nLack of Natural Predators: In the Caribbean.\n**Influences (Stressors):**\nNative Fish Populations.\n**Logic Description:** The invasive lionfish, a voracious predator with no natural predators in the Atlantic/Caribbean, is a major threat to reef fish populations in the Mesoamerican Reef.'
reefs_mesoamerican_reef_stressors["Invasive Species"]["Influenced By"] = ['Introduction through the aquarium trade (likely initial introduction).', 'Lack of Natural Predators: In the Caribbean.', '**Influences (Stressors):**', 'Native Fish Populations.', '**Logic Description:** The invasive lionfish, a voracious predator with no natural predators in the Atlantic/Caribbean, is a major threat to reef fish populations in the Mesoamerican Reef.']
reefs_mesoamerican_reef_stressors["Invasive Species"]["Influences"] = ['Native Fish Populations.', '**Logic Description:** The invasive lionfish, a voracious predator with no natural predators in the Atlantic/Caribbean, is a major threat to reef fish populations in the Mesoamerican Reef.']
reefs_mesoamerican_reef_stressors["Invasive Species"]["Logic Description"] = '---'

