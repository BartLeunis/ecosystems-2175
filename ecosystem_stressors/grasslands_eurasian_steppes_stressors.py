from stressor_templates import *
import copy

grasslands_eurasian_steppes_stressors = {
    "Land-Use Change": {},
    "Habitat Fragmentation": {},
    "Climate Change": copy.deepcopy(climate_change_template),
    "Overgrazing": {},
    "Wildfires": copy.deepcopy(fire_regime_template),
    "Invasive Species": copy.deepcopy(invasive_species_template),
}

# --- Land-Use Change ---
grasslands_eurasian_steppes_stressors["Land-Use Change"]["Metric"] = 'Area converted to agriculture, settlements, or other land uses (ha/year).'
grasslands_eurasian_steppes_stressors["Land-Use Change"]["Data Sources"] = ['Remote sensing data.', 'National government statistics (various countries across Eurasia).', 'Research publications.', '**Impact on Area:** Loss of steppe habitat; fragmentation.', '**Impact on Biodiversity:**', 'Habitat loss and fragmentation.', 'Decline of steppe-dependent species.', '**Influenced By (Stressors):**', '* Eurasian Steppes - Agricultural Expansion', '* Eurasian Steppes - Population Growth', '* Eurasian Steppes - Government Policies', '**Influences (Stressors):**', '*  Eurasian Steppes - Habitat Fragmentation', '**Logic Description:** Conversion of steppe to agriculture, particularly large-scale agriculture, is a major threat, leading to habitat loss and fragmentation.']
grasslands_eurasian_steppes_stressors["Land-Use Change"]["Impact on Area"] = 'Loss of steppe habitat; fragmentation.'
grasslands_eurasian_steppes_stressors["Land-Use Change"]["Impact on Biodiversity"] = 'Habitat loss and fragmentation.\nDecline of steppe-dependent species.\n**Influenced By (Stressors):**\n* Eurasian Steppes - Agricultural Expansion\n* Eurasian Steppes - Population Growth\n* Eurasian Steppes - Government Policies\n**Influences (Stressors):**\n*  Eurasian Steppes - Habitat Fragmentation\n**Logic Description:** Conversion of steppe to agriculture, particularly large-scale agriculture, is a major threat, leading to habitat loss and fragmentation.'
grasslands_eurasian_steppes_stressors["Land-Use Change"]["Influenced By"] = ['* Eurasian Steppes - Agricultural Expansion', '* Eurasian Steppes - Population Growth', '* Eurasian Steppes - Government Policies', '**Influences (Stressors):**', '*  Eurasian Steppes - Habitat Fragmentation', '**Logic Description:** Conversion of steppe to agriculture, particularly large-scale agriculture, is a major threat, leading to habitat loss and fragmentation.']
grasslands_eurasian_steppes_stressors["Land-Use Change"]["Influences"] = ['*  Eurasian Steppes - Habitat Fragmentation', '**Logic Description:** Conversion of steppe to agriculture, particularly large-scale agriculture, is a major threat, leading to habitat loss and fragmentation.']
grasslands_eurasian_steppes_stressors["Land-Use Change"]["Logic Description"] = '---'
grasslands_eurasian_steppes_stressors["Land-Use Change"]["Impact Function"] = "impact_land_use_change_grasslands_eurasian_steppes"

# --- Habitat Fragmentation ---
grasslands_eurasian_steppes_stressors["Habitat Fragmentation"]["Metric"] = 'Patch size distribution; edge density; connectivity indices.'
grasslands_eurasian_steppes_stressors["Habitat Fragmentation"]["Data Sources"] = ['Land cover data (from remote sensing).', 'GIS analysis.', '**Impact on Area:** Remaining steppe exists in increasingly isolated patches.', '**Impact on Biodiversity:**', 'Reduced gene flow.', 'Increased edge effects.', 'Limited dispersal ability.', 'Increased vulnerability to stochastic events.', '**Influenced By (Stressors):**', 'Eurasian Steppes - Land-Use Change', '**Influences (Stressors):**', '* Exacerbates impacts of other stressors', '**Logic Description:** Fragmentation isolates steppe patches, reducing their ecological viability.']
grasslands_eurasian_steppes_stressors["Habitat Fragmentation"]["Impact on Area"] = 'Remaining steppe exists in increasingly isolated patches.'
grasslands_eurasian_steppes_stressors["Habitat Fragmentation"]["Impact on Biodiversity"] = 'Reduced gene flow.\nIncreased edge effects.\nLimited dispersal ability.\nIncreased vulnerability to stochastic events.\n**Influenced By (Stressors):**\nEurasian Steppes - Land-Use Change\n**Influences (Stressors):**\n* Exacerbates impacts of other stressors\n**Logic Description:** Fragmentation isolates steppe patches, reducing their ecological viability.'
grasslands_eurasian_steppes_stressors["Habitat Fragmentation"]["Influenced By"] = ['Eurasian Steppes - Land-Use Change', '**Influences (Stressors):**', '* Exacerbates impacts of other stressors', '**Logic Description:** Fragmentation isolates steppe patches, reducing their ecological viability.']
grasslands_eurasian_steppes_stressors["Habitat Fragmentation"]["Influences"] = ['* Exacerbates impacts of other stressors', '**Logic Description:** Fragmentation isolates steppe patches, reducing their ecological viability.']
grasslands_eurasian_steppes_stressors["Habitat Fragmentation"]["Logic Description"] = '---'
grasslands_eurasian_steppes_stressors["Habitat Fragmentation"]["Impact Function"] = "impact_habitat_fragmentation_grasslands_eurasian_steppes"

