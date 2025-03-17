from stressor_templates import *
import copy

wetlands_danube_delta_stressors = {
    "Altered Hydrology": copy.deepcopy(altered_hydrology_template),
    "Pollution": copy.deepcopy(pollution_template),
    "Invasive Species": copy.deepcopy(invasive_species_template),
    "Overfishing": copy.deepcopy(overfishing_template),
    "Climate Change": copy.deepcopy(climate_change_template),
    "Eutrophication": {},
    "Navigation Projects": {},
    "Sedimentation": {},
}

# --- Altered Hydrology ---
wetlands_danube_delta_stressors["Altered Hydrology"]["Metric"] = "Water levels in the Danube River and in the delta's channels and lakes; water flow rates; sediment load."
wetlands_danube_delta_stressors["Altered Hydrology"]["Data Sources"] = ['Romanian and Ukrainian government agencies responsible for water management.', 'Danube Delta Biosphere Reserve Authority (Romania).', 'Research institutions (e.g., Danube Delta National Institute for Research and Development).', 'International Commission for the Protection of the Danube River (ICPDR).', '**Impact on Area:** Changes in the extent and distribution of different wetland habitats (reed beds, floating reed islands, lakes, channels).', '**Impact on Biodiversity:**', 'Impacts on fish populations (spawning, migration – the delta is *very* important for fish).', 'Changes in bird populations (breeding, feeding, migration).', 'Impacts on aquatic invertebrate communities.', 'Changes in vegetation communities.', '**Influenced By (Stressors):**', 'Upstream Dam Construction: Dams on the Danube River and its tributaries (throughout the Danube Basin) significantly alter flow regimes and sediment transport.', 'Water Management Practices: Within the delta itself (e.g., canals, dikes).', 'Climate Change: Changes in precipitation and river discharge.', '* Navigation projects', '**Influences (Stressors):**', 'Sedimentation.', 'Habitat Availability.', 'Water Quality.', "**Logic Description:** The Danube Delta's hydrology is strongly influenced by the Danube River. Upstream dams, water management practices within the delta, and climate change are all altering the natural hydrological regime, with significant impacts on the ecosystem."]
wetlands_danube_delta_stressors["Altered Hydrology"]["Impact on Area"] = 'Changes in the extent and distribution of different wetland habitats (reed beds, floating reed islands, lakes, channels).'
wetlands_danube_delta_stressors["Altered Hydrology"]["Impact on Biodiversity"] = "Impacts on fish populations (spawning, migration – the delta is *very* important for fish).\nChanges in bird populations (breeding, feeding, migration).\nImpacts on aquatic invertebrate communities.\nChanges in vegetation communities.\n**Influenced By (Stressors):**\nUpstream Dam Construction: Dams on the Danube River and its tributaries (throughout the Danube Basin) significantly alter flow regimes and sediment transport.\nWater Management Practices: Within the delta itself (e.g., canals, dikes).\nClimate Change: Changes in precipitation and river discharge.\n* Navigation projects\n**Influences (Stressors):**\nSedimentation.\nHabitat Availability.\nWater Quality.\n**Logic Description:** The Danube Delta's hydrology is strongly influenced by the Danube River. Upstream dams, water management practices within the delta, and climate change are all altering the natural hydrological regime, with significant impacts on the ecosystem."
wetlands_danube_delta_stressors["Altered Hydrology"]["Influenced By"] = ['Upstream Dam Construction: Dams on the Danube River and its tributaries (throughout the Danube Basin) significantly alter flow regimes and sediment transport.', 'Water Management Practices: Within the delta itself (e.g., canals, dikes).', 'Climate Change: Changes in precipitation and river discharge.', '* Navigation projects', '**Influences (Stressors):**', 'Sedimentation.', 'Habitat Availability.', 'Water Quality.', "**Logic Description:** The Danube Delta's hydrology is strongly influenced by the Danube River. Upstream dams, water management practices within the delta, and climate change are all altering the natural hydrological regime, with significant impacts on the ecosystem."]
wetlands_danube_delta_stressors["Altered Hydrology"]["Influences"] = ['Sedimentation.', 'Habitat Availability.', 'Water Quality.', "**Logic Description:** The Danube Delta's hydrology is strongly influenced by the Danube River. Upstream dams, water management practices within the delta, and climate change are all altering the natural hydrological regime, with significant impacts on the ecosystem."]
wetlands_danube_delta_stressors["Altered Hydrology"]["Logic Description"] = '---'
wetlands_danube_delta_stressors["Altered Hydrology"]["Impact Function"] = "impact_altered_hydrology_wetlands_danube_delta"

