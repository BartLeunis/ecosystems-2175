from stressor_templates import *
import copy

forests_rainforest_congo_stressors = {
    "Infrastructure Development": copy.deepcopy(infrastructure_development_template),
    "Deforestation": copy.deepcopy(deforestation_template),
    "Temperature Increase": copy.deepcopy(climate_change_template),
    "Changes in Precipitation": copy.deepcopy(climate_change_template),
    "Wildfires": copy.deepcopy(fire_regime_template),
}

# --- Infrastructure Development ---
forests_rainforest_congo_stressors["Infrastructure Development"]["Metric"] = 'Length of new roads constructed per year (km/year), and/or area directly affected by other infrastructure projects (dams, pipelines, mining operations) (ha/year).'
forests_rainforest_congo_stressors["Infrastructure Development"]["Data Sources"] = ['Governmental and industry reports on infrastructure projects.', 'Remote sensing data (satellite imagery).', 'Reports from environmental organizations and research institutions (e.g., World Resources Institute, Rainforest Foundation).', '**Impact on Area:** Direct loss of rainforest area; increased fragmentation.', '**Impact on Biodiversity:**', 'Habitat loss and fragmentation.', 'Disruption of ecological corridors.', 'Increased access for hunting and poaching.', 'Impacts on aquatic ecosystems from dams.', '**Influenced By (Stressors):**', 'Economic Growth: Demand for resources (timber, minerals).', 'Population Growth: Increased demand for land and resources.', 'Government Policies: Infrastructure development plans and regulations.', 'Global Commodity Prices: Prices for timber, minerals, and other resources.', '**Influences (Stressors):**', 'Deforestation: Roads facilitate logging and agricultural expansion.', 'Wildfires: Increased risk due to human activity.', 'Pollution: Mining and other industrial activities.', '**Logic Description:** Similar to the Amazon, infrastructure development (roads, dams, mines) directly reduces rainforest area and fragments habitat. This leads to biodiversity loss through habitat loss, disruption of ecological processes, and increased human access for hunting and poaching.']
forests_rainforest_congo_stressors["Infrastructure Development"]["Impact on Area"] = 'Direct loss of rainforest area; increased fragmentation.'
forests_rainforest_congo_stressors["Infrastructure Development"]["Impact on Biodiversity"] = 'Habitat loss and fragmentation.\nDisruption of ecological corridors.\nIncreased access for hunting and poaching.\nImpacts on aquatic ecosystems from dams.\n**Influenced By (Stressors):**\nEconomic Growth: Demand for resources (timber, minerals).\nPopulation Growth: Increased demand for land and resources.\nGovernment Policies: Infrastructure development plans and regulations.\nGlobal Commodity Prices: Prices for timber, minerals, and other resources.\n**Influences (Stressors):**\nDeforestation: Roads facilitate logging and agricultural expansion.\nWildfires: Increased risk due to human activity.\nPollution: Mining and other industrial activities.\n**Logic Description:** Similar to the Amazon, infrastructure development (roads, dams, mines) directly reduces rainforest area and fragments habitat. This leads to biodiversity loss through habitat loss, disruption of ecological processes, and increased human access for hunting and poaching.'
forests_rainforest_congo_stressors["Infrastructure Development"]["Influenced By"] = ['Economic Growth: Demand for resources (timber, minerals).', 'Population Growth: Increased demand for land and resources.', 'Government Policies: Infrastructure development plans and regulations.', 'Global Commodity Prices: Prices for timber, minerals, and other resources.', '**Influences (Stressors):**', 'Deforestation: Roads facilitate logging and agricultural expansion.', 'Wildfires: Increased risk due to human activity.', 'Pollution: Mining and other industrial activities.', '**Logic Description:** Similar to the Amazon, infrastructure development (roads, dams, mines) directly reduces rainforest area and fragments habitat. This leads to biodiversity loss through habitat loss, disruption of ecological processes, and increased human access for hunting and poaching.']
forests_rainforest_congo_stressors["Infrastructure Development"]["Influences"] = ['Deforestation: Roads facilitate logging and agricultural expansion.', 'Wildfires: Increased risk due to human activity.', 'Pollution: Mining and other industrial activities.', '**Logic Description:** Similar to the Amazon, infrastructure development (roads, dams, mines) directly reduces rainforest area and fragments habitat. This leads to biodiversity loss through habitat loss, disruption of ecological processes, and increased human access for hunting and poaching.']
forests_rainforest_congo_stressors["Infrastructure Development"]["Logic Description"] = '---'

