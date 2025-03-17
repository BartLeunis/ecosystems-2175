from stressor_templates import *
import copy

mountains_alps_stressors = {
    "Tourism": {},
    "Changes in Snowpack": {},
    "Air Pollution": copy.deepcopy(pollution_template),
    "Land Abandonment": {},
    "Climate Change": copy.deepcopy(climate_change_template),
}

# --- Tourism ---
mountains_alps_stressors["Tourism"]["Metric"] = 'Number of tourists (winter and summer); area of ski resorts and other tourism infrastructure.'
mountains_alps_stressors["Tourism"]["Data Sources"] = ['Tourism statistics (various Alpine countries).', 'Remote sensing data.', '**Impact on Area:** Habitat loss and fragmentation; disturbance to wildlife; pollution; pressure on water resources.', '**Impact on Biodiversity:**', 'Impacts on sensitive alpine ecosystems.', 'Disturbance to wildlife.', 'Loss of habitat.', '**Influenced By (Stressors):**', 'High Demand for Skiing and Other Mountain Recreation.', 'Economic Importance of Tourism.', '**Influences (Stressors):**', 'Habitat Fragmentation.', 'Water Resources.', '* Pollution', '**Logic Description:** Tourism, particularly skiing, is a *major* economic activity in the Alps but also a *significant* environmental stressor, impacting habitat, water resources, and wildlife.']
mountains_alps_stressors["Tourism"]["Impact on Area"] = 'Habitat loss and fragmentation; disturbance to wildlife; pollution; pressure on water resources.'
mountains_alps_stressors["Tourism"]["Impact on Biodiversity"] = 'Impacts on sensitive alpine ecosystems.\nDisturbance to wildlife.\nLoss of habitat.\n**Influenced By (Stressors):**\nHigh Demand for Skiing and Other Mountain Recreation.\nEconomic Importance of Tourism.\n**Influences (Stressors):**\nHabitat Fragmentation.\nWater Resources.\n* Pollution\n**Logic Description:** Tourism, particularly skiing, is a *major* economic activity in the Alps but also a *significant* environmental stressor, impacting habitat, water resources, and wildlife.'
mountains_alps_stressors["Tourism"]["Influenced By"] = ['High Demand for Skiing and Other Mountain Recreation.', 'Economic Importance of Tourism.', '**Influences (Stressors):**', 'Habitat Fragmentation.', 'Water Resources.', '* Pollution', '**Logic Description:** Tourism, particularly skiing, is a *major* economic activity in the Alps but also a *significant* environmental stressor, impacting habitat, water resources, and wildlife.']
mountains_alps_stressors["Tourism"]["Influences"] = ['Habitat Fragmentation.', 'Water Resources.', '* Pollution', '**Logic Description:** Tourism, particularly skiing, is a *major* economic activity in the Alps but also a *significant* environmental stressor, impacting habitat, water resources, and wildlife.']
mountains_alps_stressors["Tourism"]["Logic Description"] = '---'

# --- Changes in Snowpack ---
mountains_alps_stressors["Changes in Snowpack"]["Metric"] = 'Snow depth; snow duration; timing of snowmelt.'
mountains_alps_stressors["Changes in Snowpack"]["Data Sources"] = ['Snow monitoring stations.', 'Remote sensing data.', 'Climate models.', '**Impact on Area:** Impacts on winter tourism; changes in water availability.', '**Impact on Biodiversity:**', 'Changes in vegetation distribution.', 'Impacts on species that depend on snow cover.', 'Altered streamflow regimes.', '**Influenced By (Stressors):**', 'Temperature Increase.', 'Changes in Precipitation.', '**Influences (Stressors):**', 'Winter Tourism (skiing).', 'Water Resources.', 'Ecosystem Functioning', '**Logic Description:** Changes in snowpack, driven by climate change, are impacting winter tourism, water resources, and alpine ecosystems.']
mountains_alps_stressors["Changes in Snowpack"]["Impact on Area"] = 'Impacts on winter tourism; changes in water availability.'
mountains_alps_stressors["Changes in Snowpack"]["Impact on Biodiversity"] = 'Changes in vegetation distribution.\nImpacts on species that depend on snow cover.\nAltered streamflow regimes.\n**Influenced By (Stressors):**\nTemperature Increase.\nChanges in Precipitation.\n**Influences (Stressors):**\nWinter Tourism (skiing).\nWater Resources.\nEcosystem Functioning\n**Logic Description:** Changes in snowpack, driven by climate change, are impacting winter tourism, water resources, and alpine ecosystems.'
mountains_alps_stressors["Changes in Snowpack"]["Influenced By"] = ['Temperature Increase.', 'Changes in Precipitation.', '**Influences (Stressors):**', 'Winter Tourism (skiing).', 'Water Resources.', 'Ecosystem Functioning', '**Logic Description:** Changes in snowpack, driven by climate change, are impacting winter tourism, water resources, and alpine ecosystems.']
mountains_alps_stressors["Changes in Snowpack"]["Influences"] = ['Winter Tourism (skiing).', 'Water Resources.', 'Ecosystem Functioning', '**Logic Description:** Changes in snowpack, driven by climate change, are impacting winter tourism, water resources, and alpine ecosystems.']
mountains_alps_stressors["Changes in Snowpack"]["Logic Description"] = '---'

