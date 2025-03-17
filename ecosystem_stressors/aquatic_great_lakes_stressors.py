from stressor_templates import *
import copy

aquatic_great_lakes_stressors = {
    "Invasive Species": copy.deepcopy(invasive_species_template),
    "Eutrophication": {},
    "Legacy Pollutants": {},
    "Climate Change": copy.deepcopy(climate_change_template),
}

# --- Invasive Species ---
aquatic_great_lakes_stressors["Invasive Species"]["Metric"] = 'Distribution and abundance of key invasive species (e.g., zebra mussels, quagga mussels, sea lamprey, round goby, alewife).'
aquatic_great_lakes_stressors["Invasive Species"]["Data Sources"] = ['US Geological Survey (USGS) Great Lakes Science Center.', 'US Environmental Protection Agency (EPA) Great Lakes National Program Office.', 'Fisheries and Oceans Canada.', 'Great Lakes Fishery Commission.', 'State and provincial agencies.', 'University research programs.', '**Impact on Area:** Widespread impacts throughout the Great Lakes ecosystem.', '**Impact on Biodiversity:**', 'Zebra and quagga mussels: Filter vast amounts of water, altering the base of the food web, increasing water clarity (but reducing food for some species), and fouling infrastructure.', 'Sea lamprey: Parasitic on lake trout and other fish, causing significant mortality.', 'Round goby: Competes with native fish for food and habitat.', 'Alewife: Disrupts food webs; large die-offs can cause problems.', '**Influenced By (Stressors):**', 'Ballast Water Discharge: From transoceanic ships (historically the major pathway).', 'Canals and Waterways: Connecting the Great Lakes to other water bodies.', '**Influences (Stressors):**', 'Native Fish Populations.', 'Water Quality (in some cases, e.g., increased clarity due to mussels).', 'Food Web Structure.', '**Logic Description:** Invasive species, introduced primarily through ballast water from ships, have had *profound* and cascading impacts on the Great Lakes ecosystem, altering food webs, impacting native species, and causing economic damage.']
aquatic_great_lakes_stressors["Invasive Species"]["Impact on Area"] = 'Widespread impacts throughout the Great Lakes ecosystem.'
aquatic_great_lakes_stressors["Invasive Species"]["Impact on Biodiversity"] = 'Zebra and quagga mussels: Filter vast amounts of water, altering the base of the food web, increasing water clarity (but reducing food for some species), and fouling infrastructure.\nSea lamprey: Parasitic on lake trout and other fish, causing significant mortality.\nRound goby: Competes with native fish for food and habitat.\nAlewife: Disrupts food webs; large die-offs can cause problems.\n**Influenced By (Stressors):**\nBallast Water Discharge: From transoceanic ships (historically the major pathway).\nCanals and Waterways: Connecting the Great Lakes to other water bodies.\n**Influences (Stressors):**\nNative Fish Populations.\nWater Quality (in some cases, e.g., increased clarity due to mussels).\nFood Web Structure.\n**Logic Description:** Invasive species, introduced primarily through ballast water from ships, have had *profound* and cascading impacts on the Great Lakes ecosystem, altering food webs, impacting native species, and causing economic damage.'
aquatic_great_lakes_stressors["Invasive Species"]["Influenced By"] = ['Ballast Water Discharge: From transoceanic ships (historically the major pathway).', 'Canals and Waterways: Connecting the Great Lakes to other water bodies.', '**Influences (Stressors):**', 'Native Fish Populations.', 'Water Quality (in some cases, e.g., increased clarity due to mussels).', 'Food Web Structure.', '**Logic Description:** Invasive species, introduced primarily through ballast water from ships, have had *profound* and cascading impacts on the Great Lakes ecosystem, altering food webs, impacting native species, and causing economic damage.']
aquatic_great_lakes_stressors["Invasive Species"]["Influences"] = ['Native Fish Populations.', 'Water Quality (in some cases, e.g., increased clarity due to mussels).', 'Food Web Structure.', '**Logic Description:** Invasive species, introduced primarily through ballast water from ships, have had *profound* and cascading impacts on the Great Lakes ecosystem, altering food webs, impacting native species, and causing economic damage.']
aquatic_great_lakes_stressors["Invasive Species"]["Logic Description"] = '---'
aquatic_great_lakes_stressors["Invasive Species"]["Impact Function"] = "impact_invasive_species_aquatic_great_lakes"

