from stressor_templates import *
import copy

tundra_arctic_stressors = {
    "Infrastructure Development": copy.deepcopy(infrastructure_development_template),
    "Temperature Increase": copy.deepcopy(climate_change_template),
    "Changes in Precipitation": copy.deepcopy(climate_change_template),
    "Permafrost Thaw": {},
    "Sea Ice Loss": {},
    "Pollution": copy.deepcopy(pollution_template),
    "Invasive Species": copy.deepcopy(invasive_species_template),
    "Economic Growth": {},
    "Geopolitical Factors": {},
    "Government Policies": {},
    "Global Commodity Prices": {},
    "Technological Advancements": {},
    "Long-Range Transport of Pollutants": {},
    "Local Sources": {},
    "Disturbance": {},
    "Increased Human Activity": {},
    "Native Plant Communities": {},
    "Hydrology": copy.deepcopy(altered_hydrology_template),
    "Vegetation Changes": {},
    "Coastal Erosion": {},
    "Regional Climate": {},
    "Shrubification": {},
    "Wildlife Disturbance": {},
    "Wildlife Populations": {},
    "Wildlife Health": {},
}

# --- Infrastructure Development ---
tundra_arctic_stressors["Infrastructure Development"]["Metric"] = 'Road density (km/km²); area affected by resource extraction (oil, gas, mining) (ha/year); area affected by settlements and other infrastructure (ha/year).'
tundra_arctic_stressors["Infrastructure Development"]["Data Sources"] = ['Government statistics (national and regional).', 'Remote sensing data.', 'Industry reports.', 'Research publications.', '**Impact on Area:** Habitat fragmentation; direct loss of habitat due to resource extraction and infrastructure; permafrost degradation.', '**Impact on Biodiversity:**', 'Habitat loss and fragmentation.', 'Disruption of migration routes (e.g., caribou).', 'Disturbance to breeding and nesting sites (e.g., birds).', 'Pollution from resource extraction activities.', 'Increased human presence and activity.', '**Influenced By (Stressors):**', 'Arctic Tundra - Economic Growth', 'Arctic Tundra - Geopolitical Factors', 'Arctic Tundra - Government Policies', 'Arctic Tundra - Global Commodity Prices', 'Arctic Tundra - Technological Advancements', '**Influences (Stressors):**', 'Arctic Tundra - Permafrost Thaw', 'Arctic Tundra - Pollution', 'Arctic Tundra - Wildlife Disturbance', '**Logic Description:** Infrastructure development, primarily related to resource extraction, fragments the fragile tundra landscape, disrupts wildlife, and can accelerate permafrost thaw.']
tundra_arctic_stressors["Infrastructure Development"]["Impact on Area"] = 'Habitat fragmentation; direct loss of habitat due to resource extraction and infrastructure; permafrost degradation.'
tundra_arctic_stressors["Infrastructure Development"]["Impact on Biodiversity"] = 'Habitat loss and fragmentation.\nDisruption of migration routes (e.g., caribou).\nDisturbance to breeding and nesting sites (e.g., birds).\nPollution from resource extraction activities.\nIncreased human presence and activity.\n**Influenced By (Stressors):**\nArctic Tundra - Economic Growth\nArctic Tundra - Geopolitical Factors\nArctic Tundra - Government Policies\nArctic Tundra - Global Commodity Prices\nArctic Tundra - Technological Advancements\n**Influences (Stressors):**\nArctic Tundra - Permafrost Thaw\nArctic Tundra - Pollution\nArctic Tundra - Wildlife Disturbance\n**Logic Description:** Infrastructure development, primarily related to resource extraction, fragments the fragile tundra landscape, disrupts wildlife, and can accelerate permafrost thaw.'
tundra_arctic_stressors["Infrastructure Development"]["Influenced By"] = ['Arctic Tundra - Economic Growth', 'Arctic Tundra - Geopolitical Factors', 'Arctic Tundra - Government Policies', 'Arctic Tundra - Global Commodity Prices', 'Arctic Tundra - Technological Advancements', '**Influences (Stressors):**', 'Arctic Tundra - Permafrost Thaw', 'Arctic Tundra - Pollution', 'Arctic Tundra - Wildlife Disturbance', '**Logic Description:** Infrastructure development, primarily related to resource extraction, fragments the fragile tundra landscape, disrupts wildlife, and can accelerate permafrost thaw.']
tundra_arctic_stressors["Infrastructure Development"]["Influences"] = ['Arctic Tundra - Permafrost Thaw', 'Arctic Tundra - Pollution', 'Arctic Tundra - Wildlife Disturbance', '**Logic Description:** Infrastructure development, primarily related to resource extraction, fragments the fragile tundra landscape, disrupts wildlife, and can accelerate permafrost thaw.']
tundra_arctic_stressors["Infrastructure Development"]["Logic Description"] = '---'

