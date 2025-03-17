from stressor_templates import *
import copy

forests_rainforest_mesoamerican_stressors = {
    "Infrastructure Development": copy.deepcopy(infrastructure_development_template),
    "Deforestation": copy.deepcopy(deforestation_template),
    "Temperature Increase": copy.deepcopy(climate_change_template),
    "Changes in Precipitation": copy.deepcopy(climate_change_template),
    "Wildfires": copy.deepcopy(fire_regime_template),
}

# --- Infrastructure Development ---
forests_rainforest_mesoamerican_stressors["Infrastructure Development"]["Metric"] = 'Length of new roads (km/year); area affected by other projects (dams, etc.) (ha/year).'
forests_rainforest_mesoamerican_stressors["Infrastructure Development"]["Data Sources"] = ['Government and industry reports.', 'Remote sensing data.', 'NGO reports.', '**Impact on Area:** Direct loss and fragmentation.', '**Impact on Biodiversity:**', 'Habitat loss and fragmentation.', 'Increased access for hunting/poaching.', 'Disruption of ecological corridors.', '**Influenced By (Stressors):**', 'Economic Growth: Tourism, agriculture, resource extraction.', 'Population Growth.', 'Government Policies.', 'Global Commodity Prices.', '**Influences (Stressors):**', 'Deforestation.', 'Wildfires.', 'Pollution.', '**Logic Description:** Infrastructure development, driven by various economic activities, leads to habitat loss and facilitates other stressors.']
forests_rainforest_mesoamerican_stressors["Infrastructure Development"]["Impact on Area"] = 'Direct loss and fragmentation.'
forests_rainforest_mesoamerican_stressors["Infrastructure Development"]["Impact on Biodiversity"] = 'Habitat loss and fragmentation.\nIncreased access for hunting/poaching.\nDisruption of ecological corridors.\n**Influenced By (Stressors):**\nEconomic Growth: Tourism, agriculture, resource extraction.\nPopulation Growth.\nGovernment Policies.\nGlobal Commodity Prices.\n**Influences (Stressors):**\nDeforestation.\nWildfires.\nPollution.\n**Logic Description:** Infrastructure development, driven by various economic activities, leads to habitat loss and facilitates other stressors.'
forests_rainforest_mesoamerican_stressors["Infrastructure Development"]["Influenced By"] = ['Economic Growth: Tourism, agriculture, resource extraction.', 'Population Growth.', 'Government Policies.', 'Global Commodity Prices.', '**Influences (Stressors):**', 'Deforestation.', 'Wildfires.', 'Pollution.', '**Logic Description:** Infrastructure development, driven by various economic activities, leads to habitat loss and facilitates other stressors.']
forests_rainforest_mesoamerican_stressors["Infrastructure Development"]["Influences"] = ['Deforestation.', 'Wildfires.', 'Pollution.', '**Logic Description:** Infrastructure development, driven by various economic activities, leads to habitat loss and facilitates other stressors.']
forests_rainforest_mesoamerican_stressors["Infrastructure Development"]["Logic Description"] = '---'
forests_rainforest_mesoamerican_stressors["Infrastructure Development"]["Impact Function"] = "impact_infrastructure_development_forests_rainforest_mesoamerican"

