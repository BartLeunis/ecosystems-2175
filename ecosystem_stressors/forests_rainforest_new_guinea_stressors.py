from stressor_templates import *
import copy

forests_rainforest_new_guinea_stressors = {
    "Infrastructure Development": copy.deepcopy(infrastructure_development_template),
    "Deforestation": copy.deepcopy(deforestation_template),
    "Temperature Increase": copy.deepcopy(climate_change_template),
    "Changes in Precipitation": copy.deepcopy(climate_change_template),
    "Wildfires": copy.deepcopy(fire_regime_template),
    "Mining": {},
}

# --- Infrastructure Development ---
forests_rainforest_new_guinea_stressors["Infrastructure Development"]["Metric"] = 'Length of new roads (km/year); area affected by mining and other projects (ha/year).'
forests_rainforest_new_guinea_stressors["Infrastructure Development"]["Data Sources"] = ['Government and industry reports.', 'Remote sensing data.', 'NGO reports.', '**Impact on Area:** Direct loss and fragmentation.', '**Impact on Biodiversity:**', 'Habitat loss and fragmentation.', 'Increased access for hunting/poaching.', 'Disruption of ecological corridors.', '**Influenced By (Stressors):**', 'Economic Growth: Resource extraction (mining, logging).', 'Population Growth.', 'Government Policies.', 'Global Commodity Prices.', '**Influences (Stressors):**', 'Deforestation.', 'Wildfires.', 'Pollution (from mining).', '**Logic Description:** Similar to other rainforests, infrastructure development drives habitat loss and facilitates other stressors. Mining is a particularly significant threat in New Guinea.']
forests_rainforest_new_guinea_stressors["Infrastructure Development"]["Impact on Area"] = 'Direct loss and fragmentation.'
forests_rainforest_new_guinea_stressors["Infrastructure Development"]["Impact on Biodiversity"] = 'Habitat loss and fragmentation.\nIncreased access for hunting/poaching.\nDisruption of ecological corridors.\n**Influenced By (Stressors):**\nEconomic Growth: Resource extraction (mining, logging).\nPopulation Growth.\nGovernment Policies.\nGlobal Commodity Prices.\n**Influences (Stressors):**\nDeforestation.\nWildfires.\nPollution (from mining).\n**Logic Description:** Similar to other rainforests, infrastructure development drives habitat loss and facilitates other stressors. Mining is a particularly significant threat in New Guinea.'
forests_rainforest_new_guinea_stressors["Infrastructure Development"]["Influenced By"] = ['Economic Growth: Resource extraction (mining, logging).', 'Population Growth.', 'Government Policies.', 'Global Commodity Prices.', '**Influences (Stressors):**', 'Deforestation.', 'Wildfires.', 'Pollution (from mining).', '**Logic Description:** Similar to other rainforests, infrastructure development drives habitat loss and facilitates other stressors. Mining is a particularly significant threat in New Guinea.']
forests_rainforest_new_guinea_stressors["Infrastructure Development"]["Influences"] = ['Deforestation.', 'Wildfires.', 'Pollution (from mining).', '**Logic Description:** Similar to other rainforests, infrastructure development drives habitat loss and facilitates other stressors. Mining is a particularly significant threat in New Guinea.']
forests_rainforest_new_guinea_stressors["Infrastructure Development"]["Logic Description"] = '---'
forests_rainforest_new_guinea_stressors["Infrastructure Development"]["Impact Function"] = "impact_infrastructure_development_forests_rainforest_new_guinea"