# --- Deforestation ---
forests_rainforest_congo_stressors["Deforestation"]["Metric"] = 'Area of forest cleared per year (hectares/year).'
forests_rainforest_congo_stressors["Deforestation"]["Data Sources"] = ['Remote sensing data (satellite imagery).', 'Reports from environmental organizations and research institutions.', 'Governmental data (where available and reliable).', '**Impact on Area:** Direct reduction of rainforest area.', '**Impact on Biodiversity:**', 'Habitat loss and fragmentation.', 'Loss of carbon storage.', 'Disruption of ecological processes.', '**Influenced By (Stressors):**', 'Infrastructure Development: Access for logging and agriculture.', 'Economic Growth: Demand for timber and agricultural land.', 'Global Commodity Prices: Prices for timber, palm oil, and other commodities.', 'Population Growth: Subsistence agriculture and fuelwood collection.', 'Government Policies: Weak enforcement of environmental regulations.', '**Influences (Stressors):**', 'Wildfires: Increased susceptibility to fire.', 'Changes in Precipitation (potentially).', '**Logic Description:** Deforestation, driven by logging (both legal and illegal), agricultural expansion (including small-scale subsistence farming), and fuelwood collection, directly reduces forest area and biodiversity.']
forests_rainforest_congo_stressors["Deforestation"]["Impact on Area"] = 'Direct reduction of rainforest area.'
forests_rainforest_congo_stressors["Deforestation"]["Impact on Biodiversity"] = 'Habitat loss and fragmentation.\nLoss of carbon storage.\nDisruption of ecological processes.\n**Influenced By (Stressors):**\nInfrastructure Development: Access for logging and agriculture.\nEconomic Growth: Demand for timber and agricultural land.\nGlobal Commodity Prices: Prices for timber, palm oil, and other commodities.\nPopulation Growth: Subsistence agriculture and fuelwood collection.\nGovernment Policies: Weak enforcement of environmental regulations.\n**Influences (Stressors):**\nWildfires: Increased susceptibility to fire.\nChanges in Precipitation (potentially).\n**Logic Description:** Deforestation, driven by logging (both legal and illegal), agricultural expansion (including small-scale subsistence farming), and fuelwood collection, directly reduces forest area and biodiversity.'
forests_rainforest_congo_stressors["Deforestation"]["Influenced By"] = ['Infrastructure Development: Access for logging and agriculture.', 'Economic Growth: Demand for timber and agricultural land.', 'Global Commodity Prices: Prices for timber, palm oil, and other commodities.', 'Population Growth: Subsistence agriculture and fuelwood collection.', 'Government Policies: Weak enforcement of environmental regulations.', '**Influences (Stressors):**', 'Wildfires: Increased susceptibility to fire.', 'Changes in Precipitation (potentially).', '**Logic Description:** Deforestation, driven by logging (both legal and illegal), agricultural expansion (including small-scale subsistence farming), and fuelwood collection, directly reduces forest area and biodiversity.']
forests_rainforest_congo_stressors["Deforestation"]["Influences"] = ['Wildfires: Increased susceptibility to fire.', 'Changes in Precipitation (potentially).', '**Logic Description:** Deforestation, driven by logging (both legal and illegal), agricultural expansion (including small-scale subsistence farming), and fuelwood collection, directly reduces forest area and biodiversity.']
forests_rainforest_congo_stressors["Deforestation"]["Logic Description"] = '---'

