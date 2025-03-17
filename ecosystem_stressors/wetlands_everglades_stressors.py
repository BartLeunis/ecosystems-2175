from stressor_templates import *
import copy

wetlands_everglades_stressors = {
    "Altered Hydrology": copy.deepcopy(altered_hydrology_template),
    "Nutrient Pollution": copy.deepcopy(pollution_template),
    "Invasive Species": copy.deepcopy(invasive_species_template),
    "Climate Change": copy.deepcopy(climate_change_template),
    "Water Management Practices": {},
    "Agricultural Runoff": {},
    "Urban Development": {},
    "Sea Level": {},
    "Saltwater Intrusion": {},
    "Introduction": {},
    "Disturbance": {},
    "Native Wildlife Populations": {},
    "Urban Runoff": {},
    "Habitat Availability": {},
    "Vegetation Changes": {},
    "Water Quality": {},
}

# --- Altered Hydrology ---
wetlands_everglades_stressors["Altered Hydrology"]["Metric"] = 'Water levels (depth, duration of flooding); water flow rates; water quality (nutrient concentrations, salinity).'
wetlands_everglades_stressors["Altered Hydrology"]["Data Sources"] = ['South Florida Water Management District (SFWMD) data.', 'US Geological Survey (USGS) data.', 'Everglades National Park monitoring data.', '**Impact on Area:** Changes in the extent of different wetland types (e.g., sawgrass marshes, sloughs, mangroves); shifts in vegetation communities.', '**Impact on Biodiversity:**', 'Impacts on wading bird populations (nesting success).', 'Changes in fish and invertebrate communities.', 'Altered alligator populations and distribution.', 'Spread of invasive species (favored by altered conditions).', 'Changes in plant communities', '**Influenced By (Stressors):**', '* Everglades - Water Management Practices', '* Everglades - Agricultural Runoff', '* Everglades - Urban Development', '* Everglades - Climate Change', '**Influences (Stressors):**', '*  Everglades - Water Quality', '*  Everglades - Habitat Availability', '*  Everglades - Invasive Species Spread', '**Logic Description:** The Everglades is a highly managed hydrological system. Dams, canals, and levees have drastically altered the natural flow, impacting wetland habitats and species.']
wetlands_everglades_stressors["Altered Hydrology"]["Impact on Area"] = 'Changes in the extent of different wetland types (e.g., sawgrass marshes, sloughs, mangroves); shifts in vegetation communities.'
wetlands_everglades_stressors["Altered Hydrology"]["Impact on Biodiversity"] = 'Impacts on wading bird populations (nesting success).\nChanges in fish and invertebrate communities.\nAltered alligator populations and distribution.\nSpread of invasive species (favored by altered conditions).\nChanges in plant communities\n**Influenced By (Stressors):**\n* Everglades - Water Management Practices\n* Everglades - Agricultural Runoff\n* Everglades - Urban Development\n* Everglades - Climate Change\n**Influences (Stressors):**\n*  Everglades - Water Quality\n*  Everglades - Habitat Availability\n*  Everglades - Invasive Species Spread\n**Logic Description:** The Everglades is a highly managed hydrological system. Dams, canals, and levees have drastically altered the natural flow, impacting wetland habitats and species.'
wetlands_everglades_stressors["Altered Hydrology"]["Influenced By"] = ['* Everglades - Water Management Practices', '* Everglades - Agricultural Runoff', '* Everglades - Urban Development', '* Everglades - Climate Change', '**Influences (Stressors):**', '*  Everglades - Water Quality', '*  Everglades - Habitat Availability', '*  Everglades - Invasive Species Spread', '**Logic Description:** The Everglades is a highly managed hydrological system. Dams, canals, and levees have drastically altered the natural flow, impacting wetland habitats and species.']
wetlands_everglades_stressors["Altered Hydrology"]["Influences"] = ['*  Everglades - Water Quality', '*  Everglades - Habitat Availability', '*  Everglades - Invasive Species Spread', '**Logic Description:** The Everglades is a highly managed hydrological system. Dams, canals, and levees have drastically altered the natural flow, impacting wetland habitats and species.']
wetlands_everglades_stressors["Altered Hydrology"]["Logic Description"] = '---'