# --- Eutrophication ---
aquatic_great_lakes_stressors["Eutrophication"]["Metric"] = 'Nutrient concentrations (phosphorus, nitrogen); chlorophyll *a*; Secchi depth; dissolved oxygen; frequency and severity of harmful algal blooms.'
aquatic_great_lakes_stressors["Eutrophication"]["Data Sources"] = ['EPA Great Lakes National Program Office.', 'Environment and Climate Change Canada.', 'State and provincial environmental agencies.', 'NOAA Great Lakes Environmental Research Laboratory (GLERL).', '**Impact on Area:** Primarily affects specific areas, like western Lake Erie, Saginaw Bay (Lake Huron), and Green Bay (Lake Michigan).', '**Impact on Biodiversity:**', 'Harmful algal blooms (HABs), including toxic cyanobacteria.', 'Oxygen depletion in bottom waters (hypoxia), creating "dead zones."', 'Loss of submerged aquatic vegetation.', 'Impacts on fish and invertebrate communities.', '**Influenced By (Stressors):**', 'Agricultural Runoff: Fertilizers and animal waste are major sources of nutrients.', 'Urban Runoff: Sewage and stormwater.', 'Climate Change: Warmer water and altered precipitation patterns can exacerbate eutrophication.', '**Influences (Stressors):**', 'Harmful Algal Blooms.', 'Oxygen Depletion.', 'Water Quality.', 'Fisheries.', '**Logic Description:** Eutrophication, particularly in certain areas of the Great Lakes (e.g., western Lake Erie), remains a significant problem, driven by nutrient pollution from agriculture and urban areas. This leads to harmful algal blooms, oxygen depletion, and impacts on aquatic life.']
aquatic_great_lakes_stressors["Eutrophication"]["Impact on Area"] = 'Primarily affects specific areas, like western Lake Erie, Saginaw Bay (Lake Huron), and Green Bay (Lake Michigan).'
aquatic_great_lakes_stressors["Eutrophication"]["Impact on Biodiversity"] = 'Harmful algal blooms (HABs), including toxic cyanobacteria.\nOxygen depletion in bottom waters (hypoxia), creating "dead zones."\nLoss of submerged aquatic vegetation.\nImpacts on fish and invertebrate communities.\n**Influenced By (Stressors):**\nAgricultural Runoff: Fertilizers and animal waste are major sources of nutrients.\nUrban Runoff: Sewage and stormwater.\nClimate Change: Warmer water and altered precipitation patterns can exacerbate eutrophication.\n**Influences (Stressors):**\nHarmful Algal Blooms.\nOxygen Depletion.\nWater Quality.\nFisheries.\n**Logic Description:** Eutrophication, particularly in certain areas of the Great Lakes (e.g., western Lake Erie), remains a significant problem, driven by nutrient pollution from agriculture and urban areas. This leads to harmful algal blooms, oxygen depletion, and impacts on aquatic life.'
aquatic_great_lakes_stressors["Eutrophication"]["Influenced By"] = ['Agricultural Runoff: Fertilizers and animal waste are major sources of nutrients.', 'Urban Runoff: Sewage and stormwater.', 'Climate Change: Warmer water and altered precipitation patterns can exacerbate eutrophication.', '**Influences (Stressors):**', 'Harmful Algal Blooms.', 'Oxygen Depletion.', 'Water Quality.', 'Fisheries.', '**Logic Description:** Eutrophication, particularly in certain areas of the Great Lakes (e.g., western Lake Erie), remains a significant problem, driven by nutrient pollution from agriculture and urban areas. This leads to harmful algal blooms, oxygen depletion, and impacts on aquatic life.']
aquatic_great_lakes_stressors["Eutrophication"]["Influences"] = ['Harmful Algal Blooms.', 'Oxygen Depletion.', 'Water Quality.', 'Fisheries.', '**Logic Description:** Eutrophication, particularly in certain areas of the Great Lakes (e.g., western Lake Erie), remains a significant problem, driven by nutrient pollution from agriculture and urban areas. This leads to harmful algal blooms, oxygen depletion, and impacts on aquatic life.']
aquatic_great_lakes_stressors["Eutrophication"]["Logic Description"] = '---'
aquatic_great_lakes_stressors["Eutrophication"]["Impact Function"] = "impact_eutrophication_aquatic_great_lakes"

