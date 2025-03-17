from stressor_templates import *
import copy

forests_rainforest_atlantic_forest_stressors = {
    "Infrastructure Development": copy.deepcopy(infrastructure_development_template),
    "Deforestation": copy.deepcopy(deforestation_template),
    "Temperature Increase": copy.deepcopy(climate_change_template),
    "Changes in Precipitation": copy.deepcopy(climate_change_template),
    "Wildfires": copy.deepcopy(fire_regime_template),
}

# --- Infrastructure Development ---
forests_rainforest_atlantic_forest_stressors["Infrastructure Development"]["Metric"] = 'Road length (km/year); area affected by other projects (ha/year).'
forests_rainforest_atlantic_forest_stressors["Infrastructure Development"]["Data Sources"] = ['Government and industry reports.', 'Remote sensing data.', 'NGO reports.', '**Impact on Area:** Direct loss and fragmentation (already highly fragmented).', '**Impact on Biodiversity:**', 'Habitat loss and fragmentation.', 'Increased access for hunting/poaching.', '* Edge effects', '**Influenced By (Stressors):**', 'Economic Growth.', 'Population Growth (high population density in the region).', 'Government Policies.', '**Influences (Stressors):**', 'Deforestation.', 'Wildfires.', '**Logic Description:** Further fragmentation of an already highly fragmented ecosystem, increasing edge effects and isolating populations.']
forests_rainforest_atlantic_forest_stressors["Infrastructure Development"]["Impact on Area"] = 'Direct loss and fragmentation (already highly fragmented).'
forests_rainforest_atlantic_forest_stressors["Infrastructure Development"]["Impact on Biodiversity"] = 'Habitat loss and fragmentation.\nIncreased access for hunting/poaching.\n* Edge effects\n**Influenced By (Stressors):**\nEconomic Growth.\nPopulation Growth (high population density in the region).\nGovernment Policies.\n**Influences (Stressors):**\nDeforestation.\nWildfires.\n**Logic Description:** Further fragmentation of an already highly fragmented ecosystem, increasing edge effects and isolating populations.'
forests_rainforest_atlantic_forest_stressors["Infrastructure Development"]["Influenced By"] = ['Economic Growth.', 'Population Growth (high population density in the region).', 'Government Policies.', '**Influences (Stressors):**', 'Deforestation.', 'Wildfires.', '**Logic Description:** Further fragmentation of an already highly fragmented ecosystem, increasing edge effects and isolating populations.']
forests_rainforest_atlantic_forest_stressors["Infrastructure Development"]["Influences"] = ['Deforestation.', 'Wildfires.', '**Logic Description:** Further fragmentation of an already highly fragmented ecosystem, increasing edge effects and isolating populations.']
forests_rainforest_atlantic_forest_stressors["Infrastructure Development"]["Logic Description"] = '---'
forests_rainforest_atlantic_forest_stressors["Infrastructure Development"]["Impact Function"] = "impact_infrastructure_development_forests_rainforest_atlantic_forest"

# --- Deforestation ---
forests_rainforest_atlantic_forest_stressors["Deforestation"]["Metric"] = 'Area of forest cleared per year (ha/year).'
forests_rainforest_atlantic_forest_stressors["Deforestation"]["Data Sources"] = ['Remote sensing data.', 'NGO and research reports.', '**Impact on Area:** Direct reduction (already severely reduced).', '**Impact on Biodiversity:**', 'Habitat loss.', 'Increased extinction risk.', '**Influenced By (Stressors):**', 'Infrastructure Development.', 'Economic Growth: Agriculture (sugarcane, coffee, cattle).', 'Urban Expansion.', '* Government Policies', '**Influences (Stressors):**', 'Wildfires.', '**Logic Description:** Continued deforestation, driven by agriculture and urban expansion, further reduces the remaining fragments of this highly threatened ecosystem.']
forests_rainforest_atlantic_forest_stressors["Deforestation"]["Impact on Area"] = 'Direct reduction (already severely reduced).'
forests_rainforest_atlantic_forest_stressors["Deforestation"]["Impact on Biodiversity"] = 'Habitat loss.\nIncreased extinction risk.\n**Influenced By (Stressors):**\nInfrastructure Development.\nEconomic Growth: Agriculture (sugarcane, coffee, cattle).\nUrban Expansion.\n* Government Policies\n**Influences (Stressors):**\nWildfires.\n**Logic Description:** Continued deforestation, driven by agriculture and urban expansion, further reduces the remaining fragments of this highly threatened ecosystem.'
forests_rainforest_atlantic_forest_stressors["Deforestation"]["Influenced By"] = ['Infrastructure Development.', 'Economic Growth: Agriculture (sugarcane, coffee, cattle).', 'Urban Expansion.', '* Government Policies', '**Influences (Stressors):**', 'Wildfires.', '**Logic Description:** Continued deforestation, driven by agriculture and urban expansion, further reduces the remaining fragments of this highly threatened ecosystem.']
forests_rainforest_atlantic_forest_stressors["Deforestation"]["Influences"] = ['Wildfires.', '**Logic Description:** Continued deforestation, driven by agriculture and urban expansion, further reduces the remaining fragments of this highly threatened ecosystem.']
forests_rainforest_atlantic_forest_stressors["Deforestation"]["Logic Description"] = '---'
forests_rainforest_atlantic_forest_stressors["Deforestation"]["Impact Function"] = "impact_deforestation_forests_rainforest_atlantic_forest"