# --- Nutrient Pollution ---
wetlands_everglades_stressors["Nutrient Pollution"]["Metric"] = 'Concentrations of phosphorus and nitrogen in water and soil (ppm, µg/L).'
wetlands_everglades_stressors["Nutrient Pollution"]["Data Sources"] = ['SFWMD water quality monitoring data.', 'USGS data.', 'Research studies.', '**Impact on Area:** Changes in vegetation communities (e.g., expansion of cattails).', '**Impact on Biodiversity:**', 'Altered plant communities, leading to habitat loss.', 'Eutrophication.', 'Impacts on aquatic food webs.', '**Influenced By (Stressors):**', '*  Everglades - Agricultural Runoff', '* Everglades - Urban Runoff', '**Influences (Stressors):**', '*  Everglades - Water Quality', '*  Everglades - Vegetation Changes', '**Logic Description:** Nutrient pollution, primarily from agriculture, enriches the ecosystem, leading to vegetation changes.']
wetlands_everglades_stressors["Nutrient Pollution"]["Impact on Area"] = 'Changes in vegetation communities (e.g., expansion of cattails).'
wetlands_everglades_stressors["Nutrient Pollution"]["Impact on Biodiversity"] = 'Altered plant communities, leading to habitat loss.\nEutrophication.\nImpacts on aquatic food webs.\n**Influenced By (Stressors):**\n*  Everglades - Agricultural Runoff\n* Everglades - Urban Runoff\n**Influences (Stressors):**\n*  Everglades - Water Quality\n*  Everglades - Vegetation Changes\n**Logic Description:** Nutrient pollution, primarily from agriculture, enriches the ecosystem, leading to vegetation changes.'
wetlands_everglades_stressors["Nutrient Pollution"]["Influenced By"] = ['*  Everglades - Agricultural Runoff', '* Everglades - Urban Runoff', '**Influences (Stressors):**', '*  Everglades - Water Quality', '*  Everglades - Vegetation Changes', '**Logic Description:** Nutrient pollution, primarily from agriculture, enriches the ecosystem, leading to vegetation changes.']
wetlands_everglades_stressors["Nutrient Pollution"]["Influences"] = ['*  Everglades - Water Quality', '*  Everglades - Vegetation Changes', '**Logic Description:** Nutrient pollution, primarily from agriculture, enriches the ecosystem, leading to vegetation changes.']
wetlands_everglades_stressors["Nutrient Pollution"]["Logic Description"] = '---'

# --- Invasive Species ---
wetlands_everglades_stressors["Invasive Species"]["Metric"] = 'Abundance and distribution of key invasive species (e.g., Burmese python, Melaleuca tree, Brazilian pepper).'
wetlands_everglades_stressors["Invasive Species"]["Data Sources"] = ['Everglades National Park monitoring data.', 'USGS and FWS data.', 'Research studies.', '**Impact on Area:** Changes in vegetation communities; altered habitat structure.', '**Impact on Biodiversity:**', 'Predation on native species (e.g., Burmese pythons).', 'Competition with native species (e.g., Melaleuca trees).', 'Altered ecosystem processes (e.g., fire regimes).', '**Influenced By (Stressors):**', '* Everglades - Introduction', '* Everglades - Altered Hydrology', '* Everglades - Disturbance', '**Influences (Stressors):**', '*  Everglades - Native Wildlife Populations', '**Logic Description:** Invasive species pose a major threat, preying on natives, outcompeting plants, and altering processes.']
wetlands_everglades_stressors["Invasive Species"]["Impact on Area"] = 'Changes in vegetation communities; altered habitat structure.'
wetlands_everglades_stressors["Invasive Species"]["Impact on Biodiversity"] = 'Predation on native species (e.g., Burmese pythons).\nCompetition with native species (e.g., Melaleuca trees).\nAltered ecosystem processes (e.g., fire regimes).\n**Influenced By (Stressors):**\n* Everglades - Introduction\n* Everglades - Altered Hydrology\n* Everglades - Disturbance\n**Influences (Stressors):**\n*  Everglades - Native Wildlife Populations\n**Logic Description:** Invasive species pose a major threat, preying on natives, outcompeting plants, and altering processes.'
wetlands_everglades_stressors["Invasive Species"]["Influenced By"] = ['* Everglades - Introduction', '* Everglades - Altered Hydrology', '* Everglades - Disturbance', '**Influences (Stressors):**', '*  Everglades - Native Wildlife Populations', '**Logic Description:** Invasive species pose a major threat, preying on natives, outcompeting plants, and altering processes.']
wetlands_everglades_stressors["Invasive Species"]["Influences"] = ['*  Everglades - Native Wildlife Populations', '**Logic Description:** Invasive species pose a major threat, preying on natives, outcompeting plants, and altering processes.']
wetlands_everglades_stressors["Invasive Species"]["Logic Description"] = '---'

