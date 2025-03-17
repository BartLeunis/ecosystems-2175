from stressor_templates import *
import copy

grasslands_south_american_pampas_stressors = {
    "Land-Use Change": {},
    "Habitat Fragmentation": {},
    "Climate Change": copy.deepcopy(climate_change_template),
    "Overgrazing": {},
    "Invasive Species": copy.deepcopy(invasive_species_template),
}

# --- Land-Use Change ---
grasslands_south_american_pampas_stressors["Land-Use Change"]["Metric"] = 'Area converted to agriculture (especially soybeans), pasture, or other land uses (ha/year).'
grasslands_south_american_pampas_stressors["Land-Use Change"]["Data Sources"] = ['Remote sensing data.', 'Government statistics (Argentina, Brazil, Uruguay).', 'Research publications.', '**Impact on Area:** Massive loss of pampas habitat; fragmentation.', '**Impact on Biodiversity:**', 'Habitat loss and fragmentation.', 'Decline of pampas-dependent species.', '**Influenced By (Stressors):**', 'South American Pampas - Agricultural Expansion: Demand for soybeans and other crops, and for cattle pasture.', 'South American Pampas - Global Commodity Prices.', 'South American Pampas - Government Policies.', '**Influences (Stressors):**', '*  South American Pampas - Habitat Fragmentation', '**Logic Description:** Conversion of pampas to agriculture (especially soybean cultivation) and pasture is the dominant stressor, leading to massive habitat loss.']
grasslands_south_american_pampas_stressors["Land-Use Change"]["Impact on Area"] = 'Massive loss of pampas habitat; fragmentation.'
grasslands_south_american_pampas_stressors["Land-Use Change"]["Impact on Biodiversity"] = 'Habitat loss and fragmentation.\nDecline of pampas-dependent species.\n**Influenced By (Stressors):**\nSouth American Pampas - Agricultural Expansion: Demand for soybeans and other crops, and for cattle pasture.\nSouth American Pampas - Global Commodity Prices.\nSouth American Pampas - Government Policies.\n**Influences (Stressors):**\n*  South American Pampas - Habitat Fragmentation\n**Logic Description:** Conversion of pampas to agriculture (especially soybean cultivation) and pasture is the dominant stressor, leading to massive habitat loss.'
grasslands_south_american_pampas_stressors["Land-Use Change"]["Influenced By"] = ['South American Pampas - Agricultural Expansion: Demand for soybeans and other crops, and for cattle pasture.', 'South American Pampas - Global Commodity Prices.', 'South American Pampas - Government Policies.', '**Influences (Stressors):**', '*  South American Pampas - Habitat Fragmentation', '**Logic Description:** Conversion of pampas to agriculture (especially soybean cultivation) and pasture is the dominant stressor, leading to massive habitat loss.']
grasslands_south_american_pampas_stressors["Land-Use Change"]["Influences"] = ['*  South American Pampas - Habitat Fragmentation', '**Logic Description:** Conversion of pampas to agriculture (especially soybean cultivation) and pasture is the dominant stressor, leading to massive habitat loss.']
grasslands_south_american_pampas_stressors["Land-Use Change"]["Logic Description"] = '---'
grasslands_south_american_pampas_stressors["Land-Use Change"]["Impact Function"] = "impact_land_use_change_grasslands_south_american_pampas"

# --- Habitat Fragmentation ---
grasslands_south_american_pampas_stressors["Habitat Fragmentation"]["Metric"] = 'Patch size distribution; edge density; connectivity indices.'
grasslands_south_american_pampas_stressors["Habitat Fragmentation"]["Data Sources"] = ['Land cover data.', 'GIS analysis.', '**Impact on Area:** Remaining pampas exists in small, isolated patches.', '**Impact on Biodiversity:**', '* Reduced gene flow.', 'Increased edge effects.', '* Limited Dispersal', '* Increased vulnerability.', '**Influenced By (Stressors):**', '*  South American Pampas - Land Use Change', '**Influences (Stressors):**', '* Exacerbates other stressor impacts', '**Logic Description:** Fragmentation isolates pampas patches, reducing their ecological viability.']
grasslands_south_american_pampas_stressors["Habitat Fragmentation"]["Impact on Area"] = 'Remaining pampas exists in small, isolated patches.'
grasslands_south_american_pampas_stressors["Habitat Fragmentation"]["Impact on Biodiversity"] = '* Reduced gene flow.\nIncreased edge effects.\n* Limited Dispersal\n* Increased vulnerability.\n**Influenced By (Stressors):**\n*  South American Pampas - Land Use Change\n**Influences (Stressors):**\n* Exacerbates other stressor impacts\n**Logic Description:** Fragmentation isolates pampas patches, reducing their ecological viability.'
grasslands_south_american_pampas_stressors["Habitat Fragmentation"]["Influenced By"] = ['*  South American Pampas - Land Use Change', '**Influences (Stressors):**', '* Exacerbates other stressor impacts', '**Logic Description:** Fragmentation isolates pampas patches, reducing their ecological viability.']
grasslands_south_american_pampas_stressors["Habitat Fragmentation"]["Influences"] = ['* Exacerbates other stressor impacts', '**Logic Description:** Fragmentation isolates pampas patches, reducing their ecological viability.']
grasslands_south_american_pampas_stressors["Habitat Fragmentation"]["Logic Description"] = '---'
grasslands_south_american_pampas_stressors["Habitat Fragmentation"]["Impact Function"] = "impact_habitat_fragmentation_grasslands_south_american_pampas"