# --- Temperature Increase ---
tundra_arctic_stressors["Temperature Increase"]["Metric"] = 'Average annual temperature increase (°C) (warming is occurring at a much faster rate in the Arctic than the global average - "Arctic Amplification").'
tundra_arctic_stressors["Temperature Increase"]["Data Sources"] = ['Climate models (global and regional).', 'Historical temperature records (from weather stations and ice cores).', 'Remote sensing data (e.g., measuring surface temperature).', '**Impact on Area:** Indirect; widespread permafrost thaw; changes in vegetation cover.', '**Impact on Biodiversity:**', 'Shifts in species distributions.', 'Increased stress on cold-adapted species.', 'Changes in phenology.', 'Increased risk of shrubification.', 'Changes in snow cover.', 'Increased decomposition rates.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions', 'Arctic Tundra - Loss of Sea Ice', 'Arctic Tundra - Permafrost Thaw', '**Influences (Stressors):**', 'Arctic Tundra - Permafrost Thaw', 'Arctic Tundra - Changes in Precipitation', 'Arctic Tundra - Sea Ice Loss', 'Arctic Tundra - Shrubification', '**Logic Description:** Rapid warming in the Arctic is causing profound changes, including shifts in species distributions, permafrost degradation, and changes in vegetation cover.']
tundra_arctic_stressors["Temperature Increase"]["Impact on Area"] = 'Indirect; widespread permafrost thaw; changes in vegetation cover.'
tundra_arctic_stressors["Temperature Increase"]["Impact on Biodiversity"] = 'Shifts in species distributions.\nIncreased stress on cold-adapted species.\nChanges in phenology.\nIncreased risk of shrubification.\nChanges in snow cover.\nIncreased decomposition rates.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions\nArctic Tundra - Loss of Sea Ice\nArctic Tundra - Permafrost Thaw\n**Influences (Stressors):**\nArctic Tundra - Permafrost Thaw\nArctic Tundra - Changes in Precipitation\nArctic Tundra - Sea Ice Loss\nArctic Tundra - Shrubification\n**Logic Description:** Rapid warming in the Arctic is causing profound changes, including shifts in species distributions, permafrost degradation, and changes in vegetation cover.'
tundra_arctic_stressors["Temperature Increase"]["Influenced By"] = ['Global Greenhouse Gas Emissions', 'Arctic Tundra - Loss of Sea Ice', 'Arctic Tundra - Permafrost Thaw', '**Influences (Stressors):**', 'Arctic Tundra - Permafrost Thaw', 'Arctic Tundra - Changes in Precipitation', 'Arctic Tundra - Sea Ice Loss', 'Arctic Tundra - Shrubification', '**Logic Description:** Rapid warming in the Arctic is causing profound changes, including shifts in species distributions, permafrost degradation, and changes in vegetation cover.']
tundra_arctic_stressors["Temperature Increase"]["Influences"] = ['Arctic Tundra - Permafrost Thaw', 'Arctic Tundra - Changes in Precipitation', 'Arctic Tundra - Sea Ice Loss', 'Arctic Tundra - Shrubification', '**Logic Description:** Rapid warming in the Arctic is causing profound changes, including shifts in species distributions, permafrost degradation, and changes in vegetation cover.']
tundra_arctic_stressors["Temperature Increase"]["Logic Description"] = '---'

# --- Changes in Precipitation ---
tundra_arctic_stressors["Changes in Precipitation"]["Metric"] = 'Change in annual precipitation (mm/year); changes in snowfall amount and timing; changes in rain-on-snow events.'
tundra_arctic_stressors["Changes in Precipitation"]["Data Sources"] = ['Climate models.', 'Historical weather records.', 'Remote sensing (e.g., measuring snow cover).', '**Impact on Area:** Indirect; changes in snow cover, permafrost, and hydrology.', '**Impact on Biodiversity:**', 'Changes in vegetation composition.', 'Impacts on animal populations that depend on snow cover.', 'Changes in the timing and extent of snowmelt.', 'Increased frequency of rain-on-snow events.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions', 'Arctic Tundra - Temperature Increase', '**Influences (Stressors):**', 'Arctic Tundra - Permafrost Thaw', 'Arctic Tundra - Vegetation Changes', 'Arctic Tundra - Wildlife Populations', '**Logic Description:** Changes in precipitation patterns impact snow cover, permafrost, hydrology, and vegetation, with cascading effects on wildlife.']
tundra_arctic_stressors["Changes in Precipitation"]["Impact on Area"] = 'Indirect; changes in snow cover, permafrost, and hydrology.'
tundra_arctic_stressors["Changes in Precipitation"]["Impact on Biodiversity"] = 'Changes in vegetation composition.\nImpacts on animal populations that depend on snow cover.\nChanges in the timing and extent of snowmelt.\nIncreased frequency of rain-on-snow events.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions\nArctic Tundra - Temperature Increase\n**Influences (Stressors):**\nArctic Tundra - Permafrost Thaw\nArctic Tundra - Vegetation Changes\nArctic Tundra - Wildlife Populations\n**Logic Description:** Changes in precipitation patterns impact snow cover, permafrost, hydrology, and vegetation, with cascading effects on wildlife.'
tundra_arctic_stressors["Changes in Precipitation"]["Influenced By"] = ['Global Greenhouse Gas Emissions', 'Arctic Tundra - Temperature Increase', '**Influences (Stressors):**', 'Arctic Tundra - Permafrost Thaw', 'Arctic Tundra - Vegetation Changes', 'Arctic Tundra - Wildlife Populations', '**Logic Description:** Changes in precipitation patterns impact snow cover, permafrost, hydrology, and vegetation, with cascading effects on wildlife.']
tundra_arctic_stressors["Changes in Precipitation"]["Influences"] = ['Arctic Tundra - Permafrost Thaw', 'Arctic Tundra - Vegetation Changes', 'Arctic Tundra - Wildlife Populations', '**Logic Description:** Changes in precipitation patterns impact snow cover, permafrost, hydrology, and vegetation, with cascading effects on wildlife.']
tundra_arctic_stressors["Changes in Precipitation"]["Logic Description"] = '---'

