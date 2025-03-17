from stressor_templates import *
import copy

forests_boreal_forests_scandinavian_and_finnish_stressors = {
    "Infrastructure Development": copy.deepcopy(infrastructure_development_template),
    "Deforestation": copy.deepcopy(deforestation_template),
    "Temperature Increase": copy.deepcopy(climate_change_template),
    "Changes in Precipitation": copy.deepcopy(climate_change_template),
    "Wildfires": copy.deepcopy(fire_regime_template),
    "Invasive Species": copy.deepcopy(invasive_species_template),
}

# --- Infrastructure Development ---
forests_boreal_forests_scandinavian_and_finnish_stressors["Infrastructure Development"]["Metric"] = 'Road density (km/km²); area affected by forestry operations (ha/year).'
forests_boreal_forests_scandinavian_and_finnish_stressors["Infrastructure Development"]["Data Sources"] = ['National government statistics (Finland, Sweden, Norway).', 'Remote sensing.', '**Impact on Area:** Habitat fragmentation.', '**Impact on Biodiversity:**', 'Habitat loss and fragmentation.', 'Disruption of corridors.', '**Influenced By (Stressors):**', 'Economic Growth: Demand for timber.', 'Government Policies: Forestry regulations.', '**Influences (Stressors):**', 'Deforestation (localized).', '**Logic Description:** Forestry is a major industry, and related infrastructure (roads) contributes to fragmentation.']
forests_boreal_forests_scandinavian_and_finnish_stressors["Infrastructure Development"]["Impact on Area"] = 'Habitat fragmentation.'
forests_boreal_forests_scandinavian_and_finnish_stressors["Infrastructure Development"]["Impact on Biodiversity"] = 'Habitat loss and fragmentation.\nDisruption of corridors.\n**Influenced By (Stressors):**\nEconomic Growth: Demand for timber.\nGovernment Policies: Forestry regulations.\n**Influences (Stressors):**\nDeforestation (localized).\n**Logic Description:** Forestry is a major industry, and related infrastructure (roads) contributes to fragmentation.'
forests_boreal_forests_scandinavian_and_finnish_stressors["Infrastructure Development"]["Influenced By"] = ['Economic Growth: Demand for timber.', 'Government Policies: Forestry regulations.', '**Influences (Stressors):**', 'Deforestation (localized).', '**Logic Description:** Forestry is a major industry, and related infrastructure (roads) contributes to fragmentation.']
forests_boreal_forests_scandinavian_and_finnish_stressors["Infrastructure Development"]["Influences"] = ['Deforestation (localized).', '**Logic Description:** Forestry is a major industry, and related infrastructure (roads) contributes to fragmentation.']
forests_boreal_forests_scandinavian_and_finnish_stressors["Infrastructure Development"]["Logic Description"] = '---'
forests_boreal_forests_scandinavian_and_finnish_stressors["Infrastructure Development"]["Impact Function"] = "impact_infrastructure_development_forests_boreal_forests_scandinavian_and_finnish"

# --- Deforestation ---
forests_boreal_forests_scandinavian_and_finnish_stressors["Deforestation"]["Metric"] = 'Area of forest cleared per year (ha/year) (often related to forestry).'
forests_boreal_forests_scandinavian_and_finnish_stressors["Deforestation"]["Data Sources"] = ['National forest inventories.', 'Remote sensing.', '**Impact on Area:** Changes in forest age structure; localized forest loss.', '**Impact on Biodiversity:** Impacts are generally less severe than in Canada or Russia due to more intensive forest management, but loss of old-growth patches is still a concern.', '**Influenced By (Stressors):**', '* Infrastructure', '* Economic Growth', 'Government Policies: Forestry regulations.', '**Influences (Stressors):**', '* Carbon Cycle', '**Logic Description:** Intensive forestry practices, while often including reforestation, can still impact biodiversity through changes in forest age structure and loss of old-growth characteristics.']
forests_boreal_forests_scandinavian_and_finnish_stressors["Deforestation"]["Impact on Area"] = 'Changes in forest age structure; localized forest loss.'
forests_boreal_forests_scandinavian_and_finnish_stressors["Deforestation"]["Impact on Biodiversity"] = '**Influenced By (Stressors):**\n* Infrastructure\n* Economic Growth\nGovernment Policies: Forestry regulations.\n**Influences (Stressors):**\n* Carbon Cycle\n**Logic Description:** Intensive forestry practices, while often including reforestation, can still impact biodiversity through changes in forest age structure and loss of old-growth characteristics.'
forests_boreal_forests_scandinavian_and_finnish_stressors["Deforestation"]["Influenced By"] = ['* Infrastructure', '* Economic Growth', 'Government Policies: Forestry regulations.', '**Influences (Stressors):**', '* Carbon Cycle', '**Logic Description:** Intensive forestry practices, while often including reforestation, can still impact biodiversity through changes in forest age structure and loss of old-growth characteristics.']
forests_boreal_forests_scandinavian_and_finnish_stressors["Deforestation"]["Influences"] = ['* Carbon Cycle', '**Logic Description:** Intensive forestry practices, while often including reforestation, can still impact biodiversity through changes in forest age structure and loss of old-growth characteristics.']
forests_boreal_forests_scandinavian_and_finnish_stressors["Deforestation"]["Logic Description"] = '---'
forests_boreal_forests_scandinavian_and_finnish_stressors["Deforestation"]["Impact Function"] = "impact_deforestation_forests_boreal_forests_scandinavian_and_finnish"