# --- Climate Change ---
wetlands_everglades_stressors["Climate Change"]["Metric"] = 'Temperature increase; sea level rise; changes in precipitation'
wetlands_everglades_stressors["Climate Change"]["Data Sources"] = ['* Climate Models', '* Historical Records.', '**Impact on Area:**', '* Coastal inundation due to sea level rise.', '* Saltwater intrusion into freshwater wetlands.', '**Impact on Biodiversity:**', '* Species shifts', '* Increased Stress.', '* Increased vulnerability to storms.', '**Influenced By (Stressors):**', '* Global GHG emissions', '*  Everglades - Sea Level', '**Influences (Stressors):**', '*  Everglades - Hydrology', '*  Everglades - Saltwater Intrusion', '**Logic Description:** Sea level rise poses a threat to the low-lying Everglades, causing inundation and saltwater intrusion.']
wetlands_everglades_stressors["Climate Change"]["Impact on Area"] = ''
wetlands_everglades_stressors["Climate Change"]["Impact on Biodiversity"] = '* Species shifts\n* Increased Stress.\n* Increased vulnerability to storms.\n**Influenced By (Stressors):**\n* Global GHG emissions\n*  Everglades - Sea Level\n**Influences (Stressors):**\n*  Everglades - Hydrology\n*  Everglades - Saltwater Intrusion\n**Logic Description:** Sea level rise poses a threat to the low-lying Everglades, causing inundation and saltwater intrusion.'
wetlands_everglades_stressors["Climate Change"]["Influenced By"] = ['* Global GHG emissions', '*  Everglades - Sea Level', '**Influences (Stressors):**', '*  Everglades - Hydrology', '*  Everglades - Saltwater Intrusion', '**Logic Description:** Sea level rise poses a threat to the low-lying Everglades, causing inundation and saltwater intrusion.']
wetlands_everglades_stressors["Climate Change"]["Influences"] = ['*  Everglades - Hydrology', '*  Everglades - Saltwater Intrusion', '**Logic Description:** Sea level rise poses a threat to the low-lying Everglades, causing inundation and saltwater intrusion.']
wetlands_everglades_stressors["Climate Change"]["Logic Description"] = '---'

# --- Water Management Practices ---
wetlands_everglades_stressors["Water Management Practices"]["Metric"] = 'Water flow rates, water levels.'
wetlands_everglades_stressors["Water Management Practices"]["Data Sources"] = ['* SFWMD data.', '* USGS data', '**Impact on Area:** Altered hydrology.', '**Impact on Biodiversity:**', '* Impacts on various species', '**Influenced By (Stressors):**', '* Urban and agricultural water demand', '**Influences (Stressors):**', '* Everglades - Altered Hydrology', '**Logic Description:** Management practices drastically alter the natural hydrology.']
wetlands_everglades_stressors["Water Management Practices"]["Impact on Area"] = 'Altered hydrology.'
wetlands_everglades_stressors["Water Management Practices"]["Impact on Biodiversity"] = '* Impacts on various species\n**Influenced By (Stressors):**\n* Urban and agricultural water demand\n**Influences (Stressors):**\n* Everglades - Altered Hydrology\n**Logic Description:** Management practices drastically alter the natural hydrology.'
wetlands_everglades_stressors["Water Management Practices"]["Influenced By"] = ['* Urban and agricultural water demand', '**Influences (Stressors):**', '* Everglades - Altered Hydrology', '**Logic Description:** Management practices drastically alter the natural hydrology.']
wetlands_everglades_stressors["Water Management Practices"]["Influences"] = ['* Everglades - Altered Hydrology', '**Logic Description:** Management practices drastically alter the natural hydrology.']
wetlands_everglades_stressors["Water Management Practices"]["Logic Description"] = '---'

