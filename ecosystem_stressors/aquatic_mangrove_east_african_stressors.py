from stressor_templates import *
import copy

aquatic_mangrove_east_african_stressors = {
    "Deforestation": copy.deepcopy(deforestation_template),
    "Coastal Development": {},
    "Pollution": copy.deepcopy(pollution_template),
    "Climate Change": copy.deepcopy(climate_change_template),
}

# --- Deforestation ---
aquatic_mangrove_east_african_stressors["Deforestation"]["Metric"] = 'Area of mangroves cleared per year (ha/year) (primarily for charcoal and fuelwood).'
aquatic_mangrove_east_african_stressors["Deforestation"]["Data Sources"] = ['Remote sensing data.', 'Forestry data (often limited).', 'Research publications.', '**Impact on Area:** *Significant* loss of mangrove habitat.', '**Impact on Biodiversity:**', 'Habitat loss.', 'Reduced carbon sequestration.', 'Loss of coastal protection.', '**Influenced By (Stressors):**', 'Poverty and Lack of Alternative Livelihoods: High dependence on mangrove wood for fuel.', 'Demand for Charcoal: A major cooking fuel in the region.', 'Population Growth: Increased demand for fuelwood.', 'Weak Enforcement of Environmental Regulations.', '**Influences (Stressors):**', 'Coastal Erosion.', 'Carbon Emissions.', '**Logic Description:** Deforestation for charcoal production and fuelwood is a *major* driver of mangrove loss in East Africa, driven by poverty, population growth, and lack of alternative energy sources.']
aquatic_mangrove_east_african_stressors["Deforestation"]["Impact on Area"] = '*Significant* loss of mangrove habitat.'
aquatic_mangrove_east_african_stressors["Deforestation"]["Impact on Biodiversity"] = 'Habitat loss.\nReduced carbon sequestration.\nLoss of coastal protection.\n**Influenced By (Stressors):**\nPoverty and Lack of Alternative Livelihoods: High dependence on mangrove wood for fuel.\nDemand for Charcoal: A major cooking fuel in the region.\nPopulation Growth: Increased demand for fuelwood.\nWeak Enforcement of Environmental Regulations.\n**Influences (Stressors):**\nCoastal Erosion.\nCarbon Emissions.\n**Logic Description:** Deforestation for charcoal production and fuelwood is a *major* driver of mangrove loss in East Africa, driven by poverty, population growth, and lack of alternative energy sources.'
aquatic_mangrove_east_african_stressors["Deforestation"]["Influenced By"] = ['Poverty and Lack of Alternative Livelihoods: High dependence on mangrove wood for fuel.', 'Demand for Charcoal: A major cooking fuel in the region.', 'Population Growth: Increased demand for fuelwood.', 'Weak Enforcement of Environmental Regulations.', '**Influences (Stressors):**', 'Coastal Erosion.', 'Carbon Emissions.', '**Logic Description:** Deforestation for charcoal production and fuelwood is a *major* driver of mangrove loss in East Africa, driven by poverty, population growth, and lack of alternative energy sources.']
aquatic_mangrove_east_african_stressors["Deforestation"]["Influences"] = ['Coastal Erosion.', 'Carbon Emissions.', '**Logic Description:** Deforestation for charcoal production and fuelwood is a *major* driver of mangrove loss in East Africa, driven by poverty, population growth, and lack of alternative energy sources.']
aquatic_mangrove_east_african_stressors["Deforestation"]["Logic Description"] = '---'

# --- Coastal Development ---
aquatic_mangrove_east_african_stressors["Coastal Development"]["Metric"] = 'Area of mangroves converted to other land uses (ha/year).'
aquatic_mangrove_east_african_stressors["Coastal Development"]["Data Sources"] = ['Remote sensing data.', 'Government statistics.', 'Reports from conservation organizations.', '**Impact on Area:** Loss of mangrove habitat; fragmentation.', '**Impact on Biodiversity:**', 'Habitat loss.', 'Reduced nursery grounds for fish.', '**Influenced By (Stressors):**', 'Tourism Development: In some areas.', 'Urbanization: Expansion of coastal towns and cities.', 'Infrastructure Development (ports).', 'Aquaculture (but less so than in SE Asia)', '**Influences (Stressors):**', 'Coastal Erosion.', 'Water Quality.', '**Logic Description:** Coastal development, while less extensive than in some other regions, is a growing threat.']
aquatic_mangrove_east_african_stressors["Coastal Development"]["Impact on Area"] = 'Loss of mangrove habitat; fragmentation.'
aquatic_mangrove_east_african_stressors["Coastal Development"]["Impact on Biodiversity"] = 'Habitat loss.\nReduced nursery grounds for fish.\n**Influenced By (Stressors):**\nTourism Development: In some areas.\nUrbanization: Expansion of coastal towns and cities.\nInfrastructure Development (ports).\nAquaculture (but less so than in SE Asia)\n**Influences (Stressors):**\nCoastal Erosion.\nWater Quality.\n**Logic Description:** Coastal development, while less extensive than in some other regions, is a growing threat.'
aquatic_mangrove_east_african_stressors["Coastal Development"]["Influenced By"] = ['Tourism Development: In some areas.', 'Urbanization: Expansion of coastal towns and cities.', 'Infrastructure Development (ports).', 'Aquaculture (but less so than in SE Asia)', '**Influences (Stressors):**', 'Coastal Erosion.', 'Water Quality.', '**Logic Description:** Coastal development, while less extensive than in some other regions, is a growing threat.']
aquatic_mangrove_east_african_stressors["Coastal Development"]["Influences"] = ['Coastal Erosion.', 'Water Quality.', '**Logic Description:** Coastal development, while less extensive than in some other regions, is a growing threat.']
aquatic_mangrove_east_african_stressors["Coastal Development"]["Logic Description"] = '---'

