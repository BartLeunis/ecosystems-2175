from stressor_templates import *
import copy

forests_temperate_forests_east_asian_stressors = {
    "Infrastructure Development": copy.deepcopy(infrastructure_development_template),
    "Deforestation": copy.deepcopy(deforestation_template),
    "Temperature Increase": copy.deepcopy(climate_change_template),
    "Changes in Precipitation": copy.deepcopy(climate_change_template),
    "Air Pollution": copy.deepcopy(pollution_template),
    "Invasive Species": copy.deepcopy(invasive_species_template),
}

# --- Infrastructure Development ---
forests_temperate_forests_east_asian_stressors["Infrastructure Development"]["Metric"] = 'Road density (km/km²); area affected by development (ha/year).'
forests_temperate_forests_east_asian_stressors["Infrastructure Development"]["Data Sources"] = ['National government statistics.', 'Remote sensing.', '**Impact on Area:** Habitat fragmentation.', '**Impact on Biodiversity:**', 'Habitat loss and fragmentation.', 'Disruption of corridors.', '**Influenced By (Stressors):**', 'Economic Growth.', 'Population Growth (and high density in some areas).', 'Government Policies.', '**Influences (Stressors):**', 'Deforestation (localized).', '**Logic Description:** Rapid development continues to fragment habitat.']
forests_temperate_forests_east_asian_stressors["Infrastructure Development"]["Impact on Area"] = 'Habitat fragmentation.'
forests_temperate_forests_east_asian_stressors["Infrastructure Development"]["Impact on Biodiversity"] = 'Habitat loss and fragmentation.\nDisruption of corridors.\n**Influenced By (Stressors):**\nEconomic Growth.\nPopulation Growth (and high density in some areas).\nGovernment Policies.\n**Influences (Stressors):**\nDeforestation (localized).\n**Logic Description:** Rapid development continues to fragment habitat.'
forests_temperate_forests_east_asian_stressors["Infrastructure Development"]["Influenced By"] = ['Economic Growth.', 'Population Growth (and high density in some areas).', 'Government Policies.', '**Influences (Stressors):**', 'Deforestation (localized).', '**Logic Description:** Rapid development continues to fragment habitat.']
forests_temperate_forests_east_asian_stressors["Infrastructure Development"]["Influences"] = ['Deforestation (localized).', '**Logic Description:** Rapid development continues to fragment habitat.']
forests_temperate_forests_east_asian_stressors["Infrastructure Development"]["Logic Description"] = '---'
forests_temperate_forests_east_asian_stressors["Infrastructure Development"]["Impact Function"] = "impact_infrastructure_development_forests_temperate_forests_east_asian"

# --- Deforestation ---
forests_temperate_forests_east_asian_stressors["Deforestation"]["Metric"] = 'Area of forest cleared per year (ha/year) (localized; overall forest cover may be increasing in some areas due to afforestation, but loss of *natural* forest is a concern).'
forests_temperate_forests_east_asian_stressors["Deforestation"]["Data Sources"] = ['National forest inventories.', 'Remote sensing.', '**Impact on Area:** Localized forest loss; changes in forest age/type.', '**Impact on Biodiversity:**', 'Habitat loss.', 'Changes in species composition.', '**Influenced By (Stressors):**', 'Infrastructure Development.', 'Urban Sprawl.', 'Agricultural Expansion (in some areas).', 'Timber Harvesting.', '**Influences (Stressors):**', '* Forest Composition', '**Logic Description:** Localized deforestation and conversion of natural forest to plantations continue to be stressors.']
forests_temperate_forests_east_asian_stressors["Deforestation"]["Impact on Area"] = 'Localized forest loss; changes in forest age/type.'
forests_temperate_forests_east_asian_stressors["Deforestation"]["Impact on Biodiversity"] = 'Habitat loss.\nChanges in species composition.\n**Influenced By (Stressors):**\nInfrastructure Development.\nUrban Sprawl.\nAgricultural Expansion (in some areas).\nTimber Harvesting.\n**Influences (Stressors):**\n* Forest Composition\n**Logic Description:** Localized deforestation and conversion of natural forest to plantations continue to be stressors.'
forests_temperate_forests_east_asian_stressors["Deforestation"]["Influenced By"] = ['Infrastructure Development.', 'Urban Sprawl.', 'Agricultural Expansion (in some areas).', 'Timber Harvesting.', '**Influences (Stressors):**', '* Forest Composition', '**Logic Description:** Localized deforestation and conversion of natural forest to plantations continue to be stressors.']
forests_temperate_forests_east_asian_stressors["Deforestation"]["Influences"] = ['* Forest Composition', '**Logic Description:** Localized deforestation and conversion of natural forest to plantations continue to be stressors.']
forests_temperate_forests_east_asian_stressors["Deforestation"]["Logic Description"] = '---'
forests_temperate_forests_east_asian_stressors["Deforestation"]["Impact Function"] = "impact_deforestation_forests_temperate_forests_east_asian"

