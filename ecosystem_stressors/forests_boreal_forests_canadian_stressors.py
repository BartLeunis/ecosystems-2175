from stressor_templates import *
import copy

forests_boreal_forests_canadian_stressors = {
    "Infrastructure Development": copy.deepcopy(infrastructure_development_template),
    "Deforestation": copy.deepcopy(deforestation_template),
    "Temperature Increase": copy.deepcopy(climate_change_template),
    "Changes in Precipitation": copy.deepcopy(climate_change_template),
    "Wildfires": copy.deepcopy(fire_regime_template),
    "Permafrost Thaw": {},
    "Invasive Species": copy.deepcopy(invasive_species_template),
}

# --- Infrastructure Development ---
forests_boreal_forests_canadian_stressors["Infrastructure Development"]["Metric"] = 'Road density (km/km²); area affected by resource extraction (mining, oil sands, forestry) (ha/year).'
forests_boreal_forests_canadian_stressors["Infrastructure Development"]["Data Sources"] = ['Canadian government data (federal and provincial).', 'Remote sensing.', 'Industry reports.', '**Impact on Area:** Habitat fragmentation; direct loss from resource extraction.', '**Impact on Biodiversity:**', 'Habitat loss and fragmentation.', 'Disruption of corridors (caribou are particularly sensitive).', 'Impacts on aquatic systems.', 'Increased access for hunting/trapping.', '**Influenced By (Stressors):**', 'Economic Growth: Demand for resources (timber, oil, minerals).', 'Government Policies: Resource development plans.', 'Global Commodity Prices.', '**Influences (Stressors):**', 'Deforestation (localized around infrastructure).', 'Wildfires (increased access).', 'Pollution (from mining, oil sands).', '**Logic Description:** Linear infrastructure (roads, pipelines) and resource extraction activities (mining, oil sands, forestry) fragment habitat and lead to direct habitat loss, with significant impacts on wildlife, particularly caribou.']
forests_boreal_forests_canadian_stressors["Infrastructure Development"]["Impact on Area"] = 'Habitat fragmentation; direct loss from resource extraction.'
forests_boreal_forests_canadian_stressors["Infrastructure Development"]["Impact on Biodiversity"] = 'Habitat loss and fragmentation.\nDisruption of corridors (caribou are particularly sensitive).\nImpacts on aquatic systems.\nIncreased access for hunting/trapping.\n**Influenced By (Stressors):**\nEconomic Growth: Demand for resources (timber, oil, minerals).\nGovernment Policies: Resource development plans.\nGlobal Commodity Prices.\n**Influences (Stressors):**\nDeforestation (localized around infrastructure).\nWildfires (increased access).\nPollution (from mining, oil sands).\n**Logic Description:** Linear infrastructure (roads, pipelines) and resource extraction activities (mining, oil sands, forestry) fragment habitat and lead to direct habitat loss, with significant impacts on wildlife, particularly caribou.'
forests_boreal_forests_canadian_stressors["Infrastructure Development"]["Influenced By"] = ['Economic Growth: Demand for resources (timber, oil, minerals).', 'Government Policies: Resource development plans.', 'Global Commodity Prices.', '**Influences (Stressors):**', 'Deforestation (localized around infrastructure).', 'Wildfires (increased access).', 'Pollution (from mining, oil sands).', '**Logic Description:** Linear infrastructure (roads, pipelines) and resource extraction activities (mining, oil sands, forestry) fragment habitat and lead to direct habitat loss, with significant impacts on wildlife, particularly caribou.']
forests_boreal_forests_canadian_stressors["Infrastructure Development"]["Influences"] = ['Deforestation (localized around infrastructure).', 'Wildfires (increased access).', 'Pollution (from mining, oil sands).', '**Logic Description:** Linear infrastructure (roads, pipelines) and resource extraction activities (mining, oil sands, forestry) fragment habitat and lead to direct habitat loss, with significant impacts on wildlife, particularly caribou.']
forests_boreal_forests_canadian_stressors["Infrastructure Development"]["Logic Description"] = '---'

