from stressor_templates import *
import copy

forests_boreal_forests_russian_stressors = {
    "Infrastructure Development": copy.deepcopy(infrastructure_development_template),
    "Deforestation": copy.deepcopy(deforestation_template),
    "Temperature Increase": copy.deepcopy(climate_change_template),
    "Changes in Precipitation": copy.deepcopy(climate_change_template),
    "Wildfires": copy.deepcopy(fire_regime_template),
    "Permafrost Thaw": {},
    "Invasive Species": copy.deepcopy(invasive_species_template),
}

# --- Infrastructure Development ---
forests_boreal_forests_russian_stressors["Infrastructure Development"]["Metric"] = 'Road density (km/km²); area affected by resource extraction (mining, oil and gas, forestry) (ha/year).'
forests_boreal_forests_russian_stressors["Infrastructure Development"]["Data Sources"] = ['Russian government data (where available).', 'Remote sensing.', 'Reports from environmental organizations and research institutions.', '**Impact on Area:** Habitat fragmentation; direct loss.', '**Impact on Biodiversity:** Same as Canadian Boreal Forest', '**Influenced By (Stressors):**', 'Economic Growth: Resource extraction.', 'Government Policies.', 'Global Commodity Prices.', '**Influences (Stressors):**', '* Deforestation.', 'Wildfires.', '* Pollution', '**Logic Description:** Similar to Canada, but with potentially less stringent environmental regulations and enforcement in some areas. Resource extraction (oil, gas, minerals, timber) is a major driver.']
forests_boreal_forests_russian_stressors["Infrastructure Development"]["Impact on Area"] = 'Habitat fragmentation; direct loss.'
forests_boreal_forests_russian_stressors["Infrastructure Development"]["Impact on Biodiversity"] = '**Influenced By (Stressors):**\nEconomic Growth: Resource extraction.\nGovernment Policies.\nGlobal Commodity Prices.\n**Influences (Stressors):**\n* Deforestation.\nWildfires.\n* Pollution\n**Logic Description:** Similar to Canada, but with potentially less stringent environmental regulations and enforcement in some areas. Resource extraction (oil, gas, minerals, timber) is a major driver.'
forests_boreal_forests_russian_stressors["Infrastructure Development"]["Influenced By"] = ['Economic Growth: Resource extraction.', 'Government Policies.', 'Global Commodity Prices.', '**Influences (Stressors):**', '* Deforestation.', 'Wildfires.', '* Pollution', '**Logic Description:** Similar to Canada, but with potentially less stringent environmental regulations and enforcement in some areas. Resource extraction (oil, gas, minerals, timber) is a major driver.']
forests_boreal_forests_russian_stressors["Infrastructure Development"]["Influences"] = ['* Deforestation.', 'Wildfires.', '* Pollution', '**Logic Description:** Similar to Canada, but with potentially less stringent environmental regulations and enforcement in some areas. Resource extraction (oil, gas, minerals, timber) is a major driver.']
forests_boreal_forests_russian_stressors["Infrastructure Development"]["Logic Description"] = '---'
forests_boreal_forests_russian_stressors["Infrastructure Development"]["Impact Function"] = "impact_infrastructure_development_forests_boreal_forests_russian"

