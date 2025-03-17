from stressor_templates import *
import copy

deserts_namib_stressors = {
    "Climate Change": copy.deepcopy(climate_change_template),
    "Mining": {},
    "Off-Road Driving": {},
}

# --- Climate Change ---
deserts_namib_stressors["Climate Change"]["Metric"] = 'Temperature increase (°C); changes in fog frequency and intensity; changes in precipitation (mm/year).'
deserts_namib_stressors["Climate Change"]["Data Sources"] = ['Climate models.', 'Historical weather records (limited).', 'Research publications.', '**Impact on Area:** Increased aridity; potential shifts in fog patterns.', '**Impact on Biodiversity:**', 'The Namib Desert is highly adapted to fog, and changes in fog patterns could have *significant* impacts on species that depend on it.', 'Increased stress on desert species due to higher temperatures.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Fog Patterns: A *critical* factor for the Namib.', '**Logic Description:** Climate change impacts on temperature and, *crucially*, fog patterns, threaten the unique adaptations of Namib Desert species.']
deserts_namib_stressors["Climate Change"]["Impact on Area"] = 'Increased aridity; potential shifts in fog patterns.'
deserts_namib_stressors["Climate Change"]["Impact on Biodiversity"] = 'The Namib Desert is highly adapted to fog, and changes in fog patterns could have *significant* impacts on species that depend on it.\nIncreased stress on desert species due to higher temperatures.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\n**Influences (Stressors):**\nFog Patterns: A *critical* factor for the Namib.\n**Logic Description:** Climate change impacts on temperature and, *crucially*, fog patterns, threaten the unique adaptations of Namib Desert species.'
deserts_namib_stressors["Climate Change"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Fog Patterns: A *critical* factor for the Namib.', '**Logic Description:** Climate change impacts on temperature and, *crucially*, fog patterns, threaten the unique adaptations of Namib Desert species.']
deserts_namib_stressors["Climate Change"]["Influences"] = ['Fog Patterns: A *critical* factor for the Namib.', '**Logic Description:** Climate change impacts on temperature and, *crucially*, fog patterns, threaten the unique adaptations of Namib Desert species.']
deserts_namib_stressors["Climate Change"]["Logic Description"] = '---'

# --- Mining ---
deserts_namib_stressors["Mining"]["Metric"] = 'Area affected by mining operations (ha); water use by mining; pollution levels.'
deserts_namib_stressors["Mining"]["Data Sources"] = ['Government mining records (Namibia).', 'Environmental Impact Assessments (EIAs).', 'Research publications.', '**Impact on Area:** Habitat loss and degradation; water depletion; pollution.', '**Impact on Biodiversity:**', 'Direct habitat destruction.', 'Impacts on water resources.', 'Potential for toxic effects from pollutants.', '**Influenced By (Stressors):**', 'Global Demand for Minerals: (e.g., uranium, diamonds).', 'Government Policies.', '**Influences (Stressors):**', 'Water Resources.', 'Pollution.', '**Logic Description:** Mining activities, particularly for uranium and diamonds, can impact fragile desert habitats and water resources.']
deserts_namib_stressors["Mining"]["Impact on Area"] = 'Habitat loss and degradation; water depletion; pollution.'
deserts_namib_stressors["Mining"]["Impact on Biodiversity"] = 'Direct habitat destruction.\nImpacts on water resources.\nPotential for toxic effects from pollutants.\n**Influenced By (Stressors):**\nGlobal Demand for Minerals: (e.g., uranium, diamonds).\nGovernment Policies.\n**Influences (Stressors):**\nWater Resources.\nPollution.\n**Logic Description:** Mining activities, particularly for uranium and diamonds, can impact fragile desert habitats and water resources.'
deserts_namib_stressors["Mining"]["Influenced By"] = ['Global Demand for Minerals: (e.g., uranium, diamonds).', 'Government Policies.', '**Influences (Stressors):**', 'Water Resources.', 'Pollution.', '**Logic Description:** Mining activities, particularly for uranium and diamonds, can impact fragile desert habitats and water resources.']
deserts_namib_stressors["Mining"]["Influences"] = ['Water Resources.', 'Pollution.', '**Logic Description:** Mining activities, particularly for uranium and diamonds, can impact fragile desert habitats and water resources.']
deserts_namib_stressors["Mining"]["Logic Description"] = '---'

# --- Off-Road Driving ---
deserts_namib_stressors["Off-Road Driving"]["Metric"] = 'Area impacted'
deserts_namib_stressors["Off-Road Driving"]["Data Sources"] = ['* Remote sensing', '* Research', '**Impact on Area:**', '* Disturbance to soil crusts', '**Impact on Biodiversity:**', 'Impacts on slow-growing lichens and other desert organisms.', '**Influenced By (Stressors):**', '* Tourism', '**Influences (Stressors):**', '* Soil and vegetation', '**Logic Description:** Off-road driving can damage sensitive desert ecosystems.']
deserts_namib_stressors["Off-Road Driving"]["Impact on Area"] = ''
deserts_namib_stressors["Off-Road Driving"]["Impact on Biodiversity"] = 'Impacts on slow-growing lichens and other desert organisms.\n**Influenced By (Stressors):**\n* Tourism\n**Influences (Stressors):**\n* Soil and vegetation\n**Logic Description:** Off-road driving can damage sensitive desert ecosystems.'
deserts_namib_stressors["Off-Road Driving"]["Influenced By"] = ['* Tourism', '**Influences (Stressors):**', '* Soil and vegetation', '**Logic Description:** Off-road driving can damage sensitive desert ecosystems.']
deserts_namib_stressors["Off-Road Driving"]["Influences"] = ['* Soil and vegetation', '**Logic Description:** Off-road driving can damage sensitive desert ecosystems.']
deserts_namib_stressors["Off-Road Driving"]["Logic Description"] = '---'