# --- Climate Change ---
grasslands_south_american_pampas_stressors["Climate Change"]["Metric"] = 'Temperature increase; changes in precipitation; drought frequency/severity.'
grasslands_south_american_pampas_stressors["Climate Change"]["Data Sources"] = ['* Climate models.', '* Historical records', '**Impact on Area:** Indirect - changes in growing conditions.', '**Impact on Biodiversity:**', '* Shifts in species distributions.', '* Increased stress.', '* Changes in phenology.', '**Influenced By (Stressors):**', '* Global GHG', '**Influences (Stressors):**', '*  South American Pampas - Water Availability', '**Logic Description:** Climate change alters temperature and precipitation patterns.']
grasslands_south_american_pampas_stressors["Climate Change"]["Impact on Area"] = 'Indirect - changes in growing conditions.'
grasslands_south_american_pampas_stressors["Climate Change"]["Impact on Biodiversity"] = '* Shifts in species distributions.\n* Increased stress.\n* Changes in phenology.\n**Influenced By (Stressors):**\n* Global GHG\n**Influences (Stressors):**\n*  South American Pampas - Water Availability\n**Logic Description:** Climate change alters temperature and precipitation patterns.'
grasslands_south_american_pampas_stressors["Climate Change"]["Influenced By"] = ['* Global GHG', '**Influences (Stressors):**', '*  South American Pampas - Water Availability', '**Logic Description:** Climate change alters temperature and precipitation patterns.']
grasslands_south_american_pampas_stressors["Climate Change"]["Influences"] = ['*  South American Pampas - Water Availability', '**Logic Description:** Climate change alters temperature and precipitation patterns.']
grasslands_south_american_pampas_stressors["Climate Change"]["Logic Description"] = '---'
grasslands_south_american_pampas_stressors["Climate Change"]["Impact Function"] = "impact_climate_change_grasslands_south_american_pampas"

# --- Overgrazing ---
grasslands_south_american_pampas_stressors["Overgrazing"]["Metric"] = 'Livestock density; vegetation cover and composition.'
grasslands_south_american_pampas_stressors["Overgrazing"]["Data Sources"] = ['* Agricultural statistics.', '* Vegetation Surveys', '**Impact on Area:** Changes in vegetation structure; soil erosion.', '**Impact on Biodiversity:**', '* Loss of palatable species', '* Soil compaction', '* Spread of invasives.', '**Influenced By (Stressors):**', '*  South American Pampas - Livestock Management Practices.', '**Influences (Stressors):**', '*  South American Pampas - Vegetation Changes', '**Logic Description:** Overgrazing by livestock can degrade pampas vegetation.']
grasslands_south_american_pampas_stressors["Overgrazing"]["Impact on Area"] = 'Changes in vegetation structure; soil erosion.'
grasslands_south_american_pampas_stressors["Overgrazing"]["Impact on Biodiversity"] = '* Loss of palatable species\n* Soil compaction\n* Spread of invasives.\n**Influenced By (Stressors):**\n*  South American Pampas - Livestock Management Practices.\n**Influences (Stressors):**\n*  South American Pampas - Vegetation Changes\n**Logic Description:** Overgrazing by livestock can degrade pampas vegetation.'
grasslands_south_american_pampas_stressors["Overgrazing"]["Influenced By"] = ['*  South American Pampas - Livestock Management Practices.', '**Influences (Stressors):**', '*  South American Pampas - Vegetation Changes', '**Logic Description:** Overgrazing by livestock can degrade pampas vegetation.']
grasslands_south_american_pampas_stressors["Overgrazing"]["Influences"] = ['*  South American Pampas - Vegetation Changes', '**Logic Description:** Overgrazing by livestock can degrade pampas vegetation.']
grasslands_south_american_pampas_stressors["Overgrazing"]["Logic Description"] = '---'
grasslands_south_american_pampas_stressors["Overgrazing"]["Impact Function"] = "impact_overgrazing_grasslands_south_american_pampas"

# --- Invasive Species ---
grasslands_south_american_pampas_stressors["Invasive Species"]["Metric"] = 'Abundance/Distribution of key invasive species (e.g., certain grasses).'
grasslands_south_american_pampas_stressors["Invasive Species"]["Data Sources"] = ['* Vegetation surveys.', '* Research.', '**Impact on Area:** Changes in vegetation composition.', '**Impact on Biodiversity:**', '* Competition.', '* Altered processes.', '**Influenced By (Stressors):**', '*  South American Pampas - Disturbance', '*  South American Pampas - Climate Change', '**Influences (Stressors):**', '*  South American Pampas - Native Plant Communities', '**Logic Description:** Invasive grasses can outcompete native pampas species.']
grasslands_south_american_pampas_stressors["Invasive Species"]["Impact on Area"] = 'Changes in vegetation composition.'
grasslands_south_american_pampas_stressors["Invasive Species"]["Impact on Biodiversity"] = '* Competition.\n* Altered processes.\n**Influenced By (Stressors):**\n*  South American Pampas - Disturbance\n*  South American Pampas - Climate Change\n**Influences (Stressors):**\n*  South American Pampas - Native Plant Communities\n**Logic Description:** Invasive grasses can outcompete native pampas species.'
grasslands_south_american_pampas_stressors["Invasive Species"]["Influenced By"] = ['*  South American Pampas - Disturbance', '*  South American Pampas - Climate Change', '**Influences (Stressors):**', '*  South American Pampas - Native Plant Communities', '**Logic Description:** Invasive grasses can outcompete native pampas species.']
grasslands_south_american_pampas_stressors["Invasive Species"]["Influences"] = ['*  South American Pampas - Native Plant Communities', '**Logic Description:** Invasive grasses can outcompete native pampas species.']
grasslands_south_american_pampas_stressors["Invasive Species"]["Logic Description"] = '---'
grasslands_south_american_pampas_stressors["Invasive Species"]["Impact Function"] = "impact_invasive_species_grasslands_south_american_pampas"

