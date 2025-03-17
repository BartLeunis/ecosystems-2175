from stressor_templates import *
import copy

deserts_mojave_stressors = {
    "Urban Sprawl and Development": {},
    "Water Extraction": copy.deepcopy(water_extraction_template),
    "Off-Road Vehicle Use": {},
    "Invasive Species": copy.deepcopy(invasive_species_template),
    "Climate Change": copy.deepcopy(climate_change_template),
}

# --- Urban Sprawl and Development ---
deserts_mojave_stressors["Urban Sprawl and Development"]["Metric"] = 'Area converted to urban areas, roads, and other infrastructure (ha/year).'
deserts_mojave_stressors["Urban Sprawl and Development"]["Data Sources"] = ['Remote sensing data.', 'City and county planning documents (Las Vegas, etc.).', 'USGS data.', '**Impact on Area:** Habitat loss and fragmentation.', '**Impact on Biodiversity:**', 'Loss of habitat for desert species (e.g., desert tortoise).', 'Increased human-wildlife conflict.', 'Disruption of ecological processes.', '**Influenced By (Stressors):**', 'Population Growth: In cities like Las Vegas.', 'Urban Expansion.', 'Infrastructure Development.', '**Influences (Stressors):**', 'Habitat Fragmentation.', '**Logic Description:** Urban sprawl and development, driven by population growth in cities like Las Vegas, are encroaching on Mojave Desert habitats.']
deserts_mojave_stressors["Urban Sprawl and Development"]["Impact on Area"] = 'Habitat loss and fragmentation.'
deserts_mojave_stressors["Urban Sprawl and Development"]["Impact on Biodiversity"] = 'Loss of habitat for desert species (e.g., desert tortoise).\nIncreased human-wildlife conflict.\nDisruption of ecological processes.\n**Influenced By (Stressors):**\nPopulation Growth: In cities like Las Vegas.\nUrban Expansion.\nInfrastructure Development.\n**Influences (Stressors):**\nHabitat Fragmentation.\n**Logic Description:** Urban sprawl and development, driven by population growth in cities like Las Vegas, are encroaching on Mojave Desert habitats.'
deserts_mojave_stressors["Urban Sprawl and Development"]["Influenced By"] = ['Population Growth: In cities like Las Vegas.', 'Urban Expansion.', 'Infrastructure Development.', '**Influences (Stressors):**', 'Habitat Fragmentation.', '**Logic Description:** Urban sprawl and development, driven by population growth in cities like Las Vegas, are encroaching on Mojave Desert habitats.']
deserts_mojave_stressors["Urban Sprawl and Development"]["Influences"] = ['Habitat Fragmentation.', '**Logic Description:** Urban sprawl and development, driven by population growth in cities like Las Vegas, are encroaching on Mojave Desert habitats.']
deserts_mojave_stressors["Urban Sprawl and Development"]["Logic Description"] = '---'
deserts_mojave_stressors["Urban Sprawl and Development"]["Impact Function"] = "impact_urban_sprawl_and_development_deserts_mojave"

# --- Water Extraction ---
deserts_mojave_stressors["Water Extraction"]["Metric"] = 'Volume of groundwater extracted (m³/year); changes in groundwater levels.'
deserts_mojave_stressors["Water Extraction"]["Data Sources"] = ['USGS water resource data.', 'State and local water agencies.', '**Impact on Area:** Depletion of groundwater resources; impacts on springs and seeps.', '**Impact on Biodiversity:**', 'Loss of water sources for wildlife.', 'Decline of vegetation dependent on groundwater.', '**Influenced By (Stressors):**', 'Urban Water Demand.', 'Agricultural Water Use (in some areas).', 'Mining.', '**Influences (Stressors):**', 'Water Availability.', '**Logic Description:** Groundwater extraction is a significant concern, impacting desert water sources.']
deserts_mojave_stressors["Water Extraction"]["Impact on Area"] = 'Depletion of groundwater resources; impacts on springs and seeps.'
deserts_mojave_stressors["Water Extraction"]["Impact on Biodiversity"] = 'Loss of water sources for wildlife.\nDecline of vegetation dependent on groundwater.\n**Influenced By (Stressors):**\nUrban Water Demand.\nAgricultural Water Use (in some areas).\nMining.\n**Influences (Stressors):**\nWater Availability.\n**Logic Description:** Groundwater extraction is a significant concern, impacting desert water sources.'
deserts_mojave_stressors["Water Extraction"]["Influenced By"] = ['Urban Water Demand.', 'Agricultural Water Use (in some areas).', 'Mining.', '**Influences (Stressors):**', 'Water Availability.', '**Logic Description:** Groundwater extraction is a significant concern, impacting desert water sources.']
deserts_mojave_stressors["Water Extraction"]["Influences"] = ['Water Availability.', '**Logic Description:** Groundwater extraction is a significant concern, impacting desert water sources.']
deserts_mojave_stressors["Water Extraction"]["Logic Description"] = '---'
deserts_mojave_stressors["Water Extraction"]["Impact Function"] = "impact_water_extraction_deserts_mojave"