# --- Air Pollution ---
mountains_alps_stressors["Air Pollution"]["Metric"] = 'Concentrations of pollutants (ozone, nitrogen oxides, particulate matter).'
mountains_alps_stressors["Air Pollution"]["Data Sources"] = ['Air quality monitoring networks.', 'Research studies.', '**Impact on Area:** Impacts on forest health; acidification of soils and water.', '**Impact on Biodiversity:**', 'Damage to vegetation.', 'Impacts on sensitive species.', '**Influenced By (Stressors):**', 'Proximity to Industrial Areas: (in Europe).', 'Traffic Emissions: (in valleys).', 'Long-Range Transport of Pollutants.', '**Influences (Stressors):**', 'Forest Health.', 'Water Quality.', '**Logic Description:** Air pollution, from both local and distant sources, is a concern in the Alps, impacting forests and water quality.']
mountains_alps_stressors["Air Pollution"]["Impact on Area"] = 'Impacts on forest health; acidification of soils and water.'
mountains_alps_stressors["Air Pollution"]["Impact on Biodiversity"] = 'Damage to vegetation.\nImpacts on sensitive species.\n**Influenced By (Stressors):**\nProximity to Industrial Areas: (in Europe).\nTraffic Emissions: (in valleys).\nLong-Range Transport of Pollutants.\n**Influences (Stressors):**\nForest Health.\nWater Quality.\n**Logic Description:** Air pollution, from both local and distant sources, is a concern in the Alps, impacting forests and water quality.'
mountains_alps_stressors["Air Pollution"]["Influenced By"] = ['Proximity to Industrial Areas: (in Europe).', 'Traffic Emissions: (in valleys).', 'Long-Range Transport of Pollutants.', '**Influences (Stressors):**', 'Forest Health.', 'Water Quality.', '**Logic Description:** Air pollution, from both local and distant sources, is a concern in the Alps, impacting forests and water quality.']
mountains_alps_stressors["Air Pollution"]["Influences"] = ['Forest Health.', 'Water Quality.', '**Logic Description:** Air pollution, from both local and distant sources, is a concern in the Alps, impacting forests and water quality.']
mountains_alps_stressors["Air Pollution"]["Logic Description"] = '---'

# --- Land Abandonment ---
mountains_alps_stressors["Land Abandonment"]["Metric"] = 'Area of abandoned agricultural land.'
mountains_alps_stressors["Land Abandonment"]["Data Sources"] = ['* Agricultural statistics.', '* Remote sensing.', '**Impact on Area:** Forest encroachment on alpine meadows.', '**Impact on Biodiversity:**', 'Loss of open habitat.', '* Changes in species composition.', '**Influenced By (Stressors):**', '* Socioeconomic changes (rural depopulation).', '**Influences (Stressors):**', '* Habitat structure', '**Logic Description:** Abandonment of traditional agricultural practices can lead to changes in vegetation.']
mountains_alps_stressors["Land Abandonment"]["Impact on Area"] = 'Forest encroachment on alpine meadows.'
mountains_alps_stressors["Land Abandonment"]["Impact on Biodiversity"] = 'Loss of open habitat.\n* Changes in species composition.\n**Influenced By (Stressors):**\n* Socioeconomic changes (rural depopulation).\n**Influences (Stressors):**\n* Habitat structure\n**Logic Description:** Abandonment of traditional agricultural practices can lead to changes in vegetation.'
mountains_alps_stressors["Land Abandonment"]["Influenced By"] = ['* Socioeconomic changes (rural depopulation).', '**Influences (Stressors):**', '* Habitat structure', '**Logic Description:** Abandonment of traditional agricultural practices can lead to changes in vegetation.']
mountains_alps_stressors["Land Abandonment"]["Influences"] = ['* Habitat structure', '**Logic Description:** Abandonment of traditional agricultural practices can lead to changes in vegetation.']
mountains_alps_stressors["Land Abandonment"]["Logic Description"] = '---'

# --- Climate Change ---
mountains_alps_stressors["Climate Change"]["Metric"] = 'Changes in temperature, precipitation'
mountains_alps_stressors["Climate Change"]["Data Sources"] = ['* Models, records', '**Impact on Area:** Changes to ecosystems', '**Impact on Biodiversity:**', '* Shifts in species', '**Influenced By (Stressors):**', '* Global GHG', '**Influences (Stressors):**', '* Many factors', '**Logic Description:** Climate change.']
mountains_alps_stressors["Climate Change"]["Impact on Area"] = 'Changes to ecosystems'
mountains_alps_stressors["Climate Change"]["Impact on Biodiversity"] = '* Shifts in species\n**Influenced By (Stressors):**\n* Global GHG\n**Influences (Stressors):**\n* Many factors\n**Logic Description:** Climate change.'
mountains_alps_stressors["Climate Change"]["Influenced By"] = ['* Global GHG', '**Influences (Stressors):**', '* Many factors', '**Logic Description:** Climate change.']
mountains_alps_stressors["Climate Change"]["Influences"] = ['* Many factors', '**Logic Description:** Climate change.']
mountains_alps_stressors["Climate Change"]["Logic Description"] = '---'