# --- Deforestation ---
forests_rainforest_mesoamerican_stressors["Deforestation"]["Metric"] = 'Area of forest cleared per year (ha/year).'
forests_rainforest_mesoamerican_stressors["Deforestation"]["Data Sources"] = ['Remote sensing data.', 'NGO and research reports.', 'Government data.', '**Impact on Area:** Direct reduction.', '**Impact on Biodiversity:**', 'Habitat loss and fragmentation.', 'Loss of carbon storage.', '**Influenced By (Stressors):**', 'Infrastructure Development.', 'Economic Growth: Agriculture (cattle ranching, coffee, palm oil), logging.', 'Population Growth: Subsistence agriculture.', 'Government Policies.', '* Global Commodity Prices', '**Influences (Stressors):**', 'Wildfires.', '* Changes in Precipitation', '**Logic Description:** Deforestation, driven by agricultural expansion (including cattle ranching and, increasingly, palm oil), logging, and subsistence farming, is a major threat.']
forests_rainforest_mesoamerican_stressors["Deforestation"]["Impact on Area"] = 'Direct reduction.'
forests_rainforest_mesoamerican_stressors["Deforestation"]["Impact on Biodiversity"] = 'Habitat loss and fragmentation.\nLoss of carbon storage.\n**Influenced By (Stressors):**\nInfrastructure Development.\nEconomic Growth: Agriculture (cattle ranching, coffee, palm oil), logging.\nPopulation Growth: Subsistence agriculture.\nGovernment Policies.\n* Global Commodity Prices\n**Influences (Stressors):**\nWildfires.\n* Changes in Precipitation\n**Logic Description:** Deforestation, driven by agricultural expansion (including cattle ranching and, increasingly, palm oil), logging, and subsistence farming, is a major threat.'
forests_rainforest_mesoamerican_stressors["Deforestation"]["Influenced By"] = ['Infrastructure Development.', 'Economic Growth: Agriculture (cattle ranching, coffee, palm oil), logging.', 'Population Growth: Subsistence agriculture.', 'Government Policies.', '* Global Commodity Prices', '**Influences (Stressors):**', 'Wildfires.', '* Changes in Precipitation', '**Logic Description:** Deforestation, driven by agricultural expansion (including cattle ranching and, increasingly, palm oil), logging, and subsistence farming, is a major threat.']
forests_rainforest_mesoamerican_stressors["Deforestation"]["Influences"] = ['Wildfires.', '* Changes in Precipitation', '**Logic Description:** Deforestation, driven by agricultural expansion (including cattle ranching and, increasingly, palm oil), logging, and subsistence farming, is a major threat.']
forests_rainforest_mesoamerican_stressors["Deforestation"]["Logic Description"] = '---'
forests_rainforest_mesoamerican_stressors["Deforestation"]["Impact Function"] = "impact_deforestation_forests_rainforest_mesoamerican"

