from stressor_templates import *
import copy

tundra_alpine_stressors = {
    "Temperature Increase": copy.deepcopy(climate_change_template),
    "Changes in Precipitation": copy.deepcopy(climate_change_template),
    "Infrastructure Development": copy.deepcopy(infrastructure_development_template),
    "Pollution": copy.deepcopy(pollution_template),
    "Overgrazing": {},
    "Invasive Species": copy.deepcopy(invasive_species_template),
    "Economic Growth": {},
    "Government Policies": {},
    "Long-Range Transport of Pollutants": {},
    "Local Sources": {},
    "Disturbance": {},
    "Native Plant Communities": {},
    "Water Availability": {},
    "Vegetation Changes": {},
    "Soil Erosion": {},
    "Wildlife Health": {},
    "Livestock Management Practices": {},
    "Water Quality": {},
    "Population Dynamics": {},
    "Glacier Retreat": {},
    "Snowpack": {},
}

# --- Temperature Increase ---
tundra_alpine_stressors["Temperature Increase"]["Metric"] = 'Average Annual Temperature Increase (°C).'
tundra_alpine_stressors["Temperature Increase"]["Data Sources"] = ['Climate Models.', 'Historical Records (mountain weather stations).', '**Impact on Area:** Indirect; changes in snowpack, glacier retreat.', '**Impact on Biodiversity:**', 'Species shifts (upslope).', 'Increased stress.', 'Phenology changes.', 'Increased risk of extinction for high-elevation specialists.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions', '**Influences (Stressors):**', 'Alpine Tundra - Changes in Precipitation', 'Alpine Tundra - Glacier Retreat', 'Alpine Tundra - Snowpack', '**Logic Description:** Similar to Arctic Tundra, but with even greater risk of species extinctions due to limited "upward" movement. "Mountain top extinction."']
tundra_alpine_stressors["Temperature Increase"]["Impact on Area"] = 'Indirect; changes in snowpack, glacier retreat.'
tundra_alpine_stressors["Temperature Increase"]["Impact on Biodiversity"] = 'Species shifts (upslope).\nIncreased stress.\nPhenology changes.\nIncreased risk of extinction for high-elevation specialists.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions\n**Influences (Stressors):**\nAlpine Tundra - Changes in Precipitation\nAlpine Tundra - Glacier Retreat\nAlpine Tundra - Snowpack\n**Logic Description:** Similar to Arctic Tundra, but with even greater risk of species extinctions due to limited "upward" movement. "Mountain top extinction."'
tundra_alpine_stressors["Temperature Increase"]["Influenced By"] = ['Global Greenhouse Gas Emissions', '**Influences (Stressors):**', 'Alpine Tundra - Changes in Precipitation', 'Alpine Tundra - Glacier Retreat', 'Alpine Tundra - Snowpack', '**Logic Description:** Similar to Arctic Tundra, but with even greater risk of species extinctions due to limited "upward" movement. "Mountain top extinction."']
tundra_alpine_stressors["Temperature Increase"]["Influences"] = ['Alpine Tundra - Changes in Precipitation', 'Alpine Tundra - Glacier Retreat', 'Alpine Tundra - Snowpack', '**Logic Description:** Similar to Arctic Tundra, but with even greater risk of species extinctions due to limited "upward" movement. "Mountain top extinction."']
tundra_alpine_stressors["Temperature Increase"]["Logic Description"] = '---'

# --- Changes in Precipitation ---
tundra_alpine_stressors["Changes in Precipitation"]["Metric"] = 'Change in annual precipitation (mm/year); changes in snowpack (depth, duration).'
tundra_alpine_stressors["Changes in Precipitation"]["Data Sources"] = ['Climate Models.', 'Historical Records (mountain weather stations).', '**Impact on Area:** Indirect; changes in water availability.', '**Impact on Biodiversity:**', 'Changes in vegetation composition.', 'Altered streamflow, impacting aquatic ecosystems.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions', '**Influences (Stressors):**', 'Alpine Tundra - Water Availability', '**Logic Description:** Changes in snowpack are particularly critical, affecting water availability throughout the year.']
tundra_alpine_stressors["Changes in Precipitation"]["Impact on Area"] = 'Indirect; changes in water availability.'
tundra_alpine_stressors["Changes in Precipitation"]["Impact on Biodiversity"] = 'Changes in vegetation composition.\nAltered streamflow, impacting aquatic ecosystems.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions\n**Influences (Stressors):**\nAlpine Tundra - Water Availability\n**Logic Description:** Changes in snowpack are particularly critical, affecting water availability throughout the year.'
tundra_alpine_stressors["Changes in Precipitation"]["Influenced By"] = ['Global Greenhouse Gas Emissions', '**Influences (Stressors):**', 'Alpine Tundra - Water Availability', '**Logic Description:** Changes in snowpack are particularly critical, affecting water availability throughout the year.']
tundra_alpine_stressors["Changes in Precipitation"]["Influences"] = ['Alpine Tundra - Water Availability', '**Logic Description:** Changes in snowpack are particularly critical, affecting water availability throughout the year.']
tundra_alpine_stressors["Changes in Precipitation"]["Logic Description"] = '---'