# --- Deforestation ---
forests_boreal_forests_russian_stressors["Deforestation"]["Metric"] = 'Area of forest cleared per year (ha/year).'
forests_boreal_forests_russian_stressors["Deforestation"]["Data Sources"] = ['Russian government data (where available).', 'Remote sensing.', 'Reports from environmental organizations.', '**Impact on Area:** Changes in forest age structure; localized loss.', '**Impact on Biodiversity:** Same as Canadian Boreal Forest', '**Influenced By (Stressors):**', 'Infrastructure Development.', 'Economic Growth: Demand for timber (legal and illegal logging).', 'Government Policies.', '**Influences (Stressors):**', '* Carbon Cycle', '**Logic Description:** Logging (both legal and illegal) is a major driver of deforestation.']
forests_boreal_forests_russian_stressors["Deforestation"]["Impact on Area"] = 'Changes in forest age structure; localized loss.'
forests_boreal_forests_russian_stressors["Deforestation"]["Impact on Biodiversity"] = '**Influenced By (Stressors):**\nInfrastructure Development.\nEconomic Growth: Demand for timber (legal and illegal logging).\nGovernment Policies.\n**Influences (Stressors):**\n* Carbon Cycle\n**Logic Description:** Logging (both legal and illegal) is a major driver of deforestation.'
forests_boreal_forests_russian_stressors["Deforestation"]["Influenced By"] = ['Infrastructure Development.', 'Economic Growth: Demand for timber (legal and illegal logging).', 'Government Policies.', '**Influences (Stressors):**', '* Carbon Cycle', '**Logic Description:** Logging (both legal and illegal) is a major driver of deforestation.']
forests_boreal_forests_russian_stressors["Deforestation"]["Influences"] = ['* Carbon Cycle', '**Logic Description:** Logging (both legal and illegal) is a major driver of deforestation.']
forests_boreal_forests_russian_stressors["Deforestation"]["Logic Description"] = '---'
forests_boreal_forests_russian_stressors["Deforestation"]["Impact Function"] = "impact_deforestation_forests_boreal_forests_russian"

