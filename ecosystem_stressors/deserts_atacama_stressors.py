from stressor_templates import *
import copy

deserts_atacama_stressors = {
    "Mining": {},
    "Water Extraction": copy.deepcopy(water_extraction_template),
    "Light Pollution": copy.deepcopy(pollution_template),
    "Climate Change": copy.deepcopy(climate_change_template),
}

# --- Mining ---
deserts_atacama_stressors["Mining"]["Metric"] = 'Area affected by mining operations (ha); water use by mining; pollution levels (e.g., heavy metals).'
deserts_atacama_stressors["Mining"]["Data Sources"] = ['Chilean government mining records.', 'Environmental Impact Assessments (EIAs).', 'Research publications.', '**Impact on Area:** *Major* impacts on water resources; habitat destruction; pollution.', '**Impact on Biodiversity:**', 'Impacts on extremely limited water resources and the unique species that depend on them.', 'Potential for toxic effects from pollutants.', 'Habitat destruction.', '**Influenced By (Stressors):**', 'Global Demand for Minerals: (copper, lithium).', 'Government Policies.', '**Influences (Stressors):**', 'Water Resources: *Critical* in this hyper-arid environment.', 'Pollution.', '**Logic Description:** Mining, particularly for copper and lithium, is a *dominant* stressor in the Atacama, with *major* impacts on extremely limited water resources and unique, highly adapted biodiversity.']
deserts_atacama_stressors["Mining"]["Impact on Area"] = '*Major* impacts on water resources; habitat destruction; pollution.'
deserts_atacama_stressors["Mining"]["Impact on Biodiversity"] = 'Impacts on extremely limited water resources and the unique species that depend on them.\nPotential for toxic effects from pollutants.\nHabitat destruction.\n**Influenced By (Stressors):**\nGlobal Demand for Minerals: (copper, lithium).\nGovernment Policies.\n**Influences (Stressors):**\nWater Resources: *Critical* in this hyper-arid environment.\nPollution.\n**Logic Description:** Mining, particularly for copper and lithium, is a *dominant* stressor in the Atacama, with *major* impacts on extremely limited water resources and unique, highly adapted biodiversity.'
deserts_atacama_stressors["Mining"]["Influenced By"] = ['Global Demand for Minerals: (copper, lithium).', 'Government Policies.', '**Influences (Stressors):**', 'Water Resources: *Critical* in this hyper-arid environment.', 'Pollution.', '**Logic Description:** Mining, particularly for copper and lithium, is a *dominant* stressor in the Atacama, with *major* impacts on extremely limited water resources and unique, highly adapted biodiversity.']
deserts_atacama_stressors["Mining"]["Influences"] = ['Water Resources: *Critical* in this hyper-arid environment.', 'Pollution.', '**Logic Description:** Mining, particularly for copper and lithium, is a *dominant* stressor in the Atacama, with *major* impacts on extremely limited water resources and unique, highly adapted biodiversity.']
deserts_atacama_stressors["Mining"]["Logic Description"] = '---'

# --- Water Extraction ---
deserts_atacama_stressors["Water Extraction"]["Metric"] = 'Volume of water extracted (m³/year); changes in groundwater levels; impacts on oases.'
deserts_atacama_stressors["Water Extraction"]["Data Sources"] = ['Chilean government water resource agencies.', 'Research publications.', '**Impact on Area:** *Severe* water scarcity; loss of oases.', '**Impact on Biodiversity:**', 'Loss of water sources for wildlife and vegetation.', 'Impacts on unique and endemic species.', '**Influenced By (Stressors):**', 'Mining Activities: *Very* high water demand.', 'Agriculture (limited, but present in some areas).', 'Human Consumption.', '**Influences (Stressors):**', 'Water Availability: The *defining* factor.', '**Logic Description:** Water extraction, primarily for mining, is a *critical* threat in the hyper-arid Atacama, impacting the extremely limited water resources and the unique biodiversity that depends on them.']
deserts_atacama_stressors["Water Extraction"]["Impact on Area"] = '*Severe* water scarcity; loss of oases.'
deserts_atacama_stressors["Water Extraction"]["Impact on Biodiversity"] = 'Loss of water sources for wildlife and vegetation.\nImpacts on unique and endemic species.\n**Influenced By (Stressors):**\nMining Activities: *Very* high water demand.\nAgriculture (limited, but present in some areas).\nHuman Consumption.\n**Influences (Stressors):**\nWater Availability: The *defining* factor.\n**Logic Description:** Water extraction, primarily for mining, is a *critical* threat in the hyper-arid Atacama, impacting the extremely limited water resources and the unique biodiversity that depends on them.'
deserts_atacama_stressors["Water Extraction"]["Influenced By"] = ['Mining Activities: *Very* high water demand.', 'Agriculture (limited, but present in some areas).', 'Human Consumption.', '**Influences (Stressors):**', 'Water Availability: The *defining* factor.', '**Logic Description:** Water extraction, primarily for mining, is a *critical* threat in the hyper-arid Atacama, impacting the extremely limited water resources and the unique biodiversity that depends on them.']
deserts_atacama_stressors["Water Extraction"]["Influences"] = ['Water Availability: The *defining* factor.', '**Logic Description:** Water extraction, primarily for mining, is a *critical* threat in the hyper-arid Atacama, impacting the extremely limited water resources and the unique biodiversity that depends on them.']
deserts_atacama_stressors["Water Extraction"]["Logic Description"] = '---'

# --- Light Pollution ---
deserts_atacama_stressors["Light Pollution"]["Data Sources"] = ['* Astronomical observatories', '**Impact on Area:** N/A', '**Impact on Biodiversity**:', '* Impacts on nocturnal species.', '**Influenced By (Stressors):**', '* Astronomy', '* Urban areas', '**Influences (Stressors):**', '* Nocturnal wildlife', '**Logic Description**: The Atacama is a major center for astronomical observation.']
deserts_atacama_stressors["Light Pollution"]["Impact on Area"] = 'N/A'
deserts_atacama_stressors["Light Pollution"]["Influenced By"] = ['* Astronomy', '* Urban areas', '**Influences (Stressors):**', '* Nocturnal wildlife', '**Logic Description**: The Atacama is a major center for astronomical observation.']
deserts_atacama_stressors["Light Pollution"]["Influences"] = ['* Nocturnal wildlife', '**Logic Description**: The Atacama is a major center for astronomical observation.']

# --- Climate Change ---
deserts_atacama_stressors["Climate Change"]["Metric"] = 'Temperature and precipitation changes'
deserts_atacama_stressors["Climate Change"]["Data Sources"] = ['* Climate Models', '* Records', '**Impact on Area:** Impacts already limited water resources', '**Impact on Biodiversity:**', '* Impacts species adapted to extreme conditions', '**Influenced By (Stressors):**', '* Global GHG', '**Influences (Stressors):**', '* Water resources', '**Logic Description**: Climate change impacts.']
deserts_atacama_stressors["Climate Change"]["Impact on Area"] = 'Impacts already limited water resources'
deserts_atacama_stressors["Climate Change"]["Impact on Biodiversity"] = '* Impacts species adapted to extreme conditions\n**Influenced By (Stressors):**\n* Global GHG\n**Influences (Stressors):**\n* Water resources\n**Logic Description**: Climate change impacts.'
deserts_atacama_stressors["Climate Change"]["Influenced By"] = ['* Global GHG', '**Influences (Stressors):**', '* Water resources', '**Logic Description**: Climate change impacts.']
deserts_atacama_stressors["Climate Change"]["Influences"] = ['* Water resources', '**Logic Description**: Climate change impacts.']