# --- Infrastructure Development ---
tundra_alpine_stressors["Infrastructure Development"]["Metric"] = 'Road density (km/km²); area affected by ski resorts, tourism infrastructure, and other development (ha).'
tundra_alpine_stressors["Infrastructure Development"]["Data Sources"] = ['Government statistics (local and regional).', 'Remote sensing data.', '**Impact on Area:** Habitat fragmentation; direct loss of habitat; soil disturbance.', '**Impact on Biodiversity:**', 'Habitat loss and fragmentation.', 'Disturbance to wildlife (noise, human presence).', 'Increased risk of invasive species introduction.', '**Influenced By (Stressors):**', 'Alpine Tundra - Economic Growth (tourism)', 'Alpine Tundra - Government Policies', '**Influences (Stressors):**', 'Alpine Tundra - Localized Pollution', 'Alpine Tundra - Invasive Species', '**Logic Description:** Tourism and recreation infrastructure (ski resorts, roads) are major drivers of habitat loss and fragmentation in alpine tundra.']
tundra_alpine_stressors["Infrastructure Development"]["Impact on Area"] = 'Habitat fragmentation; direct loss of habitat; soil disturbance.'
tundra_alpine_stressors["Infrastructure Development"]["Impact on Biodiversity"] = 'Habitat loss and fragmentation.\nDisturbance to wildlife (noise, human presence).\nIncreased risk of invasive species introduction.\n**Influenced By (Stressors):**\nAlpine Tundra - Economic Growth (tourism)\nAlpine Tundra - Government Policies\n**Influences (Stressors):**\nAlpine Tundra - Localized Pollution\nAlpine Tundra - Invasive Species\n**Logic Description:** Tourism and recreation infrastructure (ski resorts, roads) are major drivers of habitat loss and fragmentation in alpine tundra.'
tundra_alpine_stressors["Infrastructure Development"]["Influenced By"] = ['Alpine Tundra - Economic Growth (tourism)', 'Alpine Tundra - Government Policies', '**Influences (Stressors):**', 'Alpine Tundra - Localized Pollution', 'Alpine Tundra - Invasive Species', '**Logic Description:** Tourism and recreation infrastructure (ski resorts, roads) are major drivers of habitat loss and fragmentation in alpine tundra.']
tundra_alpine_stressors["Infrastructure Development"]["Influences"] = ['Alpine Tundra - Localized Pollution', 'Alpine Tundra - Invasive Species', '**Logic Description:** Tourism and recreation infrastructure (ski resorts, roads) are major drivers of habitat loss and fragmentation in alpine tundra.']
tundra_alpine_stressors["Infrastructure Development"]["Logic Description"] = '---'