# --- Temperature Increase ---
forests_boreal_forests_scandinavian_and_finnish_stressors["Temperature Increase"]["Metric"] = 'Average annual temperature increase (°C).'
forests_boreal_forests_scandinavian_and_finnish_stressors["Temperature Increase"]["Data Sources"] = ['Climate models.', 'Historical records.', '**Impact on Area:** Indirect.', '**Impact on Biodiversity:**', 'Species shifts (northward).', 'Increased stress on boreal species.', 'Changes in phenology.', 'Increased pest/disease outbreaks.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Wildfires.', 'Changes in Precipitation.', '* Pest outbreaks', '**Logic Description:** Similar to other boreal regions, with rapid warming.']
forests_boreal_forests_scandinavian_and_finnish_stressors["Temperature Increase"]["Impact on Area"] = 'Indirect.'
forests_boreal_forests_scandinavian_and_finnish_stressors["Temperature Increase"]["Impact on Biodiversity"] = 'Species shifts (northward).\nIncreased stress on boreal species.\nChanges in phenology.\nIncreased pest/disease outbreaks.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\n**Influences (Stressors):**\nWildfires.\nChanges in Precipitation.\n* Pest outbreaks\n**Logic Description:** Similar to other boreal regions, with rapid warming.'
forests_boreal_forests_scandinavian_and_finnish_stressors["Temperature Increase"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Wildfires.', 'Changes in Precipitation.', '* Pest outbreaks', '**Logic Description:** Similar to other boreal regions, with rapid warming.']
forests_boreal_forests_scandinavian_and_finnish_stressors["Temperature Increase"]["Influences"] = ['Wildfires.', 'Changes in Precipitation.', '* Pest outbreaks', '**Logic Description:** Similar to other boreal regions, with rapid warming.']
forests_boreal_forests_scandinavian_and_finnish_stressors["Temperature Increase"]["Logic Description"] = '---'
forests_boreal_forests_scandinavian_and_finnish_stressors["Temperature Increase"]["Impact Function"] = "impact_temperature_increase_forests_boreal_forests_scandinavian_and_finnish"

# --- Changes in Precipitation ---
forests_boreal_forests_scandinavian_and_finnish_stressors["Changes in Precipitation"]["Metric"] = 'Change in annual precipitation (mm/year); changes in snowpack; seasonality.'
forests_boreal_forests_scandinavian_and_finnish_stressors["Changes in Precipitation"]["Data Sources"] = ['Climate models.', 'Historical records.', '**Impact on Area:** Indirect; changes in water availability.', '**Impact on Biodiversity:**', 'Changes in species composition.', 'Altered streamflow.', '* Increased risk of drought', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Wildfires (though less of a threat than in drier boreal regions).', '* Water Resources', '**Logic Description:** Changes in precipitation patterns impact water availability and ecosystem function.']
forests_boreal_forests_scandinavian_and_finnish_stressors["Changes in Precipitation"]["Impact on Area"] = 'Indirect; changes in water availability.'
forests_boreal_forests_scandinavian_and_finnish_stressors["Changes in Precipitation"]["Impact on Biodiversity"] = 'Changes in species composition.\nAltered streamflow.\n* Increased risk of drought\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\n**Influences (Stressors):**\nWildfires (though less of a threat than in drier boreal regions).\n* Water Resources\n**Logic Description:** Changes in precipitation patterns impact water availability and ecosystem function.'
forests_boreal_forests_scandinavian_and_finnish_stressors["Changes in Precipitation"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Wildfires (though less of a threat than in drier boreal regions).', '* Water Resources', '**Logic Description:** Changes in precipitation patterns impact water availability and ecosystem function.']
forests_boreal_forests_scandinavian_and_finnish_stressors["Changes in Precipitation"]["Influences"] = ['Wildfires (though less of a threat than in drier boreal regions).', '* Water Resources', '**Logic Description:** Changes in precipitation patterns impact water availability and ecosystem function.']
forests_boreal_forests_scandinavian_and_finnish_stressors["Changes in Precipitation"]["Logic Description"] = '---'
forests_boreal_forests_scandinavian_and_finnish_stressors["Changes in Precipitation"]["Impact Function"] = "impact_changes_in_precipitation_forests_boreal_forests_scandinavian_and_finnish"

# --- Wildfires ---
forests_boreal_forests_scandinavian_and_finnish_stressors["Wildfires"]["Metric"] = 'Number of fires; area burned (ha/year).'
forests_boreal_forests_scandinavian_and_finnish_stressors["Wildfires"]["Data Sources"] = ['National fire statistics.', 'Remote sensing.', '**Impact on Area:** Direct loss of forest area; changes in structure.', '**Impact on Biodiversity:** Generally less severe than in Canada or Russia due to more intensive fire management and wetter conditions, but still a concern.', '**Influenced By (Stressors):**', 'Temperature Increase.', 'Changes in Precipitation (drought).', 'Human Activities.', '**Influences (Stressors):**', '* Air Quality', '* Future Risk', '* Carbon Cycle', '**Logic Description:** Wildfires are a concern, and their risk may increase with climate change, but they are generally less frequent and extensive than in other boreal regions.']
forests_boreal_forests_scandinavian_and_finnish_stressors["Wildfires"]["Impact on Area"] = 'Direct loss of forest area; changes in structure.'
forests_boreal_forests_scandinavian_and_finnish_stressors["Wildfires"]["Impact on Biodiversity"] = '**Influenced By (Stressors):**\nTemperature Increase.\nChanges in Precipitation (drought).\nHuman Activities.\n**Influences (Stressors):**\n* Air Quality\n* Future Risk\n* Carbon Cycle\n**Logic Description:** Wildfires are a concern, and their risk may increase with climate change, but they are generally less frequent and extensive than in other boreal regions.'
forests_boreal_forests_scandinavian_and_finnish_stressors["Wildfires"]["Influenced By"] = ['Temperature Increase.', 'Changes in Precipitation (drought).', 'Human Activities.', '**Influences (Stressors):**', '* Air Quality', '* Future Risk', '* Carbon Cycle', '**Logic Description:** Wildfires are a concern, and their risk may increase with climate change, but they are generally less frequent and extensive than in other boreal regions.']
forests_boreal_forests_scandinavian_and_finnish_stressors["Wildfires"]["Influences"] = ['* Air Quality', '* Future Risk', '* Carbon Cycle', '**Logic Description:** Wildfires are a concern, and their risk may increase with climate change, but they are generally less frequent and extensive than in other boreal regions.']
forests_boreal_forests_scandinavian_and_finnish_stressors["Wildfires"]["Logic Description"] = '---'
forests_boreal_forests_scandinavian_and_finnish_stressors["Wildfires"]["Impact Function"] = "impact_wildfires_forests_boreal_forests_scandinavian_and_finnish"

# --- Invasive Species ---
forests_boreal_forests_scandinavian_and_finnish_stressors["Invasive Species"]["Metric"] = 'Distribution and abundance of key invasive species.'
forests_boreal_forests_scandinavian_and_finnish_stressors["Invasive Species"]["Data Sources"] = ['* Forest Health Monitoring.', '* Research.', '**Impact on Area:** Changes in forest structure.', '**Impact on Biodiversity:**', '* Competition.', '* Altered processes.', '**Influenced By (Stressors):**', '* Disturbance.', '* Climate change.', '**Influences (Stressors):**', '* Forest composition', '**Logic Description:** Invasive species impact.']
forests_boreal_forests_scandinavian_and_finnish_stressors["Invasive Species"]["Impact on Area"] = 'Changes in forest structure.'
forests_boreal_forests_scandinavian_and_finnish_stressors["Invasive Species"]["Impact on Biodiversity"] = '* Competition.\n* Altered processes.\n**Influenced By (Stressors):**\n* Disturbance.\n* Climate change.\n**Influences (Stressors):**\n* Forest composition\n**Logic Description:** Invasive species impact.'
forests_boreal_forests_scandinavian_and_finnish_stressors["Invasive Species"]["Influenced By"] = ['* Disturbance.', '* Climate change.', '**Influences (Stressors):**', '* Forest composition', '**Logic Description:** Invasive species impact.']
forests_boreal_forests_scandinavian_and_finnish_stressors["Invasive Species"]["Influences"] = ['* Forest composition', '**Logic Description:** Invasive species impact.']
forests_boreal_forests_scandinavian_and_finnish_stressors["Invasive Species"]["Logic Description"] = '---'
forests_boreal_forests_scandinavian_and_finnish_stressors["Invasive Species"]["Impact Function"] = "impact_invasive_species_forests_boreal_forests_scandinavian_and_finnish"

