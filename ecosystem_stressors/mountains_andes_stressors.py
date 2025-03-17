from stressor_templates import *
import copy

mountains_andes_stressors = {
    "Glacier Retreat": {},
    "Land-Use Change": {},
    "Mining": {},
    "Overgrazing": {},
    "Climate Change": copy.deepcopy(climate_change_template),
}

# --- Glacier Retreat ---
mountains_andes_stressors["Glacier Retreat"]["Metric"] = 'Change in glacier area (km²) and volume (km³); glacier mass balance.'
mountains_andes_stressors["Glacier Retreat"]["Data Sources"] = ['Remote sensing data (satellite imagery).', 'Field measurements (where available).', 'Research publications (e.g., from the *Instituto Nacional de Investigación en Glaciares y Ecosistemas de Montaña* (INAIGEM) in Peru, and similar institutions in other Andean countries).', '**Impact on Area:** *Rapid and widespread* glacier loss; changes in water availability.', '**Impact on Biodiversity:**', 'Loss of habitat for glacier-dependent species.', 'Changes in downstream water availability and temperature, affecting aquatic ecosystems.', 'Increased risk of glacial lake outburst floods (GLOFs).', '**Influenced By (Stressors):**', 'Temperature Increase: The primary driver.', 'Changes in Precipitation (in some areas).', '* Black Carbon', '**Influences (Stressors):**', 'Water Resources: *Critical* for downstream populations and agriculture.', 'Hazard Risks (GLOFs).', '**Logic Description:** The Andes are experiencing *very high* rates of glacier retreat, which is a *critical* issue for water resources in many Andean countries.  This is a major impact of climate change.']
mountains_andes_stressors["Glacier Retreat"]["Impact on Area"] = '*Rapid and widespread* glacier loss; changes in water availability.'
mountains_andes_stressors["Glacier Retreat"]["Impact on Biodiversity"] = 'Loss of habitat for glacier-dependent species.\nChanges in downstream water availability and temperature, affecting aquatic ecosystems.\nIncreased risk of glacial lake outburst floods (GLOFs).\n**Influenced By (Stressors):**\nTemperature Increase: The primary driver.\nChanges in Precipitation (in some areas).\n* Black Carbon\n**Influences (Stressors):**\nWater Resources: *Critical* for downstream populations and agriculture.\nHazard Risks (GLOFs).\n**Logic Description:** The Andes are experiencing *very high* rates of glacier retreat, which is a *critical* issue for water resources in many Andean countries.  This is a major impact of climate change.'
mountains_andes_stressors["Glacier Retreat"]["Influenced By"] = ['Temperature Increase: The primary driver.', 'Changes in Precipitation (in some areas).', '* Black Carbon', '**Influences (Stressors):**', 'Water Resources: *Critical* for downstream populations and agriculture.', 'Hazard Risks (GLOFs).', '**Logic Description:** The Andes are experiencing *very high* rates of glacier retreat, which is a *critical* issue for water resources in many Andean countries.  This is a major impact of climate change.']
mountains_andes_stressors["Glacier Retreat"]["Influences"] = ['Water Resources: *Critical* for downstream populations and agriculture.', 'Hazard Risks (GLOFs).', '**Logic Description:** The Andes are experiencing *very high* rates of glacier retreat, which is a *critical* issue for water resources in many Andean countries.  This is a major impact of climate change.']
mountains_andes_stressors["Glacier Retreat"]["Logic Description"] = '---'

# --- Land-Use Change ---
mountains_andes_stressors["Land-Use Change"]["Metric"] = 'Area deforested (ha/year); area converted to agriculture and pasture (ha/year).'
mountains_andes_stressors["Land-Use Change"]["Data Sources"] = ['Remote sensing data.', 'Government statistics (often incomplete).', 'Research publications.', '**Impact on Area:** Habitat loss and fragmentation; soil erosion.', '**Impact on Biodiversity:**', 'Loss of habitat for *highly endemic* species.', 'Increased human-wildlife conflict.', 'Impacts on water quality.', '**Influenced By (Stressors):**', 'Agricultural Expansion: Subsistence agriculture and commercial agriculture.', 'Mining Activities.', 'Population Growth.', 'Logging (in some areas).', '**Influences (Stressors):**', 'Soil Erosion.', 'Water Quality.', 'Habitat Fragmentation', '**Logic Description:** Deforestation and land-use change for agriculture and mining are significant threats, particularly given the high levels of endemism in the Andes.']
mountains_andes_stressors["Land-Use Change"]["Impact on Area"] = 'Habitat loss and fragmentation; soil erosion.'
mountains_andes_stressors["Land-Use Change"]["Impact on Biodiversity"] = 'Loss of habitat for *highly endemic* species.\nIncreased human-wildlife conflict.\nImpacts on water quality.\n**Influenced By (Stressors):**\nAgricultural Expansion: Subsistence agriculture and commercial agriculture.\nMining Activities.\nPopulation Growth.\nLogging (in some areas).\n**Influences (Stressors):**\nSoil Erosion.\nWater Quality.\nHabitat Fragmentation\n**Logic Description:** Deforestation and land-use change for agriculture and mining are significant threats, particularly given the high levels of endemism in the Andes.'
mountains_andes_stressors["Land-Use Change"]["Influenced By"] = ['Agricultural Expansion: Subsistence agriculture and commercial agriculture.', 'Mining Activities.', 'Population Growth.', 'Logging (in some areas).', '**Influences (Stressors):**', 'Soil Erosion.', 'Water Quality.', 'Habitat Fragmentation', '**Logic Description:** Deforestation and land-use change for agriculture and mining are significant threats, particularly given the high levels of endemism in the Andes.']
mountains_andes_stressors["Land-Use Change"]["Influences"] = ['Soil Erosion.', 'Water Quality.', 'Habitat Fragmentation', '**Logic Description:** Deforestation and land-use change for agriculture and mining are significant threats, particularly given the high levels of endemism in the Andes.']
mountains_andes_stressors["Land-Use Change"]["Logic Description"] = '---'