# --- Permafrost Thaw ---
tundra_arctic_stressors["Permafrost Thaw"]["Metric"] = 'Active layer thickness (cm); area of permafrost degradation (ha); ground subsidence (cm); thermokarst lake formation (area, number).'
tundra_arctic_stressors["Permafrost Thaw"]["Data Sources"] = ['Field measurements.', 'Remote sensing.', 'Climate models.', 'GIS analysis.', '**Impact on Area:** Changes in ground stability; altered hydrology; release of greenhouse gases; formation of thermokarst lakes.', '**Impact on Biodiversity:**', 'Changes in vegetation composition.', 'Loss of habitat for some species and creation of new habitat for others.', 'Impacts on infrastructure.', 'Release of methane and carbon dioxide.', 'Changes in water quality.', '**Influenced By (Stressors):**', 'Arctic Tundra - Temperature Increase', 'Arctic Tundra - Changes in Precipitation', 'Arctic Tundra - Wildfires', 'Arctic Tundra - Infrastructure Development', '**Influences (Stressors):**', 'Global Climate Change (through greenhouse gas emissions).', 'Arctic Tundra - Hydrology', 'Arctic Tundra - Vegetation Changes', 'Arctic Tundra - Coastal Erosion', '**Logic Description:** Permafrost thaw is a major and widespread stressor. It leads to ground instability, altered hydrology, greenhouse gas release, and vegetation changes.']
tundra_arctic_stressors["Permafrost Thaw"]["Impact on Area"] = 'Changes in ground stability; altered hydrology; release of greenhouse gases; formation of thermokarst lakes.'
tundra_arctic_stressors["Permafrost Thaw"]["Impact on Biodiversity"] = 'Changes in vegetation composition.\nLoss of habitat for some species and creation of new habitat for others.\nImpacts on infrastructure.\nRelease of methane and carbon dioxide.\nChanges in water quality.\n**Influenced By (Stressors):**\nArctic Tundra - Temperature Increase\nArctic Tundra - Changes in Precipitation\nArctic Tundra - Wildfires\nArctic Tundra - Infrastructure Development\n**Influences (Stressors):**\nGlobal Climate Change (through greenhouse gas emissions).\nArctic Tundra - Hydrology\nArctic Tundra - Vegetation Changes\nArctic Tundra - Coastal Erosion\n**Logic Description:** Permafrost thaw is a major and widespread stressor. It leads to ground instability, altered hydrology, greenhouse gas release, and vegetation changes.'
tundra_arctic_stressors["Permafrost Thaw"]["Influenced By"] = ['Arctic Tundra - Temperature Increase', 'Arctic Tundra - Changes in Precipitation', 'Arctic Tundra - Wildfires', 'Arctic Tundra - Infrastructure Development', '**Influences (Stressors):**', 'Global Climate Change (through greenhouse gas emissions).', 'Arctic Tundra - Hydrology', 'Arctic Tundra - Vegetation Changes', 'Arctic Tundra - Coastal Erosion', '**Logic Description:** Permafrost thaw is a major and widespread stressor. It leads to ground instability, altered hydrology, greenhouse gas release, and vegetation changes.']
tundra_arctic_stressors["Permafrost Thaw"]["Influences"] = ['Global Climate Change (through greenhouse gas emissions).', 'Arctic Tundra - Hydrology', 'Arctic Tundra - Vegetation Changes', 'Arctic Tundra - Coastal Erosion', '**Logic Description:** Permafrost thaw is a major and widespread stressor. It leads to ground instability, altered hydrology, greenhouse gas release, and vegetation changes.']
tundra_arctic_stressors["Permafrost Thaw"]["Logic Description"] = '---'

# --- Sea Ice Loss ---
tundra_arctic_stressors["Sea Ice Loss"]["Metric"] = 'Sea ice extent (million km²); sea ice thickness (m); sea ice duration (days).'
tundra_arctic_stressors["Sea Ice Loss"]["Data Sources"] = ['Satellite observations (e.g., from NSIDC).', 'Climate models.', '**Impact on Area:** Primarily impacts coastal tundra ecosystems; also influences regional climate.', '**Impact on Biodiversity:**', 'Impacts on marine mammals.', 'Changes in coastal erosion rates.', 'Indirect impacts on terrestrial species.', 'Increased human access to coastal areas.', '**Influenced By (Stressors):**', 'Arctic Tundra - Temperature Increase', 'Arctic Tundra - Changes in Ocean Currents', '**Influences (Stressors):**', 'Arctic Tundra - Regional Climate', 'Arctic Tundra - Coastal Erosion', 'Marine Ecosystems (impacts extend beyond the tundra).', '**Logic Description:** Sea ice loss has indirect impacts on coastal tundra ecosystems and influences regional climate.']
tundra_arctic_stressors["Sea Ice Loss"]["Impact on Area"] = 'Primarily impacts coastal tundra ecosystems; also influences regional climate.'
tundra_arctic_stressors["Sea Ice Loss"]["Impact on Biodiversity"] = 'Impacts on marine mammals.\nChanges in coastal erosion rates.\nIndirect impacts on terrestrial species.\nIncreased human access to coastal areas.\n**Influenced By (Stressors):**\nArctic Tundra - Temperature Increase\nArctic Tundra - Changes in Ocean Currents\n**Influences (Stressors):**\nArctic Tundra - Regional Climate\nArctic Tundra - Coastal Erosion\nMarine Ecosystems (impacts extend beyond the tundra).\n**Logic Description:** Sea ice loss has indirect impacts on coastal tundra ecosystems and influences regional climate.'
tundra_arctic_stressors["Sea Ice Loss"]["Influenced By"] = ['Arctic Tundra - Temperature Increase', 'Arctic Tundra - Changes in Ocean Currents', '**Influences (Stressors):**', 'Arctic Tundra - Regional Climate', 'Arctic Tundra - Coastal Erosion', 'Marine Ecosystems (impacts extend beyond the tundra).', '**Logic Description:** Sea ice loss has indirect impacts on coastal tundra ecosystems and influences regional climate.']
tundra_arctic_stressors["Sea Ice Loss"]["Influences"] = ['Arctic Tundra - Regional Climate', 'Arctic Tundra - Coastal Erosion', 'Marine Ecosystems (impacts extend beyond the tundra).', '**Logic Description:** Sea ice loss has indirect impacts on coastal tundra ecosystems and influences regional climate.']
tundra_arctic_stressors["Sea Ice Loss"]["Logic Description"] = '---'