# --- Pollution ---
tundra_alpine_stressors["Pollution"]["Metric"] = 'Concentrations of pollutants (e.g., nitrogen, heavy metals) in air, water, soil, and biota.'
tundra_alpine_stressors["Pollution"]["Data Sources"] = ['Environmental monitoring programs (often associated with research stations).', 'Research studies.', '**Impact on Area:** Contamination of soil, water, and air.', '**Impact on Biodiversity:**', 'Toxic effects on wildlife and plants.', 'Reduced reproductive success.', 'Alteration of nutrient cycles (especially nitrogen deposition).', '**Influenced By (Stressors):**', 'Alpine Tundra - Long-Range Transport of Pollutants', 'Alpine Tundra - Local Sources', '**Influences (Stressors):**', '*  Alpine Tundra - Wildlife Health', 'Alpine Tundra - Water Quality', '**Logic Description:** Alpine tundra receives pollutants from both long-range transport and local sources (tourism, mining). Nitrogen deposition is a particular concern.']
tundra_alpine_stressors["Pollution"]["Impact on Area"] = 'Contamination of soil, water, and air.'
tundra_alpine_stressors["Pollution"]["Impact on Biodiversity"] = 'Toxic effects on wildlife and plants.\nReduced reproductive success.\nAlteration of nutrient cycles (especially nitrogen deposition).\n**Influenced By (Stressors):**\nAlpine Tundra - Long-Range Transport of Pollutants\nAlpine Tundra - Local Sources\n**Influences (Stressors):**\n*  Alpine Tundra - Wildlife Health\nAlpine Tundra - Water Quality\n**Logic Description:** Alpine tundra receives pollutants from both long-range transport and local sources (tourism, mining). Nitrogen deposition is a particular concern.'
tundra_alpine_stressors["Pollution"]["Influenced By"] = ['Alpine Tundra - Long-Range Transport of Pollutants', 'Alpine Tundra - Local Sources', '**Influences (Stressors):**', '*  Alpine Tundra - Wildlife Health', 'Alpine Tundra - Water Quality', '**Logic Description:** Alpine tundra receives pollutants from both long-range transport and local sources (tourism, mining). Nitrogen deposition is a particular concern.']
tundra_alpine_stressors["Pollution"]["Influences"] = ['*  Alpine Tundra - Wildlife Health', 'Alpine Tundra - Water Quality', '**Logic Description:** Alpine tundra receives pollutants from both long-range transport and local sources (tourism, mining). Nitrogen deposition is a particular concern.']
tundra_alpine_stressors["Pollution"]["Logic Description"] = '---'

# --- Overgrazing ---
tundra_alpine_stressors["Overgrazing"]["Metric"] = 'Livestock density (animals/km²); vegetation cover and composition; signs of soil erosion.'
tundra_alpine_stressors["Overgrazing"]["Data Sources"] = ['Agricultural statistics (where available).', 'Vegetation surveys.', 'Research studies.', '**Impact on Area:** Changes in vegetation composition; soil erosion; degradation of water quality.', '**Impact on Biodiversity:**', 'Loss of palatable plant species.', 'Spread of unpalatable or invasive species.', 'Soil compaction, reducing water infiltration.', '**Influenced By (Stressors):**', 'Alpine Tundra - Livestock Management Practices', '**Influences (Stressors):**', 'Alpine Tundra - Vegetation Changes', '*  Alpine Tundra - Soil Erosion', '**Logic Description:** Overgrazing by livestock can damage fragile alpine vegetation and lead to soil erosion.']
tundra_alpine_stressors["Overgrazing"]["Impact on Area"] = 'Changes in vegetation composition; soil erosion; degradation of water quality.'
tundra_alpine_stressors["Overgrazing"]["Impact on Biodiversity"] = 'Loss of palatable plant species.\nSpread of unpalatable or invasive species.\nSoil compaction, reducing water infiltration.\n**Influenced By (Stressors):**\nAlpine Tundra - Livestock Management Practices\n**Influences (Stressors):**\nAlpine Tundra - Vegetation Changes\n*  Alpine Tundra - Soil Erosion\n**Logic Description:** Overgrazing by livestock can damage fragile alpine vegetation and lead to soil erosion.'
tundra_alpine_stressors["Overgrazing"]["Influenced By"] = ['Alpine Tundra - Livestock Management Practices', '**Influences (Stressors):**', 'Alpine Tundra - Vegetation Changes', '*  Alpine Tundra - Soil Erosion', '**Logic Description:** Overgrazing by livestock can damage fragile alpine vegetation and lead to soil erosion.']
tundra_alpine_stressors["Overgrazing"]["Influences"] = ['Alpine Tundra - Vegetation Changes', '*  Alpine Tundra - Soil Erosion', '**Logic Description:** Overgrazing by livestock can damage fragile alpine vegetation and lead to soil erosion.']
tundra_alpine_stressors["Overgrazing"]["Logic Description"] = '---'

