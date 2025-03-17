from stressor_templates import *
import copy

aquatic_seagrass_florida_bay_stressors = {
    "Water Quality Degradation": {},
    "Physical Damage": {},
    "Climate Change": copy.deepcopy(climate_change_template),
}

# --- Water Quality Degradation ---
aquatic_seagrass_florida_bay_stressors["Water Quality Degradation"]["Metric"] = 'Water clarity (turbidity); nutrient concentrations (nitrogen, phosphorus); salinity; chlorophyll *a* concentrations.'
aquatic_seagrass_florida_bay_stressors["Water Quality Degradation"]["Data Sources"] = ['South Florida Water Management District (SFWMD) monitoring data.', 'Florida Department of Environmental Protection (FDEP) data.', 'EPA data.', 'Research studies.', '**Impact on Area:** *Widespread* seagrass loss due to reduced light penetration and algal blooms.', '**Impact on Biodiversity:**', 'Massive seagrass die-offs (have occurred repeatedly in Florida Bay).', 'Loss of habitat for fish, invertebrates, and endangered species like manatees.', 'Altered food webs.', '**Influenced By (Stressors):**', 'Agricultural Runoff: From the Everglades Agricultural Area and other agricultural regions.', 'Urban Runoff: From South Florida.', 'Altered Hydrology: Changes in freshwater inflow from the Everglades.', '**Influences (Stressors):**', 'Light Availability (the critical factor).', 'Algal Blooms.', 'Seagrass Die-offs.', '**Logic Description:** Water quality degradation, primarily due to nutrient pollution and altered freshwater inflow from the Everglades, is the *major* driver of seagrass loss in Florida Bay. This has led to large-scale seagrass die-offs and ecosystem shifts.']
aquatic_seagrass_florida_bay_stressors["Water Quality Degradation"]["Impact on Area"] = '*Widespread* seagrass loss due to reduced light penetration and algal blooms.'
aquatic_seagrass_florida_bay_stressors["Water Quality Degradation"]["Impact on Biodiversity"] = 'Massive seagrass die-offs (have occurred repeatedly in Florida Bay).\nLoss of habitat for fish, invertebrates, and endangered species like manatees.\nAltered food webs.\n**Influenced By (Stressors):**\nAgricultural Runoff: From the Everglades Agricultural Area and other agricultural regions.\nUrban Runoff: From South Florida.\nAltered Hydrology: Changes in freshwater inflow from the Everglades.\n**Influences (Stressors):**\nLight Availability (the critical factor).\nAlgal Blooms.\nSeagrass Die-offs.\n**Logic Description:** Water quality degradation, primarily due to nutrient pollution and altered freshwater inflow from the Everglades, is the *major* driver of seagrass loss in Florida Bay. This has led to large-scale seagrass die-offs and ecosystem shifts.'
aquatic_seagrass_florida_bay_stressors["Water Quality Degradation"]["Influenced By"] = ['Agricultural Runoff: From the Everglades Agricultural Area and other agricultural regions.', 'Urban Runoff: From South Florida.', 'Altered Hydrology: Changes in freshwater inflow from the Everglades.', '**Influences (Stressors):**', 'Light Availability (the critical factor).', 'Algal Blooms.', 'Seagrass Die-offs.', '**Logic Description:** Water quality degradation, primarily due to nutrient pollution and altered freshwater inflow from the Everglades, is the *major* driver of seagrass loss in Florida Bay. This has led to large-scale seagrass die-offs and ecosystem shifts.']
aquatic_seagrass_florida_bay_stressors["Water Quality Degradation"]["Influences"] = ['Light Availability (the critical factor).', 'Algal Blooms.', 'Seagrass Die-offs.', '**Logic Description:** Water quality degradation, primarily due to nutrient pollution and altered freshwater inflow from the Everglades, is the *major* driver of seagrass loss in Florida Bay. This has led to large-scale seagrass die-offs and ecosystem shifts.']
aquatic_seagrass_florida_bay_stressors["Water Quality Degradation"]["Logic Description"] = '---'
aquatic_seagrass_florida_bay_stressors["Water Quality Degradation"]["Impact Function"] = "impact_water_quality_degradation_aquatic_seagrass_florida_bay"