# --- Pollution ---
tundra_arctic_stressors["Pollution"]["Metric"] = 'Concentrations of pollutants (e.g., heavy metals, POPs, oil) in air, water, soil, and biota.'
tundra_arctic_stressors["Pollution"]["Data Sources"] = ['Environmental monitoring programs (e.g., AMAP).', 'Research studies.', '**Impact on Area:** Contamination of soil, water, and air.', '**Impact on Biodiversity:**', 'Toxic effects on wildlife.', 'Reduced reproductive success.', 'Increased susceptibility to disease.', '**Influenced By (Stressors):**', 'Arctic Tundra - Long-Range Transport of Pollutants', 'Arctic Tundra - Local Sources', '**Influences (Stressors):**', '* Arctic Tundra - Wildlife Health', '**Logic Description:** The Arctic Tundra receives pollutants from both local and long-range sources, impacting wildlife health.']
tundra_arctic_stressors["Pollution"]["Impact on Area"] = 'Contamination of soil, water, and air.'
tundra_arctic_stressors["Pollution"]["Impact on Biodiversity"] = 'Toxic effects on wildlife.\nReduced reproductive success.\nIncreased susceptibility to disease.\n**Influenced By (Stressors):**\nArctic Tundra - Long-Range Transport of Pollutants\nArctic Tundra - Local Sources\n**Influences (Stressors):**\n* Arctic Tundra - Wildlife Health\n**Logic Description:** The Arctic Tundra receives pollutants from both local and long-range sources, impacting wildlife health.'
tundra_arctic_stressors["Pollution"]["Influenced By"] = ['Arctic Tundra - Long-Range Transport of Pollutants', 'Arctic Tundra - Local Sources', '**Influences (Stressors):**', '* Arctic Tundra - Wildlife Health', '**Logic Description:** The Arctic Tundra receives pollutants from both local and long-range sources, impacting wildlife health.']
tundra_arctic_stressors["Pollution"]["Influences"] = ['* Arctic Tundra - Wildlife Health', '**Logic Description:** The Arctic Tundra receives pollutants from both local and long-range sources, impacting wildlife health.']
tundra_arctic_stressors["Pollution"]["Logic Description"] = '---'

# --- Invasive Species ---
tundra_arctic_stressors["Invasive Species"]["Metric"] = 'Distribution and abundance of invasive species.'
tundra_arctic_stressors["Invasive Species"]["Data Sources"] = ['Research studies.', 'Monitoring programs.', '**Impact on Area:** Potential for changes in vegetation composition.', '**Impact on Biodiversity:**', 'Competition with native species.', 'Alteration of ecosystem processes.', '**Influenced By (Stressors):**', 'Arctic Tundra - Climate Change', 'Arctic Tundra - Disturbance', 'Arctic Tundra - Increased Human Activity', '**Influences (Stressors):**', '* Arctic Tundra - Native Plant Communities', '**Logic Description:** Invasive species pose an increasing threat as the climate warms and human activity increases.']
tundra_arctic_stressors["Invasive Species"]["Impact on Area"] = 'Potential for changes in vegetation composition.'
tundra_arctic_stressors["Invasive Species"]["Impact on Biodiversity"] = 'Competition with native species.\nAlteration of ecosystem processes.\n**Influenced By (Stressors):**\nArctic Tundra - Climate Change\nArctic Tundra - Disturbance\nArctic Tundra - Increased Human Activity\n**Influences (Stressors):**\n* Arctic Tundra - Native Plant Communities\n**Logic Description:** Invasive species pose an increasing threat as the climate warms and human activity increases.'
tundra_arctic_stressors["Invasive Species"]["Influenced By"] = ['Arctic Tundra - Climate Change', 'Arctic Tundra - Disturbance', 'Arctic Tundra - Increased Human Activity', '**Influences (Stressors):**', '* Arctic Tundra - Native Plant Communities', '**Logic Description:** Invasive species pose an increasing threat as the climate warms and human activity increases.']
tundra_arctic_stressors["Invasive Species"]["Influences"] = ['* Arctic Tundra - Native Plant Communities', '**Logic Description:** Invasive species pose an increasing threat as the climate warms and human activity increases.']
tundra_arctic_stressors["Invasive Species"]["Logic Description"] = '---'