# --- Deforestation ---
forests_rainforest_new_guinea_stressors["Deforestation"]["Metric"] = 'Area of forest cleared per year (ha/year).'
forests_rainforest_new_guinea_stressors["Deforestation"]["Data Sources"] = ['Remote sensing data.', 'NGO and research reports.', '**Impact on Area:** Direct reduction.', '**Impact on Biodiversity:**', 'Habitat loss and fragmentation.', 'Carbon emissions.', '**Influenced By (Stressors):**', 'Infrastructure Development.', 'Economic Growth: Palm oil, logging, mining.', 'Global Commodity Prices.', 'Population Growth.', 'Government Policies.', '**Influences (Stressors):**', 'Wildfires.', '**Logic Description:** Deforestation, driven largely by palm oil expansion, logging, and mining, is a major threat.']
forests_rainforest_new_guinea_stressors["Deforestation"]["Impact on Area"] = 'Direct reduction.'
forests_rainforest_new_guinea_stressors["Deforestation"]["Impact on Biodiversity"] = 'Habitat loss and fragmentation.\nCarbon emissions.\n**Influenced By (Stressors):**\nInfrastructure Development.\nEconomic Growth: Palm oil, logging, mining.\nGlobal Commodity Prices.\nPopulation Growth.\nGovernment Policies.\n**Influences (Stressors):**\nWildfires.\n**Logic Description:** Deforestation, driven largely by palm oil expansion, logging, and mining, is a major threat.'
forests_rainforest_new_guinea_stressors["Deforestation"]["Influenced By"] = ['Infrastructure Development.', 'Economic Growth: Palm oil, logging, mining.', 'Global Commodity Prices.', 'Population Growth.', 'Government Policies.', '**Influences (Stressors):**', 'Wildfires.', '**Logic Description:** Deforestation, driven largely by palm oil expansion, logging, and mining, is a major threat.']
forests_rainforest_new_guinea_stressors["Deforestation"]["Influences"] = ['Wildfires.', '**Logic Description:** Deforestation, driven largely by palm oil expansion, logging, and mining, is a major threat.']
forests_rainforest_new_guinea_stressors["Deforestation"]["Logic Description"] = '---'
forests_rainforest_new_guinea_stressors["Deforestation"]["Impact Function"] = "impact_deforestation_forests_rainforest_new_guinea"