# --- Pollution ---
wetlands_danube_delta_stressors["Pollution"]["Metric"] = 'Concentrations of pollutants (e.g., nutrients, heavy metals, pesticides, organic pollutants) in water, sediment, and biota.'
wetlands_danube_delta_stressors["Pollution"]["Data Sources"] = ['Water quality monitoring programs (Romanian and Ukrainian agencies, ICPDR).', 'Research studies.', '**Impact on Area:** Degradation of water quality.', '**Impact on Biodiversity:**', 'Eutrophication (nutrient enrichment, leading to algal blooms).', 'Toxic effects on wildlife.', 'Impacts on food webs.', '**Influenced By (Stressors):**', 'Agricultural Runoff: From the Danube River Basin (a *huge* area).', 'Industrial Discharge: From industries throughout the basin.', 'Untreated or Inadequately Treated Wastewater: From cities and towns along the Danube.', '* Navigation', '**Influences (Stressors):**', 'Water Quality.', 'Wildlife Health.', '**Logic Description:** The Danube Delta receives pollutants from the entire Danube River Basin, a vast area encompassing many countries. Agriculture, industry, and inadequate wastewater treatment are major sources.']
wetlands_danube_delta_stressors["Pollution"]["Impact on Area"] = 'Degradation of water quality.'
wetlands_danube_delta_stressors["Pollution"]["Impact on Biodiversity"] = 'Eutrophication (nutrient enrichment, leading to algal blooms).\nToxic effects on wildlife.\nImpacts on food webs.\n**Influenced By (Stressors):**\nAgricultural Runoff: From the Danube River Basin (a *huge* area).\nIndustrial Discharge: From industries throughout the basin.\nUntreated or Inadequately Treated Wastewater: From cities and towns along the Danube.\n* Navigation\n**Influences (Stressors):**\nWater Quality.\nWildlife Health.\n**Logic Description:** The Danube Delta receives pollutants from the entire Danube River Basin, a vast area encompassing many countries. Agriculture, industry, and inadequate wastewater treatment are major sources.'
wetlands_danube_delta_stressors["Pollution"]["Influenced By"] = ['Agricultural Runoff: From the Danube River Basin (a *huge* area).', 'Industrial Discharge: From industries throughout the basin.', 'Untreated or Inadequately Treated Wastewater: From cities and towns along the Danube.', '* Navigation', '**Influences (Stressors):**', 'Water Quality.', 'Wildlife Health.', '**Logic Description:** The Danube Delta receives pollutants from the entire Danube River Basin, a vast area encompassing many countries. Agriculture, industry, and inadequate wastewater treatment are major sources.']
wetlands_danube_delta_stressors["Pollution"]["Influences"] = ['Water Quality.', 'Wildlife Health.', '**Logic Description:** The Danube Delta receives pollutants from the entire Danube River Basin, a vast area encompassing many countries. Agriculture, industry, and inadequate wastewater treatment are major sources.']
wetlands_danube_delta_stressors["Pollution"]["Logic Description"] = '---'
wetlands_danube_delta_stressors["Pollution"]["Impact Function"] = "impact_pollution_wetlands_danube_delta"