# --- Economic Growth ---
tundra_arctic_stressors["Economic Growth"]["Data Sources"] = ['* Economic data', '**Impact on Area**: Increased pressure on resources.', '**Impact on Biodiversity**:', '* Habitat loss, disturbance', '**Influenced By (Stressors):**', '* Global demand for resources', '**Influences (Stressors):**', '*  Arctic Tundra - Infrastructure Development', '**Logic Description:** Economic growth drives resource extraction']
tundra_arctic_stressors["Economic Growth"]["Influenced By"] = ['* Global demand for resources', '**Influences (Stressors):**', '*  Arctic Tundra - Infrastructure Development', '**Logic Description:** Economic growth drives resource extraction']
tundra_arctic_stressors["Economic Growth"]["Influences"] = ['*  Arctic Tundra - Infrastructure Development', '**Logic Description:** Economic growth drives resource extraction']
tundra_arctic_stressors["Economic Growth"]["Logic Description"] = '---'

# --- Geopolitical Factors ---
tundra_arctic_stressors["Geopolitical Factors"]["Metric"] = 'International agreements, military activity'
tundra_arctic_stressors["Geopolitical Factors"]["Data Sources"] = ['* News Reports, government documents', '**Impact on Area:** Variable, can influence resource development, conservation efforts.', '**Impact on Biodiversity:**', '* Variable.', '**Influenced By (Stressors):**', '* Global politics', '**Influences (Stressors):**', '*  Arctic Tundra - Infrastructure Development', '**Logic Description:** Geopolitics can influence Arctic development.']
tundra_arctic_stressors["Geopolitical Factors"]["Impact on Area"] = 'Variable, can influence resource development, conservation efforts.'
tundra_arctic_stressors["Geopolitical Factors"]["Impact on Biodiversity"] = '* Variable.\n**Influenced By (Stressors):**\n* Global politics\n**Influences (Stressors):**\n*  Arctic Tundra - Infrastructure Development\n**Logic Description:** Geopolitics can influence Arctic development.'
tundra_arctic_stressors["Geopolitical Factors"]["Influenced By"] = ['* Global politics', '**Influences (Stressors):**', '*  Arctic Tundra - Infrastructure Development', '**Logic Description:** Geopolitics can influence Arctic development.']
tundra_arctic_stressors["Geopolitical Factors"]["Influences"] = ['*  Arctic Tundra - Infrastructure Development', '**Logic Description:** Geopolitics can influence Arctic development.']
tundra_arctic_stressors["Geopolitical Factors"]["Logic Description"] = '---'

# --- Government Policies ---
tundra_arctic_stressors["Government Policies"]["Metric"] = 'Resource management regulations, environmental protections'
tundra_arctic_stressors["Government Policies"]["Data Sources"] = ['* Policy documents', '**Impact on Area:** Variable', '**Impact on Biodiversity:**', '* Variable', '**Influenced By (Stressors):**', '* Politics, economics', '**Influences (Stressors):**', '* Arctic Tundra - Infrastructure Development', '**Logic Description:** Government policy shapes resource use.']
tundra_arctic_stressors["Government Policies"]["Impact on Area"] = 'Variable'
tundra_arctic_stressors["Government Policies"]["Impact on Biodiversity"] = '* Variable\n**Influenced By (Stressors):**\n* Politics, economics\n**Influences (Stressors):**\n* Arctic Tundra - Infrastructure Development\n**Logic Description:** Government policy shapes resource use.'
tundra_arctic_stressors["Government Policies"]["Influenced By"] = ['* Politics, economics', '**Influences (Stressors):**', '* Arctic Tundra - Infrastructure Development', '**Logic Description:** Government policy shapes resource use.']
tundra_arctic_stressors["Government Policies"]["Influences"] = ['* Arctic Tundra - Infrastructure Development', '**Logic Description:** Government policy shapes resource use.']
tundra_arctic_stressors["Government Policies"]["Logic Description"] = '---'

# --- Global Commodity Prices ---
tundra_arctic_stressors["Global Commodity Prices"]["Data Sources"] = ['* Economic Data', '**Impact on Area:** Influences the economic viability of resource extraction.', '**Impact on Biodiversity:**', '* Indirect, through impacts on development.', '**Influenced By (Stressors)**', '* Global markets.', '**Influences (Stressors):**', '* Arctic Tundra - Infrastructure Development', '**Logic Description**: Commodity prices influence resource extraction.']
tundra_arctic_stressors["Global Commodity Prices"]["Impact on Area"] = 'Influences the economic viability of resource extraction.'
tundra_arctic_stressors["Global Commodity Prices"]["Impact on Biodiversity"] = '* Indirect, through impacts on development.\n**Influenced By (Stressors)**\n* Global markets.\n**Influences (Stressors):**\n* Arctic Tundra - Infrastructure Development\n**Logic Description**: Commodity prices influence resource extraction.'
tundra_arctic_stressors["Global Commodity Prices"]["Influences"] = ['* Arctic Tundra - Infrastructure Development', '**Logic Description**: Commodity prices influence resource extraction.']

