from stressor_templates import *
import copy

deserts_kalahari_stressors = {
    "Groundwater Extraction": copy.deepcopy(water_extraction_template),
}

# --- Groundwater Extraction ---
deserts_kalahari_stressors["Groundwater Extraction"]["Metric"] = 'Water extraction rates and groundwater levels.'
deserts_kalahari_stressors["Groundwater Extraction"]["Data Sources"] = ['* Government records.', '* Research', '**Impact on Area:** Depletion of aquifers', '**Impact on Biodiversity:**', '* Loss of water sources for wildlife and vegetation.', '**Influenced By (Stressors):**', '* Agriculture, settlements, and mining.', '**Influences (Stressors):**', '* Water availability', '**Logic Description:** Groundwater extraction is a significant issue.']
deserts_kalahari_stressors["Groundwater Extraction"]["Impact on Area"] = 'Depletion of aquifers'
deserts_kalahari_stressors["Groundwater Extraction"]["Impact on Biodiversity"] = '* Loss of water sources for wildlife and vegetation.\n**Influenced By (Stressors):**\n* Agriculture, settlements, and mining.\n**Influences (Stressors):**\n* Water availability\n**Logic Description:** Groundwater extraction is a significant issue.'
deserts_kalahari_stressors["Groundwater Extraction"]["Influenced By"] = ['* Agriculture, settlements, and mining.', '**Influences (Stressors):**', '* Water availability', '**Logic Description:** Groundwater extraction is a significant issue.']
deserts_kalahari_stressors["Groundwater Extraction"]["Influences"] = ['* Water availability', '**Logic Description:** Groundwater extraction is a significant issue.']
deserts_kalahari_stressors["Groundwater Extraction"]["Logic Description"] = '---'
deserts_kalahari_stressors["Groundwater Extraction"]["Impact Function"] = "impact_groundwater_extraction_deserts_kalahari"

