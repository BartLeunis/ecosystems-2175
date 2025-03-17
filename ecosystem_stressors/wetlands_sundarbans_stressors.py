from stressor_templates import *
import copy

wetlands_sundarbans_stressors = {
    "Sea Level Rise": {},
    "Salinity Intrusion": {},
    "Climate Change": copy.deepcopy(climate_change_template),
    "Pollution": copy.deepcopy(pollution_template),
    "Overexploitation of Resources": {},
    "Cyclone Frequency and Intensity": {},
    "Reduced Freshwater Flow": {},
    "Habitat Availability": {},
    "Water Quality": {},
    "Wildlife Health": {},
    "Coastal Erosion": {},
    "Sedimentation": {},
    "Freshwater Availability": {},
}

# --- Sea Level Rise ---
wetlands_sundarbans_stressors["Sea Level Rise"]["Metric"] = 'Relative sea level rise (mm/year); rate of land subsidence (mm/year).'
wetlands_sundarbans_stressors["Sea Level Rise"]["Data Sources"] = ['Tide gauge data (from Bangladesh and India).', 'Satellite altimetry.', 'Research studies on subsidence.', '* IPCC Reports', '**Impact on Area:**', '*Major* loss of land area due to inundation. The Sundarbans is *extremely* vulnerable to sea level rise.', 'Increased salinity intrusion into freshwater areas.', '* Coastal Erosion', '**Impact on Biodiversity:**', 'Loss of mangrove habitat (mangroves are the defining feature of the Sundarbans).', 'Impacts on the Bengal tiger population (loss of habitat, increased human-wildlife conflict).', 'Impacts on other wildlife (e.g., deer, crocodiles, birds, fish).', 'Changes in species distributions.', '**Influenced By (Stressors):**', 'Sundarbans - Climate Change: Global warming leading to thermal expansion of water and melting of glaciers/ice sheets.', 'Local Land Subsidence: Can exacerbate the effects of sea level rise.', '**Influences (Stressors):**', 'Sundarbans - Salinity Intrusion.', 'Sundarbans - Habitat Availability.', '**Logic Description:** The Sundarbans, a low-lying delta region, is one of the most vulnerable places on Earth to sea level rise.  Inundation and increased salinity are major threats to the mangrove ecosystem and its biodiversity.']
wetlands_sundarbans_stressors["Sea Level Rise"]["Impact on Area"] = ''
wetlands_sundarbans_stressors["Sea Level Rise"]["Impact on Biodiversity"] = 'Loss of mangrove habitat (mangroves are the defining feature of the Sundarbans).\nImpacts on the Bengal tiger population (loss of habitat, increased human-wildlife conflict).\nImpacts on other wildlife (e.g., deer, crocodiles, birds, fish).\nChanges in species distributions.\n**Influenced By (Stressors):**\nSundarbans - Climate Change: Global warming leading to thermal expansion of water and melting of glaciers/ice sheets.\nLocal Land Subsidence: Can exacerbate the effects of sea level rise.\n**Influences (Stressors):**\nSundarbans - Salinity Intrusion.\nSundarbans - Habitat Availability.\n**Logic Description:** The Sundarbans, a low-lying delta region, is one of the most vulnerable places on Earth to sea level rise.  Inundation and increased salinity are major threats to the mangrove ecosystem and its biodiversity.'
wetlands_sundarbans_stressors["Sea Level Rise"]["Influenced By"] = ['Sundarbans - Climate Change: Global warming leading to thermal expansion of water and melting of glaciers/ice sheets.', 'Local Land Subsidence: Can exacerbate the effects of sea level rise.', '**Influences (Stressors):**', 'Sundarbans - Salinity Intrusion.', 'Sundarbans - Habitat Availability.', '**Logic Description:** The Sundarbans, a low-lying delta region, is one of the most vulnerable places on Earth to sea level rise.  Inundation and increased salinity are major threats to the mangrove ecosystem and its biodiversity.']
wetlands_sundarbans_stressors["Sea Level Rise"]["Influences"] = ['Sundarbans - Salinity Intrusion.', 'Sundarbans - Habitat Availability.', '**Logic Description:** The Sundarbans, a low-lying delta region, is one of the most vulnerable places on Earth to sea level rise.  Inundation and increased salinity are major threats to the mangrove ecosystem and its biodiversity.']
wetlands_sundarbans_stressors["Sea Level Rise"]["Logic Description"] = '---'