# --- Invasive Species ---
tundra_alpine_stressors["Invasive Species"]["Metric"] = 'Distribution and abundance of invasive plant species.'
tundra_alpine_stressors["Invasive Species"]["Data Sources"] = ['* Research studies.', '* Monitoring programs', '**Impact on Area**: Changes in vegetation', '**Impact on Biodiversity:**', '* Competition', '**Influenced By (Stressors):**', '* Alpine Tundra - Climate Change', '* Alpine Tundra - Disturbance', '**Influences (Stressors):**', '* Alpine Tundra - Native Plant Communities', '**Logic Description:** While less widespread than other, invasive species are increasing.']
tundra_alpine_stressors["Invasive Species"]["Impact on Biodiversity"] = '* Competition\n**Influenced By (Stressors):**\n* Alpine Tundra - Climate Change\n* Alpine Tundra - Disturbance\n**Influences (Stressors):**\n* Alpine Tundra - Native Plant Communities\n**Logic Description:** While less widespread than other, invasive species are increasing.'
tundra_alpine_stressors["Invasive Species"]["Influenced By"] = ['* Alpine Tundra - Climate Change', '* Alpine Tundra - Disturbance', '**Influences (Stressors):**', '* Alpine Tundra - Native Plant Communities', '**Logic Description:** While less widespread than other, invasive species are increasing.']
tundra_alpine_stressors["Invasive Species"]["Influences"] = ['* Alpine Tundra - Native Plant Communities', '**Logic Description:** While less widespread than other, invasive species are increasing.']
tundra_alpine_stressors["Invasive Species"]["Logic Description"] = '---'

# --- Economic Growth ---
tundra_alpine_stressors["Economic Growth"]["Metric"] = 'GDP, tourism revenue'
tundra_alpine_stressors["Economic Growth"]["Data Sources"] = ['* Economic Data', '**Impact on Area:** Increased pressure', '**Impact on Biodiversity:**', '* Disturbance', '**Influenced By (Stressors)**', '* Global and local economies', '**Influences (Stressors):**', '* Alpine Tundra - Infrastructure Development', '**Logic Description:** Economic growth, particularly in tourism, drives development.']
tundra_alpine_stressors["Economic Growth"]["Impact on Area"] = 'Increased pressure'
tundra_alpine_stressors["Economic Growth"]["Impact on Biodiversity"] = '* Disturbance\n**Influenced By (Stressors)**\n* Global and local economies\n**Influences (Stressors):**\n* Alpine Tundra - Infrastructure Development\n**Logic Description:** Economic growth, particularly in tourism, drives development.'
tundra_alpine_stressors["Economic Growth"]["Influences"] = ['* Alpine Tundra - Infrastructure Development', '**Logic Description:** Economic growth, particularly in tourism, drives development.']
tundra_alpine_stressors["Economic Growth"]["Logic Description"] = '---'

# --- Government Policies ---
tundra_alpine_stressors["Government Policies"]["Metric"] = 'Land use regulations, environmental protections'
tundra_alpine_stressors["Government Policies"]["Data Sources"] = ['* Policy Documents', '**Impact on Area:** Variable', '**Impact on Biodiversity:**', '* Variable', '**Influenced By (Stressors):**', '* Politics, economics', '**Influences (Stressors):**', '* Alpine Tundra - Infrastructure Development', '**Logic Description:** Government policies can have positive or negative impacts']
tundra_alpine_stressors["Government Policies"]["Impact on Area"] = 'Variable'
tundra_alpine_stressors["Government Policies"]["Impact on Biodiversity"] = '* Variable\n**Influenced By (Stressors):**\n* Politics, economics\n**Influences (Stressors):**\n* Alpine Tundra - Infrastructure Development\n**Logic Description:** Government policies can have positive or negative impacts'
tundra_alpine_stressors["Government Policies"]["Influenced By"] = ['* Politics, economics', '**Influences (Stressors):**', '* Alpine Tundra - Infrastructure Development', '**Logic Description:** Government policies can have positive or negative impacts']
tundra_alpine_stressors["Government Policies"]["Influences"] = ['* Alpine Tundra - Infrastructure Development', '**Logic Description:** Government policies can have positive or negative impacts']
tundra_alpine_stressors["Government Policies"]["Logic Description"] = '---'

