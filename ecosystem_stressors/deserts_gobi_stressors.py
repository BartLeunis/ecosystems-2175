from stressor_templates import *
import copy

deserts_gobi_stressors = {
    "Climate Change": copy.deepcopy(climate_change_template),
    "Overgrazing": {},
    "Mining": {},
    "Dust Storms": {},
}

# --- Climate Change ---
deserts_gobi_stressors["Climate Change"]["Metric"] = 'Temperature increase (°C); changes in precipitation (mm/year, seasonality); increased frequency and severity of drought.'
deserts_gobi_stressors["Climate Change"]["Data Sources"] = ['Climate models.', 'Historical weather records.', 'Research publications.', '**Impact on Area:** Increased aridity; desertification.', '**Impact on Biodiversity:**', 'Increased stress on desert-adapted species.', 'Potential for local extinctions.', 'Changes in species distributions.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Water Availability.', 'Desertification.', 'Dust Storms.', '**Logic Description:** Climate change is exacerbating aridity and increasing the risk of desertification in the Gobi Desert.']
deserts_gobi_stressors["Climate Change"]["Impact on Area"] = 'Increased aridity; desertification.'
deserts_gobi_stressors["Climate Change"]["Impact on Biodiversity"] = 'Increased stress on desert-adapted species.\nPotential for local extinctions.\nChanges in species distributions.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\n**Influences (Stressors):**\nWater Availability.\nDesertification.\nDust Storms.\n**Logic Description:** Climate change is exacerbating aridity and increasing the risk of desertification in the Gobi Desert.'
deserts_gobi_stressors["Climate Change"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Water Availability.', 'Desertification.', 'Dust Storms.', '**Logic Description:** Climate change is exacerbating aridity and increasing the risk of desertification in the Gobi Desert.']
deserts_gobi_stressors["Climate Change"]["Influences"] = ['Water Availability.', 'Desertification.', 'Dust Storms.', '**Logic Description:** Climate change is exacerbating aridity and increasing the risk of desertification in the Gobi Desert.']
deserts_gobi_stressors["Climate Change"]["Logic Description"] = '---'
deserts_gobi_stressors["Climate Change"]["Impact Function"] = "impact_climate_change_deserts_gobi"

# --- Overgrazing ---
deserts_gobi_stressors["Overgrazing"]["Metric"] = 'Livestock density (number of animals per unit area); vegetation cover and composition; soil erosion.'
deserts_gobi_stressors["Overgrazing"]["Data Sources"] = ['Government statistics (Mongolia, China).', 'Research publications.', 'Remote sensing data.', '**Impact on Area:** Degradation of vegetation; soil erosion; desertification.', '**Impact on Biodiversity:**', 'Loss of palatable plant species.', 'Spread of unpalatable or invasive species.', 'Impacts on wildlife that depend on native vegetation.', '**Influenced By (Stressors):**', 'Livestock Management Practices: Overstocking.', 'Population Growth: Increased demand for livestock products.', 'Economic Factors.', '**Influences (Stressors):**', 'Desertification: A *major* consequence.', 'Dust Storms: Loss of vegetation cover increases dust storm frequency and intensity.', '**Logic Description:** Overgrazing by livestock is a *major* driver of desertification in the Gobi Desert, leading to vegetation degradation, soil erosion, and loss of biodiversity.']
deserts_gobi_stressors["Overgrazing"]["Impact on Area"] = 'Degradation of vegetation; soil erosion; desertification.'
deserts_gobi_stressors["Overgrazing"]["Impact on Biodiversity"] = 'Loss of palatable plant species.\nSpread of unpalatable or invasive species.\nImpacts on wildlife that depend on native vegetation.\n**Influenced By (Stressors):**\nLivestock Management Practices: Overstocking.\nPopulation Growth: Increased demand for livestock products.\nEconomic Factors.\n**Influences (Stressors):**\nDesertification: A *major* consequence.\nDust Storms: Loss of vegetation cover increases dust storm frequency and intensity.\n**Logic Description:** Overgrazing by livestock is a *major* driver of desertification in the Gobi Desert, leading to vegetation degradation, soil erosion, and loss of biodiversity.'
deserts_gobi_stressors["Overgrazing"]["Influenced By"] = ['Livestock Management Practices: Overstocking.', 'Population Growth: Increased demand for livestock products.', 'Economic Factors.', '**Influences (Stressors):**', 'Desertification: A *major* consequence.', 'Dust Storms: Loss of vegetation cover increases dust storm frequency and intensity.', '**Logic Description:** Overgrazing by livestock is a *major* driver of desertification in the Gobi Desert, leading to vegetation degradation, soil erosion, and loss of biodiversity.']
deserts_gobi_stressors["Overgrazing"]["Influences"] = ['Desertification: A *major* consequence.', 'Dust Storms: Loss of vegetation cover increases dust storm frequency and intensity.', '**Logic Description:** Overgrazing by livestock is a *major* driver of desertification in the Gobi Desert, leading to vegetation degradation, soil erosion, and loss of biodiversity.']
deserts_gobi_stressors["Overgrazing"]["Logic Description"] = '---'
deserts_gobi_stressors["Overgrazing"]["Impact Function"] = "impact_overgrazing_deserts_gobi"

# --- Mining ---
deserts_gobi_stressors["Mining"]["Data Sources"] = ['* Government and Company reports', '**Impact on Area:** Habitat Loss', '**Impact on Biodiversity:**', 'Habitat loss and fragmentation.', '* Pollution', '**Influenced By (Stressors):**', '* Demand for resources', '**Influences (Stressors):**', '* Pollution', '**Logic Description:** Mining activities impact.']
deserts_gobi_stressors["Mining"]["Impact on Area"] = 'Habitat Loss'
deserts_gobi_stressors["Mining"]["Impact on Biodiversity"] = 'Habitat loss and fragmentation.\n* Pollution\n**Influenced By (Stressors):**\n* Demand for resources\n**Influences (Stressors):**\n* Pollution\n**Logic Description:** Mining activities impact.'
deserts_gobi_stressors["Mining"]["Influenced By"] = ['* Demand for resources', '**Influences (Stressors):**', '* Pollution', '**Logic Description:** Mining activities impact.']
deserts_gobi_stressors["Mining"]["Influences"] = ['* Pollution', '**Logic Description:** Mining activities impact.']
deserts_gobi_stressors["Mining"]["Logic Description"] = '---'
deserts_gobi_stressors["Mining"]["Impact Function"] = "impact_mining_deserts_gobi"

# --- Dust Storms ---
deserts_gobi_stressors["Dust Storms"]["Metric"] = 'Frequency and intensity of dust storms; visibility; particulate matter concentrations.'
deserts_gobi_stressors["Dust Storms"]["Data Sources"] = ['* Meteorological data.', '* Remote sensing data', '* Research publications.', '**Impact on Area:** Impacts on air quality, soil fertility, and human health *far beyond* the Gobi Desert itself.', '**Impact on Biodiversity:**', 'Can damage vegetation.', 'Can affect animal health.', '**Influenced By (Stressors):**', '* Desertification (loss of vegetation cover).', '* Overgrazing', '* Climate Change (changes in wind patterns, drought).', '**Influences (Stressors):**', '* Air Quality (downwind).', '* Human Health (downwind).', '* Soil Fertility (in areas where dust is deposited).', '**Logic Description:** The Gobi Desert is a major source of dust storms, which can have significant impacts on air quality, human health, and even soil fertility in downwind areas. Desertification and climate change are exacerbating the problem.']
deserts_gobi_stressors["Dust Storms"]["Impact on Area"] = 'Impacts on air quality, soil fertility, and human health *far beyond* the Gobi Desert itself.'
deserts_gobi_stressors["Dust Storms"]["Impact on Biodiversity"] = 'Can damage vegetation.\nCan affect animal health.\n**Influenced By (Stressors):**\n* Desertification (loss of vegetation cover).\n* Overgrazing\n* Climate Change (changes in wind patterns, drought).\n**Influences (Stressors):**\n* Air Quality (downwind).\n* Human Health (downwind).\n* Soil Fertility (in areas where dust is deposited).\n**Logic Description:** The Gobi Desert is a major source of dust storms, which can have significant impacts on air quality, human health, and even soil fertility in downwind areas. Desertification and climate change are exacerbating the problem.'
deserts_gobi_stressors["Dust Storms"]["Influenced By"] = ['* Desertification (loss of vegetation cover).', '* Overgrazing', '* Climate Change (changes in wind patterns, drought).', '**Influences (Stressors):**', '* Air Quality (downwind).', '* Human Health (downwind).', '* Soil Fertility (in areas where dust is deposited).', '**Logic Description:** The Gobi Desert is a major source of dust storms, which can have significant impacts on air quality, human health, and even soil fertility in downwind areas. Desertification and climate change are exacerbating the problem.']
deserts_gobi_stressors["Dust Storms"]["Influences"] = ['* Air Quality (downwind).', '* Human Health (downwind).', '* Soil Fertility (in areas where dust is deposited).', '**Logic Description:** The Gobi Desert is a major source of dust storms, which can have significant impacts on air quality, human health, and even soil fertility in downwind areas. Desertification and climate change are exacerbating the problem.']
deserts_gobi_stressors["Dust Storms"]["Logic Description"] = '---'
deserts_gobi_stressors["Dust Storms"]["Impact Function"] = "impact_dust_storms_deserts_gobi"