# --- Salinity Intrusion ---
wetlands_sundarbans_stressors["Salinity Intrusion"]["Metric"] = 'Salinity levels in water and soil (parts per thousand - ppt).'
wetlands_sundarbans_stressors["Salinity Intrusion"]["Data Sources"] = ['Water quality monitoring data (Bangladesh and India).', 'Research studies.', '**Impact on Area:** Changes in the distribution of different mangrove species (some are more salt-tolerant than others).', '**Impact on Biodiversity:**', 'Impacts on freshwater-dependent species.', 'Changes in plant communities.', 'Impacts on fisheries.', '**Influenced By (Stressors):**', 'Sundarbans - Sea Level Rise', 'Sundarbans - Reduced Freshwater Flow: Upstream water diversions and dams on rivers that feed the Sundarbans (e.g., the Ganges).', '* Sundarbans - Climate Change', '**Influences (Stressors):**', 'Sundarbans - Water Quality.', 'Sundarbans - Habitat Availability.', '* Sundarbans - Freshwater Availability', '**Logic Description:** Sea level rise and reduced freshwater flow from rivers lead to increased salinity intrusion, impacting both the mangrove ecosystem and human populations who depend on freshwater resources.']
wetlands_sundarbans_stressors["Salinity Intrusion"]["Impact on Area"] = 'Changes in the distribution of different mangrove species (some are more salt-tolerant than others).'
wetlands_sundarbans_stressors["Salinity Intrusion"]["Impact on Biodiversity"] = 'Impacts on freshwater-dependent species.\nChanges in plant communities.\nImpacts on fisheries.\n**Influenced By (Stressors):**\nSundarbans - Sea Level Rise\nSundarbans - Reduced Freshwater Flow: Upstream water diversions and dams on rivers that feed the Sundarbans (e.g., the Ganges).\n* Sundarbans - Climate Change\n**Influences (Stressors):**\nSundarbans - Water Quality.\nSundarbans - Habitat Availability.\n* Sundarbans - Freshwater Availability\n**Logic Description:** Sea level rise and reduced freshwater flow from rivers lead to increased salinity intrusion, impacting both the mangrove ecosystem and human populations who depend on freshwater resources.'
wetlands_sundarbans_stressors["Salinity Intrusion"]["Influenced By"] = ['Sundarbans - Sea Level Rise', 'Sundarbans - Reduced Freshwater Flow: Upstream water diversions and dams on rivers that feed the Sundarbans (e.g., the Ganges).', '* Sundarbans - Climate Change', '**Influences (Stressors):**', 'Sundarbans - Water Quality.', 'Sundarbans - Habitat Availability.', '* Sundarbans - Freshwater Availability', '**Logic Description:** Sea level rise and reduced freshwater flow from rivers lead to increased salinity intrusion, impacting both the mangrove ecosystem and human populations who depend on freshwater resources.']
wetlands_sundarbans_stressors["Salinity Intrusion"]["Influences"] = ['Sundarbans - Water Quality.', 'Sundarbans - Habitat Availability.', '* Sundarbans - Freshwater Availability', '**Logic Description:** Sea level rise and reduced freshwater flow from rivers lead to increased salinity intrusion, impacting both the mangrove ecosystem and human populations who depend on freshwater resources.']
wetlands_sundarbans_stressors["Salinity Intrusion"]["Logic Description"] = '---'