# --- Invasive Species ---
wetlands_danube_delta_stressors["Invasive Species"]["Metric"] = 'Abundance and distribution of key invasive species (e.g., certain fish, mollusks, plants).'
wetlands_danube_delta_stressors["Invasive Species"]["Data Sources"] = ['Research studies.', 'Monitoring programs by the Danube Delta Biosphere Reserve Authority.', '**Impact on Area:** Changes in species composition and ecosystem structure.', '**Impact on Biodiversity:**', 'Competition with native species.', 'Predation on native species.', 'Alteration of habitat.', '**Influenced By (Stressors):**', 'Introduction through shipping (ballast water).', 'Aquaculture (escaped fish).', '* Climate Change (may favor some invasives)', '**Influences (Stressors):**', '* Native Species', "**Logic Description:** Invasive species, introduced through various pathways, can outcompete native species and disrupt the delta's ecosystem."]
wetlands_danube_delta_stressors["Invasive Species"]["Impact on Area"] = 'Changes in species composition and ecosystem structure.'
wetlands_danube_delta_stressors["Invasive Species"]["Impact on Biodiversity"] = "Competition with native species.\nPredation on native species.\nAlteration of habitat.\n**Influenced By (Stressors):**\nIntroduction through shipping (ballast water).\nAquaculture (escaped fish).\n* Climate Change (may favor some invasives)\n**Influences (Stressors):**\n* Native Species\n**Logic Description:** Invasive species, introduced through various pathways, can outcompete native species and disrupt the delta's ecosystem."
wetlands_danube_delta_stressors["Invasive Species"]["Influenced By"] = ['Introduction through shipping (ballast water).', 'Aquaculture (escaped fish).', '* Climate Change (may favor some invasives)', '**Influences (Stressors):**', '* Native Species', "**Logic Description:** Invasive species, introduced through various pathways, can outcompete native species and disrupt the delta's ecosystem."]
wetlands_danube_delta_stressors["Invasive Species"]["Influences"] = ['* Native Species', "**Logic Description:** Invasive species, introduced through various pathways, can outcompete native species and disrupt the delta's ecosystem."]
wetlands_danube_delta_stressors["Invasive Species"]["Logic Description"] = '---'
wetlands_danube_delta_stressors["Invasive Species"]["Impact Function"] = "impact_invasive_species_wetlands_danube_delta"

# --- Overfishing ---
wetlands_danube_delta_stressors["Overfishing"]["Metric"] = 'Fish catches, population sizes.'
wetlands_danube_delta_stressors["Overfishing"]["Data Sources"] = ['* Fishery statistics', '* Research', '**Impact on Area:** N/A', '**Impact on Biodiversity:**', '* Decline in fish populations.', '* Food web effects', '**Influenced By (Stressors):**', '* Fishing pressure', '**Influences (Stressors):**', '* Fish Stocks', '* Food Webs', '**Logic Description:** Unsustainable fishing practices impact fish.']
wetlands_danube_delta_stressors["Overfishing"]["Impact on Area"] = 'N/A'
wetlands_danube_delta_stressors["Overfishing"]["Impact on Biodiversity"] = '* Decline in fish populations.\n* Food web effects\n**Influenced By (Stressors):**\n* Fishing pressure\n**Influences (Stressors):**\n* Fish Stocks\n* Food Webs\n**Logic Description:** Unsustainable fishing practices impact fish.'
wetlands_danube_delta_stressors["Overfishing"]["Influenced By"] = ['* Fishing pressure', '**Influences (Stressors):**', '* Fish Stocks', '* Food Webs', '**Logic Description:** Unsustainable fishing practices impact fish.']
wetlands_danube_delta_stressors["Overfishing"]["Influences"] = ['* Fish Stocks', '* Food Webs', '**Logic Description:** Unsustainable fishing practices impact fish.']
wetlands_danube_delta_stressors["Overfishing"]["Logic Description"] = '---'
wetlands_danube_delta_stressors["Overfishing"]["Impact Function"] = "impact_overfishing_wetlands_danube_delta"

# --- Climate Change ---
wetlands_danube_delta_stressors["Climate Change"]["Metric"] = 'Temp, precip, sea level rise.'
wetlands_danube_delta_stressors["Climate Change"]["Data Sources"] = ['* Climate Models.', '* Historical Records', '**Impact on Area:** Changes in hydro, coastal erosion.', '**Impact on Biodiversity:**', '* Species shifts, stress.', '**Influenced By (Stressors):**', '* Global GHG', '**Influences (Stressors):**', '* Hydrology', '**Logic Description**: Climate change is a long-term threat.']
wetlands_danube_delta_stressors["Climate Change"]["Impact on Area"] = 'Changes in hydro, coastal erosion.'
wetlands_danube_delta_stressors["Climate Change"]["Impact on Biodiversity"] = '* Species shifts, stress.\n**Influenced By (Stressors):**\n* Global GHG\n**Influences (Stressors):**\n* Hydrology\n**Logic Description**: Climate change is a long-term threat.'
wetlands_danube_delta_stressors["Climate Change"]["Influenced By"] = ['* Global GHG', '**Influences (Stressors):**', '* Hydrology', '**Logic Description**: Climate change is a long-term threat.']
wetlands_danube_delta_stressors["Climate Change"]["Influences"] = ['* Hydrology', '**Logic Description**: Climate change is a long-term threat.']
wetlands_danube_delta_stressors["Climate Change"]["Impact Function"] = "impact_climate_change_wetlands_danube_delta"