# --- Temperature Increase ---
forests_rainforest_new_guinea_stressors["Temperature Increase"]["Metric"] = 'Average annual temperature increase (°C).'
forests_rainforest_new_guinea_stressors["Temperature Increase"]["Data Sources"] = ['Global and regional climate models.', 'Limited historical data.', '**Impact on Area:** Indirect.', '**Impact on Biodiversity:**', 'Species shifts.', 'Physiological stress.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', 'Deforestation.', '**Influences (Stressors):**', 'Wildfires.', 'Changes in Precipitation.', '**Logic Description:**  Global warming impacts, exacerbated by local deforestation.']
forests_rainforest_new_guinea_stressors["Temperature Increase"]["Impact on Area"] = 'Indirect.'
forests_rainforest_new_guinea_stressors["Temperature Increase"]["Impact on Biodiversity"] = 'Species shifts.\nPhysiological stress.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\nDeforestation.\n**Influences (Stressors):**\nWildfires.\nChanges in Precipitation.\n**Logic Description:**  Global warming impacts, exacerbated by local deforestation.'
forests_rainforest_new_guinea_stressors["Temperature Increase"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', 'Deforestation.', '**Influences (Stressors):**', 'Wildfires.', 'Changes in Precipitation.', '**Logic Description:**  Global warming impacts, exacerbated by local deforestation.']
forests_rainforest_new_guinea_stressors["Temperature Increase"]["Influences"] = ['Wildfires.', 'Changes in Precipitation.', '**Logic Description:**  Global warming impacts, exacerbated by local deforestation.']
forests_rainforest_new_guinea_stressors["Temperature Increase"]["Logic Description"] = '---'
forests_rainforest_new_guinea_stressors["Temperature Increase"]["Impact Function"] = "impact_temperature_increase_forests_rainforest_new_guinea"

# --- Changes in Precipitation ---
forests_rainforest_new_guinea_stressors["Changes in Precipitation"]["Metric"] = 'Change in annual precipitation (mm/year); dry season changes.'
forests_rainforest_new_guinea_stressors["Changes in Precipitation"]["Data Sources"] = ['Climate models.', 'Limited historical data.', '**Impact on Area:** Indirect.', '**Impact on Biodiversity:**', 'Species shifts.', 'Drought stress.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', 'Deforestation (potentially).', '**Influences (Stressors):**', 'Wildfires.', '**Logic Description:** Changes in rainfall patterns, linked to climate change.']
forests_rainforest_new_guinea_stressors["Changes in Precipitation"]["Impact on Area"] = 'Indirect.'
forests_rainforest_new_guinea_stressors["Changes in Precipitation"]["Impact on Biodiversity"] = 'Species shifts.\nDrought stress.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\nDeforestation (potentially).\n**Influences (Stressors):**\nWildfires.\n**Logic Description:** Changes in rainfall patterns, linked to climate change.'
forests_rainforest_new_guinea_stressors["Changes in Precipitation"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', 'Deforestation (potentially).', '**Influences (Stressors):**', 'Wildfires.', '**Logic Description:** Changes in rainfall patterns, linked to climate change.']
forests_rainforest_new_guinea_stressors["Changes in Precipitation"]["Influences"] = ['Wildfires.', '**Logic Description:** Changes in rainfall patterns, linked to climate change.']
forests_rainforest_new_guinea_stressors["Changes in Precipitation"]["Logic Description"] = '---'
forests_rainforest_new_guinea_stressors["Changes in Precipitation"]["Impact Function"] = "impact_changes_in_precipitation_forests_rainforest_new_guinea"

# --- Wildfires ---
forests_rainforest_new_guinea_stressors["Wildfires"]["Metric"] = 'Number of fires; area burned (ha/year).'
forests_rainforest_new_guinea_stressors["Wildfires"]["Data Sources"] = ['Remote sensing.', 'Local reports.', '**Impact on Area:** Direct loss.', '**Impact on Biodiversity:**', 'Mortality.', 'Habitat loss.', '**Influenced By (Stressors):**', 'Deforestation.', 'Temperature Increase.', 'Changes in Precipitation.', 'Human Activities (land clearing).', '**Influences (Stressors):**', 'Deforestation.', '**Logic Description:**  Fires, often linked to land clearing and exacerbated by climate change.']
forests_rainforest_new_guinea_stressors["Wildfires"]["Impact on Area"] = 'Direct loss.'
forests_rainforest_new_guinea_stressors["Wildfires"]["Impact on Biodiversity"] = 'Mortality.\nHabitat loss.\n**Influenced By (Stressors):**\nDeforestation.\nTemperature Increase.\nChanges in Precipitation.\nHuman Activities (land clearing).\n**Influences (Stressors):**\nDeforestation.\n**Logic Description:**  Fires, often linked to land clearing and exacerbated by climate change.'
forests_rainforest_new_guinea_stressors["Wildfires"]["Influenced By"] = ['Deforestation.', 'Temperature Increase.', 'Changes in Precipitation.', 'Human Activities (land clearing).', '**Influences (Stressors):**', 'Deforestation.', '**Logic Description:**  Fires, often linked to land clearing and exacerbated by climate change.']
forests_rainforest_new_guinea_stressors["Wildfires"]["Influences"] = ['Deforestation.', '**Logic Description:**  Fires, often linked to land clearing and exacerbated by climate change.']
forests_rainforest_new_guinea_stressors["Wildfires"]["Logic Description"] = '---'
forests_rainforest_new_guinea_stressors["Wildfires"]["Impact Function"] = "impact_wildfires_forests_rainforest_new_guinea"

# --- Mining ---
forests_rainforest_new_guinea_stressors["Mining"]["Metric"] = 'Area affected by mining; pollution levels.'
forests_rainforest_new_guinea_stressors["Mining"]["Data Sources"] = ['* Government and company records.', '* Remote Sensing', '* Research', '**Impact on Area:** Direct habitat loss; pollution.', '**Impact on Biodiversity:**', '* Habitat loss.', '* Toxic effects.', '**Influenced By (Stressors):**', '* Global demand for minerals', '**Influences (Stressors):**', '* Pollution', '* Habitat loss', '**Logic Description**: Mining operations cause pollution and habitat destruction.']
forests_rainforest_new_guinea_stressors["Mining"]["Impact on Area"] = 'Direct habitat loss; pollution.'
forests_rainforest_new_guinea_stressors["Mining"]["Impact on Biodiversity"] = '* Habitat loss.\n* Toxic effects.\n**Influenced By (Stressors):**\n* Global demand for minerals\n**Influences (Stressors):**\n* Pollution\n* Habitat loss\n**Logic Description**: Mining operations cause pollution and habitat destruction.'
forests_rainforest_new_guinea_stressors["Mining"]["Influenced By"] = ['* Global demand for minerals', '**Influences (Stressors):**', '* Pollution', '* Habitat loss', '**Logic Description**: Mining operations cause pollution and habitat destruction.']
forests_rainforest_new_guinea_stressors["Mining"]["Influences"] = ['* Pollution', '* Habitat loss', '**Logic Description**: Mining operations cause pollution and habitat destruction.']
forests_rainforest_new_guinea_stressors["Mining"]["Impact Function"] = "impact_mining_forests_rainforest_new_guinea"