# --- Climate Change ---
wetlands_sundarbans_stressors["Climate Change"]["Metric"] = 'Temperature, Precipitation, Cyclone intensity'
wetlands_sundarbans_stressors["Climate Change"]["Data Sources"] = ['* Climate models', '* Historical Records', '**Impact on Area:** Indirect - sea level rise, etc.', '**Impact on Biodiversity:**', '* Increased stress, species shifts', '**Influenced By (Stressors):**', '* Global GHG', '**Influences (Stressors):**', '* Sundarbans - Sea Level Rise', '* Sundarbans - Cyclone Frequency and Intensity', '* Sundarbans - Reduced Freshwater Flow', '**Logic Description:** Climate change drives multiple stressors.']
wetlands_sundarbans_stressors["Climate Change"]["Impact on Area"] = 'Indirect - sea level rise, etc.'
wetlands_sundarbans_stressors["Climate Change"]["Impact on Biodiversity"] = '* Increased stress, species shifts\n**Influenced By (Stressors):**\n* Global GHG\n**Influences (Stressors):**\n* Sundarbans - Sea Level Rise\n* Sundarbans - Cyclone Frequency and Intensity\n* Sundarbans - Reduced Freshwater Flow\n**Logic Description:** Climate change drives multiple stressors.'
wetlands_sundarbans_stressors["Climate Change"]["Influenced By"] = ['* Global GHG', '**Influences (Stressors):**', '* Sundarbans - Sea Level Rise', '* Sundarbans - Cyclone Frequency and Intensity', '* Sundarbans - Reduced Freshwater Flow', '**Logic Description:** Climate change drives multiple stressors.']
wetlands_sundarbans_stressors["Climate Change"]["Influences"] = ['* Sundarbans - Sea Level Rise', '* Sundarbans - Cyclone Frequency and Intensity', '* Sundarbans - Reduced Freshwater Flow', '**Logic Description:** Climate change drives multiple stressors.']
wetlands_sundarbans_stressors["Climate Change"]["Logic Description"] = '---'

# --- Pollution ---
wetlands_sundarbans_stressors["Pollution"]["Metric"] = 'Concentrations of pollutants (e.g., heavy metals, oil, plastics) in water, sediment, and biota.'
wetlands_sundarbans_stressors["Pollution"]["Data Sources"] = ['Water quality monitoring data.', 'Research studies.', '**Impact on Area:** Degradation of water quality.', '**Impact on Biodiversity:**', 'Toxic effects on wildlife.', 'Impacts on fisheries.', 'Impacts on human health.', '**Influenced By (Stressors):**', 'Industrial Discharge: From industries in Bangladesh and India.', 'Shipping Activities: Oil spills and discharge.', 'Agricultural Runoff', 'Untreated Sewage', '* Tourism', '**Influences (Stressors):**', 'Sundarbans - Water Quality.', '*  Sundarbans - Wildlife Health.', '**Logic Description:** Pollution from various sources degrades water quality and impacts the ecosystem.']
wetlands_sundarbans_stressors["Pollution"]["Impact on Area"] = 'Degradation of water quality.'
wetlands_sundarbans_stressors["Pollution"]["Impact on Biodiversity"] = 'Toxic effects on wildlife.\nImpacts on fisheries.\nImpacts on human health.\n**Influenced By (Stressors):**\nIndustrial Discharge: From industries in Bangladesh and India.\nShipping Activities: Oil spills and discharge.\nAgricultural Runoff\nUntreated Sewage\n* Tourism\n**Influences (Stressors):**\nSundarbans - Water Quality.\n*  Sundarbans - Wildlife Health.\n**Logic Description:** Pollution from various sources degrades water quality and impacts the ecosystem.'
wetlands_sundarbans_stressors["Pollution"]["Influenced By"] = ['Industrial Discharge: From industries in Bangladesh and India.', 'Shipping Activities: Oil spills and discharge.', 'Agricultural Runoff', 'Untreated Sewage', '* Tourism', '**Influences (Stressors):**', 'Sundarbans - Water Quality.', '*  Sundarbans - Wildlife Health.', '**Logic Description:** Pollution from various sources degrades water quality and impacts the ecosystem.']
wetlands_sundarbans_stressors["Pollution"]["Influences"] = ['Sundarbans - Water Quality.', '*  Sundarbans - Wildlife Health.', '**Logic Description:** Pollution from various sources degrades water quality and impacts the ecosystem.']
wetlands_sundarbans_stressors["Pollution"]["Logic Description"] = '---'

