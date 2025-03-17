from stressor_templates import *
import copy

aquatic_rivers_murray_darling_stressors = {
    "Water Extraction": copy.deepcopy(water_extraction_template),
    "Altered Flow Regimes": {},
    "Climate Change": copy.deepcopy(climate_change_template),
    "Invasive Species": copy.deepcopy(invasive_species_template),
    "Pollution": copy.deepcopy(pollution_template),
    "Salinity": {},
}

# --- Water Extraction ---
aquatic_rivers_murray_darling_stressors["Water Extraction"]["Metric"] = 'Volume of water extracted for irrigation and other uses (gigalitres/year); river flow rates; water levels in wetlands.'
aquatic_rivers_murray_darling_stressors["Water Extraction"]["Data Sources"] = ['Murray-Darling Basin Authority (MDBA).', 'Australian Bureau of Meteorology (BOM).', 'State government water agencies.', 'Research publications.', '**Impact on Area:** *Significant* reduction in river flows; drying of wetlands; reduced environmental flows.', '**Impact on Biodiversity:**', 'Decline of native fish populations.', 'Impacts on waterbirds (breeding and feeding).', 'Loss of wetland habitats.', 'Degradation of riverine ecosystems.', 'Increased salinity (in some areas).', '**Influenced By (Stressors):**', 'Irrigated Agriculture: The primary user of water in the basin.', 'Government Water Policies: Water allocation and management.', 'Climate Change: Reduced rainfall and increased evaporation.', '**Influences (Stressors):**', 'Water Availability (the dominant impact).', 'River Health.', 'Wetland Extent.', '**Logic Description:** Over-extraction of water, primarily for irrigated agriculture, is the *major* stressor on the Murray-Darling Basin, leading to drastically reduced river flows, the drying of wetlands, and widespread environmental degradation.']
aquatic_rivers_murray_darling_stressors["Water Extraction"]["Impact on Area"] = '*Significant* reduction in river flows; drying of wetlands; reduced environmental flows.'
aquatic_rivers_murray_darling_stressors["Water Extraction"]["Impact on Biodiversity"] = 'Decline of native fish populations.\nImpacts on waterbirds (breeding and feeding).\nLoss of wetland habitats.\nDegradation of riverine ecosystems.\nIncreased salinity (in some areas).\n**Influenced By (Stressors):**\nIrrigated Agriculture: The primary user of water in the basin.\nGovernment Water Policies: Water allocation and management.\nClimate Change: Reduced rainfall and increased evaporation.\n**Influences (Stressors):**\nWater Availability (the dominant impact).\nRiver Health.\nWetland Extent.\n**Logic Description:** Over-extraction of water, primarily for irrigated agriculture, is the *major* stressor on the Murray-Darling Basin, leading to drastically reduced river flows, the drying of wetlands, and widespread environmental degradation.'
aquatic_rivers_murray_darling_stressors["Water Extraction"]["Influenced By"] = ['Irrigated Agriculture: The primary user of water in the basin.', 'Government Water Policies: Water allocation and management.', 'Climate Change: Reduced rainfall and increased evaporation.', '**Influences (Stressors):**', 'Water Availability (the dominant impact).', 'River Health.', 'Wetland Extent.', '**Logic Description:** Over-extraction of water, primarily for irrigated agriculture, is the *major* stressor on the Murray-Darling Basin, leading to drastically reduced river flows, the drying of wetlands, and widespread environmental degradation.']
aquatic_rivers_murray_darling_stressors["Water Extraction"]["Influences"] = ['Water Availability (the dominant impact).', 'River Health.', 'Wetland Extent.', '**Logic Description:** Over-extraction of water, primarily for irrigated agriculture, is the *major* stressor on the Murray-Darling Basin, leading to drastically reduced river flows, the drying of wetlands, and widespread environmental degradation.']
aquatic_rivers_murray_darling_stressors["Water Extraction"]["Logic Description"] = '---'

