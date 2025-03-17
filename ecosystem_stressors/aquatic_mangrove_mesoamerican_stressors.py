from stressor_templates import *
import copy

aquatic_mangrove_mesoamerican_stressors = {
    "Coastal Development": {},
    "Pollution": copy.deepcopy(pollution_template),
    "Climate Change": copy.deepcopy(climate_change_template),
}

# --- Coastal Development ---
aquatic_mangrove_mesoamerican_stressors["Coastal Development"]["Metric"] = 'Area of mangroves converted to tourism infrastructure, urban areas, or aquaculture (ha/year).'
aquatic_mangrove_mesoamerican_stressors["Coastal Development"]["Data Sources"] = ['Remote sensing data.', 'Government statistics (Mexico, Belize, Guatemala, Honduras).', 'Reports from conservation organizations.', '**Impact on Area:** *Major* loss of mangrove habitat; fragmentation.', '**Impact on Biodiversity:**', 'Loss of habitat.', 'Reduced nursery grounds for fish.', 'Loss of coastal protection.', '**Influenced By (Stressors):**', 'Tourism Development: A *major* driver, particularly in areas like the Riviera Maya.', 'Aquaculture Expansion: Shrimp farming.', 'Population Growth.', 'Government Policies.', '**Influences (Stressors):**', 'Coastal Erosion.', 'Water Quality.', '**Logic Description:** Coastal development, particularly for tourism and aquaculture, is a *dominant* threat to Mesoamerican mangroves, leading to significant habitat loss.']
aquatic_mangrove_mesoamerican_stressors["Coastal Development"]["Impact on Area"] = '*Major* loss of mangrove habitat; fragmentation.'
aquatic_mangrove_mesoamerican_stressors["Coastal Development"]["Impact on Biodiversity"] = 'Loss of habitat.\nReduced nursery grounds for fish.\nLoss of coastal protection.\n**Influenced By (Stressors):**\nTourism Development: A *major* driver, particularly in areas like the Riviera Maya.\nAquaculture Expansion: Shrimp farming.\nPopulation Growth.\nGovernment Policies.\n**Influences (Stressors):**\nCoastal Erosion.\nWater Quality.\n**Logic Description:** Coastal development, particularly for tourism and aquaculture, is a *dominant* threat to Mesoamerican mangroves, leading to significant habitat loss.'
aquatic_mangrove_mesoamerican_stressors["Coastal Development"]["Influenced By"] = ['Tourism Development: A *major* driver, particularly in areas like the Riviera Maya.', 'Aquaculture Expansion: Shrimp farming.', 'Population Growth.', 'Government Policies.', '**Influences (Stressors):**', 'Coastal Erosion.', 'Water Quality.', '**Logic Description:** Coastal development, particularly for tourism and aquaculture, is a *dominant* threat to Mesoamerican mangroves, leading to significant habitat loss.']
aquatic_mangrove_mesoamerican_stressors["Coastal Development"]["Influences"] = ['Coastal Erosion.', 'Water Quality.', '**Logic Description:** Coastal development, particularly for tourism and aquaculture, is a *dominant* threat to Mesoamerican mangroves, leading to significant habitat loss.']
aquatic_mangrove_mesoamerican_stressors["Coastal Development"]["Logic Description"] = '---'

# --- Pollution ---
aquatic_mangrove_mesoamerican_stressors["Pollution"]["Metric"] = 'Concentrations of pollutants (nutrients, pesticides, etc.) in water and sediments.'
aquatic_mangrove_mesoamerican_stressors["Pollution"]["Data Sources"] = ['Water quality monitoring data (often limited).', 'Research studies.', '**Impact on Area:** Water quality degradation.', '**Impact on Biodiversity:**', 'Impacts on mangroves and associated fauna.', 'Eutrophication.', '**Influenced By (Stressors):**', 'Agricultural Runoff.', 'Urban Runoff.', 'Tourism Activities.', 'Inadequate Wastewater Treatment.', '**Influences (Stressors):**', 'Water Quality.', 'Mangrove Health.', '**Logic Description:** Pollution from agriculture, urban areas, and tourism degrades water quality and impacts mangrove ecosystems.']
aquatic_mangrove_mesoamerican_stressors["Pollution"]["Impact on Area"] = 'Water quality degradation.'
aquatic_mangrove_mesoamerican_stressors["Pollution"]["Impact on Biodiversity"] = 'Impacts on mangroves and associated fauna.\nEutrophication.\n**Influenced By (Stressors):**\nAgricultural Runoff.\nUrban Runoff.\nTourism Activities.\nInadequate Wastewater Treatment.\n**Influences (Stressors):**\nWater Quality.\nMangrove Health.\n**Logic Description:** Pollution from agriculture, urban areas, and tourism degrades water quality and impacts mangrove ecosystems.'
aquatic_mangrove_mesoamerican_stressors["Pollution"]["Influenced By"] = ['Agricultural Runoff.', 'Urban Runoff.', 'Tourism Activities.', 'Inadequate Wastewater Treatment.', '**Influences (Stressors):**', 'Water Quality.', 'Mangrove Health.', '**Logic Description:** Pollution from agriculture, urban areas, and tourism degrades water quality and impacts mangrove ecosystems.']
aquatic_mangrove_mesoamerican_stressors["Pollution"]["Influences"] = ['Water Quality.', 'Mangrove Health.', '**Logic Description:** Pollution from agriculture, urban areas, and tourism degrades water quality and impacts mangrove ecosystems.']
aquatic_mangrove_mesoamerican_stressors["Pollution"]["Logic Description"] = '---'

# --- Climate Change ---
aquatic_mangrove_mesoamerican_stressors["Climate Change"]["Metric"] = 'Sea level rise; temperature increase; storm intensity.'
aquatic_mangrove_mesoamerican_stressors["Climate Change"]["Data Sources"] = ['* Climate Models', '* Historical records', '**Impact on Area:** Inundation; erosion; storm damage.', '**Impact on Biodiversity:**', '* Species shifts', '* Increased Stress', '**Influenced By (Stressors):**', '* Global GHG', '**Influences (Stressors):**', '* Sea Level Rise', '* Storm Surge', '**Logic Description:** Climate change, particularly sea level rise and increased storm intensity, poses a significant threat.']
aquatic_mangrove_mesoamerican_stressors["Climate Change"]["Impact on Area"] = 'Inundation; erosion; storm damage.'
aquatic_mangrove_mesoamerican_stressors["Climate Change"]["Impact on Biodiversity"] = '* Species shifts\n* Increased Stress\n**Influenced By (Stressors):**\n* Global GHG\n**Influences (Stressors):**\n* Sea Level Rise\n* Storm Surge\n**Logic Description:** Climate change, particularly sea level rise and increased storm intensity, poses a significant threat.'
aquatic_mangrove_mesoamerican_stressors["Climate Change"]["Influenced By"] = ['* Global GHG', '**Influences (Stressors):**', '* Sea Level Rise', '* Storm Surge', '**Logic Description:** Climate change, particularly sea level rise and increased storm intensity, poses a significant threat.']
aquatic_mangrove_mesoamerican_stressors["Climate Change"]["Influences"] = ['* Sea Level Rise', '* Storm Surge', '**Logic Description:** Climate change, particularly sea level rise and increased storm intensity, poses a significant threat.']
aquatic_mangrove_mesoamerican_stressors["Climate Change"]["Logic Description"] = '---'