# --- Off-Road Vehicle Use ---
deserts_mojave_stressors["Off-Road Vehicle Use"]["Metric"] = 'Area affected by off-road vehicle use; density of trails.'
deserts_mojave_stressors["Off-Road Vehicle Use"]["Data Sources"] = ['Bureau of Land Management (BLM) data.', 'Remote sensing.', 'Research studies.', '**Impact on Area:** Soil compaction; damage to vegetation; disturbance to wildlife.', '**Impact on Biodiversity:**', 'Crushing of plants and animals.', 'Soil erosion.', 'Spread of invasive species.', 'Disturbance to sensitive desert habitats (e.g., cryptobiotic soil crusts).', '**Influenced By (Stressors):**', 'Recreational Activities.', 'Lack of Enforcement of Regulations.', '**Influences (Stressors):**', 'Soil Erosion.', 'Vegetation Damage.', '**Logic Description:** Off-road vehicle use causes significant physical damage to desert soils and vegetation, impacting biodiversity.']
deserts_mojave_stressors["Off-Road Vehicle Use"]["Impact on Area"] = 'Soil compaction; damage to vegetation; disturbance to wildlife.'
deserts_mojave_stressors["Off-Road Vehicle Use"]["Impact on Biodiversity"] = 'Crushing of plants and animals.\nSoil erosion.\nSpread of invasive species.\nDisturbance to sensitive desert habitats (e.g., cryptobiotic soil crusts).\n**Influenced By (Stressors):**\nRecreational Activities.\nLack of Enforcement of Regulations.\n**Influences (Stressors):**\nSoil Erosion.\nVegetation Damage.\n**Logic Description:** Off-road vehicle use causes significant physical damage to desert soils and vegetation, impacting biodiversity.'
deserts_mojave_stressors["Off-Road Vehicle Use"]["Influenced By"] = ['Recreational Activities.', 'Lack of Enforcement of Regulations.', '**Influences (Stressors):**', 'Soil Erosion.', 'Vegetation Damage.', '**Logic Description:** Off-road vehicle use causes significant physical damage to desert soils and vegetation, impacting biodiversity.']
deserts_mojave_stressors["Off-Road Vehicle Use"]["Influences"] = ['Soil Erosion.', 'Vegetation Damage.', '**Logic Description:** Off-road vehicle use causes significant physical damage to desert soils and vegetation, impacting biodiversity.']
deserts_mojave_stressors["Off-Road Vehicle Use"]["Logic Description"] = '---'
deserts_mojave_stressors["Off-Road Vehicle Use"]["Impact Function"] = "impact_off_road_vehicle_use_deserts_mojave"

# --- Invasive Species ---
deserts_mojave_stressors["Invasive Species"]["Metric"] = 'Distribution and abundance of invasive plants (e.g., cheatgrass, red brome).'
deserts_mojave_stressors["Invasive Species"]["Data Sources"] = ['Vegetation surveys.', 'Research studies.', '**Impact on Area:** Changes in vegetation composition; increased fire frequency.', '**Impact on Biodiversity:**', 'Competition with native desert plants.', 'Altered fire regimes (invasive grasses can increase fire frequency and intensity).', '**Influenced By (Stressors):**', 'Disturbance: (e.g., off-road vehicle use, grazing).', 'Climate Change: May favor some invasives.', '**Influences (Stressors):**', 'Fire Regimes.', 'Native Plant Communities.', '**Logic Description:** Invasive plants, particularly annual grasses, are altering fire regimes and outcompeting native desert vegetation.']
deserts_mojave_stressors["Invasive Species"]["Impact on Area"] = 'Changes in vegetation composition; increased fire frequency.'
deserts_mojave_stressors["Invasive Species"]["Impact on Biodiversity"] = 'Competition with native desert plants.\nAltered fire regimes (invasive grasses can increase fire frequency and intensity).\n**Influenced By (Stressors):**\nDisturbance: (e.g., off-road vehicle use, grazing).\nClimate Change: May favor some invasives.\n**Influences (Stressors):**\nFire Regimes.\nNative Plant Communities.\n**Logic Description:** Invasive plants, particularly annual grasses, are altering fire regimes and outcompeting native desert vegetation.'
deserts_mojave_stressors["Invasive Species"]["Influenced By"] = ['Disturbance: (e.g., off-road vehicle use, grazing).', 'Climate Change: May favor some invasives.', '**Influences (Stressors):**', 'Fire Regimes.', 'Native Plant Communities.', '**Logic Description:** Invasive plants, particularly annual grasses, are altering fire regimes and outcompeting native desert vegetation.']
deserts_mojave_stressors["Invasive Species"]["Influences"] = ['Fire Regimes.', 'Native Plant Communities.', '**Logic Description:** Invasive plants, particularly annual grasses, are altering fire regimes and outcompeting native desert vegetation.']
deserts_mojave_stressors["Invasive Species"]["Logic Description"] = '---'
deserts_mojave_stressors["Invasive Species"]["Impact Function"] = "impact_invasive_species_deserts_mojave"

# --- Climate Change ---
deserts_mojave_stressors["Climate Change"]["Metric"] = 'Temperature increase; changes in precipitation.'
deserts_mojave_stressors["Climate Change"]["Data Sources"] = ['* Climate models.', '* Historical records', '**Impact on Area:** Increased aridity.', '**Impact on Biodiversity:**', '* Increased stress.', '* Species shifts.', '**Influenced By (Stressors):**', '* Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', '* Water availability', '**Logic Description:** Climate change impacts.']
deserts_mojave_stressors["Climate Change"]["Impact on Area"] = 'Increased aridity.'
deserts_mojave_stressors["Climate Change"]["Impact on Biodiversity"] = '* Increased stress.\n* Species shifts.\n**Influenced By (Stressors):**\n* Global Greenhouse Gas Emissions.\n**Influences (Stressors):**\n* Water availability\n**Logic Description:** Climate change impacts.'
deserts_mojave_stressors["Climate Change"]["Influenced By"] = ['* Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', '* Water availability', '**Logic Description:** Climate change impacts.']
deserts_mojave_stressors["Climate Change"]["Influences"] = ['* Water availability', '**Logic Description:** Climate change impacts.']
deserts_mojave_stressors["Climate Change"]["Logic Description"] = '---'
deserts_mojave_stressors["Climate Change"]["Impact Function"] = "impact_climate_change_deserts_mojave"