# --- Temperature Increase ---
forests_rainforest_congo_stressors["Temperature Increase"]["Metric"] = 'Average annual temperature increase (°C) above a pre-industrial baseline.'
forests_rainforest_congo_stressors["Temperature Increase"]["Data Sources"] = ['Global climate models (GCMs) projections.', 'Regional climate models.', 'Historical temperature records (limited availability in some areas).', '**Impact on Area:** Indirect; exacerbates other stressors.', '**Impact on Biodiversity:**', 'Shifts in species distributions.', 'Increased physiological stress.', 'Increased risk of exceeding thermal limits.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', 'Deforestation: Reduced carbon sequestration.', '**Influences (Stressors):**', 'Wildfires: Increased fire risk.', 'Changes in Precipitation.', '**Logic Description:**  Global warming, exacerbated locally by deforestation, increases temperatures, stressing species and increasing the risk of other stressors like wildfires.']
forests_rainforest_congo_stressors["Temperature Increase"]["Impact on Area"] = 'Indirect; exacerbates other stressors.'
forests_rainforest_congo_stressors["Temperature Increase"]["Impact on Biodiversity"] = 'Shifts in species distributions.\nIncreased physiological stress.\nIncreased risk of exceeding thermal limits.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\nDeforestation: Reduced carbon sequestration.\n**Influences (Stressors):**\nWildfires: Increased fire risk.\nChanges in Precipitation.\n**Logic Description:**  Global warming, exacerbated locally by deforestation, increases temperatures, stressing species and increasing the risk of other stressors like wildfires.'
forests_rainforest_congo_stressors["Temperature Increase"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', 'Deforestation: Reduced carbon sequestration.', '**Influences (Stressors):**', 'Wildfires: Increased fire risk.', 'Changes in Precipitation.', '**Logic Description:**  Global warming, exacerbated locally by deforestation, increases temperatures, stressing species and increasing the risk of other stressors like wildfires.']
forests_rainforest_congo_stressors["Temperature Increase"]["Influences"] = ['Wildfires: Increased fire risk.', 'Changes in Precipitation.', '**Logic Description:**  Global warming, exacerbated locally by deforestation, increases temperatures, stressing species and increasing the risk of other stressors like wildfires.']
forests_rainforest_congo_stressors["Temperature Increase"]["Logic Description"] = '---'

# --- Changes in Precipitation ---
forests_rainforest_congo_stressors["Changes in Precipitation"]["Metric"] = 'Change in annual precipitation (mm/year); changes in dry season length and severity.'
forests_rainforest_congo_stressors["Changes in Precipitation"]["Data Sources"] = ['Global and regional climate models.', 'Historical rainfall records (limited availability).', '**Impact on Area:** Indirect; potential vegetation shifts.', '**Impact on Biodiversity:**', 'Changes in species distributions.', 'Increased drought stress.', 'Altered river flow regimes.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', 'Deforestation (potentially).', '**Influences (Stressors):**', 'Wildfires: Increased fire risk with longer dry seasons.', '**Logic Description:** Climate change and potentially deforestation alter rainfall patterns, increasing drought stress and affecting aquatic ecosystems.']
forests_rainforest_congo_stressors["Changes in Precipitation"]["Impact on Area"] = 'Indirect; potential vegetation shifts.'
forests_rainforest_congo_stressors["Changes in Precipitation"]["Impact on Biodiversity"] = 'Changes in species distributions.\nIncreased drought stress.\nAltered river flow regimes.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\nDeforestation (potentially).\n**Influences (Stressors):**\nWildfires: Increased fire risk with longer dry seasons.\n**Logic Description:** Climate change and potentially deforestation alter rainfall patterns, increasing drought stress and affecting aquatic ecosystems.'
forests_rainforest_congo_stressors["Changes in Precipitation"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', 'Deforestation (potentially).', '**Influences (Stressors):**', 'Wildfires: Increased fire risk with longer dry seasons.', '**Logic Description:** Climate change and potentially deforestation alter rainfall patterns, increasing drought stress and affecting aquatic ecosystems.']
forests_rainforest_congo_stressors["Changes in Precipitation"]["Influences"] = ['Wildfires: Increased fire risk with longer dry seasons.', '**Logic Description:** Climate change and potentially deforestation alter rainfall patterns, increasing drought stress and affecting aquatic ecosystems.']
forests_rainforest_congo_stressors["Changes in Precipitation"]["Logic Description"] = '---'

# --- Wildfires ---
forests_rainforest_congo_stressors["Wildfires"]["Metric"] = 'Number of wildfires per year; total area burned (hectares/year).'
forests_rainforest_congo_stressors["Wildfires"]["Data Sources"] = [' Remote sensing data (satellite imagery).', ' Reports from local communities and environmental organizations.', '**Impact on Area:** Direct loss of forest area.', '**Impact on Biodiversity:**', ' Direct mortality of plants and animals.', 'Habitat loss.', ' Air pollution.', '**Influenced By (Stressors):**', 'Deforestation: Creates drier, more flammable conditions.', 'Temperature Increase: Increased fire risk.', ' Changes in Precipitation: Longer dry seasons increase risk.', 'Human Activities: Agricultural burning, accidental fires.', '**Influences (Stressors):**', 'Deforestation.', '**Logic Description:** Wildfires, often linked to deforestation and agricultural practices, are exacerbated by climate change, leading to direct forest loss and biodiversity impacts.']
forests_rainforest_congo_stressors["Wildfires"]["Impact on Area"] = 'Direct loss of forest area.'
forests_rainforest_congo_stressors["Wildfires"]["Impact on Biodiversity"] = ' Direct mortality of plants and animals.\nHabitat loss.\n Air pollution.\n**Influenced By (Stressors):**\nDeforestation: Creates drier, more flammable conditions.\nTemperature Increase: Increased fire risk.\n Changes in Precipitation: Longer dry seasons increase risk.\nHuman Activities: Agricultural burning, accidental fires.\n**Influences (Stressors):**\nDeforestation.\n**Logic Description:** Wildfires, often linked to deforestation and agricultural practices, are exacerbated by climate change, leading to direct forest loss and biodiversity impacts.'
forests_rainforest_congo_stressors["Wildfires"]["Influenced By"] = ['Deforestation: Creates drier, more flammable conditions.', 'Temperature Increase: Increased fire risk.', ' Changes in Precipitation: Longer dry seasons increase risk.', 'Human Activities: Agricultural burning, accidental fires.', '**Influences (Stressors):**', 'Deforestation.', '**Logic Description:** Wildfires, often linked to deforestation and agricultural practices, are exacerbated by climate change, leading to direct forest loss and biodiversity impacts.']
forests_rainforest_congo_stressors["Wildfires"]["Influences"] = ['Deforestation.', '**Logic Description:** Wildfires, often linked to deforestation and agricultural practices, are exacerbated by climate change, leading to direct forest loss and biodiversity impacts.']
forests_rainforest_congo_stressors["Wildfires"]["Logic Description"] = '---'

