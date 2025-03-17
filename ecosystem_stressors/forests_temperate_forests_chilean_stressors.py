from stressor_templates import *
import copy

forests_temperate_forests_chilean_stressors = {
    "Infrastructure Development": copy.deepcopy(infrastructure_development_template),
    "Deforestation": copy.deepcopy(deforestation_template),
    "Temperature Increase": copy.deepcopy(climate_change_template),
    "Changes in Precipitation": copy.deepcopy(climate_change_template),
    "Wildfires": copy.deepcopy(fire_regime_template),
    "Invasive Species": copy.deepcopy(invasive_species_template),
}

# --- Infrastructure Development ---
forests_temperate_forests_chilean_stressors["Infrastructure Development"]["Metric"] = 'Road density (km/km²); area affected by development (hydroelectric, etc.) (ha/year).'
forests_temperate_forests_chilean_stressors["Infrastructure Development"]["Data Sources"] = ['Government statistics.', 'Remote sensing.', '**Impact on Area:** Habitat fragmentation.', '**Impact on Biodiversity:**', 'Habitat loss and fragmentation.', 'Disruption of corridors.', 'Impacts on aquatic systems (from dams).', '**Influenced By (Stressors):**', 'Economic Growth: Resource extraction (timber, hydropower).', 'Government Policies.', '**Influences (Stressors):**', 'Deforestation.', '* Water quality (Dams)', '**Logic Description:** Infrastructure development, including roads and hydroelectric projects, fragments habitat.']
forests_temperate_forests_chilean_stressors["Infrastructure Development"]["Impact on Area"] = 'Habitat fragmentation.'
forests_temperate_forests_chilean_stressors["Infrastructure Development"]["Impact on Biodiversity"] = 'Habitat loss and fragmentation.\nDisruption of corridors.\nImpacts on aquatic systems (from dams).\n**Influenced By (Stressors):**\nEconomic Growth: Resource extraction (timber, hydropower).\nGovernment Policies.\n**Influences (Stressors):**\nDeforestation.\n* Water quality (Dams)\n**Logic Description:** Infrastructure development, including roads and hydroelectric projects, fragments habitat.'
forests_temperate_forests_chilean_stressors["Infrastructure Development"]["Influenced By"] = ['Economic Growth: Resource extraction (timber, hydropower).', 'Government Policies.', '**Influences (Stressors):**', 'Deforestation.', '* Water quality (Dams)', '**Logic Description:** Infrastructure development, including roads and hydroelectric projects, fragments habitat.']
forests_temperate_forests_chilean_stressors["Infrastructure Development"]["Influences"] = ['Deforestation.', '* Water quality (Dams)', '**Logic Description:** Infrastructure development, including roads and hydroelectric projects, fragments habitat.']
forests_temperate_forests_chilean_stressors["Infrastructure Development"]["Logic Description"] = '---'

# --- Deforestation ---
forests_temperate_forests_chilean_stressors["Deforestation"]["Metric"] = 'Area of forest cleared per year (ha/year) (often conversion to plantations).'
forests_temperate_forests_chilean_stressors["Deforestation"]["Data Sources"] = ['Government statistics.', 'Remote sensing.', '**Impact on Area:** Loss of native forest; changes in forest type.', '**Impact on Biodiversity:**', 'Habitat loss (especially for old-growth dependent species).', 'Changes in species composition.', '**Influenced By (Stressors):**', 'Infrastructure Development.', 'Economic Growth: Demand for timber and pulp.', 'Government Policies: Forestry regulations.', '**Influences (Stressors):**', '* Carbon Storage', '**Logic Description:** Conversion of native forest to plantations (e.g., eucalyptus, pine) is a major driver of deforestation.']
forests_temperate_forests_chilean_stressors["Deforestation"]["Impact on Area"] = 'Loss of native forest; changes in forest type.'
forests_temperate_forests_chilean_stressors["Deforestation"]["Impact on Biodiversity"] = 'Habitat loss (especially for old-growth dependent species).\nChanges in species composition.\n**Influenced By (Stressors):**\nInfrastructure Development.\nEconomic Growth: Demand for timber and pulp.\nGovernment Policies: Forestry regulations.\n**Influences (Stressors):**\n* Carbon Storage\n**Logic Description:** Conversion of native forest to plantations (e.g., eucalyptus, pine) is a major driver of deforestation.'
forests_temperate_forests_chilean_stressors["Deforestation"]["Influenced By"] = ['Infrastructure Development.', 'Economic Growth: Demand for timber and pulp.', 'Government Policies: Forestry regulations.', '**Influences (Stressors):**', '* Carbon Storage', '**Logic Description:** Conversion of native forest to plantations (e.g., eucalyptus, pine) is a major driver of deforestation.']
forests_temperate_forests_chilean_stressors["Deforestation"]["Influences"] = ['* Carbon Storage', '**Logic Description:** Conversion of native forest to plantations (e.g., eucalyptus, pine) is a major driver of deforestation.']
forests_temperate_forests_chilean_stressors["Deforestation"]["Logic Description"] = '---'