# --- Agricultural Runoff ---
wetlands_everglades_stressors["Agricultural Runoff"]["Metric"] = 'Nutrient concentrations.'
wetlands_everglades_stressors["Agricultural Runoff"]["Data Sources"] = ['* Water quality monitoring data.', '**Impact on Area:** Water quality degradation.', '**Impact on Biodiversity:**', 'Eutrophication.', 'Altered plant communities', '**Influenced By (Stressors):**', '* Agricultural practices.', '**Influences (Stressors):**', '*  Everglades - Nutrient Pollution', '**Logic Description**: Runoff carries pollutants into the Everglades.']
wetlands_everglades_stressors["Agricultural Runoff"]["Impact on Area"] = 'Water quality degradation.'
wetlands_everglades_stressors["Agricultural Runoff"]["Impact on Biodiversity"] = 'Eutrophication.\nAltered plant communities\n**Influenced By (Stressors):**\n* Agricultural practices.\n**Influences (Stressors):**\n*  Everglades - Nutrient Pollution\n**Logic Description**: Runoff carries pollutants into the Everglades.'
wetlands_everglades_stressors["Agricultural Runoff"]["Influenced By"] = ['* Agricultural practices.', '**Influences (Stressors):**', '*  Everglades - Nutrient Pollution', '**Logic Description**: Runoff carries pollutants into the Everglades.']
wetlands_everglades_stressors["Agricultural Runoff"]["Influences"] = ['*  Everglades - Nutrient Pollution', '**Logic Description**: Runoff carries pollutants into the Everglades.']

# --- Urban Development ---
wetlands_everglades_stressors["Urban Development"]["Data Sources"] = ['* Land Cover data', '**Impact on Area:** Habitat loss, altered hydrology', '**Impact on Biodiversity**:', '* Species loss, changes in water dynamics', '**Influenced By (Stressors):**', '* Population growth', '* Economic development', '**Influences (Stressors):**', '*  Everglades - Altered Hydrology', '**Logic Description:** Urban expansion impacts wetlands.']
wetlands_everglades_stressors["Urban Development"]["Impact on Area"] = 'Habitat loss, altered hydrology'
wetlands_everglades_stressors["Urban Development"]["Influenced By"] = ['* Population growth', '* Economic development', '**Influences (Stressors):**', '*  Everglades - Altered Hydrology', '**Logic Description:** Urban expansion impacts wetlands.']
wetlands_everglades_stressors["Urban Development"]["Influences"] = ['*  Everglades - Altered Hydrology', '**Logic Description:** Urban expansion impacts wetlands.']
wetlands_everglades_stressors["Urban Development"]["Logic Description"] = '---'

# --- Sea Level ---
wetlands_everglades_stressors["Sea Level"]["Metric"] = 'Sea level height (relative to land).'
wetlands_everglades_stressors["Sea Level"]["Data Sources"] = ['Tide gauges.', 'Satellite altimetry.', '**Impact on Area:** Coastal inundation.', '**Impact on Biodiversity:**', '* Habitat Loss', '**Influenced By (Stressors):**', '* Everglades - Climate Change', '**Influences (Stressors):**', '* Everglades - Climate Change', '**Logic Description**: Rising sea levels inundate low-lying areas.']
wetlands_everglades_stressors["Sea Level"]["Impact on Area"] = 'Coastal inundation.'
wetlands_everglades_stressors["Sea Level"]["Impact on Biodiversity"] = '* Habitat Loss\n**Influenced By (Stressors):**\n* Everglades - Climate Change\n**Influences (Stressors):**\n* Everglades - Climate Change\n**Logic Description**: Rising sea levels inundate low-lying areas.'
wetlands_everglades_stressors["Sea Level"]["Influenced By"] = ['* Everglades - Climate Change', '**Influences (Stressors):**', '* Everglades - Climate Change', '**Logic Description**: Rising sea levels inundate low-lying areas.']
wetlands_everglades_stressors["Sea Level"]["Influences"] = ['* Everglades - Climate Change', '**Logic Description**: Rising sea levels inundate low-lying areas.']