# --- Technological Advancements ---
tundra_arctic_stressors["Technological Advancements"]["Metric"] = 'Development of new technologies for resource extraction, transportation.'
tundra_arctic_stressors["Technological Advancements"]["Data Sources"] = ['* Industry reports, research publications.', '**Impact on Area:** Can make resource extraction more feasible or less impactful.', '**Impact on Biodiversity:**', '* Variable', '**Influenced By (Stressors)**', '* Research and development.', '**Influences (Stressors):**', '* Arctic Tundra - Infrastructure Development', '**Logic Description:** Technology can change the feasibility of resource extraction.']
tundra_arctic_stressors["Technological Advancements"]["Impact on Area"] = 'Can make resource extraction more feasible or less impactful.'
tundra_arctic_stressors["Technological Advancements"]["Impact on Biodiversity"] = '* Variable\n**Influenced By (Stressors)**\n* Research and development.\n**Influences (Stressors):**\n* Arctic Tundra - Infrastructure Development\n**Logic Description:** Technology can change the feasibility of resource extraction.'
tundra_arctic_stressors["Technological Advancements"]["Influences"] = ['* Arctic Tundra - Infrastructure Development', '**Logic Description:** Technology can change the feasibility of resource extraction.']
tundra_arctic_stressors["Technological Advancements"]["Logic Description"] = '---'

# --- Long-Range Transport of Pollutants ---
tundra_arctic_stressors["Long-Range Transport of Pollutants"]["Data Sources"] = ['*  Environmental monitoring programs (AMAP)', '**Impact on Area:** Widespread contamination.', '**Impact on Biodiversity:**', 'Toxic effects on wildlife.', '**Influenced By (Stressors):**', '* Industrial activity in other regions.', '**Influences (Stressors):**', '* Arctic Tundra - Pollution', '**Logic Description:** Pollutants travel long distances to the Arctic.']
tundra_arctic_stressors["Long-Range Transport of Pollutants"]["Impact on Area"] = 'Widespread contamination.'
tundra_arctic_stressors["Long-Range Transport of Pollutants"]["Impact on Biodiversity"] = 'Toxic effects on wildlife.\n**Influenced By (Stressors):**\n* Industrial activity in other regions.\n**Influences (Stressors):**\n* Arctic Tundra - Pollution\n**Logic Description:** Pollutants travel long distances to the Arctic.'
tundra_arctic_stressors["Long-Range Transport of Pollutants"]["Influenced By"] = ['* Industrial activity in other regions.', '**Influences (Stressors):**', '* Arctic Tundra - Pollution', '**Logic Description:** Pollutants travel long distances to the Arctic.']
tundra_arctic_stressors["Long-Range Transport of Pollutants"]["Influences"] = ['* Arctic Tundra - Pollution', '**Logic Description:** Pollutants travel long distances to the Arctic.']
tundra_arctic_stressors["Long-Range Transport of Pollutants"]["Logic Description"] = '---'

# --- Local Sources ---
tundra_arctic_stressors["Local Sources"]["Metric"] = 'Pollutant emissions from local activities.'
tundra_arctic_stressors["Local Sources"]["Data Sources"] = ['* Environmental monitoring.', '**Impact on Area:** Localized pollution.', '**Impact on Biodiversity:**', '* Impacts on wildlife.', '**Influenced By (Stressors):**', '*  Arctic Tundra - Infrastructure Development', '**Influences (Stressors):**', '* Arctic Tundra - Pollution', '**Logic Description:** Local activities contribute to pollution.']
tundra_arctic_stressors["Local Sources"]["Impact on Area"] = 'Localized pollution.'
tundra_arctic_stressors["Local Sources"]["Impact on Biodiversity"] = '* Impacts on wildlife.\n**Influenced By (Stressors):**\n*  Arctic Tundra - Infrastructure Development\n**Influences (Stressors):**\n* Arctic Tundra - Pollution\n**Logic Description:** Local activities contribute to pollution.'
tundra_arctic_stressors["Local Sources"]["Influenced By"] = ['*  Arctic Tundra - Infrastructure Development', '**Influences (Stressors):**', '* Arctic Tundra - Pollution', '**Logic Description:** Local activities contribute to pollution.']
tundra_arctic_stressors["Local Sources"]["Influences"] = ['* Arctic Tundra - Pollution', '**Logic Description:** Local activities contribute to pollution.']
tundra_arctic_stressors["Local Sources"]["Logic Description"] = '---'

# --- Disturbance ---
tundra_arctic_stressors["Disturbance"]["Metric"] = 'Area and frequency'
tundra_arctic_stressors["Disturbance"]["Data Sources"] = ['* Field Observations, remote sensing', '**Impact on Area:** Varies', '**Impact on Biodiversity**:', '* Variable', '**Influenced By (Stressors):**', '* Many', '**Influences (Stressors):**', '* Arctic Tundra - Invasive Species', '**Logic Description**: General category for various disturbances.']
tundra_arctic_stressors["Disturbance"]["Impact on Area"] = 'Varies'
tundra_arctic_stressors["Disturbance"]["Influenced By"] = ['* Many', '**Influences (Stressors):**', '* Arctic Tundra - Invasive Species', '**Logic Description**: General category for various disturbances.']
tundra_arctic_stressors["Disturbance"]["Influences"] = ['* Arctic Tundra - Invasive Species', '**Logic Description**: General category for various disturbances.']