# --- Physical Damage ---
aquatic_seagrass_florida_bay_stressors["Physical Damage"]["Metric"] = 'Area of seagrass scarred by boat propellers; number of boating accidents in seagrass areas.'
aquatic_seagrass_florida_bay_stressors["Physical Damage"]["Data Sources"] = ['Aerial surveys.', 'Florida Fish and Wildlife Conservation Commission (FWC) data.', '**Impact on Area:** Direct damage to seagrass; fragmentation.', '**Impact on Biodiversity:**', 'Habitat loss.', 'Slow recovery.', '**Influenced By (Stressors):**', 'High Boating Traffic: In shallow waters.', 'Lack of Boater Education.', '**Influences (Stressors):**', 'Habitat Loss (localized).', '**Logic Description:** Boat propeller scarring is a significant problem in Florida Bay due to the shallow waters and extensive seagrass beds.']
aquatic_seagrass_florida_bay_stressors["Physical Damage"]["Impact on Area"] = 'Direct damage to seagrass; fragmentation.'
aquatic_seagrass_florida_bay_stressors["Physical Damage"]["Impact on Biodiversity"] = 'Habitat loss.\nSlow recovery.\n**Influenced By (Stressors):**\nHigh Boating Traffic: In shallow waters.\nLack of Boater Education.\n**Influences (Stressors):**\nHabitat Loss (localized).\n**Logic Description:** Boat propeller scarring is a significant problem in Florida Bay due to the shallow waters and extensive seagrass beds.'
aquatic_seagrass_florida_bay_stressors["Physical Damage"]["Influenced By"] = ['High Boating Traffic: In shallow waters.', 'Lack of Boater Education.', '**Influences (Stressors):**', 'Habitat Loss (localized).', '**Logic Description:** Boat propeller scarring is a significant problem in Florida Bay due to the shallow waters and extensive seagrass beds.']
aquatic_seagrass_florida_bay_stressors["Physical Damage"]["Influences"] = ['Habitat Loss (localized).', '**Logic Description:** Boat propeller scarring is a significant problem in Florida Bay due to the shallow waters and extensive seagrass beds.']
aquatic_seagrass_florida_bay_stressors["Physical Damage"]["Logic Description"] = '---'
aquatic_seagrass_florida_bay_stressors["Physical Damage"]["Impact Function"] = "impact_physical_damage_aquatic_seagrass_florida_bay"

# --- Climate Change ---
aquatic_seagrass_florida_bay_stressors["Climate Change"]["Metric"] = 'Sea surface temperature, ocean acidification, sea level, storm intensity.'
aquatic_seagrass_florida_bay_stressors["Climate Change"]["Data Sources"] = ['* Climate models', '* Historical data.', '**Impact on Area:** Die-offs, distribution changes.', '**Impact on Biodiversity:**', '* Species stress.', '**Influenced By (Stressors):**', '* Global GHG emissions.', '**Influences (Stressors):**', '* Sea Level Rise', '* Ocean acidification.', '**Logic Description:**  Climate change stressors impact.']
aquatic_seagrass_florida_bay_stressors["Climate Change"]["Impact on Area"] = 'Die-offs, distribution changes.'
aquatic_seagrass_florida_bay_stressors["Climate Change"]["Impact on Biodiversity"] = '* Species stress.\n**Influenced By (Stressors):**\n* Global GHG emissions.\n**Influences (Stressors):**\n* Sea Level Rise\n* Ocean acidification.\n**Logic Description:**  Climate change stressors impact.'
aquatic_seagrass_florida_bay_stressors["Climate Change"]["Influenced By"] = ['* Global GHG emissions.', '**Influences (Stressors):**', '* Sea Level Rise', '* Ocean acidification.', '**Logic Description:**  Climate change stressors impact.']
aquatic_seagrass_florida_bay_stressors["Climate Change"]["Influences"] = ['* Sea Level Rise', '* Ocean acidification.', '**Logic Description:**  Climate change stressors impact.']
aquatic_seagrass_florida_bay_stressors["Climate Change"]["Logic Description"] = '---'
aquatic_seagrass_florida_bay_stressors["Climate Change"]["Impact Function"] = "impact_climate_change_aquatic_seagrass_florida_bay"