# --- Saltwater Intrusion ---
wetlands_everglades_stressors["Saltwater Intrusion"]["Metric"] = 'Salinity levels in groundwater and surface water.'
wetlands_everglades_stressors["Saltwater Intrusion"]["Data Sources"] = ['Water quality monitoring data.', 'USGS data.', '**Impact on Area:** Changes in water and soil chemistry', '**Impact on Biodiversity:**', '* Impacts freshwater species', '**Influenced By (Stressors):**', 'Everglades - Sea Level', 'Everglades - Climate Change', 'Everglades - Altered Hydrology', '**Influences (Stressors):**', '* Many, varies', '**Logic Description:** Saltwater contaminates freshwater resources']
wetlands_everglades_stressors["Saltwater Intrusion"]["Impact on Area"] = 'Changes in water and soil chemistry'
wetlands_everglades_stressors["Saltwater Intrusion"]["Impact on Biodiversity"] = '* Impacts freshwater species\n**Influenced By (Stressors):**\nEverglades - Sea Level\nEverglades - Climate Change\nEverglades - Altered Hydrology\n**Influences (Stressors):**\n* Many, varies\n**Logic Description:** Saltwater contaminates freshwater resources'
wetlands_everglades_stressors["Saltwater Intrusion"]["Influenced By"] = ['Everglades - Sea Level', 'Everglades - Climate Change', 'Everglades - Altered Hydrology', '**Influences (Stressors):**', '* Many, varies', '**Logic Description:** Saltwater contaminates freshwater resources']
wetlands_everglades_stressors["Saltwater Intrusion"]["Influences"] = ['* Many, varies', '**Logic Description:** Saltwater contaminates freshwater resources']
wetlands_everglades_stressors["Saltwater Intrusion"]["Logic Description"] = '---'

# --- Introduction ---
wetlands_everglades_stressors["Introduction"]["Metric"] = 'Number of introduced species.'
wetlands_everglades_stressors["Introduction"]["Impact on Biodiversity"] = '*  Competition, predation, etc.\n**Influenced By (Stressors):**\n* Human Activities.\n**Influences (Stressors):**\n* Everglades - Invasive Species\n**Logic Description**: Intentional and unintentional species introductions.'
wetlands_everglades_stressors["Introduction"]["Influenced By"] = ['* Human Activities.', '**Influences (Stressors):**', '* Everglades - Invasive Species', '**Logic Description**: Intentional and unintentional species introductions.']
wetlands_everglades_stressors["Introduction"]["Influences"] = ['* Everglades - Invasive Species', '**Logic Description**: Intentional and unintentional species introductions.']

# --- Disturbance ---
wetlands_everglades_stressors["Disturbance"]["Metric"] = 'Area and frequency of disturbance events.'
wetlands_everglades_stressors["Disturbance"]["Data Sources"] = ['Field observations.', 'Remote sensing.', '**Impact on Area**: Site Specific', '**Impact on Biodiversity:**', '* Variable', '**Influenced By (Stressors):**', '* Many', '**Influences (Stressors):**', '* Everglades - Invasive Species', '**Logic Description:** General category representing physical disturbances.']
wetlands_everglades_stressors["Disturbance"]["Impact on Biodiversity"] = '* Variable\n**Influenced By (Stressors):**\n* Many\n**Influences (Stressors):**\n* Everglades - Invasive Species\n**Logic Description:** General category representing physical disturbances.'
wetlands_everglades_stressors["Disturbance"]["Influenced By"] = ['* Many', '**Influences (Stressors):**', '* Everglades - Invasive Species', '**Logic Description:** General category representing physical disturbances.']
wetlands_everglades_stressors["Disturbance"]["Influences"] = ['* Everglades - Invasive Species', '**Logic Description:** General category representing physical disturbances.']
wetlands_everglades_stressors["Disturbance"]["Logic Description"] = '---'

# --- Native Wildlife Populations ---
wetlands_everglades_stressors["Native Wildlife Populations"]["Metric"] = 'Population sizes of key native species.'
wetlands_everglades_stressors["Native Wildlife Populations"]["Data Sources"] = ['* Wildlife surveys.', '**Impact on Area:** Indirect, through trophic interactions', '**Impact on Biodiversity:**', 'Ecosystem function.', '**Influenced By (Stressors):**', '*  Everglades - Invasive Species', '**Influences (Stressors):**', '* Many', '**Logic Description**: Changes in native wildlife can have cascading effects.']
wetlands_everglades_stressors["Native Wildlife Populations"]["Impact on Area"] = 'Indirect, through trophic interactions'
wetlands_everglades_stressors["Native Wildlife Populations"]["Impact on Biodiversity"] = 'Ecosystem function.\n**Influenced By (Stressors):**\n*  Everglades - Invasive Species\n**Influences (Stressors):**\n* Many\n**Logic Description**: Changes in native wildlife can have cascading effects.'
wetlands_everglades_stressors["Native Wildlife Populations"]["Influenced By"] = ['*  Everglades - Invasive Species', '**Influences (Stressors):**', '* Many', '**Logic Description**: Changes in native wildlife can have cascading effects.']
wetlands_everglades_stressors["Native Wildlife Populations"]["Influences"] = ['* Many', '**Logic Description**: Changes in native wildlife can have cascading effects.']