# --- Long-Range Transport of Pollutants ---
tundra_alpine_stressors["Long-Range Transport of Pollutants"]["Data Sources"] = ['* Environmental Monitoring', '**Impact on Area:** Widespread, low-level contamination', '**Impact on Biodiversity:**', '*  Toxic effects', '* Bioaccumulation', '**Influenced By (Stressors):**', '* Industrial activity in other regions.', '**Influences (Stressors):**', '* Alpine Tundra - Pollution', '**Logic Description:** Pollutants travel long distances']
tundra_alpine_stressors["Long-Range Transport of Pollutants"]["Impact on Area"] = 'Widespread, low-level contamination'
tundra_alpine_stressors["Long-Range Transport of Pollutants"]["Impact on Biodiversity"] = '*  Toxic effects\n* Bioaccumulation\n**Influenced By (Stressors):**\n* Industrial activity in other regions.\n**Influences (Stressors):**\n* Alpine Tundra - Pollution\n**Logic Description:** Pollutants travel long distances'
tundra_alpine_stressors["Long-Range Transport of Pollutants"]["Influenced By"] = ['* Industrial activity in other regions.', '**Influences (Stressors):**', '* Alpine Tundra - Pollution', '**Logic Description:** Pollutants travel long distances']
tundra_alpine_stressors["Long-Range Transport of Pollutants"]["Influences"] = ['* Alpine Tundra - Pollution', '**Logic Description:** Pollutants travel long distances']
tundra_alpine_stressors["Long-Range Transport of Pollutants"]["Logic Description"] = '---'

# --- Local Sources ---
tundra_alpine_stressors["Local Sources"]["Data Sources"] = ['* Environmental monitoring.', '**Impact on Area:** Localized pollution hot spots.', '**Impact on Biodiversity:**', '* Impacts on wildlife.', '**Influenced By (Stressors):**', '* Alpine Tundra - Infrastructure Development', '**Influences (Stressors):**', '* Alpine Tundra - Pollution', '**Logic Description:** Local activities (tourism, mining, etc.) contribute to pollution']
tundra_alpine_stressors["Local Sources"]["Impact on Area"] = 'Localized pollution hot spots.'
tundra_alpine_stressors["Local Sources"]["Impact on Biodiversity"] = '* Impacts on wildlife.\n**Influenced By (Stressors):**\n* Alpine Tundra - Infrastructure Development\n**Influences (Stressors):**\n* Alpine Tundra - Pollution\n**Logic Description:** Local activities (tourism, mining, etc.) contribute to pollution'
tundra_alpine_stressors["Local Sources"]["Influenced By"] = ['* Alpine Tundra - Infrastructure Development', '**Influences (Stressors):**', '* Alpine Tundra - Pollution', '**Logic Description:** Local activities (tourism, mining, etc.) contribute to pollution']
tundra_alpine_stressors["Local Sources"]["Influences"] = ['* Alpine Tundra - Pollution', '**Logic Description:** Local activities (tourism, mining, etc.) contribute to pollution']
tundra_alpine_stressors["Local Sources"]["Logic Description"] = '---'

# --- Disturbance ---
tundra_alpine_stressors["Disturbance"]["Metric"] = 'Area and frequency.'
tundra_alpine_stressors["Disturbance"]["Data Sources"] = ['* Field observations', '* Remote Sensing', '**Impact on Area**: Site Specific', '**Impact on Biodiversity:**', '* Variable', '**Influenced By (Stressors)**', '* Many', '**Influences (Stressors):**', '*  Alpine Tundra - Invasive Species', '**Logic Description:** General category']
tundra_alpine_stressors["Disturbance"]["Impact on Biodiversity"] = '* Variable\n**Influenced By (Stressors)**\n* Many\n**Influences (Stressors):**\n*  Alpine Tundra - Invasive Species\n**Logic Description:** General category'
tundra_alpine_stressors["Disturbance"]["Influences"] = ['*  Alpine Tundra - Invasive Species', '**Logic Description:** General category']
tundra_alpine_stressors["Disturbance"]["Logic Description"] = '---'

# --- Native Plant Communities ---
tundra_alpine_stressors["Native Plant Communities"]["Metric"] = 'Plant species composition, abundance'
tundra_alpine_stressors["Native Plant Communities"]["Data Sources"] = ['* Field Surveys', '**Impact on Area:** Overall ecosystem structure', '**Impact on Biodiversity:**', 'Interactions with other species.', '**Influenced By (Stressors)**', '* Alpine Tundra - Invasive Species', '**Influences (Stressors):**', '* Many', '**Logic Description**: Foundation of the ecosystem.']
tundra_alpine_stressors["Native Plant Communities"]["Impact on Area"] = 'Overall ecosystem structure'
tundra_alpine_stressors["Native Plant Communities"]["Impact on Biodiversity"] = 'Interactions with other species.\n**Influenced By (Stressors)**\n* Alpine Tundra - Invasive Species\n**Influences (Stressors):**\n* Many\n**Logic Description**: Foundation of the ecosystem.'
tundra_alpine_stressors["Native Plant Communities"]["Influences"] = ['* Many', '**Logic Description**: Foundation of the ecosystem.']