# --- Pollution ---
aquatic_mangrove_east_african_stressors["Pollution"]["Metric"] = 'Concentrations of pollutants in water and sediment.'
aquatic_mangrove_east_african_stressors["Pollution"]["Data Sources"] = ['Water quality monitoring data (limited).', 'Research studies.', '**Impact on Area:** Water quality degradation.', '**Impact on Biodiversity:**', 'Impacts on mangroves and associated fauna.', '**Influenced By (Stressors):**', 'Urban Runoff.', 'Industrial Discharge (in some areas).', 'Agricultural Runoff.', '**Influences (Stressors):**', '* Water Quality', '* Mangrove Health', '**Logic Description:** Pollution from various sources impacts water quality.']
aquatic_mangrove_east_african_stressors["Pollution"]["Impact on Area"] = 'Water quality degradation.'
aquatic_mangrove_east_african_stressors["Pollution"]["Impact on Biodiversity"] = 'Impacts on mangroves and associated fauna.\n**Influenced By (Stressors):**\nUrban Runoff.\nIndustrial Discharge (in some areas).\nAgricultural Runoff.\n**Influences (Stressors):**\n* Water Quality\n* Mangrove Health\n**Logic Description:** Pollution from various sources impacts water quality.'
aquatic_mangrove_east_african_stressors["Pollution"]["Influenced By"] = ['Urban Runoff.', 'Industrial Discharge (in some areas).', 'Agricultural Runoff.', '**Influences (Stressors):**', '* Water Quality', '* Mangrove Health', '**Logic Description:** Pollution from various sources impacts water quality.']
aquatic_mangrove_east_african_stressors["Pollution"]["Influences"] = ['* Water Quality', '* Mangrove Health', '**Logic Description:** Pollution from various sources impacts water quality.']
aquatic_mangrove_east_african_stressors["Pollution"]["Logic Description"] = '---'

# --- Climate Change ---
aquatic_mangrove_east_african_stressors["Climate Change"]["Metric"] = 'Sea Level Rise, temperature increase, changes in rainfall'
aquatic_mangrove_east_african_stressors["Climate Change"]["Data Sources"] = ['* Climate Models', '* Tide Gauges', '* Historical Weather Records', '**Impact on Area:** Inundation and erosion, salinity changes', '**Impact on Biodiversity:**', '* Species shifts', '* Increased Stress on mangroves', '**Influenced By (Stressors):**', '* Global GHG', '**Influences (Stressors):**', '* Sea Level', '* Coastal erosion', '**Logic Description:** Climate change, particularly sea level rise.']
aquatic_mangrove_east_african_stressors["Climate Change"]["Impact on Area"] = 'Inundation and erosion, salinity changes'
aquatic_mangrove_east_african_stressors["Climate Change"]["Impact on Biodiversity"] = '* Species shifts\n* Increased Stress on mangroves\n**Influenced By (Stressors):**\n* Global GHG\n**Influences (Stressors):**\n* Sea Level\n* Coastal erosion\n**Logic Description:** Climate change, particularly sea level rise.'
aquatic_mangrove_east_african_stressors["Climate Change"]["Influenced By"] = ['* Global GHG', '**Influences (Stressors):**', '* Sea Level', '* Coastal erosion', '**Logic Description:** Climate change, particularly sea level rise.']
aquatic_mangrove_east_african_stressors["Climate Change"]["Influences"] = ['* Sea Level', '* Coastal erosion', '**Logic Description:** Climate change, particularly sea level rise.']
aquatic_mangrove_east_african_stressors["Climate Change"]["Logic Description"] = '---'