# --- Overexploitation of Resources ---
wetlands_sundarbans_stressors["Overexploitation of Resources"]["Metric"] = 'Fish catches; timber harvesting rates; honey collection rates.'
wetlands_sundarbans_stressors["Overexploitation of Resources"]["Data Sources"] = ['* Fisheries data.', 'Forestry data.', 'Research studies.', '**Impact on Area:** Depletion of natural resources.', '**Impact on Biodiversity:**', '* Decline in fish populations.', '* Loss of mangrove trees (due to illegal logging).', '* Impacts on wildlife that depend on those resources.', '**Influenced By (Stressors):**', '* Population growth', '* Poverty', '* Lack of alternative livelihoods.', '**Influences (Stressors):**', '* Resource availability', '**Logic Description:** Unsustainable harvesting of fish, timber, and other resources depletes stocks and impacts the ecosystem.']
wetlands_sundarbans_stressors["Overexploitation of Resources"]["Impact on Area"] = 'Depletion of natural resources.'
wetlands_sundarbans_stressors["Overexploitation of Resources"]["Impact on Biodiversity"] = '* Decline in fish populations.\n* Loss of mangrove trees (due to illegal logging).\n* Impacts on wildlife that depend on those resources.\n**Influenced By (Stressors):**\n* Population growth\n* Poverty\n* Lack of alternative livelihoods.\n**Influences (Stressors):**\n* Resource availability\n**Logic Description:** Unsustainable harvesting of fish, timber, and other resources depletes stocks and impacts the ecosystem.'
wetlands_sundarbans_stressors["Overexploitation of Resources"]["Influenced By"] = ['* Population growth', '* Poverty', '* Lack of alternative livelihoods.', '**Influences (Stressors):**', '* Resource availability', '**Logic Description:** Unsustainable harvesting of fish, timber, and other resources depletes stocks and impacts the ecosystem.']
wetlands_sundarbans_stressors["Overexploitation of Resources"]["Influences"] = ['* Resource availability', '**Logic Description:** Unsustainable harvesting of fish, timber, and other resources depletes stocks and impacts the ecosystem.']
wetlands_sundarbans_stressors["Overexploitation of Resources"]["Logic Description"] = '---'

# --- Cyclone Frequency and Intensity ---
wetlands_sundarbans_stressors["Cyclone Frequency and Intensity"]["Metric"] = 'Number of cyclones making landfall; wind speeds; storm surge height.'
wetlands_sundarbans_stressors["Cyclone Frequency and Intensity"]["Data Sources"] = ['Meteorological data (Bangladesh and India).', 'Historical records.', '**Impact on Area:**', '* Coastal erosion.', '* Flooding.', '* Damage to infrastructure.', '* Salinization', '**Impact on Biodiversity:**', 'Damage to mangrove forests.', 'Wildlife mortality.', 'Habitat loss.', '**Influenced By (Stressors):**', '*  Sundarbans - Climate Change', '**Influences (Stressors):**', '*  Sundarbans - Coastal Erosion.', '* Many', '**Logic Description:** The Sundarbans is highly vulnerable to cyclones, and climate change may increase their frequency and intensity.']
wetlands_sundarbans_stressors["Cyclone Frequency and Intensity"]["Impact on Area"] = ''
wetlands_sundarbans_stressors["Cyclone Frequency and Intensity"]["Impact on Biodiversity"] = 'Damage to mangrove forests.\nWildlife mortality.\nHabitat loss.\n**Influenced By (Stressors):**\n*  Sundarbans - Climate Change\n**Influences (Stressors):**\n*  Sundarbans - Coastal Erosion.\n* Many\n**Logic Description:** The Sundarbans is highly vulnerable to cyclones, and climate change may increase their frequency and intensity.'
wetlands_sundarbans_stressors["Cyclone Frequency and Intensity"]["Influenced By"] = ['*  Sundarbans - Climate Change', '**Influences (Stressors):**', '*  Sundarbans - Coastal Erosion.', '* Many', '**Logic Description:** The Sundarbans is highly vulnerable to cyclones, and climate change may increase their frequency and intensity.']
wetlands_sundarbans_stressors["Cyclone Frequency and Intensity"]["Influences"] = ['*  Sundarbans - Coastal Erosion.', '* Many', '**Logic Description:** The Sundarbans is highly vulnerable to cyclones, and climate change may increase their frequency and intensity.']
wetlands_sundarbans_stressors["Cyclone Frequency and Intensity"]["Logic Description"] = '---'