# --- Temperature Increase ---
forests_temperate_forests_east_asian_stressors["Temperature Increase"]["Metric"] = 'Average annual temperature increase (°C).'
forests_temperate_forests_east_asian_stressors["Temperature Increase"]["Data Sources"] = ['Climate models.', 'Historical records.', '**Impact on Area:** Indirect.', '**Impact on Biodiversity:**', 'Species shifts.', 'Increased stress.', 'Changes in phenology.', 'Pest/disease outbreaks.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Wildfires.', 'Changes in Precipitation.', '* Pest and disease outbreaks', '**Logic Description:** Climate change impacts.']
forests_temperate_forests_east_asian_stressors["Temperature Increase"]["Impact on Area"] = 'Indirect.'
forests_temperate_forests_east_asian_stressors["Temperature Increase"]["Impact on Biodiversity"] = 'Species shifts.\nIncreased stress.\nChanges in phenology.\nPest/disease outbreaks.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\n**Influences (Stressors):**\nWildfires.\nChanges in Precipitation.\n* Pest and disease outbreaks\n**Logic Description:** Climate change impacts.'
forests_temperate_forests_east_asian_stressors["Temperature Increase"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Wildfires.', 'Changes in Precipitation.', '* Pest and disease outbreaks', '**Logic Description:** Climate change impacts.']
forests_temperate_forests_east_asian_stressors["Temperature Increase"]["Influences"] = ['Wildfires.', 'Changes in Precipitation.', '* Pest and disease outbreaks', '**Logic Description:** Climate change impacts.']
forests_temperate_forests_east_asian_stressors["Temperature Increase"]["Logic Description"] = '---'
forests_temperate_forests_east_asian_stressors["Temperature Increase"]["Impact Function"] = "impact_temperature_increase_forests_temperate_forests_east_asian"

# --- Changes in Precipitation ---
forests_temperate_forests_east_asian_stressors["Changes in Precipitation"]["Metric"] = 'Change in annual precipitation (mm/year); changes in seasonality (e.g., changes in monsoon patterns).'
forests_temperate_forests_east_asian_stressors["Changes in Precipitation"]["Data Sources"] = ['Climate models.', 'Historical records.', '**Impact on Area:** Indirect.', '**Impact on Biodiversity:**', 'Changes in species composition.', 'Altered streamflow.', 'Increased drought stress (in some areas).', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', '* Wildfires (in some areas)', '* Water availability.', '**Logic Description:** Changes in precipitation patterns, including changes in monsoon intensity and distribution, impact water resources and ecosystems.']
forests_temperate_forests_east_asian_stressors["Changes in Precipitation"]["Impact on Area"] = 'Indirect.'
forests_temperate_forests_east_asian_stressors["Changes in Precipitation"]["Impact on Biodiversity"] = 'Changes in species composition.\nAltered streamflow.\nIncreased drought stress (in some areas).\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\n**Influences (Stressors):**\n* Wildfires (in some areas)\n* Water availability.\n**Logic Description:** Changes in precipitation patterns, including changes in monsoon intensity and distribution, impact water resources and ecosystems.'
forests_temperate_forests_east_asian_stressors["Changes in Precipitation"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', '* Wildfires (in some areas)', '* Water availability.', '**Logic Description:** Changes in precipitation patterns, including changes in monsoon intensity and distribution, impact water resources and ecosystems.']
forests_temperate_forests_east_asian_stressors["Changes in Precipitation"]["Influences"] = ['* Wildfires (in some areas)', '* Water availability.', '**Logic Description:** Changes in precipitation patterns, including changes in monsoon intensity and distribution, impact water resources and ecosystems.']
forests_temperate_forests_east_asian_stressors["Changes in Precipitation"]["Logic Description"] = '---'
forests_temperate_forests_east_asian_stressors["Changes in Precipitation"]["Impact Function"] = "impact_changes_in_precipitation_forests_temperate_forests_east_asian"

# --- Air Pollution ---
forests_temperate_forests_east_asian_stressors["Air Pollution"]["Metric"] = 'Concentrations of pollutants (e.g., ozone, particulate matter, nitrogen oxides).'
forests_temperate_forests_east_asian_stressors["Air Pollution"]["Data Sources"] = ['National air quality monitoring networks.', '**Impact on Area:** Reduced forest health and productivity.', '**Impact on Biodiversity:**', 'Damage to foliage.', 'Increased susceptibility to pests/diseases.', 'Acidification of soils and water.', '**Influenced By (Stressors):**', 'Industrial Activity.', 'Fossil Fuel Combustion.', 'Agricultural Practices.', '**Influences (Stressors):**', '* Water Quality', '* Forest Health', '**Logic Description:** Severe air pollution, particularly in parts of China, is a major stressor.']
forests_temperate_forests_east_asian_stressors["Air Pollution"]["Impact on Area"] = 'Reduced forest health and productivity.'
forests_temperate_forests_east_asian_stressors["Air Pollution"]["Impact on Biodiversity"] = 'Damage to foliage.\nIncreased susceptibility to pests/diseases.\nAcidification of soils and water.\n**Influenced By (Stressors):**\nIndustrial Activity.\nFossil Fuel Combustion.\nAgricultural Practices.\n**Influences (Stressors):**\n* Water Quality\n* Forest Health\n**Logic Description:** Severe air pollution, particularly in parts of China, is a major stressor.'
forests_temperate_forests_east_asian_stressors["Air Pollution"]["Influenced By"] = ['Industrial Activity.', 'Fossil Fuel Combustion.', 'Agricultural Practices.', '**Influences (Stressors):**', '* Water Quality', '* Forest Health', '**Logic Description:** Severe air pollution, particularly in parts of China, is a major stressor.']
forests_temperate_forests_east_asian_stressors["Air Pollution"]["Influences"] = ['* Water Quality', '* Forest Health', '**Logic Description:** Severe air pollution, particularly in parts of China, is a major stressor.']
forests_temperate_forests_east_asian_stressors["Air Pollution"]["Logic Description"] = '---'
forests_temperate_forests_east_asian_stressors["Air Pollution"]["Impact Function"] = "impact_air_pollution_forests_temperate_forests_east_asian"

# --- Invasive Species ---
forests_temperate_forests_east_asian_stressors["Invasive Species"]["Metric"] = 'Abundance and distribution of key invasives.'
forests_temperate_forests_east_asian_stressors["Invasive Species"]["Data Sources"] = ['* Forest health monitoring.', '* Research.', '**Impact on Area:** Changes in composition.', '**Impact on Biodiversity:**', '* Competition.', '* Altered processes.', '**Influenced By (Stressors):**', '* Disturbance.', '* Climate change.', '* Global trade.', '**Influences (Stressors):**', '* Forest Structure', '**Logic Description:** Invasive species impact.']
forests_temperate_forests_east_asian_stressors["Invasive Species"]["Impact on Area"] = 'Changes in composition.'
forests_temperate_forests_east_asian_stressors["Invasive Species"]["Impact on Biodiversity"] = '* Competition.\n* Altered processes.\n**Influenced By (Stressors):**\n* Disturbance.\n* Climate change.\n* Global trade.\n**Influences (Stressors):**\n* Forest Structure\n**Logic Description:** Invasive species impact.'
forests_temperate_forests_east_asian_stressors["Invasive Species"]["Influenced By"] = ['* Disturbance.', '* Climate change.', '* Global trade.', '**Influences (Stressors):**', '* Forest Structure', '**Logic Description:** Invasive species impact.']
forests_temperate_forests_east_asian_stressors["Invasive Species"]["Influences"] = ['* Forest Structure', '**Logic Description:** Invasive species impact.']
forests_temperate_forests_east_asian_stressors["Invasive Species"]["Logic Description"] = '---'
forests_temperate_forests_east_asian_stressors["Invasive Species"]["Impact Function"] = "impact_invasive_species_forests_temperate_forests_east_asian"