# --- Altered Flow Regimes ---
aquatic_rivers_murray_darling_stressors["Altered Flow Regimes"]["Metric"] = 'Changes in the timing, duration, and magnitude of flow events; reduced frequency of floods.'
aquatic_rivers_murray_darling_stressors["Altered Flow Regimes"]["Data Sources"] = ['MDBA.', 'BOM.', 'Research publications.', '**Impact on Area:** Changes in river and wetland habitats.', '**Impact on Biodiversity:**', 'Impacts on fish spawning and migration (many native fish need floods to trigger spawning).', 'Loss of floodplain wetlands.', 'Changes in vegetation communities.', '**Influenced By (Stressors):**', 'Dams and Weirs: Regulate flow and reduce flood peaks.', 'Water Extraction: Reduces overall flow.', '**Influences (Stressors):**', 'Habitat Connectivity.', 'Fish Breeding.', 'Wetland Ecosystems.', '**Logic Description:** Dams, weirs, and water extraction have altered the natural flow regime of the rivers, reducing the frequency and magnitude of floods, which are essential for many ecological processes.']
aquatic_rivers_murray_darling_stressors["Altered Flow Regimes"]["Impact on Area"] = 'Changes in river and wetland habitats.'
aquatic_rivers_murray_darling_stressors["Altered Flow Regimes"]["Impact on Biodiversity"] = 'Impacts on fish spawning and migration (many native fish need floods to trigger spawning).\nLoss of floodplain wetlands.\nChanges in vegetation communities.\n**Influenced By (Stressors):**\nDams and Weirs: Regulate flow and reduce flood peaks.\nWater Extraction: Reduces overall flow.\n**Influences (Stressors):**\nHabitat Connectivity.\nFish Breeding.\nWetland Ecosystems.\n**Logic Description:** Dams, weirs, and water extraction have altered the natural flow regime of the rivers, reducing the frequency and magnitude of floods, which are essential for many ecological processes.'
aquatic_rivers_murray_darling_stressors["Altered Flow Regimes"]["Influenced By"] = ['Dams and Weirs: Regulate flow and reduce flood peaks.', 'Water Extraction: Reduces overall flow.', '**Influences (Stressors):**', 'Habitat Connectivity.', 'Fish Breeding.', 'Wetland Ecosystems.', '**Logic Description:** Dams, weirs, and water extraction have altered the natural flow regime of the rivers, reducing the frequency and magnitude of floods, which are essential for many ecological processes.']
aquatic_rivers_murray_darling_stressors["Altered Flow Regimes"]["Influences"] = ['Habitat Connectivity.', 'Fish Breeding.', 'Wetland Ecosystems.', '**Logic Description:** Dams, weirs, and water extraction have altered the natural flow regime of the rivers, reducing the frequency and magnitude of floods, which are essential for many ecological processes.']
aquatic_rivers_murray_darling_stressors["Altered Flow Regimes"]["Logic Description"] = '---'

# --- Climate Change ---
aquatic_rivers_murray_darling_stressors["Climate Change"]["Metric"] = 'Temperature increase; changes to precipiation, increased droughts'
aquatic_rivers_murray_darling_stressors["Climate Change"]["Data Sources"] = ['* Climate models', '* Historical data', '**Impact on Area:** Reduced water availability', '**Impact on Biodiversity:**', '* Increased stress', '* Species shifts', '**Influenced By (Stressors):**', '* Global GHG', '**Influences (Stressors):**', '* Water availability', '* Fire Regimes', '**Logic Description:** Climate change exacerbates water scarcity and increases temperatures.']
aquatic_rivers_murray_darling_stressors["Climate Change"]["Impact on Area"] = 'Reduced water availability'
aquatic_rivers_murray_darling_stressors["Climate Change"]["Impact on Biodiversity"] = '* Increased stress\n* Species shifts\n**Influenced By (Stressors):**\n* Global GHG\n**Influences (Stressors):**\n* Water availability\n* Fire Regimes\n**Logic Description:** Climate change exacerbates water scarcity and increases temperatures.'
aquatic_rivers_murray_darling_stressors["Climate Change"]["Influenced By"] = ['* Global GHG', '**Influences (Stressors):**', '* Water availability', '* Fire Regimes', '**Logic Description:** Climate change exacerbates water scarcity and increases temperatures.']
aquatic_rivers_murray_darling_stressors["Climate Change"]["Influences"] = ['* Water availability', '* Fire Regimes', '**Logic Description:** Climate change exacerbates water scarcity and increases temperatures.']
aquatic_rivers_murray_darling_stressors["Climate Change"]["Logic Description"] = '---'