# --- Temperature Increase ---
forests_boreal_forests_russian_stressors["Temperature Increase"]["Metric"] = 'Average annual temperature increase (°C).'
forests_boreal_forests_russian_stressors["Temperature Increase"]["Data Sources"] = ['Climate models.', 'Historical records.', '**Impact on Area:** Indirect; thawing permafrost.', '**Impact on Biodiversity:** Same as Canadian Boreal Forest, plus increased risk of Siberian silk moth outbreaks.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Wildfires.', 'Changes in Precipitation.', 'Permafrost Thaw.', '* Insect outbreaks', '**Logic Description:** Similar to Canada, with rapid warming and significant impacts from thawing permafrost.']
forests_boreal_forests_russian_stressors["Temperature Increase"]["Impact on Area"] = 'Indirect; thawing permafrost.'
forests_boreal_forests_russian_stressors["Temperature Increase"]["Impact on Biodiversity"] = '**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\n**Influences (Stressors):**\nWildfires.\nChanges in Precipitation.\nPermafrost Thaw.\n* Insect outbreaks\n**Logic Description:** Similar to Canada, with rapid warming and significant impacts from thawing permafrost.'
forests_boreal_forests_russian_stressors["Temperature Increase"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Wildfires.', 'Changes in Precipitation.', 'Permafrost Thaw.', '* Insect outbreaks', '**Logic Description:** Similar to Canada, with rapid warming and significant impacts from thawing permafrost.']
forests_boreal_forests_russian_stressors["Temperature Increase"]["Influences"] = ['Wildfires.', 'Changes in Precipitation.', 'Permafrost Thaw.', '* Insect outbreaks', '**Logic Description:** Similar to Canada, with rapid warming and significant impacts from thawing permafrost.']
forests_boreal_forests_russian_stressors["Temperature Increase"]["Logic Description"] = '---'
forests_boreal_forests_russian_stressors["Temperature Increase"]["Impact Function"] = "impact_temperature_increase_forests_boreal_forests_russian"

# --- Changes in Precipitation ---
forests_boreal_forests_russian_stressors["Changes in Precipitation"]["Metric"] = 'Change in annual precipitation (mm/year); changes in snowpack; seasonality.'
forests_boreal_forests_russian_stressors["Changes in Precipitation"]["Data Sources"] = ['Climate models.', 'Historical records.', '**Impact on Area:** Indirect; changes in water availability and permafrost.', '**Impact on Biodiversity:** Same as Canadian Boreal Forest', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', '* Wildfires.', '* Permafrost Thaw', '* Water Resources', '**Logic Description:** Similar to Canada.']
forests_boreal_forests_russian_stressors["Changes in Precipitation"]["Impact on Area"] = 'Indirect; changes in water availability and permafrost.'
forests_boreal_forests_russian_stressors["Changes in Precipitation"]["Impact on Biodiversity"] = '**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\n**Influences (Stressors):**\n* Wildfires.\n* Permafrost Thaw\n* Water Resources\n**Logic Description:** Similar to Canada.'
forests_boreal_forests_russian_stressors["Changes in Precipitation"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', '* Wildfires.', '* Permafrost Thaw', '* Water Resources', '**Logic Description:** Similar to Canada.']
forests_boreal_forests_russian_stressors["Changes in Precipitation"]["Influences"] = ['* Wildfires.', '* Permafrost Thaw', '* Water Resources', '**Logic Description:** Similar to Canada.']
forests_boreal_forests_russian_stressors["Changes in Precipitation"]["Logic Description"] = '---'
forests_boreal_forests_russian_stressors["Changes in Precipitation"]["Impact Function"] = "impact_changes_in_precipitation_forests_boreal_forests_russian"

# --- Wildfires ---
forests_boreal_forests_russian_stressors["Wildfires"]["Metric"] = 'Number of fires; area burned (ha/year).'
forests_boreal_forests_russian_stressors["Wildfires"]["Data Sources"] = ['Russian government data (where available).', 'Remote sensing.', 'Reports from environmental organizations.', '**Impact on Area:** Direct loss of forest; changes in structure and age.', '**Impact on Biodiversity:** Same as Canadian Boreal Forest, potentially larger scale.', '**Influenced By (Stressors):**', 'Temperature Increase.', 'Changes in Precipitation.', 'Insect outbreaks.', 'Lightning strikes.', '* Human Activities', '* Inadequate Fire Management', '**Influences (Stressors):**', '* Air quality', '* Future Risk', '* Carbon cycle', '**Logic Description:** Wildfires are a massive and growing problem in the Russian Boreal Forest, driven by climate change and, in some cases, inadequate fire management.']
forests_boreal_forests_russian_stressors["Wildfires"]["Impact on Area"] = 'Direct loss of forest; changes in structure and age.'
forests_boreal_forests_russian_stressors["Wildfires"]["Impact on Biodiversity"] = '**Influenced By (Stressors):**\nTemperature Increase.\nChanges in Precipitation.\nInsect outbreaks.\nLightning strikes.\n* Human Activities\n* Inadequate Fire Management\n**Influences (Stressors):**\n* Air quality\n* Future Risk\n* Carbon cycle\n**Logic Description:** Wildfires are a massive and growing problem in the Russian Boreal Forest, driven by climate change and, in some cases, inadequate fire management.'
forests_boreal_forests_russian_stressors["Wildfires"]["Influenced By"] = ['Temperature Increase.', 'Changes in Precipitation.', 'Insect outbreaks.', 'Lightning strikes.', '* Human Activities', '* Inadequate Fire Management', '**Influences (Stressors):**', '* Air quality', '* Future Risk', '* Carbon cycle', '**Logic Description:** Wildfires are a massive and growing problem in the Russian Boreal Forest, driven by climate change and, in some cases, inadequate fire management.']
forests_boreal_forests_russian_stressors["Wildfires"]["Influences"] = ['* Air quality', '* Future Risk', '* Carbon cycle', '**Logic Description:** Wildfires are a massive and growing problem in the Russian Boreal Forest, driven by climate change and, in some cases, inadequate fire management.']
forests_boreal_forests_russian_stressors["Wildfires"]["Logic Description"] = '---'
forests_boreal_forests_russian_stressors["Wildfires"]["Impact Function"] = "impact_wildfires_forests_boreal_forests_russian"

# --- Permafrost Thaw ---
forests_boreal_forests_russian_stressors["Permafrost Thaw"]["Metric"] = 'Active layer thickness (cm); area of permafrost degradation (ha).'
forests_boreal_forests_russian_stressors["Permafrost Thaw"]["Data Sources"] = ['Field measurements.', 'Remote sensing.', 'Climate models.', '**Impact on Area:** Changes in ground stability; altered hydrology; greenhouse gas release.', '**Impact on Biodiversity:** Same as Canadian Boreal Forest', '**Influenced By (Stressors):**', 'Temperature Increase.', 'Changes in Precipitation (snow cover).', 'Wildfires.', '* Infrastructure development', '**Influences (Stressors):**', 'Climate Change (through greenhouse gas emissions).', '* Hydrology', '* Habitat Loss', '**Logic Description:** Similar to Canada, with vast areas of permafrost and significant potential for greenhouse gas release.']
forests_boreal_forests_russian_stressors["Permafrost Thaw"]["Impact on Area"] = 'Changes in ground stability; altered hydrology; greenhouse gas release.'
forests_boreal_forests_russian_stressors["Permafrost Thaw"]["Impact on Biodiversity"] = '**Influenced By (Stressors):**\nTemperature Increase.\nChanges in Precipitation (snow cover).\nWildfires.\n* Infrastructure development\n**Influences (Stressors):**\nClimate Change (through greenhouse gas emissions).\n* Hydrology\n* Habitat Loss\n**Logic Description:** Similar to Canada, with vast areas of permafrost and significant potential for greenhouse gas release.'
forests_boreal_forests_russian_stressors["Permafrost Thaw"]["Influenced By"] = ['Temperature Increase.', 'Changes in Precipitation (snow cover).', 'Wildfires.', '* Infrastructure development', '**Influences (Stressors):**', 'Climate Change (through greenhouse gas emissions).', '* Hydrology', '* Habitat Loss', '**Logic Description:** Similar to Canada, with vast areas of permafrost and significant potential for greenhouse gas release.']
forests_boreal_forests_russian_stressors["Permafrost Thaw"]["Influences"] = ['Climate Change (through greenhouse gas emissions).', '* Hydrology', '* Habitat Loss', '**Logic Description:** Similar to Canada, with vast areas of permafrost and significant potential for greenhouse gas release.']
forests_boreal_forests_russian_stressors["Permafrost Thaw"]["Logic Description"] = '---'
forests_boreal_forests_russian_stressors["Permafrost Thaw"]["Impact Function"] = "impact_permafrost_thaw_forests_boreal_forests_russian"

# --- Invasive Species ---
forests_boreal_forests_russian_stressors["Invasive Species"]["Metric"] = 'Distribution and abundance of key invasive species.'
forests_boreal_forests_russian_stressors["Invasive Species"]["Data Sources"] = ['* Forest Health Monitoring.', '* Research.', '**Impact on Area:** Changes in forest structure.', '**Impact on Biodiversity:**', '* Competition.', '* Altered processes.', '**Influenced By (Stressors):**', '* Disturbance.', '* Climate change.', '**Influences (Stressors):**', '* Forest composition', '**Logic Description:** Invasive species impact.']
forests_boreal_forests_russian_stressors["Invasive Species"]["Impact on Area"] = 'Changes in forest structure.'
forests_boreal_forests_russian_stressors["Invasive Species"]["Impact on Biodiversity"] = '* Competition.\n* Altered processes.\n**Influenced By (Stressors):**\n* Disturbance.\n* Climate change.\n**Influences (Stressors):**\n* Forest composition\n**Logic Description:** Invasive species impact.'
forests_boreal_forests_russian_stressors["Invasive Species"]["Influenced By"] = ['* Disturbance.', '* Climate change.', '**Influences (Stressors):**', '* Forest composition', '**Logic Description:** Invasive species impact.']
forests_boreal_forests_russian_stressors["Invasive Species"]["Influences"] = ['* Forest composition', '**Logic Description:** Invasive species impact.']
forests_boreal_forests_russian_stressors["Invasive Species"]["Logic Description"] = '---'
forests_boreal_forests_russian_stressors["Invasive Species"]["Impact Function"] = "impact_invasive_species_forests_boreal_forests_russian"