# --- Urban Runoff ---
wetlands_everglades_stressors["Urban Runoff"]["Metric"] = 'Pollutant concentrations in runoff.'
wetlands_everglades_stressors["Urban Runoff"]["Data Sources"] = ['* Water quality monitoring.', '**Impact on Area**: Water quality degradation', '**Impact on Biodiversity:**', 'Impacts on aquatic life.', '**Influenced By (Stressors):**', '* Everglades - Urban Development', '**Influences (Stressors):**', '* Everglades - Nutrient Pollution', '**Logic Description**: Runoff from urban areas carries pollutants.']
wetlands_everglades_stressors["Urban Runoff"]["Impact on Biodiversity"] = 'Impacts on aquatic life.\n**Influenced By (Stressors):**\n* Everglades - Urban Development\n**Influences (Stressors):**\n* Everglades - Nutrient Pollution\n**Logic Description**: Runoff from urban areas carries pollutants.'
wetlands_everglades_stressors["Urban Runoff"]["Influenced By"] = ['* Everglades - Urban Development', '**Influences (Stressors):**', '* Everglades - Nutrient Pollution', '**Logic Description**: Runoff from urban areas carries pollutants.']
wetlands_everglades_stressors["Urban Runoff"]["Influences"] = ['* Everglades - Nutrient Pollution', '**Logic Description**: Runoff from urban areas carries pollutants.']

# --- Habitat Availability ---
wetlands_everglades_stressors["Habitat Availability"]["Influenced By"] = ['* Everglades - Altered Hydrology', '* Everglades - Invasive Species', '**Influences (Stressors)**:', '* Many', '**Logic Description:** The amount of suitable habitat affects wildlife.']
wetlands_everglades_stressors["Habitat Availability"]["Logic Description"] = '---'

# --- Vegetation Changes ---
wetlands_everglades_stressors["Vegetation Changes"]["Impact on Area"] = 'Habitat Changes'
wetlands_everglades_stressors["Vegetation Changes"]["Impact on Biodiversity"] = 'Altered species interactions.\n**Influenced By (Stressors):**\n* Everglades - Nutrient Pollution\n**Influences (Stressors):**\n* Many\n**Logic Description:** Changes in the dominant plant species.'
wetlands_everglades_stressors["Vegetation Changes"]["Influenced By"] = ['* Everglades - Nutrient Pollution', '**Influences (Stressors):**', '* Many', '**Logic Description:** Changes in the dominant plant species.']
wetlands_everglades_stressors["Vegetation Changes"]["Influences"] = ['* Many', '**Logic Description:** Changes in the dominant plant species.']
wetlands_everglades_stressors["Vegetation Changes"]["Logic Description"] = '---'

# --- Water Quality ---
wetlands_everglades_stressors["Water Quality"]["Impact on Biodiversity"] = '* Impacts on aquatic life\n**Influenced By (Stressors):**\n* Everglades - Nutrient Pollution\n* Everglades - Altered Hydrology\n* Everglades - Saltwater Intrusion\n**Influences (Stressors):**\n* Many, varies\n**Logic Description:** Overall water quality affects ecosystem health'
wetlands_everglades_stressors["Water Quality"]["Influenced By"] = ['* Everglades - Nutrient Pollution', '* Everglades - Altered Hydrology', '* Everglades - Saltwater Intrusion', '**Influences (Stressors):**', '* Many, varies', '**Logic Description:** Overall water quality affects ecosystem health']
wetlands_everglades_stressors["Water Quality"]["Influences"] = ['* Many, varies', '**Logic Description:** Overall water quality affects ecosystem health']
wetlands_everglades_stressors["Water Quality"]["Logic Description"] = ''

