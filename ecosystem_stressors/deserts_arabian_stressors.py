from stressor_templates import *
import copy

deserts_arabian_stressors = {
    "Climate Change": copy.deepcopy(climate_change_template),
    "Water Extraction": copy.deepcopy(water_extraction_template),
    "Oil and Gas Extraction": {},
    "Overgrazing": {},
}

# --- Climate Change ---
deserts_arabian_stressors["Climate Change"]["Metric"] = 'Temperature increase (°C); changes in precipitation (mm/year); increased frequency/severity of drought and heatwaves.'
deserts_arabian_stressors["Climate Change"]["Data Sources"] = ['Climate models.', 'Historical weather records (sparse).', 'Remote sensing.', '**Impact on Area:**  Further aridification; increased stress on water resources.', '**Impact on Biodiversity:**', 'Increased stress on desert-adapted species.', 'Potential for local extinctions.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Water Availability.', '**Logic Description:** Climate change is exacerbating the already extreme conditions of the Arabian Desert.']
deserts_arabian_stressors["Climate Change"]["Impact on Area"] = 'Further aridification; increased stress on water resources.'
deserts_arabian_stressors["Climate Change"]["Impact on Biodiversity"] = 'Increased stress on desert-adapted species.\nPotential for local extinctions.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\n**Influences (Stressors):**\nWater Availability.\n**Logic Description:** Climate change is exacerbating the already extreme conditions of the Arabian Desert.'
deserts_arabian_stressors["Climate Change"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Water Availability.', '**Logic Description:** Climate change is exacerbating the already extreme conditions of the Arabian Desert.']
deserts_arabian_stressors["Climate Change"]["Influences"] = ['Water Availability.', '**Logic Description:** Climate change is exacerbating the already extreme conditions of the Arabian Desert.']
deserts_arabian_stressors["Climate Change"]["Logic Description"] = '---'

# --- Water Extraction ---
deserts_arabian_stressors["Water Extraction"]["Metric"] = 'Volume of groundwater extracted (m³/year); changes in groundwater levels.'
deserts_arabian_stressors["Water Extraction"]["Data Sources"] = ['Governmental water resource agencies (data may be limited).', 'Research studies.', '**Impact on Area:** *Critical* depletion of groundwater resources; loss of oases.', '**Impact on Biodiversity:**', 'Loss of water sources for wildlife.', 'Decline of vegetation.', '**Influenced By (Stressors):**', 'Agricultural Expansion: *Heavy* reliance on groundwater for irrigation.', 'Population Growth: Increased demand for water.', 'Industrial Use.', '**Influences (Stressors):**', 'Water Availability:  A *critical* limiting factor.', '**Logic Description:** Groundwater extraction, primarily for agriculture, is a *major* threat to water resources in the Arabian Desert, impacting both human populations and the limited biodiversity.']
deserts_arabian_stressors["Water Extraction"]["Impact on Area"] = '*Critical* depletion of groundwater resources; loss of oases.'
deserts_arabian_stressors["Water Extraction"]["Impact on Biodiversity"] = 'Loss of water sources for wildlife.\nDecline of vegetation.\n**Influenced By (Stressors):**\nAgricultural Expansion: *Heavy* reliance on groundwater for irrigation.\nPopulation Growth: Increased demand for water.\nIndustrial Use.\n**Influences (Stressors):**\nWater Availability:  A *critical* limiting factor.\n**Logic Description:** Groundwater extraction, primarily for agriculture, is a *major* threat to water resources in the Arabian Desert, impacting both human populations and the limited biodiversity.'
deserts_arabian_stressors["Water Extraction"]["Influenced By"] = ['Agricultural Expansion: *Heavy* reliance on groundwater for irrigation.', 'Population Growth: Increased demand for water.', 'Industrial Use.', '**Influences (Stressors):**', 'Water Availability:  A *critical* limiting factor.', '**Logic Description:** Groundwater extraction, primarily for agriculture, is a *major* threat to water resources in the Arabian Desert, impacting both human populations and the limited biodiversity.']
deserts_arabian_stressors["Water Extraction"]["Influences"] = ['Water Availability:  A *critical* limiting factor.', '**Logic Description:** Groundwater extraction, primarily for agriculture, is a *major* threat to water resources in the Arabian Desert, impacting both human populations and the limited biodiversity.']
deserts_arabian_stressors["Water Extraction"]["Logic Description"] = '---'

# --- Oil and Gas Extraction ---
deserts_arabian_stressors["Oil and Gas Extraction"]["Metric"] = 'Area affected by oil and gas exploration and production (ha); number of oil spills; pollution levels.'
deserts_arabian_stressors["Oil and Gas Extraction"]["Data Sources"] = ['Industry reports.', 'Government data (may be limited).', 'Remote sensing.', 'Research publications.', '**Impact on Area:** Habitat loss and fragmentation; pollution.', '**Impact on Biodiversity:**', 'Direct habitat destruction.', 'Toxic effects of oil spills and pollution.', 'Disturbance from noise and activity.', '**Influenced By (Stressors):**', 'Global Demand for Oil and Gas.', 'Government Policies.', '**Influences (Stressors):**', 'Pollution.', 'Habitat Loss.', '**Logic Description:** Oil and gas extraction is a *major* industry in the Arabian Desert, leading to habitat loss, fragmentation, and pollution, impacting biodiversity.']
deserts_arabian_stressors["Oil and Gas Extraction"]["Impact on Area"] = 'Habitat loss and fragmentation; pollution.'
deserts_arabian_stressors["Oil and Gas Extraction"]["Impact on Biodiversity"] = 'Direct habitat destruction.\nToxic effects of oil spills and pollution.\nDisturbance from noise and activity.\n**Influenced By (Stressors):**\nGlobal Demand for Oil and Gas.\nGovernment Policies.\n**Influences (Stressors):**\nPollution.\nHabitat Loss.\n**Logic Description:** Oil and gas extraction is a *major* industry in the Arabian Desert, leading to habitat loss, fragmentation, and pollution, impacting biodiversity.'
deserts_arabian_stressors["Oil and Gas Extraction"]["Influenced By"] = ['Global Demand for Oil and Gas.', 'Government Policies.', '**Influences (Stressors):**', 'Pollution.', 'Habitat Loss.', '**Logic Description:** Oil and gas extraction is a *major* industry in the Arabian Desert, leading to habitat loss, fragmentation, and pollution, impacting biodiversity.']
deserts_arabian_stressors["Oil and Gas Extraction"]["Influences"] = ['Pollution.', 'Habitat Loss.', '**Logic Description:** Oil and gas extraction is a *major* industry in the Arabian Desert, leading to habitat loss, fragmentation, and pollution, impacting biodiversity.']
deserts_arabian_stressors["Oil and Gas Extraction"]["Logic Description"] = '---'

# --- Overgrazing ---
deserts_arabian_stressors["Overgrazing"]["Metric"] = 'Livestock density'
deserts_arabian_stressors["Overgrazing"]["Data Sources"] = ['* Agricultural data', '**Impact on Area:** Soil and vegetation degradation', '**Impact on Biodiversity:**', '* Impacts on native plant communities.', '**Influenced By (Stressors):**', '* Livestock management.', '**Influences (Stressors):**', '* Desertification', '**Logic Description:** Overgrazing impacts vegetation.']
deserts_arabian_stressors["Overgrazing"]["Impact on Area"] = 'Soil and vegetation degradation'
deserts_arabian_stressors["Overgrazing"]["Impact on Biodiversity"] = '* Impacts on native plant communities.\n**Influenced By (Stressors):**\n* Livestock management.\n**Influences (Stressors):**\n* Desertification\n**Logic Description:** Overgrazing impacts vegetation.'
deserts_arabian_stressors["Overgrazing"]["Influenced By"] = ['* Livestock management.', '**Influences (Stressors):**', '* Desertification', '**Logic Description:** Overgrazing impacts vegetation.']
deserts_arabian_stressors["Overgrazing"]["Influences"] = ['* Desertification', '**Logic Description:** Overgrazing impacts vegetation.']
deserts_arabian_stressors["Overgrazing"]["Logic Description"] = '---'