# --- Water Availability ---
tundra_alpine_stressors["Water Availability"]["Impact on Area"] = 'Water availability'
tundra_alpine_stressors["Water Availability"]["Influenced By"] = ['* Alpine Tundra - Changes in Precipitation', '**Influences (Stressors)**', '* Many', '**Logic Description:** Water is essential.']
tundra_alpine_stressors["Water Availability"]["Logic Description"] = '---'

# --- Vegetation Changes ---
tundra_alpine_stressors["Vegetation Changes"]["Data Sources"] = ['* Field Surveys, Remote Sensing', '**Impact on Area:** Habitat Structure.', '**Impact on Biodiversity:**', '* Altered species interactions.', '**Influenced By (Stressors):**', '* Many, Varies', '**Influences (Stressors):**', '* Many, Varies', '**Logic Description**: Changes in vegetation reflect other stressors.']
tundra_alpine_stressors["Vegetation Changes"]["Impact on Area"] = 'Habitat Structure.'
tundra_alpine_stressors["Vegetation Changes"]["Impact on Biodiversity"] = '* Altered species interactions.\n**Influenced By (Stressors):**\n* Many, Varies\n**Influences (Stressors):**\n* Many, Varies\n**Logic Description**: Changes in vegetation reflect other stressors.'
tundra_alpine_stressors["Vegetation Changes"]["Influenced By"] = ['* Many, Varies', '**Influences (Stressors):**', '* Many, Varies', '**Logic Description**: Changes in vegetation reflect other stressors.']
tundra_alpine_stressors["Vegetation Changes"]["Influences"] = ['* Many, Varies', '**Logic Description**: Changes in vegetation reflect other stressors.']

# --- Soil Erosion ---
tundra_alpine_stressors["Soil Erosion"]["Impact on Area"] = 'Loss of topsoil, reduced soil fertility.'
tundra_alpine_stressors["Soil Erosion"]["Impact on Biodiversity"] = '* Impacts on plant growth.\n**Influenced By (Stressors):**\n*  Alpine Tundra - Overgrazing\n**Influences (Stressors):**\n* Many, Varies\n**Logic Description**: Erosion degrades soil.'
tundra_alpine_stressors["Soil Erosion"]["Influenced By"] = ['*  Alpine Tundra - Overgrazing', '**Influences (Stressors):**', '* Many, Varies', '**Logic Description**: Erosion degrades soil.']
tundra_alpine_stressors["Soil Erosion"]["Influences"] = ['* Many, Varies', '**Logic Description**: Erosion degrades soil.']

# --- Wildlife Health ---
tundra_alpine_stressors["Wildlife Health"]["Data Sources"] = ['* Wildlife Monitoring', '**Impact on Area:** Indirect, via population', '**Impact on Biodiversity:**', '* Population Declines', '**Influenced By (Stressors):**', '* Alpine Tundra - Pollution', '**Influences (Stressors):**', '* Alpine Tundra - Population Dynamics', '**Logic Description:** Health']
tundra_alpine_stressors["Wildlife Health"]["Impact on Area"] = 'Indirect, via population'
tundra_alpine_stressors["Wildlife Health"]["Impact on Biodiversity"] = '* Population Declines\n**Influenced By (Stressors):**\n* Alpine Tundra - Pollution\n**Influences (Stressors):**\n* Alpine Tundra - Population Dynamics\n**Logic Description:** Health'
tundra_alpine_stressors["Wildlife Health"]["Influenced By"] = ['* Alpine Tundra - Pollution', '**Influences (Stressors):**', '* Alpine Tundra - Population Dynamics', '**Logic Description:** Health']
tundra_alpine_stressors["Wildlife Health"]["Influences"] = ['* Alpine Tundra - Population Dynamics', '**Logic Description:** Health']
tundra_alpine_stressors["Wildlife Health"]["Logic Description"] = '---'