# --- Climate Change ---
grasslands_eurasian_steppes_stressors["Climate Change"]["Metric"] = 'Temperature increase (°C); changes in precipitation (mm/year, seasonality); increased frequency and severity of drought.'
grasslands_eurasian_steppes_stressors["Climate Change"]["Data Sources"] = ['* Climate models.', '* Historical data.', '**Impact on Area:** Indirect; changes in growing conditions.', '**Impact on Biodiversity:**', 'Shifts in species distributions.', 'Increased stress on steppe species.', 'Changes in phenology.', 'Increased fire risk (in some areas).', 'Desertification (in some areas).', '**Influenced By (Stressors):**', '* Global GHG', '**Influences (Stressors):**', '*  Eurasian Steppes - Fire Regimes', '*  Eurasian Steppes - Water Availability.', '**Logic Description:** Climate change is altering temperature and precipitation patterns, increasing aridity and the risk of desertification in some areas.']
grasslands_eurasian_steppes_stressors["Climate Change"]["Impact on Area"] = 'Indirect; changes in growing conditions.'
grasslands_eurasian_steppes_stressors["Climate Change"]["Impact on Biodiversity"] = 'Shifts in species distributions.\nIncreased stress on steppe species.\nChanges in phenology.\nIncreased fire risk (in some areas).\nDesertification (in some areas).\n**Influenced By (Stressors):**\n* Global GHG\n**Influences (Stressors):**\n*  Eurasian Steppes - Fire Regimes\n*  Eurasian Steppes - Water Availability.\n**Logic Description:** Climate change is altering temperature and precipitation patterns, increasing aridity and the risk of desertification in some areas.'
grasslands_eurasian_steppes_stressors["Climate Change"]["Influenced By"] = ['* Global GHG', '**Influences (Stressors):**', '*  Eurasian Steppes - Fire Regimes', '*  Eurasian Steppes - Water Availability.', '**Logic Description:** Climate change is altering temperature and precipitation patterns, increasing aridity and the risk of desertification in some areas.']
grasslands_eurasian_steppes_stressors["Climate Change"]["Influences"] = ['*  Eurasian Steppes - Fire Regimes', '*  Eurasian Steppes - Water Availability.', '**Logic Description:** Climate change is altering temperature and precipitation patterns, increasing aridity and the risk of desertification in some areas.']
grasslands_eurasian_steppes_stressors["Climate Change"]["Logic Description"] = '---'
grasslands_eurasian_steppes_stressors["Climate Change"]["Impact Function"] = "impact_climate_change_grasslands_eurasian_steppes"

# --- Overgrazing ---
grasslands_eurasian_steppes_stressors["Overgrazing"]["Metric"] = 'Livestock density; vegetation cover and composition; soil erosion.'
grasslands_eurasian_steppes_stressors["Overgrazing"]["Data Sources"] = ['* Agricultural Statistics', '* Vegetation surveys', '* Remote sensing', '**Impact on Area:** Changes in vegetation structure; soil degradation.', '**Impact on Biodiversity:**', '* Loss of palatable species', '* Soil Compaction', '* Spread of unpalatable plants.', '**Influenced By (Stressors):**', '*  Eurasian Steppes - Livestock Management', '**Influences (Stressors):**', '*  Eurasian Steppes - Vegetation Changes', '*  Eurasian Steppes - Desertification (in extreme cases).', '**Logic Description:** Overgrazing by livestock is a widespread problem, leading to vegetation degradation and soil erosion.']
grasslands_eurasian_steppes_stressors["Overgrazing"]["Impact on Area"] = 'Changes in vegetation structure; soil degradation.'
grasslands_eurasian_steppes_stressors["Overgrazing"]["Impact on Biodiversity"] = '* Loss of palatable species\n* Soil Compaction\n* Spread of unpalatable plants.\n**Influenced By (Stressors):**\n*  Eurasian Steppes - Livestock Management\n**Influences (Stressors):**\n*  Eurasian Steppes - Vegetation Changes\n*  Eurasian Steppes - Desertification (in extreme cases).\n**Logic Description:** Overgrazing by livestock is a widespread problem, leading to vegetation degradation and soil erosion.'
grasslands_eurasian_steppes_stressors["Overgrazing"]["Influenced By"] = ['*  Eurasian Steppes - Livestock Management', '**Influences (Stressors):**', '*  Eurasian Steppes - Vegetation Changes', '*  Eurasian Steppes - Desertification (in extreme cases).', '**Logic Description:** Overgrazing by livestock is a widespread problem, leading to vegetation degradation and soil erosion.']
grasslands_eurasian_steppes_stressors["Overgrazing"]["Influences"] = ['*  Eurasian Steppes - Vegetation Changes', '*  Eurasian Steppes - Desertification (in extreme cases).', '**Logic Description:** Overgrazing by livestock is a widespread problem, leading to vegetation degradation and soil erosion.']
grasslands_eurasian_steppes_stressors["Overgrazing"]["Logic Description"] = '---'
grasslands_eurasian_steppes_stressors["Overgrazing"]["Impact Function"] = "impact_overgrazing_grasslands_eurasian_steppes"

