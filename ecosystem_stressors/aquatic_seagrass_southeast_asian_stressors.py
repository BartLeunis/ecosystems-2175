from stressor_templates import *
import copy

aquatic_seagrass_southeast_asian_stressors = {
    "Coastal Development": {},
    "Water Pollution": copy.deepcopy(pollution_template),
    "Destructive Fishing Practices": {},
    "Climate Change": copy.deepcopy(climate_change_template),
}

# --- Coastal Development ---
aquatic_seagrass_southeast_asian_stressors["Coastal Development"]["Metric"] = 'Area of seagrass habitat converted to other land uses (aquaculture, ports, urban development) (ha/year).'
aquatic_seagrass_southeast_asian_stressors["Coastal Development"]["Data Sources"] = ['Remote sensing data.', 'Government statistics (various countries).', 'Research publications.', '**Impact on Area:** *Significant* loss of seagrass habitat; fragmentation.', '**Impact on Biodiversity:**', 'Loss of habitat for a wide range of species.', 'Reduced nursery grounds for fish.', '**Influenced By (Stressors):**', 'Aquaculture Expansion: Shrimp and fish farming.', 'Urbanization and Population Growth.', 'Infrastructure Development (ports, roads).', '**Influences (Stressors):**', 'Habitat Loss (the primary impact).', 'Water Quality.', '**Logic Description:** Coastal development, driven by aquaculture, urbanization, and infrastructure projects, is a major threat to seagrass meadows in Southeast Asia.']
aquatic_seagrass_southeast_asian_stressors["Coastal Development"]["Impact on Area"] = '*Significant* loss of seagrass habitat; fragmentation.'
aquatic_seagrass_southeast_asian_stressors["Coastal Development"]["Impact on Biodiversity"] = 'Loss of habitat for a wide range of species.\nReduced nursery grounds for fish.\n**Influenced By (Stressors):**\nAquaculture Expansion: Shrimp and fish farming.\nUrbanization and Population Growth.\nInfrastructure Development (ports, roads).\n**Influences (Stressors):**\nHabitat Loss (the primary impact).\nWater Quality.\n**Logic Description:** Coastal development, driven by aquaculture, urbanization, and infrastructure projects, is a major threat to seagrass meadows in Southeast Asia.'
aquatic_seagrass_southeast_asian_stressors["Coastal Development"]["Influenced By"] = ['Aquaculture Expansion: Shrimp and fish farming.', 'Urbanization and Population Growth.', 'Infrastructure Development (ports, roads).', '**Influences (Stressors):**', 'Habitat Loss (the primary impact).', 'Water Quality.', '**Logic Description:** Coastal development, driven by aquaculture, urbanization, and infrastructure projects, is a major threat to seagrass meadows in Southeast Asia.']
aquatic_seagrass_southeast_asian_stressors["Coastal Development"]["Influences"] = ['Habitat Loss (the primary impact).', 'Water Quality.', '**Logic Description:** Coastal development, driven by aquaculture, urbanization, and infrastructure projects, is a major threat to seagrass meadows in Southeast Asia.']
aquatic_seagrass_southeast_asian_stressors["Coastal Development"]["Logic Description"] = '---'
aquatic_seagrass_southeast_asian_stressors["Coastal Development"]["Impact Function"] = "impact_coastal_development_aquatic_seagrass_southeast_asian"

# --- Water Pollution ---
aquatic_seagrass_southeast_asian_stressors["Water Pollution"]["Metric"] = 'Concentrations of nutrients, sediments, and other pollutants in coastal waters.'
aquatic_seagrass_southeast_asian_stressors["Water Pollution"]["Data Sources"] = ['Water quality monitoring data (often limited).', 'Research studies.', '**Impact on Area:** Reduced water clarity; stress on seagrasses.', '**Impact on Biodiversity:**', 'Reduced seagrass growth and survival.', 'Algal blooms.', '**Influenced By (Stressors):**', 'Agricultural Runoff.', 'Urban Runoff.', 'Industrial Discharge.', 'Aquaculture Effluent.', '* Deforestation', '**Influences (Stressors):**', 'Light Availability.', 'Seagrass Health.', '**Logic Description:** Pollution from various sources degrades water quality and impacts seagrass meadows.']
aquatic_seagrass_southeast_asian_stressors["Water Pollution"]["Impact on Area"] = 'Reduced water clarity; stress on seagrasses.'
aquatic_seagrass_southeast_asian_stressors["Water Pollution"]["Impact on Biodiversity"] = 'Reduced seagrass growth and survival.\nAlgal blooms.\n**Influenced By (Stressors):**\nAgricultural Runoff.\nUrban Runoff.\nIndustrial Discharge.\nAquaculture Effluent.\n* Deforestation\n**Influences (Stressors):**\nLight Availability.\nSeagrass Health.\n**Logic Description:** Pollution from various sources degrades water quality and impacts seagrass meadows.'
aquatic_seagrass_southeast_asian_stressors["Water Pollution"]["Influenced By"] = ['Agricultural Runoff.', 'Urban Runoff.', 'Industrial Discharge.', 'Aquaculture Effluent.', '* Deforestation', '**Influences (Stressors):**', 'Light Availability.', 'Seagrass Health.', '**Logic Description:** Pollution from various sources degrades water quality and impacts seagrass meadows.']
aquatic_seagrass_southeast_asian_stressors["Water Pollution"]["Influences"] = ['Light Availability.', 'Seagrass Health.', '**Logic Description:** Pollution from various sources degrades water quality and impacts seagrass meadows.']
aquatic_seagrass_southeast_asian_stressors["Water Pollution"]["Logic Description"] = '---'
aquatic_seagrass_southeast_asian_stressors["Water Pollution"]["Impact Function"] = "impact_water_pollution_aquatic_seagrass_southeast_asian"

