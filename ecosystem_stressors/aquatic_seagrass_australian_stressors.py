from stressor_templates import *
import copy

aquatic_seagrass_australian_stressors = {
    "Climate Change": copy.deepcopy(climate_change_template),
    "Water Quality Degradation": {},
    "Physical Damage": {},
}

# --- Climate Change ---
aquatic_seagrass_australian_stressors["Climate Change"]["Metric"] = 'Sea surface temperature (°C); frequency and severity of marine heatwaves; ocean acidification (pH); sea level rise.'
aquatic_seagrass_australian_stressors["Climate Change"]["Data Sources"] = ['Australian Bureau of Meteorology (BOM).', 'CSIRO (Commonwealth Scientific and Industrial Research Organisation).', 'Climate models.', 'Research publications.', '**Impact on Area:** Seagrass die-offs (have occurred during marine heatwaves); changes in seagrass distribution.', '**Impact on Biodiversity:**', 'Loss of habitat.', 'Shifts in species composition.', 'Increased vulnerability to other stressors.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Marine Heatwaves (a primary driver of recent die-offs).', 'Ocean Acidification.', 'Sea Level Rise.', '**Logic Description:** Climate change, particularly marine heatwaves, has caused significant seagrass die-offs in parts of Australia. Ocean acidification and sea level rise are also long-term threats.']
aquatic_seagrass_australian_stressors["Climate Change"]["Impact on Area"] = 'Seagrass die-offs (have occurred during marine heatwaves); changes in seagrass distribution.'
aquatic_seagrass_australian_stressors["Climate Change"]["Impact on Biodiversity"] = 'Loss of habitat.\nShifts in species composition.\nIncreased vulnerability to other stressors.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\n**Influences (Stressors):**\nMarine Heatwaves (a primary driver of recent die-offs).\nOcean Acidification.\nSea Level Rise.\n**Logic Description:** Climate change, particularly marine heatwaves, has caused significant seagrass die-offs in parts of Australia. Ocean acidification and sea level rise are also long-term threats.'
aquatic_seagrass_australian_stressors["Climate Change"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Marine Heatwaves (a primary driver of recent die-offs).', 'Ocean Acidification.', 'Sea Level Rise.', '**Logic Description:** Climate change, particularly marine heatwaves, has caused significant seagrass die-offs in parts of Australia. Ocean acidification and sea level rise are also long-term threats.']
aquatic_seagrass_australian_stressors["Climate Change"]["Influences"] = ['Marine Heatwaves (a primary driver of recent die-offs).', 'Ocean Acidification.', 'Sea Level Rise.', '**Logic Description:** Climate change, particularly marine heatwaves, has caused significant seagrass die-offs in parts of Australia. Ocean acidification and sea level rise are also long-term threats.']
aquatic_seagrass_australian_stressors["Climate Change"]["Logic Description"] = '---'

# --- Water Quality Degradation ---
aquatic_seagrass_australian_stressors["Water Quality Degradation"]["Metric"] = 'Water clarity (turbidity); nutrient concentrations; concentrations of other pollutants.'
aquatic_seagrass_australian_stressors["Water Quality Degradation"]["Data Sources"] = ['State government environmental monitoring programs (e.g., Queensland, Western Australia).', 'Research studies (e.g., from universities, CSIRO).', '**Impact on Area:** Reduced light penetration; stress on seagrasses.', '**Impact on Biodiversity:**', 'Reduced seagrass growth and survival.', 'Algal blooms.', '**Influenced By (Stressors):**', 'Agricultural Runoff: Nutrients and sediments.', 'Urban Runoff: Pollutants and sediments.', 'Coastal Development.', 'Dredging.', '**Influences (Stressors):**', 'Light Availability.', 'Seagrass Health.', '**Logic Description:** Reduced water quality, due to runoff from agriculture, urban areas, and coastal development, is a significant threat to Australian seagrass meadows.']
aquatic_seagrass_australian_stressors["Water Quality Degradation"]["Impact on Area"] = 'Reduced light penetration; stress on seagrasses.'
aquatic_seagrass_australian_stressors["Water Quality Degradation"]["Impact on Biodiversity"] = 'Reduced seagrass growth and survival.\nAlgal blooms.\n**Influenced By (Stressors):**\nAgricultural Runoff: Nutrients and sediments.\nUrban Runoff: Pollutants and sediments.\nCoastal Development.\nDredging.\n**Influences (Stressors):**\nLight Availability.\nSeagrass Health.\n**Logic Description:** Reduced water quality, due to runoff from agriculture, urban areas, and coastal development, is a significant threat to Australian seagrass meadows.'
aquatic_seagrass_australian_stressors["Water Quality Degradation"]["Influenced By"] = ['Agricultural Runoff: Nutrients and sediments.', 'Urban Runoff: Pollutants and sediments.', 'Coastal Development.', 'Dredging.', '**Influences (Stressors):**', 'Light Availability.', 'Seagrass Health.', '**Logic Description:** Reduced water quality, due to runoff from agriculture, urban areas, and coastal development, is a significant threat to Australian seagrass meadows.']
aquatic_seagrass_australian_stressors["Water Quality Degradation"]["Influences"] = ['Light Availability.', 'Seagrass Health.', '**Logic Description:** Reduced water quality, due to runoff from agriculture, urban areas, and coastal development, is a significant threat to Australian seagrass meadows.']
aquatic_seagrass_australian_stressors["Water Quality Degradation"]["Logic Description"] = '---'

# --- Physical Damage ---
aquatic_seagrass_australian_stressors["Physical Damage"]["Metric"] = 'Area damaged'
aquatic_seagrass_australian_stressors["Physical Damage"]["Data Sources"] = ['* Research', '* Monitoring', '**Impact on Area:** Localized loss and fragmentation', '**Impact on Biodiversity:**', '* Habitat loss', '**Influenced By (Stressors):**', '* Coastal development, boating, dredging', '**Influences (Stressors):**', '* Habitat Fragmentation', '**Logic Description:** Physical damage.']
aquatic_seagrass_australian_stressors["Physical Damage"]["Impact on Area"] = 'Localized loss and fragmentation'
aquatic_seagrass_australian_stressors["Physical Damage"]["Impact on Biodiversity"] = '* Habitat loss\n**Influenced By (Stressors):**\n* Coastal development, boating, dredging\n**Influences (Stressors):**\n* Habitat Fragmentation\n**Logic Description:** Physical damage.'
aquatic_seagrass_australian_stressors["Physical Damage"]["Influenced By"] = ['* Coastal development, boating, dredging', '**Influences (Stressors):**', '* Habitat Fragmentation', '**Logic Description:** Physical damage.']
aquatic_seagrass_australian_stressors["Physical Damage"]["Influences"] = ['* Habitat Fragmentation', '**Logic Description:** Physical damage.']
aquatic_seagrass_australian_stressors["Physical Damage"]["Logic Description"] = '---'

