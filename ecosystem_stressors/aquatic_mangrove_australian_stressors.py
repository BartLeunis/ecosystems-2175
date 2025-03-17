from stressor_templates import *
import copy

aquatic_mangrove_australian_stressors = {
    "Climate Change": copy.deepcopy(climate_change_template),
    "Coastal Development": {},
    "Pollution": copy.deepcopy(pollution_template),
}

# --- Climate Change ---
aquatic_mangrove_australian_stressors["Climate Change"]["Metric"] = 'Sea level rise (mm/year); sea surface temperature (°C); changes in precipitation patterns; increased storm intensity.'
aquatic_mangrove_australian_stressors["Climate Change"]["Data Sources"] = ['Australian Bureau of Meteorology (BOM).', 'CSIRO (Commonwealth Scientific and Industrial Research Organisation).', 'Climate models.', 'Tide gauge records.', 'Research publications.', '**Impact on Area:**', 'Coastal inundation and erosion due to sea level rise.', 'Changes in salinity due to altered freshwater input.', 'Increased damage from storms.', '**Impact on Biodiversity:**', 'Shifts in mangrove species distributions.', 'Increased stress on mangroves.', 'Loss of mangrove habitat due to sea level rise.', 'Changes in phenology.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Sea Level Rise.', 'Coastal Erosion.', 'Storm Surge.', '**Logic Description:** Climate change, particularly sea level rise, poses a *major* threat to Australian mangroves. Increased storm intensity and changes in rainfall patterns also have impacts.']
aquatic_mangrove_australian_stressors["Climate Change"]["Impact on Area"] = ''
aquatic_mangrove_australian_stressors["Climate Change"]["Impact on Biodiversity"] = 'Shifts in mangrove species distributions.\nIncreased stress on mangroves.\nLoss of mangrove habitat due to sea level rise.\nChanges in phenology.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\n**Influences (Stressors):**\nSea Level Rise.\nCoastal Erosion.\nStorm Surge.\n**Logic Description:** Climate change, particularly sea level rise, poses a *major* threat to Australian mangroves. Increased storm intensity and changes in rainfall patterns also have impacts.'
aquatic_mangrove_australian_stressors["Climate Change"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Sea Level Rise.', 'Coastal Erosion.', 'Storm Surge.', '**Logic Description:** Climate change, particularly sea level rise, poses a *major* threat to Australian mangroves. Increased storm intensity and changes in rainfall patterns also have impacts.']
aquatic_mangrove_australian_stressors["Climate Change"]["Influences"] = ['Sea Level Rise.', 'Coastal Erosion.', 'Storm Surge.', '**Logic Description:** Climate change, particularly sea level rise, poses a *major* threat to Australian mangroves. Increased storm intensity and changes in rainfall patterns also have impacts.']
aquatic_mangrove_australian_stressors["Climate Change"]["Logic Description"] = '---'
aquatic_mangrove_australian_stressors["Climate Change"]["Impact Function"] = "impact_climate_change_aquatic_mangrove_australian"

# --- Coastal Development ---
aquatic_mangrove_australian_stressors["Coastal Development"]["Metric"] = 'Area converted'
aquatic_mangrove_australian_stressors["Coastal Development"]["Data Sources"] = ['* Remote sensing', '* Government statistics', '**Impact on Area:** Loss of habitat and fragmentation', '**Impact on Biodiversity:**', '* Habitat Loss', '**Influenced By (Stressors):**', '* Urban expansion', '* Infrastructure', '**Influences (Stressors):**', '* Habitat Fragmentation', '**Logic Description:** Coastal development is a pressure.']
aquatic_mangrove_australian_stressors["Coastal Development"]["Impact on Area"] = 'Loss of habitat and fragmentation'
aquatic_mangrove_australian_stressors["Coastal Development"]["Impact on Biodiversity"] = '* Habitat Loss\n**Influenced By (Stressors):**\n* Urban expansion\n* Infrastructure\n**Influences (Stressors):**\n* Habitat Fragmentation\n**Logic Description:** Coastal development is a pressure.'
aquatic_mangrove_australian_stressors["Coastal Development"]["Influenced By"] = ['* Urban expansion', '* Infrastructure', '**Influences (Stressors):**', '* Habitat Fragmentation', '**Logic Description:** Coastal development is a pressure.']
aquatic_mangrove_australian_stressors["Coastal Development"]["Influences"] = ['* Habitat Fragmentation', '**Logic Description:** Coastal development is a pressure.']
aquatic_mangrove_australian_stressors["Coastal Development"]["Logic Description"] = '---'
aquatic_mangrove_australian_stressors["Coastal Development"]["Impact Function"] = "impact_coastal_development_aquatic_mangrove_australian"

# --- Pollution ---
aquatic_mangrove_australian_stressors["Pollution"]["Metric"] = 'Concentrations of pollutants.'
aquatic_mangrove_australian_stressors["Pollution"]["Data Sources"] = ['Water quality monitoring programs.', 'Research studies.', '**Impact on Area:** Water quality degradation', '**Impact on Biodiversity:** Impacts mangroves and associated species.', '**Influenced By (Stressors):**', '* Agricultural, urban, and industrial runoff', '**Influences (Stressors):**', '* Mangrove Health', '**Logic Description:** Runoff a concern in some areas.']
aquatic_mangrove_australian_stressors["Pollution"]["Impact on Area"] = 'Water quality degradation'
aquatic_mangrove_australian_stressors["Pollution"]["Impact on Biodiversity"] = '**Influenced By (Stressors):**\n* Agricultural, urban, and industrial runoff\n**Influences (Stressors):**\n* Mangrove Health\n**Logic Description:** Runoff a concern in some areas.'
aquatic_mangrove_australian_stressors["Pollution"]["Influenced By"] = ['* Agricultural, urban, and industrial runoff', '**Influences (Stressors):**', '* Mangrove Health', '**Logic Description:** Runoff a concern in some areas.']
aquatic_mangrove_australian_stressors["Pollution"]["Influences"] = ['* Mangrove Health', '**Logic Description:** Runoff a concern in some areas.']
aquatic_mangrove_australian_stressors["Pollution"]["Logic Description"] = '---'
aquatic_mangrove_australian_stressors["Pollution"]["Impact Function"] = "impact_pollution_aquatic_mangrove_australian"