# --- Destructive Fishing Practices ---
aquatic_seagrass_southeast_asian_stressors["Destructive Fishing Practices"]["Metric"] = 'Use of bottom trawls, dynamite fishing, and other destructive methods.'
aquatic_seagrass_southeast_asian_stressors["Destructive Fishing Practices"]["Data Sources"] = ['Fisheries data (often unreliable).', 'Reports from local communities and conservation organizations.', 'Research studies.', '**Impact on Area:** Direct physical damage to seagrass beds.', '**Impact on Biodiversity:**', 'Habitat destruction.', 'Decline of fish populations.', '**Influenced By (Stressors):**', 'Poverty and Lack of Alternative Livelihoods.', 'Weak Enforcement of Fisheries Regulations.', '**Influences (Stressors):**', 'Habitat Loss.', '**Logic Description:** Destructive fishing practices, such as bottom trawling and dynamite fishing, damage seagrass beds and impact associated biodiversity.']
aquatic_seagrass_southeast_asian_stressors["Destructive Fishing Practices"]["Impact on Area"] = 'Direct physical damage to seagrass beds.'
aquatic_seagrass_southeast_asian_stressors["Destructive Fishing Practices"]["Impact on Biodiversity"] = 'Habitat destruction.\nDecline of fish populations.\n**Influenced By (Stressors):**\nPoverty and Lack of Alternative Livelihoods.\nWeak Enforcement of Fisheries Regulations.\n**Influences (Stressors):**\nHabitat Loss.\n**Logic Description:** Destructive fishing practices, such as bottom trawling and dynamite fishing, damage seagrass beds and impact associated biodiversity.'
aquatic_seagrass_southeast_asian_stressors["Destructive Fishing Practices"]["Influenced By"] = ['Poverty and Lack of Alternative Livelihoods.', 'Weak Enforcement of Fisheries Regulations.', '**Influences (Stressors):**', 'Habitat Loss.', '**Logic Description:** Destructive fishing practices, such as bottom trawling and dynamite fishing, damage seagrass beds and impact associated biodiversity.']
aquatic_seagrass_southeast_asian_stressors["Destructive Fishing Practices"]["Influences"] = ['Habitat Loss.', '**Logic Description:** Destructive fishing practices, such as bottom trawling and dynamite fishing, damage seagrass beds and impact associated biodiversity.']
aquatic_seagrass_southeast_asian_stressors["Destructive Fishing Practices"]["Logic Description"] = '---'
aquatic_seagrass_southeast_asian_stressors["Destructive Fishing Practices"]["Impact Function"] = "impact_destructive_fishing_practices_aquatic_seagrass_southeast_asian"

# --- Climate Change ---
aquatic_seagrass_southeast_asian_stressors["Climate Change"]["Metric"] = 'Sea surface temperature; ocean acidification; sea level rise; storm intensity.'
aquatic_seagrass_southeast_asian_stressors["Climate Change"]["Data Sources"] = ['Climate models.', '* Oceanographic data.', '**Impact on Area:** Seagrass die-offs; distribution changes', '**Impact on Biodiversity:**', '* Increased stress; species shifts.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Sea Level Rise.', 'Ocean Acidification.', '**Logic Description:** Climate change related impacts on seagrass.']
aquatic_seagrass_southeast_asian_stressors["Climate Change"]["Impact on Area"] = 'Seagrass die-offs; distribution changes'
aquatic_seagrass_southeast_asian_stressors["Climate Change"]["Impact on Biodiversity"] = '* Increased stress; species shifts.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\n**Influences (Stressors):**\nSea Level Rise.\nOcean Acidification.\n**Logic Description:** Climate change related impacts on seagrass.'
aquatic_seagrass_southeast_asian_stressors["Climate Change"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Sea Level Rise.', 'Ocean Acidification.', '**Logic Description:** Climate change related impacts on seagrass.']
aquatic_seagrass_southeast_asian_stressors["Climate Change"]["Influences"] = ['Sea Level Rise.', 'Ocean Acidification.', '**Logic Description:** Climate change related impacts on seagrass.']
aquatic_seagrass_southeast_asian_stressors["Climate Change"]["Logic Description"] = '---'
aquatic_seagrass_southeast_asian_stressors["Climate Change"]["Impact Function"] = "impact_climate_change_aquatic_seagrass_southeast_asian"