# --- Deforestation ---
forests_boreal_forests_canadian_stressors["Deforestation"]["Metric"] = 'Area of forest cleared per year (ha/year) (often associated with logging and conversion to other land uses).'
forests_boreal_forests_canadian_stressors["Deforestation"]["Data Sources"] = ['Canadian government data (National Forest Inventory).', 'Remote sensing.', '**Impact on Area:** Changes in forest age structure; localized forest loss.', '**Impact on Biodiversity:**', 'Habitat loss (especially for species requiring older forest).', 'Changes in species composition.', '**Influenced By (Stressors):**', 'Infrastructure Development (roads).', 'Economic Growth: Demand for timber.', 'Government Policies: Forestry regulations.', '**Influences (Stressors):**', '* Carbon Storage and Sequestration', '**Logic Description:** Logging is a major driver of deforestation, impacting forest age structure and biodiversity. Conversion to agriculture is less common than in some other forest types, but resource extraction (oil sands) can result in significant deforestation.']
forests_boreal_forests_canadian_stressors["Deforestation"]["Impact on Area"] = 'Changes in forest age structure; localized forest loss.'
forests_boreal_forests_canadian_stressors["Deforestation"]["Impact on Biodiversity"] = 'Habitat loss (especially for species requiring older forest).\nChanges in species composition.\n**Influenced By (Stressors):**\nInfrastructure Development (roads).\nEconomic Growth: Demand for timber.\nGovernment Policies: Forestry regulations.\n**Influences (Stressors):**\n* Carbon Storage and Sequestration\n**Logic Description:** Logging is a major driver of deforestation, impacting forest age structure and biodiversity. Conversion to agriculture is less common than in some other forest types, but resource extraction (oil sands) can result in significant deforestation.'
forests_boreal_forests_canadian_stressors["Deforestation"]["Influenced By"] = ['Infrastructure Development (roads).', 'Economic Growth: Demand for timber.', 'Government Policies: Forestry regulations.', '**Influences (Stressors):**', '* Carbon Storage and Sequestration', '**Logic Description:** Logging is a major driver of deforestation, impacting forest age structure and biodiversity. Conversion to agriculture is less common than in some other forest types, but resource extraction (oil sands) can result in significant deforestation.']
forests_boreal_forests_canadian_stressors["Deforestation"]["Influences"] = ['* Carbon Storage and Sequestration', '**Logic Description:** Logging is a major driver of deforestation, impacting forest age structure and biodiversity. Conversion to agriculture is less common than in some other forest types, but resource extraction (oil sands) can result in significant deforestation.']
forests_boreal_forests_canadian_stressors["Deforestation"]["Logic Description"] = '---'