# --- Eutrophication ---
wetlands_danube_delta_stressors["Eutrophication"]["Metric"] = 'Nutrient levels, algal blooms'
wetlands_danube_delta_stressors["Eutrophication"]["Data Sources"] = ['* Water quality data.', '**Impact on Area:** Water quality degradation', '**Impact on Biodiversity:**', '* Harmful algal blooms, oxygen depletion.', '**Influenced By (Stressors):**', '* Danube Delta - Pollution', '**Influences (Stressors):**', '* Danube Delta - Water Quality', '**Logic Description:** Excess nutrients lead to algal overgrowth.']
wetlands_danube_delta_stressors["Eutrophication"]["Impact on Area"] = 'Water quality degradation'
wetlands_danube_delta_stressors["Eutrophication"]["Impact on Biodiversity"] = '* Harmful algal blooms, oxygen depletion.\n**Influenced By (Stressors):**\n* Danube Delta - Pollution\n**Influences (Stressors):**\n* Danube Delta - Water Quality\n**Logic Description:** Excess nutrients lead to algal overgrowth.'
wetlands_danube_delta_stressors["Eutrophication"]["Influenced By"] = ['* Danube Delta - Pollution', '**Influences (Stressors):**', '* Danube Delta - Water Quality', '**Logic Description:** Excess nutrients lead to algal overgrowth.']
wetlands_danube_delta_stressors["Eutrophication"]["Influences"] = ['* Danube Delta - Water Quality', '**Logic Description:** Excess nutrients lead to algal overgrowth.']
wetlands_danube_delta_stressors["Eutrophication"]["Logic Description"] = '---'
wetlands_danube_delta_stressors["Eutrophication"]["Impact Function"] = "impact_eutrophication_wetlands_danube_delta"

# --- Navigation Projects ---
wetlands_danube_delta_stressors["Navigation Projects"]["Data Sources"] = ['* Government records, project reports.', '**Impact on Area**: Altered hydrology, habitat loss.', '**Impact on Biodiversity:**', '* Direct habitat destruction, impacts on fish migration.', '**Influenced By (Stressors):**', '*  Economic development, international agreements.', '**Influences (Stressors):**', '* Danube Delta - Altered Hydrology', '* Danube Delta - Pollution', '**Logic Description:** Infrastructure development for shipping can damage the ecosystem.']
wetlands_danube_delta_stressors["Navigation Projects"]["Impact on Biodiversity"] = '* Direct habitat destruction, impacts on fish migration.\n**Influenced By (Stressors):**\n*  Economic development, international agreements.\n**Influences (Stressors):**\n* Danube Delta - Altered Hydrology\n* Danube Delta - Pollution\n**Logic Description:** Infrastructure development for shipping can damage the ecosystem.'
wetlands_danube_delta_stressors["Navigation Projects"]["Influenced By"] = ['*  Economic development, international agreements.', '**Influences (Stressors):**', '* Danube Delta - Altered Hydrology', '* Danube Delta - Pollution', '**Logic Description:** Infrastructure development for shipping can damage the ecosystem.']
wetlands_danube_delta_stressors["Navigation Projects"]["Influences"] = ['* Danube Delta - Altered Hydrology', '* Danube Delta - Pollution', '**Logic Description:** Infrastructure development for shipping can damage the ecosystem.']
wetlands_danube_delta_stressors["Navigation Projects"]["Logic Description"] = '---'
wetlands_danube_delta_stressors["Navigation Projects"]["Impact Function"] = "impact_navigation_projects_wetlands_danube_delta"

# --- Sedimentation ---
wetlands_danube_delta_stressors["Sedimentation"]["Influenced By"] = ['* Danube Delta - Altered Hydrology', '**Influences (Stressors):**', '* Habitat quality', '**Logic Description:** Changes in sediment dynamics affect the delta.']
wetlands_danube_delta_stressors["Sedimentation"]["Influences"] = ['* Habitat quality', '**Logic Description:** Changes in sediment dynamics affect the delta.']
wetlands_danube_delta_stressors["Sedimentation"]["Logic Description"] = '---'
wetlands_danube_delta_stressors["Sedimentation"]["Impact Function"] = "impact_sedimentation_wetlands_danube_delta"

