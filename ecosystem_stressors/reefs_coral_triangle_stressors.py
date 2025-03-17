from stressor_templates import *
import copy

reefs_coral_triangle_stressors = {
    "Destructive Fishing Practices": {},
    "Overfishing": copy.deepcopy(overfishing_template),
    "Water Pollution": copy.deepcopy(pollution_template),
    "Coastal Development": {},
    "Climate Change": copy.deepcopy(climate_change_template),
}

# --- Destructive Fishing Practices ---
reefs_coral_triangle_stressors["Destructive Fishing Practices"]["Metric"] = 'Frequency of blast fishing, cyanide fishing, and other destructive practices; area of reef damaged.'
reefs_coral_triangle_stressors["Destructive Fishing Practices"]["Data Sources"] = ['Underwater surveys.', 'Reports from local communities and conservation organizations.', 'Law enforcement data (often limited).', '**Impact on Area:** Direct physical damage to coral reefs.', '**Impact on Biodiversity:**', 'Coral mortality.', 'Loss of reef structure.', 'Decline of fish populations.', 'Impacts on other reef organisms.', '**Influenced By (Stressors):**', 'Poverty and Lack of Economic Opportunities.', 'Weak Law Enforcement.', 'Demand for Reef Fish (food and aquarium trade).', 'Lack of Awareness: Of the impacts of these practices.', '**Influences (Stressors):**', 'Coral Reef Structure and Health.', '**Logic Description:** Destructive fishing practices, including blast fishing (using explosives) and cyanide fishing, are *widespread* in the Coral Triangle and cause severe damage to coral reefs and their associated biodiversity.']
reefs_coral_triangle_stressors["Destructive Fishing Practices"]["Impact on Area"] = 'Direct physical damage to coral reefs.'
reefs_coral_triangle_stressors["Destructive Fishing Practices"]["Impact on Biodiversity"] = 'Coral mortality.\nLoss of reef structure.\nDecline of fish populations.\nImpacts on other reef organisms.\n**Influenced By (Stressors):**\nPoverty and Lack of Economic Opportunities.\nWeak Law Enforcement.\nDemand for Reef Fish (food and aquarium trade).\nLack of Awareness: Of the impacts of these practices.\n**Influences (Stressors):**\nCoral Reef Structure and Health.\n**Logic Description:** Destructive fishing practices, including blast fishing (using explosives) and cyanide fishing, are *widespread* in the Coral Triangle and cause severe damage to coral reefs and their associated biodiversity.'
reefs_coral_triangle_stressors["Destructive Fishing Practices"]["Influenced By"] = ['Poverty and Lack of Economic Opportunities.', 'Weak Law Enforcement.', 'Demand for Reef Fish (food and aquarium trade).', 'Lack of Awareness: Of the impacts of these practices.', '**Influences (Stressors):**', 'Coral Reef Structure and Health.', '**Logic Description:** Destructive fishing practices, including blast fishing (using explosives) and cyanide fishing, are *widespread* in the Coral Triangle and cause severe damage to coral reefs and their associated biodiversity.']
reefs_coral_triangle_stressors["Destructive Fishing Practices"]["Influences"] = ['Coral Reef Structure and Health.', '**Logic Description:** Destructive fishing practices, including blast fishing (using explosives) and cyanide fishing, are *widespread* in the Coral Triangle and cause severe damage to coral reefs and their associated biodiversity.']
reefs_coral_triangle_stressors["Destructive Fishing Practices"]["Logic Description"] = '---'