# --- Temperature Increase ---
forests_temperate_forests_chilean_stressors["Temperature Increase"]["Metric"] = 'Average annual temperature increase (°C).'
forests_temperate_forests_chilean_stressors["Temperature Increase"]["Data Sources"] = ['Climate models.', 'Historical records.', '**Impact on Area:** Indirect.', '**Impact on Biodiversity:**', 'Species shifts (upslope).', 'Increased stress.', 'Changes in phenology.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Wildfires.', 'Changes in Precipitation.', '**Logic Description:** Climate change impacts.']
forests_temperate_forests_chilean_stressors["Temperature Increase"]["Impact on Area"] = 'Indirect.'
forests_temperate_forests_chilean_stressors["Temperature Increase"]["Impact on Biodiversity"] = 'Species shifts (upslope).\nIncreased stress.\nChanges in phenology.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\n**Influences (Stressors):**\nWildfires.\nChanges in Precipitation.\n**Logic Description:** Climate change impacts.'
forests_temperate_forests_chilean_stressors["Temperature Increase"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Wildfires.', 'Changes in Precipitation.', '**Logic Description:** Climate change impacts.']
forests_temperate_forests_chilean_stressors["Temperature Increase"]["Influences"] = ['Wildfires.', 'Changes in Precipitation.', '**Logic Description:** Climate change impacts.']
forests_temperate_forests_chilean_stressors["Temperature Increase"]["Logic Description"] = '---'

# --- Changes in Precipitation ---
forests_temperate_forests_chilean_stressors["Changes in Precipitation"]["Metric"] = 'Change in annual precipitation (mm/year); changes in seasonality.'
forests_temperate_forests_chilean_stressors["Changes in Precipitation"]["Data Sources"] = ['Climate models.', 'Historical records.', '**Impact on Area:** Indirect; changes in water availability.', '**Impact on Biodiversity:**', 'Changes in species composition.', 'Altered streamflow.', 'Increased drought stress (in some areas).', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', '* Wildfires (in some areas)', '* Water resources', '**Logic Description:** Changes in precipitation patterns, including potential for increased drought in some areas, impact ecosystems.']
forests_temperate_forests_chilean_stressors["Changes in Precipitation"]["Impact on Area"] = 'Indirect; changes in water availability.'
forests_temperate_forests_chilean_stressors["Changes in Precipitation"]["Impact on Biodiversity"] = 'Changes in species composition.\nAltered streamflow.\nIncreased drought stress (in some areas).\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\n**Influences (Stressors):**\n* Wildfires (in some areas)\n* Water resources\n**Logic Description:** Changes in precipitation patterns, including potential for increased drought in some areas, impact ecosystems.'
forests_temperate_forests_chilean_stressors["Changes in Precipitation"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', '* Wildfires (in some areas)', '* Water resources', '**Logic Description:** Changes in precipitation patterns, including potential for increased drought in some areas, impact ecosystems.']
forests_temperate_forests_chilean_stressors["Changes in Precipitation"]["Influences"] = ['* Wildfires (in some areas)', '* Water resources', '**Logic Description:** Changes in precipitation patterns, including potential for increased drought in some areas, impact ecosystems.']
forests_temperate_forests_chilean_stressors["Changes in Precipitation"]["Logic Description"] = '---'

# --- Wildfires ---
forests_temperate_forests_chilean_stressors["Wildfires"]["Metric"] = 'Number of fires; area burned (ha/year).'
forests_temperate_forests_chilean_stressors["Wildfires"]["Data Sources"] = ['Government statistics.', 'Remote sensing.', '**Impact on Area:** Direct loss of forest area; changes in forest structure.', '**Impact on Biodiversity:**', 'Mortality.', 'Habitat loss.', 'Changes in species composition.', '**Influenced By (Stressors):**', 'Temperature Increase.', 'Changes in Precipitation (drier conditions).', 'Land Use Practices (plantations).', 'Human Activities (negligence, arson).', '**Influences (Stressors):**', '* Future fire risk', '**Logic Description:** Wildfires, becoming more frequent and intense due to climate change and land use, are a growing threat.']
forests_temperate_forests_chilean_stressors["Wildfires"]["Impact on Area"] = 'Direct loss of forest area; changes in forest structure.'
forests_temperate_forests_chilean_stressors["Wildfires"]["Impact on Biodiversity"] = 'Mortality.\nHabitat loss.\nChanges in species composition.\n**Influenced By (Stressors):**\nTemperature Increase.\nChanges in Precipitation (drier conditions).\nLand Use Practices (plantations).\nHuman Activities (negligence, arson).\n**Influences (Stressors):**\n* Future fire risk\n**Logic Description:** Wildfires, becoming more frequent and intense due to climate change and land use, are a growing threat.'
forests_temperate_forests_chilean_stressors["Wildfires"]["Influenced By"] = ['Temperature Increase.', 'Changes in Precipitation (drier conditions).', 'Land Use Practices (plantations).', 'Human Activities (negligence, arson).', '**Influences (Stressors):**', '* Future fire risk', '**Logic Description:** Wildfires, becoming more frequent and intense due to climate change and land use, are a growing threat.']
forests_temperate_forests_chilean_stressors["Wildfires"]["Influences"] = ['* Future fire risk', '**Logic Description:** Wildfires, becoming more frequent and intense due to climate change and land use, are a growing threat.']
forests_temperate_forests_chilean_stressors["Wildfires"]["Logic Description"] = '---'

# --- Invasive Species ---
forests_temperate_forests_chilean_stressors["Invasive Species"]["Metric"] = 'Abundance and distribution of key invasives.'
forests_temperate_forests_chilean_stressors["Invasive Species"]["Data Sources"] = ['Forest health monitoring.', 'Research studies.', '**Impact on Area:** Changes in forest composition and structure.', '**Impact on Biodiversity:**', '* Competition.', '* Altered processes.', '**Influenced By (Stressors):**', '* Disturbance.', '* Climate change', '* Global Trade', '**Influences (Stressors):**', '* Forest Composition', '**Logic Description**: Invasive species impacts.']
forests_temperate_forests_chilean_stressors["Invasive Species"]["Impact on Area"] = 'Changes in forest composition and structure.'
forests_temperate_forests_chilean_stressors["Invasive Species"]["Impact on Biodiversity"] = '* Competition.\n* Altered processes.\n**Influenced By (Stressors):**\n* Disturbance.\n* Climate change\n* Global Trade\n**Influences (Stressors):**\n* Forest Composition\n**Logic Description**: Invasive species impacts.'
forests_temperate_forests_chilean_stressors["Invasive Species"]["Influenced By"] = ['* Disturbance.', '* Climate change', '* Global Trade', '**Influences (Stressors):**', '* Forest Composition', '**Logic Description**: Invasive species impacts.']
forests_temperate_forests_chilean_stressors["Invasive Species"]["Influences"] = ['* Forest Composition', '**Logic Description**: Invasive species impacts.']