# --- Increased Human Activity ---
tundra_arctic_stressors["Increased Human Activity"]["Metric"] = 'Population, tourism, shipping traffic'
tundra_arctic_stressors["Increased Human Activity"]["Data Sources"] = ['* Various', '**Impact on Area:** Disturbance, pollution', '**Impact on Biodiversity:**', '* Impacts on wildlife', '**Influenced By (Stressors):**', '* Many', '**Influences (Stressors):**', '* Arctic Tundra - Invasive Species', '**Logic Description**: Increasing human presence has impacts.']
tundra_arctic_stressors["Increased Human Activity"]["Impact on Area"] = 'Disturbance, pollution'
tundra_arctic_stressors["Increased Human Activity"]["Impact on Biodiversity"] = '* Impacts on wildlife\n**Influenced By (Stressors):**\n* Many\n**Influences (Stressors):**\n* Arctic Tundra - Invasive Species\n**Logic Description**: Increasing human presence has impacts.'
tundra_arctic_stressors["Increased Human Activity"]["Influenced By"] = ['* Many', '**Influences (Stressors):**', '* Arctic Tundra - Invasive Species', '**Logic Description**: Increasing human presence has impacts.']
tundra_arctic_stressors["Increased Human Activity"]["Influences"] = ['* Arctic Tundra - Invasive Species', '**Logic Description**: Increasing human presence has impacts.']

# --- Native Plant Communities ---
tundra_arctic_stressors["Native Plant Communities"]["Metric"] = 'Plant species composition, abundance'
tundra_arctic_stressors["Native Plant Communities"]["Data Sources"] = ['* Field Surveys', '**Impact on Area:** Overall ecosystem structure', '**Impact on Biodiversity:**', '* Interactions with other species.', '**Influenced By (Stressors)**', '* Arctic Tundra - Invasive Species', '**Influences (Stressors):**', '* Many', '**Logic Description:** Native plants are the foundation of the ecosystem.']
tundra_arctic_stressors["Native Plant Communities"]["Impact on Area"] = 'Overall ecosystem structure'
tundra_arctic_stressors["Native Plant Communities"]["Impact on Biodiversity"] = '* Interactions with other species.\n**Influenced By (Stressors)**\n* Arctic Tundra - Invasive Species\n**Influences (Stressors):**\n* Many\n**Logic Description:** Native plants are the foundation of the ecosystem.'
tundra_arctic_stressors["Native Plant Communities"]["Influences"] = ['* Many', '**Logic Description:** Native plants are the foundation of the ecosystem.']
tundra_arctic_stressors["Native Plant Communities"]["Logic Description"] = '---'

# --- Hydrology ---
tundra_arctic_stressors["Hydrology"]["Data Sources"] = ['* Hydrological monitoring data', '**Impact on Area:** Water availability, wetland extent', '**Impact on Biodiversity:**', '* Impacts on aquatic and wetland species', '**Influenced By (Stressors):**', '* Arctic Tundra - Permafrost Thaw', '**Influences (Stressors):**', '* Many, Varies', '**Logic Description:** Water flow is fundamental.']
tundra_arctic_stressors["Hydrology"]["Impact on Area"] = 'Water availability, wetland extent'
tundra_arctic_stressors["Hydrology"]["Impact on Biodiversity"] = '* Impacts on aquatic and wetland species\n**Influenced By (Stressors):**\n* Arctic Tundra - Permafrost Thaw\n**Influences (Stressors):**\n* Many, Varies\n**Logic Description:** Water flow is fundamental.'
tundra_arctic_stressors["Hydrology"]["Influenced By"] = ['* Arctic Tundra - Permafrost Thaw', '**Influences (Stressors):**', '* Many, Varies', '**Logic Description:** Water flow is fundamental.']
tundra_arctic_stressors["Hydrology"]["Influences"] = ['* Many, Varies', '**Logic Description:** Water flow is fundamental.']
tundra_arctic_stressors["Hydrology"]["Logic Description"] = '---'

# --- Vegetation Changes ---
tundra_arctic_stressors["Vegetation Changes"]["Influences"] = ['* Many, Varies', '**Logic Description:** Vegetation changes reflect other stressors.']
tundra_arctic_stressors["Vegetation Changes"]["Logic Description"] = '---'

# --- Coastal Erosion ---
tundra_arctic_stressors["Coastal Erosion"]["Metric"] = 'Rate of shoreline retreat'
tundra_arctic_stressors["Coastal Erosion"]["Data Sources"] = ['* Remote Sensing', '* Field measurements', '**Impact on Area:** Land Loss', '**Impact on Biodiversity:**', '* Habitat loss', '**Influenced By (Stressors):**', '* Arctic Tundra - Permafrost Thaw', '* Arctic Tundra - Sea Ice Loss', '**Influences (Stressors):**', '* Many, varies', '**Logic Description**: Erosion is a major issue in coastal areas']
tundra_arctic_stressors["Coastal Erosion"]["Impact on Area"] = 'Land Loss'
tundra_arctic_stressors["Coastal Erosion"]["Impact on Biodiversity"] = '* Habitat loss\n**Influenced By (Stressors):**\n* Arctic Tundra - Permafrost Thaw\n* Arctic Tundra - Sea Ice Loss\n**Influences (Stressors):**\n* Many, varies\n**Logic Description**: Erosion is a major issue in coastal areas'
tundra_arctic_stressors["Coastal Erosion"]["Influenced By"] = ['* Arctic Tundra - Permafrost Thaw', '* Arctic Tundra - Sea Ice Loss', '**Influences (Stressors):**', '* Many, varies', '**Logic Description**: Erosion is a major issue in coastal areas']
tundra_arctic_stressors["Coastal Erosion"]["Influences"] = ['* Many, varies', '**Logic Description**: Erosion is a major issue in coastal areas']