# --- Overfishing ---
reefs_coral_triangle_stressors["Overfishing"]["Metric"] = 'Fish biomass, size structure, and abundance of target species; catch per unit effort.'
reefs_coral_triangle_stressors["Overfishing"]["Data Sources"] = ['Fisheries data (often incomplete).', 'Underwater surveys.', 'Research publications.', '**Impact on Area:** Not directly applicable, but affects ecosystem structure.', '**Impact on Biodiversity:**', 'Decline of important fish species.', 'Disruption of the food web.', 'Loss of top predators.', 'Potential for algal overgrowth (if herbivores are removed).', '**Influenced By (Stressors):**', 'High Fishing Pressure: Due to large coastal populations and dependence on fishing.', 'Weak Enforcement of Fisheries Regulations.', 'Lack of Alternative Livelihoods.', '**Influences (Stressors):**', 'Algal Overgrowth.', 'Coral Reef Health.', '* Food web', '**Logic Description:** Overfishing is a major and widespread threat in the Coral Triangle, depleting fish populations and disrupting the ecological balance of reef ecosystems.']
reefs_coral_triangle_stressors["Overfishing"]["Impact on Area"] = 'Not directly applicable, but affects ecosystem structure.'
reefs_coral_triangle_stressors["Overfishing"]["Impact on Biodiversity"] = 'Decline of important fish species.\nDisruption of the food web.\nLoss of top predators.\nPotential for algal overgrowth (if herbivores are removed).\n**Influenced By (Stressors):**\nHigh Fishing Pressure: Due to large coastal populations and dependence on fishing.\nWeak Enforcement of Fisheries Regulations.\nLack of Alternative Livelihoods.\n**Influences (Stressors):**\nAlgal Overgrowth.\nCoral Reef Health.\n* Food web\n**Logic Description:** Overfishing is a major and widespread threat in the Coral Triangle, depleting fish populations and disrupting the ecological balance of reef ecosystems.'
reefs_coral_triangle_stressors["Overfishing"]["Influenced By"] = ['High Fishing Pressure: Due to large coastal populations and dependence on fishing.', 'Weak Enforcement of Fisheries Regulations.', 'Lack of Alternative Livelihoods.', '**Influences (Stressors):**', 'Algal Overgrowth.', 'Coral Reef Health.', '* Food web', '**Logic Description:** Overfishing is a major and widespread threat in the Coral Triangle, depleting fish populations and disrupting the ecological balance of reef ecosystems.']
reefs_coral_triangle_stressors["Overfishing"]["Influences"] = ['Algal Overgrowth.', 'Coral Reef Health.', '* Food web', '**Logic Description:** Overfishing is a major and widespread threat in the Coral Triangle, depleting fish populations and disrupting the ecological balance of reef ecosystems.']
reefs_coral_triangle_stressors["Overfishing"]["Logic Description"] = '---'

# --- Water Pollution ---
reefs_coral_triangle_stressors["Water Pollution"]["Metric"] = 'Concentrations of nutrients, sediments, and pollutants in coastal waters.'
reefs_coral_triangle_stressors["Water Pollution"]["Data Sources"] = ['Water quality monitoring programs (often limited).', 'Research studies.', '**Impact on Area:** Reduced water quality.', '**Impact on Biodiversity:**', 'Algal overgrowth.', 'Reduced light penetration.', 'Direct harm to corals and other organisms.', '**Influenced By (Stressors):**', 'Agricultural Runoff: Fertilizers and pesticides.', 'Deforestation: Increased sediment runoff.', 'Urban Runoff: Sewage and industrial effluent.', 'Mining Activities: Release of heavy metals and other pollutants.', 'Inadequate Waste Management.', '**Influences (Stressors):**', 'Coral Reef Health.', 'Algal Blooms.', '**Logic Description:** Pollution from various sources, including agriculture, deforestation, urbanization, and mining, degrades water quality and impacts coral reefs.']
reefs_coral_triangle_stressors["Water Pollution"]["Impact on Area"] = 'Reduced water quality.'
reefs_coral_triangle_stressors["Water Pollution"]["Impact on Biodiversity"] = 'Algal overgrowth.\nReduced light penetration.\nDirect harm to corals and other organisms.\n**Influenced By (Stressors):**\nAgricultural Runoff: Fertilizers and pesticides.\nDeforestation: Increased sediment runoff.\nUrban Runoff: Sewage and industrial effluent.\nMining Activities: Release of heavy metals and other pollutants.\nInadequate Waste Management.\n**Influences (Stressors):**\nCoral Reef Health.\nAlgal Blooms.\n**Logic Description:** Pollution from various sources, including agriculture, deforestation, urbanization, and mining, degrades water quality and impacts coral reefs.'
reefs_coral_triangle_stressors["Water Pollution"]["Influenced By"] = ['Agricultural Runoff: Fertilizers and pesticides.', 'Deforestation: Increased sediment runoff.', 'Urban Runoff: Sewage and industrial effluent.', 'Mining Activities: Release of heavy metals and other pollutants.', 'Inadequate Waste Management.', '**Influences (Stressors):**', 'Coral Reef Health.', 'Algal Blooms.', '**Logic Description:** Pollution from various sources, including agriculture, deforestation, urbanization, and mining, degrades water quality and impacts coral reefs.']
reefs_coral_triangle_stressors["Water Pollution"]["Influences"] = ['Coral Reef Health.', 'Algal Blooms.', '**Logic Description:** Pollution from various sources, including agriculture, deforestation, urbanization, and mining, degrades water quality and impacts coral reefs.']
reefs_coral_triangle_stressors["Water Pollution"]["Logic Description"] = '---'