# --- Invasive Species ---
aquatic_rivers_murray_darling_stressors["Invasive Species"]["Metric"] = 'Distribution and abundance of key invasive species (e.g., common carp, *Salvinia molesta*).'
aquatic_rivers_murray_darling_stressors["Invasive Species"]["Impact on Area"] = 'Alters aquatic habitats'
aquatic_rivers_murray_darling_stressors["Invasive Species"]["Logic Description"] = '---'

# --- Pollution ---
aquatic_rivers_murray_darling_stressors["Pollution"]["Data Sources"] = ['* Water Quality Monitoring', '**Impact on Area:** Degraded water quality', '**Impact on Biodiversity:**', '* Impacts aquatic species, algal blooms.', '**Influenced By:**', '* Agriculture', '* Urban runoff', '**Influences (Stressors):**', '* Water Quality', '**Logic Description**: Agricultural runoff and other pollution degrades water quality.']
aquatic_rivers_murray_darling_stressors["Pollution"]["Impact on Area"] = 'Degraded water quality'
aquatic_rivers_murray_darling_stressors["Pollution"]["Impact on Biodiversity"] = '* Impacts aquatic species, algal blooms.\n**Influenced By:**\n* Agriculture\n* Urban runoff\n**Influences (Stressors):**\n* Water Quality\n**Logic Description**: Agricultural runoff and other pollution degrades water quality.'
aquatic_rivers_murray_darling_stressors["Pollution"]["Influences"] = ['* Water Quality', '**Logic Description**: Agricultural runoff and other pollution degrades water quality.']

# --- Salinity ---
aquatic_rivers_murray_darling_stressors["Salinity"]["Data Sources"] = ['* Monitoring programs', '**Impact on Area:** Degraded soil and water', '**Impact on Biodiversity:**', '* Impacts salt-sensitive species', '**Influenced By (Stressors):**', '* Irrigation', '* Land Clearing', '* Reduced Flows', '**Influences (Stressors):**', '* Water quality', '* Soil health.', '**Logic Description**: Dryland and irrigation-induced salinity are major problems.']
aquatic_rivers_murray_darling_stressors["Salinity"]["Impact on Area"] = 'Degraded soil and water'
aquatic_rivers_murray_darling_stressors["Salinity"]["Impact on Biodiversity"] = '* Impacts salt-sensitive species\n**Influenced By (Stressors):**\n* Irrigation\n* Land Clearing\n* Reduced Flows\n**Influences (Stressors):**\n* Water quality\n* Soil health.\n**Logic Description**: Dryland and irrigation-induced salinity are major problems.'
aquatic_rivers_murray_darling_stressors["Salinity"]["Influenced By"] = ['* Irrigation', '* Land Clearing', '* Reduced Flows', '**Influences (Stressors):**', '* Water quality', '* Soil health.', '**Logic Description**: Dryland and irrigation-induced salinity are major problems.']
aquatic_rivers_murray_darling_stressors["Salinity"]["Influences"] = ['* Water quality', '* Soil health.', '**Logic Description**: Dryland and irrigation-induced salinity are major problems.']

