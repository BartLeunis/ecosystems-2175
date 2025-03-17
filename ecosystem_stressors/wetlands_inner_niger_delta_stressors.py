from stressor_templates import *
import copy

wetlands_inner_niger_delta_stressors = {
    "Deforestation": copy.deepcopy(deforestation_template),
}

# --- Deforestation ---
wetlands_inner_niger_delta_stressors["Deforestation"]["Metric"] = 'Area of forest cleared (ha/year), particularly in the floodplain.'
wetlands_inner_niger_delta_stressors["Deforestation"]["Data Sources"] = ['Remote sensing data.', 'Local reports.', 'Research studies.', '**Impact on Area:** Loss of trees within and around the delta.', '**Impact on Biodiversity:**', 'Loss of habitat for birds and other wildlife.', 'Increased soil erosion and sedimentation in the delta.', 'Reduced availability of fuelwood (impacting local communities).', '**Influenced By (Stressors):**', 'Population Growth: Increased demand for fuelwood and land.', 'Agricultural Expansion: Clearing land for crops.', '**Influences (Stressors):**', 'Water Quality (through increased sedimentation).', 'Habitat Availability', '**Logic Description:** Deforestation, driven by population growth and agricultural expansion, is impacting both biodiversity and the livelihoods of communities that depend on forest resources.']
wetlands_inner_niger_delta_stressors["Deforestation"]["Impact on Area"] = 'Loss of trees within and around the delta.'
wetlands_inner_niger_delta_stressors["Deforestation"]["Impact on Biodiversity"] = 'Loss of habitat for birds and other wildlife.\nIncreased soil erosion and sedimentation in the delta.\nReduced availability of fuelwood (impacting local communities).\n**Influenced By (Stressors):**\nPopulation Growth: Increased demand for fuelwood and land.\nAgricultural Expansion: Clearing land for crops.\n**Influences (Stressors):**\nWater Quality (through increased sedimentation).\nHabitat Availability\n**Logic Description:** Deforestation, driven by population growth and agricultural expansion, is impacting both biodiversity and the livelihoods of communities that depend on forest resources.'
wetlands_inner_niger_delta_stressors["Deforestation"]["Influenced By"] = ['Population Growth: Increased demand for fuelwood and land.', 'Agricultural Expansion: Clearing land for crops.', '**Influences (Stressors):**', 'Water Quality (through increased sedimentation).', 'Habitat Availability', '**Logic Description:** Deforestation, driven by population growth and agricultural expansion, is impacting both biodiversity and the livelihoods of communities that depend on forest resources.']
wetlands_inner_niger_delta_stressors["Deforestation"]["Influences"] = ['Water Quality (through increased sedimentation).', 'Habitat Availability', '**Logic Description:** Deforestation, driven by population growth and agricultural expansion, is impacting both biodiversity and the livelihoods of communities that depend on forest resources.']
wetlands_inner_niger_delta_stressors["Deforestation"]["Logic Description"] = '---'
wetlands_inner_niger_delta_stressors["Deforestation"]["Impact Function"] = "impact_deforestation_wetlands_inner_niger_delta"