# --- Regional Climate ---
tundra_arctic_stressors["Regional Climate"]["Metric"] = 'Temperature, precipitation, wind patterns'
tundra_arctic_stressors["Regional Climate"]["Data Sources"] = ['* Climate data.', '**Impact on Area**: Overall climate conditions', '**Impact on Biodiversity**:', '* Many Impacts', '**Influenced By (Stressors):**', '* Arctic Tundra - Sea Ice Loss', '**Influences (Stressors):**', '* Many', '**Logic Description**: Regional climate drives local conditions.']
tundra_arctic_stressors["Regional Climate"]["Influenced By"] = ['* Arctic Tundra - Sea Ice Loss', '**Influences (Stressors):**', '* Many', '**Logic Description**: Regional climate drives local conditions.']
tundra_arctic_stressors["Regional Climate"]["Influences"] = ['* Many', '**Logic Description**: Regional climate drives local conditions.']

# --- Shrubification ---
tundra_arctic_stressors["Shrubification"]["Metric"] = 'Shrub cover and abundance.'
tundra_arctic_stressors["Shrubification"]["Data Sources"] = ['* Remote sensing', '* Field surveys.', '**Impact on Area**: Changes in vegetation structure and albedo.', '**Impact on Biodiversity:**', '* Impacts on species that prefer open tundra.', '* Changes in snow cover and permafrost.', '**Influenced By (Stressors):**', '* Arctic Tundra - Temperature Increase', '**Influences (Stressors)**', '* Many', '**Logic Description**: Expansion of shrubs is a major vegetation change.']
tundra_arctic_stressors["Shrubification"]["Impact on Biodiversity"] = '* Impacts on species that prefer open tundra.\n* Changes in snow cover and permafrost.\n**Influenced By (Stressors):**\n* Arctic Tundra - Temperature Increase\n**Influences (Stressors)**\n* Many\n**Logic Description**: Expansion of shrubs is a major vegetation change.'
tundra_arctic_stressors["Shrubification"]["Influenced By"] = ['* Arctic Tundra - Temperature Increase', '**Influences (Stressors)**', '* Many', '**Logic Description**: Expansion of shrubs is a major vegetation change.']

# --- Wildlife Disturbance ---
tundra_arctic_stressors["Wildlife Disturbance"]["Metric"] = 'Frequency and intensity of human disturbance to wildlife.'
tundra_arctic_stressors["Wildlife Disturbance"]["Data Sources"] = ['* Research Studies', '**Impact on Area**: Indirect, through impacts on animal behavior and populations.', '**Impact on Biodiversity:**', 'Altered behavior, reduced reproductive success, increased stress.', '**Influenced By (Stressors)**', '* Arctic Tundra - Infrastructure Development', '**Influences (Stressors)**:', '* Arctic Tundra - Population Dynamics']
tundra_arctic_stressors["Wildlife Disturbance"]["Impact on Biodiversity"] = 'Altered behavior, reduced reproductive success, increased stress.\n**Influenced By (Stressors)**\n* Arctic Tundra - Infrastructure Development\n**Influences (Stressors)**:\n* Arctic Tundra - Population Dynamics'

# --- Wildlife Populations ---
tundra_arctic_stressors["Wildlife Populations"]["Metric"] = 'Population sizes and distributions of key species.'
tundra_arctic_stressors["Wildlife Populations"]["Impact on Biodiversity"] = '* Ecosystem Function.\n**Influenced By (Stressors):**\n* Arctic Tundra - Changes in Precipitation\n**Influences (Stressors):**\n* Many\n**Logic Description:** Wildlife populations are affected by many stressors.'
tundra_arctic_stressors["Wildlife Populations"]["Influenced By"] = ['* Arctic Tundra - Changes in Precipitation', '**Influences (Stressors):**', '* Many', '**Logic Description:** Wildlife populations are affected by many stressors.']
tundra_arctic_stressors["Wildlife Populations"]["Influences"] = ['* Many', '**Logic Description:** Wildlife populations are affected by many stressors.']
tundra_arctic_stressors["Wildlife Populations"]["Logic Description"] = '---'

# --- Wildlife Health ---
tundra_arctic_stressors["Wildlife Health"]["Metric"] = 'Disease prevalence, mortality rates.'
tundra_arctic_stressors["Wildlife Health"]["Data Sources"] = ['* Wildlife monitoring programs', '**Impact on Area:** Indirect, through population impacts.', '**Impact on Biodiversity**:', '* Population Declines', '**Influenced By (Stressors)**:', '* Arctic Tundra - Pollution', '**Influences (Stressors)**', '* Arctic Tundra - Population Dynamics', '**Logic Description:** Overall Health']
tundra_arctic_stressors["Wildlife Health"]["Impact on Area"] = 'Indirect, through population impacts.'
tundra_arctic_stressors["Wildlife Health"]["Logic Description"] = '---'