# --- Wildfires ---
grasslands_eurasian_steppes_stressors["Wildfires"]["Metric"] = 'Fire frequency; area burned (ha/year).'
grasslands_eurasian_steppes_stressors["Wildfires"]["Data Sources"] = ['Remote sensing data.', 'Government statistics (various countries).', '**Impact on Area:** Changes in vegetation structure and composition.', '**Impact on Biodiversity:**', '* Can be beneficial for some steppe species if fire regimes are natural, but increased frequency or intensity due to climate change or human activities can be detrimental.', '**Influenced By (Stressors):**', '*  Eurasian Steppes - Climate Change', '* Human activities.', '**Influences (Stressors):**', '*  Eurasian Steppes - Vegetation Structure.', '**Logic Description:** Changes in fire regimes, often linked to human activities and climate change, can impact steppe ecosystems.']
grasslands_eurasian_steppes_stressors["Wildfires"]["Impact on Area"] = 'Changes in vegetation structure and composition.'
grasslands_eurasian_steppes_stressors["Wildfires"]["Impact on Biodiversity"] = '* Can be beneficial for some steppe species if fire regimes are natural, but increased frequency or intensity due to climate change or human activities can be detrimental.\n**Influenced By (Stressors):**\n*  Eurasian Steppes - Climate Change\n* Human activities.\n**Influences (Stressors):**\n*  Eurasian Steppes - Vegetation Structure.\n**Logic Description:** Changes in fire regimes, often linked to human activities and climate change, can impact steppe ecosystems.'
grasslands_eurasian_steppes_stressors["Wildfires"]["Influenced By"] = ['*  Eurasian Steppes - Climate Change', '* Human activities.', '**Influences (Stressors):**', '*  Eurasian Steppes - Vegetation Structure.', '**Logic Description:** Changes in fire regimes, often linked to human activities and climate change, can impact steppe ecosystems.']
grasslands_eurasian_steppes_stressors["Wildfires"]["Influences"] = ['*  Eurasian Steppes - Vegetation Structure.', '**Logic Description:** Changes in fire regimes, often linked to human activities and climate change, can impact steppe ecosystems.']
grasslands_eurasian_steppes_stressors["Wildfires"]["Logic Description"] = '---'
grasslands_eurasian_steppes_stressors["Wildfires"]["Impact Function"] = "impact_wildfires_grasslands_eurasian_steppes"

# --- Invasive Species ---
grasslands_eurasian_steppes_stressors["Invasive Species"]["Metric"] = 'Distribution and abundance of key invasive species.'
grasslands_eurasian_steppes_stressors["Invasive Species"]["Data Sources"] = ['Vegetation surveys.', 'Research studies.', '**Impact on Area:** Changes in vegetation composition.', '**Impact on Biodiversity:**', '* Competition', '* Altered processes', '**Influenced By (Stressors):**', '*  Eurasian Steppes - Disturbance', '*  Eurasian Steppes - Climate Change', '**Influences (Stressors):**', '*  Eurasian Steppes - Native Communities', '**Logic Description:** Invasive species impacts.']
grasslands_eurasian_steppes_stressors["Invasive Species"]["Impact on Area"] = 'Changes in vegetation composition.'
grasslands_eurasian_steppes_stressors["Invasive Species"]["Impact on Biodiversity"] = '* Competition\n* Altered processes\n**Influenced By (Stressors):**\n*  Eurasian Steppes - Disturbance\n*  Eurasian Steppes - Climate Change\n**Influences (Stressors):**\n*  Eurasian Steppes - Native Communities\n**Logic Description:** Invasive species impacts.'
grasslands_eurasian_steppes_stressors["Invasive Species"]["Influenced By"] = ['*  Eurasian Steppes - Disturbance', '*  Eurasian Steppes - Climate Change', '**Influences (Stressors):**', '*  Eurasian Steppes - Native Communities', '**Logic Description:** Invasive species impacts.']
grasslands_eurasian_steppes_stressors["Invasive Species"]["Influences"] = ['*  Eurasian Steppes - Native Communities', '**Logic Description:** Invasive species impacts.']
grasslands_eurasian_steppes_stressors["Invasive Species"]["Logic Description"] = '---'
grasslands_eurasian_steppes_stressors["Invasive Species"]["Impact Function"] = "impact_invasive_species_grasslands_eurasian_steppes"