# --- Temperature Increase ---
forests_rainforest_mesoamerican_stressors["Temperature Increase"]["Metric"] = 'Average annual temperature increase (°C).'
forests_rainforest_mesoamerican_stressors["Temperature Increase"]["Data Sources"] = ['Global and regional climate models.', 'Historical data.', '**Impact on Area:** Indirect.', '**Impact on Biodiversity:**', 'Species shifts.', 'Physiological stress.', '* Increased risk of coral bleaching in coastal areas.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', 'Deforestation.', '**Influences (Stressors):**', 'Wildfires.', 'Changes in Precipitation.', '**Logic Description:** Global warming impacts, with potential impacts on both terrestrial and coastal ecosystems (e.g., coral reefs).']
forests_rainforest_mesoamerican_stressors["Temperature Increase"]["Impact on Area"] = 'Indirect.'
forests_rainforest_mesoamerican_stressors["Temperature Increase"]["Impact on Biodiversity"] = 'Species shifts.\nPhysiological stress.\n* Increased risk of coral bleaching in coastal areas.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\nDeforestation.\n**Influences (Stressors):**\nWildfires.\nChanges in Precipitation.\n**Logic Description:** Global warming impacts, with potential impacts on both terrestrial and coastal ecosystems (e.g., coral reefs).'
forests_rainforest_mesoamerican_stressors["Temperature Increase"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', 'Deforestation.', '**Influences (Stressors):**', 'Wildfires.', 'Changes in Precipitation.', '**Logic Description:** Global warming impacts, with potential impacts on both terrestrial and coastal ecosystems (e.g., coral reefs).']
forests_rainforest_mesoamerican_stressors["Temperature Increase"]["Influences"] = ['Wildfires.', 'Changes in Precipitation.', '**Logic Description:** Global warming impacts, with potential impacts on both terrestrial and coastal ecosystems (e.g., coral reefs).']
forests_rainforest_mesoamerican_stressors["Temperature Increase"]["Logic Description"] = '---'
forests_rainforest_mesoamerican_stressors["Temperature Increase"]["Impact Function"] = "impact_temperature_increase_forests_rainforest_mesoamerican"

# --- Changes in Precipitation ---
forests_rainforest_mesoamerican_stressors["Changes in Precipitation"]["Metric"] = 'Change in annual precipitation (mm/year); dry season changes.'
forests_rainforest_mesoamerican_stressors["Changes in Precipitation"]["Data Sources"] = ['Climate models.', 'Historical data.', '**Impact on Area:** Indirect.', '**Impact on Biodiversity:**', 'Species shifts.', 'Drought stress.', '* Altered hurricane patterns.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', 'Deforestation (potentially).', '**Influences (Stressors):**', 'Wildfires.', '**Logic Description:** Changes in rainfall patterns and potential changes in hurricane frequency/intensity, linked to climate change.']
forests_rainforest_mesoamerican_stressors["Changes in Precipitation"]["Impact on Area"] = 'Indirect.'
forests_rainforest_mesoamerican_stressors["Changes in Precipitation"]["Impact on Biodiversity"] = 'Species shifts.\nDrought stress.\n* Altered hurricane patterns.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\nDeforestation (potentially).\n**Influences (Stressors):**\nWildfires.\n**Logic Description:** Changes in rainfall patterns and potential changes in hurricane frequency/intensity, linked to climate change.'
forests_rainforest_mesoamerican_stressors["Changes in Precipitation"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', 'Deforestation (potentially).', '**Influences (Stressors):**', 'Wildfires.', '**Logic Description:** Changes in rainfall patterns and potential changes in hurricane frequency/intensity, linked to climate change.']
forests_rainforest_mesoamerican_stressors["Changes in Precipitation"]["Influences"] = ['Wildfires.', '**Logic Description:** Changes in rainfall patterns and potential changes in hurricane frequency/intensity, linked to climate change.']
forests_rainforest_mesoamerican_stressors["Changes in Precipitation"]["Logic Description"] = '---'
forests_rainforest_mesoamerican_stressors["Changes in Precipitation"]["Impact Function"] = "impact_changes_in_precipitation_forests_rainforest_mesoamerican"

# --- Wildfires ---
forests_rainforest_mesoamerican_stressors["Wildfires"]["Metric"] = 'Number of fires; area burned (ha/year).'
forests_rainforest_mesoamerican_stressors["Wildfires"]["Data Sources"] = ['Remote sensing data.', 'Local reports.', '**Impact on Area:** Direct loss.', '**Impact on Biodiversity:**', 'Mortality.', 'Habitat loss.', '**Influenced By (Stressors):**', 'Deforestation.', 'Temperature Increase.', 'Changes in Precipitation.', 'Human Activities (agricultural burning).', '**Influences (Stressors):**', 'Deforestation.', '**Logic Description:** Wildfires, often linked to land clearing and exacerbated by climate change.']
forests_rainforest_mesoamerican_stressors["Wildfires"]["Impact on Area"] = 'Direct loss.'
forests_rainforest_mesoamerican_stressors["Wildfires"]["Impact on Biodiversity"] = 'Mortality.\nHabitat loss.\n**Influenced By (Stressors):**\nDeforestation.\nTemperature Increase.\nChanges in Precipitation.\nHuman Activities (agricultural burning).\n**Influences (Stressors):**\nDeforestation.\n**Logic Description:** Wildfires, often linked to land clearing and exacerbated by climate change.'
forests_rainforest_mesoamerican_stressors["Wildfires"]["Influenced By"] = ['Deforestation.', 'Temperature Increase.', 'Changes in Precipitation.', 'Human Activities (agricultural burning).', '**Influences (Stressors):**', 'Deforestation.', '**Logic Description:** Wildfires, often linked to land clearing and exacerbated by climate change.']
forests_rainforest_mesoamerican_stressors["Wildfires"]["Influences"] = ['Deforestation.', '**Logic Description:** Wildfires, often linked to land clearing and exacerbated by climate change.']
forests_rainforest_mesoamerican_stressors["Wildfires"]["Logic Description"] = '---'
forests_rainforest_mesoamerican_stressors["Wildfires"]["Impact Function"] = "impact_wildfires_forests_rainforest_mesoamerican"