# --- Mining ---
mountains_andes_stressors["Mining"]["Metric"] = 'Area affected by mining operations; water use and pollution from mining.'
mountains_andes_stressors["Mining"]["Data Sources"] = ['* Government records', '* Research', '**Impact on Area:** Habitat destruction, water pollution, and contamination.', '**Impact on Biodiversity:**', '* Impacts on sensitive ecosystems.', '**Influenced By (Stressors):**', '* Global demand for minerals', '**Influences (Stressors):**', '* Water resources', '* Pollution', '**Logic Description:** Mining is a major economic activity but also a significant environmental stressor.']
mountains_andes_stressors["Mining"]["Impact on Area"] = 'Habitat destruction, water pollution, and contamination.'
mountains_andes_stressors["Mining"]["Impact on Biodiversity"] = '* Impacts on sensitive ecosystems.\n**Influenced By (Stressors):**\n* Global demand for minerals\n**Influences (Stressors):**\n* Water resources\n* Pollution\n**Logic Description:** Mining is a major economic activity but also a significant environmental stressor.'
mountains_andes_stressors["Mining"]["Influenced By"] = ['* Global demand for minerals', '**Influences (Stressors):**', '* Water resources', '* Pollution', '**Logic Description:** Mining is a major economic activity but also a significant environmental stressor.']
mountains_andes_stressors["Mining"]["Influences"] = ['* Water resources', '* Pollution', '**Logic Description:** Mining is a major economic activity but also a significant environmental stressor.']
mountains_andes_stressors["Mining"]["Logic Description"] = '---'

# --- Overgrazing ---
mountains_andes_stressors["Overgrazing"]["Metric"] = 'Livestock density.'
mountains_andes_stressors["Overgrazing"]["Data Sources"] = ['* Agricultural statistics.', '**Impact on Area:** Vegetation degradation.', '**Impact on Biodiversity:**', '* Impact on plant communities.', '**Influenced By (Stressors):**', 'Livestock management.', '**Influences (Stressors):**', '* Desertification', '**Logic Description:** Overgrazing impacts vegetation.']
mountains_andes_stressors["Overgrazing"]["Impact on Area"] = 'Vegetation degradation.'
mountains_andes_stressors["Overgrazing"]["Impact on Biodiversity"] = '* Impact on plant communities.\n**Influenced By (Stressors):**\nLivestock management.\n**Influences (Stressors):**\n* Desertification\n**Logic Description:** Overgrazing impacts vegetation.'
mountains_andes_stressors["Overgrazing"]["Influenced By"] = ['Livestock management.', '**Influences (Stressors):**', '* Desertification', '**Logic Description:** Overgrazing impacts vegetation.']
mountains_andes_stressors["Overgrazing"]["Influences"] = ['* Desertification', '**Logic Description:** Overgrazing impacts vegetation.']
mountains_andes_stressors["Overgrazing"]["Logic Description"] = '---'

# --- Climate Change ---
mountains_andes_stressors["Climate Change"]["Metric"] = 'Temperature changes, precipitation changes, frequency of extreme events.'
mountains_andes_stressors["Climate Change"]["Data Sources"] = ['* Climate Models', '* Historical records', '**Impact on Area:** Changes to ecosystems', '**Impact on Biodiversity:**', '* Shifts in species distributions.', '* Increased stress', '**Influenced By (Stressors):**', '* Global GHG', '**Influences (Stressors):**', '* Water resources.', '**Logic Description:** Climate change is a pervasive stressor.']
mountains_andes_stressors["Climate Change"]["Impact on Area"] = 'Changes to ecosystems'
mountains_andes_stressors["Climate Change"]["Impact on Biodiversity"] = '* Shifts in species distributions.\n* Increased stress\n**Influenced By (Stressors):**\n* Global GHG\n**Influences (Stressors):**\n* Water resources.\n**Logic Description:** Climate change is a pervasive stressor.'
mountains_andes_stressors["Climate Change"]["Influenced By"] = ['* Global GHG', '**Influences (Stressors):**', '* Water resources.', '**Logic Description:** Climate change is a pervasive stressor.']
mountains_andes_stressors["Climate Change"]["Influences"] = ['* Water resources.', '**Logic Description:** Climate change is a pervasive stressor.']
mountains_andes_stressors["Climate Change"]["Logic Description"] = '---'