# --- Coastal Development ---
reefs_coral_triangle_stressors["Coastal Development"]["Metric"] = 'Area of coastline developed (km or ha); population density in coastal areas.'
reefs_coral_triangle_stressors["Coastal Development"]["Data Sources"] = ['Government statistics.', 'Remote sensing data.', 'Reports from conservation organizations.', '**Impact on Area:** Habitat loss (mangroves, seagrass beds); increased sedimentation and pollution.', '**Impact on Biodiversity:**', 'Loss of critical habitats.', 'Reduced water quality.', 'Physical damage to reefs.', '**Influenced By (Stressors):**', 'Population Growth: Rapid population growth in many coastal areas.', 'Tourism Development.', 'Urbanization.', 'Infrastructure Development.', '**Influences (Stressors):**', 'Water Quality.', 'Sedimentation.', 'Habitat Loss.', '**Logic Description:** Rapid population growth and coastal development are leading to habitat loss, increased sedimentation, and pollution, impacting coral reefs.']
reefs_coral_triangle_stressors["Coastal Development"]["Impact on Area"] = 'Habitat loss (mangroves, seagrass beds); increased sedimentation and pollution.'
reefs_coral_triangle_stressors["Coastal Development"]["Impact on Biodiversity"] = 'Loss of critical habitats.\nReduced water quality.\nPhysical damage to reefs.\n**Influenced By (Stressors):**\nPopulation Growth: Rapid population growth in many coastal areas.\nTourism Development.\nUrbanization.\nInfrastructure Development.\n**Influences (Stressors):**\nWater Quality.\nSedimentation.\nHabitat Loss.\n**Logic Description:** Rapid population growth and coastal development are leading to habitat loss, increased sedimentation, and pollution, impacting coral reefs.'
reefs_coral_triangle_stressors["Coastal Development"]["Influenced By"] = ['Population Growth: Rapid population growth in many coastal areas.', 'Tourism Development.', 'Urbanization.', 'Infrastructure Development.', '**Influences (Stressors):**', 'Water Quality.', 'Sedimentation.', 'Habitat Loss.', '**Logic Description:** Rapid population growth and coastal development are leading to habitat loss, increased sedimentation, and pollution, impacting coral reefs.']
reefs_coral_triangle_stressors["Coastal Development"]["Influences"] = ['Water Quality.', 'Sedimentation.', 'Habitat Loss.', '**Logic Description:** Rapid population growth and coastal development are leading to habitat loss, increased sedimentation, and pollution, impacting coral reefs.']
reefs_coral_triangle_stressors["Coastal Development"]["Logic Description"] = '---'

# --- Climate Change ---
reefs_coral_triangle_stressors["Climate Change"]["Metric"] = 'Sea surface temperature (SST) (°C); ocean acidification (pH); frequency and intensity of tropical cyclones.'
reefs_coral_triangle_stressors["Climate Change"]["Data Sources"] = ['Climate models.', 'Oceanographic data.', 'Historical records.', '**Impact on Area:** Coral bleaching; reduced coral growth rates.', '**Impact on Biodiversity:**', 'Coral mortality (from bleaching).', 'Shifts in coral species composition.', 'Impacts on fish and invertebrate communities.', 'Increased vulnerability to disease.', '* Acidification impacts', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Coral Bleaching.', 'Ocean Acidification.', 'Storm Damage.', '**Logic Description:** Climate change, including warming waters, ocean acidification, and potentially increased storm intensity, poses a significant threat to coral reefs in the Coral Triangle.']
reefs_coral_triangle_stressors["Climate Change"]["Impact on Area"] = 'Coral bleaching; reduced coral growth rates.'
reefs_coral_triangle_stressors["Climate Change"]["Impact on Biodiversity"] = 'Coral mortality (from bleaching).\nShifts in coral species composition.\nImpacts on fish and invertebrate communities.\nIncreased vulnerability to disease.\n* Acidification impacts\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\n**Influences (Stressors):**\nCoral Bleaching.\nOcean Acidification.\nStorm Damage.\n**Logic Description:** Climate change, including warming waters, ocean acidification, and potentially increased storm intensity, poses a significant threat to coral reefs in the Coral Triangle.'
reefs_coral_triangle_stressors["Climate Change"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Coral Bleaching.', 'Ocean Acidification.', 'Storm Damage.', '**Logic Description:** Climate change, including warming waters, ocean acidification, and potentially increased storm intensity, poses a significant threat to coral reefs in the Coral Triangle.']
reefs_coral_triangle_stressors["Climate Change"]["Influences"] = ['Coral Bleaching.', 'Ocean Acidification.', 'Storm Damage.', '**Logic Description:** Climate change, including warming waters, ocean acidification, and potentially increased storm intensity, poses a significant threat to coral reefs in the Coral Triangle.']
reefs_coral_triangle_stressors["Climate Change"]["Logic Description"] = '---'