# --- Reduced Freshwater Flow ---
wetlands_sundarbans_stressors["Reduced Freshwater Flow"]["Metric"] = 'Water flow rates in the rivers that feed the Sundarbans (e.g., the Ganges).'
wetlands_sundarbans_stressors["Reduced Freshwater Flow"]["Data Sources"] = ['Hydrological data (Bangladesh and India).', '**Impact on Area:**', '* Increased salinity intrusion.', '* Reduced sediment deposition (which helps maintain the delta).', '**Impact on Biodiversity:**', '* Impacts on freshwater-dependent species.', '* Changes in plant communities.', '**Influenced By (Stressors):**', '* Upstream water diversions and dams.', '*  Sundarbans - Climate Change', '**Influences (Stressors):**', '* Sundarbans - Salinity Intrusion', '* Sundarbans - Sedimentation', '**Logic Description:** Reduced freshwater flow exacerbates salinity problems and affects delta formation.']
wetlands_sundarbans_stressors["Reduced Freshwater Flow"]["Impact on Area"] = ''
wetlands_sundarbans_stressors["Reduced Freshwater Flow"]["Impact on Biodiversity"] = '* Impacts on freshwater-dependent species.\n* Changes in plant communities.\n**Influenced By (Stressors):**\n* Upstream water diversions and dams.\n*  Sundarbans - Climate Change\n**Influences (Stressors):**\n* Sundarbans - Salinity Intrusion\n* Sundarbans - Sedimentation\n**Logic Description:** Reduced freshwater flow exacerbates salinity problems and affects delta formation.'
wetlands_sundarbans_stressors["Reduced Freshwater Flow"]["Influenced By"] = ['* Upstream water diversions and dams.', '*  Sundarbans - Climate Change', '**Influences (Stressors):**', '* Sundarbans - Salinity Intrusion', '* Sundarbans - Sedimentation', '**Logic Description:** Reduced freshwater flow exacerbates salinity problems and affects delta formation.']
wetlands_sundarbans_stressors["Reduced Freshwater Flow"]["Influences"] = ['* Sundarbans - Salinity Intrusion', '* Sundarbans - Sedimentation', '**Logic Description:** Reduced freshwater flow exacerbates salinity problems and affects delta formation.']
wetlands_sundarbans_stressors["Reduced Freshwater Flow"]["Logic Description"] = '---'

# --- Habitat Availability ---
wetlands_sundarbans_stressors["Habitat Availability"]["Impact on Biodiversity"] = '* Population sizes and distributions\n**Influenced By (Stressors):**\n* Sundarbans - Sea Level Rise\n* Sundarbans - Salinity Intrusion\n**Influences (Stressors):**\n* Many\n**Logic Description:** The amount of suitable habitat is critical.'
wetlands_sundarbans_stressors["Habitat Availability"]["Influenced By"] = ['* Sundarbans - Sea Level Rise', '* Sundarbans - Salinity Intrusion', '**Influences (Stressors):**', '* Many', '**Logic Description:** The amount of suitable habitat is critical.']
wetlands_sundarbans_stressors["Habitat Availability"]["Influences"] = ['* Many', '**Logic Description:** The amount of suitable habitat is critical.']
wetlands_sundarbans_stressors["Habitat Availability"]["Logic Description"] = '---'

# --- Water Quality ---
wetlands_sundarbans_stressors["Water Quality"]["Metric"] = 'Various water quality parameters.'
wetlands_sundarbans_stressors["Water Quality"]["Impact on Area"] = 'Overall ecosystem health'
wetlands_sundarbans_stressors["Water Quality"]["Influenced By"] = ['* Sundarbans - Pollution', '*  Sundarbans - Salinity Intrusion', '**Influences (Stressors):**', '* Many, varies', '**Logic Description:** Water quality is essential for ecosystem health.']
wetlands_sundarbans_stressors["Water Quality"]["Influences"] = ['* Many, varies', '**Logic Description:** Water quality is essential for ecosystem health.']
wetlands_sundarbans_stressors["Water Quality"]["Logic Description"] = '---'