# --- Livestock Management Practices ---
tundra_alpine_stressors["Livestock Management Practices"]["Metric"] = 'Grazing intensity, timing, and type of livestock.'
tundra_alpine_stressors["Livestock Management Practices"]["Data Sources"] = ['* Agricultural records, field observations.', '**Impact on Area:** Changes in vegetation composition and structure, soil compaction.', '**Impact on Biodiversity:**', '* Impacts on plant communities, potential for competition with native herbivores.', '**Influenced By (Stressors)**', '* Economic factors, cultural practices, government policies.', '**Influences (Stressors)**', '* Alpine Tundra - Overgrazing']
tundra_alpine_stressors["Livestock Management Practices"]["Impact on Area"] = 'Changes in vegetation composition and structure, soil compaction.'
tundra_alpine_stressors["Livestock Management Practices"]["Impact on Biodiversity"] = '* Impacts on plant communities, potential for competition with native herbivores.\n**Influenced By (Stressors)**\n* Economic factors, cultural practices, government policies.\n**Influences (Stressors)**\n* Alpine Tundra - Overgrazing'

# --- Water Quality ---
tundra_alpine_stressors["Water Quality"]["Impact on Biodiversity"] = '* Impacts on aquatic life.\n**Influenced By (Stressors):**\n* Alpine Tundra - Pollution\n**Influences (Stressors):**\n* Many\n**Logic Description**: Water quality is fundamental.'
tundra_alpine_stressors["Water Quality"]["Influenced By"] = ['* Alpine Tundra - Pollution', '**Influences (Stressors):**', '* Many', '**Logic Description**: Water quality is fundamental.']
tundra_alpine_stressors["Water Quality"]["Influences"] = ['* Many', '**Logic Description**: Water quality is fundamental.']

# --- Population Dynamics ---
tundra_alpine_stressors["Population Dynamics"]["Data Sources"] = ['* Wildlife/Plant Surveys.', '**Impact on Area:** Indirect.', '**Impact on Biodiversity:**', '* Ecosystem Function', '**Influenced By (Stressors)**', '* Alpine Tundra - Wildlife Health', '**Influences (Stressors)**:', '* Many', '**Logic Description:** Changes affect ecosystem']
tundra_alpine_stressors["Population Dynamics"]["Impact on Area"] = 'Indirect.'
tundra_alpine_stressors["Population Dynamics"]["Impact on Biodiversity"] = '* Ecosystem Function\n**Influenced By (Stressors)**\n* Alpine Tundra - Wildlife Health\n**Influences (Stressors)**:\n* Many\n**Logic Description:** Changes affect ecosystem'
tundra_alpine_stressors["Population Dynamics"]["Logic Description"] = '---'

# --- Glacier Retreat ---
tundra_alpine_stressors["Glacier Retreat"]["Data Sources"] = ['* Remote sensing', '* Field measurements', '**Impact on Area:** Water availability (long-term decrease).', '**Impact on Biodiversity:**', '* Impacts on downstream ecosystems.', '**Influenced By (Stressors):**', '* Alpine Tundra - Temperature Increase', '**Influences (Stressors):**', '*  Alpine Tundra - Water Availability', '**Logic Description**: Glaciers are a critical water source.']
tundra_alpine_stressors["Glacier Retreat"]["Impact on Area"] = 'Water availability (long-term decrease).'
tundra_alpine_stressors["Glacier Retreat"]["Impact on Biodiversity"] = '* Impacts on downstream ecosystems.\n**Influenced By (Stressors):**\n* Alpine Tundra - Temperature Increase\n**Influences (Stressors):**\n*  Alpine Tundra - Water Availability\n**Logic Description**: Glaciers are a critical water source.'
tundra_alpine_stressors["Glacier Retreat"]["Influenced By"] = ['* Alpine Tundra - Temperature Increase', '**Influences (Stressors):**', '*  Alpine Tundra - Water Availability', '**Logic Description**: Glaciers are a critical water source.']
tundra_alpine_stressors["Glacier Retreat"]["Influences"] = ['*  Alpine Tundra - Water Availability', '**Logic Description**: Glaciers are a critical water source.']

# --- Snowpack ---
tundra_alpine_stressors["Snowpack"]["Metric"] = 'Snow depth, duration, water content.'
tundra_alpine_stressors["Snowpack"]["Impact on Area"] = 'Water availability, insulation for plants and animals.'
tundra_alpine_stressors["Snowpack"]["Impact on Biodiversity"] = 'Impacts on plant growth, animal survival, and timing of biological events.\n**Influenced By (Stressors)**\n* Alpine Tundra - Temperature Increase\n* Alpine Tundra- Changes in Precipitation\n**Influences (Stressors)**\n* Many\n**Logic Description**: Snowpack is critical for water and insulation.'