# --- Legacy Pollutants ---
aquatic_great_lakes_stressors["Legacy Pollutants"]["Metric"] = 'Concentrations of persistent organic pollutants (POPs) (e.g., PCBs, DDT, mercury) in sediments, fish tissue, and wildlife.'
aquatic_great_lakes_stressors["Legacy Pollutants"]["Data Sources"] = ['EPA Great Lakes National Program Office.', 'Environment and Climate Change Canada.', 'State and provincial environmental agencies.', 'Fish consumption advisories.', '**Impact on Area:** Contamination of sediments and biota.', '**Impact on Biodiversity:**', 'Toxic effects on fish, birds, and other wildlife.', 'Bioaccumulation and biomagnification in the food chain.', 'Reproductive problems in wildlife.', '**Influenced By (Stressors):**', 'Historical Industrial Discharges: From past industrial activities.', 'Atmospheric Deposition.', '**Influences (Stressors):**', 'Wildlife Health.', 'Human Health (through consumption of contaminated fish).', '**Logic Description:**  Legacy pollutants, such as PCBs and mercury, from past industrial activities persist in the Great Lakes ecosystem, contaminating sediments and accumulating in the food chain, posing risks to wildlife and human health.']
aquatic_great_lakes_stressors["Legacy Pollutants"]["Impact on Area"] = 'Contamination of sediments and biota.'
aquatic_great_lakes_stressors["Legacy Pollutants"]["Impact on Biodiversity"] = 'Toxic effects on fish, birds, and other wildlife.\nBioaccumulation and biomagnification in the food chain.\nReproductive problems in wildlife.\n**Influenced By (Stressors):**\nHistorical Industrial Discharges: From past industrial activities.\nAtmospheric Deposition.\n**Influences (Stressors):**\nWildlife Health.\nHuman Health (through consumption of contaminated fish).\n**Logic Description:**  Legacy pollutants, such as PCBs and mercury, from past industrial activities persist in the Great Lakes ecosystem, contaminating sediments and accumulating in the food chain, posing risks to wildlife and human health.'
aquatic_great_lakes_stressors["Legacy Pollutants"]["Influenced By"] = ['Historical Industrial Discharges: From past industrial activities.', 'Atmospheric Deposition.', '**Influences (Stressors):**', 'Wildlife Health.', 'Human Health (through consumption of contaminated fish).', '**Logic Description:**  Legacy pollutants, such as PCBs and mercury, from past industrial activities persist in the Great Lakes ecosystem, contaminating sediments and accumulating in the food chain, posing risks to wildlife and human health.']
aquatic_great_lakes_stressors["Legacy Pollutants"]["Influences"] = ['Wildlife Health.', 'Human Health (through consumption of contaminated fish).', '**Logic Description:**  Legacy pollutants, such as PCBs and mercury, from past industrial activities persist in the Great Lakes ecosystem, contaminating sediments and accumulating in the food chain, posing risks to wildlife and human health.']
aquatic_great_lakes_stressors["Legacy Pollutants"]["Logic Description"] = '---'
aquatic_great_lakes_stressors["Legacy Pollutants"]["Impact Function"] = "impact_legacy_pollutants_aquatic_great_lakes"

# --- Climate Change ---
aquatic_great_lakes_stressors["Climate Change"]["Metric"] = 'Water temperature; ice cover duration; water levels; frequency and intensity of storms.'
aquatic_great_lakes_stressors["Climate Change"]["Data Sources"] = ['NOAA GLERL.', 'Environment and Climate Change Canada.', 'Climate models.', '**Impact on Area:** Changes in thermal structure; altered water levels; changes in ice cover.', '**Impact on Biodiversity:**', 'Shifts in fish species distributions.', 'Impacts on spawning and recruitment.', 'Increased stress on cold-water species.', 'Changes in the timing of biological events.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Eutrophication (warmer water can exacerbate nutrient problems).', 'Invasive Species (some may benefit from warmer waters).', 'Water Levels.', '**Logic Description:** Climate change is impacting the Great Lakes through warming waters, altered ice cover, fluctuating water levels, and potentially more intense storms, with significant consequences for the ecosystem.']
aquatic_great_lakes_stressors["Climate Change"]["Impact on Area"] = 'Changes in thermal structure; altered water levels; changes in ice cover.'
aquatic_great_lakes_stressors["Climate Change"]["Impact on Biodiversity"] = 'Shifts in fish species distributions.\nImpacts on spawning and recruitment.\nIncreased stress on cold-water species.\nChanges in the timing of biological events.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\n**Influences (Stressors):**\nEutrophication (warmer water can exacerbate nutrient problems).\nInvasive Species (some may benefit from warmer waters).\nWater Levels.\n**Logic Description:** Climate change is impacting the Great Lakes through warming waters, altered ice cover, fluctuating water levels, and potentially more intense storms, with significant consequences for the ecosystem.'
aquatic_great_lakes_stressors["Climate Change"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Eutrophication (warmer water can exacerbate nutrient problems).', 'Invasive Species (some may benefit from warmer waters).', 'Water Levels.', '**Logic Description:** Climate change is impacting the Great Lakes through warming waters, altered ice cover, fluctuating water levels, and potentially more intense storms, with significant consequences for the ecosystem.']
aquatic_great_lakes_stressors["Climate Change"]["Influences"] = ['Eutrophication (warmer water can exacerbate nutrient problems).', 'Invasive Species (some may benefit from warmer waters).', 'Water Levels.', '**Logic Description:** Climate change is impacting the Great Lakes through warming waters, altered ice cover, fluctuating water levels, and potentially more intense storms, with significant consequences for the ecosystem.']
aquatic_great_lakes_stressors["Climate Change"]["Logic Description"] = '---'
aquatic_great_lakes_stressors["Climate Change"]["Impact Function"] = "impact_climate_change_aquatic_great_lakes"