# --- Wildlife Health ---
wetlands_sundarbans_stressors["Wildlife Health"]["Metric"] = 'Disease prevalence, mortality rates'
wetlands_sundarbans_stressors["Wildlife Health"]["Data Sources"] = ['* Wildlife Monitoring.', '**Impact on Area**: Indirect', '**Impact on Biodiversity:**', '* Population Declines.', '**Influenced By (Stressors)**:', '* Sundarbans - Pollution', '**Influences (Stressors):**', '* Population dynamics', '**Logic Description:** Wildlife health is an indicator of overall stress.']
wetlands_sundarbans_stressors["Wildlife Health"]["Impact on Biodiversity"] = '* Population Declines.\n**Influenced By (Stressors)**:\n* Sundarbans - Pollution\n**Influences (Stressors):**\n* Population dynamics\n**Logic Description:** Wildlife health is an indicator of overall stress.'
wetlands_sundarbans_stressors["Wildlife Health"]["Influences"] = ['* Population dynamics', '**Logic Description:** Wildlife health is an indicator of overall stress.']
wetlands_sundarbans_stressors["Wildlife Health"]["Logic Description"] = '---'

# --- Coastal Erosion ---
wetlands_sundarbans_stressors["Coastal Erosion"]["Metric"] = 'Rate of shoreline retreat.'
wetlands_sundarbans_stressors["Coastal Erosion"]["Data Sources"] = ['* Remote sensing', 'Field measurements.', '**Impact on Area:**', '* Land loss', '**Impact on Biodiversity:**', 'Habitat loss.', '**Influenced By (Stressors):**', 'Sundarbans - Sea Level Rise', '* Sundarbans - Cyclone Frequency and Intensity', '**Influences (Stressors):**', '* Many', '**Logic Description**: Erosion reduces land area.']
wetlands_sundarbans_stressors["Coastal Erosion"]["Impact on Area"] = ''
wetlands_sundarbans_stressors["Coastal Erosion"]["Impact on Biodiversity"] = 'Habitat loss.\n**Influenced By (Stressors):**\nSundarbans - Sea Level Rise\n* Sundarbans - Cyclone Frequency and Intensity\n**Influences (Stressors):**\n* Many\n**Logic Description**: Erosion reduces land area.'
wetlands_sundarbans_stressors["Coastal Erosion"]["Influenced By"] = ['Sundarbans - Sea Level Rise', '* Sundarbans - Cyclone Frequency and Intensity', '**Influences (Stressors):**', '* Many', '**Logic Description**: Erosion reduces land area.']
wetlands_sundarbans_stressors["Coastal Erosion"]["Influences"] = ['* Many', '**Logic Description**: Erosion reduces land area.']

# --- Sedimentation ---
wetlands_sundarbans_stressors["Sedimentation"]["Metric"] = 'Sediment deposition rates.'
wetlands_sundarbans_stressors["Sedimentation"]["Data Sources"] = ['* Research studies', '**Impact on Area**: Changes in land elevation and delta formation.', '**Impact on Biodiversity:**', '* Can be positive (building new land) or negative (smothering habitats)', '**Influenced By (Stressors)**:', '*  Sundarbans - Reduced Freshwater Flow', '**Influences (Stressors):**', '* Habitat availability', '**Logic Description**: Sediment dynamics are crucial for delta ecosystems.']
wetlands_sundarbans_stressors["Sedimentation"]["Impact on Biodiversity"] = '* Can be positive (building new land) or negative (smothering habitats)\n**Influenced By (Stressors)**:\n*  Sundarbans - Reduced Freshwater Flow\n**Influences (Stressors):**\n* Habitat availability\n**Logic Description**: Sediment dynamics are crucial for delta ecosystems.'
wetlands_sundarbans_stressors["Sedimentation"]["Influences"] = ['* Habitat availability', '**Logic Description**: Sediment dynamics are crucial for delta ecosystems.']

# --- Freshwater Availability ---
wetlands_sundarbans_stressors["Freshwater Availability"]["Influenced By"] = ['* Sundarbans - Salinity Intrusion', '**Influences (Stressors):**', 'Human well-being.', '* Many', '**Logic Description:** Freshwater is a scarce resource in some areas']
wetlands_sundarbans_stressors["Freshwater Availability"]["Influences"] = ['Human well-being.', '* Many', '**Logic Description:** Freshwater is a scarce resource in some areas']
wetlands_sundarbans_stressors["Freshwater Availability"]["Logic Description"] = '---'