# --- Temperature Increase ---
forests_boreal_forests_canadian_stressors["Temperature Increase"]["Metric"] = 'Average annual temperature increase (°C) (warming is occurring at a faster rate at higher latitudes).'
forests_boreal_forests_canadian_stressors["Temperature Increase"]["Data Sources"] = ['Climate models.', 'Historical records.', '**Impact on Area:** Indirect; thawing permafrost.', '**Impact on Biodiversity:**', 'Shifts in species distributions (northward).', 'Increased stress on boreal species.', 'Changes in phenology.', 'Increased pest/disease outbreaks (e.g., mountain pine beetle).', 'Thawing permafrost impacts forest structure and hydrology.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Wildfires.', 'Changes in Precipitation.', 'Permafrost Thaw.', '* Pest outbreaks', '**Logic Description:** Rapid warming is a major threat, leading to shifts in species distributions, increased pest outbreaks, and thawing permafrost, which has significant impacts on the ecosystem.']
forests_boreal_forests_canadian_stressors["Temperature Increase"]["Impact on Area"] = 'Indirect; thawing permafrost.'
forests_boreal_forests_canadian_stressors["Temperature Increase"]["Impact on Biodiversity"] = 'Shifts in species distributions (northward).\nIncreased stress on boreal species.\nChanges in phenology.\nIncreased pest/disease outbreaks (e.g., mountain pine beetle).\nThawing permafrost impacts forest structure and hydrology.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\n**Influences (Stressors):**\nWildfires.\nChanges in Precipitation.\nPermafrost Thaw.\n* Pest outbreaks\n**Logic Description:** Rapid warming is a major threat, leading to shifts in species distributions, increased pest outbreaks, and thawing permafrost, which has significant impacts on the ecosystem.'
forests_boreal_forests_canadian_stressors["Temperature Increase"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Wildfires.', 'Changes in Precipitation.', 'Permafrost Thaw.', '* Pest outbreaks', '**Logic Description:** Rapid warming is a major threat, leading to shifts in species distributions, increased pest outbreaks, and thawing permafrost, which has significant impacts on the ecosystem.']
forests_boreal_forests_canadian_stressors["Temperature Increase"]["Influences"] = ['Wildfires.', 'Changes in Precipitation.', 'Permafrost Thaw.', '* Pest outbreaks', '**Logic Description:** Rapid warming is a major threat, leading to shifts in species distributions, increased pest outbreaks, and thawing permafrost, which has significant impacts on the ecosystem.']
forests_boreal_forests_canadian_stressors["Temperature Increase"]["Logic Description"] = '---'

# --- Changes in Precipitation ---
forests_boreal_forests_canadian_stressors["Changes in Precipitation"]["Metric"] = 'Change in annual precipitation (mm/year); changes in snowpack; changes in seasonality.'
forests_boreal_forests_canadian_stressors["Changes in Precipitation"]["Data Sources"] = ['Climate models.', 'Historical records.', '**Impact on Area:** Indirect; changes in water availability and permafrost.', '**Impact on Biodiversity:**', 'Changes in species composition.', 'Altered streamflow.', 'Increased drought stress (in some areas).', 'Changes in wetland extent.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Wildfires.', '* Permafrost Thaw', '* Water availability', '**Logic Description:** Changes in precipitation patterns, including changes in snowpack and the timing of precipitation, impact water availability and ecosystem processes.']
forests_boreal_forests_canadian_stressors["Changes in Precipitation"]["Impact on Area"] = 'Indirect; changes in water availability and permafrost.'
forests_boreal_forests_canadian_stressors["Changes in Precipitation"]["Impact on Biodiversity"] = 'Changes in species composition.\nAltered streamflow.\nIncreased drought stress (in some areas).\nChanges in wetland extent.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\n**Influences (Stressors):**\nWildfires.\n* Permafrost Thaw\n* Water availability\n**Logic Description:** Changes in precipitation patterns, including changes in snowpack and the timing of precipitation, impact water availability and ecosystem processes.'
forests_boreal_forests_canadian_stressors["Changes in Precipitation"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Wildfires.', '* Permafrost Thaw', '* Water availability', '**Logic Description:** Changes in precipitation patterns, including changes in snowpack and the timing of precipitation, impact water availability and ecosystem processes.']
forests_boreal_forests_canadian_stressors["Changes in Precipitation"]["Influences"] = ['Wildfires.', '* Permafrost Thaw', '* Water availability', '**Logic Description:** Changes in precipitation patterns, including changes in snowpack and the timing of precipitation, impact water availability and ecosystem processes.']
forests_boreal_forests_canadian_stressors["Changes in Precipitation"]["Logic Description"] = '---'

# --- Wildfires ---
forests_boreal_forests_canadian_stressors["Wildfires"]["Metric"] = 'Number of fires; area burned (ha/year).'
forests_boreal_forests_canadian_stressors["Wildfires"]["Data Sources"] = ['Canadian government data (Canadian Wildland Fire Information System).', 'Remote sensing.', '**Impact on Area:** Direct loss of forest area; changes in forest structure and age.', '**Impact on Biodiversity:**', 'Mortality.', 'Habitat loss.', 'Changes in species composition (favoring fire-adapted species).', '* Large carbon emissions', '**Influenced By (Stressors):**', 'Temperature Increase (longer fire season, drier conditions).', 'Changes in Precipitation (drought).', 'Insect outbreaks (creating dead trees).', 'Lightning strikes (natural ignition source).', '*  Human Activities', '**Influences (Stressors):**', '* Air Quality', '* Future Fire Risk', '* Carbon cycle', '**Logic Description:** Wildfires are a natural part of the boreal ecosystem, but their frequency and intensity are increasing due to climate change, leading to significant impacts on forest structure, biodiversity, and the carbon cycle.']
forests_boreal_forests_canadian_stressors["Wildfires"]["Impact on Area"] = 'Direct loss of forest area; changes in forest structure and age.'
forests_boreal_forests_canadian_stressors["Wildfires"]["Impact on Biodiversity"] = 'Mortality.\nHabitat loss.\nChanges in species composition (favoring fire-adapted species).\n* Large carbon emissions\n**Influenced By (Stressors):**\nTemperature Increase (longer fire season, drier conditions).\nChanges in Precipitation (drought).\nInsect outbreaks (creating dead trees).\nLightning strikes (natural ignition source).\n*  Human Activities\n**Influences (Stressors):**\n* Air Quality\n* Future Fire Risk\n* Carbon cycle\n**Logic Description:** Wildfires are a natural part of the boreal ecosystem, but their frequency and intensity are increasing due to climate change, leading to significant impacts on forest structure, biodiversity, and the carbon cycle.'
forests_boreal_forests_canadian_stressors["Wildfires"]["Influenced By"] = ['Temperature Increase (longer fire season, drier conditions).', 'Changes in Precipitation (drought).', 'Insect outbreaks (creating dead trees).', 'Lightning strikes (natural ignition source).', '*  Human Activities', '**Influences (Stressors):**', '* Air Quality', '* Future Fire Risk', '* Carbon cycle', '**Logic Description:** Wildfires are a natural part of the boreal ecosystem, but their frequency and intensity are increasing due to climate change, leading to significant impacts on forest structure, biodiversity, and the carbon cycle.']
forests_boreal_forests_canadian_stressors["Wildfires"]["Influences"] = ['* Air Quality', '* Future Fire Risk', '* Carbon cycle', '**Logic Description:** Wildfires are a natural part of the boreal ecosystem, but their frequency and intensity are increasing due to climate change, leading to significant impacts on forest structure, biodiversity, and the carbon cycle.']
forests_boreal_forests_canadian_stressors["Wildfires"]["Logic Description"] = '---'

# --- Permafrost Thaw ---
forests_boreal_forests_canadian_stressors["Permafrost Thaw"]["Metric"] = 'Active layer thickness (depth of soil that thaws each summer) (cm); area of permafrost degradation (ha).'
forests_boreal_forests_canadian_stressors["Permafrost Thaw"]["Data Sources"] = ['Field measurements.', 'Remote sensing (e.g., measuring ground subsidence).', 'Climate models.', '**Impact on Area:** Changes in ground stability; altered hydrology; release of greenhouse gases.', '**Impact on Biodiversity:**', 'Changes in vegetation composition (e.g., shift from forests to wetlands).', 'Impacts on infrastructure (roads, buildings).', 'Release of methane and carbon dioxide (positive feedback to climate change).', '**Influenced By (Stressors):**', 'Temperature Increase.', 'Changes in Precipitation (snow cover).', 'Wildfires (removing insulating vegetation).', '* Infrastructure Development', '**Influences (Stressors):**', 'Climate Change (through greenhouse gas emissions).', '* Hydrology', '* Habitat availability', '**Logic Description:** Thawing permafrost, driven by warming temperatures, leads to ground instability, altered hydrology, and the release of large amounts of greenhouse gases (methane and carbon dioxide), creating a positive feedback loop that accelerates climate change.']
forests_boreal_forests_canadian_stressors["Permafrost Thaw"]["Impact on Area"] = 'Changes in ground stability; altered hydrology; release of greenhouse gases.'
forests_boreal_forests_canadian_stressors["Permafrost Thaw"]["Impact on Biodiversity"] = 'Changes in vegetation composition (e.g., shift from forests to wetlands).\nImpacts on infrastructure (roads, buildings).\nRelease of methane and carbon dioxide (positive feedback to climate change).\n**Influenced By (Stressors):**\nTemperature Increase.\nChanges in Precipitation (snow cover).\nWildfires (removing insulating vegetation).\n* Infrastructure Development\n**Influences (Stressors):**\nClimate Change (through greenhouse gas emissions).\n* Hydrology\n* Habitat availability\n**Logic Description:** Thawing permafrost, driven by warming temperatures, leads to ground instability, altered hydrology, and the release of large amounts of greenhouse gases (methane and carbon dioxide), creating a positive feedback loop that accelerates climate change.'
forests_boreal_forests_canadian_stressors["Permafrost Thaw"]["Influenced By"] = ['Temperature Increase.', 'Changes in Precipitation (snow cover).', 'Wildfires (removing insulating vegetation).', '* Infrastructure Development', '**Influences (Stressors):**', 'Climate Change (through greenhouse gas emissions).', '* Hydrology', '* Habitat availability', '**Logic Description:** Thawing permafrost, driven by warming temperatures, leads to ground instability, altered hydrology, and the release of large amounts of greenhouse gases (methane and carbon dioxide), creating a positive feedback loop that accelerates climate change.']
forests_boreal_forests_canadian_stressors["Permafrost Thaw"]["Influences"] = ['Climate Change (through greenhouse gas emissions).', '* Hydrology', '* Habitat availability', '**Logic Description:** Thawing permafrost, driven by warming temperatures, leads to ground instability, altered hydrology, and the release of large amounts of greenhouse gases (methane and carbon dioxide), creating a positive feedback loop that accelerates climate change.']
forests_boreal_forests_canadian_stressors["Permafrost Thaw"]["Logic Description"] = '---'

# --- Invasive Species ---
forests_boreal_forests_canadian_stressors["Invasive Species"]["Metric"] = 'Distribution and abundance of key invasive species.'
forests_boreal_forests_canadian_stressors["Invasive Species"]["Data Sources"] = ['* Forest Health Monitoring.', '* Research.', '**Impact on Area:** Changes in forest structure.', '**Impact on Biodiversity:**', '* Competition.', '* Altered processes.', '**Influenced By (Stressors):**', '* Disturbance.', '* Climate change.', '**Influences (Stressors):**', '* Forest composition', '**Logic Description:** Invasive species impact.']
forests_boreal_forests_canadian_stressors["Invasive Species"]["Impact on Area"] = 'Changes in forest structure.'
forests_boreal_forests_canadian_stressors["Invasive Species"]["Impact on Biodiversity"] = '* Competition.\n* Altered processes.\n**Influenced By (Stressors):**\n* Disturbance.\n* Climate change.\n**Influences (Stressors):**\n* Forest composition\n**Logic Description:** Invasive species impact.'
forests_boreal_forests_canadian_stressors["Invasive Species"]["Influenced By"] = ['* Disturbance.', '* Climate change.', '**Influences (Stressors):**', '* Forest composition', '**Logic Description:** Invasive species impact.']
forests_boreal_forests_canadian_stressors["Invasive Species"]["Influences"] = ['* Forest composition', '**Logic Description:** Invasive species impact.']
forests_boreal_forests_canadian_stressors["Invasive Species"]["Logic Description"] = '---'