# --- Temperature Increase ---
forests_rainforest_atlantic_forest_stressors["Temperature Increase"]["Metric"] = 'Average annual temperature increase (°C).'
forests_rainforest_atlantic_forest_stressors["Temperature Increase"]["Data Sources"] = ['Global and regional climate models.', 'Historical data.', '**Impact on Area:** Indirect.', '**Impact on Biodiversity:**', 'Species shifts.', 'Physiological stress.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', 'Deforestation.', '**Influences (Stressors):**', 'Wildfires.', 'Changes in Precipitation.', '**Logic Description:** Global warming impacts.']
forests_rainforest_atlantic_forest_stressors["Temperature Increase"]["Impact on Area"] = 'Indirect.'
forests_rainforest_atlantic_forest_stressors["Temperature Increase"]["Impact on Biodiversity"] = 'Species shifts.\nPhysiological stress.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\nDeforestation.\n**Influences (Stressors):**\nWildfires.\nChanges in Precipitation.\n**Logic Description:** Global warming impacts.'
forests_rainforest_atlantic_forest_stressors["Temperature Increase"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', 'Deforestation.', '**Influences (Stressors):**', 'Wildfires.', 'Changes in Precipitation.', '**Logic Description:** Global warming impacts.']
forests_rainforest_atlantic_forest_stressors["Temperature Increase"]["Influences"] = ['Wildfires.', 'Changes in Precipitation.', '**Logic Description:** Global warming impacts.']
forests_rainforest_atlantic_forest_stressors["Temperature Increase"]["Logic Description"] = '---'
forests_rainforest_atlantic_forest_stressors["Temperature Increase"]["Impact Function"] = "impact_temperature_increase_forests_rainforest_atlantic_forest"

# --- Changes in Precipitation ---
forests_rainforest_atlantic_forest_stressors["Changes in Precipitation"]["Metric"] = 'Change in annual precipitation (mm/year); dry season changes.'
forests_rainforest_atlantic_forest_stressors["Changes in Precipitation"]["Data Sources"] = ['Climate models.', 'Historical data.', '**Impact on Area:** Indirect.', '**Impact on Biodiversity:**', 'Species shifts.', 'Drought stress.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', 'Deforestation (potentially).', '**Influences (Stressors):**', 'Wildfires.', '**Logic Description:** Changes in rainfall patterns.']
forests_rainforest_atlantic_forest_stressors["Changes in Precipitation"]["Impact on Area"] = 'Indirect.'
forests_rainforest_atlantic_forest_stressors["Changes in Precipitation"]["Impact on Biodiversity"] = 'Species shifts.\nDrought stress.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\nDeforestation (potentially).\n**Influences (Stressors):**\nWildfires.\n**Logic Description:** Changes in rainfall patterns.'
forests_rainforest_atlantic_forest_stressors["Changes in Precipitation"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', 'Deforestation (potentially).', '**Influences (Stressors):**', 'Wildfires.', '**Logic Description:** Changes in rainfall patterns.']
forests_rainforest_atlantic_forest_stressors["Changes in Precipitation"]["Influences"] = ['Wildfires.', '**Logic Description:** Changes in rainfall patterns.']
forests_rainforest_atlantic_forest_stressors["Changes in Precipitation"]["Logic Description"] = '---'
forests_rainforest_atlantic_forest_stressors["Changes in Precipitation"]["Impact Function"] = "impact_changes_in_precipitation_forests_rainforest_atlantic_forest"

# --- Wildfires ---
forests_rainforest_atlantic_forest_stressors["Wildfires"]["Metric"] = 'Number of wildfires per year; total area burned (hectares/year).'
forests_rainforest_atlantic_forest_stressors["Wildfires"]["Data Sources"] = ['*  Remote sensing', '* Fire department and agency reports', '**Impact on Area:** Direct loss within fragmented patches.', '**Impact on Biodiversity:**', '* Mortality', '* Habitat loss', '* Exacerbation of fragmentation.', '**Influenced By (Stressors):**', '* Deforestation', '* Temp increase', '* Precipitation changes', '* Human activities', '**Influences (Stressors):**', '* Deforestation (further fragmentation).', '**Logic Description:** Wildfires, often linked to ag practices and climate, degrade fragmented forest.']
forests_rainforest_atlantic_forest_stressors["Wildfires"]["Impact on Area"] = 'Direct loss within fragmented patches.'
forests_rainforest_atlantic_forest_stressors["Wildfires"]["Impact on Biodiversity"] = '* Mortality\n* Habitat loss\n* Exacerbation of fragmentation.\n**Influenced By (Stressors):**\n* Deforestation\n* Temp increase\n* Precipitation changes\n* Human activities\n**Influences (Stressors):**\n* Deforestation (further fragmentation).\n**Logic Description:** Wildfires, often linked to ag practices and climate, degrade fragmented forest.'
forests_rainforest_atlantic_forest_stressors["Wildfires"]["Influenced By"] = ['* Deforestation', '* Temp increase', '* Precipitation changes', '* Human activities', '**Influences (Stressors):**', '* Deforestation (further fragmentation).', '**Logic Description:** Wildfires, often linked to ag practices and climate, degrade fragmented forest.']
forests_rainforest_atlantic_forest_stressors["Wildfires"]["Influences"] = ['* Deforestation (further fragmentation).', '**Logic Description:** Wildfires, often linked to ag practices and climate, degrade fragmented forest.']
forests_rainforest_atlantic_forest_stressors["Wildfires"]["Logic Description"] = '---'
forests_rainforest_atlantic_forest_stressors["Wildfires"]["Impact Function"] = "impact_wildfires_forests_rainforest_atlantic_forest"

