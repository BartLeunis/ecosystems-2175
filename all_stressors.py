# all_stressors.py

from stressor_templates import *
import copy



all_stressors_data = {
    "Amazon Rainforest": {
        "Infrastructure Development": copy.deepcopy(infrastructure_development_template),
        "Deforestation": copy.deepcopy(deforestation_template),
        "Temperature Increase": copy.deepcopy(climate_change_template),
        "Changes in Precipitation": copy.deepcopy(climate_change_template),
        "Wildfires": copy.deepcopy(fire_regime_template),
        "Hydrological Changes": copy.deepcopy(altered_hydrology_template),
        "Overexploitation": copy.deepcopy(overfishing_template),  # Corrected template
        "Mining": copy.deepcopy(pollution_template),        # Corrected template
        "Pollution": copy.deepcopy(pollution_template)
    },
    "Congo Rainforest": {
        "Deforestation": copy.deepcopy(deforestation_template),
        "Temperature Increase": copy.deepcopy(climate_change_template),
        "Changes in Precipitation": copy.deepcopy(climate_change_template),
        "Wildfires": copy.deepcopy(fire_regime_template),
        "Overexploitation": copy.deepcopy(overfishing_template), # Using overfishing as a base
        "Mining": copy.deepcopy(mining_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Infrastructure Development": copy.deepcopy(infrastructure_development_template)
    },
    "Southeast Asian Rainforest": {
        "Deforestation": copy.deepcopy(deforestation_template),
        "Temperature Increase": copy.deepcopy(climate_change_template),
        "Changes in Precipitation": copy.deepcopy(climate_change_template),
        "Wildfires": copy.deepcopy(fire_regime_template),
        "Overexploitation": copy.deepcopy(overfishing_template), # Using overfishing template as base
        "Mining": copy.deepcopy(mining_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Infrastructure Development": copy.deepcopy(infrastructure_development_template),
        "Peatland Degradation": copy.deepcopy(land_use_change_template) #Using land-use change for now
    },
    "Sundaland Rainforest": {
        "Deforestation": copy.deepcopy(deforestation_template),
        "Temperature Increase": copy.deepcopy(climate_change_template),
        "Changes in Precipitation": copy.deepcopy(climate_change_template),
        "Wildfires": copy.deepcopy(fire_regime_template),
        "Overexploitation": copy.deepcopy(overfishing_template), #Using as base
        "Pollution": copy.deepcopy(pollution_template),
        "Infrastructure Development": copy.deepcopy(infrastructure_development_template),
        "Peatland Degradation": copy.deepcopy(land_use_change_template) # Using land use for now
    },
    "New Guinea Rainforest": {
        "Deforestation": copy.deepcopy(deforestation_template),
        "Temperature Increase": copy.deepcopy(climate_change_template),
        "Changes in Precipitation": copy.deepcopy(climate_change_template),
        "Wildfires": copy.deepcopy(fire_regime_template),
        "Overexploitation": copy.deepcopy(overfishing_template),  #Using as a base again
        "Mining": copy.deepcopy(mining_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Infrastructure Development": copy.deepcopy(infrastructure_development_template)
    },
    "Atlantic Forest": {
        "Deforestation": copy.deepcopy(deforestation_template),
        "Temperature Increase": copy.deepcopy(climate_change_template),
        "Changes in Precipitation": copy.deepcopy(climate_change_template),
        "Wildfires": copy.deepcopy(fire_regime_template),
        "Overexploitation": copy.deepcopy(overfishing_template), #Using as a base
        "Pollution": copy.deepcopy(pollution_template),
        "Infrastructure Development": copy.deepcopy(infrastructure_development_template)
    },
    "Mesoamerican Forests": {
        "Deforestation": copy.deepcopy(deforestation_template),
        "Temperature Increase": copy.deepcopy(climate_change_template),
        "Changes in Precipitation": copy.deepcopy(climate_change_template),
        "Wildfires": copy.deepcopy(fire_regime_template),
        "Overexploitation": copy.deepcopy(overfishing_template), # Using overfishing as base
        "Pollution": copy.deepcopy(pollution_template),
        "Infrastructure Development": copy.deepcopy(infrastructure_development_template)
    },
    "Great Barrier Reef": {
        "Temperature Increase": copy.deepcopy(climate_change_template),
        "Ocean Acidification": copy.deepcopy(ocean_acidification_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Overfishing": copy.deepcopy(overfishing_template),
        "Coastal Development": copy.deepcopy(infrastructure_development_template),
        "Crown-of-Thorns Starfish Outbreaks": copy.deepcopy(invasive_species_template) #Rename
    },
    "Mesoamerican Reef": {
        "Temperature Increase": copy.deepcopy(climate_change_template),
        "Ocean Acidification": copy.deepcopy(ocean_acidification_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Overfishing": copy.deepcopy(overfishing_template),
        "Coastal Development": copy.deepcopy(infrastructure_development_template),
        "Invasive Species": copy.deepcopy(invasive_species_template)
    },
    "Coral Triangle": {
        "Temperature Increase": copy.deepcopy(climate_change_template),
        "Ocean Acidification": copy.deepcopy(ocean_acidification_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Overfishing": copy.deepcopy(overfishing_template),
        "Destructive Fishing Practices": copy.deepcopy(destructive_fishing_template),
        "Coastal Development": copy.deepcopy(infrastructure_development_template)
    },
     "Florida Keys Reefs": {
        "Temperature Increase": copy.deepcopy(climate_change_template),
        "Ocean Acidification": copy.deepcopy(ocean_acidification_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Overfishing": copy.deepcopy(overfishing_template),
        "Coastal Development": copy.deepcopy(infrastructure_development_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Coral Disease": copy.deepcopy(invasive_species_template) # Using invasive species as a base
    },
    "Caribbean Reefs": {
        "Temperature Increase": copy.deepcopy(climate_change_template),
        "Ocean Acidification": copy.deepcopy(ocean_acidification_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Overfishing": copy.deepcopy(overfishing_template),
        "Coastal Development": copy.deepcopy(infrastructure_development_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Coral Disease": copy.deepcopy(invasive_species_template) # Using invasive species as a base
    },
    "Red Sea Reefs": {
        "Temperature Increase": copy.deepcopy(climate_change_template),
        "Ocean Acidification": copy.deepcopy(ocean_acidification_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Overfishing": copy.deepcopy(overfishing_template),
        "Coastal Development": copy.deepcopy(infrastructure_development_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Coral Disease": copy.deepcopy(invasive_species_template)
    },
    "North American Prairies": {
        "Land-Use Change": copy.deepcopy(land_use_change_template),
        "Habitat Fragmentation": copy.deepcopy(fragmentation_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Fire Suppression": copy.deepcopy(fire_regime_template),
        "Overgrazing": copy.deepcopy(overgrazing_template),
        "Agricultural Expansion": copy.deepcopy(land_use_change_template),
        "Urban Sprawl": copy.deepcopy(land_use_change_template),
        "Government Policies": copy.deepcopy(land_use_change_template),
        "Infrastructure Development": copy.deepcopy(infrastructure_development_template),
        "Disturbance": copy.deepcopy(invasive_species_template),  #Using as generic template
        "Introduction": copy.deepcopy(invasive_species_template),
        "Land Management Practices": copy.deepcopy(land_use_change_template), #Using as generic
        "Fire Regimes": copy.deepcopy(fire_regime_template),
        "Woody Encroachment": copy.deepcopy(land_use_change_template),  # Using land use as a general template for now
        "Fire Intensity": copy.deepcopy(fire_regime_template),
        "Water Availability": copy.deepcopy(climate_change_template),
        "Vegetation Changes": copy.deepcopy(land_use_change_template)
    },
    "African Savannas": {
        "Land-Use Change": copy.deepcopy(land_use_change_template),
        "Habitat Fragmentation": copy.deepcopy(fragmentation_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Wildfires": copy.deepcopy(fire_regime_template),
        "Poaching": copy.deepcopy(invasive_species_template), #Using invasive as base
        "Overgrazing": copy.deepcopy(overgrazing_template),
        "Invasive Species": copy.deepcopy(invasive_species_template)
    },
    "Eurasian Steppes":{
        "Temperature Increase": copy.deepcopy(climate_change_template),
        "Changes in Precipitation": copy.deepcopy(climate_change_template),
        "Land-Use Change": copy.deepcopy(land_use_change_template),
        "Overgrazing": copy.deepcopy(overgrazing_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Wildfires": copy.deepcopy(fire_regime_template),
        "Habitat Fragmentation": copy.deepcopy(fragmentation_template)
    },
    "South American Pampas": {
        "Land-Use Change": copy.deepcopy(land_use_change_template),
        "Habitat Fragmentation": copy.deepcopy(fragmentation_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Overgrazing": copy.deepcopy(overgrazing_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Pollution": copy.deepcopy(pollution_template)
    },
    "Australian Grasslands": {
        "Land-Use Change": copy.deepcopy(land_use_change_template),
        "Habitat Fragmentation": copy.deepcopy(fragmentation_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Overgrazing": copy.deepcopy(overgrazing_template),
        "Wildfires": copy.deepcopy(fire_regime_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Pollution": copy.deepcopy(pollution_template)
    },
    "South American Cerrado": {
        "Temperature Increase": copy.deepcopy(climate_change_template),
        "Habitat Fragmentation": copy.deepcopy(fragmentation_template),
        "Government Policies": copy.deepcopy(land_use_change_template),
        "Changes in Precipitation": copy.deepcopy(climate_change_template),
        "Land-Use Change": copy.deepcopy(land_use_change_template),
        "Infrastructure Development": copy.deepcopy(infrastructure_development_template),
        "Overgrazing": copy.deepcopy(overgrazing_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Wildfires": copy.deepcopy(fire_regime_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Deforestation": copy.deepcopy(deforestation_template),
        "Agricultural Expansion": copy.deepcopy(land_use_change_template)
    },
    "Appalachian Temperate Forests": {
        "Land-Use Change": copy.deepcopy(land_use_change_template),
        "Habitat Fragmentation": copy.deepcopy(fragmentation_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Air Pollution": copy.deepcopy(air_pollution_template),
        "Overbrowsing (Deer)": copy.deepcopy(overgrazing_template), #Using overgrazing as base
        "Forestry Practices": copy.deepcopy(land_use_change_template),
        "Mining": copy.deepcopy(land_use_change_template), #Using land use as a generic template
        "Acid Deposition": copy.deepcopy(air_pollution_template) #Using air pollution as a base.
    },
    "Chilean Temperate Forests": {
        "Land-Use Change": copy.deepcopy(land_use_change_template),
        "Habitat Fragmentation": copy.deepcopy(fragmentation_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Forestry Practices": copy.deepcopy(land_use_change_template),
        "Introduced Species (Mammals)": copy.deepcopy(invasive_species_template),  # Using invasive species as a base
        "Fire Regimes": copy.deepcopy(fire_regime_template)
    },
    "East Asian Temperate Forests": {
        "Land-Use Change": copy.deepcopy(land_use_change_template),
        "Habitat Fragmentation": copy.deepcopy(fragmentation_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Air Pollution": copy.deepcopy(air_pollution_template),
        "Overexploitation (Plants)": copy.deepcopy(overexploitation_template), # Using overexploitation as base
        "Forestry Practices": copy.deepcopy(land_use_change_template)
    },
    "European Temperate Forests": {
        "Land-Use Change": copy.deepcopy(land_use_change_template),
        "Habitat Fragmentation": copy.deepcopy(fragmentation_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Air Pollution": copy.deepcopy(air_pollution_template),
        "Overbrowsing (Deer)": copy.deepcopy(overgrazing_template), # Using overgrazing template
        "Forestry Practices": copy.deepcopy(land_use_change_template),
        "Acid Deposition": copy.deepcopy(air_pollution_template)
    },
    "Pacific Northwest Temperate Forests": {
        "Land-Use Change": copy.deepcopy(land_use_change_template),
        "Habitat Fragmentation": copy.deepcopy(fragmentation_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Forestry Practices": copy.deepcopy(land_use_change_template),
        "Fire Regimes": copy.deepcopy(fire_regime_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Stream Alteration": copy.deepcopy(water_stress_template) # Using water stress as generic
    },
    "Canadian Boreal Forests": {
        "Climate Change": copy.deepcopy(climate_change_template),
        "Fire Regimes": copy.deepcopy(fire_regime_template),
        "Forestry Practices": copy.deepcopy(land_use_change_template),
        "Mining and Energy Development": copy.deepcopy(land_use_change_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Insect Outbreaks": copy.deepcopy(invasive_species_template), # Using invasive species as a template
        "Habitat Fragmentation": copy.deepcopy(fragmentation_template),
        "Permafrost Thaw": copy.deepcopy(climate_change_template) #Using climate change as a base
    },

    "Russian Boreal Forests": {
        "Climate Change": copy.deepcopy(climate_change_template),
        "Fire Regimes": copy.deepcopy(fire_regime_template),
        "Forestry Practices": copy.deepcopy(land_use_change_template),
        "Mining and Energy Development": copy.deepcopy(land_use_change_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Insect Outbreaks": copy.deepcopy(invasive_species_template), #Using invasive species as template.
        "Habitat Fragmentation": copy.deepcopy(fragmentation_template),
        "Permafrost Thaw": copy.deepcopy(climate_change_template),  #Using climate change as a template
        "Illegal Logging": copy.deepcopy(land_use_change_template) # Using land-use as template.
    },
    "Scandinavian and Finnish Boreal Forests": {
        "Climate Change": copy.deepcopy(climate_change_template),
        "Fire Regimes": copy.deepcopy(fire_regime_template),
        "Forestry Practices": copy.deepcopy(land_use_change_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Insect Outbreaks": copy.deepcopy(invasive_species_template), # Using invasive species template
        "Habitat Fragmentation": copy.deepcopy(fragmentation_template),
    },
    "Alps Mountains": {
        "Climate Change": copy.deepcopy(climate_change_template),
        "Tourism and Recreation": copy.deepcopy(land_use_change_template), #Using land-use as a base
        "Habitat Fragmentation": copy.deepcopy(fragmentation_template),
        "Land-Use Change": copy.deepcopy(land_use_change_template),
        "Air Pollution": copy.deepcopy(air_pollution_template),
        "Changes in Water Availability": copy.deepcopy(climate_change_template) #Using CC as a template
    },
    "Andes Mountains": {
        "Climate Change": copy.deepcopy(climate_change_template),
        "Land-Use Change": copy.deepcopy(land_use_change_template),
        "Mining": copy.deepcopy(land_use_change_template),
        "Habitat Fragmentation": copy.deepcopy(fragmentation_template),
        "Glacier Retreat": copy.deepcopy(climate_change_template), # Using CC template
        "Overgrazing": copy.deepcopy(overgrazing_template),
        "Invasive Species": copy.deepcopy(invasive_species_template)
    },
    "Ethiopian Highlands Mountains": {
        "Climate Change": copy.deepcopy(climate_change_template),
        "Land-Use Change": copy.deepcopy(land_use_change_template),
        "Soil Erosion": copy.deepcopy(land_use_change_template),  # Using land-use change as base
        "Overgrazing": copy.deepcopy(overgrazing_template),
        "Deforestation": copy.deepcopy(deforestation_template),
        "Population Growth": copy.deepcopy(climate_change_template) # Using CC as generic template
    },
     "Himalayas Mountains": {
        "Climate Change": copy.deepcopy(climate_change_template),
        "Land-Use Change": copy.deepcopy(land_use_change_template),
        "Overgrazing": copy.deepcopy(overgrazing_template),
        "Deforestation": copy.deepcopy(deforestation_template),
        "Tourism": copy.deepcopy(infrastructure_development_template), # Using infrastructure as base
        "Pollution": copy.deepcopy(pollution_template),
        "Glacier Retreat": copy.deepcopy(climate_change_template),
        "Black Carbon Deposition": copy.deepcopy(pollution_template)
    },
    "Rocky Mountains": {
        "Climate Change": copy.deepcopy(climate_change_template),
        "Land-Use Change": copy.deepcopy(land_use_change_template),
        "Fire Suppression": copy.deepcopy(fire_regime_template), # Using fire regime
        "Mining": copy.deepcopy(land_use_change_template), # Using land use
        "Recreation and Tourism": copy.deepcopy(infrastructure_development_template), # Using infrastructure
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Air Pollution": copy.deepcopy(air_pollution_template)
    },
    "Alpine Tundra": {
        "Temperature Increase": copy.deepcopy(climate_change_template),
        "Changes in Precipitation": copy.deepcopy(climate_change_template),
        "Infrastructure Development": copy.deepcopy(infrastructure_development_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Overgrazing": copy.deepcopy(overgrazing_template),
        "Invasive Species": copy.deepcopy(invasive_species_template)
    },
   "Arctic Tundra": {
        "Infrastructure Development": copy.deepcopy(infrastructure_development_template),
        "Temperature Increase": copy.deepcopy(climate_change_template),
        "Changes in Precipitation": copy.deepcopy(climate_change_template),
        "Permafrost Thaw": copy.deepcopy(climate_change_template), #Using as base
        "Sea Ice Loss (indirect)": copy.deepcopy(climate_change_template), #Using as base
        "Pollution": copy.deepcopy(pollution_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Economic Growth": copy.deepcopy(infrastructure_development_template), # Using as a base
        "Geopolitical Factors": copy.deepcopy(infrastructure_development_template), # Using as a base
        "Government Policies": copy.deepcopy(infrastructure_development_template), # Using as a base
        "Global Commodity Prices": copy.deepcopy(infrastructure_development_template), # Using as a base
        "Technological Advancements": copy.deepcopy(infrastructure_development_template),# Using as a base
        "Long-Range Transport of Pollutants": copy.deepcopy(pollution_template),
        "Local Sources": copy.deepcopy(pollution_template),
        "Disturbance": copy.deepcopy(invasive_species_template), #Using as a base template
        "Increased Human Activity": copy.deepcopy(invasive_species_template),
        "Native Plant Communities": copy.deepcopy(invasive_species_template),
        "Hydrology": copy.deepcopy(altered_hydrology_template),
        "Vegetation Changes": copy.deepcopy(land_use_change_template),
        "Coastal Erosion": copy.deepcopy(land_use_change_template),
        "Regional Climate": copy.deepcopy(climate_change_template),
        "Shrubification": copy.deepcopy(land_use_change_template),
        "Wildlife Disturbance": copy.deepcopy(invasive_species_template),
        "Wildlife Populations": copy.deepcopy(invasive_species_template),
        "Wildlife Health": copy.deepcopy(invasive_species_template)
    },
    "Camargue Wetlands": {
        "Altered Hydrology": copy.deepcopy(altered_hydrology_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Tourism": copy.deepcopy(infrastructure_development_template), # Using infrastructure as base
        "Sea Level Rise" : copy.deepcopy(climate_change_template), # Using CC as base
        "Agriculture": copy.deepcopy(land_use_change_template)
    },
    "Danube Delta Wetlands": {
        "Altered Hydrology": copy.deepcopy(altered_hydrology_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Eutrophication": copy.deepcopy(pollution_template), # Using pollution as template.
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Overfishing": copy.deepcopy(overfishing_template),
        "Tourism and Recreation": copy.deepcopy(infrastructure_development_template), # Infrastructure as template
        "Climate Change": copy.deepcopy(climate_change_template),
        "Agriculture": copy.deepcopy(land_use_change_template)
    },
    "Everglades Wetlands": {
        "Altered Hydrology": copy.deepcopy(altered_hydrology_template),
        "Nutrient Pollution": copy.deepcopy(pollution_template), # Specific for nutrients
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Sea Level Rise": copy.deepcopy(climate_change_template), # Using CC as a base
        "Urban Development": copy.deepcopy(land_use_change_template),
        "Agricultural Runoff": copy.deepcopy(pollution_template) # Using pollution as a base
    },
    "Inner Niger Delta Wetlands": {
        "Altered Hydrology": copy.deepcopy(altered_hydrology_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Overfishing": copy.deepcopy(overfishing_template),
        "Population Growth": copy.deepcopy(climate_change_template), # Using CC as a general template
        "Overgrazing": copy.deepcopy(overgrazing_template),
        "Deforestation": copy.deepcopy(deforestation_template),
        "Water Diversion": copy.deepcopy(water_extraction_template),
        "Pollution": copy.deepcopy(pollution_template)
    },
    "Mesopotamian Marshes Wetlands": {
        "Water Diversion": copy.deepcopy(water_extraction_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Salinization": copy.deepcopy(pollution_template), # Using pollution as a base
        "Upstream Dam Construction": copy.deepcopy(infrastructure_development_template) # Using Infrastructure Development as a template
    },
    "Okavango Delta Wetlands": {
        "Water Diversion": copy.deepcopy(water_extraction_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Overfishing": copy.deepcopy(overfishing_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Upstream Water Demand" : copy.deepcopy(water_extraction_template),
        "Government Policies" : copy.deepcopy(water_extraction_template), #Using water extraction as a generic template
        "Tourism": copy.deepcopy(infrastructure_development_template),
        "Agricultural Runoff": copy.deepcopy(pollution_template)
    },
    "Pantanal Wetlands": {
        "Land-Use Change": copy.deepcopy(land_use_change_template),
        "Altered Hydrology": copy.deepcopy(altered_hydrology_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Wildfires": copy.deepcopy(fire_regime_template),
        "Agricultural Expansion": copy.deepcopy(land_use_change_template),
        "Economic Growth": copy.deepcopy(land_use_change_template), #Using as generic
        "Government Policies": copy.deepcopy(land_use_change_template), # Using as generic
        "Infrastructure Development": copy.deepcopy(infrastructure_development_template),
        "Upstream Dam Construction": copy.deepcopy(infrastructure_development_template), #Using infrastructure as a template
        "Deforestation": copy.deepcopy(deforestation_template),
        "Water Diversion": copy.deepcopy(water_extraction_template),
        "Mining Activities": copy.deepcopy(mining_template),
        "Agricultural Runoff": copy.deepcopy(pollution_template),
        "Wildlife Health": copy.deepcopy(invasive_species_template), #Using as a base
        "Temperature": copy.deepcopy(climate_change_template), #Using as a base
        "Changes in Precipitation": copy.deepcopy(climate_change_template),
        "Human Activities": copy.deepcopy(land_use_change_template), #Using as generic
        "Air Quality": copy.deepcopy(pollution_template),#Using pollution
        "Habitat Availability": copy.deepcopy(land_use_change_template),
        "Water Quality": copy.deepcopy(pollution_template),
        "Habitat Fragmentation": copy.deepcopy(fragmentation_template),
        "Global Demand": copy.deepcopy(land_use_change_template), # Using as generic
        "Water Demand": copy.deepcopy(water_extraction_template),
        "Politics" : copy.deepcopy(land_use_change_template), # Using as generic
        "Energy Demand": copy.deepcopy(infrastructure_development_template) # Using as generic
    },
    "Sundarbans Wetlands": {
        "Sea Level Rise": copy.deepcopy(climate_change_template), # Using climate change as a base
        "Salinity Intrusion": copy.deepcopy(pollution_template), #Using pollution as base
        "Climate Change": copy.deepcopy(climate_change_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Overexploitation of Resources": copy.deepcopy(overfishing_template), #Using overfishing
        "Cyclone Frequency and Intensity": copy.deepcopy(climate_change_template), # Using climate change
        "Reduced Freshwater Flow": copy.deepcopy(water_extraction_template)
    },
    "Arabian Deserts": {
        "Overgrazing": copy.deepcopy(overgrazing_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Water Scarcity": copy.deepcopy(water_extraction_template),
        "Desertification": copy.deepcopy(desertification_template),  # Using the desertification template
        "Urbanization": copy.deepcopy(urbanization_template),
        "Off-Road Vehicle Use": copy.deepcopy(infrastructure_development_template), # Using infrastructure as a general template
        "Oil and Gas Extraction": copy.deepcopy(mining_template) # Using mining as base
    },
    "Atacama Deserts": {
        "Mining Activities": copy.deepcopy(mining_template),
        "Water Scarcity": copy.deepcopy(water_extraction_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Tourism": copy.deepcopy(infrastructure_development_template), # Infrastructure as template
        "Light Pollution": copy.deepcopy(pollution_template), #Using pollution as a template
        "Off-Road Vehicle Use": copy.deepcopy(infrastructure_development_template) # Using infrastructure.
    },
    "Australian Deserts": {
        "Climate Change": copy.deepcopy(climate_change_template),
        "Overgrazing": copy.deepcopy(overgrazing_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Feral Animals": copy.deepcopy(invasive_species_template),  # Using invasive species template
        "Fire Regimes": copy.deepcopy(fire_regime_template),
        "Mining": copy.deepcopy(mining_template),
        "Tourism": copy.deepcopy(infrastructure_development_template), #Using infrastructure
        "Water Extraction": copy.deepcopy(water_extraction_template)
    },
    "Chihuahuan Deserts": {
        "Overgrazing": copy.deepcopy(overgrazing_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Water Scarcity": copy.deepcopy(water_extraction_template),
        "Shrub Encroachment": copy.deepcopy(invasive_species_template),  # Using invasive species as a base
        "Urbanization": copy.deepcopy(urbanization_template),
        "Mining": copy.deepcopy(mining_template),
        "Agricultural Expansion": copy.deepcopy(land_use_change_template)
    },
    "Gobi Deserts": {
        "Climate Change": copy.deepcopy(climate_change_template),
        "Overgrazing": copy.deepcopy(overgrazing_template),
        "Desertification": copy.deepcopy(land_use_change_template), # Using land-use change as a base.
        "Mining": copy.deepcopy(mining_template),
        "Infrastructure Development": copy.deepcopy(infrastructure_development_template),
        "Pollution": copy.deepcopy(pollution_template)
    },
    "Kalahari Deserts": {
        "Climate Change": copy.deepcopy(climate_change_template),
        "Overgrazing": copy.deepcopy(overgrazing_template),
        "Bush Encroachment": copy.deepcopy(invasive_species_template), # Using invasive species as a base
        "Water Extraction": copy.deepcopy(water_extraction_template),
        "Land-Use Change": copy.deepcopy(land_use_change_template),
        "Tourism": copy.deepcopy(infrastructure_development_template)
    },
    "Mojave Deserts": {
        "Climate Change": copy.deepcopy(climate_change_template),
        "Water Extraction": copy.deepcopy(water_extraction_template),
        "Land-Use Change": copy.deepcopy(land_use_change_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Off-Road Vehicle Use": copy.deepcopy(infrastructure_development_template), # Using infrastructure as a base
        "Pollution": copy.deepcopy(pollution_template),
        "Military Activities": copy.deepcopy(land_use_change_template)
    },
    "Namib Deserts": {
        "Climate Change": copy.deepcopy(climate_change_template),
        "Mining": copy.deepcopy(mining_template),
        "Coastal Development": copy.deepcopy(infrastructure_development_template), #Using infrastructure
        "Off-Road Driving": copy.deepcopy(infrastructure_development_template), # Using infrastructure
        "Water Extraction": copy.deepcopy(water_extraction_template)
    },
    "Sahara Deserts": {
        "Climate Change": copy.deepcopy(climate_change_template),
        "Desertification": copy.deepcopy(desertification_template),
        "Overgrazing": copy.deepcopy(overgrazing_template),
        "Water Scarcity": copy.deepcopy(water_extraction_template),
        "Land-Use Change": copy.deepcopy(land_use_change_template),
        "Dust Storms": copy.deepcopy(climate_change_template), # Using Climate Change
        "Political Instability": copy.deepcopy(governance_template)
    },
    "Sonoran Deserts": {
        "Climate Change": copy.deepcopy(climate_change_template),
        "Water Extraction": copy.deepcopy(water_extraction_template),
        "Land-Use Change": copy.deepcopy(land_use_change_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Urbanization": copy.deepcopy(land_use_change_template), # Using land-use as a base
        "Border Wall Impacts": copy.deepcopy(infrastructure_development_template) #Infrastructure as base
    },
    "Agroforestry": {
        "Land Use Change": copy.deepcopy(land_use_change_template),
        "Management Practices": copy.deepcopy(land_use_change_template), #Using land use as general template
        "Climate Change": copy.deepcopy(climate_change_template),
        "Pest and Disease Outbreaks": copy.deepcopy(invasive_species_template), #Using invasive as a base
        "Soil Degradation": copy.deepcopy(land_use_change_template), # Using land use change
        "Water Availability": copy.deepcopy(climate_change_template), # Using CC as a base
        "Market Access": copy.deepcopy(land_use_change_template), # Using as a general template
        "Farmer Knowledge and Skills": copy.deepcopy(land_use_change_template), # Using as a general template
        "Economic Incentives": copy.deepcopy(land_use_change_template),  # Using as a general template
        "Government Policies": copy.deepcopy(land_use_change_template), # Using as a general template
        "Population Pressure": copy.deepcopy(land_use_change_template), # Using as a general template
        "Access to Resources": copy.deepcopy(land_use_change_template), # Using as a general template
        "Carbon Sequestration": copy.deepcopy(climate_change_template), # Using as base
        "Tree and Crop Productivity": copy.deepcopy(land_use_change_template),# Using as generic
        "Introduction of Exotic Species": copy.deepcopy(invasive_species_template), # Using invasive
        "Erosion": copy.deepcopy(land_use_change_template), #Generic
        "Water Use": copy.deepcopy(water_extraction_template)
    },
    "Aquaculture": {
        "Water Pollution": copy.deepcopy(pollution_template),
        "Habitat Conversion": copy.deepcopy(land_use_change_template),
        "Disease Outbreaks": copy.deepcopy(invasive_species_template), # Using invasive_species as a base
        "Escaped Fish": copy.deepcopy(invasive_species_template), # Using invasive species as base
        "Introduction of Non-Native Species": copy.deepcopy(invasive_species_template),
        "Feed Sourcing": copy.deepcopy(overfishing_template), # Using overfishing as base
        "Genetic Impacts": copy.deepcopy(invasive_species_template) # Using invasive_species
    },
    "Intensive Croplands": {
        "Land-Use Change": copy.deepcopy(land_use_change_template),
        "Soil Degradation": copy.deepcopy(land_use_change_template), #Using as base
        "Water Pollution": copy.deepcopy(pollution_template),
        "Pesticide Use": copy.deepcopy(pollution_template), #Using pollution as base
        "Habitat Loss": copy.deepcopy(land_use_change_template),
        "Genetic Homogeneity": copy.deepcopy(invasive_species_template), #Using invasive_species as base for lack of diversity
        "Climate Change": copy.deepcopy(climate_change_template),
        "Water Use": copy.deepcopy(water_extraction_template),
        "Energy Use": copy.deepcopy(climate_change_template),  # Using climate change as a general template for energy
        "Soil Erosion": copy.deepcopy(land_use_change_template), # Using land use change
        "Agricultural Expansion": copy.deepcopy(land_use_change_template)
    },
    "Pastoral Lands": {
        "Overgrazing": copy.deepcopy(overgrazing_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Land Use Change": copy.deepcopy(land_use_change_template),
        "Soil Degradation": copy.deepcopy(land_use_change_template), # Using land-use change as a base
        "Water Availability": copy.deepcopy(climate_change_template), # Using climate change as a base
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Socioeconomic Factors": copy.deepcopy(land_use_change_template),# Using as generic
        "Stocking Rates": copy.deepcopy(overgrazing_template), # Part of overgrazing
        "Grazing Management Practices": copy.deepcopy(land_use_change_template), # Using as generic
        "Climate Variability": copy.deepcopy(climate_change_template),
        "Land Tenure and Access Rights": copy.deepcopy(land_use_change_template), # Using as generic
        "Desertification": copy.deepcopy(land_use_change_template), # Using land use change
        "Water Quality": copy.deepcopy(pollution_template),
        "Vegetation Changes": copy.deepcopy(land_use_change_template),
        "Wildfires": copy.deepcopy(fire_regime_template),
        "Forage Production": copy.deepcopy(climate_change_template) # Using CC as template
    },
    "Plantations": {
        "Monoculture": copy.deepcopy(invasive_species_template),  # Using invasive_species as a template for lack of diversity
        "Land Conversion": copy.deepcopy(land_use_change_template),
        "Pesticide Use": copy.deepcopy(pollution_template),
        "Fertilizer Use": copy.deepcopy(pollution_template),
        "Water Use": copy.deepcopy(water_extraction_template),
        "Soil Erosion": copy.deepcopy(land_use_change_template), #Using land use as generic
        "Climate Change": copy.deepcopy(climate_change_template),
        "Pest and Disease Outbreaks": copy.deepcopy(invasive_species_template), #Using invasive species as a base
        "Soil Degradation": copy.deepcopy(land_use_change_template) # Using land use change
    },
    "Urban Ecosystems": {
        "Habitat Loss and Fragmentation": copy.deepcopy(fragmentation_template),
        "Urban Heat Island Effect": copy.deepcopy(climate_change_template), # Using climate change as base
        "Pollution": copy.deepcopy(pollution_template),
        "Altered Hydrology": copy.deepcopy(altered_hydrology_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Urban Sprawl": copy.deepcopy(land_use_change_template),
        "Population Growth": copy.deepcopy(land_use_change_template), # Using as a base
        "Economic Development": copy.deepcopy(land_use_change_template), #Using as a base
        "Infrastructure Development": copy.deepcopy(infrastructure_development_template),
        "Loss of Vegetation": copy.deepcopy(land_use_change_template),
        "Impervious Surfaces": copy.deepcopy(land_use_change_template),# Using as a base
        "Anthropogenic Heat Release": copy.deepcopy(climate_change_template), # Using as base
       "Industrial Activity": copy.deepcopy(pollution_template), #Using pollution
        "Transportation": copy.deepcopy(infrastructure_development_template), # Using infrastructure
        "Waste Disposal": copy.deepcopy(pollution_template), #Using pollution
        "Construction": copy.deepcopy(infrastructure_development_template) # Using infrastructure
    },
    "Abyssal Plains": {
        "Deep-Sea Mining": copy.deepcopy(mining_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Plastic Pollution": copy.deepcopy(pollution_template),
        "Sedimentation": copy.deepcopy(pollution_template), # Using as a general base
        "Ocean Acidification": copy.deepcopy(ocean_acidification_template),
        "Bottom Trawling": copy.deepcopy(fishing_template) # Using as a base (even if less frequent)
    },
    "African Great Lakes": {
        "Overfishing": copy.deepcopy(overfishing_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Sedimentation": copy.deepcopy(land_use_change_template), # Using land-use as a base.
        "Eutrophication": copy.deepcopy(pollution_template) # Using pollution
    },
    "Cold-Water Corals": {
        "Bottom Trawling": copy.deepcopy(overfishing_template), # Using overfishing as a template
        "Climate Change": copy.deepcopy(climate_change_template),
        "Ocean Acidification": copy.deepcopy(ocean_acidification_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Deep-Sea Mining": copy.deepcopy(mining_template),
        "Oil and Gas Exploration/Extraction": copy.deepcopy(infrastructure_development_template) #Using infrastructure development
    },
    "Great Lakes": {  # Corrected ecosystem name
        "Pollution": copy.deepcopy(pollution_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Coastal Development": copy.deepcopy(land_use_change_template),
        "Water Level Fluctuations": copy.deepcopy(climate_change_template),  # Using Climate Change as a base
        "Overfishing": copy.deepcopy(overfishing_template), #Include, even if less of an issue NOW
        "Eutrophication": copy.deepcopy(pollution_template),
        "Habitat Loss": copy.deepcopy(land_use_change_template)
    },
    "Hydrothermal Vents": {
        "Deep-Sea Mining": copy.deepcopy(mining_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Research Activities": copy.deepcopy(infrastructure_development_template), # Using infrastructure as a template
        "Pollution": copy.deepcopy(pollution_template)
    },
    "Australian Kelp Forests": {
        "Climate Change": copy.deepcopy(climate_change_template),
        "Overgrazing": copy.deepcopy(overgrazing_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Coastal Development": copy.deepcopy(infrastructure_development_template)
    },
    "California Kelp Forests": {
        "Climate Change": copy.deepcopy(climate_change_template),
        "Overgrazing": copy.deepcopy(overgrazing_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Coastal Development": copy.deepcopy(infrastructure_development_template),
        "Ocean Acidification": copy.deepcopy(ocean_acidification_template),
        "Fishing": copy.deepcopy(fishing_template) # Includes impacts on predators of urchins
    },
    "North Atlantic Kelp Forests": {
        "Climate Change": copy.deepcopy(climate_change_template),
        "Overfishing": copy.deepcopy(overfishing_template),
        "Coastal Development": copy.deepcopy(infrastructure_development_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Ocean Acidification": copy.deepcopy(ocean_acidification_template)
    },
    "Pacific Northwest Kelp Forests": {
        "Climate Change": copy.deepcopy(climate_change_template),
        "Overgrazing": copy.deepcopy(overgrazing_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Coastal Development": copy.deepcopy(infrastructure_development_template),
        "Ocean Acidification": copy.deepcopy(ocean_acidification_template),
        "Fishing": copy.deepcopy(overfishing_template) #Using overfishing template.
    },
    "South American Kelp Forests": {
        "Climate Change": copy.deepcopy(climate_change_template),
        "Overfishing": copy.deepcopy(overfishing_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Coastal Development": copy.deepcopy(infrastructure_development_template),
        "Sea Urchin Harvesting": copy.deepcopy(overfishing_template), # Using overfishing as a template
        "Invasive Species": copy.deepcopy(invasive_species_template)
    },
    "Lake Baikal": {
        "Climate Change": copy.deepcopy(climate_change_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Eutrophication": copy.deepcopy(pollution_template),  #Using pollution as base.
        "Overexploitation": copy.deepcopy(overfishing_template), # Using overfishing
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Tourism": copy.deepcopy(infrastructure_development_template)
    },
    "Australian Mangroves": {
        "Climate Change": copy.deepcopy(climate_change_template),
        "Coastal Development": copy.deepcopy(infrastructure_development_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Altered Hydrology": copy.deepcopy(altered_hydrology_template),
        "Overexploitation": copy.deepcopy(overfishing_template) # Using as base.
    },
    "East African Mangroves": {
        "Climate Change": copy.deepcopy(climate_change_template),
        "Coastal Development": copy.deepcopy(infrastructure_development_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Overexploitation": copy.deepcopy(overfishing_template),  # Using overfishing as a template
        "Altered Hydrology": copy.deepcopy(altered_hydrology_template)
    },
    "Mesoamerican Mangroves": {
        "Coastal Development": copy.deepcopy(infrastructure_development_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Overexploitation": copy.deepcopy(overfishing_template),  # Using overfishing
        "Deforestation": copy.deepcopy(deforestation_template),
        "Altered Hydrology": copy.deepcopy(altered_hydrology_template)
    },
    "Southeast Asian Mangroves": {
        "Coastal Development": copy.deepcopy(infrastructure_development_template),
        "Aquaculture Expansion": copy.deepcopy(land_use_change_template), # Using land-use change
        "Deforestation": copy.deepcopy(deforestation_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Overexploitation": copy.deepcopy(overfishing_template), #Using overfishing as base.
        "Sedimentation": copy.deepcopy(pollution_template) # Using as a base
    },
    "Sundarbans Mangroves": {
        "Climate Change": copy.deepcopy(climate_change_template),
        "Sea Level Rise": copy.deepcopy(climate_change_template), # Using CC as a base
        "Salinity Intrusion": copy.deepcopy(pollution_template), # Using pollution as a base
        "Pollution": copy.deepcopy(pollution_template),
        "Overexploitation of Resources": copy.deepcopy(overfishing_template), #Using overfishing
        "Cyclone Frequency and Intensity": copy.deepcopy(climate_change_template),
        "Reduced Freshwater Flow": copy.deepcopy(water_extraction_template)
    },
    "Open Ocean": {  # Corrected ecosystem name
        "Overfishing": copy.deepcopy(overfishing_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Plastic Pollution": copy.deepcopy(pollution_template),
        "Chemical Pollution": copy.deepcopy(pollution_template),
        "Noise Pollution": copy.deepcopy(pollution_template)  # Using pollution template as a base
    },
    "Amazon Rivers": {
        "Deforestation": copy.deepcopy(deforestation_template),
        "Dam Construction": copy.deepcopy(infrastructure_development_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Overfishing": copy.deepcopy(overfishing_template),
        "Mining": copy.deepcopy(mining_template)
    },
    "Danube Rivers": {
        "Altered Hydrology": copy.deepcopy(altered_hydrology_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Navigation": copy.deepcopy(infrastructure_development_template), # Using infrastructure as base
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Overfishing": copy.deepcopy(overfishing_template),
        "Habitat Degradation": copy.deepcopy(land_use_change_template)
    },
    "Mississippi Rivers": {
        "Agricultural Runoff": copy.deepcopy(pollution_template),  # Using pollution as a base
        "Dams and Levees": copy.deepcopy(infrastructure_development_template), #Using infrastructure
        "Climate Change": copy.deepcopy(climate_change_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Channelization": copy.deepcopy(altered_hydrology_template), # Using hydrology
        "Pollution": copy.deepcopy(pollution_template),
        "Overfishing": copy.deepcopy(overfishing_template)
    },
    "Murray-Darling Rivers": {
        "Water Extraction": copy.deepcopy(water_extraction_template),
        "Altered Flow Regimes": copy.deepcopy(altered_hydrology_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Salinity": copy.deepcopy(pollution_template), # Using pollution as a base
        "Habitat Degradation": copy.deepcopy(land_use_change_template)
    },
    "Yangtze Rivers": {
        "Dam Construction": copy.deepcopy(infrastructure_development_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Overfishing": copy.deepcopy(overfishing_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Shipping": copy.deepcopy(infrastructure_development_template), # Using infrastructure as a base
        "Sand Mining": copy.deepcopy(mining_template) #Using mining template
    },
    "Australian Salt Marshes": {
        "Climate Change": copy.deepcopy(climate_change_template),
        "Coastal Development": copy.deepcopy(infrastructure_development_template),
        "Altered Hydrology": copy.deepcopy(altered_hydrology_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Overgrazing": copy.deepcopy(overgrazing_template) # In some areas
    },
    "European Salt Marshes": {
        "Sea Level Rise": copy.deepcopy(climate_change_template), # Using CC
        "Coastal Development": copy.deepcopy(infrastructure_development_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Land Reclamation": copy.deepcopy(land_use_change_template),
        "Changes in Sediment Supply": copy.deepcopy(altered_hydrology_template) # Using hydrology as base
    },
    "Gulf of Mexico Salt Marshes": {
        "Sea Level Rise": copy.deepcopy(climate_change_template), #using climate change
        "Coastal Development": copy.deepcopy(infrastructure_development_template),
        "Oil Spills and Pollution": copy.deepcopy(pollution_template),
        "Altered Hydrology and Sedimentation": copy.deepcopy(altered_hydrology_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Nutrient Loading": copy.deepcopy(pollution_template) # Using pollution
    },
    "North American Atlantic Coast Salt Marshes": {
        "Sea Level Rise": copy.deepcopy(climate_change_template), # Using CC template
        "Coastal Development": copy.deepcopy(infrastructure_development_template),
        "Altered Hydrology": copy.deepcopy(altered_hydrology_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Invasive Species": copy.deepcopy(invasive_species_template)
    },
    "San Francisco Bay Salt Marshes": {
        "Historical Habitat Loss": copy.deepcopy(land_use_change_template), # Using land-use change
        "Sea Level Rise": copy.deepcopy(climate_change_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Altered Hydrology": copy.deepcopy(altered_hydrology_template)
    },
    "Australian Seagrass": {
        "Climate Change": copy.deepcopy(climate_change_template),
        "Water Quality Degradation": copy.deepcopy(pollution_template),
        "Physical Damage": copy.deepcopy(infrastructure_development_template), # Using infrastructure template
        "Coastal Development": copy.deepcopy(infrastructure_development_template),
        "Overfishing": copy.deepcopy(overfishing_template)
    },
    "Florida Bay Seagrass": {
        "Water Quality Degradation": copy.deepcopy(pollution_template),
        "Physical Damage": copy.deepcopy(infrastructure_development_template), #Using infrastructure
        "Climate Change": copy.deepcopy(climate_change_template),
        "Altered Hydrology": copy.deepcopy(altered_hydrology_template),
        "Overfishing": copy.deepcopy(overfishing_template)
    },
    "Mediterranean Seagrass": {
        "Coastal Development": copy.deepcopy(infrastructure_development_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Fishing Activities": copy.deepcopy(overfishing_template),  # Using overfishing as a base, includes trawling
        "Anchoring": copy.deepcopy(infrastructure_development_template) #Using infrastructure
    },
    "Southeast Asian Seagrass": {
        "Coastal Development": copy.deepcopy(infrastructure_development_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Destructive Fishing Practices": copy.deepcopy(fishing_template), #Using fishing as base
        "Sedimentation": copy.deepcopy(pollution_template), # Using pollution
        "Overfishing": copy.deepcopy(overfishing_template)
    },
    "Seamounts": {
        "Bottom Trawling": copy.deepcopy(overfishing_template),  # Using overfishing template
        "Deep-Sea Mining": copy.deepcopy(mining_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Plastic Pollution": copy.deepcopy(pollution_template),
        "Ocean Acidification": copy.deepcopy(ocean_acidification_template)
    },
    "Smaller Lakes and Ponds": {
        "Nutrient Pollution (Eutrophication)": copy.deepcopy(pollution_template),
        "Climate Change": copy.deepcopy(climate_change_template),
        "Acidification": copy.deepcopy(ocean_acidification_template),
        "Water Withdrawals": copy.deepcopy(water_extraction_template),
        "Pollution": copy.deepcopy(pollution_template),
        "Invasive Species": copy.deepcopy(invasive_species_template),
        "Habitat Alteration": copy.deepcopy(land_use_change_template),
    },
}

# --- Amazon Rainforest ---
# (Populate as before, but directly in Python)
amazon = all_stressors_data["Amazon Rainforest"]  # shorter name

amazon["Infrastructure Development"]["Metric"] = "Length of new roads constructed per year (km/year) within the Amazon region, and/or area directly affected by other infrastructure projects (dams, pipelines, mining operations) (ha/year)."
amazon["Infrastructure Development"]["Data Sources"] = [
    "Brazilian Ministry of Infrastructure",
    "Brazilian Institute of Geography and Statistics (IBGE)",
    "Remote sensing data (satellite imagery)",
     "Reports from environmental NGOs and research institutions (e.g., Imazon, Instituto Socioambiental)"
]
amazon["Infrastructure Development"]["Influenced By"] = [
    "Economic Growth",
    "Population Growth",
    "Government Policies",
    "Global Commodity Prices",
   "Technological advancements"
]
amazon["Infrastructure Development"]["Influences"] = [
    "Amazon Rainforest - Deforestation",
    "Amazon Rainforest - Wildfires",
    "Amazon Rainforest - Pollution",
    "Amazon Rainforest - Habitat Fragmentation",
]
amazon["Infrastructure Development"]["Logic Description"] = "The construction of new infrastructure (primarily roads, but also dams, pipelines, and mining operations) results in a direct loss of rainforest area proportional to the length of roads built or the area affected by other projects. This loss of area reduces the total available habitat for rainforest species. Furthermore, infrastructure fragments the remaining forest, creating smaller, isolated patches.  This fragmentation reduces the effective habitat size for many species, disrupts ecological processes (like seed dispersal and animal movement), and increases edge effects (making the forest more vulnerable to external influences). Increased human access via roads leads to secondary impacts, such as increased hunting, poaching, and illegal logging, further reducing biodiversity. Dams significantly alter river flows, impacting both upstream and downstream ecosystems."
amazon["Infrastructure Development"]["Impact Function"] = "impact_infrastructure_development_amazon_rainforest"

amazon["Deforestation"]["Metric"] = "Area of forest cleared per year (hectares/year or km²/year)."
amazon["Deforestation"]["Data Sources"] = [
    "Remote sensing data (satellite imagery) from sources like Brazil's National Institute for Space Research (INPE) (PRODES and DETER projects).",
    "Land-use change models.",
    "Reports from environmental NGOs and research institutions."
]
amazon["Deforestation"]["Impact on Area"] = "Direct reduction of rainforest area."
amazon["Deforestation"]["Impact on Biodiversity"] = "Habitat loss and fragmentation, leading to population decline and increased extinction risk.\nLoss of carbon storage, contributing to climate change.\nDisruption of ecological processes (e.g., seed dispersal, pollination).\nIncreased edge effects."
amazon["Deforestation"]["Influenced By"] = [
    "Amazon Rainforest - Infrastructure Development",
    "Economic Growth",
    "Global Commodity Prices",
    "Population Growth",
    "Government Policies"
]
amazon["Deforestation"]["Influences"] = [
    "Amazon Rainforest - Wildfires",
    "Amazon Rainforest - Changes in Precipitation",
    "Amazon Rainforest - Temperature Increase",
    "Amazon Rainforest - Habitat Fragmentation",
]
amazon["Deforestation"]["Logic Description"] = "Deforestation is the direct removal of forest cover, primarily for agriculture (cattle ranching, soy farming), logging, and mining. The metric directly measures the area lost. This loss of area directly reduces habitat for species and fragments the remaining forest, leading to biodiversity loss.  The drivers of deforestation are interconnected, with economic factors and infrastructure development playing significant roles.  Deforestation contributes to other stressors, like wildfires and potentially regional climate change."
amazon["Deforestation"]["Impact Function"] = "impact_deforestation_amazon_rainforest"

amazon["Temperature Increase"]["Metric"] = "Average annual temperature increase (°C) above a pre-industrial baseline"
amazon["Temperature Increase"]["Data Sources"] = [
    "Global climate models (GCMs) projections (e.g., CMIP6, specifically RCP scenarios)",
    "Regional climate models downscaled for the Amazon basin",
    "Historical temperature records from weather stations in the region (if available and reliable).",
    "IPCC reports (Assessment Reports and Special Reports)"
]
amazon["Temperature Increase"]["Impact on Area"] = "Indirect; exacerbates other stressors and could lead to biome shifts at high temperature increases"
amazon["Temperature Increase"]["Impact on Biodiversity"] = "Shifts in species distributions, as species move to track suitable climates.\nIncreased physiological stress on species, particularly those with narrow thermal tolerances.\nIncreased risk of exceeding thermal limits, leading to mortality.\nChanges in phenology (timing of biological events).\nIncreased susceptibility to diseases and pests."
amazon["Temperature Increase"]["Influenced By"] = [
    "Global Greenhouse Gas Emissions",
    "Amazon Rainforest - Deforestation"
]
amazon["Temperature Increase"]["Influences"] = [
    "Amazon Rainforest - Wildfires",
    "Amazon Rainforest - Changes in Precipitation",
    "Amazon Rainforest - Drought Frequency and Severity", #Not defined, but good to include
]
amazon["Temperature Increase"]["Logic Description"] = "Temperature increase is primarily driven by global greenhouse gas emissions, but deforestation within the Amazon also contributes locally. While not directly reducing area, increased temperature acts as a stress multiplier. It pushes species beyond their thermal tolerance limits, alters ecological processes, and increases the risk and severity of other stressors like wildfires."
amazon["Temperature Increase"]["Impact Function"] = "impact_temperature_increase_amazon_rainforest"

amazon["Changes in Precipitation"]["Metric"] = "Change in annual precipitation (mm/year) and changes in the length and severity of the dry season (number of months with rainfall below a threshold)."
amazon["Changes in Precipitation"]["Data Sources"] = [
   "Global climate models (GCMs) projections (e.g., CMIP6, specifically RCP scenarios).",
    "Regional climate models downscaled for the Amazon basin.",
    "Historical rainfall records from weather stations in the region.",
    "IPCC reports"
]
amazon["Changes in Precipitation"]["Impact on Area"] = "Indirect, but can lead to changes in vegetation types over long time scales (e.g., savannization)."
amazon["Changes in Precipitation"]["Impact on Biodiversity"] = "Changes in species distributions as rainfall patterns shift, increased drought stress on plants, leading to mortality, altered river flow regimes, affecting aquatic ecosystems, changes in the frequency and intensity of flooding events."
amazon["Changes in Precipitation"]["Influenced By"] = [
    "Global Greenhouse Gas Emissions",
    "Amazon Rainforest - Deforestation",
    "Amazon Rainforest - Temperature Increase"
]
amazon["Changes in Precipitation"]["Influences"] = [
    "Amazon Rainforest - Wildfires",
    "Amazon Rainforest - Species composition changes",
    "Amazon Rainforest - Hydrological Changes"
]
amazon["Changes in Precipitation"]["Logic Description"] = "Changes in precipitation are driven by global climate change and, regionally, by deforestation. The Amazon is particularly sensitive to changes in the length and intensity of the dry season. Decreased rainfall or longer dry seasons lead to increased drought stress on plants, favoring drought-tolerant species and potentially leading to shifts in vegetation types over time. Altered rainfall patterns also affect river systems and the frequency of flooding events."
amazon["Changes in Precipitation"]["Impact Function"] = "impact_precipitation_changes_amazon_rainforest"

amazon["Wildfires"]["Metric"] = "Number of wildfires per year and total area burned (hectares/year)"
amazon["Wildfires"]["Data Sources"] = [
    "Brazilian National Institute for Space Research (INPE) - fire monitoring",
    "Remote sensing data (MODIS, VIIRS)",
   "Reports from fire departments and environmental agencies."
]
amazon["Wildfires"]["Impact on Area"] = "Direct loss of forest cover (in severe cases); changes in vegetation structure"
amazon["Wildfires"]["Impact on Biodiversity"] = "Mortality of plants and animals, habitat loss, changes in species composition, increased susceptibility to future fires, air pollution affecting both human and animal health"
amazon["Wildfires"]["Influenced By"] = [
   "Amazon Rainforest - Deforestation",
    "Amazon Rainforest - Climate Change",
   "Human Activities (accidental or intentional ignitions)",
    "Amazon Rainforest - Land Management Practices"
]
amazon["Wildfires"]["Influences"] = [
    "Air Quality",
    "Carbon Emissions",
   "Amazon Rainforest - Vegetation Regeneration",
    "Amazon Rainforest - Deforestation",
    "Amazon Rainforest - Temperature Increase"
]
amazon["Wildfires"]["Logic Description"] = "Wildfires are a major threat to the Amazon, and their frequency and intensity are increasing due to a combination of factors. Deforestation creates drier, more flammable edges, while climate change (increased temperature and drier conditions) provides the ideal conditions for fires to spread. Human activities are the primary source of ignition. Fires directly burn forest area, killing plants and animals, and release large amounts of carbon dioxide."
amazon["Wildfires"]["Impact Function"] = "impact_wildfires_amazon_rainforest"


amazon["Hydrological Changes"]["Metric"] = "Changes in river flow (cubic meters per second), water levels (meters), flood pulse dynamics (timing, duration, extent of flooding)."
amazon["Hydrological Changes"]["Data Sources"] = [
   "River gauge data (from Brazilian National Water Agency - ANA, and other regional agencies).",
    "Hydrological models.",
    "Remote sensing data (e.g., measuring inundation extent).",
    "Research studies on Amazon hydrology."
]
amazon["Hydrological Changes"]["Impact on Area"] = "Changes in the extent and duration of flooding in floodplain forests (várzea and igapó); changes in river channel morphology."
amazon["Hydrological Changes"]["Impact on Biodiversity"] = "Impacts on aquatic species (fish, invertebrates), riparian vegetation, and wildlife that depend on the flood pulse. Changes in fish migration and spawning. Disruption of nutrient cycles."
amazon["Hydrological Changes"]["Influenced By"] = [
   "Amazon Rainforest - Dam Construction",
    "Amazon Rainforest - Deforestation",
    "Amazon Rainforest - Climate Change",
    "Water Diversions (for irrigation and other uses)"
]
amazon["Hydrological Changes"]["Influences"] = [
    "Amazon Rainforest - Water Availability",
    "Amazon Rainforest - Sediment Transport",
   "Amazon Rainforest - Fish Migration",
    "Amazon Rainforest - Floodplain Ecosystems",
    "Amazon Rainforest - Water Quality"
]
amazon["Hydrological Changes"]["Logic Description"] = "Changes in the Amazon River's hydrology, driven by dams, deforestation, and climate change, impact floodplain ecosystems and aquatic biodiversity. The natural flood pulse is crucial for many species, and alterations to this pulse have cascading effects."
amazon["Hydrological Changes"]["Impact Function"] = "impact_hydrology_changes_amazon_rainforest"

amazon["Overexploitation"]["Metric"] = "Hunting intensity (estimated number of animals killed per unit area per year); population sizes of targeted species (e.g., primates, tapirs, peccaries, game birds)."
amazon["Overexploitation"]["Data Sources"] = [
     "Wildlife surveys (often challenging in the Amazon).",
    "Hunting records (where available and reliable, often very limited).",
    "Research studies on specific species or areas.",
    "Reports from conservation organizations."
]

amazon["Overexploitation"]["Impact on Area"] = "Indirect, through changes in species populations and ecological interactions."
amazon["Overexploitation"]["Impact on Biodiversity"] = "Decline of populations of large mammals and birds. Loss of seed dispersers and other key functional groups. Altered forest structure and composition (e.g., if large seed dispersers are removed)."
amazon["Overexploitation"]["Influenced By"] = [
     "Hunting (for subsistence and commercial purposes).",
    "Amazon Rainforest - Deforestation",
     "Amazon Rainforest - Infrastructure Development",
     "Weak enforcement of wildlife protection laws."
]
amazon["Overexploitation"]["Influences"] = [
    "Amazon Rainforest - Seed dispersal",
    "Amazon Rainforest - Forest regeneration",
  "Amazon Rainforest - Trophic interactions",
    "Population sizes of targeted species"
]
amazon["Overexploitation"]["Logic Description"] = "Overexploitation of wildlife, particularly large mammals and birds, through hunting can lead to population declines and alter ecological processes like seed dispersal, impacting forest regeneration and overall biodiversity."
amazon["Overexploitation"]["Impact Function"] = "impact_overexploitation_amazon_rainforest"

amazon["Mining"]["Metric"] = "Area affected by mining activities (ha); concentrations of pollutants (e.g., mercury, sediment) in water and sediments."
amazon["Mining"]["Data Sources"] = [
    "Brazilian government mining records (where available).",
    "Remote sensing data (detecting mining areas).",
    "Water quality monitoring data.",
    "Research studies on the impacts of mining."
]
amazon["Mining"]["Impact on Area"] = "Direct habitat loss due to mining operations; pollution of rivers and streams (e.g., mercury from gold mining, sediment from other mining activities)."
amazon["Mining"]["Impact on Biodiversity"] = "Toxic effects of pollutants (especially mercury) on aquatic life and human populations; habitat destruction. Disruption of hydrological regimes."
amazon["Mining"]["Influenced By"] = [
     "Global demand for minerals (gold, iron ore, bauxite, etc.).",
    "Government policies (mining concessions, environmental regulations).",
    "Economic factors (mineral prices)."
]
amazon["Mining"]["Influences"] = [
    "Amazon Rainforest - Water Quality",
   "Amazon Rainforest - Habitat destruction",
    "Amazon Rainforest - Deforestation",
  "Amazon Rainforest - Pollution",
    "Amazon Rainforest - Hydrological Changes"
]
amazon["Mining"]["Logic Description"] = "Mining activities, both legal and illegal, cause deforestation, habitat destruction, and significant pollution, particularly mercury contamination from gold mining, which impacts both aquatic ecosystems and human health."
amazon["Mining"]["Impact Function"] = "impact_mining_amazon_rainforest"

amazon["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., mercury, pesticides, plastics, sediment) in water, sediments, and biota."
amazon["Pollution"]["Data Sources"] = [
    "Water quality monitoring data (from government agencies and research institutions).",
     "Sediment analysis.",
     "Research studies on pollution impacts in the Amazon."
]
amazon["Pollution"]["Impact on Area"] = "Degradation of water quality; contamination of ecosystems."
amazon["Pollution"]["Impact on Biodiversity"] = "Toxic effects on aquatic and terrestrial organisms; bioaccumulation of pollutants in the food chain; reduced reproductive success; increased susceptibility to disease."
amazon["Pollution"]["Influenced By"] = [
       "Amazon Rainforest - Mining Activities",
    "Amazon Rainforest - Agricultural Runoff",
    "Amazon Rainforest - Industrial Discharge",
     "Amazon Rainforest - Urban Runoff",
    "Amazon Rainforest - Deforestation"
]
amazon["Pollution"]["Influences"] = [
  "Amazon Rainforest - Water Quality",
     "Amazon Rainforest - Wildlife Health",
    "Human Health"
]
amazon["Pollution"]["Logic Description"] = "Pollution from a variety of sources impacts the amazon"
amazon["Pollution"]["Impact Function"] = "impact_pollution_amazon_rainforest"


# --- Congo Rainforest ---
congo = all_stressors_data["Congo Rainforest"]

congo["Deforestation"]["Metric"] = "Area of forest cleared per year (hectares/year)."
congo["Deforestation"]["Data Sources"] = [
    "Global Forest Watch",
    "University of Maryland GLAD deforestation alerts",
    "Reports from NGOs (e.g., Rainforest Foundation)",
    "National Forest Inventory data (if available)"
]
congo["Deforestation"]["Impact on Area"] = "Direct reduction of rainforest area."
congo["Deforestation"]["Impact on Biodiversity"] = "Habitat loss and fragmentation, leading to population declines. Loss of carbon storage. Disruption of ecosystem services."
congo["Deforestation"]["Influenced By"] = [
    "Commercial Logging (legal and illegal)",
    "Agricultural Expansion (small-scale and industrial)",
    "Mining",
    "Infrastructure Development",
    "Population Growth",
    "Weak Governance and Law Enforcement"
]
congo["Deforestation"]["Influences"] = [
    "Congo Rainforest - Wildfires",
    "Congo Rainforest - Changes in Precipitation",
     "Congo Rainforest - Habitat Fragmentation"
]
congo["Deforestation"]["Logic Description"] = "Deforestation in the Congo Basin is driven by a combination of factors, including logging, agriculture, mining, and infrastructure. It leads directly to habitat loss and fragmentation, impacting biodiversity."
congo["Deforestation"]["Impact Function"] = "impact_deforestation_congo_rainforest"

congo["Temperature Increase"]["Metric"] = "Average annual temperature increase (°C) above a pre-industrial baseline."
congo["Temperature Increase"]["Data Sources"] = [
    "Global Climate Models (GCMs)",
    "Regional Climate Models",
    "IPCC Reports",
    "Limited local weather station data"
]
congo["Temperature Increase"]["Impact on Area"] = "Indirect; exacerbates other stressors."
congo["Temperature Increase"]["Impact on Biodiversity"] = "Shifts in species ranges, increased stress on species, potential for increased disease outbreaks."
congo["Temperature Increase"]["Influenced By"] = [
    "Global Greenhouse Gas Emissions",
    "Congo Rainforest - Deforestation"
]
congo["Temperature Increase"]["Influences"] = [
   "Congo Rainforest - Wildfires",
    "Congo Rainforest - Changes in Precipitation"
]
congo["Temperature Increase"]["Logic Description"] = "Temperature increase is primarily driven by global greenhouse gas emissions. Deforestation within the Congo Basin can also contribute locally. Higher temperatures exacerbate the impacts of other stressors."
congo["Temperature Increase"]["Impact Function"] = "impact_temperature_increase_congo_rainforest"

congo["Changes in Precipitation"]["Metric"] = "Change in annual precipitation (mm/year) and changes in the dry season length."
congo["Changes in Precipitation"]["Data Sources"] = [
    "Global Climate Models (GCMs)",
    "Regional Climate Models",
    "IPCC Reports",
    "Limited local rainfall data"
]
congo["Changes in Precipitation"]["Impact on Area"] = "Potential for shifts in vegetation types over the long term."
congo["Changes in Precipitation"]["Impact on Biodiversity"] = "Altered water availability for plants and animals, changes in river flow, increased drought or flood risk."
congo["Changes in Precipitation"]["Influenced By"] = [
    "Global Greenhouse Gas Emissions",
    "Congo Rainforest - Deforestation",
]
congo["Changes in Precipitation"]["Influences"] = [
    "Congo Rainforest - Wildfires",
    "Congo Rainforest - Hydrological Changes"

]
congo["Changes in Precipitation"]["Logic Description"] = "Changes in precipitation patterns, influenced by global climate change and regional deforestation, can alter water availability, affecting both terrestrial and aquatic ecosystems in the Congo Basin."
congo["Changes in Precipitation"]["Impact Function"] = "impact_precipitation_changes_congo_rainforest"

congo["Wildfires"]["Metric"] = "Number of fires per year and area burned (hectares/year)."
congo["Wildfires"]["Data Sources"] = [
    "Satellite-based fire detection (e.g., MODIS, VIIRS)",
    "Reports from local communities and authorities (often limited)"
]
congo["Wildfires"]["Impact on Area"] = "Direct loss of forest cover; changes in vegetation structure."
congo["Wildfires"]["Impact on Biodiversity"] = "Direct mortality of plants and animals; habitat loss; increased vulnerability to future fires."
congo["Wildfires"]["Influenced By"] = [
    "Congo Rainforest - Deforestation",
    "Congo Rainforest - Changes in Precipitation",
    "Congo Rainforest - Temperature Increase",
    "Agricultural Practices (slash-and-burn)",
    "Accidental Ignitions"
]
congo["Wildfires"]["Influences"] = [
    "Congo Rainforest - Air Quality",
    "Congo Rainforest - Carbon Emissions",
   "Congo Rainforest - Deforestation"
]
congo["Wildfires"]["Logic Description"] = "While historically less frequent than in the Amazon, wildfires are becoming a growing concern in the Congo Basin, driven by deforestation, climate change, and human activities."
congo["Wildfires"]["Impact Function"] = "impact_wildfires_congo_rainforest"

congo["Overexploitation"]["Metric"] = "Population declines of targeted species (e.g., elephants, gorillas, okapi); bushmeat trade volume."
congo["Overexploitation"]["Data Sources"] = [
    "Wildlife surveys (challenging in the region)",
    "Bushmeat market surveys",
    "Reports from conservation organizations (e.g., WCS, WWF)",
    "CITES trade data"
]
congo["Overexploitation"]["Impact on Area"] = "Indirect, through impacts on species populations and ecological interactions."
congo["Overexploitation"]["Impact on Biodiversity"] = "Population declines of key species; disruption of ecological processes (e.g., seed dispersal); potential for local extinctions."
congo["Overexploitation"]["Influenced By"] = [
    "Hunting (for bushmeat, ivory, and other wildlife products)",
    "Congo Rainforest - Infrastructure Development (roads providing access)",
    "Weak Law Enforcement",
    "Poverty and Food Insecurity"
]
congo["Overexploitation"]["Influences"] = [
    "Congo Rainforest - Forest Structure and Composition",
   "Congo Rainforest - Seed Dispersal",
    "Congo Rainforest - Trophic Cascades"

]
congo["Overexploitation"]["Logic Description"] = "Overexploitation of wildlife, particularly through hunting for bushmeat and the illegal wildlife trade, poses a significant threat to biodiversity in the Congo Basin, leading to population declines and disrupting ecological processes."
congo["Overexploitation"]["Impact Function"] = "impact_overexploitation_congo_rainforest"

congo["Mining"]["Metric"] = "Area affected by mining operations (ha); concentrations of pollutants in water and soil."
congo["Mining"]["Data Sources"] = [
     "Government mining records",
    "Reports from NGOs and research institutions",
    "Remote sensing data",
   "Water and soil quality monitoring data"
]
congo["Mining"]["Impact on Area"] = "Direct habitat loss; pollution of water bodies; soil degradation."
congo["Mining"]["Impact on Biodiversity"] = "Habitat destruction; toxic effects of pollutants on wildlife; disruption of aquatic ecosystems."
congo["Mining"]["Influenced By"] = [
    "Global demand for minerals (e.g., coltan, copper, cobalt, diamonds)",
   "Government policies and mining concessions",
    "Weak environmental regulations"
]
congo["Mining"]["Influences"] = [
   "Congo Rainforest - Deforestation",
    "Congo Rainforest - Pollution",
     "Congo Rainforest - Water Quality",
     "Congo Rainforest - Habitat Fragmentation"
]
congo["Mining"]["Logic Description"] = "Mining, both artisanal and industrial, contributes to deforestation, habitat loss, and pollution in the Congo Basin, particularly affecting water quality and aquatic ecosystems."
congo["Mining"]["Impact Function"] = "impact_mining_congo_rainforest"

congo["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., heavy metals, pesticides, plastic waste) in water, soil, and biota."
congo["Pollution"]["Data Sources"] = [
    "Water and soil quality monitoring data",
   "Research studies",
   "Reports from environmental organizations"
]
congo["Pollution"]["Impact on Area"] = "Degradation of water and soil quality; contamination of ecosystems."
congo["Pollution"]["Impact on Biodiversity"] = "Toxic effects on wildlife; bioaccumulation of pollutants; reduced reproductive success; increased disease susceptibility."
congo["Pollution"]["Influenced By"] = [
    "Congo Rainforest - Mining",
    "Congo Rainforest - Agricultural Runoff",
  "Congo Rainforest - Industrial Activities",
    "Congo Rainforest - Urban Waste",
    "Congo Rainforest - Deforestation"
]
congo["Pollution"]["Influences"] = [
     "Congo Rainforest - Water Quality",
    "Congo Rainforest - Wildlife Health",
    "Human Health"
]
congo["Pollution"]["Logic Description"] = "Pollution from mining, agriculture, industrial activities, and urban waste degrades water and soil quality, impacting both wildlife and human populations."
congo["Pollution"]["Impact Function"] = "impact_pollution_congo_rainforest"

congo["Infrastructure Development"]["Metric"] = "Length of new roads constructed (km/year); area affected by new infrastructure projects (ha/year)."
congo["Infrastructure Development"]["Data Sources"] = [
    "Government infrastructure plans",
    "Reports from development agencies",
   "Remote sensing data"
]
congo["Infrastructure Development"]["Impact on Area"] = "Direct habitat loss; fragmentation of forests."
congo["Infrastructure Development"]["Impact on Biodiversity"] = "Habitat loss and fragmentation; increased access for hunting and poaching; disruption of wildlife movement."
congo["Infrastructure Development"]["Influenced By"] = [
    "Economic Development Plans",
   "Population Growth",
   "Investment in Resource Extraction (mining, logging)"
]
congo["Infrastructure Development"]["Influences"] = [
  "Congo Rainforest - Deforestation",
  "Congo Rainforest - Overexploitation",
   "Congo Rainforest - Habitat Fragmentation"
]
congo["Infrastructure Development"]["Logic Description"] = "Infrastructure development, particularly road construction, leads to habitat loss and fragmentation, and increases access to previously remote areas, facilitating deforestation and overexploitation of resources."
congo["Infrastructure Development"]["Impact Function"] = "impact_infrastructure_development_congo_rainforest"

# --- Southeast Asian Rainforest ---
se_asian_rainforest = all_stressors_data["Southeast Asian Rainforest"]

se_asian_rainforest["Infrastructure Development"]["Metric"] = "Road length (km/year); area affected by other projects (ha/year)."
se_asian_rainforest["Infrastructure Development"]["Data Sources"] = [
    "Government and industry reports.",
    "Remote sensing data.",
    "NGO reports."
]
se_asian_rainforest["Infrastructure Development"]["Impact on Area"] = "Direct Loss and fragmentation"
se_asian_rainforest["Infrastructure Development"]["Impact on Biodiversity"] = "Habitat Loss; Increased Access; Disruption of Corridors"
se_asian_rainforest["Infrastructure Development"]["Influenced By"] = [
    "Economic Growth",
    "Population Growth",
    "Government Policies",
    "Global Commodity Prices"
]
se_asian_rainforest["Infrastructure Development"]["Influences"] = [
    "Southeast Asian Rainforest - Deforestation",
    "Southeast Asian Rainforest - Wildfires",
    "Southeast Asian Rainforest - Pollution"
]
se_asian_rainforest["Infrastructure Development"]["Logic Description"] = "Similar to other rainforests, infrastructure development drives habitat loss and facilitates other stressors."
se_asian_rainforest["Infrastructure Development"]["Impact Function"] = "impact_infrastructure_development_se_asian_rainforest"


se_asian_rainforest["Deforestation"]["Metric"] = "Area of Forest Cleared (ha/year)"
se_asian_rainforest["Deforestation"]["Data Sources"] = [
    "Remote Sensing",
    "NGO and research reports"
    ]
se_asian_rainforest["Deforestation"]["Impact on Area"] = "Direct Reduction"
se_asian_rainforest["Deforestation"]["Impact on Biodiversity"] = "Habitat Loss; Carbon Emissions"
se_asian_rainforest["Deforestation"]["Influenced By"] = [
    "Southeast Asian Rainforest - Infrastructure Development",
    "Economic Growth (Palm Oil)",
    "Global Commodity Prices",
    "Population Growth",
    "Goverment Policies"
]
se_asian_rainforest["Deforestation"]["Influences"] = [
    "Southeast Asian Rainforest - Wildfires",
    "Southeast Asian Rainforest - Peatland Degradation"
]
se_asian_rainforest["Deforestation"]["Logic Description"] = "Palm oil plantation expansion is the dominant driver, along with logging, mining, and other agricultural expansion.  Significant impact on peatlands."
se_asian_rainforest["Deforestation"]["Impact Function"] = "impact_deforestation_se_asian_rainforest"

se_asian_rainforest["Temperature Increase"]["Metric"] = "Average annual temperature increase (Celsius)"
se_asian_rainforest["Temperature Increase"]["Data Sources"] = [
    "Global and Regional climate models.",
     "Limited historical data."
]
se_asian_rainforest["Temperature Increase"]["Impact on Area"] = "Indirect"
se_asian_rainforest["Temperature Increase"]["Impact on Biodiversity"] = "Species shifts; Physiological Stress"
se_asian_rainforest["Temperature Increase"]["Influenced By"] = [
      "Global GHG Emissions",
      "Southeast Asian Rainforest - Deforestation",
      "Southeast Asian Rainforest - Peatland Degradation"
]
se_asian_rainforest["Temperature Increase"]["Influences"] = [
      "Southeast Asian Rainforest - Wildfires",
      "Southeast Asian Rainforest - Changes in Precipitation"
]
se_asian_rainforest["Temperature Increase"]["Logic Description"] = "Global warming amplified by deforestation and peatland degradation."
se_asian_rainforest["Temperature Increase"]["Impact Function"] = "impact_temperature_increase_se_asian_rainforest"

se_asian_rainforest["Changes in Precipitation"]["Metric"] = "Change in annual precipitation; dry season length/severity"
se_asian_rainforest["Changes in Precipitation"]["Data Sources"] =[
    "Climate models.",
    "Limited historical data."
]
se_asian_rainforest["Changes in Precipitation"]["Impact on Area"] = "Indirect"
se_asian_rainforest["Changes in Precipitation"]["Impact on Biodiversity"] = "Species shifts; Drought stress"
se_asian_rainforest["Changes in Precipitation"]["Influenced By"] = [
      "Global GHG Emissions",
      "Southeast Asian Rainforest - Deforestation"
]
se_asian_rainforest["Changes in Precipitation"]["Influences"] = [
    "Southeast Asian Rainforest - Wildfires",
    "Southeast Asian Rainforest - Peatland Fires"
]
se_asian_rainforest["Changes in Precipitation"]["Logic Description"] = "Changes in rainfall patterns and increased drought risk."
se_asian_rainforest["Changes in Precipitation"]["Impact Function"] = "impact_precipitation_changes_se_asian_rainforest"

se_asian_rainforest["Wildfires"]["Metric"] = "Number of fires, Area Burned"
se_asian_rainforest["Wildfires"]["Data Sources"] = [
    "Remote Sensing.",
     "Local reports."
]
se_asian_rainforest["Wildfires"]["Impact on Area"] = "Direct loss, particularly of peatland."
se_asian_rainforest["Wildfires"]["Impact on Biodiversity"] = "Mortality; Habitat loss; Severe air pollution (haze)."
se_asian_rainforest["Wildfires"]["Influenced By"] = [
        "Southeast Asian Rainforest - Deforestation",
        "Southeast Asian Rainforest - Temperature Increase",
        "Southeast Asian Rainforest - Changes in Precipitation",
        "Southeast Asian Rainforest - Peatland Drainage",
        "Human Activities (land clearing)."
]
se_asian_rainforest["Wildfires"]["Influences"] = [
        "Southeast Asian Rainforest - Deforestation",
        "Southeast Asian Rainforest - Peatland Degradation",
        "Southeast Asian Rainforest - Climate Change (through massive carbon emissions)"
]
se_asian_rainforest["Wildfires"]["Logic Description"] = "Wildfires, often intentionally set for land clearing (especially for palm oil), are a HUGE problem in Sundaland, particularly due to the presence of peatlands.  These fires release massive amounts of carbon and cause severe regional air pollution."
se_asian_rainforest["Wildfires"]["Impact Function"] = "impact_wildfires_se_asian_rainforest"

se_asian_rainforest["Peatland Degradation"]["Metric"] = "Area of drained peatland (ha/year); Depth of water table in peatlands (meters)"
se_asian_rainforest["Peatland Degradation"]["Data Sources"] = [
   "Remote sensing (measuring subsidence, vegetation changes).",
    "Field measurements of water table depth.",
    "Reports from organizations specializing in peatland conservation."
]
se_asian_rainforest["Peatland Degradation"]["Impact on Area"] = "Loss of peatland ecosystem (which is a distinct subset of the rainforest area)."
se_asian_rainforest["Peatland Degradation"]["Impact on Biodiversity"] = "Loss of specialized peat swamp forest species. Massive carbon emissions (peat is a huge carbon store). Increased fire risk. Subsidence (land sinking), leading to flooding and infrastructure damage."
se_asian_rainforest["Peatland Degradation"]["Influenced By"] = [
        "Southeast Asian Rainforest - Infrastructure Development (drainage canals).",
    "Southeast Asian Rainforest - Deforestation (clearing of peat swamp forests).",
    "Southeast Asian Rainforest - Agricultural Expansion (primarily palm oil and pulpwood plantations).",
    "Southeast Asian Rainforest - Climate Change"
]
se_asian_rainforest["Peatland Degradation"]["Influences"] = [
        "Southeast Asian Rainforest - Wildfires",
        "Southeast Asian Rainforest - Climate Change",
    "Flooding (due to subsidence)" # Not defined
]
se_asian_rainforest["Peatland Degradation"]["Logic Description"] = "Peatlands are waterlogged ecosystems with thick layers of partially decayed organic matter.  Drainage for agriculture/plantations and logging causes peat decomposition, releasing CO2. Drained peat is also extremely vulnerable to fire. Critical stressor."
se_asian_rainforest["Peatland Degradation"]["Impact Function"] = "impact_peatland_degradation_se_asian_rainforest"

se_asian_rainforest["Overexploitation"]["Metric"] = "Population declines of targeted species (e.g., orangutans, tigers, rhinos); poaching incidents."
se_asian_rainforest["Overexploitation"]["Data Sources"] = [
        "Wildlife surveys.",
        "CITES trade data.",
        "Reports from conservation organizations (e.g., WWF, TRAFFIC)."
]
se_asian_rainforest["Overexploitation"]["Impact on Area"] = "Indirect, through impacts on species populations and ecological interactions."
se_asian_rainforest["Overexploitation"]["Impact on Biodiversity"] = "Population declines and local extinctions of charismatic and ecologically important species; loss of genetic diversity."
se_asian_rainforest["Overexploitation"]["Influenced By"] = [
        "Hunting and Poaching (for traditional medicine, pet trade, and bushmeat).",
        "Southeast Asian Rainforest - Infrastructure Development (roads providing access)",
       "Southeast Asian Rainforest - Deforestation (reducing habitat and making animals more vulnerable)"
        "Weak Law Enforcement."
]
se_asian_rainforest["Overexploitation"]["Influences"] = [
    "Southeast Asian Rainforest - Forest Structure (loss of seed dispersers, etc.)",
    "Trophic Cascades" #Not defined
]
se_asian_rainforest["Overexploitation"]["Logic Description"] = "Overexploitation of wildlife through hunting and poaching, often facilitated by infrastructure and deforestation, directly threatens many species with extinction."
se_asian_rainforest["Overexploitation"]["Impact Function"] = "impact_overexploitation_se_asian_rainforest"

se_asian_rainforest["Mining"]["Metric"] = "Area affected by mining operations (ha); concentrations of pollutants in water and soil."
se_asian_rainforest["Mining"]["Data Sources"] = [
        "Government mining records.",
       "Remote sensing data.",
       "Water and soil quality monitoring data.",
        "Research studies on the impacts of mining."
]
se_asian_rainforest["Mining"]["Impact on Area"] = "Direct habitat loss; pollution of rivers and streams; soil degradation."
se_asian_rainforest["Mining"]["Impact on Biodiversity"] = "Habitat destruction; toxic effects of pollutants on wildlife; disruption of aquatic ecosystems."
se_asian_rainforest["Mining"]["Influenced By"] = [
   "Global demand for minerals (e.g., tin, bauxite, nickel, gold).",
        "Government policies (mining concessions, environmental regulations).",
        "Economic factors (mineral prices)."
]
se_asian_rainforest["Mining"]["Influences"] = [
   "Southeast Asian Rainforest - Deforestation",
    "Southeast Asian Rainforest - Water Quality",
    "Southeast Asian Rainforest - Pollution",
    "Southeast Asian Rainforest - Soil Degradation"
]
se_asian_rainforest["Mining"]["Logic Description"] = "Mining activities, both legal and illegal, cause deforestation, habitat destruction, and significant pollution, particularly impacting water quality and aquatic ecosystems."
se_asian_rainforest["Mining"]["Impact Function"] = "impact_mining_se_asian_rainforest"

se_asian_rainforest["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., heavy metals, pesticides, plastic waste) in water, soil, and biota."
se_asian_rainforest["Pollution"]["Data Sources"] = [
    "Water and soil quality monitoring data.",
   "Research studies.",
    "Reports from environmental organizations."
]
se_asian_rainforest["Pollution"]["Impact on Area"] = "Degradation of water and soil quality; contamination of ecosystems."
se_asian_rainforest["Pollution"]["Impact on Biodiversity"] = "Toxic effects on wildlife; bioaccumulation of pollutants; reduced reproductive success; increased disease susceptibility."
se_asian_rainforest["Pollution"]["Influenced By"] = [
        "Southeast Asian Rainforest - Mining Activities",
    "Southeast Asian Rainforest - Agricultural Runoff",
     "Southeast Asian Rainforest - Industrial Discharge",
    "Southeast Asian Rainforest - Urban Waste",
    "Southeast Asian Rainforest - Deforestation",
    "Southeast Asian Rainforest - Peatland Degradation"
]
se_asian_rainforest["Pollution"]["Influences"] = [
    "Southeast Asian Rainforest - Water Quality",
     "Southeast Asian Rainforest - Soil Quality",
    "Southeast Asian Rainforest - Wildlife Health",
    "Human Health"
]
se_asian_rainforest["Pollution"]["Logic Description"] = "Pollution from mining, agriculture, industrial activities, urban waste, deforestation, and peatland degradation degrades water and soil quality, impacting both wildlife and human populations."
se_asian_rainforest["Pollution"]["Impact Function"] = "impact_pollution_se_asian_rainforest"

# --- Sundaland Rainforest ---
sundaland = all_stressors_data["Sundaland Rainforest"]

sundaland["Deforestation"]["Metric"] = "Area of forest cleared per year (hectares/year)."
sundaland["Deforestation"]["Data Sources"] = [
    "Global Forest Watch",
    "University of Maryland GLAD deforestation alerts",
    "Reports from NGOs (e.g., Greenpeace, WWF)",
    "Government data (where available and reliable)"
]
sundaland["Deforestation"]["Impact on Area"] = "Direct reduction of rainforest area, including significant loss of peat swamp forests."
sundaland["Deforestation"]["Impact on Biodiversity"] = "Habitat loss and fragmentation, threatening iconic species like orangutans, tigers, and rhinos. Loss of carbon storage (especially from peatlands). Disruption of ecosystem services."
sundaland["Deforestation"]["Influenced By"] = [
    "Agricultural Expansion (especially palm oil and rubber plantations)",
    "Logging (legal and illegal)",
    "Mining",
    "Infrastructure Development",
    "Population Growth",
    "Weak Governance and Law Enforcement"
]
sundaland["Deforestation"]["Influences"] = [
    "Sundaland Rainforest - Wildfires",
    "Sundaland Rainforest - Peatland Degradation",
    "Sundaland Rainforest - Changes in Precipitation"
]
sundaland["Deforestation"]["Logic Description"] = "Deforestation in Sundaland, driven largely by palm oil expansion and logging, is among the highest in the world. It has a devastating impact on biodiversity, contributes significantly to climate change (especially through peatland destruction), and increases the risk of wildfires."
sundaland["Deforestation"]["Impact Function"] = "impact_deforestation_sundaland_rainforest"

sundaland["Temperature Increase"]["Metric"] = "Average annual temperature increase (°C) above a pre-industrial baseline."
sundaland["Temperature Increase"]["Data Sources"] = [
    "Global Climate Models (GCMs)",
    "Regional Climate Models",
    "IPCC Reports"
]
sundaland["Temperature Increase"]["Impact on Area"] = "Indirect; exacerbates other stressors, particularly wildfires and peatland degradation."
sundaland["Temperature Increase"]["Impact on Biodiversity"] = "Shifts in species distributions, increased thermal stress on species, increased risk of coral bleaching in adjacent marine ecosystems."
sundaland["Temperature Increase"]["Influenced By"] = [
    "Global Greenhouse Gas Emissions",
    "Sundaland Rainforest - Deforestation",
    "Sundaland Rainforest - Peatland Degradation"
]
sundaland["Temperature Increase"]["Influences"] = [
    "Sundaland Rainforest - Wildfires",
    "Sundaland Rainforest - Changes in Precipitation",
    "Coral Bleaching in adjacent coral reefs"
]
sundaland["Temperature Increase"]["Logic Description"] = "Global warming, combined with deforestation and peatland degradation, creates a positive feedback loop, increasing temperatures and exacerbating other stressors in Sundaland."
sundaland["Temperature Increase"]["Impact Function"] = "impact_temperature_increase_sundaland_rainforest"
sundaland["Changes in Precipitation"]["Metric"] = "Change in annual precipitation (mm/year) and changes in the dry season length and intensity."
sundaland["Changes in Precipitation"]["Data Sources"] = [
     "Global Climate Models (GCMs)",
    "Regional Climate Models",
    "IPCC Reports",
    "Local meteorological data (where available)"
]
sundaland["Changes in Precipitation"]["Impact on Area"] = "Indirect, but can contribute to increased fire risk and peatland degradation."
sundaland["Changes in Precipitation"]["Impact on Biodiversity"] = "Altered water availability, affecting plant and animal life; increased drought stress; potential impacts on river systems."
sundaland["Changes in Precipitation"]["Influenced By"] = [
  "Global Greenhouse Gas Emissions",
    "Sundaland Rainforest - Deforestation",
    "Sundaland Rainforest - Peatland Degradation",
    "El Niño-Southern Oscillation (ENSO)"
]
sundaland["Changes in Precipitation"]["Influences"] = [
    "Sundaland Rainforest - Wildfires",
    "Sundaland Rainforest - Peatland Degradation",
    "Sundaland Rainforest - Hydrological Changes"
]
sundaland["Changes in Precipitation"]["Logic Description"] = "Changes in precipitation patterns, influenced by global climate change and regional deforestation/peatland degradation, increase the risk of drought, wildfires, and impact water resources in Sundaland."
sundaland["Changes in Precipitation"]["Impact Function"] = "impact_precipitation_changes_sundaland_rainforest"

sundaland["Wildfires"]["Metric"] = "Number of wildfires per year and total area burned (hectares/year); frequency and intensity of haze events."
sundaland["Wildfires"]["Data Sources"] = [
    "Satellite-based fire detection (e.g., MODIS, VIIRS)",
   "ASEAN Specialized Meteorological Centre (ASMC) haze reports",
   "Ground-based reports (often limited)"
]
sundaland["Wildfires"]["Impact on Area"] = "Extensive loss of forest cover, particularly peat swamp forests; severe air pollution (haze)."
sundaland["Wildfires"]["Impact on Biodiversity"] = "High mortality of plants and animals; habitat destruction; respiratory problems in wildlife and humans; long-term impacts on forest regeneration."
sundaland["Wildfires"]["Influenced By"] = [
   "Sundaland Rainforest - Deforestation",
    "Sundaland Rainforest - Peatland Degradation",
    "Sundaland Rainforest - Changes in Precipitation",
    "Land Clearing Practices (burning)",
   "El Niño events"
]
sundaland["Wildfires"]["Influences"] = [
    "Sundaland Rainforest - Air Quality (regional and global)",
    "Sundaland Rainforest - Carbon Emissions (massive)",
   "Sundaland Rainforest - Deforestation",
    "Human Health (respiratory problems)"
]
sundaland["Wildfires"]["Logic Description"] = "Wildfires, largely human-caused and exacerbated by peatland drainage and deforestation, are a catastrophic recurring problem in Sundaland, releasing vast amounts of carbon, causing severe air pollution (the Southeast Asian haze), and devastating biodiversity."
sundaland["Wildfires"]["Impact Function"] = "impact_wildfires_sundaland_rainforest"

sundaland["Overexploitation"]["Metric"] = "Population declines of targeted species (e.g., orangutans, tigers, rhinos, pangolins); illegal wildlife trade volume."
sundaland["Overexploitation"]["Data Sources"] = [
     "Wildlife surveys (often difficult and expensive)",
    "CITES trade data",
   "Reports from conservation organizations (e.g., TRAFFIC, WWF)",
    "Seizure data from law enforcement"
]
sundaland["Overexploitation"]["Impact on Area"] = "Indirect; primarily through impacts on species populations and ecological interactions."
sundaland["Overexploitation"]["Impact on Biodiversity"] = "Population declines and local extinctions of key species; disruption of ecological processes (e.g., seed dispersal); increased risk of extinction for critically endangered species."
sundaland["Overexploitation"]["Influenced By"] = [
   "Hunting and Poaching (for traditional medicine, pet trade, bushmeat, and trophies)",
   "Sundaland Rainforest - Deforestation (making animals more accessible)",
   "Sundaland Rainforest - Infrastructure Development (roads providing access)",
     "Weak Law Enforcement and Corruption"
]
sundaland["Overexploitation"]["Influences"] = [
  "Sundaland Rainforest - Forest Structure",
   "Sundaland Rainforest - Seed Dispersal",
    "Sundaland Rainforest - Trophic Cascades"
]
sundaland["Overexploitation"]["Logic Description"] = "Overexploitation, driven by the illegal wildlife trade and hunting, is a major threat to Sundaland's biodiversity, pushing many iconic species towards extinction."
sundaland["Overexploitation"]["Impact Function"] = "impact_overexploitation_sundaland_rainforest"

sundaland["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., mercury, pesticides, industrial effluent, plastic waste) in water, soil, and biota."
sundaland["Pollution"]["Data Sources"] = [
   "Water quality monitoring data",
    "Soil contamination studies",
   "Research on pollutant levels in wildlife",
   "Reports from environmental agencies"
]
sundaland["Pollution"]["Impact on Area"] = "Degradation of water and soil quality; contamination of ecosystems, including waterways and coastal areas."
sundaland["Pollution"]["Impact on Biodiversity"] = "Toxic effects on aquatic and terrestrial life; bioaccumulation of pollutants in the food chain; reduced reproductive success; increased disease susceptibility."
sundaland["Pollution"]["Influenced By"] = [
  "Sundaland Rainforest - Mining Activities",
  "Sundaland Rainforest - Agricultural Runoff (pesticides, fertilizers)",
  "Sundaland Rainforest - Industrial Discharge",
 "Sundaland Rainforest - Urban Waste and Sewage",
   "Sundaland Rainforest - Deforestation (leading to increased erosion and sediment pollution)"
]
sundaland["Pollution"]["Influences"] = [
     "Sundaland Rainforest - Water Quality",
    "Sundaland Rainforest - Soil Quality",
     "Sundaland Rainforest - Wildlife Health",
    "Human Health (through contaminated food and water)"
]
sundaland["Pollution"]["Logic Description"] = "Pollution from various sources, including mining, agriculture, industry, and inadequate waste management, contaminates Sundaland's ecosystems, posing risks to biodiversity and human health."
sundaland["Pollution"]["Impact Function"] = "impact_pollution_sundaland_rainforest"

sundaland["Infrastructure Development"]["Metric"] = "Length of new roads constructed (km/year); area affected by new infrastructure projects (e.g., dams, ports) (ha/year)."
sundaland["Infrastructure Development"]["Data Sources"] = [
  "Government infrastructure plans and reports",
    "Reports from development banks and agencies",
  "Remote sensing data"
]
sundaland["Infrastructure Development"]["Impact on Area"] = "Direct habitat loss due to construction; fragmentation of forests and other ecosystems."
sundaland["Infrastructure Development"]["Impact on Biodiversity"] = "Habitat loss and fragmentation; increased access for poaching and illegal logging; disruption of wildlife movement and migration; barrier effects."
sundaland["Infrastructure Development"]["Influenced By"] = [
    "Economic Growth and Development Plans",
   "Population Growth",
    "Investment in Resource Extraction (mining, logging, plantations)",
    "Regional Connectivity Initiatives"
]
sundaland["Infrastructure Development"]["Influences"] = [
 "Sundaland Rainforest - Deforestation",
  "Sundaland Rainforest - Overexploitation",
   "Sundaland Rainforest - Habitat Fragmentation",
   "Sundaland Rainforest - Pollution"
]
sundaland["Infrastructure Development"]["Logic Description"] = "Infrastructure development, particularly road construction, facilitates access to previously remote areas, accelerating deforestation, overexploitation, and other threats to biodiversity in Sundaland."
sundaland["Infrastructure Development"]["Impact Function"] = "impact_infrastructure_development_sundaland_rainforest"

sundaland["Peatland Degradation"]["Metric"] = "Area of drained peatland (ha/year); depth of water table in peatlands (meters); subsidence rates (cm/year)."
sundaland["Peatland Degradation"]["Data Sources"] = [
   "Remote sensing (measuring subsidence, vegetation changes, and fire occurrence).",
    "Field measurements of water table depth and peat thickness.",
   "Reports from organizations specializing in peatland conservation (e.g., Wetlands International).",
  "Government data (where available)"
]
sundaland["Peatland Degradation"]["Impact on Area"] = "Loss of peat swamp forest ecosystem (a unique and highly biodiverse habitat); increased flood risk due to land subsidence."
sundaland["Peatland Degradation"]["Impact on Biodiversity"] = "Loss of specialized peat swamp forest species (plants, animals, microorganisms); massive carbon emissions (contributing to climate change); increased fire risk; habitat loss and fragmentation."
sundaland["Peatland Degradation"]["Influenced By"] = [
       "Sundaland Rainforest - Drainage for Agriculture (especially palm oil and pulpwood plantations).",
    "Sundaland Rainforest - Logging (often involving canal construction for timber extraction).",
   "Sundaland Rainforest - Infrastructure Development",
    "Sundaland Rainforest - Climate Change (drier conditions exacerbate peat degradation)"
]
sundaland["Peatland Degradation"]["Influences"] = [
    "Sundaland Rainforest - Wildfires (drained peat is extremely flammable)",
   "Sundaland Rainforest - Carbon Emissions (massive release of stored carbon)",
    "Sundaland Rainforest - Flooding (due to land subsidence)",
    "Sundaland Rainforest - Deforestation",
    "Sundaland Rainforest - Climate Change"
]
sundaland["Peatland Degradation"]["Logic Description"] = "Peatland degradation in Sundaland is a major environmental crisis. Drainage for agriculture and logging makes the peat highly susceptible to fire, releasing enormous amounts of carbon dioxide and causing widespread haze. It also leads to land subsidence and biodiversity loss."
sundaland["Peatland Degradation"]["Impact Function"] = "impact_peatland_degradation_sundaland_rainforest"

# --- New Guinea Rainforest ---
new_guinea = all_stressors_data["New Guinea Rainforest"]

new_guinea["Deforestation"]["Metric"] = "Area of forest cleared per year (hectares/year)."
new_guinea["Deforestation"]["Data Sources"] = [
    "Global Forest Watch",
    "University of Maryland GLAD deforestation alerts",
    "Reports from NGOs (e.g., Greenpeace)",
     "Government data (if available/reliable)"
]
new_guinea["Deforestation"]["Impact on Area"] = "Direct reduction of rainforest area."
new_guinea["Deforestation"]["Impact on Biodiversity"] = "Habitat loss and fragmentation, threatening endemic species. Loss of carbon storage. Disruption of ecosystem services."
new_guinea["Deforestation"]["Influenced By"] = [
   "Logging (legal and illegal)",
   "Agricultural Expansion (palm oil, subsistence farming)",
    "Mining",
   "Infrastructure Development",
   "Population Growth"
]
new_guinea["Deforestation"]["Influences"] = [
    "New Guinea Rainforest - Wildfires",
   "New Guinea Rainforest - Changes in Precipitation"
]
new_guinea["Deforestation"]["Logic Description"] = "Deforestation in New Guinea is driven by logging, agricultural expansion (including palm oil), mining, and infrastructure development. While currently lower than in some other regions, it's a growing threat."
new_guinea["Deforestation"]["Impact Function"] = "impact_deforestation_new_guinea_rainforest"

new_guinea["Temperature Increase"]["Metric"] = "Average annual temperature increase (°C) above a pre-industrial baseline."
new_guinea["Temperature Increase"]["Data Sources"] = [
    "Global Climate Models (GCMs)",
     "Regional Climate Models",
     "IPCC Reports"
]
new_guinea["Temperature Increase"]["Impact on Area"] = "Indirect; exacerbates other stressors."
new_guinea["Temperature Increase"]["Impact on Biodiversity"] = "Shifts in species distributions; increased thermal stress, particularly at higher elevations; potential impacts on cloud forests."
new_guinea["Temperature Increase"]["Influenced By"] = [
     "Global Greenhouse Gas Emissions",
    "New Guinea Rainforest - Deforestation"
]
new_guinea["Temperature Increase"]["Influences"] = [
    "New Guinea Rainforest - Wildfires",
   "New Guinea Rainforest - Changes in Precipitation",
  "New Guinea Rainforest - Cloud Forest Impacts"
]
new_guinea["Temperature Increase"]["Logic Description"] = "Global warming poses a significant threat to New Guinea's biodiversity, particularly in high-altitude ecosystems and cloud forests, which are highly sensitive to temperature changes."
new_guinea["Temperature Increase"]["Impact Function"] = "impact_temperature_increase_new_guinea_rainforest"

new_guinea["Changes in Precipitation"]["Metric"] = "Change in annual precipitation (mm/year) and changes in the dry season length and intensity."
new_guinea["Changes in Precipitation"]["Data Sources"] = [
   "Global Climate Models (GCMs)",
    "Regional Climate Models",
    "IPCC Reports",
   "Local meteorological data (limited)"
]
new_guinea["Changes in Precipitation"]["Impact on Area"] = "Indirect; can influence vegetation types and fire risk."
new_guinea["Changes in Precipitation"]["Impact on Biodiversity"] = "Changes in water availability, affecting plant and animal life; altered river flow regimes; potential impacts on cloud forests."
new_guinea["Changes in Precipitation"]["Influenced By"] = [
    "Global Greenhouse Gas Emissions",
    "New Guinea Rainforest - Deforestation",
     "El Niño-Southern Oscillation (ENSO)"
]
new_guinea["Changes in Precipitation"]["Influences"] = [
     "New Guinea Rainforest - Wildfires",
  "New Guinea Rainforest - Hydrological Changes",
     "New Guinea Rainforest - Cloud Forest Impacts"
]
new_guinea["Changes in Precipitation"]["Logic Description"] = "Changes in precipitation, including shifts in rainfall patterns and potential increases in drought frequency/intensity, pose risks to New Guinea's ecosystems, particularly its unique cloud forests."
new_guinea["Changes in Precipitation"]["Impact Function"] = "impact_precipitation_changes_new_guinea_rainforest"

new_guinea["Wildfires"]["Metric"] = "Number of wildfires per year and total area burned (hectares/year)."
new_guinea["Wildfires"]["Data Sources"] = [
    "Satellite-based fire detection (e.g., MODIS, VIIRS)",
    "Reports from local communities and authorities (often limited)"
]
new_guinea["Wildfires"]["Impact on Area"] = "Direct loss of forest cover; changes in vegetation structure."
new_guinea["Wildfires"]["Impact on Biodiversity"] = "Mortality of plants and animals; habitat loss; increased vulnerability to future fires."
new_guinea["Wildfires"]["Influenced By"] = [
    "New Guinea Rainforest - Deforestation",
    "New Guinea Rainforest - Changes in Precipitation",
    "Land Clearing Practices (burning)",
    "El Niño events"
]
new_guinea["Wildfires"]["Influences"] = [
  "New Guinea Rainforest - Air Quality",
    "New Guinea Rainforest - Carbon Emissions",
  "New Guinea Rainforest - Deforestation"
]
new_guinea["Wildfires"]["Logic Description"] = "While not as prevalent as in some other rainforests, wildfires are a growing concern in New Guinea, particularly during El Niño-related droughts and in areas affected by deforestation and land clearing."
new_guinea["Wildfires"]["Impact Function"] = "impact_wildfires_new_guinea_rainforest"

new_guinea["Overexploitation"]["Metric"] = "Population declines of targeted species (e.g., birds of paradise, tree kangaroos, certain reptiles); illegal wildlife trade volume."
new_guinea["Overexploitation"]["Data Sources"] = [
   "Wildlife surveys (challenging in the region)",
  "CITES trade data",
    "Reports from conservation organizations",
    "Seizure data from law enforcement"
]
new_guinea["Overexploitation"]["Impact on Area"] = "Indirect; primarily through impacts on species populations and ecological interactions."
new_guinea["Overexploitation"]["Impact on Biodiversity"] = "Population declines of key species; disruption of ecological processes (e.g., seed dispersal); potential for local extinctions; loss of unique endemic species."
new_guinea["Overexploitation"]["Influenced By"] = [
   "Hunting (for food, traditional uses, and the pet trade)",
   "New Guinea Rainforest - Infrastructure Development (roads providing access)",
    "Weak Law Enforcement"
]
new_guinea["Overexploitation"]["Influences"] = [
   "New Guinea Rainforest - Forest Structure and Composition",
    "New Guinea Rainforest - Seed Dispersal"
]
new_guinea["Overexploitation"]["Logic Description"] = "Overexploitation, driven by hunting and the illegal wildlife trade, threatens New Guinea's unique and highly endemic biodiversity."
new_guinea["Overexploitation"]["Impact Function"] = "impact_overexploitation_new_guinea_rainforest"

new_guinea["Mining"]["Metric"] = "Area affected by mining operations (ha); concentrations of pollutants (e.g., heavy metals) in water and soil."
new_guinea["Mining"]["Data Sources"] = [
    "Government mining records",
   "Reports from NGOs and research institutions",
  "Remote sensing data",
    "Water and soil quality monitoring data"
]
new_guinea["Mining"]["Impact on Area"] = "Direct habitat loss; pollution of rivers and streams (e.g., sediment, heavy metals); soil degradation."
new_guinea["Mining"]["Impact on Biodiversity"] = "Habitat destruction; toxic effects of pollutants on aquatic and terrestrial life; disruption of hydrological regimes."
new_guinea["Mining"]["Influenced By"] = [
    "Global demand for minerals (e.g., copper, gold, nickel)",
   "Government policies and mining concessions",
  "Weak environmental regulations"
]
new_guinea["Mining"]["Influences"] = [
  "New Guinea Rainforest - Deforestation",
   "New Guinea Rainforest - Water Quality",
   "New Guinea Rainforest - Pollution",
    "New Guinea Rainforest - Soil Degradation",
   "New Guinea Rainforest - Hydrological Changes"
]
new_guinea["Mining"]["Logic Description"] = "Mining activities, often large-scale and with significant environmental impacts, pose a major threat to New Guinea's ecosystems, causing deforestation, pollution, and habitat destruction."
new_guinea["Mining"]["Impact Function"] = "impact_mining_new_guinea_rainforest"

new_guinea["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., heavy metals, pesticides, plastic waste) in water, soil, and biota."
new_guinea["Pollution"]["Data Sources"] = [
   "Water quality monitoring data",
   "Soil contamination studies",
    "Research on pollutant levels in wildlife",
    "Reports from environmental agencies"
]
new_guinea["Pollution"]["Impact on Area"] = "Degradation of water and soil quality; contamination of ecosystems."
new_guinea["Pollution"]["Impact on Biodiversity"] = "Toxic effects on aquatic and terrestrial life; bioaccumulation of pollutants; reduced reproductive success; increased disease susceptibility."
new_guinea["Pollution"]["Influenced By"] = [
 "New Guinea Rainforest - Mining Activities",
 "New Guinea Rainforest - Agricultural Runoff",
 "New Guinea Rainforest - Industrial Discharge",
  "New Guinea Rainforest - Urban Waste",
  "New Guinea Rainforest - Deforestation"
]
new_guinea["Pollution"]["Influences"] = [
     "New Guinea Rainforest - Water Quality",
    "New Guinea Rainforest - Soil Quality",
  "New Guinea Rainforest - Wildlife Health",
  "Human Health"
]
new_guinea["Pollution"]["Logic Description"] = "Pollution from mining, agriculture, and other sources contaminates New Guinea's environment, impacting both biodiversity and human well-being."
new_guinea["Pollution"]["Impact Function"] = "impact_pollution_new_guinea_rainforest"

new_guinea["Infrastructure Development"]["Metric"] = "Length of new roads constructed (km/year); area affected by new infrastructure projects (ha/year)."
new_guinea["Infrastructure Development"]["Data Sources"] = [
     "Government infrastructure plans and reports",
   "Reports from development agencies",
     "Remote sensing data"
]
new_guinea["Infrastructure Development"]["Impact on Area"] = "Direct habitat loss; fragmentation of forests."
new_guinea["Infrastructure Development"]["Impact on Biodiversity"] = "Habitat loss and fragmentation; increased access for hunting, poaching, and illegal logging; disruption of wildlife movement."
new_guinea["Infrastructure Development"]["Influenced By"] = [
    "Economic Development Plans",
   "Population Growth",
  "Investment in Resource Extraction (mining, logging)"
]
new_guinea["Infrastructure Development"]["Influences"] = [
  "New Guinea Rainforest - Deforestation",
   "New Guinea Rainforest - Overexploitation",
  "New Guinea Rainforest - Habitat Fragmentation"
]
new_guinea["Infrastructure Development"]["Logic Description"] = "Infrastructure development, particularly road construction, facilitates access to previously remote rainforest areas, increasing the risk of deforestation, overexploitation, and other threats."

# --- Atlantic Forest ---
atlantic_forest = all_stressors_data["Atlantic Forest"]

atlantic_forest["Infrastructure Development"]["Metric"] = "Road length (km/year); area affected by other projects (ha/year)."
atlantic_forest["Infrastructure Development"]["Data Sources"] = [
    "Government and industry reports.",
    "Remote sensing data.",
    "NGO reports."
]
atlantic_forest["Infrastructure Development"]["Impact on Area"] = "Direct loss and fragmentation (already highly fragmented)."
atlantic_forest["Infrastructure Development"]["Impact on Biodiversity"] = "Habitat loss and fragmentation; Increased access for hunting/poaching; Edge effects"
atlantic_forest["Infrastructure Development"]["Influenced By"] = [
    "Economic Growth",
    "Population Growth (high population density in the region)",
    "Government Policies"
]
atlantic_forest["Infrastructure Development"]["Influences"] = [
   "Atlantic Forest - Deforestation",
   "Atlantic Forest - Wildfires"
]
atlantic_forest["Infrastructure Development"]["Logic Description"] = "Further fragmentation of an already highly fragmented ecosystem, increasing edge effects and isolating populations."
atlantic_forest["Infrastructure Development"]["Impact Function"] = "impact_infrastructure_development_atlantic_forest"


atlantic_forest["Deforestation"]["Metric"] = "Area of forest cleared per year (ha/year)."
atlantic_forest["Deforestation"]["Data Sources"] = [
    "Remote sensing data.",
  "NGO and research reports (e.g., SOS Mata Atlântica)."
]
atlantic_forest["Deforestation"]["Impact on Area"] = "Direct reduction (already severely reduced)."
atlantic_forest["Deforestation"]["Impact on Biodiversity"] = "Habitat loss.; Increased extinction risk."
atlantic_forest["Deforestation"]["Influenced By"] = [
    "Atlantic Forest - Infrastructure Development",
   "Economic Growth: Agriculture (sugarcane, coffee, cattle).",
   "Atlantic Forest - Urban Expansion",
   "Government Policies"
]
atlantic_forest["Deforestation"]["Influences"] = [
    "Atlantic Forest - Wildfires"
]
atlantic_forest["Deforestation"]["Logic Description"] = "Continued deforestation, driven by agriculture and urban expansion, further reduces the remaining fragments of this highly threatened ecosystem."
atlantic_forest["Deforestation"]["Impact Function"] = "impact_deforestation_atlantic_forest"

atlantic_forest["Temperature Increase"]["Metric"] = "Average annual temperature increase (°C)."
atlantic_forest["Temperature Increase"]["Data Sources"] = [
   "Global and regional climate models.",
   "Historical data."
]
atlantic_forest["Temperature Increase"]["Impact on Area"] = "Indirect."
atlantic_forest["Temperature Increase"]["Impact on Biodiversity"] = "Species shifts; Physiological stress."
atlantic_forest["Temperature Increase"]["Influenced By"] = [
    "Global Greenhouse Gas Emissions",
   "Atlantic Forest - Deforestation"
]
atlantic_forest["Temperature Increase"]["Influences"] = [
    "Atlantic Forest - Wildfires",
    "Atlantic Forest - Changes in Precipitation"
]
atlantic_forest["Temperature Increase"]["Logic Description"] = "Global warming impacts."
atlantic_forest["Temperature Increase"]["Impact Function"] = "impact_temperature_increase_atlantic_forest"

atlantic_forest["Changes in Precipitation"]["Metric"] = "Change in annual precipitation (mm/year); dry season changes."
atlantic_forest["Changes in Precipitation"]["Data Sources"] = [
  "Climate models.",
    "Historical data."
]
atlantic_forest["Changes in Precipitation"]["Impact on Area"] = "Indirect."
atlantic_forest["Changes in Precipitation"]["Impact on Biodiversity"] = "Species shifts; Drought stress."
atlantic_forest["Changes in Precipitation"]["Influenced By"] = [
   "Global Greenhouse Gas Emissions",
   "Atlantic Forest - Deforestation (potentially)."
]
atlantic_forest["Changes in Precipitation"]["Influences"] = [
     "Atlantic Forest - Wildfires"
]
atlantic_forest["Changes in Precipitation"]["Logic Description"] = "Changes in rainfall patterns."
atlantic_forest["Changes in Precipitation"]["Impact Function"] = "impact_precipitation_changes_atlantic_forest"

atlantic_forest["Wildfires"]["Metric"] = "Number of wildfires per year; total area burned (hectares/year)."
atlantic_forest["Wildfires"]["Data Sources"] = [
 "Remote sensing",
  "Fire department and agency reports"
]
atlantic_forest["Wildfires"]["Impact on Area"] = "Direct loss within fragmented patches."
atlantic_forest["Wildfires"]["Impact on Biodiversity"] = "Mortality; Habitat loss; Exacerbation of fragmentation."
atlantic_forest["Wildfires"]["Influenced By"] = [
    "Atlantic Forest - Deforestation",
    "Atlantic Forest - Temperature Increase",
    "Atlantic Forest - Changes in Precipitation",
    "Human Activities"
]
atlantic_forest["Wildfires"]["Influences"] = [
   "Atlantic Forest - Deforestation"
]
atlantic_forest["Wildfires"]["Logic Description"] = "Wildfires, often linked to ag practices and climate, degrade fragmented forest."
atlantic_forest["Wildfires"]["Impact Function"] = "impact_wildfires_atlantic_forest"

atlantic_forest["Overexploitation"]["Metric"] = "Population declines of targeted species (e.g., certain birds, mammals); hunting pressure."
atlantic_forest["Overexploitation"]["Data Sources"] = [
   "Wildlife surveys.",
   "Reports from conservation organizations.",
    "Research studies."
]
atlantic_forest["Overexploitation"]["Impact on Area"] = "Indirect, through impacts on species populations."
atlantic_forest["Overexploitation"]["Impact on Biodiversity"] = "Population declines of targeted species; disruption of ecological processes (e.g., seed dispersal)."
atlantic_forest["Overexploitation"]["Influenced By"] = [
     "Hunting (for food, sport, and the illegal wildlife trade).",
   "Atlantic Forest - Habitat Fragmentation (making animals more accessible)."
]
atlantic_forest["Overexploitation"]["Influences"] = [
   "Trophic Cascades"
]
atlantic_forest["Overexploitation"]["Logic Description"] = "Hunting and poaching, exacerbated by habitat fragmentation, threaten wildlife populations."
atlantic_forest["Overexploitation"]["Impact Function"] = "impact_overexploitation_atlantic_forest"


atlantic_forest["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., pesticides, industrial chemicals) in water, soil, and biota."
atlantic_forest["Pollution"]["Data Sources"] = [
  "Water and soil quality monitoring data.",
    "Research studies."
]
atlantic_forest["Pollution"]["Impact on Area"] = "Degradation of water and soil quality."
atlantic_forest["Pollution"]["Impact on Biodiversity"] = "Toxic effects on wildlife; impacts on aquatic ecosystems."
atlantic_forest["Pollution"]["Influenced By"] = [
  "Atlantic Forest - Agricultural Runoff",
   "Atlantic Forest - Industrial Discharge",
 "Atlantic Forest - Urban Runoff"
]
atlantic_forest["Pollution"]["Influences"] = [
     "Atlantic Forest - Water Quality",
   "Atlantic Forest - Wildlife Health"
]
atlantic_forest["Pollution"]["Logic Description"] = "Pollution from agriculture, industry, and urban areas degrades water and soil quality, impacting wildlife."
atlantic_forest["Pollution"]["Impact Function"] = "impact_pollution_atlantic_forest"

# --- Mesoamerican Forests ---
mesoamerican_forests = all_stressors_data["Mesoamerican Forests"]

mesoamerican_forests["Infrastructure Development"]["Metric"] = "Length of new roads (km/year); area affected by other projects (dams, etc.) (ha/year)."
mesoamerican_forests["Infrastructure Development"]["Data Sources"] = [
    "Government and industry reports.",
   "Remote sensing data.",
    "NGO reports."
]
mesoamerican_forests["Infrastructure Development"]["Impact on Area"] = "Direct loss and fragmentation."
mesoamerican_forests["Infrastructure Development"]["Impact on Biodiversity"] = "Habitat loss and fragmentation.; Increased access for hunting/poaching.; Disruption of ecological corridors."
mesoamerican_forests["Infrastructure Development"]["Influenced By"] = [
    "Economic Growth: Tourism, agriculture, resource extraction.",
   "Population Growth.",
     "Government Policies.",
    "Global Commodity Prices."
]
mesoamerican_forests["Infrastructure Development"]["Influences"] = [
    "Mesoamerican Forests - Deforestation",
    "Mesoamerican Forests - Wildfires",
    "Mesoamerican Forests - Pollution"
]
mesoamerican_forests["Infrastructure Development"]["Logic Description"] = "Infrastructure development, driven by various economic activities, leads to habitat loss and facilitates other stressors."
mesoamerican_forests["Infrastructure Development"]["Impact Function"] = "impact_infrastructure_development_mesoamerican_forests"

mesoamerican_forests["Deforestation"]["Metric"] = "Area of forest cleared per year (ha/year)."
mesoamerican_forests["Deforestation"]["Data Sources"] = [
   "Remote sensing data.",
  "NGO and research reports.",
   "Government data."
]
mesoamerican_forests["Deforestation"]["Impact on Area"] = "Direct reduction."
mesoamerican_forests["Deforestation"]["Impact on Biodiversity"] = "Habitat loss and fragmentation.; Loss of carbon storage."
mesoamerican_forests["Deforestation"]["Influenced By"] = [
     "Mesoamerican Forests - Infrastructure Development",
   "Economic Growth: Agriculture (cattle ranching, coffee, palm oil), logging.",
  "Population Growth: Subsistence agriculture.",
  "Government Policies.",
 "Global Commodity Prices"
]
mesoamerican_forests["Deforestation"]["Influences"] = [
  "Mesoamerican Forests - Wildfires",
    "Mesoamerican Forests - Changes in Precipitation"
]
mesoamerican_forests["Deforestation"]["Logic Description"] = "Deforestation, driven by agricultural expansion (including cattle ranching and, increasingly, palm oil), logging, and subsistence farming, is a major threat."
mesoamerican_forests["Deforestation"]["Impact Function"] = "impact_deforestation_mesoamerican_forests"

mesoamerican_forests["Temperature Increase"]["Metric"] = "Average annual temperature increase (°C)."
mesoamerican_forests["Temperature Increase"]["Data Sources"] = [
    "Global and regional climate models.",
   "Historical data."
]
mesoamerican_forests["Temperature Increase"]["Impact on Area"] = "Indirect."
mesoamerican_forests["Temperature Increase"]["Impact on Biodiversity"] = "Species shifts.; Physiological stress.;Increased risk of coral bleaching in coastal areas."
mesoamerican_forests["Temperature Increase"]["Influenced By"] = [
 "Global Greenhouse Gas Emissions.",
    "Mesoamerican Forests - Deforestation"
]
mesoamerican_forests["Temperature Increase"]["Influences"] = [
   "Mesoamerican Forests - Wildfires",
    "Mesoamerican Forests - Changes in Precipitation"
]
mesoamerican_forests["Temperature Increase"]["Logic Description"] = "Global warming impacts, with potential impacts on both terrestrial and coastal ecosystems (e.g., coral reefs)."
mesoamerican_forests["Temperature Increase"]["Impact Function"] = "impact_temperature_increase_mesoamerican_forests"

mesoamerican_forests["Changes in Precipitation"]["Metric"] = "Change in annual precipitation (mm/year); dry season changes."
mesoamerican_forests["Changes in Precipitation"]["Data Sources"] = [
 "Climate models.",
    "Historical data."
]
mesoamerican_forests["Changes in Precipitation"]["Impact on Area"] = "Indirect."
mesoamerican_forests["Changes in Precipitation"]["Impact on Biodiversity"] = "Species shifts.;Drought stress.;Altered hurricane patterns."
mesoamerican_forests["Changes in Precipitation"]["Influenced By"] = [
    "Global Greenhouse Gas Emissions",
   "Mesoamerican Forests - Deforestation (potentially)"
]
mesoamerican_forests["Changes in Precipitation"]["Influences"] = [
   "Mesoamerican Forests - Wildfires"
]
mesoamerican_forests["Changes in Precipitation"]["Logic Description"] = "Changes in rainfall patterns and potential changes in hurricane frequency/intensity, linked to climate change."
mesoamerican_forests["Changes in Precipitation"]["Impact Function"] = "impact_precipitation_changes_mesoamerican_forests"

mesoamerican_forests["Wildfires"]["Metric"] = "Number of fires; area burned (ha/year)."
mesoamerican_forests["Wildfires"]["Data Sources"] = [
   "Remote sensing data.",
 "Local reports."
]
mesoamerican_forests["Wildfires"]["Impact on Area"] = "Direct loss."
mesoamerican_forests["Wildfires"]["Impact on Biodiversity"] = "Mortality.;Habitat loss."
mesoamerican_forests["Wildfires"]["Influenced By"] = [
   "Mesoamerican Forests - Deforestation",
    "Mesoamerican Forests - Temperature Increase",
   "Mesoamerican Forests - Changes in Precipitation",
   "Human Activities (agricultural burning)."
]
mesoamerican_forests["Wildfires"]["Influences"] = [
    "Mesoamerican Forests - Deforestation"
]
mesoamerican_forests["Wildfires"]["Logic Description"] = "Wildfires, often linked to land clearing and exacerbated by climate change."
mesoamerican_forests["Wildfires"]["Impact Function"] = "impact_wildfires_mesoamerican_forests"

mesoamerican_forests["Overexploitation"]["Metric"] = "Hunting pressure; population declines of targeted species (e.g., jaguars, tapirs, macaws)."
mesoamerican_forests["Overexploitation"]["Data Sources"] = [
    "Wildlife surveys.",
  "Reports from conservation organizations.",
  "Research studies."
]
mesoamerican_forests["Overexploitation"]["Impact on Area"] = "Indirect, through species loss."
mesoamerican_forests["Overexploitation"]["Impact on Biodiversity"] = "Population declines of key species, impacting ecosystem function (e.g., seed dispersal)."
mesoamerican_forests["Overexploitation"]["Influenced By"] = [
   "Hunting and Poaching",
  "Mesoamerican Forests - Infrastructure Development (roads providing access)",
  "Mesoamerican Forests - Deforestation (fragmentation and access)"
]
mesoamerican_forests["Overexploitation"]["Influences"] = [
  "Trophic Cascades",
  "Seed Dispersal"
]
mesoamerican_forests["Overexploitation"]["Logic Description"] = "Hunting and poaching, often facilitated by infrastructure development and deforestation, threaten wildlife populations."
mesoamerican_forests["Overexploitation"]["Impact Function"] = "impact_overexploitation_mesoamerican_forests"

mesoamerican_forests["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., pesticides, heavy metals) in water, soil, and biota."
mesoamerican_forests["Pollution"]["Data Sources"] = [
     "Water and soil quality monitoring data.",
        "Research studies."
]
mesoamerican_forests["Pollution"]["Impact on Area"] = "Degradation of water and soil quality."
mesoamerican_forests["Pollution"]["Impact on Biodiversity"] = "Toxic effects on wildlife and plants; bioaccumulation of pollutants."
mesoamerican_forests["Pollution"]["Influenced By"] = [
   "Mesoamerican Forests - Agricultural Runoff",
  "Mesoamerican Forests - Mining Activities",
    "Mesoamerican Forests - Industrial Discharge"
]
mesoamerican_forests["Pollution"]["Influences"] = [
    "Mesoamerican Forests - Water Quality",
    "Mesoamerican Forests - Wildlife Health"
]
mesoamerican_forests["Pollution"]["Logic Description"] = "Pollution from agriculture, mining, and industry degrades water and soil quality, harming wildlife."
mesoamerican_forests["Pollution"]["Impact Function"] = "impact_pollution_mesoamerican_forests"

# --- Great Barrier Reef ---
great_barrier_reef = all_stressors_data["Great Barrier Reef"]

great_barrier_reef["Temperature Increase"]["Metric"] = "Sea surface temperature (SST) anomalies (°C above long-term average); frequency and severity of marine heatwaves."
great_barrier_reef["Temperature Increase"]["Data Sources"] = [
    "Australian Institute of Marine Science (AIMS) long-term monitoring program.",
    "Bureau of Meteorology (BoM) sea surface temperature data.",
   "NOAA Coral Reef Watch.",
    "Satellite data (e.g., MODIS, AVHRR)."
]
great_barrier_reef["Temperature Increase"]["Impact on Area"] = "Indirect - through coral bleaching and mortality, can lead to large-scale reef degradation."
great_barrier_reef["Temperature Increase"]["Impact on Biodiversity"] = "Coral bleaching and mortality. Shifts in species distributions (fish, invertebrates). Increased susceptibility to disease. Disruption of reef ecosystem function."
great_barrier_reef["Temperature Increase"]["Influenced By"] = [
    "Global Greenhouse Gas Emissions"
]
great_barrier_reef["Temperature Increase"]["Influences"] = [
   "Great Barrier Reef - Coral Bleaching",
    "Great Barrier Reef - Coral Disease",
   "Great Barrier Reef - Species Shifts"
]
great_barrier_reef["Temperature Increase"]["Logic Description"] = "Increased sea surface temperatures, primarily driven by global greenhouse gas emissions, cause coral bleaching, which can lead to widespread coral mortality and reef degradation."
great_barrier_reef["Temperature Increase"]["Impact Function"] = "impact_temperature_increase_great_barrier_reef"

great_barrier_reef["Ocean Acidification"]["Metric"] = "Change in seawater pH; aragonite saturation state (Ωarag)."
great_barrier_reef["Ocean Acidification"]["Data Sources"] = [
     "AIMS monitoring data.",
    "CSIRO research data.",
    "Global ocean acidification observing networks (e.g., GOA-ON)."
]
great_barrier_reef["Ocean Acidification"]["Impact on Area"] = "Indirect - reduces coral growth rates and skeletal density, making reefs more vulnerable to erosion."
great_barrier_reef["Ocean Acidification"]["Impact on Biodiversity"] = "Reduced calcification rates in corals and other calcifying organisms (e.g., shellfish, coralline algae). Impacts on larval development and settlement. Potential for shifts in community structure."
great_barrier_reef["Ocean Acidification"]["Influenced By"] = [
     "Global Carbon Dioxide Emissions"
]
great_barrier_reef["Ocean Acidification"]["Influences"] = [
   "Great Barrier Reef - Coral Growth Rates",
   "Great Barrier Reef - Reef Resilience"
]
great_barrier_reef["Ocean Acidification"]["Logic Description"] = "Increased atmospheric CO2 is absorbed by the ocean, leading to a decrease in pH (ocean acidification). This reduces the availability of carbonate ions, which corals need to build their skeletons."
great_barrier_reef["Ocean Acidification"]["Impact Function"] = "impact_ocean_acidification_great_barrier_reef"

great_barrier_reef["Pollution"]["Metric"] = "Concentrations of pollutants (nutrients, sediments, pesticides, heavy metals) in water and sediments."
great_barrier_reef["Pollution"]["Data Sources"] = [
   "Queensland Government water quality monitoring programs.",
    "AIMS research data.",
  "Reports from catchment management authorities."
]
great_barrier_reef["Pollution"]["Impact on Area"] = "Reduced water quality; increased turbidity; smothering of corals by sediment."
great_barrier_reef["Pollution"]["Impact on Biodiversity"] = "Nutrient enrichment leading to algal blooms (which can smother corals). Toxic effects of pollutants on marine life. Reduced coral growth and reproduction. Increased susceptibility to disease."
great_barrier_reef["Pollution"]["Influenced By"] = [
   "Agricultural Runoff (nutrients, sediments, pesticides)",
  "Urban and Industrial Discharge",
   "Coastal Development",
    "Shipping and Ports"
]
great_barrier_reef["Pollution"]["Influences"] = [
  "Great Barrier Reef - Water Quality",
    "Great Barrier Reef - Algal Blooms",
 "Great Barrier Reef - Coral Health"
]
great_barrier_reef["Pollution"]["Logic Description"] = "Pollution from land-based sources (primarily agriculture) reduces water quality, impacting coral health and promoting algal growth, which can outcompete corals."
great_barrier_reef["Pollution"]["Impact Function"] = "impact_pollution_great_barrier_reef"

great_barrier_reef["Overfishing"]["Metric"] = "Fishing effort (e.g., number of boats, fishing days); catch per unit effort (CPUE); biomass of targeted fish species."
great_barrier_reef["Overfishing"]["Data Sources"] = [
    "Queensland Department of Agriculture and Fisheries data.",
  "Fisheries surveys.",
 "Research studies."
]
great_barrier_reef["Overfishing"]["Impact on Area"] = "Indirect - through trophic cascades and impacts on ecosystem structure."
great_barrier_reef["Overfishing"]["Impact on Biodiversity"] = "Depletion of fish stocks. Removal of top predators, leading to trophic cascades (e.g., increases in herbivorous fish or crown-of-thorns starfish). Changes in fish community structure."
great_barrier_reef["Overfishing"]["Influenced By"] = [
  "Commercial Fishing",
    "Recreational Fishing",
   "Illegal Fishing"
]
great_barrier_reef["Overfishing"]["Influences"] = [
  "Great Barrier Reef - Trophic Cascades",
  "Great Barrier Reef - Crown-of-Thorns Starfish Outbreaks (potentially)",
   "Great Barrier Reef - Fish Populations"
]
great_barrier_reef["Overfishing"]["Logic Description"] = "Overfishing, particularly of predatory fish, can disrupt the balance of the reef ecosystem and potentially contribute to outbreaks of coral-eating crown-of-thorns starfish."
great_barrier_reef["Overfishing"]["Impact Function"] = "impact_overfishing_great_barrier_reef"

great_barrier_reef["Coastal Development"]["Metric"] = "Area of coastal habitat modified or lost (ha); number and size of coastal developments (e.g., ports, marinas, resorts)."
great_barrier_reef["Coastal Development"]["Data Sources"] = [
    "Government planning and development approvals.",
  "Remote sensing data.",
  "Environmental impact assessments."
]
great_barrier_reef["Coastal Development"]["Impact on Area"] = "Direct loss of coastal habitats (e.g., mangroves, seagrass beds) that provide nursery grounds for reef species. Increased sediment and pollution runoff."
great_barrier_reef["Coastal Development"]["Impact on Biodiversity"] = "Loss of critical habitats for reef-associated species. Increased turbidity and pollution, impacting water quality and coral health. Altered coastal hydrology."
great_barrier_reef["Coastal Development"]["Influenced By"] = [
  "Population Growth",
  "Tourism Development",
  "Industrial Development (e.g., ports)"
]
great_barrier_reef["Coastal Development"]["Influences"] = [
  "Great Barrier Reef - Water Quality",
    "Great Barrier Reef - Habitat Loss",
    "Great Barrier Reef - Pollution"
]
great_barrier_reef["Coastal Development"]["Logic Description"] = "Coastal development leads to habitat loss, increased pollution, and altered sediment dynamics, negatively impacting the health of the Great Barrier Reef."
great_barrier_reef["Coastal Development"]["Impact Function"] = "impact_coastal_development_great_barrier_reef"

great_barrier_reef["Crown-of-Thorns Starfish Outbreaks"]["Metric"] = "Density of crown-of-thorns starfish (number per hectare); area of coral consumed by starfish."
great_barrier_reef["Crown-of-Thorns Starfish Outbreaks"]["Data Sources"] = [
  "AIMS long-term monitoring program (reef surveys).",
   "CSIRO research."
]
great_barrier_reef["Crown-of-Thorns Starfish Outbreaks"]["Impact on Area"] = "Direct and significant loss of coral cover."
great_barrier_reef["Crown-of-Thorns Starfish Outbreaks"]["Impact on Biodiversity"] = "Extensive coral mortality, leading to reef degradation and loss of habitat for other reef species. Shifts in reef community structure."
great_barrier_reef["Crown-of-Thorns Starfish Outbreaks"]["Influenced By"] = [
 "Great Barrier Reef - Water Quality (nutrient enrichment may enhance larval survival).",
    "Great Barrier Reef - Overfishing (removal of starfish predators).",
    "Natural Population Cycles"
]
great_barrier_reef["Crown-of-Thorns Starfish Outbreaks"]["Influences"] = [
  "Great Barrier Reef - Coral Cover",
  "Great Barrier Reef - Reef Structure",
    "Great Barrier Reef - Biodiversity"
]
great_barrier_reef["Crown-of-Thorns Starfish Outbreaks"]["Logic Description"] = "Outbreaks of crown-of-thorns starfish, a voracious coral predator, are a major cause of coral loss on the Great Barrier Reef. The causes of outbreaks are complex and likely involve a combination of factors, including nutrient pollution and overfishing of starfish predators."
great_barrier_reef["Crown-of-Thorns Starfish Outbreaks"]["Impact Function"] = "impact_crown_of_thorns_starfish_outbreaks_great_barrier_reef"

# --- Mesoamerican Reef ---
mesoamerican_reef = all_stressors_data["Mesoamerican Reef"]

mesoamerican_reef["Temperature Increase"]["Metric"] = "Sea surface temperature (SST) anomalies (°C above long-term average); frequency and severity of marine heatwaves; Degree Heating Weeks (DHW)."
mesoamerican_reef["Temperature Increase"]["Data Sources"] = [
    "NOAA Coral Reef Watch.",
     "Satellite data.",
     "In-situ temperature loggers.",
    "Climate models."
]
mesoamerican_reef["Temperature Increase"]["Impact on Area"] = "Indirect - through coral bleaching and mortality, can lead to large-scale reef degradation."
mesoamerican_reef["Temperature Increase"]["Impact on Biodiversity"] = "Coral bleaching and mortality. Shifts in species distributions (fish, invertebrates). Increased susceptibility to disease. Disruption of reef ecosystem function."
mesoamerican_reef["Temperature Increase"]["Influenced By"] = [
        "Global Greenhouse Gas Emissions"
]
mesoamerican_reef["Temperature Increase"]["Influences"] = [
     "Mesoamerican Reef - Coral Bleaching",
     "Mesoamerican Reef - Coral Disease",
        "Mesoamerican Reef - Species Shifts"
]
mesoamerican_reef["Temperature Increase"]["Logic Description"] = "Increased sea surface temperatures, primarily driven by global greenhouse gas emissions, cause coral bleaching, which can lead to widespread coral mortality and reef degradation."
mesoamerican_reef["Temperature Increase"]["Impact Function"] = "impact_temperature_increase_mesoamerican_reef"

mesoamerican_reef["Ocean Acidification"]["Metric"] = "Ocean pH; aragonite saturation state (Ωarag)."
mesoamerican_reef["Ocean Acidification"]["Data Sources"] = [
   "Oceanographic surveys.",
    "Chemical analysis of seawater samples.",
    "Models that simulate ocean chemistry."
]
mesoamerican_reef["Ocean Acidification"]["Impact on Area"] = "Reduced calcification rates of corals and other calcifying organisms."
mesoamerican_reef["Ocean Acidification"]["Impact on Biodiversity"] = "Slower coral growth.; Weaker coral skeletons, making them more vulnerable to erosion and breakage.; Impacts on other calcifying organisms (e.g., shellfish, plankton)."
mesoamerican_reef["Ocean Acidification"]["Influenced By"] = [
 "Global Carbon Dioxide Emissions"
]
mesoamerican_reef["Ocean Acidification"]["Influences"] = [
        "Mesoamerican Reef - Coral Growth Rates",
        "Mesoamerican Reef - Reef Resilience"
]
mesoamerican_reef["Ocean Acidification"]["Logic Description"] = "Increased atmospheric CO2 is absorbed by the ocean, leading to a decrease in pH (ocean acidification). This reduces the availability of carbonate ions, which corals need to build their skeletons."
mesoamerican_reef["Ocean Acidification"]["Impact Function"] = "impact_ocean_acidification_mesoamerican_reef"

mesoamerican_reef["Pollution"]["Metric"] = "Concentrations of nutrients (nitrogen, phosphorus), sediments, pesticides, and other pollutants in coastal waters."
mesoamerican_reef["Pollution"]["Data Sources"] = [
     "Water quality monitoring programs (often limited).",
    "Research studies."
]
mesoamerican_reef["Pollution"]["Impact on Area"] = "Reduced water quality; increased turbidity."
mesoamerican_reef["Pollution"]["Impact on Biodiversity"] = "Algal overgrowth, smothering corals.; Reduced light penetration.; Direct harm to corals and other organisms."
mesoamerican_reef["Pollution"]["Influenced By"] = [
       "Mesoamerican Reef - Agricultural Runoff",
    "Mesoamerican Reef - Deforestation",
     "Mesoamerican Reef - Urban Runoff",
     "Mesoamerican Reef - Inadequate Wastewater Treatment"
]
mesoamerican_reef["Pollution"]["Influences"] = [
   "Mesoamerican Reef - Coral Reef Health",
   "Mesoamerican Reef - Algal Blooms"
]
mesoamerican_reef["Pollution"]["Logic Description"] = "Runoff from agriculture, deforestation, and urban areas carries pollutants (nutrients, sediments, pesticides) into coastal waters, degrading water quality and impacting coral reefs."
mesoamerican_reef["Pollution"]["Impact Function"] = "impact_pollution_mesoamerican_reef"

mesoamerican_reef["Overfishing"]["Metric"] = "Fish biomass, size structure, and abundance of key species (e.g., groupers, snappers, parrotfish)."
mesoamerican_reef["Overfishing"]["Data Sources"] = [
   "Fisheries data (often limited and unreliable).",
     "Underwater surveys (conducted by research organizations and conservation groups).",
     "Research publications."
]
mesoamerican_reef["Overfishing"]["Impact on Area"] = "Not directly applicable, but affects ecosystem structure."
mesoamerican_reef["Overfishing"]["Impact on Biodiversity"] = "Decline of important fish species.; Disruption of the food web (e.g., loss of herbivores can lead to algal overgrowth).; Loss of top predators."
mesoamerican_reef["Overfishing"]["Influenced By"] = [
    "High Fishing Pressure: Due to local dependence on fishing and tourism.",
   "Weak Enforcement of Fisheries Regulations.",
 "Lack of Alternative Livelihoods."
]
mesoamerican_reef["Overfishing"]["Influences"] = [
  "Mesoamerican Reef - Algal Overgrowth",
    "Mesoamerican Reef - Coral Reef Health"
]
mesoamerican_reef["Overfishing"]["Logic Description"] = "Overfishing is a major problem in the Mesoamerican Reef, depleting populations of important fish species and disrupting the food web."
mesoamerican_reef["Overfishing"]["Impact Function"] = "impact_overfishing_mesoamerican_reef"

mesoamerican_reef["Coastal Development"]["Metric"] = "Area of coastline developed (km or ha); tourism intensity (number of visitors); infrastructure development (e.g., hotels, marinas)."
mesoamerican_reef["Coastal Development"]["Data Sources"] = [
    "Government statistics (tourism, construction).",
  "Remote sensing data.",
  "Reports from conservation organizations."
]
mesoamerican_reef["Coastal Development"]["Impact on Area"] = "Habitat loss (mangroves, seagrass beds); increased sedimentation and pollution."
mesoamerican_reef["Coastal Development"]["Impact on Biodiversity"] = "Loss of critical habitats (nursery grounds for fish).;Reduced water quality.;Physical damage to reefs (from anchors, construction)."
mesoamerican_reef["Coastal Development"]["Influenced By"] = [
    "Tourism Development: Rapid growth in tourism in some areas.",
     "Population Growth: Increased demand for housing and infrastructure.",
     "Government Policies: Land-use planning and zoning."
]
mesoamerican_reef["Coastal Development"]["Influences"] = [
   "Mesoamerican Reef - Water Quality",
  "Mesoamerican Reef - Sedimentation",
 "Mesoamerican Reef - Habitat Loss"
]
mesoamerican_reef["Coastal Development"]["Logic Description"] = "Rapid coastal development, driven by tourism and population growth, is leading to habitat loss, increased sedimentation, and pollution, impacting coral reefs."
mesoamerican_reef["Coastal Development"]["Impact Function"] = "impact_coastal_development_mesoamerican_reef"

mesoamerican_reef["Invasive Species"]["Metric"] = "Abundance and distribution of lionfish (and other invasive species, if relevant)."
mesoamerican_reef["Invasive Species"]["Data Sources"] = [
     "Underwater surveys.",
   "Research studies.",
   "Lionfish removal programs."
]
mesoamerican_reef["Invasive Species"]["Impact on Area"] = "Indirect - affects the native fish populations."
mesoamerican_reef["Invasive Species"]["Impact on Biodiversity"] = "Predation on native fish and invertebrates.; Competition with native predators.;Significant reduction in recruitment of native fish."
mesoamerican_reef["Invasive Species"]["Influenced By"] = [
  "Introduction through the aquarium trade (likely initial introduction).",
  "Lack of Natural Predators: In the Caribbean."
]
mesoamerican_reef["Invasive Species"]["Influences"] = [
 "Mesoamerican Reef - Native Fish Populations",
  "Mesoamerican Reef - Reef Ecosystem Structure"
]
mesoamerican_reef["Invasive Species"]["Logic Description"] = "The invasive lionfish, a voracious predator with no natural predators in the Atlantic/Caribbean, is a major threat to reef fish populations in the Mesoamerican Reef."
mesoamerican_reef["Invasive Species"]["Impact Function"] = "impact_invasive_species_mesoamerican_reef"

# --- Coral Triangle ---
coral_triangle = all_stressors_data["Coral Triangle"]

coral_triangle["Temperature Increase"]["Metric"] = "Sea surface temperature (SST) anomalies (°C above long-term average); frequency and severity of marine heatwaves."
coral_triangle["Temperature Increase"]["Data Sources"] = [
    "NOAA Coral Reef Watch.",
    "Satellite data.",
    "In-situ temperature loggers.",
   "Climate models."
]
coral_triangle["Temperature Increase"]["Impact on Area"] = "Indirect - through coral bleaching and mortality."
coral_triangle["Temperature Increase"]["Impact on Biodiversity"] = "Coral bleaching and mortality, leading to habitat loss. Shifts in species distributions. Increased susceptibility to coral disease."
coral_triangle["Temperature Increase"]["Influenced By"] = [
  "Global Greenhouse Gas Emissions"
]
coral_triangle["Temperature Increase"]["Influences"] = [
  "Coral Triangle - Coral Bleaching",
   "Coral Triangle - Coral Disease",
    "Coral Triangle - Species Shifts"
]
coral_triangle["Temperature Increase"]["Logic Description"] = "Increased sea temperatures, driven by global warming, cause coral bleaching events, which can lead to widespread coral death and reef degradation."
coral_triangle["Temperature Increase"]["Impact Function"] = "impact_temperature_increase_coral_triangle"

coral_triangle["Ocean Acidification"]["Metric"] = "Seawater pH; aragonite saturation state (Ωarag)."
coral_triangle["Ocean Acidification"]["Data Sources"] = [
  "Oceanographic surveys.",
   "Chemical analysis of seawater.",
  "Models that simulate ocean chemistry."
]
coral_triangle["Ocean Acidification"]["Impact on Area"] = "Indirect - reduces coral growth rates and skeletal density."
coral_triangle["Ocean Acidification"]["Impact on Biodiversity"] = "Reduced calcification rates in corals and other calcifying organisms (e.g., shellfish, coralline algae). Impacts on larval development and settlement. Potential for shifts in community structure."
coral_triangle["Ocean Acidification"]["Influenced By"] = [
     "Global Carbon Dioxide Emissions"
]
coral_triangle["Ocean Acidification"]["Influences"] = [
    "Coral Triangle - Coral Growth Rates",
    "Coral Triangle - Reef Resilience"
]
coral_triangle["Ocean Acidification"]["Logic Description"] = "As the ocean absorbs CO2 from the atmosphere, it becomes more acidic, making it harder for corals and other organisms to build their skeletons and shells."
coral_triangle["Ocean Acidification"]["Impact Function"] = "impact_ocean_acidification_coral_triangle"

coral_triangle["Pollution"]["Metric"] = "Concentrations of nutrients (nitrogen, phosphorus), sediments, plastics, and other pollutants in coastal waters."
coral_triangle["Pollution"]["Data Sources"] = [
    "Water quality monitoring programs (often limited).",
     "Research studies.",
    "Remote sensing (for sediment plumes)."
]
coral_triangle["Pollution"]["Impact on Area"] = "Reduced water quality; increased turbidity; nutrient enrichment leading to algal blooms."
coral_triangle["Pollution"]["Impact on Biodiversity"] = "Algal overgrowth, smothering corals. Reduced light penetration. Toxic effects of pollutants on marine life. Plastic pollution harming marine animals (e.g., entanglement, ingestion)."
coral_triangle["Pollution"]["Influenced By"] = [
   "Agricultural Runoff",
    "Deforestation (leading to increased sediment runoff)",
    "Urban Runoff",
    "Industrial Discharge",
  "Inadequate Waste Management (plastic pollution)",
 "Mining Activities"
]
coral_triangle["Pollution"]["Influences"] = [
   "Coral Triangle - Coral Reef Health",
    "Coral Triangle - Algal Blooms",
  "Coral Triangle - Water Quality",
  "Coral Triangle - Marine Life Health"
]
coral_triangle["Pollution"]["Logic Description"] = "Pollution from land-based sources (agriculture, deforestation, urban areas) and marine sources (e.g., plastic pollution) degrades water quality and harms coral reefs and other marine life."
coral_triangle["Pollution"]["Impact Function"] = "impact_pollution_coral_triangle"

coral_triangle["Overfishing"]["Metric"] = "Fish biomass, size structure, and abundance of key species (e.g., groupers, snappers, sharks); catch per unit effort (CPUE)."
coral_triangle["Overfishing"]["Data Sources"] = [
    "Fisheries data (often limited and unreliable).",
     "Underwater surveys.",
    "Research studies.",
    "Reports from conservation organizations (e.g., WWF, TNC)."
]
coral_triangle["Overfishing"]["Impact on Area"] = "Indirect - through changes in reef ecosystem structure and function."
coral_triangle["Overfishing"]["Impact on Biodiversity"] = "Depletion of fish stocks. Removal of top predators, leading to trophic cascades. Changes in fish community structure. Impacts on coral reef health (e.g., by removing herbivorous fish that control algae)."
coral_triangle["Overfishing"]["Influenced By"] = [
  "High Fishing Pressure (due to large coastal populations and dependence on fishing).",
    "Weak Enforcement of Fisheries Regulations.",
    "Lack of Alternative Livelihoods."
]
coral_triangle["Overfishing"]["Influences"] = [
  "Coral Triangle - Trophic Cascades",
 "Coral Triangle - Coral Reef Health",
 "Coral Triangle - Fish Populations"
]
coral_triangle["Overfishing"]["Logic Description"] = "Overfishing is a major threat to the Coral Triangle, depleting fish populations, disrupting the food web, and impacting coral reef health."
coral_triangle["Overfishing"]["Impact Function"] = "impact_overfishing_coral_triangle"

coral_triangle["Destructive Fishing Practices"]["Metric"] = "Frequency of blast fishing and cyanide fishing incidents; area of reef damaged by these practices."
coral_triangle["Destructive Fishing Practices"]["Data Sources"] = [
   "Reports from local communities and fishers.",
    "Underwater surveys (assessing damage to coral reefs).",
  "Law enforcement data (often limited).",
   "Research studies."
]
coral_triangle["Destructive Fishing Practices"]["Impact on Area"] = "Direct and severe damage to coral reefs (physical destruction of coral structure)."
coral_triangle["Destructive Fishing Practices"]["Impact on Biodiversity"] = "High mortality of corals and other reef organisms. Loss of reef habitat. Long-term impacts on reef recovery."
coral_triangle["Destructive Fishing Practices"]["Influenced By"] = [
     "Poverty and Lack of Alternative Livelihoods",
    "Weak Enforcement of Laws and Regulations",
   "High Demand for Live Reef Fish (for the aquarium and restaurant trade)"
]
coral_triangle["Destructive Fishing Practices"]["Influences"] = [
   "Coral Triangle - Coral Reef Structure",
  "Coral Triangle - Fish Populations",
    "Coral Triangle - Reef Recovery"
]
coral_triangle["Destructive Fishing Practices"]["Logic Description"] = "Destructive fishing practices, such as blast fishing (using explosives) and cyanide fishing (using poison), cause significant damage to coral reefs, killing corals and other marine life."
coral_triangle["Destructive Fishing Practices"]["Impact Function"] = "impact_destructive_fishing_coral_triangle"

coral_triangle["Coastal Development"]["Metric"] = "Area of coastline developed; infrastructure development (e.g., ports, resorts); population growth in coastal areas."
coral_triangle["Coastal Development"]["Data Sources"] = [
   "Government statistics.",
    "Remote sensing data.",
 "Reports from conservation organizations."
]
coral_triangle["Coastal Development"]["Impact on Area"] = "Habitat loss (mangroves, seagrass beds); increased sedimentation and pollution."
coral_triangle["Coastal Development"]["Impact on Biodiversity"] = "Loss of critical habitats (nursery grounds for fish); Reduced water quality; Physical damage to reefs."
coral_triangle["Coastal Development"]["Influenced By"] = [
   "Tourism Development",
    "Population Growth",
  "Urbanization",
    "Industrial Development"
]
coral_triangle["Coastal Development"]["Influences"] = [
  "Coral Triangle - Water Quality",
 "Coral Triangle - Sedimentation",
  "Coral Triangle - Habitat Loss"
]
coral_triangle["Coastal Development"]["Logic Description"] = "Coastal development leads to habitat loss, increased pollution, and sedimentation, negatively impacting coral reefs and other coastal ecosystems."
coral_triangle["Coastal Development"]["Impact Function"] = "impact_coastal_development_coral_triangle"

# --- Florida Keys Reefs ---
florida_keys = all_stressors_data["Florida Keys Reefs"]

florida_keys["Temperature Increase"]["Metric"] = "Sea surface temperature (SST) in degrees C, frequency/severity of marine heatwaves, and Degree Heating Weeks (DHW)."
florida_keys["Temperature Increase"]["Data Sources"] = [
    "NOAA Coral Reef Watch.",
    "Florida Keys National Marine Sanctuary (FKNMS) monitoring data.",
    "Research publications."
    ]
florida_keys["Temperature Increase"]["Impact on Area"] = "Coral bleaching, reduced coral growth rates."
florida_keys["Temperature Increase"]["Impact on Biodiversity"] = "Coral mortality. Shifts in species composition. Increased susceptibility to disease."
florida_keys["Temperature Increase"]["Influenced By"] = [
        "Global Greenhouse Gas Emissions"
]
florida_keys["Temperature Increase"]["Influences"] = [
   "Florida Keys Reefs - Coral Bleaching",
    "Florida Keys Reefs - Coral Disease",
   "Florida Keys Reefs - Reef Resilience"
]
florida_keys["Temperature Increase"]["Logic Description"] = "Rising ocean temperatures cause coral bleaching, mortality, and make the reef more susceptible to other stressors"
florida_keys["Temperature Increase"]["Impact Function"] = "impact_temperature_increase_florida_keys_reefs"

florida_keys["Ocean Acidification"]["Metric"] = "Ocean pH, aragonite saturation state"
florida_keys["Ocean Acidification"]["Data Sources"] = [
  "FKNMS monitoring data",
  "Research publications"
]
florida_keys["Ocean Acidification"]["Impact on Area"] = "Reduced coral calcification rates"
florida_keys["Ocean Acidification"]["Impact on Biodiversity"] = "Slower coral growth, Weaker skeletons"
florida_keys["Ocean Acidification"]["Influenced By"] = [
       "Global Carbon Dioxide Emissions"
]
florida_keys["Ocean Acidification"]["Influences"] = [
    "Florida Keys Reefs - Coral Growth Rates",
   "Florida Keys Reefs - Reef Resilience"
]
florida_keys["Ocean Acidification"]["Logic Description"] = "Ocean acidification reduces coral's ability to build their skeletons"
florida_keys["Ocean Acidification"]["Impact Function"] = "impact_ocean_acidification_florida_keys_reefs"

florida_keys["Pollution"]["Metric"] = "Concentrations of nutrients, contaminants and fecal bacteria."
florida_keys["Pollution"]["Data Sources"] = [
    "FKNMS water quality monitoring",
     "Florida Department of Environmental Protection (FDEP) data",
    "US Environmental Protection Agency (EPA) data",
   "Research studies"
]
florida_keys["Pollution"]["Impact on Area"] = "Reduced water quality; algal blooms"
florida_keys["Pollution"]["Impact on Biodiversity"] = "Algal overgrowth smothering corals, coral disease outbreaks, impacts to food web"
florida_keys["Pollution"]["Influenced By"] = [
    "Florida Keys Reefs - Urban Runoff",
    "Florida Keys Reefs - Agricultural Runoff",
   "Florida Keys Reefs - Inadequate Wastewater Treatment",
  "Florida Keys Reefs - Boating Activities"
]
florida_keys["Pollution"]["Influences"] = [
   "Florida Keys Reefs - Coral Reef Health",
    "Florida Keys Reefs - Algal Blooms",
   "Florida Keys Reefs - Disease Outbreaks",
    "Florida Keys Reefs - Water Clarity"
]
florida_keys["Pollution"]["Logic Description"] = "Poor water quality due to nutrient pollution from runoff and inadequate waste treatment is a major stressor."
florida_keys["Pollution"]["Impact Function"] = "impact_pollution_florida_keys_reefs"

florida_keys["Overfishing"]["Metric"] = "Fish biomass, size structure, abundance of key species."
florida_keys["Overfishing"]["Data Sources"] = [
    "Fisheries data.",
  "Underwater surveys."
]
florida_keys["Overfishing"]["Impact on Area"] = "N/A - affects ecosystem structure."
florida_keys["Overfishing"]["Impact on Biodiversity"] = "Loss of key species, changes in trophic structure, increased algal growth."
florida_keys["Overfishing"]["Influenced By"] = [
     "Fishing pressure."
]
florida_keys["Overfishing"]["Influences"] = [
     "Florida Keys Reefs - Food Web Dynamics",
    "Florida Keys Reefs - Reef Health"
]
florida_keys["Overfishing"]["Logic Description"] = "Overfishing removes key species, impacting food web."
florida_keys["Overfishing"]["Impact Function"] = "impact_overfishing_florida_keys_reefs"

florida_keys["Coastal Development"]["Metric"] = "Area of coastline developed; infrastructure development."
florida_keys["Coastal Development"]["Data Sources"] = [
   "Government statistics.",
   "Remote sensing."
]
florida_keys["Coastal Development"]["Impact on Area"] = "Habitat loss; increased pollution."
florida_keys["Coastal Development"]["Impact on Biodiversity"] = "Loss of critical habitats; reduced water quality."
florida_keys["Coastal Development"]["Influenced By"] = [
    "Tourism Development",
    "Population Growth"
]
florida_keys["Coastal Development"]["Influences"] = [
    "Florida Keys Reefs - Water Quality",
   "Florida Keys Reefs - Sedimentation",
    "Florida Keys Reefs - Habitat Loss"
]
florida_keys["Coastal Development"]["Logic Description"] = "Coastal development leads to habitat loss, increased pollution."
florida_keys["Coastal Development"]["Impact Function"] = "impact_coastal_development_florida_keys_reefs"

florida_keys["Invasive Species"]["Metric"] = "Abundance and distribution of lionfish (and other invasive species, if relevant)."
florida_keys["Invasive Species"]["Data Sources"] = [
   "Underwater surveys",
   "Research"
]
florida_keys["Invasive Species"]["Impact on Area"] = "Impacts native fish populations."
florida_keys["Invasive Species"]["Impact on Biodiversity"] = "Predation on native fish and invertebrates; competition."
florida_keys["Invasive Species"]["Influenced By"] = [
     "Introduction events"
]
florida_keys["Invasive Species"]["Influences"] = [
     "Florida Keys Reefs - Native fish populations"
]
florida_keys["Invasive Species"]["Logic Description"] = "The invasive lionfish is a major threat to native reef fish."
florida_keys["Invasive Species"]["Impact Function"] = "impact_invasive_species_florida_keys_reefs"

florida_keys["Coral Disease"]["Metric"] = "Prevalence and severity of coral diseases (e.g., white band disease, black band disease, stony coral tissue loss disease)."
florida_keys["Coral Disease"]["Data Sources"] = [
  "Underwater surveys.",
 "Research Studies"
]
florida_keys["Coral Disease"]["Impact on Area"] = "Coral mortality; changes in coral community structure."
florida_keys["Coral Disease"]["Impact on Biodiversity"] = "Significant coral mortality. Loss of coral cover. Shifts in species composition."
florida_keys["Coral Disease"]["Influenced By"] = [
   "Florida Keys Reefs - Water Pollution",
   "Florida Keys Reefs - Ocean Warming",
    "Other Stressors"
]
florida_keys["Coral Disease"]["Influences"] = [
    "Florida Keys Reefs - Coral Cover",
   "Florida Keys Reefs - Reef Resilience"
]
florida_keys["Coral Disease"]["Logic Description"] = "Coral diseases have caused significant coral mortality in the Florida Keys. Stony Coral Tissue Loss Disease (SCTLD) has been particularly devastating."
florida_keys["Coral Disease"]["Impact Function"] = "impact_coral_disease_florida_keys_reefs"

# --- Caribbean Reefs ---
caribbean_reefs = all_stressors_data["Caribbean Reefs"]

caribbean_reefs["Temperature Increase"]["Metric"] = "Sea surface temperature (SST) anomalies, frequency/severity of marine heatwaves, DHW."
caribbean_reefs["Temperature Increase"]["Data Sources"] = [
     "NOAA Coral Reef Watch",
    "Satellite data",
    "In-situ temperature loggers",
     "Research publications"
]
caribbean_reefs["Temperature Increase"]["Impact on Area"] = "Coral bleaching, reduced growth rates."
caribbean_reefs["Temperature Increase"]["Impact on Biodiversity"] = "Coral mortality, shifts in species composition, increased disease susceptibility."
caribbean_reefs["Temperature Increase"]["Influenced By"] = [
    "Global Greenhouse Gas Emissions"
]
caribbean_reefs["Temperature Increase"]["Influences"] = [
    "Caribbean Reefs - Coral Bleaching",
     "Caribbean Reefs - Coral Disease",
    "Caribbean Reefs - Reef Resilience"
]
caribbean_reefs["Temperature Increase"]["Logic Description"] = "Rising ocean temperatures are a major threat, causing widespread bleaching and mortality."
caribbean_reefs["Temperature Increase"]["Impact Function"] = "impact_temperature_increase_caribbean_reefs"

caribbean_reefs["Ocean Acidification"]["Metric"] = "Ocean pH, aragonite saturation state."
caribbean_reefs["Ocean Acidification"]["Data Sources"] = [
 "Oceanographic surveys",
 "Chemical analysis",
  "Models"
]
caribbean_reefs["Ocean Acidification"]["Impact on Area"] = "Reduced coral calcification rates."
caribbean_reefs["Ocean Acidification"]["Impact on Biodiversity"] = "Slower coral growth, weaker skeletons."
caribbean_reefs["Ocean Acidification"]["Influenced By"] = [
  "Global Carbon Dioxide Emissions"
]
caribbean_reefs["Ocean Acidification"]["Influences"] = [
    "Caribbean Reefs - Coral Growth Rates",
   "Caribbean Reefs - Reef Resilience"
]
caribbean_reefs["Ocean Acidification"]["Logic Description"] = "Ocean acidification hinders coral growth and makes them more vulnerable."
caribbean_reefs["Ocean Acidification"]["Impact Function"] = "impact_ocean_acidification_caribbean_reefs"

caribbean_reefs["Pollution"]["Metric"] = "Concentrations of nutrients (nitrogen, phosphorus), sediments, and other pollutants."
caribbean_reefs["Pollution"]["Data Sources"] = [
  "Water quality monitoring programs",
   "Research studies"
]
caribbean_reefs["Pollution"]["Impact on Area"] = "Reduced water quality; algal blooms; increased sedimentation."
caribbean_reefs["Pollution"]["Impact on Biodiversity"] = "Algal overgrowth, smothering corals; Reduced light; Harm to marine life."
caribbean_reefs["Pollution"]["Influenced By"] = [
     "Caribbean Reefs - Agricultural Runoff",
  "Caribbean Reefs - Urban Runoff",
    "Caribbean Reefs - Deforestation",
     "Caribbean Reefs - Industrial Discharge",
     "Caribbean Reefs - Inadequate Wastewater Treatment"
]
caribbean_reefs["Pollution"]["Influences"] = [
   "Caribbean Reefs - Coral Reef Health",
    "Caribbean Reefs - Algal Blooms",
  "Caribbean Reefs - Water Quality"
]
caribbean_reefs["Pollution"]["Logic Description"] = "Pollution from land-based sources degrades water quality and harms coral reefs."
caribbean_reefs["Pollution"]["Impact Function"] = "impact_pollution_caribbean_reefs"

caribbean_reefs["Overfishing"]["Metric"] = "Fish biomass, size structure, and abundance of key species."
caribbean_reefs["Overfishing"]["Data Sources"] = [
   "Fisheries data (often limited).",
  "Underwater surveys.",
 "Research studies"
]
caribbean_reefs["Overfishing"]["Impact on Area"] = "N/A - affects ecosystem structure."
caribbean_reefs["Overfishing"]["Impact on Biodiversity"] = "Loss of key species; Trophic cascades; Reduced reef resilience."
caribbean_reefs["Overfishing"]["Influenced By"] = [
   "High fishing pressure."
]
caribbean_reefs["Overfishing"]["Influences"] = [
     "Caribbean Reefs - Food Web Dynamics",
   "Caribbean Reefs - Algal Growth",
   "Caribbean Reefs - Reef Health"
]
caribbean_reefs["Overfishing"]["Logic Description"] = "Overfishing removes key species, disrupting the food web and often leading to algal overgrowth."
caribbean_reefs["Overfishing"]["Impact Function"] = "impact_overfishing_caribbean_reefs"

caribbean_reefs["Coastal Development"]["Metric"] = "Area of coastline developed; infrastructure development; tourism intensity."
caribbean_reefs["Coastal Development"]["Data Sources"] = [
   "Government statistics.",
    "Remote sensing data.",
 "Reports from conservation organizations"
]
caribbean_reefs["Coastal Development"]["Impact on Area"] = "Habitat loss (mangroves, seagrass); increased pollution and sedimentation."
caribbean_reefs["Coastal Development"]["Impact on Biodiversity"] = "Loss of critical habitats.;Reduced water quality.;Physical damage to reefs."
caribbean_reefs["Coastal Development"]["Influenced By"] = [
  "Tourism Development",
    "Population Growth",
   "Urbanization"
]
caribbean_reefs["Coastal Development"]["Influences"] = [
 "Caribbean Reefs - Water Quality",
    "Caribbean Reefs - Sedimentation",
   "Caribbean Reefs - Habitat Loss"
]
caribbean_reefs["Coastal Development"]["Logic Description"] = "Coastal development leads to habitat loss, increased pollution, and sedimentation, harming reefs."
caribbean_reefs["Coastal Development"]["Impact Function"] = "impact_coastal_development_caribbean_reefs"

caribbean_reefs["Invasive Species"]["Metric"] = "Abundance and distribution of lionfish (and other relevant invasive species)."
caribbean_reefs["Invasive Species"]["Data Sources"] = [
    "Underwater surveys.",
  "Lionfish removal programs.",
  "Research studies."
]
caribbean_reefs["Invasive Species"]["Impact on Area"] = "Indirectly affects reef area through impacts on biodiversity."
caribbean_reefs["Invasive Species"]["Impact on Biodiversity"] = "Predation on native fish and invertebrates. Competition with native predators. Reduction in native fish populations."
caribbean_reefs["Invasive Species"]["Influenced By"] = [
   "Introduction through the aquarium trade."
]
caribbean_reefs["Invasive Species"]["Influences"] = [
   "Caribbean Reefs - Native Fish Populations",
  "Caribbean Reefs - Reef Ecosystem Structure"
]
caribbean_reefs["Invasive Species"]["Logic Description"] = "The invasive lionfish is a significant threat to native reef fish populations throughout the Caribbean."
caribbean_reefs["Invasive Species"]["Impact Function"] = "impact_invasive_species_caribbean_reefs"

caribbean_reefs["Coral Disease"]["Metric"] = "Prevalence and severity of coral diseases (e.g., white band disease, black band disease, stony coral tissue loss disease)."
caribbean_reefs["Coral Disease"]["Data Sources"] = [
    "Underwater surveys.",
     "Research publications.",
   "Monitoring programs."
]
caribbean_reefs["Coral Disease"]["Impact on Area"] = "Coral mortality; changes in coral community structure; significant loss of coral cover."
caribbean_reefs["Coral Disease"]["Impact on Biodiversity"] = "Loss of coral cover and diversity. Shifts in reef community composition. Reduced reef resilience."
caribbean_reefs["Coral Disease"]["Influenced By"] = [
  "Caribbean Reefs - Water Pollution",
 "Caribbean Reefs - Ocean Warming",
    "Other Stressors"
]
caribbean_reefs["Coral Disease"]["Influences"] = [
 "Caribbean Reefs - Coral Cover",
  "Caribbean Reefs - Reef Resilience"
]
caribbean_reefs["Coral Disease"]["Logic Description"] = "Coral diseases, exacerbated by other stressors, have caused widespread coral mortality across the Caribbean. Stony Coral Tissue Loss Disease (SCTLD) is a particularly aggressive and damaging disease."
caribbean_reefs["Coral Disease"]["Impact Function"] = "impact_coral_disease_caribbean_reefs"

# --- Red Sea Reefs ---
red_sea_reefs = all_stressors_data["Red Sea Reefs"]

red_sea_reefs["Temperature Increase"]["Metric"] = "Sea surface temperature (SST) anomalies (°C above long-term average); frequency and severity of marine heatwaves."
red_sea_reefs["Temperature Increase"]["Data Sources"] = [
    "NOAA Coral Reef Watch.",
    "Satellite data.",
    "In-situ temperature loggers.",
    "Research publications (e.g., studies on Red Sea coral resilience).",
]
red_sea_reefs["Temperature Increase"]["Impact on Area"] = "Potential for coral bleaching, though Red Sea corals are relatively heat-tolerant."
red_sea_reefs["Temperature Increase"]["Impact on Biodiversity"] = "While Red Sea corals are more resistant to bleaching than corals in many other regions, extreme temperatures can still cause bleaching and mortality. Potential shifts in species distributions."
red_sea_reefs["Temperature Increase"]["Influenced By"] = [
    "Global Greenhouse Gas Emissions"
]
red_sea_reefs["Temperature Increase"]["Influences"] = [
    "Red Sea Reefs - Coral Bleaching"
]
red_sea_reefs["Temperature Increase"]["Logic Description"] = "Although Red Sea corals have a higher thermal tolerance, continued warming poses a long-term threat, especially if combined with other stressors."
red_sea_reefs["Temperature Increase"]["Impact Function"] = "impact_temperature_increase_red_sea_reefs"

red_sea_reefs["Ocean Acidification"]["Metric"] = "Ocean pH; aragonite saturation state (Ωarag)."
red_sea_reefs["Ocean Acidification"]["Data Sources"] = [
  "Oceanographic surveys.",
    "Chemical analysis of seawater samples.",
    "Models that simulate ocean chemistry.",
    "Research publications."
]
red_sea_reefs["Ocean Acidification"]["Impact on Area"] = "Reduced calcification rates of corals and other calcifying organisms."
red_sea_reefs["Ocean Acidification"]["Impact on Biodiversity"] = "Slower coral growth.; Weaker coral skeletons.; Impacts on other calcifying organisms."
red_sea_reefs["Ocean Acidification"]["Influenced By"] = [
    "Global Carbon Dioxide Emissions"
]
red_sea_reefs["Ocean Acidification"]["Influences"] = [
   "Red Sea Reefs - Coral Growth Rates",
    "Red Sea Reefs - Reef Resilience"
]
red_sea_reefs["Ocean Acidification"]["Logic Description"] = "Ocean acidification reduces the availability of carbonate ions, which corals need to build their skeletons. The impact on Red Sea corals might be less immediate than in other regions, but it's a long-term concern."
red_sea_reefs["Ocean Acidification"]["Impact Function"] = "impact_ocean_acidification_red_sea_reefs"

red_sea_reefs["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., nutrients, heavy metals, oil) in seawater and sediments."
red_sea_reefs["Pollution"]["Data Sources"] = [
     "Water quality monitoring programs (limited in some areas).",
    "Research studies."
]
red_sea_reefs["Pollution"]["Impact on Area"] = "Reduced water quality."
red_sea_reefs["Pollution"]["Impact on Biodiversity"] = "Toxic effects on corals and other reef organisms.; Eutrophication (in some areas)."
red_sea_reefs["Pollution"]["Influenced By"] = [
  "Coastal Development",
    "Industrial Discharge",
  "Shipping Activities (oil spills, discharge of waste)",
   "Agricultural Runoff (in some areas)"
]
red_sea_reefs["Pollution"]["Influences"] = [
 "Red Sea Reefs - Coral Health",
    "Red Sea Reefs - Water Quality"
]
red_sea_reefs["Pollution"]["Logic Description"] = "Pollution from coastal development, industrial discharge, and shipping activities can degrade water quality and harm coral reefs."
red_sea_reefs["Pollution"]["Impact Function"] = "impact_pollution_red_sea_reefs"

red_sea_reefs["Overfishing"]["Metric"] = "Fish biomass, size structure, and abundance of key species."
red_sea_reefs["Overfishing"]["Data Sources"] = [
  "Fisheries data (often limited).",
   "Underwater surveys.",
    "Research studies."
]
red_sea_reefs["Overfishing"]["Impact on Area"] = "Indirect, through changes in reef ecosystem structure."
red_sea_reefs["Overfishing"]["Impact on Biodiversity"] = "Decline of important fish species.; Disruption of the food web."
red_sea_reefs["Overfishing"]["Influenced By"] = [
    "Fishing Pressure",
  "Weak Enforcement of Fisheries Regulations"
]
red_sea_reefs["Overfishing"]["Influences"] = [
  "Red Sea Reefs - Trophic Cascades",
    "Red Sea Reefs - Reef Health"
]
red_sea_reefs["Overfishing"]["Logic Description"] = "Overfishing can impact fish populations and disrupt the balance of the reef ecosystem."
red_sea_reefs["Overfishing"]["Impact Function"] = "impact_overfishing_red_sea_reefs"

red_sea_reefs["Coastal Development"]["Metric"] = "Area of coastline developed (km or ha); tourism intensity (number of visitors); infrastructure development (e.g., hotels, ports)."
red_sea_reefs["Coastal Development"]["Data Sources"] = [
    "Government statistics (tourism, construction).",
   "Remote sensing data.",
 "Reports from conservation organizations."
]
red_sea_reefs["Coastal Development"]["Impact on Area"] = "Habitat loss (e.g., mangroves, seagrass beds); increased sedimentation and pollution."
red_sea_reefs["Coastal Development"]["Impact on Biodiversity"] = "Loss of critical habitats.; Reduced water quality.; Physical damage to reefs (from construction, anchors)."
red_sea_reefs["Coastal Development"]["Influenced By"] = [
    "Tourism Development: Rapid growth in tourism in some areas (e.g., Egypt, Saudi Arabia).",
   "Urbanization: Expansion of coastal cities.",
   "Industrial Development (e.g., ports, desalination plants)."
]
red_sea_reefs["Coastal Development"]["Influences"] = [
  "Red Sea Reefs - Water Quality",
  "Red Sea Reefs - Sedimentation",
   "Red Sea Reefs - Habitat Loss"
]
red_sea_reefs["Coastal Development"]["Logic Description"] = "Rapid coastal development, driven by tourism, urbanization, and industrial expansion, is a growing threat, leading to habitat loss, increased sedimentation, and pollution."
red_sea_reefs["Coastal Development"]["Impact Function"] = "impact_coastal_development_red_sea_reefs"

# --- North American Prairies ---
north_american_prairies = all_stressors_data["North American Prairies"]

north_american_prairies["Land-Use Change"]["Metric"] = "Area converted to agriculture, urban development, or other land uses (ha/year)."
north_american_prairies["Land-Use Change"]["Data Sources"] = [
    "USDA National Agricultural Statistics Service (NASS).",
    "USGS National Land Cover Database (NLCD).",
    "Canadian government data (e.g., Agriculture and Agri-Food Canada).",
    "Remote sensing data."
]
north_american_prairies["Land-Use Change"]["Impact on Area"] = "Drastic reduction in prairie area (historically, the most significant stressor)."
north_american_prairies["Land-Use Change"]["Impact on Biodiversity"] = "Massive habitat loss and fragmentation. Decline of prairie-dependent species (plants, animals, insects). Increased risk of extinction for many species."
north_american_prairies["Land-Use Change"]["Influenced By"] = [
    "North American Prairies - Agricultural Expansion",
    "North American Prairies - Urban Sprawl",
    "North American Prairies - Government Policies"
]
north_american_prairies["Land-Use Change"]["Influences"] = [
    "North American Prairies - Habitat Fragmentation"
]
north_american_prairies["Land-Use Change"]["Logic Description"] = "Conversion of prairie to agriculture and urban areas has been the dominant stressor, leading to massive habitat loss and fragmentation. This is the primary reason why prairies are one of the most endangered ecosystems on Earth."
north_american_prairies["Land-Use Change"]["Impact Function"] = "impact_land_use_change_north_american_prairies"

north_american_prairies["Habitat Fragmentation"]["Metric"] = "Patch size distribution; edge density; connectivity indices."
north_american_prairies["Habitat Fragmentation"]["Data Sources"] = [
   "Land cover data (from remote sensing and other sources).",
    "GIS analysis."
]
north_american_prairies["Habitat Fragmentation"]["Impact on Area"] = "Remaining prairie exists in small, isolated patches."
north_american_prairies["Habitat Fragmentation"]["Impact on Biodiversity"] = "Reduced gene flow.; Increased edge effects (exposure to predators, invasive species, altered microclimate).; Limited dispersal ability for many species.; Increased vulnerability to stochastic events (e.g., disease outbreaks, extreme weather)."
north_american_prairies["Habitat Fragmentation"]["Influenced By"] = [
   "North American Prairies - Land-Use Change",
   "North American Prairies - Infrastructure Development"
]
north_american_prairies["Habitat Fragmentation"]["Influences"] = [
   "Exacerbates impacts of other stressors."
]
north_american_prairies["Habitat Fragmentation"]["Logic Description"] = "Fragmentation, a consequence of land-use change, isolates remaining prairie patches, reducing their ecological viability and increasing the vulnerability of prairie species."
north_american_prairies["Habitat Fragmentation"]["Impact Function"] = "impact_habitat_fragmentation_north_american_prairies"

north_american_prairies["Invasive Species"]["Metric"] = "Abundance and distribution of key invasive species (e.g., smooth brome, leafy spurge, cheatgrass)."
north_american_prairies["Invasive Species"]["Data Sources"] = [
   "Vegetation surveys.",
    "Research studies.",
   "Land management agency data."
]
north_american_prairies["Invasive Species"]["Impact on Area"] = "Changes in vegetation composition and structure."
north_american_prairies["Invasive Species"]["Impact on Biodiversity"] = "Competition with native prairie plants.; Altered fire regimes (some invasives increase fire frequency or intensity).; Reduced forage quality for native grazers.; Changes in soil properties."
north_american_prairies["Invasive Species"]["Influenced By"] = [
  "North American Prairies - Disturbance",
   "North American Prairies - Climate Change",
   "North American Prairies - Introduction"
]
north_american_prairies["Invasive Species"]["Influences"] = [
  "North American Prairies - Fire Regimes"
]
north_american_prairies["Invasive Species"]["Logic Description"] = "Invasive species outcompete native prairie plants, altering ecosystem structure and function."
north_american_prairies["Invasive Species"]["Impact Function"] = "impact_invasive_species_north_american_prairies"

north_american_prairies["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality); increased frequency and severity of drought."
north_american_prairies["Climate Change"]["Data Sources"] = [
    "Climate Models",
    "Historical Records"
    ]
north_american_prairies["Climate Change"]["Impact on Area"] = "Indirect; changes in growing conditions."
north_american_prairies["Climate Change"]["Impact on Biodiversity"] = "Shifts in species distributions.; Increased stress on native species.; Changes in phenology.; Increased fire risk (in some areas).; May favor some invasive species."
north_american_prairies["Climate Change"]["Influenced By"] = [
        "Global GHG"
]
north_american_prairies["Climate Change"]["Influences"] = [
       "North American Prairies - Fire Regimes",
       "North American Prairies - Water Availability"
]
north_american_prairies["Climate Change"]["Logic Description"] = "Climate change is altering temperature and precipitation patterns, increasing stress on prairie ecosystems and potentially favoring invasive species."
north_american_prairies["Climate Change"]["Impact Function"] = "impact_climate_change_north_american_prairies"

north_american_prairies["Fire Suppression"]["Metric"] = "Fire frequency (return interval - years); area burned (ha/year)."
north_american_prairies["Fire Suppression"]["Data Sources"] = [
 "Historical fire records.",
   "Land management agency data."
]
north_american_prairies["Fire Suppression"]["Impact on Area"] = "Changes in vegetation structure (woody encroachment)."
north_american_prairies["Fire Suppression"]["Impact on Biodiversity"] = "Loss of open prairie habitat.; Decline of fire-dependent species.; Increased fuel loads, leading to more intense fires when they do occur."
north_american_prairies["Fire Suppression"]["Influenced By"] = [
     "North American Prairies - Land Management Practices"
]
north_american_prairies["Fire Suppression"]["Influences"] = [
     "North American Prairies - Woody Encroachment",
     "North American Prairies - Fire Intensity"
]
north_american_prairies["Fire Suppression"]["Logic Description"] = "Fire suppression, a common management practice, has altered the natural fire regime of prairies, leading to woody encroachment (trees and shrubs invading grasslands) and the decline of fire-dependent species."
north_american_prairies["Fire Suppression"]["Impact Function"] = "impact_fire_suppression_north_american_prairies"

north_american_prairies["Overgrazing"]["Metric"] = "Livestock Density, vegetation cover"
north_american_prairies["Overgrazing"]["Data Sources"] = [
    "Agricultural Statistics",
   "Vegetation surveys"
]
north_american_prairies["Overgrazing"]["Impact on Area"] = "Changes in vegetation, soil erosion."
north_american_prairies["Overgrazing"]["Impact on Biodiversity"] = "Loss of palatable species.; Spread of invasives.; Soil compaction."
north_american_prairies["Overgrazing"]["Influenced By"] = [
 "North American Prairies - Livestock Management"
]
north_american_prairies["Overgrazing"]["Influences"] = [
        "North American Prairies - Vegetation Changes"
]
north_american_prairies["Overgrazing"]["Logic Description"] = "Overgrazing can degrade prairie vegetation, leading to soil erosion and the spread of invasive species."
north_american_prairies["Overgrazing"]["Impact Function"] = "impact_overgrazing_north_american_prairies"

north_american_prairies["Agricultural Expansion"]["Impact Function"] = "impact_agricultural_expansion_north_american_prairies"
north_american_prairies["Urban Sprawl"]["Impact Function"] = "impact_urban_sprawl_north_american_prairies"
north_american_prairies["Government Policies"]["Impact Function"] = "impact_government_policies_north_american_prairies"
north_american_prairies["Infrastructure Development"]["Impact Function"] = "impact_infrastructure_development_north_american_prairies"
north_american_prairies["Disturbance"]["Impact Function"] = "impact_disturbance_north_american_prairies"
north_american_prairies["Introduction"]["Impact Function"] = "impact_introduction_north_american_prairies"
north_american_prairies["Land Management Practices"]["Impact Function"] = "impact_land_management_practices_north_american_prairies"
north_american_prairies["Fire Regimes"]["Impact Function"] = "impact_fire_regimes_north_american_prairies"
north_american_prairies["Woody Encroachment"]["Impact Function"] = "impact_woody_encroachment_north_american_prairies"
north_american_prairies["Fire Intensity"]["Impact Function"] = "impact_fire_intensity_north_american_prairies"
north_american_prairies["Water Availability"]["Impact Function"] = "impact_water_availability_north_american_prairies"
north_american_prairies["Vegetation Changes"]["Impact Function"] = "impact_vegetation_changes_north_american_prairies"

# --- African Savannas ---
african_savannas = all_stressors_data["African Savannas"]

african_savannas["Land-Use Change"]["Metric"] = "Area converted to agriculture, settlements, or other land uses (ha/year)."
african_savannas["Land-Use Change"]["Data Sources"] = [
    "Remote sensing data.",
    "National government statistics (various African countries).",
    "Research publications."
]
african_savannas["Land-Use Change"]["Impact on Area"] = "Loss of savanna habitat; fragmentation."
african_savannas["Land-Use Change"]["Impact on Biodiversity"] = "Habitat loss and fragmentation; Disruption of migration routes (for large mammals); Increased human-wildlife conflict."
african_savannas["Land-Use Change"]["Influenced By"] = [
    "African Savannas - Agricultural Expansion",
    "African Savannas - Population Growth",
    "African Savannas - Government Policies"
]
african_savannas["Land-Use Change"]["Influences"] = [
     "African Savannas - Habitat Fragmentation"
]
african_savannas["Land-Use Change"]["Logic Description"] = "Conversion of savanna to agriculture and settlements is a major threat, leading to habitat loss, fragmentation, and increased conflict between humans and wildlife."
african_savannas["Land-Use Change"]["Impact Function"] = "impact_land_use_change_african_savannas"

african_savannas["Habitat Fragmentation"]["Metric"] = "Patch size distribution; edge density; connectivity indices."
african_savannas["Habitat Fragmentation"]["Data Sources"] = [
    "Land cover data (from remote sensing).",
    "GIS analysis."
]
african_savannas["Habitat Fragmentation"]["Impact on Area"] = "Remaining savanna exists in increasingly isolated patches."
african_savannas["Habitat Fragmentation"]["Impact on Biodiversity"] = "Reduced gene flow; Increased edge effects.; Limited dispersal ability.; Increased vulnerability to stochastic events."
african_savannas["Habitat Fragmentation"]["Influenced By"] = [
       "African Savannas - Land-Use Change"
]
african_savannas["Habitat Fragmentation"]["Influences"] = [
 "Exacerbates other stressor impacts"  #Generic impact
]
african_savannas["Habitat Fragmentation"]["Logic Description"] = "Fragmentation isolates savanna patches, reducing their ecological viability and increasing the vulnerability of wildlife populations."
african_savannas["Habitat Fragmentation"]["Impact Function"] = "impact_habitat_fragmentation_african_savannas"

african_savannas["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality); increased frequency and severity of drought."
african_savannas["Climate Change"]["Data Sources"] = [
    "Climate models.",
   "Historical records"
]
african_savannas["Climate Change"]["Impact on Area"] = "Indirect; changes in growing conditions."
african_savannas["Climate Change"]["Impact on Biodiversity"] = "Shifts in species distributions.; Increased stress on savanna species.; Changes in phenology.; Increased fire risk (in some areas).; Changes in water availability."
african_savannas["Climate Change"]["Influenced By"] = [
      "Global GHG"
]
african_savannas["Climate Change"]["Influences"] = [
         "African Savannas - Fire Regimes",
       "African Savannas - Water Availability"
]
african_savannas["Climate Change"]["Logic Description"] = "Climate change is altering temperature and precipitation patterns, increasing stress on savanna ecosystems and impacting water resources."
african_savannas["Climate Change"]["Impact Function"] = "impact_climate_change_african_savannas"

african_savannas["Wildfires"]["Metric"] = "Fire frequency (return interval); area burned (ha/year); fire intensity."
african_savannas["Wildfires"]["Data Sources"] = [
  "Remote sensing data (fire detection).",
 "Research studies.",
    "Local community knowledge."
]
african_savannas["Wildfires"]["Impact on Area"] = "Changes in vegetation structure and composition (can be both beneficial and detrimental, depending on fire regime)."
african_savannas["Wildfires"]["Impact on Biodiversity"] = "Many savanna species are adapted to fire, and fire is a natural and important process.; However, changes in fire frequency, intensity, or timing (due to climate change or human activities) can have negative impacts.; Too frequent or intense fires can damage trees and favor grasses.; Too infrequent fires can lead to woody encroachment."
african_savannas["Wildfires"]["Influenced By"] = [
    "African Savannas - Climate Change",
    "African Savannas - Human Activities",
    "African Savannas - Land-Use Change"
]
african_savannas["Wildfires"]["Influences"] = [
  "African Savannas - Vegetation Structure"
]
african_savannas["Wildfires"]["Logic Description"] = "Fire is a natural and important process in savannas, but changes in fire regimes due to climate change and human activities can have significant ecological impacts."
african_savannas["Wildfires"]["Impact Function"] = "impact_wildfires_african_savannas"

african_savannas["Poaching"]["Metric"] = "Number of illegally killed animals (for key species, e.g., elephants, rhinos); poaching incidents."
african_savannas["Poaching"]["Data Sources"] = [
    "Law enforcement data.",
   "Wildlife monitoring programs.",
    "Reports from conservation organizations."
]
african_savannas["Poaching"]["Impact on Area"] = "Indirect (through impacts on wildlife populations)."
african_savannas["Poaching"]["Impact on Biodiversity"] = "Decline of key species (e.g., elephants, rhinos, lions).; Cascading effects on the ecosystem (e.g., loss of keystone herbivores can alter vegetation structure). Loss of genetic diversity."
african_savannas["Poaching"]["Influenced By"] = [
   "Demand for Wildlife Products: Ivory, rhino horn, bushmeat.",
   "Poverty and Lack of Economic Opportunities: Can drive people to poaching.",
 "Weak Law Enforcement and Governance.",
    "Organized Crime: Involvement of criminal networks."
]
african_savannas["Poaching"]["Influences"] = [
      "African Savannas - Wildlife Populations",
    "African Savannas - Ecosystem Function"
]
african_savannas["Poaching"]["Logic Description"] = "Poaching, driven by demand for wildlife products and other factors, is a major threat to many savanna species, with cascading effects on the ecosystem."
african_savannas["Poaching"]["Impact Function"] = "impact_poaching_african_savannas" #Corrected function name.

african_savannas["Overgrazing"]["Metric"] = "Livestock density; vegetation cover and composition; soil erosion."
african_savannas["Overgrazing"]["Data Sources"] = [
 "Agricultural statistics",
  "Vegetation surveys.",
 "Remote sensing"
]
african_savannas["Overgrazing"]["Impact on Area"] = "Changes in vegetation structure; soil degradation."
african_savannas["Overgrazing"]["Impact on Biodiversity"] = "Loss of palatable plant species.; Spread of unpalatable or invasive species.; Soil compaction and erosion.; Competition with wild herbivores."
african_savannas["Overgrazing"]["Influenced By"] = [
     "African Savannas - Livestock Management",
    "Population Growth: Increased demand for livestock products."
]
african_savannas["Overgrazing"]["Influences"] = [
 "African Savannas - Vegetation Structure"
]
african_savannas["Overgrazing"]["Logic Description"] = "Overgrazing by livestock can degrade savanna vegetation, leading to soil erosion and competition with wild herbivores."
african_savannas["Overgrazing"]["Impact Function"] = "impact_overgrazing_african_savannas"

african_savannas["Invasive Species"]["Metric"] = "Abundance/Distribution of key invasive species."
african_savannas["Invasive Species"]["Data Sources"] = [
    "Vegetation surveys.",
  "Research."
]
african_savannas["Invasive Species"]["Impact on Area"] = "Changes in vegetation composition."
african_savannas["Invasive Species"]["Impact on Biodiversity"] = "Competition with native species.; Altered fire regimes."
african_savannas["Invasive Species"]["Influenced By"] = [
     "African Savannas - Disturbance",
   "African Savannas - Climate Change"
]
african_savannas["Invasive Species"]["Influences"] = [
  "African Savannas - Native Plant Communities"
]
african_savannas["Invasive Species"]["Logic Description"] = "Invasive species can outcompete native plants and alter ecosystem processes."
african_savannas["Invasive Species"]["Impact Function"] = "impact_invasive_species_african_savannas"

# --- Eurasian Steppes ---
eurasian_steppes = all_stressors_data["Eurasian Steppes"]

eurasian_steppes["Land-Use Change"]["Metric"] = "Area converted to agriculture, settlements, or other land uses (ha/year)."
eurasian_steppes["Land-Use Change"]["Data Sources"] = [
    "Remote sensing data.",
    "National government statistics (various countries across Eurasia).",
    "Research publications."
]
eurasian_steppes["Land-Use Change"]["Impact on Area"] = "Loss of steppe habitat; fragmentation."
eurasian_steppes["Land-Use Change"]["Impact on Biodiversity"] = "Habitat loss and fragmentation.; Decline of steppe-dependent species."
eurasian_steppes["Land-Use Change"]["Influenced By"] = [
     "Eurasian Steppes - Agricultural Expansion",
    "Eurasian Steppes - Population Growth",
     "Eurasian Steppes - Government Policies"
]
eurasian_steppes["Land-Use Change"]["Influences"] = [
   "Eurasian Steppes - Habitat Fragmentation"
]
eurasian_steppes["Land-Use Change"]["Logic Description"] = "Conversion of steppe to agriculture, particularly large-scale agriculture, is a major threat, leading to habitat loss and fragmentation."
eurasian_steppes["Land-Use Change"]["Impact Function"] = "impact_land_use_change_eurasian_steppes"


eurasian_steppes["Habitat Fragmentation"]["Metric"] = "Patch size distribution; edge density; connectivity indices."
eurasian_steppes["Habitat Fragmentation"]["Data Sources"] = [
        "Land cover data (from remote sensing).",
        "GIS analysis."
]
eurasian_steppes["Habitat Fragmentation"]["Impact on Area"] = "Remaining steppe exists in increasingly isolated patches."
eurasian_steppes["Habitat Fragmentation"]["Impact on Biodiversity"] = "Reduced gene flow.; Increased edge effects.; Limited dispersal ability.; Increased vulnerability to stochastic events."
eurasian_steppes["Habitat Fragmentation"]["Influenced By"] = [
      "Eurasian Steppes - Land-Use Change"
]
eurasian_steppes["Habitat Fragmentation"]["Influences"] = [
     "Exacerbates impacts of other stressors"
]
eurasian_steppes["Habitat Fragmentation"]["Logic Description"] = "Fragmentation isolates steppe patches, reducing their ecological viability."
eurasian_steppes["Habitat Fragmentation"]["Impact Function"] = "impact_habitat_fragmentation_eurasian_steppes"

eurasian_steppes["Temperature Increase"]["Metric"] = "Average annual temperature increase (°C) above a pre-industrial baseline."
eurasian_steppes["Temperature Increase"]["Data Sources"] = [
        "Global and regional climate models (GCMs).",
        "Historical temperature records.",
        "IPCC reports."
]
eurasian_steppes["Temperature Increase"]["Impact on Area"] = "Indirect, exacerbates aridity and desertification in some regions"
eurasian_steppes["Temperature Increase"]["Impact on Biodiversity"] = "Increased stress on species, potential shifts in species distributions, and altered phenology."
eurasian_steppes["Temperature Increase"]["Influenced By"] = [
        "Global Greenhouse Gas Emissions"
]
eurasian_steppes["Temperature Increase"]["Influences"] = [
         "Eurasian Steppes - Changes in Precipitation",
        "Eurasian Steppes - Wildfires",
        "Eurasian Steppes - Desertification"
]
eurasian_steppes["Temperature Increase"]["Logic Description"] = "Rising temperatures due to climate change further stress the already arid steppe environment."
eurasian_steppes["Temperature Increase"]["Impact Function"] = "impact_temperature_increase_eurasian_steppes"

eurasian_steppes["Changes in Precipitation"]["Metric"] = "Change in annual precipitation (mm/year) and changes in seasonal distribution."
eurasian_steppes["Changes in Precipitation"]["Data Sources"] = [
   "Global and regional climate models (GCMs).",
        "Historical precipitation records.",
        "IPCC reports."
]
eurasian_steppes["Changes in Precipitation"]["Impact on Area"] = "Indirect; changes in water availability, potentially contributing to desertification."
eurasian_steppes["Changes in Precipitation"]["Impact on Biodiversity"] = "Shifts in species composition; increased drought stress; altered plant productivity."
eurasian_steppes["Changes in Precipitation"]["Influenced By"] = [
    "Global Greenhouse Gas Emissions"
]
eurasian_steppes["Changes in Precipitation"]["Influences"] = [
    "Eurasian Steppes - Wildfires",
   "Eurasian Steppes - Desertification",
  "Eurasian Steppes - Water Availability"
]
eurasian_steppes["Changes in Precipitation"]["Logic Description"] = "Changes in precipitation patterns, combined with rising temperatures, lead to increased aridity and affect the ecosystem."
eurasian_steppes["Changes in Precipitation"]["Impact Function"] = "impact_precipitation_changes_eurasian_steppes"

eurasian_steppes["Overgrazing"]["Metric"] = "Livestock density; vegetation cover and composition; soil erosion."
eurasian_steppes["Overgrazing"]["Data Sources"] = [
     "Agricultural Statistics",
    "Vegetation surveys",
    "Remote sensing"
]
eurasian_steppes["Overgrazing"]["Impact on Area"] = "Changes in vegetation structure; soil degradation."
eurasian_steppes["Overgrazing"]["Impact on Biodiversity"] = "Loss of palatable species; Soil Compaction; Spread of unpalatable plants."
eurasian_steppes["Overgrazing"]["Influenced By"] = [
     "Eurasian Steppes - Livestock Management"
]
eurasian_steppes["Overgrazing"]["Influences"] = [
   "Eurasian Steppes - Vegetation Changes",
  "Eurasian Steppes - Desertification"
]
eurasian_steppes["Overgrazing"]["Logic Description"] = "Overgrazing by livestock is a widespread problem, leading to vegetation degradation and soil erosion."
eurasian_steppes["Overgrazing"]["Impact Function"] = "impact_overgrazing_eurasian_steppes"

eurasian_steppes["Wildfires"]["Metric"] = "Fire frequency; area burned (ha/year)."
eurasian_steppes["Wildfires"]["Data Sources"] = [
   "Remote sensing data.",
   "Government statistics (various countries)."
]
eurasian_steppes["Wildfires"]["Impact on Area"] = "Changes in vegetation structure and composition."
eurasian_steppes["Wildfires"]["Impact on Biodiversity"] = "Can be beneficial for some steppe species if fire regimes are natural, but increased frequency or intensity due to climate change or human activities can be detrimental."
eurasian_steppes["Wildfires"]["Influenced By"] = [
   "Eurasian Steppes - Climate Change",
  "Human activities."
]
eurasian_steppes["Wildfires"]["Influences"] = [
    "Eurasian Steppes - Vegetation Structure."
]
eurasian_steppes["Wildfires"]["Logic Description"] = "Changes in fire regimes, often linked to human activities and climate change, can impact steppe ecosystems."
eurasian_steppes["Wildfires"]["Impact Function"] = "impact_wildfires_eurasian_steppes"

eurasian_steppes["Invasive Species"]["Metric"] = "Distribution and abundance of key invasive species."
eurasian_steppes["Invasive Species"]["Data Sources"] = [
  "Vegetation surveys.",
        "Research studies."
]
eurasian_steppes["Invasive Species"]["Impact on Area"] = "Changes in vegetation composition."
eurasian_steppes["Invasive Species"]["Impact on Biodiversity"] = "Competition; Altered processes"
eurasian_steppes["Invasive Species"]["Influenced By"] = [
     "Eurasian Steppes - Disturbance",
   "Eurasian Steppes - Climate Change"
]
eurasian_steppes["Invasive Species"]["Influences"] = [
         "Eurasian Steppes - Native Communities"
]
eurasian_steppes["Invasive Species"]["Logic Description"] = "Invasive species impact."
eurasian_steppes["Invasive Species"]["Impact Function"] = "impact_invasive_species_eurasian_steppes"

eurasian_steppes["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., heavy metals, pesticides) in soil and water."
eurasian_steppes["Pollution"]["Data Sources"] = [
  "Environmental monitoring data.",
     "Research studies."
]
eurasian_steppes["Pollution"]["Impact on Area"] = "Contamination of soil and water resources."
eurasian_steppes["Pollution"]["Impact on Biodiversity"] = "Toxic effects on plants and animals; bioaccumulation of pollutants."
eurasian_steppes["Pollution"]["Influenced By"] = [
    "Industrial Activities",
     "Mining",
   "Agricultural Runoff"
]
eurasian_steppes["Pollution"]["Influences"] = [
   "Eurasian Steppes - Soil Quality",
    "Eurasian Steppes - Water Quality"
]
eurasian_steppes["Pollution"]["Logic Description"] = "Pollution from industrial activities, mining, and agriculture can contaminate soil and water resources."
eurasian_steppes["Pollution"]["Impact Function"] = "impact_pollution_eurasian_steppes"

# --- South American Pampas ---
pampas = all_stressors_data["South American Pampas"]

pampas["Land-Use Change"]["Metric"] = "Area converted to agriculture (especially soybeans), pasture, or other land uses (ha/year)."
pampas["Land-Use Change"]["Data Sources"] = [
    "Remote sensing data.",
   "Government statistics (Argentina, Brazil, Uruguay).",
  "Research publications."
]
pampas["Land-Use Change"]["Impact on Area"] = "Massive loss of pampas habitat; fragmentation."
pampas["Land-Use Change"]["Impact on Biodiversity"] = "Habitat loss and fragmentation.; Decline of pampas-dependent species."
pampas["Land-Use Change"]["Influenced By"] = [
        "South American Pampas - Agricultural Expansion",
     "South American Pampas - Global Commodity Prices",
      "South American Pampas - Government Policies"
]
pampas["Land-Use Change"]["Influences"] = [
  "South American Pampas - Habitat Fragmentation"
]
pampas["Land-Use Change"]["Logic Description"] = "Conversion of pampas to agriculture (especially soybean cultivation) and pasture is the dominant stressor, leading to massive habitat loss."
pampas["Land-Use Change"]["Impact Function"] = "impact_land_use_change_south_american_pampas"

pampas["Habitat Fragmentation"]["Metric"] = "Patch size distribution; edge density; connectivity indices."
pampas["Habitat Fragmentation"]["Data Sources"] = [
 "Land cover data.",
    "GIS analysis."
]
pampas["Habitat Fragmentation"]["Impact on Area"] = "Remaining pampas exists in small, isolated patches."
pampas["Habitat Fragmentation"]["Impact on Biodiversity"] = "Reduced gene flow.; Increased edge effects.;Limited Dispersal; Increased vulnerability."
pampas["Habitat Fragmentation"]["Influenced By"] = [
    "South American Pampas - Land Use Change"
]
pampas["Habitat Fragmentation"]["Influences"] = [
 "Exacerbates other stressor impacts"
]
pampas["Habitat Fragmentation"]["Logic Description"] = "Fragmentation isolates pampas patches, reducing their ecological viability."
pampas["Habitat Fragmentation"]["Impact Function"] = "impact_habitat_fragmentation_south_american_pampas"

pampas["Climate Change"]["Metric"] = "Temperature increase; changes in precipitation; drought frequency/severity."
pampas["Climate Change"]["Data Sources"] = [
   "Climate models.",
   "Historical records"
]
pampas["Climate Change"]["Impact on Area"] = "Indirect - changes in growing conditions."
pampas["Climate Change"]["Impact on Biodiversity"] = "Shifts in species distributions.; Increased stress.; Changes in phenology."
pampas["Climate Change"]["Influenced By"] = [
  "Global GHG"
]
pampas["Climate Change"]["Influences"] = [
   "South American Pampas - Water Availability"
]
pampas["Climate Change"]["Logic Description"] = "Climate change alters temperature and precipitation patterns."
pampas["Climate Change"]["Impact Function"] = "impact_climate_change_south_american_pampas"


pampas["Overgrazing"]["Metric"] = "Livestock density; vegetation cover and composition."
pampas["Overgrazing"]["Data Sources"] = [
        "Agricultural statistics.",
     "Vegetation Surveys"
]
pampas["Overgrazing"]["Impact on Area"] = "Changes in vegetation structure; soil erosion."
pampas["Overgrazing"]["Impact on Biodiversity"] = "Loss of palatable species; Soil compaction; Spread of invasives."
pampas["Overgrazing"]["Influenced By"] = [
       "South American Pampas - Livestock Management Practices"
]
pampas["Overgrazing"]["Influences"] = [
    "South American Pampas - Vegetation Changes"
]
pampas["Overgrazing"]["Logic Description"] = "Overgrazing by livestock can degrade pampas vegetation."
pampas["Overgrazing"]["Impact Function"] = "impact_overgrazing_south_american_pampas"

pampas["Invasive Species"]["Metric"] = "Abundance/Distribution of key invasive species (e.g., certain grasses)."
pampas["Invasive Species"]["Data Sources"] = [
        "Vegetation surveys.",
        "Research."
]
pampas["Invasive Species"]["Impact on Area"] = "Changes in vegetation composition."
pampas["Invasive Species"]["Impact on Biodiversity"] = "Competition; Altered processes."
pampas["Invasive Species"]["Influenced By"] = [
    "South American Pampas - Disturbance",
     "South American Pampas - Climate Change"
]
pampas["Invasive Species"]["Influences"] = [
      "South American Pampas - Native Plant Communities"
]
pampas["Invasive Species"]["Logic Description"] = "Invasive grasses can outcompete native pampas species."
pampas["Invasive Species"]["Impact Function"] = "impact_invasive_species_south_american_pampas"

pampas["Pollution"]["Metric"] = "Concentrations of pesticides, fertilizers, and other pollutants in soil and water."
pampas["Pollution"]["Data Sources"] = [
      "Water quality monitoring data.",
        "Soil surveys.",
     "Research studies."
]
pampas["Pollution"]["Impact on Area"] = "Degradation of soil and water quality."
pampas["Pollution"]["Impact on Biodiversity"] = "Toxic effects on plants and animals; contamination of food webs."
pampas["Pollution"]["Influenced By"] = [
      "South American Pampas - Agricultural Runoff",
    "South American Pampas - Industrial Activities"
]
pampas["Pollution"]["Influences"] = [
     "South American Pampas - Water Quality",
    "South American Pampas - Soil Quality"
]
pampas["Pollution"]["Logic Description"] = "Pollution from agriculture and other sources can harm soil and water quality."
pampas["Pollution"]["Impact Function"] = "impact_pollution_south_american_pampas"

# --- Australian Grasslands ---
australian_grasslands = all_stressors_data["Australian Grasslands"]

australian_grasslands["Land-Use Change"]["Metric"] = "Area converted to agriculture, pasture, or other land uses (ha/year)."
australian_grasslands["Land-Use Change"]["Data Sources"] = [
    "Remote sensing data.",
    "Australian government data (e.g., Department of Agriculture, Water and the Environment).",
   "Research publications."
]
australian_grasslands["Land-Use Change"]["Impact on Area"] = "Loss of grassland habitat; fragmentation."
australian_grasslands["Land-Use Change"]["Impact on Biodiversity"] = "Habitat loss and fragmentation.; Decline of grassland-dependent species."
australian_grasslands["Land-Use Change"]["Influenced By"] = [
      "Australian Grasslands - Agricultural Expansion",
   "Australian Grasslands - Population Growth",
     "Australian Grasslands - Government Policies"
]
australian_grasslands["Land-Use Change"]["Influences"] = [
  "Australian Grasslands - Habitat Fragmentation"
]
australian_grasslands["Land-Use Change"]["Logic Description"] = "Conversion of grasslands to agriculture and pasture is a major threat."
australian_grasslands["Land-Use Change"]["Impact Function"] = "impact_land_use_change_australian_grasslands"

australian_grasslands["Habitat Fragmentation"]["Metric"] = "Patch size distribution; edge density; connectivity indices."
australian_grasslands["Habitat Fragmentation"]["Data Sources"] = [
    "Land cover data.",
    "GIS analysis."
]
australian_grasslands["Habitat Fragmentation"]["Impact on Area"] = "Remaining grasslands exist in isolated patches."
australian_grasslands["Habitat Fragmentation"]["Impact on Biodiversity"] = "Reduced gene flow.; Increased edge effects.; Limited dispersal; Increased vulnerability"
australian_grasslands["Habitat Fragmentation"]["Influenced By"] = [
    "Australian Grasslands - Land-Use Change"
]
australian_grasslands["Habitat Fragmentation"]["Influences"] = [
 "Exacerbates other stressors"
]
australian_grasslands["Habitat Fragmentation"]["Logic Description"] = "Fragmentation isolates grassland patches."
australian_grasslands["Habitat Fragmentation"]["Impact Function"] = "impact_habitat_fragmentation_australian_grasslands"

australian_grasslands["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality); increased frequency and severity of drought."
australian_grasslands["Climate Change"]["Data Sources"] = [
   "Climate models.",
   "Historical records (Bureau of Meteorology)."
]
australian_grasslands["Climate Change"]["Impact on Area"] = "Indirect; changes in growing conditions."
australian_grasslands["Climate Change"]["Impact on Biodiversity"] = "Shifts in species distributions.; Increased stress on grassland species.; Changes in phenology.; Increased fire risk (in some areas)."
australian_grasslands["Climate Change"]["Influenced By"] = [
 "Global GHG"
]
australian_grasslands["Climate Change"]["Influences"] = [
"Australian Grasslands - Fire Regimes",
"Australian Grasslands - Water Availability"
]
australian_grasslands["Climate Change"]["Logic Description"] = "Climate change is altering temperature and precipitation patterns, increasing aridity and fire risk in many areas."
australian_grasslands["Climate Change"]["Impact Function"] = "impact_climate_change_australian_grasslands"

australian_grasslands["Overgrazing"]["Metric"] = "Livestock density; vegetation cover and composition; soil erosion."
australian_grasslands["Overgrazing"]["Data Sources"] = [
        "Agricultural statistics",
       "Vegetation Surveys",
    "Remote sensing"
]
australian_grasslands["Overgrazing"]["Impact on Area"] = "Changes in vegetation; soil degradation."
australian_grasslands["Overgrazing"]["Impact on Biodiversity"] = "Loss of palatable species; Spread of unpalatable species and weeds.; Soil compaction and erosion.; Competition with native herbivores."
australian_grasslands["Overgrazing"]["Influenced By"] = [
  "Australian Grasslands - Livestock Management",
  "Australian Grasslands - Feral Herbivores"
]
australian_grasslands["Overgrazing"]["Influences"] = [
 "Australian Grasslands - Vegetation Structure",
    "Desertification"
]
australian_grasslands["Overgrazing"]["Logic Description"] = "Overgrazing by livestock and feral herbivores is a widespread problem, leading to vegetation degradation and soil erosion."
australian_grasslands["Overgrazing"]["Impact Function"] = "impact_overgrazing_australian_grasslands"

australian_grasslands["Wildfires"]["Metric"] = "Fire frequency; area burned (ha/year); fire intensity."
australian_grasslands["Wildfires"]["Data Sources"] = [
   "Remote sensing data.",
  "Government fire agency data."
]
australian_grasslands["Wildfires"]["Impact on Area"] = "Changes in vegetation structure and composition."
australian_grasslands["Wildfires"]["Impact on Biodiversity"] = "Can be beneficial or detrimental, depending on fire regime. Many Australian grassland species are adapted to fire, but changes in fire frequency or intensity can have negative impacts."
australian_grasslands["Wildfires"]["Influenced By"] = [
  "Australian Grasslands - Climate Change",
 "Australian Grasslands - Land Management Practices",
     "Australian Grasslands - Human Activities"
]
australian_grasslands["Wildfires"]["Influences"] = [
   "Australian Grasslands - Vegetation Structure"
]
australian_grasslands["Wildfires"]["Logic Description"] = "Changes in fire regimes, often linked to climate change and land management, can impact grassland ecosystems."
australian_grasslands["Wildfires"]["Impact Function"] = "impact_wildfires_australian_grasslands"

australian_grasslands["Invasive Species"]["Metric"] = "Abundance/Distribution, e.g., Buffel grass"
australian_grasslands["Invasive Species"]["Data Sources"] = [
     "Vegetation surveys",
     "Research"
]
australian_grasslands["Invasive Species"]["Impact on Area"] = "Vegetation changes."
australian_grasslands["Invasive Species"]["Impact on Biodiversity"] = "Competition; Altered fire regimes (some invasives increase fire intensity)."
australian_grasslands["Invasive Species"]["Influenced By"] = [
    "Australian Grasslands - Disturbance",
   "Australian Grasslands - Climate Change"
]
australian_grasslands["Invasive Species"]["Influences"] = [
     "Australian Grasslands - Native Plant Communities",
   "Australian Grasslands - Fire Regimes"
]
australian_grasslands["Invasive Species"]["Logic Description"] = "Invasive species, particularly some grasses (e.g., buffel grass), can outcompete native plants and alter fire regimes."
australian_grasslands["Invasive Species"]["Impact Function"] = "impact_invasive_species_australian_grasslands"

australian_grasslands["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., pesticides, heavy metals) in soil and water."
australian_grasslands["Pollution"]["Data Sources"] = [
    "Environmental monitoring data (limited in many areas).",
   "Research studies."
]
australian_grasslands["Pollution"]["Impact on Area"] = "Degradation of soil and water quality."
australian_grasslands["Pollution"]["Impact on Biodiversity"] = "Toxic effects on plants and animals."
australian_grasslands["Pollution"]["Influenced By"] = [
    "Agricultural Runoff",
 "Mining Activities (in some areas)",
 "Industrial Activities (in some areas)"
]
australian_grasslands["Pollution"]["Influences"] = [
   "Australian Grasslands - Soil Quality",
  "Australian Grasslands - Water Quality"
]
australian_grasslands["Pollution"]["Logic Description"] = "Pollution from agriculture, mining, and industry can impact soil and water quality."
australian_grasslands["Pollution"]["Impact Function"] = "impact_pollution_australian_grasslands"

# --- South American Cerrado ---
cerrado = all_stressors_data["South American Cerrado"]

cerrado["Deforestation"]["Metric"] = "Area of Cerrado converted to other land uses (ha/year), primarily for agriculture."
cerrado["Deforestation"]["Data Sources"] = [
        "Brazilian Institute of Geography and Statistics (IBGE)",
        "Brazilian National Institute for Space Research (INPE) - PRODES and DETER Cerrado",
        "Remote sensing data (Landsat, Sentinel, etc.)",
        "Research publications and reports from NGOs"
]
cerrado["Deforestation"]["Impact on Area"] = "Direct loss of Cerrado habitat, a highly biodiverse savanna ecosystem."
cerrado["Deforestation"]["Impact on Biodiversity"] = "Habitat loss and fragmentation, threatening many endemic species. Loss of carbon storage and disruption of ecosystem services."
cerrado["Deforestation"]["Influenced By"] = [
       "Cerrado - Agricultural Expansion (soybeans, cattle ranching)",
        "Global Commodity Prices (soy, beef)",
        "Government Policies (agricultural subsidies, infrastructure projects)",
        "Economic Growth",
        "Land Speculation"
]
cerrado["Deforestation"]["Influences"] = [
     "Cerrado - Habitat Fragmentation",
     "Cerrado - Wildfires",
      "Cerrado - Water Quality (increased sedimentation and runoff)"
]
cerrado["Deforestation"]["Logic Description"] = "Deforestation in the Cerrado is primarily driven by the expansion of large-scale agriculture, particularly for soybeans and cattle ranching. This conversion represents the largest threat to this biome."
cerrado["Deforestation"]["Impact Function"] = "impact_deforestation_cerrado"

cerrado["Land-Use Change"]["Metric"] = "Area converted to agriculture, pasture, or other land uses (ha/year)."
cerrado["Land-Use Change"]["Data Sources"] = [
   "Remote sensing data.",
  "Brazilian government statistics (IBGE).",
  "Research publications."
]
cerrado["Land-Use Change"]["Impact on Area"] = "Loss of Cerrado habitat; fragmentation."
cerrado["Land-Use Change"]["Impact on Biodiversity"] = "Habitat loss and fragmentation.; Decline of Cerrado-dependent species."
cerrado["Land-Use Change"]["Influenced By"] = [
  "Cerrado - Agricultural Expansion",
   "Cerrado - Government Policies",
  "Global Commodity Prices",
   "Infrastructure Development"
]
cerrado["Land-Use Change"]["Influences"] = [
    "Cerrado - Habitat Fragmentation"
]
cerrado["Land-Use Change"]["Logic Description"] = "Conversion of Cerrado to agriculture (soybeans, cattle) and pasture is the dominant stressor."
cerrado["Land-Use Change"]["Impact Function"] = "impact_land_use_change_cerrado"

cerrado["Habitat Fragmentation"]["Impact Function"] = "impact_habitat_fragmentation_cerrado" # Needs Metric, Data, etc.

cerrado["Temperature Increase"]["Metric"] = "Average annual temperature increase (°C)."
cerrado["Temperature Increase"]["Data Sources"] = [
   "Global and regional climate models.",
   "Historical weather records."
]
cerrado["Temperature Increase"]["Impact on Area"] = "Indirect; exacerbates other stressors, like fire."
cerrado["Temperature Increase"]["Impact on Biodiversity"] = "Increased stress on Cerrado species; shifts in species distributions; changes in phenology."
cerrado["Temperature Increase"]["Influenced By"] = [
     "Global Greenhouse Gas Emissions"
]
cerrado["Temperature Increase"]["Influences"] = [
    "Cerrado - Wildfires",
  "Cerrado - Changes in Precipitation"
]
cerrado["Temperature Increase"]["Logic Description"] = "Climate change is increasing temperatures in the Cerrado, exacerbating drought and fire risk."
cerrado["Temperature Increase"]["Impact Function"] = "impact_temperature_increase_cerrado"

cerrado["Changes in Precipitation"]["Metric"] = "Change in annual precipitation (mm/year); changes in dry season length and intensity."
cerrado["Changes in Precipitation"]["Data Sources"] = [
  "Climate models.",
    "Historical weather records."
]
cerrado["Changes in Precipitation"]["Impact on Area"] = "Indirect; changes in water availability."
cerrado["Changes in Precipitation"]["Impact on Biodiversity"] = "Increased drought stress; shifts in species composition; impacts on wetlands."
cerrado["Changes in Precipitation"]["Influenced By"] = [
 "Global Greenhouse Gas Emissions"
]
cerrado["Changes in Precipitation"]["Influences"] = [
  "Cerrado - Wildfires",
    "Cerrado - Water Availability"
]
cerrado["Changes in Precipitation"]["Logic Description"] = "Climate change is altering rainfall patterns, increasing drought risk and impacting water resources."
cerrado["Changes in Precipitation"]["Impact Function"] = "impact_precipitation_changes_cerrado"

cerrado["Wildfires"]["Metric"] = "Number of wildfires per year; total area burned (ha/year); fire intensity."
cerrado["Wildfires"]["Data Sources"] = [
    "Remote sensing data (fire detection).",
   "INPE fire monitoring data.",
    "Research publications."
]
cerrado["Wildfires"]["Impact on Area"] = "Direct loss of vegetation; changes in vegetation structure; increased soil erosion."
cerrado["Wildfires"]["Impact on Biodiversity"] = "Mortality of plants and animals; habitat loss; can favor fire-adapted species, but increased frequency and intensity can be detrimental."
cerrado["Wildfires"]["Influenced By"] = [
   "Cerrado - Climate Change",
   "Cerrado - Deforestation",
   "Human Activities (accidental and intentional fires)"
]
cerrado["Wildfires"]["Influences"] = [
  "Cerrado - Air Quality",
  "Cerrado - Soil Erosion",
  "Cerrado - Vegetation Structure"
]
cerrado["Wildfires"]["Logic Description"] = "Wildfires are a natural part of the Cerrado ecosystem, but increased frequency and intensity due to climate change, deforestation, and human activities are a major threat."
cerrado["Wildfires"]["Impact Function"] = "impact_wildfires_cerrado"

cerrado["Overgrazing"]["Metric"] = "Livestock density; vegetation cover and composition."
cerrado["Overgrazing"]["Data Sources"] = [
    "Agricultural statistics.",
    "Vegetation surveys."
]
cerrado["Overgrazing"]["Impact on Area"] = "Changes in vegetation structure; soil degradation."
cerrado["Overgrazing"]["Impact on Biodiversity"] = "Loss of palatable plant species.; Soil compaction and erosion."
cerrado["Overgrazing"]["Influenced By"] = [
   "Cerrado - Livestock Management Practices"
]
cerrado["Overgrazing"]["Influences"] = [
  "Cerrado - Vegetation Changes"
]
cerrado["Overgrazing"]["Logic Description"] = "Overgrazing by cattle can degrade Cerrado vegetation and contribute to soil erosion."
cerrado["Overgrazing"]["Impact Function"] = "impact_overgrazing_cerrado"

cerrado["Invasive Species"]["Metric"] = "Abundance and distribution of invasive plant species (e.g., African grasses)."
cerrado["Invasive Species"]["Data Sources"] = [
   "Vegetation surveys.",
   "Research studies."
]
cerrado["Invasive Species"]["Impact on Area"] = "Changes in vegetation composition; increased fire risk (some invasive grasses)."
cerrado["Invasive Species"]["Impact on Biodiversity"] = "Competition with native Cerrado plants; altered fire regimes."
cerrado["Invasive Species"]["Influenced By"] = [
  "Cerrado - Disturbance",
   "Cerrado - Climate Change",
  "Introduction (often for pasture improvement)"
]
cerrado["Invasive Species"]["Influences"] = [
 "Cerrado - Native Plant Communities",
     "Cerrado - Fire Regimes"
]
cerrado["Invasive Species"]["Logic Description"] = "Invasive grasses, often introduced for pasture improvement, can outcompete native Cerrado vegetation and increase fire risk."
cerrado["Invasive Species"]["Impact Function"] = "impact_invasive_species_cerrado"

cerrado["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., pesticides, fertilizers, sediment) in water and soil."
cerrado["Pollution"]["Data Sources"] = [
   "Water quality monitoring data.",
    "Soil surveys.",
   "Research studies."
]
cerrado["Pollution"]["Impact on Area"] = "Degradation of water and soil quality."
cerrado["Pollution"]["Impact on Biodiversity"] = "Toxic effects on plants and animals; impacts on aquatic ecosystems."
cerrado["Pollution"]["Influenced By"] = [
   "Cerrado - Agricultural Runoff",
   "Mining Activities"
]
cerrado["Pollution"]["Influences"] = [
   "Cerrado - Water Quality",
   "Cerrado - Soil Quality"
]
cerrado["Pollution"]["Logic Description"] = "Pollution from agriculture (pesticides, fertilizers) and mining activities can contaminate water and soil resources."
cerrado["Pollution"]["Impact Function"] = "impact_pollution_cerrado"

cerrado["Agricultural Expansion"]["Impact Function"] = "impact_agricultural_expansion_cerrado"
cerrado["Government Policies"]["Impact Function"] = "impact_government_policies_cerrado"
cerrado["Infrastructure Development"]["Impact Function"] = "impact_infrastructure_development_cerrado"

# --- Temperate Forests (Appalachian) ---
temperate_forests_appalachian = all_stressors_data["Appalachian Temperate Forests"]

temperate_forests_appalachian["Land-Use Change"]["Metric"] = "Area converted to agriculture, urban development, or other land uses (ha/year)."
temperate_forests_appalachian["Land-Use Change"]["Data Sources"] = [
    "USGS National Land Cover Database (NLCD).",
    "Forest Inventory and Analysis (FIA) data.",
    "Local and regional land-use planning documents."
]
temperate_forests_appalachian["Land-Use Change"]["Impact on Area"] = "Historical deforestation and ongoing conversion for development and agriculture."
temperate_forests_appalachian["Land-Use Change"]["Impact on Biodiversity"] = "Habitat loss and fragmentation. Decline of forest-dependent species."
temperate_forests_appalachian["Land-Use Change"]["Influenced By"] = [
    "Temperate Forests (Appalachian) - Forestry Practices",
    "Temperate Forests (Appalachian) - Mining",
    "Urban Sprawl",
    "Agricultural Expansion"
]
temperate_forests_appalachian["Land-Use Change"]["Influences"] = [
    "Temperate Forests (Appalachian) - Habitat Fragmentation"
]
temperate_forests_appalachian["Land-Use Change"]["Logic Description"] = "Land-use change, primarily from historical logging, agriculture, and ongoing development, is a major driver of habitat loss and fragmentation in the Appalachian region."
temperate_forests_appalachian["Land-Use Change"]["Impact Function"] = "impact_land_use_change_appalachian"

temperate_forests_appalachian["Habitat Fragmentation"]["Metric"] = "Patch size distribution; edge density; connectivity indices."
temperate_forests_appalachian["Habitat Fragmentation"]["Data Sources"] = [
    "Land cover data (from remote sensing and other sources).",
    "GIS analysis."
]
temperate_forests_appalachian["Habitat Fragmentation"]["Impact on Area"] = "Forests exist in a mosaic of patches, often separated by roads, fields, and development."
temperate_forests_appalachian["Habitat Fragmentation"]["Impact on Biodiversity"] = "Reduced gene flow; increased edge effects; limited dispersal ability; increased vulnerability to stochastic events."
temperate_forests_appalachian["Habitat Fragmentation"]["Influenced By"] = [
    "Temperate Forests (Appalachian) - Land-Use Change",
    "Temperate Forests (Appalachian) - Forestry Practices",
    "Infrastructure Development"
]
temperate_forests_appalachian["Habitat Fragmentation"]["Influences"] = [
    "Exacerbates impacts of other stressors."
]
temperate_forests_appalachian["Habitat Fragmentation"]["Logic Description"] = "Fragmentation isolates forest patches, reducing habitat quality and connectivity for many species."
temperate_forests_appalachian["Habitat Fragmentation"]["Impact Function"] = "impact_habitat_fragmentation_appalachian"

temperate_forests_appalachian["Invasive Species"]["Metric"] = "Abundance and distribution of key invasive species (e.g., hemlock woolly adelgid, gypsy moth, emerald ash borer)."
temperate_forests_appalachian["Invasive Species"]["Data Sources"] = [
    "Forest health monitoring programs.",
    "Research studies.",
    "Land management agency data."
]
temperate_forests_appalachian["Invasive Species"]["Impact on Area"] = "Changes in forest composition and structure; tree mortality."
temperate_forests_appalachian["Invasive Species"]["Impact on Biodiversity"] = "Loss of key tree species (e.g., hemlock, ash); cascading effects on other species that depend on those trees."
temperate_forests_appalachian["Invasive Species"]["Influenced By"] = [
    "Global Trade",
    "Climate Change",
     "Temperate Forests (Appalachian) - Disturbance",
    "Temperate Forests (Appalachian) - Introduction"
]
temperate_forests_appalachian["Invasive Species"]["Influences"] = [
    "Alters ecosystem processes."
]
temperate_forests_appalachian["Invasive Species"]["Logic Description"] = "Invasive insects and pathogens are causing widespread tree mortality and altering forest composition."
temperate_forests_appalachian["Invasive Species"]["Impact Function"] = "impact_invasive_species_appalachian"

temperate_forests_appalachian["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality); changes in growing season length."
temperate_forests_appalachian["Climate Change"]["Data Sources"] = ["Climate models; historical climate records."]
temperate_forests_appalachian["Climate Change"]["Impact on Area"] = "Indirect; changes in growing conditions, species distributions."
temperate_forests_appalachian["Climate Change"]["Impact on Biodiversity"] = "Shifts in species ranges; increased stress on some species; changes in phenology; increased fire risk in some areas."
temperate_forests_appalachian["Climate Change"]["Influenced By"] = ["Global GHG"]
temperate_forests_appalachian["Climate Change"]["Influences"] = ["Temperate Forests (Appalachian) - Invasive Species", "Temperate Forests (Appalachian) - Fire Regimes"]
temperate_forests_appalachian["Climate Change"]["Logic Description"] = "Climate change is altering temperature and precipitation patterns, potentially leading to shifts in species distributions and increased stress on forest ecosystems."
temperate_forests_appalachian["Climate Change"]["Impact Function"] = "impact_climate_change_appalachian"

temperate_forests_appalachian["Air Pollution"]["Metric"] = "Concentrations of ozone, nitrogen oxides (NOx), and sulfur dioxide (SO2)."
temperate_forests_appalachian["Air Pollution"]["Data Sources"] = [
    "EPA Air Quality System (AQS).",
    "National Atmospheric Deposition Program (NADP)."
]
temperate_forests_appalachian["Air Pollution"]["Impact on Area"] = "Reduced tree growth; increased susceptibility to other stressors."
temperate_forests_appalachian["Air Pollution"]["Impact on Biodiversity"] = "Damage to sensitive plant species; changes in forest composition."
temperate_forests_appalachian["Air Pollution"]["Influenced By"] = [
    "Industrial Emissions",
    "Vehicle Emissions",
    "Power Generation"
]
temperate_forests_appalachian["Air Pollution"]["Influences"] = [
    "Temperate Forests (Appalachian) - Acid Deposition"
]
temperate_forests_appalachian["Air Pollution"]["Logic Description"] = "Air pollution, particularly ozone and acid deposition, can damage trees and alter forest ecosystem processes."
temperate_forests_appalachian["Air Pollution"]["Impact Function"] = "impact_air_pollution_appalachian"

temperate_forests_appalachian["Overbrowsing (Deer)"]["Metric"] = "Deer density (deer/km²); browsing intensity on key plant species."
temperate_forests_appalachian["Overbrowsing (Deer)"]["Data Sources"] = [
    "Deer population surveys.",
    "Vegetation surveys (measuring browse impacts)."
]
temperate_forests_appalachian["Overbrowsing (Deer)"]["Impact on Area"] = "Changes in forest understory composition; reduced tree regeneration."
temperate_forests_appalachian["Overbrowsing (Deer)"]["Impact on Biodiversity"] = "Decline of palatable plant species; loss of understory habitat for other animals."
temperate_forests_appalachian["Overbrowsing (Deer)"]["Influenced By"] = [
    "Predator Management (or lack thereof)",
     "Temperate Forests (Appalachian) - Forest Management",
    "Habitat Fragmentation"
]
temperate_forests_appalachian["Overbrowsing (Deer)"]["Influences"] = [
    "Temperate Forests (Appalachian) - Forest Regeneration"
]
temperate_forests_appalachian["Overbrowsing (Deer)"]["Logic Description"] = "High deer populations, often due to the absence of predators and fragmented habitat, can lead to overbrowsing, which suppresses forest regeneration and alters understory plant communities."
temperate_forests_appalachian["Overbrowsing (Deer)"]["Impact Function"] = "impact_overbrowsing_deer_appalachian"

temperate_forests_appalachian["Forestry Practices"]["Metric"] = "Area harvested (ha/year); type of harvesting method (e.g., clearcutting, selective logging)."
temperate_forests_appalachian["Forestry Practices"]["Data Sources"] = [
    "Forest Inventory and Analysis (FIA) data.",
    "State forestry agency data.",
    "Timber harvest permits."
]
temperate_forests_appalachian["Forestry Practices"]["Impact on Area"] = "Changes in forest age structure, composition, and habitat."
temperate_forests_appalachian["Forestry Practices"]["Impact on Biodiversity"] = "Varies depending on practices; can create early successional habitat but also fragment forests and reduce habitat for old-growth dependent species."
temperate_forests_appalachian["Forestry Practices"]["Influenced By"] = [
    "Economic Demand for Timber",
    "Forest Management Policies"
]
temperate_forests_appalachian["Forestry Practices"]["Influences"] = [
    "Temperate Forests (Appalachian) - Habitat Fragmentation",
     "Temperate Forests (Appalachian) - Land-Use Change"
]
temperate_forests_appalachian["Forestry Practices"]["Logic Description"] = "Forestry practices, while providing timber resources, can significantly alter forest structure and composition, impacting biodiversity."
temperate_forests_appalachian["Forestry Practices"]["Impact Function"] = "impact_forestry_practices_appalachian"

temperate_forests_appalachian["Mining"]["Metric"] = "Area disturbed by mining activities (ha/year); water quality parameters in affected streams."
temperate_forests_appalachian["Mining"]["Data Sources"] = [
    "Mining permits and reclamation records.",
    "Water quality monitoring data."
]
temperate_forests_appalachian["Mining"]["Impact on Area"] = "Direct habitat loss; water pollution; soil contamination."
temperate_forests_appalachian["Mining"]["Impact on Biodiversity"] = "Loss of habitat; impacts on aquatic species from water pollution; fragmentation."
temperate_forests_appalachian["Mining"]["Influenced By"] = [
        "Resource Extraction",
        "Government Regulation (or lack thereof)"
]
temperate_forests_appalachian["Mining"]["Influences"] = [
        "Temperate Forests (Appalachian) - Water Pollution",
        "Temperate Forests (Appalachian) - Land-Use Change"

]
temperate_forests_appalachian["Mining"]["Logic Description"] = "Mining activities, particularly coal mining, can cause significant habitat destruction and water pollution in the Appalachian region."
temperate_forests_appalachian["Mining"]["Impact Function"] = "impact_mining_appalachian"

temperate_forests_appalachian["Acid Deposition"]["Metric"] = "pH of precipitation and streamwater; levels of sulfate and nitrate deposition."
temperate_forests_appalachian["Acid Deposition"]["Data Sources"] = [
    "National Atmospheric Deposition Program (NADP).",
    "USGS water quality data."
]
temperate_forests_appalachian["Acid Deposition"]["Impact on Area"] = "Soil acidification; nutrient imbalances; damage to trees."
temperate_forests_appalachian["Acid Deposition"]["Impact on Biodiversity"] = "Decline of acid-sensitive tree species (e.g., red spruce); impacts on aquatic ecosystems."
temperate_forests_appalachian["Acid Deposition"]["Influenced By"] = [
    "Temperate Forests (Appalachian) - Air Pollution"
]
temperate_forests_appalachian["Acid Deposition"]["Influences"] = [
    "Temperate Forests (Appalachian) - Water Quality",
    "Temperate Forests (Appalachian) - Soil Chemistry"
]
temperate_forests_appalachian["Acid Deposition"]["Logic Description"] = "Acid deposition, primarily from air pollution, can acidify soils and water bodies, harming sensitive species and altering ecosystem processes."
temperate_forests_appalachian["Acid Deposition"]["Impact Function"] = "impact_acid_deposition_appalachian"

# --- Temperate Forests (Chilean) ---
temperate_forests_chilean = all_stressors_data["Chilean Temperate Forests"]

temperate_forests_chilean["Land-Use Change"]["Metric"] = "Area converted to plantations, agriculture, or other land uses (ha/year)."
temperate_forests_chilean["Land-Use Change"]["Data Sources"] = [
    "CONAF (Corporación Nacional Forestal - Chilean Forest Service).",
    "Instituto Forestal (INFOR) - Chilean Forest Institute.",
    "Remote sensing data (Landsat, Sentinel, etc.).",
    "Research publications."
]
temperate_forests_chilean["Land-Use Change"]["Impact on Area"] = "Significant loss of native forest area, particularly in the lowlands."
temperate_forests_chilean["Land-Use Change"]["Impact on Biodiversity"] = "Habitat loss and fragmentation, threatening many endemic species.  Loss of old-growth forests."
temperate_forests_chilean["Land-Use Change"]["Influenced By"] = [
    "Temperate Forests (Chilean) - Forestry Practices",
    "Agricultural Expansion",
    "Urbanization"
]
temperate_forests_chilean["Land-Use Change"]["Influences"] = [
    "Temperate Forests (Chilean) - Habitat Fragmentation"
]
temperate_forests_chilean["Land-Use Change"]["Logic Description"] = "Conversion of native forests to exotic tree plantations (pine and eucalyptus) and agriculture is a major driver of habitat loss."
temperate_forests_chilean["Land-Use Change"]["Impact Function"] = "impact_land_use_change_chilean"

temperate_forests_chilean["Habitat Fragmentation"]["Metric"] = "Patch size distribution; edge density; connectivity indices."
temperate_forests_chilean["Habitat Fragmentation"]["Data Sources"] = [
    "Land cover data (from remote sensing and other sources).",
    "GIS analysis."
]
temperate_forests_chilean["Habitat Fragmentation"]["Impact on Area"] = "Remaining native forests are increasingly fragmented, particularly in the lowlands."
temperate_forests_chilean["Habitat Fragmentation"]["Impact on Biodiversity"] = "Reduced gene flow; increased edge effects; limited dispersal ability; increased vulnerability to stochastic events."
temperate_forests_chilean["Habitat Fragmentation"]["Influenced By"] = [
    "Temperate Forests (Chilean) - Land-Use Change",
    "Temperate Forests (Chilean) - Forestry Practices",
    "Infrastructure Development"
]
temperate_forests_chilean["Habitat Fragmentation"]["Influences"] = [
    "Exacerbates impacts of other stressors."
]
temperate_forests_chilean["Habitat Fragmentation"]["Logic Description"] = "Fragmentation isolates forest patches, reducing habitat quality and connectivity for many species, especially those with limited dispersal capabilities."
temperate_forests_chilean["Habitat Fragmentation"]["Impact Function"] = "impact_habitat_fragmentation_chilean"

temperate_forests_chilean["Invasive Species"]["Metric"] = "Abundance and distribution of key invasive species (e.g., *Ulex europaeus* (gorse), *Rubus constrictus* (blackberry))."
temperate_forests_chilean["Invasive Species"]["Data Sources"] = [
    "Vegetation surveys.",
    "Research studies.",
    "CONAF data."
]
temperate_forests_chilean["Invasive Species"]["Impact on Area"] = "Changes in vegetation composition and structure; altered fire regimes."
temperate_forests_chilean["Invasive Species"]["Impact on Biodiversity"] = "Competition with native plants; altered habitat structure; reduced resources for native fauna."
temperate_forests_chilean["Invasive Species"]["Influenced By"] = [
   "Temperate Forests (Chilean) - Disturbance",
    "Temperate Forests (Chilean) - Climate Change",
    "Temperate Forests (Chilean) - Introduction"
]
temperate_forests_chilean["Invasive Species"]["Influences"] = [
    "Temperate Forests (Chilean) - Fire Regimes"
]
temperate_forests_chilean["Invasive Species"]["Logic Description"] = "Invasive plants can outcompete native species and alter ecosystem processes, including fire regimes."
temperate_forests_chilean["Invasive Species"]["Impact Function"] = "impact_invasive_species_chilean"

temperate_forests_chilean["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality); changes in snowpack."
temperate_forests_chilean["Climate Change"]["Data Sources"] = ["Climate models; historical climate records; Dirección Meteorológica de Chile."]
temperate_forests_chilean["Climate Change"]["Impact on Area"] = "Indirect; changes in growing conditions, species distributions, fire risk."
temperate_forests_chilean["Climate Change"]["Impact on Biodiversity"] = "Shifts in species ranges (especially elevational shifts); increased stress on some species; increased fire risk."
temperate_forests_chilean["Climate Change"]["Influenced By"] = ["Global GHG"]
temperate_forests_chilean["Climate Change"]["Influences"] = ["Temperate Forests (Chilean) - Fire Regimes", "Temperate Forests (Chilean) - Water Availability"]
temperate_forests_chilean["Climate Change"]["Logic Description"] = "Climate change is projected to lead to warmer temperatures, altered precipitation patterns, and increased fire risk, potentially impacting forest composition and biodiversity."
temperate_forests_chilean["Climate Change"]["Impact Function"] = "impact_climate_change_chilean"

temperate_forests_chilean["Forestry Practices"]["Metric"] = "Area of native forest converted to plantations (ha/year); area of native forest harvested (ha/year); type of harvesting method."
temperate_forests_chilean["Forestry Practices"]["Data Sources"] = [
    "CONAF data.",
    "INFOR data.",
    "Forest certification data (e.g., FSC).",
     "Remote sensing"
]
temperate_forests_chilean["Forestry Practices"]["Impact on Area"] = "Significant loss of native forest area; changes in forest structure and composition."
temperate_forests_chilean["Forestry Practices"]["Impact on Biodiversity"] = "Loss of old-growth forests and associated species; reduced habitat diversity; increased fragmentation."
temperate_forests_chilean["Forestry Practices"]["Influenced By"] = [
    "Global Demand for Pulp and Paper",
    "Economic Incentives",
    "Government Policies"
]
temperate_forests_chilean["Forestry Practices"]["Influences"] = [
    "Temperate Forests (Chilean) - Land-Use Change",
    "Temperate Forests (Chilean) - Habitat Fragmentation",
    "Temperate Forests (Chilean) - Introduced Species (Mammals)"
]
temperate_forests_chilean["Forestry Practices"]["Logic Description"] = "The replacement of native forests with fast-growing exotic tree plantations is a major driver of habitat loss and fragmentation."
temperate_forests_chilean["Forestry Practices"]["Impact Function"] = "impact_forestry_practices_chilean"

temperate_forests_chilean["Introduced Species (Mammals)"]["Metric"] = "Population densities of introduced mammals (e.g., deer, wild boar, mink)."
temperate_forests_chilean["Introduced Species (Mammals)"]["Data Sources"] = [
    "Hunting records.",
    "Research studies (e.g., camera trapping, scat surveys).",
    "SAG (Servicio Agrícola y Ganadero - Chilean Agriculture and Livestock Service) data."
]
temperate_forests_chilean["Introduced Species (Mammals)"]["Impact on Area"] = "Changes in forest understory; altered seed dispersal and predation patterns."
temperate_forests_chilean["Introduced Species (Mammals)"]["Impact on Biodiversity"] = "Browsing pressure on native plants; predation on native fauna; competition with native herbivores."
temperate_forests_chilean["Introduced Species (Mammals)"]["Influenced By"] = [
    "Introduction (Intentional and Accidental)",
    "Lack of Natural Predators"
]
temperate_forests_chilean["Introduced Species (Mammals)"]["Influences"] = [
 "Temperate Forests (Chilean) - Vegetation Changes"
]
temperate_forests_chilean["Introduced Species (Mammals)"]["Logic Description"] = "Introduced mammals, such as deer and wild boar, can have significant impacts on forest regeneration and understory plant communities."
temperate_forests_chilean["Introduced Species (Mammals)"]["Impact Function"] = "impact_introduced_mammals_chilean"

temperate_forests_chilean["Fire Regimes"]["Metric"] = "Fire frequency (return interval - years); fire intensity; area burned (ha/year)."
temperate_forests_chilean["Fire Regimes"]["Data Sources"] = [
   "CONAF fire statistics.",
    "Remote sensing data.",
    "Research studies."
]
temperate_forests_chilean["Fire Regimes"]["Impact on Area"] = "Changes in vegetation structure and composition; increased dominance of fire-adapted species."
temperate_forests_chilean["Fire Regimes"]["Impact on Biodiversity"] = "Loss of fire-sensitive species; changes in habitat structure."
temperate_forests_chilean["Fire Regimes"]["Influenced By"] = [
   "Temperate Forests (Chilean) - Climate Change",
    "Temperate Forests (Chilean) - Land-Use Change",
    "Temperate Forests (Chilean) - Invasive Species",
   "Human Ignitions"
]
temperate_forests_chilean["Fire Regimes"]["Influences"] = [
 "Temperate Forests (Chilean) - Vegetation Changes"
]
temperate_forests_chilean["Fire Regimes"]["Logic Description"] = "Changes in fire regimes, often driven by climate change, land use, and invasive species, can alter forest composition and structure."
temperate_forests_chilean["Fire Regimes"]["Impact Function"] = "impact_fire_regimes_chilean"

# --- Temperate Forests (East Asian) ---
temperate_forests_east_asian = all_stressors_data["East Asian Temperate Forests"]

temperate_forests_east_asian["Land-Use Change"]["Metric"] = "Area converted to agriculture, urban development, or other land uses (ha/year)."
temperate_forests_east_asian["Land-Use Change"]["Data Sources"] = [
    "National Forest Inventories (for specific countries, e.g., China's National Forest Inventory).",
    "Remote sensing data (Landsat, Sentinel, etc.).",
    "Land-use planning documents.",
    "Research publications."
]
temperate_forests_east_asian["Land-Use Change"]["Impact on Area"] = "Significant historical deforestation and ongoing conversion, particularly in densely populated areas."
temperate_forests_east_asian["Land-Use Change"]["Impact on Biodiversity"] = "Habitat loss and fragmentation, threatening many endemic species. Loss of old-growth forests."
temperate_forests_east_asian["Land-Use Change"]["Influenced By"] = [
    "Agricultural Expansion",
    "Urbanization",
    "Infrastructure Development",
    "Temperate Forests (East Asian) - Forestry Practices"
]
temperate_forests_east_asian["Land-Use Change"]["Influences"] = [
    "Temperate Forests (East Asian) - Habitat Fragmentation"
]
temperate_forests_east_asian["Land-Use Change"]["Logic Description"] = "Land-use change, driven by agriculture, urbanization, and infrastructure development, is a major threat to East Asian temperate forests."
temperate_forests_east_asian["Land-Use Change"]["Impact Function"] = "impact_land_use_change_east_asian"

temperate_forests_east_asian["Habitat Fragmentation"]["Metric"] = "Patch size distribution; edge density; connectivity indices."
temperate_forests_east_asian["Habitat Fragmentation"]["Data Sources"] = [
    "Land cover data (from remote sensing and other sources).",
    "GIS analysis."
]
temperate_forests_east_asian["Habitat Fragmentation"]["Impact on Area"] = "Remaining forests are often highly fragmented, particularly in densely populated regions."
temperate_forests_east_asian["Habitat Fragmentation"]["Impact on Biodiversity"] = "Reduced gene flow; increased edge effects; limited dispersal ability; increased vulnerability to stochastic events."
temperate_forests_east_asian["Habitat Fragmentation"]["Influenced By"] = [
    "Temperate Forests (East Asian) - Land-Use Change",
    "Infrastructure Development"
]
temperate_forests_east_asian["Habitat Fragmentation"]["Influences"] = [
    "Exacerbates impacts of other stressors."
]
temperate_forests_east_asian["Habitat Fragmentation"]["Logic Description"] = "Fragmentation isolates forest patches, reducing habitat quality and connectivity, especially for species with limited dispersal ability."
temperate_forests_east_asian["Habitat Fragmentation"]["Impact Function"] = "impact_habitat_fragmentation_east_asian"

temperate_forests_east_asian["Invasive Species"]["Metric"] = "Abundance and distribution of key invasive species (e.g., *Fallopia japonica* (Japanese knotweed), *Ailanthus altissima* (tree-of-heaven))."
temperate_forests_east_asian["Invasive Species"]["Data Sources"] = [
    "Vegetation surveys.",
    "Research studies.",
    "Government agency reports (e.g., invasive species databases)."
]
temperate_forests_east_asian["Invasive Species"]["Impact on Area"] = "Changes in vegetation composition and structure; altered disturbance regimes."
temperate_forests_east_asian["Invasive Species"]["Impact on Biodiversity"] = "Competition with native plants; altered habitat structure; reduced resources for native fauna."
temperate_forests_east_asian["Invasive Species"]["Influenced By"] = [
    "Disturbance",
    "Temperate Forests (East Asian) - Climate Change",
    "Temperate Forests (East Asian) - Introduction"
]
temperate_forests_east_asian["Invasive Species"]["Influences"] = [
   "Can alter succession and other ecosystem processes."
]
temperate_forests_east_asian["Invasive Species"]["Logic Description"] = "Invasive plants can outcompete native species and alter ecosystem processes."
temperate_forests_east_asian["Invasive Species"]["Impact Function"] = "impact_invasive_species_east_asian"

temperate_forests_east_asian["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality); changes in monsoon patterns."
temperate_forests_east_asian["Climate Change"]["Data Sources"] = ["Climate models; historical climate records; national meteorological agency data."]
temperate_forests_east_asian["Climate Change"]["Impact on Area"] = "Indirect; changes in growing conditions, species distributions, fire risk."
temperate_forests_east_asian["Climate Change"]["Impact on Biodiversity"] = "Shifts in species ranges; increased stress on some species; changes in phenology; altered disturbance regimes."
temperate_forests_east_asian["Climate Change"]["Influenced By"] = ["Global GHG"]
temperate_forests_east_asian["Climate Change"]["Influences"] = ["Temperate Forests (East Asian) - Fire Regimes", "Temperate Forests (East Asian) - Water Availability", "Temperate Forests (East Asian) - Invasive Species"]
temperate_forests_east_asian["Climate Change"]["Logic Description"] = "Climate change, including changes in temperature, precipitation, and monsoon patterns, is expected to significantly impact East Asian temperate forests."
temperate_forests_east_asian["Climate Change"]["Impact Function"] = "impact_climate_change_east_asian"

temperate_forests_east_asian["Air Pollution"]["Metric"] = "Concentrations of ozone, nitrogen oxides (NOx), sulfur dioxide (SO2), and particulate matter."
temperate_forests_east_asian["Air Pollution"]["Data Sources"] = [
    "Air quality monitoring networks (national and regional).",
    "Research studies."
]
temperate_forests_east_asian["Air Pollution"]["Impact on Area"] = "Reduced tree growth; increased susceptibility to other stressors; acid deposition."
temperate_forests_east_asian["Air Pollution"]["Impact on Biodiversity"] = "Damage to sensitive plant species; changes in forest composition; impacts on lichens and other epiphytes."
temperate_forests_east_asian["Air Pollution"]["Influenced By"] = [
    "Industrial Emissions",
    "Vehicle Emissions",
    "Energy Production"
]
temperate_forests_east_asian["Air Pollution"]["Influences"] = [
    "Temperate Forests (East Asian) - Acid Deposition", "Temperate Forests (East Asian) - Plant Health"
]
temperate_forests_east_asian["Air Pollution"]["Logic Description"] = "High levels of air pollution, particularly in industrialized regions of East Asia, can damage forests and reduce their resilience to other stressors."
temperate_forests_east_asian["Air Pollution"]["Impact Function"] = "impact_air_pollution_east_asian"
temperate_forests_east_asian["Overexploitation (Plants)"]["Metric"] = "Harvest rates of commercially valuable or traditionally used plant species (e.g., medicinal plants, timber species)."
temperate_forests_east_asian["Overexploitation (Plants)"]["Data Sources"] = [
    "Forestry statistics.",
    "Market surveys.",
    "Ethnobotanical studies.",
    "CITES data (for internationally traded species)."
]
temperate_forests_east_asian["Overexploitation (Plants)"]["Impact on Area"] = "Local depletion of targeted species; changes in forest composition."
temperate_forests_east_asian["Overexploitation (Plants)"]["Impact on Biodiversity"] = "Decline of targeted species; potential impacts on species that depend on them."
temperate_forests_east_asian["Overexploitation (Plants)"]["Influenced By"] = [
        "Demand for Traditional Medicine",
        "Commercial Value",
       "Lack of Regulation/Enforcement"
]
temperate_forests_east_asian["Overexploitation (Plants)"]["Influences"] = [
        "Temperate Forests (East Asian) - Plant populations"
]
temperate_forests_east_asian["Overexploitation (Plants)"]["Logic Description"] = "Overexploitation of certain plant species for timber, medicine, or other uses can lead to their decline and impact forest structure."
temperate_forests_east_asian["Overexploitation (Plants)"]["Impact Function"] = "impact_overexploitation_plants_east_asian"

temperate_forests_east_asian["Forestry Practices"]["Metric"] = "Area of native forest converted to plantations (ha/year); area of native forest harvested (ha/year); type of harvesting system."
temperate_forests_east_asian["Forestry Practices"]["Data Sources"] = [
"National Forest Inventories.",
"Forestry statistics.",
"Research publications."
]
temperate_forests_east_asian["Forestry Practices"]["Impact on Area"] = "Changes in forest structure, age distribution, and composition."
temperate_forests_east_asian["Forestry Practices"]["Impact on Biodiversity"] = "Loss of old-growth forests; reduced habitat diversity; potential impacts on specific species depending on the type of forestry."
temperate_forests_east_asian["Forestry Practices"]["Influenced By"] = [
    "Demand for Timber and Wood Products",
    "Forest Management Policies",
    "Economic Factors"
]
temperate_forests_east_asian["Forestry Practices"]["Influences"] = [
        "Temperate Forests (East Asian) - Habitat Fragmentation",
    "Temperate Forests (East Asian) - Land-Use Change"

]
temperate_forests_east_asian["Forestry Practices"]["Logic Description"] = "Forestry practices, including the conversion of native forests to plantations, can significantly alter forest ecosystems."
temperate_forests_east_asian["Forestry Practices"]["Impact Function"] = "impact_forestry_practices_east_asian"

# --- Temperate Forests (European) ---
temperate_forests_european = all_stressors_data["European Temperate Forests"]

temperate_forests_european["Land-Use Change"]["Metric"] = "Area converted to agriculture, urban development, or other land uses (ha/year)."
temperate_forests_european["Land-Use Change"]["Data Sources"] = [
    "CORINE Land Cover (CLC) data.",
    "LUCAS (Land Use/Cover Area frame Survey) data.",
    "National forest inventories.",
    "Research publications."
]
temperate_forests_european["Land-Use Change"]["Impact on Area"] = "Significant historical deforestation and ongoing conversion, although at a slower rate than in some other regions."
temperate_forests_european["Land-Use Change"]["Impact on Biodiversity"] = "Habitat loss and fragmentation. Decline of forest-dependent species."
temperate_forests_european["Land-Use Change"]["Influenced By"] = [
    "Agricultural Expansion",
    "Urbanization",
    "Infrastructure Development",
     "Temperate Forests (European) - Forestry Practices"
]
temperate_forests_european["Land-Use Change"]["Influences"] = [
    "Temperate Forests (European) - Habitat Fragmentation"
]
temperate_forests_european["Land-Use Change"]["Logic Description"] = "Land-use change, due to a long history of agriculture, urbanization, and forestry, is a major driver of habitat loss and fragmentation in European temperate forests."
temperate_forests_european["Land-Use Change"]["Impact Function"] = "impact_land_use_change_european"

temperate_forests_european["Habitat Fragmentation"]["Metric"] = "Patch size distribution; edge density; connectivity indices."
temperate_forests_european["Habitat Fragmentation"]["Data Sources"] = [
    "Land cover data (from remote sensing and other sources, including CORINE).",
    "GIS analysis."
]
temperate_forests_european["Habitat Fragmentation"]["Impact on Area"] = "Forests exist in a highly fragmented landscape in many parts of Europe."
temperate_forests_european["Habitat Fragmentation"]["Impact on Biodiversity"] = "Reduced gene flow; increased edge effects; limited dispersal ability; increased vulnerability to stochastic events."
temperate_forests_european["Habitat Fragmentation"]["Influenced By"] = [
     "Temperate Forests (European) - Land-Use Change",
    "Infrastructure Development"
]
temperate_forests_european["Habitat Fragmentation"]["Influences"] = [
     "Exacerbates impacts of other stressors."
]
temperate_forests_european["Habitat Fragmentation"]["Logic Description"] = "Fragmentation isolates forest patches, reducing habitat quality and connectivity for many species."
temperate_forests_european["Habitat Fragmentation"]["Impact Function"] = "impact_habitat_fragmentation_european"

temperate_forests_european["Invasive Species"]["Metric"] = "Abundance and distribution of key invasive species (e.g., *Robinia pseudoacacia* (black locust), *Prunus serotina* (black cherry))."
temperate_forests_european["Invasive Species"]["Data Sources"] = [
   "Vegetation surveys.",
    "National forest inventories.",
    "Research studies.",
    "Invasive species databases (e.g., DAISIE - Delivering Alien Invasive Species Inventories for Europe)."
]
temperate_forests_european["Invasive Species"]["Impact on Area"] = "Changes in vegetation composition and structure."
temperate_forests_european["Invasive Species"]["Impact on Biodiversity"] = "Competition with native plants; altered habitat structure; reduced resources for native fauna."
temperate_forests_european["Invasive Species"]["Influenced By"] = [
    "Disturbance",
    "Temperate Forests (European) - Climate Change",
    "Temperate Forests (European) - Introduction"
]
temperate_forests_european["Invasive Species"]["Influences"] = [
  "Can affect ecosystem processes."
]
temperate_forests_european["Invasive Species"]["Logic Description"] = "Invasive plants can outcompete native species and alter forest ecosystem structure and function."
temperate_forests_european["Invasive Species"]["Impact Function"] = "impact_invasive_species_european"

temperate_forests_european["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality); changes in growing season length."
temperate_forests_european["Climate Change"]["Data Sources"] = ["Climate models; historical climate records; European Environment Agency (EEA) data."]
temperate_forests_european["Climate Change"]["Impact on Area"] = "Indirect; changes in growing conditions, species distributions, fire risk."
temperate_forests_european["Climate Change"]["Impact on Biodiversity"] = "Shifts in species ranges; increased stress on some species; changes in phenology; increased drought and fire risk in some areas."
temperate_forests_european["Climate Change"]["Influenced By"] = ["Global GHG"]
temperate_forests_european["Climate Change"]["Influences"] = ["Temperate Forests (European) - Fire Regimes", "Temperate Forests (European) - Water Availability", "Temperate Forests (European) - Invasive Species"]
temperate_forests_european["Climate Change"]["Logic Description"] = "Climate change is altering temperature and precipitation patterns, leading to increased stress on European forests and potentially favoring some invasive species."
temperate_forests_european["Climate Change"]["Impact Function"] = "impact_climate_change_european"

temperate_forests_european["Air Pollution"]["Metric"] = "Concentrations of ozone, nitrogen oxides (NOx), sulfur dioxide (SO2), and particulate matter."
temperate_forests_european["Air Pollution"]["Data Sources"] = [
    "European Monitoring and Evaluation Programme (EMEP).",
    "Air quality monitoring networks.",
    "Research studies."
]
temperate_forests_european["Air Pollution"]["Impact on Area"] = "Reduced tree growth; increased susceptibility to other stressors; acid deposition."
temperate_forests_european["Air Pollution"]["Impact on Biodiversity"] = "Damage to sensitive plant species; changes in forest composition; impacts on lichens and other epiphytes."
temperate_forests_european["Air Pollution"]["Influenced By"] = [
   "Industrial Emissions",
    "Vehicle Emissions",
    "Energy Production"
]
temperate_forests_european["Air Pollution"]["Influences"] = ["Temperate Forests (European) - Acid Deposition"]
temperate_forests_european["Air Pollution"]["Logic Description"] = "Air pollution, particularly in industrialized parts of Europe, can damage forests and reduce their resilience to other stressors."
temperate_forests_european["Air Pollution"]["Impact Function"] = "impact_air_pollution_european"

temperate_forests_european["Overbrowsing (Deer)"]["Metric"] = "Deer density (deer/km²); browsing intensity on key plant species."
temperate_forests_european["Overbrowsing (Deer)"]["Data Sources"] = [
    "Hunting statistics.",
    "Vegetation surveys (measuring browse impacts).",
   "Research studies."
]
temperate_forests_european["Overbrowsing (Deer)"]["Impact on Area"] = "Changes in forest understory composition; reduced tree regeneration."
temperate_forests_european["Overbrowsing (Deer)"]["Impact on Biodiversity"] = "Decline of palatable plant species; loss of understory habitat for other animals; impacts on forest regeneration."
temperate_forests_european["Overbrowsing (Deer)"]["Influenced By"] = [
    "Predator Management (or lack thereof)",
    "Hunting Regulations",
    "Habitat Fragmentation"
]
temperate_forests_european["Overbrowsing (Deer)"]["Influences"] = [
 "Temperate Forests (European) - Forest Regeneration"
]
temperate_forests_european["Overbrowsing (Deer)"]["Logic Description"] = "High deer populations, often due to a lack of predators and changes in land use, can suppress forest regeneration and alter understory plant communities."
temperate_forests_european["Overbrowsing (Deer)"]["Impact Function"] = "impact_overbrowsing_deer_european"

temperate_forests_european["Forestry Practices"]["Metric"] = "Area of native forest converted to plantations (ha/year); area of forest harvested (ha/year); type of harvesting system."
temperate_forests_european["Forestry Practices"]["Data Sources"] = [
  "National forest inventories.",
    "Forestry statistics.",
    "Research publications."
]
temperate_forests_european["Forestry Practices"]["Impact on Area"] = "Changes in forest structure, age distribution, and composition."
temperate_forests_european["Forestry Practices"]["Impact on Biodiversity"] = "Varies depending on practices; can create early successional habitat but also reduce habitat for old-growth dependent species and fragment forests."
temperate_forests_european["Forestry Practices"]["Influenced By"] = [
 "Demand for Timber and Wood Products",
    "Forest Management Policies",
    "Economic Factors"
]
temperate_forests_european["Forestry Practices"]["Influences"] = [
    "Temperate Forests (European) - Habitat Fragmentation",
    "Temperate Forests (European) - Land-Use Change"
]
temperate_forests_european["Forestry Practices"]["Logic Description"] = "Forestry practices, while providing timber resources, can significantly alter forest ecosystems, impacting biodiversity and ecosystem services."
temperate_forests_european["Forestry Practices"]["Impact Function"] = "impact_forestry_practices_european"

temperate_forests_european["Acid Deposition"]["Metric"] = "pH of precipitation and streamwater; levels of sulfate and nitrate deposition."
temperate_forests_european["Acid Deposition"]["Data Sources"] = [
    "European Monitoring and Evaluation Programme (EMEP).",
    "National monitoring programs."
]
temperate_forests_european["Acid Deposition"]["Impact on Area"] = "Soil acidification; nutrient imbalances; damage to trees (especially at higher elevations)."
temperate_forests_european["Acid Deposition"]["Impact on Biodiversity"] = "Decline of acid-sensitive species; impacts on aquatic ecosystems in forested areas."
temperate_forests_european["Acid Deposition"]["Influenced By"] = ["Temperate Forests (European) - Air Pollution"]
temperate_forests_european["Acid Deposition"]["Influences"] = [
 "Temperate Forests (European) - Water Quality",
    "Temperate Forests (European) - Soil Chemistry"
]
temperate_forests_european["Acid Deposition"]["Logic Description"] = "Acid deposition, resulting from air pollution, can damage forests and aquatic ecosystems by acidifying soils and water bodies."
temperate_forests_european["Acid Deposition"]["Impact Function"] = "impact_acid_deposition_european"

# --- Temperate Forests (Pacific Northwest) ---
temperate_forests_pacific_northwest = all_stressors_data["Pacific Northwest Temperate Forests"]

temperate_forests_pacific_northwest["Land-Use Change"]["Metric"] = "Area converted to urban development, agriculture, or other land uses (ha/year)."
temperate_forests_pacific_northwest["Land-Use Change"]["Data Sources"] = [
    "USGS National Land Cover Database (NLCD).",
    "Forest Inventory and Analysis (FIA) data.",
    "Canadian government data (for British Columbia).",
    "Local and regional land-use planning documents."
]
temperate_forests_pacific_northwest["Land-Use Change"]["Impact on Area"] = "Historical deforestation and ongoing conversion, particularly in low-elevation areas and near urban centers."
temperate_forests_pacific_northwest["Land-Use Change"]["Impact on Biodiversity"] = "Habitat loss and fragmentation. Decline of forest-dependent species, including old-growth associated species."
temperate_forests_pacific_northwest["Land-Use Change"]["Influenced By"] = [
   "Urbanization",
    "Temperate Forests (Pacific Northwest) - Forestry Practices",
    "Agricultural Expansion (Historically)"
]
temperate_forests_pacific_northwest["Land-Use Change"]["Influences"] = [
 "Temperate Forests (Pacific Northwest) - Habitat Fragmentation"
]
temperate_forests_pacific_northwest["Land-Use Change"]["Logic Description"] = "Land-use change, primarily from historical logging and ongoing urban expansion, is a significant stressor in the Pacific Northwest."
temperate_forests_pacific_northwest["Land-Use Change"]["Impact Function"] = "impact_land_use_change_pacific_northwest"

temperate_forests_pacific_northwest["Habitat Fragmentation"]["Metric"] = "Patch size distribution; edge density; connectivity indices."
temperate_forests_pacific_northwest["Habitat Fragmentation"]["Data Sources"] = [
    "Land cover data (from remote sensing and other sources).",
    "GIS analysis."
]
temperate_forests_pacific_northwest["Habitat Fragmentation"]["Impact on Area"] = "Forests are fragmented by roads, clearcuts, and urban development."
temperate_forests_pacific_northwest["Habitat Fragmentation"]["Impact on Biodiversity"] = "Reduced gene flow; increased edge effects; limited dispersal ability for some species; increased vulnerability to stochastic events."
temperate_forests_pacific_northwest["Habitat Fragmentation"]["Influenced By"] = [
  "Temperate Forests (Pacific Northwest) - Land-Use Change",
   "Temperate Forests (Pacific Northwest) - Forestry Practices",
    "Infrastructure Development"
]
temperate_forests_pacific_northwest["Habitat Fragmentation"]["Influences"] = [
 "Exacerbates impacts of other stressors."
]
temperate_forests_pacific_northwest["Habitat Fragmentation"]["Logic Description"] = "Fragmentation isolates forest patches, reducing habitat quality and connectivity, particularly for old-growth dependent species."
temperate_forests_pacific_northwest["Habitat Fragmentation"]["Impact Function"] = "impact_habitat_fragmentation_pacific_northwest"

temperate_forests_pacific_northwest["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality); snowpack depth; changes in streamflow."
temperate_forests_pacific_northwest["Climate Change"]["Data Sources"] = ["Climate models; historical climate records; snowpack monitoring data (SNOTEL); streamflow gauges."]
temperate_forests_pacific_northwest["Climate Change"]["Impact on Area"] = "Indirect; changes in growing conditions, species distributions, fire risk, and water availability."
temperate_forests_pacific_northwest["Climate Change"]["Impact on Biodiversity"] = "Shifts in species ranges (especially elevational shifts); increased stress on some species; increased fire risk; altered streamflow patterns affecting aquatic species."
temperate_forests_pacific_northwest["Climate Change"]["Influenced By"] = ["Global GHG"]
temperate_forests_pacific_northwest["Climate Change"]["Influences"] = ["Temperate Forests (Pacific Northwest) - Fire Regimes", "Temperate Forests (Pacific Northwest) - Stream Alteration", "Temperate Forests (Pacific Northwest) - Water Availability"]
temperate_forests_pacific_northwest["Climate Change"]["Logic Description"] = "Climate change is leading to warmer temperatures, reduced snowpack, and altered precipitation patterns, impacting forest ecosystems and water resources."
temperate_forests_pacific_northwest["Climate Change"]["Impact Function"] = "impact_climate_change_pacific_northwest"

temperate_forests_pacific_northwest["Forestry Practices"]["Metric"] = "Area harvested (ha/year); type of harvesting method (e.g., clearcutting, variable retention); road density."
temperate_forests_pacific_northwest["Forestry Practices"]["Data Sources"] = [
  "Forest Inventory and Analysis (FIA) data.",
    "State and provincial forestry agency data.",
    "Timber harvest permits.",
    "Research studies."
]
temperate_forests_pacific_northwest["Forestry Practices"]["Impact on Area"] = "Changes in forest age structure, composition, and habitat; increased road density."
temperate_forests_pacific_northwest["Forestry Practices"]["Impact on Biodiversity"] = "Loss of old-growth forests and associated species; reduced habitat diversity; impacts on stream ecosystems from sedimentation and increased water temperatures."
temperate_forests_pacific_northwest["Forestry Practices"]["Influenced By"] = [
    "Demand for Timber and Wood Products",
   "Forest Management Policies",
    "Economic Factors"
]
temperate_forests_pacific_northwest["Forestry Practices"]["Influences"] = [
   "Temperate Forests (Pacific Northwest) - Habitat Fragmentation",
   "Temperate Forests (Pacific Northwest) - Land-Use Change",
   "Temperate Forests (Pacific Northwest) - Stream Alteration"
]
temperate_forests_pacific_northwest["Forestry Practices"]["Logic Description"] = "Forestry practices, particularly historical clearcutting, have significantly altered forest structure and composition, impacting biodiversity and ecosystem services."
temperate_forests_pacific_northwest["Forestry Practices"]["Impact Function"] = "impact_forestry_practices_pacific_northwest"

temperate_forests_pacific_northwest["Fire Regimes"]["Metric"] = "Fire frequency (return interval - years); fire severity; area burned (ha/year)."
temperate_forests_pacific_northwest["Fire Regimes"]["Data Sources"] = [
   "Fire history data (from tree rings, charcoal records).",
    "Remote sensing data.",
    "Land management agency records."
]
temperate_forests_pacific_northwest["Fire Regimes"]["Impact on Area"] = "Changes in vegetation structure and composition; increased dominance of fire-adapted species in some areas."
temperate_forests_pacific_northwest["Fire Regimes"]["Impact on Biodiversity"] = "Loss of fire-sensitive species; changes in habitat structure.  Can be beneficial or detrimental depending on fire severity and frequency."
temperate_forests_pacific_northwest["Fire Regimes"]["Influenced By"] = [
    "Temperate Forests (Pacific Northwest) - Climate Change",
    "Temperate Forests (Pacific Northwest) - Forestry Practices",
  "Fire Suppression Policies",
    "Human Ignitions"
]
temperate_forests_pacific_northwest["Fire Regimes"]["Influences"] = [
 "Temperate Forests (Pacific Northwest) - Vegetation Changes"
]
temperate_forests_pacific_northwest["Fire Regimes"]["Logic Description"] = "Changes in fire regimes, influenced by climate change, past fire suppression, and forestry practices, can alter forest structure and composition."
temperate_forests_pacific_northwest["Fire Regimes"]["Impact Function"] = "impact_fire_regimes_pacific_northwest"

temperate_forests_pacific_northwest["Invasive Species"]["Metric"] = "Abundance and distribution of key invasive species (e.g., *Cytisus scoparius* (Scotch broom), *Hedera helix* (English ivy))."
temperate_forests_pacific_northwest["Invasive Species"]["Data Sources"] = [
   "Vegetation surveys.",
    "Research studies.",
    "Land management agency data."
]
temperate_forests_pacific_northwest["Invasive Species"]["Impact on Area"] = "Changes in vegetation composition and structure; altered disturbance regimes."
temperate_forests_pacific_northwest["Invasive Species"]["Impact on Biodiversity"] = "Competition with native plants; altered habitat structure; reduced resources for native fauna."
temperate_forests_pacific_northwest["Invasive Species"]["Influenced By"] = [
  "Disturbance",
   "Temperate Forests (Pacific Northwest) - Climate Change",
    "Temperate Forests (Pacific Northwest) - Introduction"
]
temperate_forests_pacific_northwest["Invasive Species"]["Influences"] = [
    "Can alter ecosystem processes."
]
temperate_forests_pacific_northwest["Invasive Species"]["Logic Description"] = "Invasive plants can outcompete native species and alter ecosystem processes, particularly in disturbed areas."
temperate_forests_pacific_northwest["Invasive Species"]["Impact Function"] = "impact_invasive_species_pacific_northwest"

temperate_forests_pacific_northwest["Stream Alteration"]["Metric"] = "Changes in streamflow; water temperature; sediment load; presence of dams and culverts."
temperate_forests_pacific_northwest["Stream Alteration"]["Data Sources"] = [
 "Streamflow gauges.",
    "Water quality monitoring data.",
    "Dam inventories.",
   "Research studies."
]
temperate_forests_pacific_northwest["Stream Alteration"]["Impact on Area"] = "Impacts on riparian habitats and aquatic ecosystems."
temperate_forests_pacific_northwest["Stream Alteration"]["Impact on Biodiversity"] = "Impacts on salmon and other aquatic species; reduced habitat quality; altered connectivity."
temperate_forests_pacific_northwest["Stream Alteration"]["Influenced By"] = [
   "Temperate Forests (Pacific Northwest) - Forestry Practices",
   "Dams and Water Diversions",
    "Urbanization",
   "Temperate Forests (Pacific Northwest) - Climate Change"
]
temperate_forests_pacific_northwest["Stream Alteration"]["Influences"] = [
 "Temperate Forests (Pacific Northwest) - Water Quality",
    "Temperate Forests (Pacific Northwest) - Aquatic Ecosystems"
]
temperate_forests_pacific_northwest["Stream Alteration"]["Logic Description"] = "Alteration of streamflow, water quality, and habitat due to forestry practices, dams, and other human activities has significant impacts on aquatic ecosystems, particularly for salmon."
temperate_forests_pacific_northwest["Stream Alteration"]["Impact Function"] = "impact_stream_alteration_pacific_northwest"

# --- Boreal Forests (Canadian) ---
boreal_forests_canadian = all_stressors_data["Canadian Boreal Forests"]

boreal_forests_canadian["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality); changes in growing season length; changes in snow cover."
boreal_forests_canadian["Climate Change"]["Data Sources"] = [
    "Climate models.",
    "Historical climate records.",
    "Environment and Climate Change Canada data."
]
boreal_forests_canadian["Climate Change"]["Impact on Area"] = "Indirect; changes in growing conditions, species distributions, fire risk, and permafrost stability."
boreal_forests_canadian["Climate Change"]["Impact on Biodiversity"] = "Shifts in species ranges; increased stress on some species; increased fire frequency and intensity; impacts on permafrost-dependent ecosystems."
boreal_forests_canadian["Climate Change"]["Influenced By"] = ["Global GHG"]
boreal_forests_canadian["Climate Change"]["Influences"] = [
   "Boreal Forests (Canadian) - Fire Regimes",
   "Boreal Forests (Canadian) - Permafrost Thaw",
   "Boreal Forests (Canadian) - Insect Outbreaks",
    "Boreal Forests (Canadian) - Water Availability"

]
boreal_forests_canadian["Climate Change"]["Logic Description"] = "Climate change is causing rapid warming in the boreal region, leading to changes in fire regimes, permafrost thaw, and insect outbreaks, among other impacts."
boreal_forests_canadian["Climate Change"]["Impact Function"] = "impact_climate_change_boreal_canadian"

boreal_forests_canadian["Fire Regimes"]["Metric"] = "Fire frequency (return interval - years); fire severity; area burned (ha/year)."
boreal_forests_canadian["Fire Regimes"]["Data Sources"] = [
    "Canadian National Fire Database (CNFDB).",
    "Remote sensing data.",
   "Research studies (e.g., tree-ring data)."
]
boreal_forests_canadian["Fire Regimes"]["Impact on Area"] = "Changes in forest age structure and composition; increased dominance of fire-adapted species."
boreal_forests_canadian["Fire Regimes"]["Impact on Biodiversity"] = "Loss of fire-sensitive species; changes in habitat structure. Fire is a natural and essential process in boreal forests, but changes in frequency and intensity can have negative impacts."
boreal_forests_canadian["Fire Regimes"]["Influenced By"] = [
  "Boreal Forests (Canadian) - Climate Change",
    "Boreal Forests (Canadian) - Forestry Practices",
   "Human Ignitions",
    "Insect Outbreaks"
]
boreal_forests_canadian["Fire Regimes"]["Influences"] = [
  "Boreal Forests (Canadian) - Vegetation Changes",
        "Boreal Forests (Canadian) - Carbon Cycling"
]
boreal_forests_canadian["Fire Regimes"]["Logic Description"] = "Climate change is increasing the frequency and intensity of wildfires in the boreal forest, altering forest structure and composition."
boreal_forests_canadian["Fire Regimes"]["Impact Function"] = "impact_fire_regimes_boreal_canadian"

boreal_forests_canadian["Forestry Practices"]["Metric"] = "Area harvested (ha/year); type of harvesting method; road density."
boreal_forests_canadian["Forestry Practices"]["Data Sources"] = [
 "National Forestry Database (Canada).",
    "Provincial government data.",
    "Research publications."
]
boreal_forests_canadian["Forestry Practices"]["Impact on Area"] = "Changes in forest age structure, composition, and habitat; increased road density."
boreal_forests_canadian["Forestry Practices"]["Impact on Biodiversity"] = "Loss of old-growth forests; reduced habitat diversity; impacts on species that require large, contiguous forest areas."
boreal_forests_canadian["Forestry Practices"]["Influenced By"] = [
   "Demand for Timber and Wood Products",
    "Forest Management Policies",
    "Economic Factors"
]
boreal_forests_canadian["Forestry Practices"]["Influences"] = [
    "Boreal Forests (Canadian) - Habitat Fragmentation",
    "Boreal Forests (Canadian) - Fire Regimes"
]
boreal_forests_canadian["Forestry Practices"]["Logic Description"] = "Forestry practices can alter forest structure and composition, impacting biodiversity and ecosystem services."
boreal_forests_canadian["Forestry Practices"]["Impact Function"] = "impact_forestry_practices_boreal_canadian"

boreal_forests_canadian["Mining and Energy Development"]["Metric"] = "Area disturbed by mining and energy development (ha/year); water quality parameters in affected areas."
boreal_forests_canadian["Mining and Energy Development"]["Data Sources"] = [
   "Mining and energy project permits and environmental assessments.",
    "Government data on resource extraction.",
   "Water quality monitoring data."
]
boreal_forests_canadian["Mining and Energy Development"]["Impact on Area"] = "Direct habitat loss; fragmentation; pollution (air, water, soil)."
boreal_forests_canadian["Mining and Energy Development"]["Impact on Biodiversity"] = "Loss of habitat; impacts on aquatic ecosystems from water pollution; disturbance to wildlife."
boreal_forests_canadian["Mining and Energy Development"]["Influenced By"] = [
    "Global Demand for Resources",
    "Government Policies",
    "Economic Factors"
]
boreal_forests_canadian["Mining and Energy Development"]["Influences"] = [
  "Boreal Forests (Canadian) - Habitat Fragmentation",
    "Boreal Forests (Canadian) - Water Pollution",
   "Boreal Forests (Canadian) - Land-Use Change"
]
boreal_forests_canadian["Mining and Energy Development"]["Logic Description"] = "Mining and energy development, including oil sands extraction, can cause significant habitat destruction and pollution in the boreal forest."
boreal_forests_canadian["Mining and Energy Development"]["Impact Function"] = "impact_mining_energy_boreal_canadian"

boreal_forests_canadian["Invasive Species"]["Metric"] = "Abundance and distribution of key invasive species (e.g., certain plants, insects, and pathogens)."
boreal_forests_canadian["Invasive Species"]["Data Sources"] = [
   "Vegetation surveys.",
    "Forest health monitoring data.",
    "Research studies."
]
boreal_forests_canadian["Invasive Species"]["Impact on Area"] = "Changes in vegetation composition and structure; potential impacts on forest health."
boreal_forests_canadian["Invasive Species"]["Impact on Biodiversity"] = "Competition with native species; potential for increased tree mortality (for invasive insects and pathogens)."
boreal_forests_canadian["Invasive Species"]["Influenced By"] = [
    "Disturbance",
   "Boreal Forests (Canadian) - Climate Change",
    "Boreal Forests (Canadian) - Introduction"
]
boreal_forests_canadian["Invasive Species"]["Influences"] = [
    "Can exacerbate other stressors."
]
boreal_forests_canadian["Invasive Species"]["Logic Description"] = "Invasive species, while currently less of a threat than in some other ecosystems, pose a growing risk to the boreal forest, particularly with climate change."
boreal_forests_canadian["Invasive Species"]["Impact Function"] = "impact_invasive_species_boreal_canadian"

boreal_forests_canadian["Insect Outbreaks"]["Metric"] = "Area affected by insect outbreaks (ha/year); severity of defoliation."
boreal_forests_canadian["Insect Outbreaks"]["Data Sources"] = [
 "Aerial surveys of insect damage.",
    "Forest health monitoring data.",
    "Research studies."
]
boreal_forests_canadian["Insect Outbreaks"]["Impact on Area"] = "Widespread tree mortality; changes in forest composition and structure."
boreal_forests_canadian["Insect Outbreaks"]["Impact on Biodiversity"] = "Impacts on species that depend on affected tree species; changes in forest dynamics.  Can be a natural part of boreal forest ecology, but outbreaks are becoming more frequent and severe."
boreal_forests_canadian["Insect Outbreaks"]["Influenced By"] = [
   "Boreal Forests (Canadian) - Climate Change",
   "Boreal Forests (Canadian) - Forest Management Practices"
]
boreal_forests_canadian["Insect Outbreaks"]["Influences"] = [
 "Boreal Forests (Canadian) - Fire Regimes",
    "Boreal Forests (Canadian) - Forest Composition"
]
boreal_forests_canadian["Insect Outbreaks"]["Logic Description"] = "Climate change is contributing to more frequent and severe insect outbreaks, such as spruce budworm and mountain pine beetle, which can cause widespread tree mortality."
boreal_forests_canadian["Insect Outbreaks"]["Impact Function"] = "impact_insect_outbreaks_boreal_canadian"

boreal_forests_canadian["Habitat Fragmentation"]["Metric"] = "Patch size distribution; edge density; connectivity indices."
boreal_forests_canadian["Habitat Fragmentation"]["Data Sources"] = [
 "Land cover data (from remote sensing and other sources).",
    "GIS analysis."
]
boreal_forests_canadian["Habitat Fragmentation"]["Impact on Area"] = "Forests are fragmented by roads, pipelines, seismic lines, and other development."
boreal_forests_canadian["Habitat Fragmentation"]["Impact on Biodiversity"] = "Reduced gene flow; increased edge effects; limited dispersal ability for some species; increased vulnerability to stochastic events."
boreal_forests_canadian["Habitat Fragmentation"]["Influenced By"] = [
    "Boreal Forests (Canadian) - Forestry Practices",
   "Boreal Forests (Canadian) - Mining and Energy Development",
   "Infrastructure Development"
]
boreal_forests_canadian["Habitat Fragmentation"]["Influences"] = [
"Exacerbates impacts of other stressors, like invasive species"
]
boreal_forests_canadian["Habitat Fragmentation"]["Logic Description"] = "Fragmentation isolates forest patches, reducing habitat quality and connectivity, which is a particular concern for species like caribou."
boreal_forests_canadian["Habitat Fragmentation"]["Impact Function"] = "impact_habitat_fragmentation_boreal_canadian"

boreal_forests_canadian["Permafrost Thaw"]["Metric"] = "Active layer thickness; ground temperature; area of permafrost degradation."
boreal_forests_canadian["Permafrost Thaw"]["Data Sources"] = [
"Permafrost monitoring networks.",
"Remote sensing data.",
"Research studies."
]
boreal_forests_canadian["Permafrost Thaw"]["Impact on Area"] = "Changes in ground stability; altered hydrology; release of greenhouse gases (methane and carbon dioxide)."
boreal_forests_canadian["Permafrost Thaw"]["Impact on Biodiversity"] = "Impacts on vegetation communities; changes in wetland habitats; impacts on infrastructure."
boreal_forests_canadian["Permafrost Thaw"]["Influenced By"] = [
        "Boreal Forests (Canadian) - Climate Change"
]
boreal_forests_canadian["Permafrost Thaw"]["Influences"] = [
        "Boreal Forests (Canadian) - Hydrology",
        "Boreal Forests (Canadian) - Carbon Cycling",
    "Boreal Forests (Canadian) - GHG emissions"
]
boreal_forests_canadian["Permafrost Thaw"]["Logic Description"] = "Warming temperatures are causing permafrost to thaw, leading to ground instability, altered hydrology, and the release of greenhouse gases."
boreal_forests_canadian["Permafrost Thaw"]["Impact Function"] = "impact_permafrost_thaw_boreal_canadian"

# --- Boreal Forests (Russian) ---
boreal_forests_russian = all_stressors_data["Russian Boreal Forests"]

boreal_forests_russian["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality); changes in growing season length; changes in snow cover."
boreal_forests_russian["Climate Change"]["Data Sources"] = [
    "Climate models.",
    "Historical climate records.",
    "Roshydromet (Russian Federal Service for Hydrometeorology and Environmental Monitoring) data."
]
boreal_forests_russian["Climate Change"]["Impact on Area"] = "Indirect; changes in growing conditions, species distributions, fire risk, and permafrost stability."
boreal_forests_russian["Climate Change"]["Impact on Biodiversity"] = "Shifts in species ranges; increased stress on some species; increased fire frequency and intensity; impacts on permafrost-dependent ecosystems."
boreal_forests_russian["Climate Change"]["Influenced By"] = ["Global GHG"]
boreal_forests_russian["Climate Change"]["Influences"] = [
   "Boreal Forests (Russian) - Fire Regimes",
    "Boreal Forests (Russian) - Permafrost Thaw",
    "Boreal Forests (Russian) - Insect Outbreaks",
    "Boreal Forests (Russian) - Water Availability"
]
boreal_forests_russian["Climate Change"]["Logic Description"] = "Climate change is causing rapid warming in the boreal region, leading to changes in fire regimes, permafrost thaw, and insect outbreaks, among other impacts. The effects are particularly pronounced in Siberia."
boreal_forests_russian["Climate Change"]["Impact Function"] = "impact_climate_change_boreal_russian"

boreal_forests_russian["Fire Regimes"]["Metric"] = "Fire frequency (return interval - years); fire severity; area burned (ha/year)."
boreal_forests_russian["Fire Regimes"]["Data Sources"] = [
    "Russian Federal Forestry Agency data.",
    "Remote sensing data (e.g., MODIS, Landsat).",
    "Research studies (e.g., tree-ring data)."
]
boreal_forests_russian["Fire Regimes"]["Impact on Area"] = "Changes in forest age structure and composition; increased dominance of fire-adapted species; large areas burned annually."
boreal_forests_russian["Fire Regimes"]["Impact on Biodiversity"] = "Loss of fire-sensitive species; changes in habitat structure. Fire is a natural process, but increasing frequency and intensity are causing significant changes."
boreal_forests_russian["Fire Regimes"]["Influenced By"] = [
   "Boreal Forests (Russian) - Climate Change",
   "Boreal Forests (Russian) - Forestry Practices",
   "Human Ignitions",
    "Insect Outbreaks",
     "Boreal Forests (Russian) - Illegal Logging"
]
boreal_forests_russian["Fire Regimes"]["Influences"] = [
   "Boreal Forests (Russian) - Vegetation Changes",
    "Boreal Forests (Russian) - Carbon Cycling"
]
boreal_forests_russian["Fire Regimes"]["Logic Description"] = "Climate change and human activities are increasing the frequency and intensity of wildfires, leading to significant impacts on forest ecosystems."
boreal_forests_russian["Fire Regimes"]["Impact Function"] = "impact_fire_regimes_boreal_russian"

boreal_forests_russian["Forestry Practices"]["Metric"] = "Area harvested (ha/year); type of harvesting method; road density."
boreal_forests_russian["Forestry Practices"]["Data Sources"] = [
    "Russian Federal Forestry Agency data.",
    "Research publications.",
    "Remote Sensing"
]
boreal_forests_russian["Forestry Practices"]["Impact on Area"] = "Changes in forest age structure, composition, and habitat; increased road density."
boreal_forests_russian["Forestry Practices"]["Impact on Biodiversity"] = "Loss of old-growth forests; reduced habitat diversity; impacts on species that require large, contiguous forest areas."
boreal_forests_russian["Forestry Practices"]["Influenced By"] = [
   "Demand for Timber and Wood Products",
    "Forest Management Policies",
    "Economic Factors",
    "Boreal Forests (Russian) - Illegal Logging"
]
boreal_forests_russian["Forestry Practices"]["Influences"] = [
    "Boreal Forests (Russian) - Habitat Fragmentation",
    "Boreal Forests (Russian) - Fire Regimes"
]
boreal_forests_russian["Forestry Practices"]["Logic Description"] = "Forestry practices, including legal and illegal logging, can significantly alter forest structure and composition."
boreal_forests_russian["Forestry Practices"]["Impact Function"] = "impact_forestry_practices_boreal_russian"

boreal_forests_russian["Mining and Energy Development"]["Metric"] = "Area disturbed by mining and energy development (ha/year); water quality parameters in affected areas."
boreal_forests_russian["Mining and Energy Development"]["Data Sources"] = [
   "Mining and energy project permits and environmental assessments.",
    "Government data on resource extraction.",
    "Water quality monitoring data."
]
boreal_forests_russian["Mining and Energy Development"]["Impact on Area"] = "Direct habitat loss; fragmentation; pollution (air, water, soil)."
boreal_forests_russian["Mining and Energy Development"]["Impact on Biodiversity"] = "Loss of habitat; impacts on aquatic ecosystems from water pollution; disturbance to wildlife, particularly from oil and gas development in Siberia."
boreal_forests_russian["Mining and Energy Development"]["Influenced By"] = [
    "Global Demand for Resources",
   "Government Policies",
    "Economic Factors"
]
boreal_forests_russian["Mining and Energy Development"]["Influences"] = [
 "Boreal Forests (Russian) - Habitat Fragmentation",
    "Boreal Forests (Russian) - Water Pollution",
     "Boreal Forests (Russian) - Land-Use Change"
]
boreal_forests_russian["Mining and Energy Development"]["Logic Description"] = "Extensive mining and energy development, particularly oil and gas extraction in Siberia, poses a major threat to the Russian boreal forest."
boreal_forests_russian["Mining and Energy Development"]["Impact Function"] = "impact_mining_energy_boreal_russian"

boreal_forests_russian["Invasive Species"]["Metric"] = "Abundance and distribution of key invasive species (e.g., certain plants, insects, and pathogens)."
boreal_forests_russian["Invasive Species"]["Data Sources"] = [
    "Vegetation surveys.",
    "Forest health monitoring data.",
    "Research studies."
]
boreal_forests_russian["Invasive Species"]["Impact on Area"] = "Changes in vegetation composition and structure; potential impacts on forest health."
boreal_forests_russian["Invasive Species"]["Impact on Biodiversity"] = "Competition with native species; potential for increased tree mortality (for invasive insects and pathogens)."
boreal_forests_russian["Invasive Species"]["Influenced By"] = [
    "Disturbance",
    "Boreal Forests (Russian) - Climate Change",
     "Boreal Forests (Russian) - Introduction"
]
boreal_forests_russian["Invasive Species"]["Influences"] = [
 "Can exacerbate existing stressors"
]
boreal_forests_russian["Invasive Species"]["Logic Description"] = "Invasive species, while currently a smaller threat compared to other stressors, pose an increasing risk, particularly with climate change."
boreal_forests_russian["Invasive Species"]["Impact Function"] = "impact_invasive_species_boreal_russian"

boreal_forests_russian["Insect Outbreaks"]["Metric"] = "Area affected by insect outbreaks (ha/year); severity of defoliation."
boreal_forests_russian["Insect Outbreaks"]["Data Sources"] = [
   "Aerial surveys of insect damage.",
    "Forest health monitoring data.",
    "Research studies.",
    "Russian Federal Forestry Agency data"
]
boreal_forests_russian["Insect Outbreaks"]["Impact on Area"] = "Widespread tree mortality; changes in forest composition and structure.  Siberian silk moth is a major concern."
boreal_forests_russian["Insect Outbreaks"]["Impact on Biodiversity"] = "Impacts on species that depend on affected tree species; changes in forest dynamics. Outbreaks can be a natural part of boreal forest ecology, but they are becoming more frequent and severe."
boreal_forests_russian["Insect Outbreaks"]["Influenced By"] = [
   "Boreal Forests (Russian) - Climate Change",
   "Boreal Forests (Russian) - Forest Management Practices"
]
boreal_forests_russian["Insect Outbreaks"]["Influences"] = [
    "Boreal Forests (Russian) - Fire Regimes",
   "Boreal Forests (Russian) - Forest Composition"
]
boreal_forests_russian["Insect Outbreaks"]["Logic Description"] = "Climate change is contributing to more frequent and severe insect outbreaks, such as the Siberian silk moth, which can cause extensive tree mortality."
boreal_forests_russian["Insect Outbreaks"]["Impact Function"] = "impact_insect_outbreaks_boreal_russian"

boreal_forests_russian["Habitat Fragmentation"]["Metric"] = "Patch size distribution; edge density; connectivity indices."
boreal_forests_russian["Habitat Fragmentation"]["Data Sources"] = [
    "Land cover data (from remote sensing and other sources).",
   "GIS analysis."
]
boreal_forests_russian["Habitat Fragmentation"]["Impact on Area"] = "Forests are fragmented by roads, pipelines, seismic lines, and other development, particularly in areas with resource extraction."
boreal_forests_russian["Habitat Fragmentation"]["Impact on Biodiversity"] = "Reduced gene flow; increased edge effects; limited dispersal ability for some species; increased vulnerability to stochastic events."
boreal_forests_russian["Habitat Fragmentation"]["Influenced By"] = [
    "Boreal Forests (Russian) - Forestry Practices",
    "Boreal Forests (Russian) - Mining and Energy Development",
    "Infrastructure Development"
]
boreal_forests_russian["Habitat Fragmentation"]["Influences"] = [
 "Exacerbates other stressors."
]
boreal_forests_russian["Habitat Fragmentation"]["Logic Description"] = "Fragmentation isolates forest patches, reducing habitat quality and connectivity, particularly impacting large mammals and migratory species."
boreal_forests_russian["Habitat Fragmentation"]["Impact Function"] = "impact_habitat_fragmentation_boreal_russian"

boreal_forests_russian["Permafrost Thaw"]["Metric"] = "Active layer thickness; ground temperature; area of permafrost degradation."
boreal_forests_russian["Permafrost Thaw"]["Data Sources"] = [
    "Permafrost monitoring networks.",
    "Remote sensing data.",
    "Research studies."
]
boreal_forests_russian["Permafrost Thaw"]["Impact on Area"] = "Changes in ground stability; altered hydrology; release of greenhouse gases (methane and carbon dioxide); formation of thermokarst features."
boreal_forests_russian["Permafrost Thaw"]["Impact on Biodiversity"] = "Impacts on vegetation communities; changes in wetland habitats; impacts on infrastructure.  Significant implications for global climate change due to greenhouse gas release."
boreal_forests_russian["Permafrost Thaw"]["Influenced By"] = ["Boreal Forests (Russian) - Climate Change"]
boreal_forests_russian["Permafrost Thaw"]["Influences"] = ["Boreal Forests (Russian) - Hydrology",
        "Boreal Forests (Russian) - Carbon Cycling", "Global GHG"]
boreal_forests_russian["Permafrost Thaw"]["Logic Description"] = "Warming temperatures are causing widespread permafrost thaw, leading to significant landscape changes and the release of large amounts of greenhouse gases."
boreal_forests_russian["Permafrost Thaw"]["Impact Function"] = "impact_permafrost_thaw_boreal_russian"

boreal_forests_russian["Illegal Logging"]["Metric"] = "Estimated volume of illegally harvested timber; number of illegal logging cases."
boreal_forests_russian["Illegal Logging"]["Data Sources"] = [
    "Reports from environmental organizations (e.g., WWF, Greenpeace).",
    "Remote sensing analysis (detecting illegal logging activity).",
   "Government reports (though often underestimate the problem)."
]
boreal_forests_russian["Illegal Logging"]["Impact on Area"] = "Loss of valuable timber species; degradation of forest ecosystems; economic losses."
boreal_forests_russian["Illegal Logging"]["Impact on Biodiversity"] = "Loss of habitat; disruption of forest structure; impacts on endangered species."
boreal_forests_russian["Illegal Logging"]["Influenced By"] = [
 "Corruption",
    "Weak Law Enforcement",
   "Demand for Timber (Domestic and International)"
]
boreal_forests_russian["Illegal Logging"]["Influences"] = [
    "Boreal Forests (Russian) - Forestry Practices",
    "Boreal Forests (Russian) - Fire Regimes"
]
boreal_forests_russian["Illegal Logging"]["Logic Description"] = "Illegal logging is a significant problem in the Russian Far East and other parts of the boreal forest, contributing to deforestation and forest degradation."
boreal_forests_russian["Illegal Logging"]["Impact Function"] = "impact_illegal_logging_boreal_russian"

# --- Boreal Forests (Scandinavian and Finnish) ---
boreal_forests_scandinavian_finnish = all_stressors_data["Scandinavian and Finnish Boreal Forests"]

boreal_forests_scandinavian_finnish["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality); changes in growing season length; changes in snow cover."
boreal_forests_scandinavian_finnish["Climate Change"]["Data Sources"] = [
    "Climate models.",
    "Historical climate records.",
    "National meteorological institutes (e.g., Finnish Meteorological Institute, Swedish Meteorological and Hydrological Institute, Norwegian Meteorological Institute)."
]
boreal_forests_scandinavian_finnish["Climate Change"]["Impact on Area"] = "Indirect; changes in growing conditions, species distributions, fire risk."
boreal_forests_scandinavian_finnish["Climate Change"]["Impact on Biodiversity"] = "Shifts in species ranges; increased stress on some species; potential for increased fire frequency and intensity; impacts on snow-dependent species."
boreal_forests_scandinavian_finnish["Climate Change"]["Influenced By"] = ["Global GHG"]
boreal_forests_scandinavian_finnish["Climate Change"]["Influences"] = [
    "Boreal Forests (Scandinavian and Finnish) - Fire Regimes",
    "Boreal Forests (Scandinavian and Finnish) - Insect Outbreaks",
     "Boreal Forests (Scandinavian and Finnish) - Water Availability"
]
boreal_forests_scandinavian_finnish["Climate Change"]["Logic Description"] = "Climate change is causing warming and changes in precipitation patterns, impacting forest ecosystems and potentially increasing fire risk and insect outbreaks."
boreal_forests_scandinavian_finnish["Climate Change"]["Impact Function"] = "impact_climate_change_boreal_scandinavian_finnish"

boreal_forests_scandinavian_finnish["Fire Regimes"]["Metric"] = "Fire frequency (return interval - years); fire severity; area burned (ha/year)."
boreal_forests_scandinavian_finnish["Fire Regimes"]["Data Sources"] = [
    "National forest inventory data.",
    "Remote sensing data.",
    "Research studies (e.g., fire history reconstructions)."
]
boreal_forests_scandinavian_finnish["Fire Regimes"]["Impact on Area"] = "Changes in forest age structure and composition; increased dominance of fire-adapted species in some areas.  Historically, fire has been suppressed in many areas."
boreal_forests_scandinavian_finnish["Fire Regimes"]["Impact on Biodiversity"] = "Loss of fire-sensitive species in areas with increased fire activity; changes in habitat structure. Fire is a natural process, but altered frequency and intensity can have negative impacts."
boreal_forests_scandinavian_finnish["Fire Regimes"]["Influenced By"] = [
    "Boreal Forests (Scandinavian and Finnish) - Climate Change",
     "Boreal Forests (Scandinavian and Finnish) - Forestry Practices",
    "Fire Suppression Policies",
    "Human Ignitions"
]
boreal_forests_scandinavian_finnish["Fire Regimes"]["Influences"] = [
  "Boreal Forests (Scandinavian and Finnish) - Vegetation Changes"
]
boreal_forests_scandinavian_finnish["Fire Regimes"]["Logic Description"] = "Changes in fire regimes, influenced by climate change and forestry practices, are altering forest dynamics."
boreal_forests_scandinavian_finnish["Fire Regimes"]["Impact Function"] = "impact_fire_regimes_boreal_scandinavian_finnish"

boreal_forests_scandinavian_finnish["Forestry Practices"]["Metric"] = "Area harvested (ha/year); type of harvesting method (e.g., clearcutting, continuous cover forestry); proportion of forest managed for timber production."
boreal_forests_scandinavian_finnish["Forestry Practices"]["Data Sources"] = [
    "National forest inventory data.",
    "Forestry statistics from government agencies.",
    "Research publications."
]
boreal_forests_scandinavian_finnish["Forestry Practices"]["Impact on Area"] = "Significant changes in forest age structure, composition, and habitat; high proportion of managed forests."
boreal_forests_scandinavian_finnish["Forestry Practices"]["Impact on Biodiversity"] = "Loss of old-growth forests and associated species; reduced structural diversity; impacts on species that require dead wood or specific forest types."
boreal_forests_scandinavian_finnish["Forestry Practices"]["Influenced By"] = [
    "Demand for Timber and Wood Products",
    "Forest Management Policies",
   "Economic Factors"
]
boreal_forests_scandinavian_finnish["Forestry Practices"]["Influences"] = [
  "Boreal Forests (Scandinavian and Finnish) - Habitat Fragmentation",
    "Boreal Forests (Scandinavian and Finnish) - Fire Regimes"
]
boreal_forests_scandinavian_finnish["Forestry Practices"]["Logic Description"] = "Intensive forestry practices, including clearcutting and the establishment of even-aged stands, have significantly altered the structure and composition of Fennoscandian boreal forests."
boreal_forests_scandinavian_finnish["Forestry Practices"]["Impact Function"] = "impact_forestry_practices_boreal_scandinavian_finnish"

boreal_forests_scandinavian_finnish["Invasive Species"]["Metric"] = "Abundance and distribution of key invasive species (e.g., *Lupinus polyphyllus* (large-leaved lupine))."
boreal_forests_scandinavian_finnish["Invasive Species"]["Data Sources"] = [
   "Vegetation surveys.",
    "National invasive species databases.",
    "Research studies."
]
boreal_forests_scandinavian_finnish["Invasive Species"]["Impact on Area"] = "Changes in vegetation composition and structure, particularly in disturbed areas."
boreal_forests_scandinavian_finnish["Invasive Species"]["Impact on Biodiversity"] = "Competition with native plants; potential impacts on nutrient cycling."
boreal_forests_scandinavian_finnish["Invasive Species"]["Influenced By"] = [
    "Disturbance",
   "Boreal Forests (Scandinavian and Finnish) - Climate Change",
    "Boreal Forests (Scandinavian and Finnish) - Introduction"
]
boreal_forests_scandinavian_finnish["Invasive Species"]["Influences"] = [
 "Can alter ecosystem processes"
]
boreal_forests_scandinavian_finnish["Invasive Species"]["Logic Description"] = "While invasive species are not as widespread a problem as in some other regions, certain invasive plants can impact forest ecosystems, particularly in disturbed areas."
boreal_forests_scandinavian_finnish["Invasive Species"]["Impact Function"] = "impact_invasive_species_boreal_scandinavian_finnish"

boreal_forests_scandinavian_finnish["Insect Outbreaks"]["Metric"] = "Area affected by insect outbreaks (ha/year); severity of defoliation."
boreal_forests_scandinavian_finnish["Insect Outbreaks"]["Data Sources"] = [
    "Forest health monitoring data.",
    "Aerial surveys.",
    "Research studies."
]
boreal_forests_scandinavian_finnish["Insect Outbreaks"]["Impact on Area"] = "Potential for tree mortality; changes in forest composition and structure."
boreal_forests_scandinavian_finnish["Insect Outbreaks"]["Impact on Biodiversity"] = "Impacts on species that depend on affected tree species; changes in forest dynamics. Outbreaks can be a natural part of forest ecology."
boreal_forests_scandinavian_finnish["Insect Outbreaks"]["Influenced By"] = [
   "Boreal Forests (Scandinavian and Finnish) - Climate Change",
    "Boreal Forests (Scandinavian and Finnish) - Forestry Practices"
]
boreal_forests_scandinavian_finnish["Insect Outbreaks"]["Influences"] = [
    "Boreal Forests (Scandinavian and Finnish) - Fire Regimes",
    "Boreal Forests (Scandinavian and Finnish) - Forest Composition"
]
boreal_forests_scandinavian_finnish["Insect Outbreaks"]["Logic Description"] = "Climate change may increase the risk of insect outbreaks, potentially impacting forest health."
boreal_forests_scandinavian_finnish["Insect Outbreaks"]["Impact Function"] = "impact_insect_outbreaks_boreal_scandinavian_finnish"

boreal_forests_scandinavian_finnish["Habitat Fragmentation"]["Metric"] = "Patch size distribution; edge density; connectivity indices."
boreal_forests_scandinavian_finnish["Habitat Fragmentation"]["Data Sources"] = [
    "Land cover data (from remote sensing and other sources).",
    "GIS analysis."
]
boreal_forests_scandinavian_finnish["Habitat Fragmentation"]["Impact on Area"] = "Forests are fragmented by roads, forestry operations, and other human activities."
boreal_forests_scandinavian_finnish["Habitat Fragmentation"]["Impact on Biodiversity"] = "Reduced gene flow; increased edge effects; limited dispersal ability for some species; increased vulnerability to stochastic events."
boreal_forests_scandinavian_finnish["Habitat Fragmentation"]["Influenced By"] = [
   "Boreal Forests (Scandinavian and Finnish) - Forestry Practices",
    "Infrastructure Development"
]
boreal_forests_scandinavian_finnish["Habitat Fragmentation"]["Influences"] = [
 "Exacerbates the impacts of other stressors."
]
boreal_forests_scandinavian_finnish["Habitat Fragmentation"]["Logic Description"] = "Fragmentation isolates forest patches, reducing habitat quality and connectivity, particularly for species that require large, continuous forest areas or old-growth characteristics."
boreal_forests_scandinavian_finnish["Habitat Fragmentation"]["Impact Function"] = "impact_habitat_fragmentation_boreal_scandinavian_finnish"

# --- Mountains (Alps) ---
mountains_alps = all_stressors_data["Alps Mountains"]

mountains_alps["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality); glacier retreat (area, volume); snow cover duration."
mountains_alps["Climate Change"]["Data Sources"] = [
    "Climate models.",
    "Historical climate records.",
    "Glacier monitoring programs (e.g., WGMS - World Glacier Monitoring Service).",
    "National meteorological services of Alpine countries."
]
mountains_alps["Climate Change"]["Impact on Area"] = "Indirect; changes in growing conditions, species distributions, water availability, and glacier extent."
mountains_alps["Climate Change"]["Impact on Biodiversity"] = "Shifts in species ranges (upslope migration); increased stress on high-elevation species; loss of glacier-fed habitats; changes in vegetation communities."
mountains_alps["Climate Change"]["Influenced By"] = ["Global GHG"]
mountains_alps["Climate Change"]["Influences"] = [
    "Mountains (Alps) - Changes in Water Availability",
    "Mountains (Alps) - Glacier Retreat",
    "Mountains (Alps) - Snow Cover Changes"
]
mountains_alps["Climate Change"]["Logic Description"] = "The Alps are highly sensitive to climate change, experiencing warming at a rate higher than the global average. This leads to glacier retreat, changes in snow cover, and shifts in species distributions."
mountains_alps["Climate Change"]["Impact Function"] = "impact_climate_change_alps"

mountains_alps["Tourism and Recreation"]["Metric"] = "Number of tourists; area of ski resorts and other infrastructure; intensity of recreational activities."
mountains_alps["Tourism and Recreation"]["Data Sources"] = [
    "Tourism statistics from national and regional agencies.",
    "Data on ski resort infrastructure.",
   "Research studies."
]
mountains_alps["Tourism and Recreation"]["Impact on Area"] = "Habitat destruction and fragmentation; soil erosion; disturbance to wildlife; pollution (waste, noise)."
mountains_alps["Tourism and Recreation"]["Impact on Biodiversity"] = "Impacts on sensitive alpine vegetation; disturbance to wildlife, particularly during breeding seasons; habitat loss."
mountains_alps["Tourism and Recreation"]["Influenced By"] = [
    "Economic Demand for Tourism",
   "Accessibility",
    "Marketing and Promotion"
]
mountains_alps["Tourism and Recreation"]["Influences"] = [
    "Mountains (Alps) - Habitat Fragmentation",
    "Mountains (Alps) - Land-Use Change"
]
mountains_alps["Tourism and Recreation"]["Logic Description"] = "Intensive tourism and recreation, particularly winter sports, put significant pressure on alpine ecosystems."
mountains_alps["Tourism and Recreation"]["Impact Function"] = "impact_tourism_recreation_alps"

mountains_alps["Habitat Fragmentation"]["Metric"] = "Patch size distribution; edge density; connectivity indices."
mountains_alps["Habitat Fragmentation"]["Data Sources"] = [
   "Land cover data (from remote sensing and other sources).",
    "GIS analysis."
]
mountains_alps["Habitat Fragmentation"]["Impact on Area"] = "Natural habitats are fragmented by roads, ski runs, settlements, and other infrastructure."
mountains_alps["Habitat Fragmentation"]["Impact on Biodiversity"] = "Reduced gene flow; increased edge effects; limited dispersal ability; increased vulnerability to stochastic events."
mountains_alps["Habitat Fragmentation"]["Influenced By"] = [
  "Mountains (Alps) - Tourism and Recreation",
  "Mountains (Alps) - Land-Use Change",
    "Infrastructure Development"
]
mountains_alps["Habitat Fragmentation"]["Influences"] = [
   "Exacerbates impacts of other stressors."
]
mountains_alps["Habitat Fragmentation"]["Logic Description"] = "Fragmentation isolates habitats, reducing connectivity and making populations more vulnerable to other stressors."
mountains_alps["Habitat Fragmentation"]["Impact Function"] = "impact_habitat_fragmentation_alps"

mountains_alps["Land-Use Change"]["Metric"] = "Area of agricultural land abandonment; area of forest expansion; area converted to settlements and infrastructure."
mountains_alps["Land-Use Change"]["Data Sources"] = [
    "Land cover data (e.g., CORINE).",
    "Agricultural statistics.",
    "National and regional land-use planning documents."
]
mountains_alps["Land-Use Change"]["Impact on Area"] = "Changes in landscape structure and composition; loss of traditional agricultural landscapes."
mountains_alps["Land-Use Change"]["Impact on Biodiversity"] = "Impacts on species adapted to specific land-use types (e.g., traditional meadows); changes in habitat diversity."
mountains_alps["Land-Use Change"]["Influenced By"] = [
   "Agricultural Policies",
    "Socioeconomic Changes",
    "Mountains (Alps) - Tourism and Recreation"
]
mountains_alps["Land-Use Change"]["Influences"] = [
   "Mountains (Alps) - Habitat Fragmentation"
]
mountains_alps["Land-Use Change"]["Logic Description"] = "Land-use changes, including agricultural abandonment and expansion of infrastructure, are altering alpine landscapes."
mountains_alps["Land-Use Change"]["Impact Function"] = "impact_land_use_change_alps"

mountains_alps["Air Pollution"]["Metric"] = "Concentrations of pollutants (e.g., nitrogen oxides, ozone); deposition of pollutants."
mountains_alps["Air Pollution"]["Data Sources"] = [
 "Air quality monitoring networks.",
    "Research studies."
]
mountains_alps["Air Pollution"]["Impact on Area"] = "Impacts on sensitive vegetation; soil acidification; nutrient imbalances."
mountains_alps["Air Pollution"]["Impact on Biodiversity"] = "Damage to lichens and other sensitive species; changes in plant communities."
mountains_alps["Air Pollution"]["Influenced By"] = [
 "Industrial Emissions (Local and Long-Range Transport)",
    "Vehicle Emissions",
    "Agricultural Practices"
]
mountains_alps["Air Pollution"]["Influences"] = [
    "Mountains (Alps) - Ecosystem Health"
]
mountains_alps["Air Pollution"]["Logic Description"] = "Air pollution, transported from lower elevations and industrial areas, can affect sensitive alpine ecosystems."
mountains_alps["Air Pollution"]["Impact Function"] = "impact_air_pollution_alps"

mountains_alps["Changes in Water Availability"]["Metric"] = "Streamflow; snowpack; groundwater levels."
mountains_alps["Changes in Water Availability"]["Data Sources"] = [
    "Hydrological monitoring networks.",
    "Snowpack measurements.",
     "Mountains (Alps) - Climate Change data"
]
mountains_alps["Changes in Water Availability"]["Impact on Area"] = "Altered streamflow patterns; reduced water availability in some areas; impacts on wetlands."
mountains_alps["Changes in Water Availability"]["Impact on Biodiversity"] = "Impacts on aquatic ecosystems and species; changes in vegetation communities dependent on specific water regimes."
mountains_alps["Changes in Water Availability"]["Influenced By"] = [
 "Mountains (Alps) - Climate Change",
   "Mountains (Alps) - Glacier Retreat",
    "Water Management Practices"
]
mountains_alps["Changes in Water Availability"]["Influences"] = [
  "Mountains (Alps) - Ecosystem Functioning"
]
mountains_alps["Changes in Water Availability"]["Logic Description"] = "Changes in precipitation, snowmelt, and glacier runoff, primarily driven by climate change, are altering water availability in the Alps."
mountains_alps["Changes in Water Availability"]["Impact Function"] = "impact_water_availability_changes_alps"

# --- Mountains (Andes) ---
mountains_andes = all_stressors_data["Andes Mountains"]

mountains_andes["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality); glacier retreat (area, volume); changes in snow cover."
mountains_andes["Climate Change"]["Data Sources"] = [
    "Climate models.",
    "Historical climate records.",
    "Glacier monitoring programs.",
    "National meteorological services of Andean countries.",
    "Research publications."
]
mountains_andes["Climate Change"]["Impact on Area"] = "Indirect; changes in growing conditions, species distributions, water availability, and glacier extent."
mountains_andes["Climate Change"]["Impact on Biodiversity"] = "Shifts in species ranges (upslope migration); increased stress on high-elevation species; loss of glacier-fed habitats; changes in vegetation communities; impacts on unique ecosystems like *páramo* and cloud forests."
mountains_andes["Climate Change"]["Influenced By"] = ["Global GHG"]
mountains_andes["Climate Change"]["Influences"] = [
    "Mountains (Andes) - Glacier Retreat",
    "Mountains (Andes) - Water Availability",
     "Mountains (Andes) - Fire Regimes"
]
mountains_andes["Climate Change"]["Logic Description"] = "The Andes are highly vulnerable to climate change, experiencing rapid warming, glacier retreat, and changes in precipitation patterns. This has significant impacts on biodiversity and water resources."
mountains_andes["Climate Change"]["Impact Function"] = "impact_climate_change_andes"

mountains_andes["Land-Use Change"]["Metric"] = "Area converted to agriculture, pasture, settlements, or infrastructure (ha/year)."
mountains_andes["Land-Use Change"]["Data Sources"] = [
    "Land cover data (from remote sensing and other sources).",
    "Agricultural statistics.",
    "National and regional land-use planning documents.",
     "Census data."
]
mountains_andes["Land-Use Change"]["Impact on Area"] = "Changes in landscape structure and composition; loss of native vegetation; deforestation in lower elevation areas."
mountains_andes["Land-Use Change"]["Impact on Biodiversity"] = "Habitat loss and fragmentation; impacts on species adapted to specific habitats (e.g., cloud forests, *páramo*); loss of traditional land-use practices that maintained biodiversity in some areas."
mountains_andes["Land-Use Change"]["Influenced By"] = [
   "Agricultural Expansion",
   "Population Growth",
    "Urbanization",
    "Mountains (Andes) - Mining"
]
mountains_andes["Land-Use Change"]["Influences"] = [
    "Mountains (Andes) - Habitat Fragmentation",
    "Mountains (Andes) - Overgrazing"
]
mountains_andes["Land-Use Change"]["Logic Description"] = "Land-use change, driven by agriculture, population growth, and infrastructure development, is a major threat to Andean ecosystems."
mountains_andes["Land-Use Change"]["Impact Function"] = "impact_land_use_change_andes"

mountains_andes["Mining"]["Metric"] = "Area disturbed by mining activities (ha/year); water quality parameters in affected areas; volume of tailings produced."
mountains_andes["Mining"]["Data Sources"] = [
   "Mining permits and environmental impact assessments.",
    "Government data on mineral production.",
    "Water quality monitoring data.",
    "Remote Sensing"
]
mountains_andes["Mining"]["Impact on Area"] = "Direct habitat loss; water pollution (heavy metals, acid mine drainage); soil contamination; landscape alteration."
mountains_andes["Mining"]["Impact on Biodiversity"] = "Loss of habitat; impacts on aquatic ecosystems from water pollution; impacts on terrestrial species due to habitat loss and contamination."
mountains_andes["Mining"]["Influenced By"] = [
  "Global Demand for Minerals",
    "Government Policies",
   "Economic Factors"
]
mountains_andes["Mining"]["Influences"] = [
    "Mountains (Andes) - Water Pollution",
     "Mountains (Andes) - Land-Use Change",
   "Mountains (Andes) - Habitat Fragmentation"
]
mountains_andes["Mining"]["Logic Description"] = "Mining, particularly for copper, gold, and other minerals, is a major environmental stressor in the Andes, causing habitat destruction, water pollution, and social conflicts."
mountains_andes["Mining"]["Impact Function"] = "impact_mining_andes"

mountains_andes["Habitat Fragmentation"]["Metric"] = "Patch size distribution; edge density; connectivity indices."
mountains_andes["Habitat Fragmentation"]["Data Sources"] = [
    "Land cover data (from remote sensing and other sources).",
   "GIS analysis."
]
mountains_andes["Habitat Fragmentation"]["Impact on Area"] = "Natural habitats are fragmented by roads, agriculture, mining, and other human activities."
mountains_andes["Habitat Fragmentation"]["Impact on Biodiversity"] = "Reduced gene flow; increased edge effects; limited dispersal ability; increased vulnerability to stochastic events and climate change."
mountains_andes["Habitat Fragmentation"]["Influenced By"] = [
 "Mountains (Andes) - Land-Use Change",
   "Mountains (Andes) - Mining",
   "Infrastructure Development"
]
mountains_andes["Habitat Fragmentation"]["Influences"] = [
    "Exacerbates impacts of other stressors."
]
mountains_andes["Habitat Fragmentation"]["Logic Description"] = "Fragmentation isolates populations and reduces habitat quality, making species more vulnerable to other threats."
mountains_andes["Habitat Fragmentation"]["Impact Function"] = "impact_habitat_fragmentation_andes"

mountains_andes["Glacier Retreat"]["Metric"] = "Glacier area change (km²); glacier volume change (km³); changes in meltwater runoff."
mountains_andes["Glacier Retreat"]["Data Sources"] = [
   "Satellite imagery (e.g., Landsat, ASTER).",
    "Glacier inventories.",
    "Field measurements (e.g., mass balance studies).",
    "Research publications."
]
mountains_andes["Glacier Retreat"]["Impact on Area"] = "Loss of glacier area; changes in downstream water availability."
mountains_andes["Glacier Retreat"]["Impact on Biodiversity"] = "Loss of glacier-fed habitats; impacts on aquatic species adapted to cold, glacier-fed streams; potential for long-term changes in downstream ecosystems."
mountains_andes["Glacier Retreat"]["Influenced By"] = ["Mountains (Andes) - Climate Change"]
mountains_andes["Glacier Retreat"]["Influences"] = [
  "Mountains (Andes) - Water Availability",
   "Mountains (Andes) - Hydrology"
]
mountains_andes["Glacier Retreat"]["Logic Description"] = "Rapid glacier retreat, driven by climate change, is a major concern in the Andes, with significant implications for water resources and biodiversity."
mountains_andes["Glacier Retreat"]["Impact Function"] = "impact_glacier_retreat_andes"

mountains_andes["Overgrazing"]["Metric"] = "Livestock density; vegetation cover; soil erosion rates."
mountains_andes["Overgrazing"]["Data Sources"] = [
   "Agricultural statistics.",
   "Vegetation surveys.",
    "Soil erosion studies.",
   "Research publications."
]
mountains_andes["Overgrazing"]["Impact on Area"] = "Degradation of vegetation; soil erosion; changes in plant community composition."
mountains_andes["Overgrazing"]["Impact on Biodiversity"] = "Loss of palatable plant species; reduced habitat quality for native herbivores; impacts on soil organisms."
mountains_andes["Overgrazing"]["Influenced By"] = [
    "Livestock Management Practices",
  "Land Tenure Systems",
   "Socioeconomic Factors"
]
mountains_andes["Overgrazing"]["Influences"] = [
  "Mountains (Andes) - Soil Erosion",
   "Mountains (Andes) - Vegetation Changes"
]
mountains_andes["Overgrazing"]["Logic Description"] = "Overgrazing by livestock, particularly in high-elevation grasslands and *páramo* ecosystems, can lead to soil degradation and biodiversity loss."
mountains_andes["Overgrazing"]["Impact Function"] = "impact_overgrazing_andes"

mountains_andes["Invasive Species"]["Metric"] = "Abundance and distribution of key invasive species (e.g., certain grasses, trees, and animals)."
mountains_andes["Invasive Species"]["Data Sources"] = [
   "Vegetation surveys.",
    "Research studies.",
    "National and regional invasive species databases."
]
mountains_andes["Invasive Species"]["Impact on Area"] = "Changes in vegetation composition and structure; altered fire regimes in some areas."
mountains_andes["Invasive Species"]["Impact on Biodiversity"] = "Competition with native plants; altered habitat structure; impacts on native fauna."
mountains_andes["Invasive Species"]["Influenced By"] = [
    "Disturbance",
    "Mountains (Andes) - Climate Change",
   "Mountains (Andes) - Land-Use Change",
    "Mountains (Andes) - Introduction"
]
mountains_andes["Invasive Species"]["Influences"] = [
 "Can alter ecosystem processes"
]
mountains_andes["Invasive Species"]["Logic Description"] = "Invasive species, introduced through human activities, can outcompete native species and alter ecosystem dynamics."
mountains_andes["Invasive Species"]["Impact Function"] = "impact_invasive_species_andes"

# --- Mountains (Ethiopian Highlands) ---
mountains_ethiopian_highlands = all_stressors_data["Ethiopian Highlands Mountains"]

mountains_ethiopian_highlands["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality); increased frequency of drought."
mountains_ethiopian_highlands["Climate Change"]["Data Sources"] = [
    "Climate models.",
    "Historical weather records.",
    "Research publications specific to the Ethiopian Highlands."
]
mountains_ethiopian_highlands["Climate Change"]["Impact on Area"] = "Indirect; changes in growing conditions, water availability, and potentially increased aridity."
mountains_ethiopian_highlands["Climate Change"]["Impact on Biodiversity"] = "Shifts in species distributions (upslope); increased stress on high-elevation endemic species; changes in vegetation communities."
mountains_ethiopian_highlands["Climate Change"]["Influenced By"] = ["Global GHG"]
mountains_ethiopian_highlands["Climate Change"]["Influences"] = [
"Mountains (Ethiopian Highlands) - Water Availability",
    "Mountains (Ethiopian Highlands) - Soil Erosion",
"Mountains (Ethiopian Highlands) - Agricultural Productivity"
]
mountains_ethiopian_highlands["Climate Change"]["Logic Description"] = "Climate change is projected to lead to warming temperatures and altered rainfall patterns in the Ethiopian Highlands, increasing stress on ecosystems and impacting water resources."
mountains_ethiopian_highlands["Climate Change"]["Impact Function"] = "impact_climate_change_ethiopian_highlands"

mountains_ethiopian_highlands["Land-Use Change"]["Metric"] = "Area converted to agriculture, settlements, or other land uses (ha/year)."
mountains_ethiopian_highlands["Land-Use Change"]["Data Sources"] = [
    "Remote sensing data.",
    "Government statistics (Ethiopia).",
    "Research publications."
]
mountains_ethiopian_highlands["Land-Use Change"]["Impact on Area"] = "Loss of natural habitats (e.g., Afroalpine grasslands, montane forests); habitat fragmentation."
mountains_ethiopian_highlands["Land-Use Change"]["Impact on Biodiversity"] = "Habitat loss, threatening endemic species (e.g., Ethiopian wolf, Walia ibex); increased human-wildlife conflict."
mountains_ethiopian_highlands["Land-Use Change"]["Influenced By"] = [
    "Mountains (Ethiopian Highlands) - Population Growth",
    "Agricultural Expansion",
    "Lack of Alternative Livelihoods"
]
mountains_ethiopian_highlands["Land-Use Change"]["Influences"] = [
"Mountains (Ethiopian Highlands) - Habitat Fragmentation",
    "Mountains (Ethiopian Highlands) - Soil Erosion"
]
mountains_ethiopian_highlands["Land-Use Change"]["Logic Description"] = "Land-use change, driven by high population density and agricultural expansion, is a *major* threat to the unique ecosystems and endemic biodiversity of the Ethiopian Highlands."
mountains_ethiopian_highlands["Land-Use Change"]["Impact Function"] = "impact_land_use_change_ethiopian_highlands"

mountains_ethiopian_highlands["Soil Erosion"]["Metric"] = "Soil loss rate (tonnes/ha/year); gully formation; sediment load in rivers."
mountains_ethiopian_highlands["Soil Erosion"]["Data Sources"] = [
    "Field measurements (e.g., using erosion pins, sediment traps).",
    "Remote sensing data.",
    "Research publications."
]
mountains_ethiopian_highlands["Soil Erosion"]["Impact on Area"] = "*Severe* soil degradation; reduced land productivity; increased sedimentation in rivers and reservoirs."
mountains_ethiopian_highlands["Soil Erosion"]["Impact on Biodiversity"] = "Loss of soil fertility, impacting plant communities; degradation of water quality, affecting aquatic ecosystems."
mountains_ethiopian_highlands["Soil Erosion"]["Influenced By"] = [
    "Mountains (Ethiopian Highlands) - Deforestation",
    "Mountains (Ethiopian Highlands) - Overgrazing",
    "Mountains (Ethiopian Highlands) - Intensive Agriculture (on steep slopes without conservation practices)",
    "Mountains (Ethiopian Highlands) - Population Growth"
]
mountains_ethiopian_highlands["Soil Erosion"]["Influences"] = [
    "Agricultural Productivity",
    "Water Quality",
        "Reservoir Siltation"
]
mountains_ethiopian_highlands["Soil Erosion"]["Logic Description"] = "Soil erosion is an *extremely severe* problem in the Ethiopian Highlands, driven by deforestation, overgrazing, intensive agriculture on steep slopes, and high population density.  This has led to widespread land degradation and reduced agricultural productivity."
mountains_ethiopian_highlands["Soil Erosion"]["Impact Function"] = "impact_soil_erosion_ethiopian_highlands"

mountains_ethiopian_highlands["Overgrazing"]["Metric"] = "Livestock density (animals/km²); vegetation cover and composition; soil compaction."
mountains_ethiopian_highlands["Overgrazing"]["Data Sources"] = [
    "Agricultural statistics.",
    "Vegetation surveys.",
    "Research publications."
]
mountains_ethiopian_highlands["Overgrazing"]["Impact on Area"] = "Degradation of grasslands and other vegetation; soil erosion; reduced water infiltration."
mountains_ethiopian_highlands["Overgrazing"]["Impact on Biodiversity"] = "Loss of palatable plant species; changes in plant community composition; impacts on wildlife that depend on grasslands."
mountains_ethiopian_highlands["Overgrazing"]["Influenced By"] = [
    "Mountains (Ethiopian Highlands) - Livestock Management Practices",
    "Mountains (Ethiopian Highlands) - Population Growth",
"Land Tenure Systems"
]
mountains_ethiopian_highlands["Overgrazing"]["Influences"] = [
        "Mountains (Ethiopian Highlands) - Soil Erosion",
    "Mountains (Ethiopian Highlands) - Desertification (in some areas)",
    "Mountains (Ethiopian Highlands) - Vegetation Changes"
]
mountains_ethiopian_highlands["Overgrazing"]["Logic Description"] = "Overgrazing by livestock is a widespread problem, contributing to land degradation and soil erosion, particularly in a region with high livestock densities."
mountains_ethiopian_highlands["Overgrazing"]["Impact Function"] = "impact_overgrazing_ethiopian_highlands"

mountains_ethiopian_highlands["Deforestation"]["Metric"] = "Area of forest cleared per year (ha/year); remaining forest cover (%)."
mountains_ethiopian_highlands["Deforestation"]["Data Sources"] = [
"Remote sensing data.",
    "Forest inventory data (limited).",
"Research publications."
]
mountains_ethiopian_highlands["Deforestation"]["Impact on Area"] = "Loss of forest cover; increased soil erosion."
mountains_ethiopian_highlands["Deforestation"]["Impact on Biodiversity"] = "Habitat loss for forest-dwelling species, including endemic species; loss of ecosystem services (e.g., water regulation, carbon sequestration)."
mountains_ethiopian_highlands["Deforestation"]["Influenced By"] = [
"Agricultural Expansion",
"Fuelwood Collection",
"Population Growth",
"Livestock"
]
mountains_ethiopian_highlands["Deforestation"]["Influences"] = [
    "Mountains (Ethiopian Highlands) - Soil Erosion",
    "Mountains (Ethiopian Highlands) - Water Quality",
    "Mountains (Ethiopian Highlands) - Land-Use Change"
]
mountains_ethiopian_highlands["Deforestation"]["Logic Description"] = "Deforestation, driven by agricultural expansion, fuelwood collection, and population growth, has significantly reduced forest cover in the Ethiopian Highlands, leading to habitat loss and increased soil erosion."
mountains_ethiopian_highlands["Deforestation"]["Impact Function"] = "impact_deforestation_ethiopian_highlands"

mountains_ethiopian_highlands["Population Growth"]["Metric"] = "Population density and growth rate."
mountains_ethiopian_highlands["Population Growth"]["Data Sources"] = ["Census Data"]
mountains_ethiopian_highlands["Population Growth"]["Impact on Area"] = "Increased pressure on natural resources."
mountains_ethiopian_highlands["Population Growth"]["Impact on Biodiversity"] = "Indirect through multiple pathways."
mountains_ethiopian_highlands["Population Growth"]["Influenced By"] = ["Socioeconomic factors"]
mountains_ethiopian_highlands["Population Growth"]["Influences"] = [
    "Mountains (Ethiopian Highlands) - Land-Use Change",
    "Mountains (Ethiopian Highlands) - Deforestation",
    "Mountains (Ethiopian Highlands) - Overgrazing",
    "Mountains (Ethiopian Highlands) - Water Extraction"
]
mountains_ethiopian_highlands["Population Growth"]["Logic Description"] = "High population density and growth rate in the Ethiopian Highlands are major underlying drivers of environmental degradation."
mountains_ethiopian_highlands["Population Growth"]["Impact Function"] = "impact_population_growth_ethiopian_highlands"

# --- Mountains (Himalayas) ---
mountains_himalayas = all_stressors_data["Himalayas Mountains"]

mountains_himalayas["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality); glacier retreat (area, volume); changes in snow cover; frequency of extreme weather events."
mountains_himalayas["Climate Change"]["Data Sources"] = [
    "Climate models (global and regional, with downscaling for mountain areas).",
    "Historical temperature and precipitation records (often sparse at high elevations).",
    "Remote sensing data (e.g., measuring snow cover, glacier extent).",
    "Research publications (e.g., from ICIMOD - International Centre for Integrated Mountain Development).",
    "IPCC reports."
]
mountains_himalayas["Climate Change"]["Impact on Area"] = "Indirect, but significant: glacier retreat, changes in snowpack, shifts in vegetation zones, increased risk of extreme events."
mountains_himalayas["Climate Change"]["Impact on Biodiversity"] = "Upslope shifts in species distributions; increased stress on high-elevation species; loss of glacier-fed habitats; changes in vegetation communities; increased risk of extreme events (floods, droughts)."
mountains_himalayas["Climate Change"]["Influenced By"] = [
        "Global Greenhouse Gas Emissions",
        "Mountains (Himalayas) - Black Carbon Deposition"
]
mountains_himalayas["Climate Change"]["Influences"] = [
       "Mountains (Himalayas) - Glacier Retreat",
       "Mountains (Himalayas) - Changes in Water Availability",
      "Mountains (Himalayas) - Extreme Weather Events"
]
mountains_himalayas["Climate Change"]["Logic Description"] = "The Himalayas are warming rapidly, leading to glacier retreat, changes in snowpack, and altered precipitation patterns. This has profound implications for water resources, biodiversity, and hazard risks."
mountains_himalayas["Climate Change"]["Impact Function"] = "impact_climate_change_himalayas"

mountains_himalayas["Land-Use Change"]["Metric"] = "Area converted to agriculture, pasture, settlements, or other land uses (ha/year); road density (km/km²)."
mountains_himalayas["Land-Use Change"]["Data Sources"] = [
    "Remote sensing data.",
        "Land cover maps.",
    "Government statistics (various Himalayan countries/regions).",
    "Research publications."
]
mountains_himalayas["Land-Use Change"]["Impact on Area"] = "Habitat loss and fragmentation (particularly in lower elevation areas); deforestation."
mountains_himalayas["Land-Use Change"]["Impact on Biodiversity"] = "Habitat loss and fragmentation; impacts on species adapted to specific habitats; increased human-wildlife conflict."
mountains_himalayas["Land-Use Change"]["Influenced By"] = [
        "Population Growth",
        "Agricultural Expansion",
       "Infrastructure Development",
        "Tourism"
]
mountains_himalayas["Land-Use Change"]["Influences"] = [
   "Mountains (Himalayas) - Habitat Fragmentation",
    "Mountains (Himalayas) - Soil Erosion"
]
mountains_himalayas["Land-Use Change"]["Logic Description"] = "Land-use change, driven by population growth, agriculture, and infrastructure development, is leading to habitat loss and fragmentation, particularly in the lower elevations of the Himalayas."
mountains_himalayas["Land-Use Change"]["Impact Function"] = "impact_land_use_change_himalayas"

mountains_himalayas["Overgrazing"]["Metric"] = "Livestock density (animals/km²); vegetation cover and composition; soil erosion."
mountains_himalayas["Overgrazing"]["Data Sources"] = [
     "Livestock censuses.",
    "Vegetation surveys.",
    "Research publications."
]
mountains_himalayas["Overgrazing"]["Impact on Area"] = "Degradation of grasslands and other vegetation; soil erosion; reduced water infiltration."
mountains_himalayas["Overgrazing"]["Impact on Biodiversity"] = "Loss of palatable plant species; changes in plant community composition; impacts on wildlife that depend on grasslands."
mountains_himalayas["Overgrazing"]["Influenced By"] = [
 "Livestock Management Practices",
    "Population Growth (of livestock and humans)"
]
mountains_himalayas["Overgrazing"]["Influences"] = [
     "Mountains (Himalayas) - Soil Erosion",
   "Mountains (Himalayas) - Vegetation Changes"
]
mountains_himalayas["Overgrazing"]["Logic Description"] = "Overgrazing by livestock, particularly in high-altitude pastures, is a significant problem, leading to vegetation degradation and soil erosion."
mountains_himalayas["Overgrazing"]["Impact Function"] = "impact_overgrazing_himalayas"

mountains_himalayas["Deforestation"]["Metric"] = "Area of forest cleared per year (ha/year); changes in forest cover."
mountains_himalayas["Deforestation"]["Data Sources"] = [
   "Remote sensing data.",
  "Forest inventory data (often limited).",
    "Research publications."
]
mountains_himalayas["Deforestation"]["Impact on Area"] = "Loss of forest cover; increased soil erosion; landslides."
mountains_himalayas["Deforestation"]["Impact on Biodiversity"] = "Habitat loss for forest-dwelling species; loss of ecosystem services (e.g., water regulation, carbon sequestration)."
mountains_himalayas["Deforestation"]["Influenced By"] = [
    "Fuelwood Collection",
  "Timber Harvesting (legal and illegal)",
   "Agricultural Expansion",
    "Infrastructure Development"
]
mountains_himalayas["Deforestation"]["Influences"] = [
    "Mountains (Himalayas) - Soil Erosion",
   "Mountains (Himalayas) - Water Quality",
  "Mountains (Himalayas) - Landslides"
]
mountains_himalayas["Deforestation"]["Logic Description"] = "Deforestation, driven by fuelwood collection, timber harvesting, and agricultural expansion, is a significant threat to Himalayan forests."
mountains_himalayas["Deforestation"]["Impact Function"] = "impact_deforestation_himalayas"

mountains_himalayas["Tourism"]["Metric"] = "Number of tourists visiting the region; area of infrastructure development related to tourism (e.g., hotels, trails)."
mountains_himalayas["Tourism"]["Data Sources"] = [
   "Tourism statistics (from government agencies and tourism operators).",
  "Remote sensing data.",
   "Research studies."
]
mountains_himalayas["Tourism"]["Impact on Area"] = "Localized habitat disturbance; pollution (solid waste, sewage); pressure on water resources."
mountains_himalayas["Tourism"]["Impact on Biodiversity"] = "Disturbance to wildlife (especially in sensitive areas); habitat degradation; introduction of invasive species."
mountains_himalayas["Tourism"]["Influenced By"] = [
   "Accessibility (roads, airports)",
 "Economic Opportunities",
  "Marketing and Promotion"
]
mountains_himalayas["Tourism"]["Influences"] = [
 "Mountains (Himalayas) - Pollution",
     "Mountains (Himalayas) - Habitat Disturbance"
]
mountains_himalayas["Tourism"]["Logic Description"] = "Tourism, while providing economic benefits, can also have negative impacts on fragile Himalayan ecosystems if not managed sustainably."
mountains_himalayas["Tourism"]["Impact Function"] = "impact_tourism_himalayas"

mountains_himalayas["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., air pollutants, heavy metals, plastic waste) in air, water, soil, and biota."
mountains_himalayas["Pollution"]["Data Sources"] = [
   "Air and water quality monitoring data (often limited).",
    "Research studies."
]
mountains_himalayas["Pollution"]["Impact on Area"] = "Degradation of air, water, and soil quality."
mountains_himalayas["Pollution"]["Impact on Biodiversity"] = "Toxic effects on wildlife and plants; impacts on aquatic ecosystems; bioaccumulation of pollutants."
mountains_himalayas["Pollution"]["Influenced By"] = [
   "Mountains (Himalayas) - Tourism",
    "Urbanization (in some areas)",
    "Industrial Activities (in some areas)",
   "Long-Range Transport of Pollutants",
    "Mining Activities"
]
mountains_himalayas["Pollution"]["Influences"] = [
    "Mountains (Himalayas) - Water Quality",
    "Mountains (Himalayas) - Wildlife Health"
]
mountains_himalayas["Pollution"]["Logic Description"] = "Pollution from various sources, including tourism, urbanization, industry, and long-range transport, is a growing concern in the Himalayas."
mountains_himalayas["Pollution"]["Impact Function"] = "impact_pollution_himalayas"

mountains_himalayas["Glacier Retreat"]["Metric"] = "Change in glacier area (km²) and volume (km³); changes in meltwater runoff; mass balance."
mountains_himalayas["Glacier Retreat"]["Data Sources"] = [
   "Remote sensing data (satellite imagery).",
    "Field measurements (glaciological studies).",
    "Research publications (e.g., from ICIMOD).",
     "Climate models."
]
mountains_himalayas["Glacier Retreat"]["Impact on Area"] = "*Extensive* glacier loss; changes in river flow; increased risk of glacial lake outburst floods (GLOFs)."
mountains_himalayas["Glacier Retreat"]["Impact on Biodiversity"] = "Changes in downstream water availability and temperature, impacting aquatic ecosystems; loss of glacier-fed habitats; impacts on downstream wetlands and floodplains."
mountains_himalayas["Glacier Retreat"]["Influenced By"] = [
   "Mountains (Himalayas) - Climate Change",
   "Mountains (Himalayas) - Black Carbon Deposition"
]
mountains_himalayas["Glacier Retreat"]["Influences"] = [
   "Mountains (Himalayas) - Water Resources",
     "Mountains (Himalayas) - Hazard Risks (GLOFs)",
      "Mountains (Himalayas) - Hydrology"
]
mountains_himalayas["Glacier Retreat"]["Logic Description"] = "The Himalayas are experiencing rapid glacier retreat due to climate change and black carbon deposition. This is a *critical* threat to water resources for millions of people downstream and increases the risk of catastrophic glacial lake outburst floods."
mountains_himalayas["Glacier Retreat"]["Impact Function"] = "impact_glacier_retreat_himalayas"

mountains_himalayas["Black Carbon Deposition"]["Metric"] = "Concentration of black carbon in snow and ice; changes in albedo."
mountains_himalayas["Black Carbon Deposition"]["Data Sources"] = [
   "Field measurements on glaciers.",
    "Atmospheric monitoring.",
   "Research publications."
]
mountains_himalayas["Black Carbon Deposition"]["Impact on Area"] = "Accelerates glacier and snow melt."
mountains_himalayas["Black Carbon Deposition"]["Impact on Biodiversity"] = "Indirect, through impacts on glacier retreat and water resources."
mountains_himalayas["Black Carbon Deposition"]["Influenced By"] = [
    "Combustion of Fossil Fuels (in South Asia and other regions)",
    "Biomass Burning (e.g., cooking fires, agricultural burning)"
]
mountains_himalayas["Black Carbon Deposition"]["Influences"] = [
   "Mountains (Himalayas) - Glacier Retreat"
]
mountains_himalayas["Black Carbon Deposition"]["Logic Description"] = "Black carbon (soot) deposition on snow and ice darkens the surface, increasing absorption of solar radiation and accelerating melting. This is a significant contributor to glacier retreat in the Himalayas."
mountains_himalayas["Black Carbon Deposition"]["Impact Function"] = "impact_black_carbon_deposition_himalayas"

# --- Mountains (Rocky) ---
mountains_rocky = all_stressors_data["Rocky Mountains"]

mountains_rocky["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality); snowpack depth and duration; glacier extent (where applicable)."
mountains_rocky["Climate Change"]["Data Sources"] = [
    "Climate models (global and regional, downscaled).",
    "Historical climate records (weather stations).",
    "SNOTEL data (snowpack measurements).",
    "USGS glacier monitoring data (where applicable).",
    "Research publications."
]
mountains_rocky["Climate Change"]["Impact on Area"] = "Indirect; changes in growing conditions, water availability, fire risk, and species distributions."
mountains_rocky["Climate Change"]["Impact on Biodiversity"] = "Upslope shifts in species distributions; increased stress on high-elevation and cold-adapted species (e.g., pika, whitebark pine); changes in forest composition; increased risk of wildfires."
mountains_rocky["Climate Change"]["Influenced By"] = ["Global GHG"]
mountains_rocky["Climate Change"]["Influences"] = [
    "Mountains (Rocky) - Water Availability",
    "Mountains (Rocky) - Fire Regimes",
        "Mountains (Rocky) - Insect Outbreaks",
        "Mountains (Rocky) - Snowpack"
]
mountains_rocky["Climate Change"]["Logic Description"] = "The Rocky Mountains are experiencing warming temperatures, reduced snowpack, and altered precipitation patterns. This is leading to changes in ecosystems and increasing the risk of wildfires and insect outbreaks."
mountains_rocky["Climate Change"]["Impact Function"] = "impact_climate_change_rocky"

mountains_rocky["Land-Use Change"]["Metric"] = "Area converted to urban development, agriculture, resource extraction (e.g., oil and gas), or other uses (ha/year); road density (km/km²)."
mountains_rocky["Land-Use Change"]["Data Sources"] = [
    "USGS National Land Cover Database (NLCD).",
    "Land-use planning documents (county and state level).",
    "Remote sensing data.",
    "Research publications."
]
mountains_rocky["Land-Use Change"]["Impact on Area"] = "Habitat loss and fragmentation; impacts on wildlife corridors; changes in land cover."
mountains_rocky["Land-Use Change"]["Impact on Biodiversity"] = "Habitat loss and fragmentation; disruption of wildlife migration; increased human-wildlife conflict."
mountains_rocky["Land-Use Change"]["Influenced By"] = [
    "Population Growth",
    "Urban Sprawl",
    "Resource Extraction (mining, oil and gas)",
    "Agricultural Expansion (in some areas)"
]
mountains_rocky["Land-Use Change"]["Influences"] = [
    "Mountains (Rocky) - Habitat Fragmentation",
    "Mountains (Rocky) - Water Use"
]
mountains_rocky["Land-Use Change"]["Logic Description"] = "Land-use change, particularly from urban development and resource extraction, is fragmenting habitats and impacting wildlife in the Rocky Mountains."
mountains_rocky["Land-Use Change"]["Impact Function"] = "impact_land_use_change_rocky"

mountains_rocky["Fire Suppression"]["Metric"] = "Fire return interval (years); fuel load (biomass/area); forest density; area burned (ha/year)."
mountains_rocky["Fire Suppression"]["Data Sources"] = [
    "US Forest Service data.",
    "National Park Service data.",
    "State forestry agency data.",
    "Fire history studies (e.g., tree-ring data).",
    "Remote sensing data."
]
mountains_rocky["Fire Suppression"]["Impact on Area"] = "Increased forest density; accumulation of fuels; altered forest structure and composition."
mountains_rocky["Fire Suppression"]["Impact on Biodiversity"] = "Increased risk of large, high-severity wildfires; loss of fire-dependent species; changes in habitat structure. Can negatively or positively impact, context specific."
mountains_rocky["Fire Suppression"]["Influenced By"] = [
    "Past and Current Forest Management Practices",
    "Human Settlement Patterns"
]
mountains_rocky["Fire Suppression"]["Influences"] = [
    "Mountains (Rocky) - Fire Regimes (increased severity)",
    "Mountains (Rocky) - Forest Structure and Composition"
]
mountains_rocky["Fire Suppression"]["Logic Description"] = "Decades of fire suppression have led to an unnatural buildup of fuels in many Rocky Mountain forests, increasing the risk of large, severe wildfires."
mountains_rocky["Fire Suppression"]["Impact Function"] = "impact_fire_suppression_rocky"

mountains_rocky["Mining"]["Metric"] = "Area disturbed by mining activities (ha); water quality parameters in affected areas; volume of tailings produced."
mountains_rocky["Mining"]["Data Sources"] = [
    "Mining permits and environmental impact statements.",
    "USGS mineral resource data.",
    "State agency data (e.g., departments of mining, environment).",
    "Water quality monitoring data."
]
mountains_rocky["Mining"]["Impact on Area"] = "Habitat destruction; water pollution (heavy metals, acid mine drainage); soil contamination; landscape alteration."
mountains_rocky["Mining"]["Impact on Biodiversity"] = "Loss of habitat; impacts on aquatic ecosystems from water pollution; impacts on terrestrial species due to habitat loss and contamination."
mountains_rocky["Mining"]["Influenced By"] = [
    "Demand for Minerals",
    "Government Regulations",
    "Economic Factors"
]
mountains_rocky["Mining"]["Influences"] = [
    "Mountains (Rocky) - Water Pollution",
    "Mountains (Rocky) - Habitat Loss",
    "Mountains (Rocky) - Land-Use Change"
]
mountains_rocky["Mining"]["Logic Description"] = "Mining, both historical and current, has had significant environmental impacts in the Rocky Mountains, particularly on water quality and habitat."
mountains_rocky["Mining"]["Impact Function"] = "impact_mining_rocky"

mountains_rocky["Recreation and Tourism"]["Metric"] = "Number of visitors to parks and protected areas; area of developed recreation infrastructure (e.g., trails, ski areas); vehicle traffic."
mountains_rocky["Recreation and Tourism"]["Data Sources"] = [
    "National Park Service visitor statistics.",
    "US Forest Service data.",
    "State park data.",
    "Ski area data.",
    "Research studies."
]
mountains_rocky["Recreation and Tourism"]["Impact on Area"] = "Localized habitat disturbance; soil compaction; trail erosion; wildlife disturbance."
mountains_rocky["Recreation and Tourism"]["Impact on Biodiversity"] = "Disturbance to wildlife (especially during breeding seasons); habitat degradation; introduction of invasive species."
mountains_rocky["Recreation and Tourism"]["Influenced By"] = [
"Accessibility",
"Economic Opportunities",
    "Marketing and Promotion"
]
mountains_rocky["Recreation and Tourism"]["Influences"] = [
"Mountains (Rocky) - Habitat Disturbance",
"Mountains (Rocky) - Wildlife Impacts"
]
mountains_rocky["Recreation and Tourism"]["Logic Description"] = "High levels of recreation and tourism, while economically important, can put pressure on sensitive mountain ecosystems."
mountains_rocky["Recreation and Tourism"]["Impact Function"] = "impact_recreation_tourism_rocky"

mountains_rocky["Invasive Species"]["Metric"] = "Abundance and distribution of key invasive species (e.g., cheatgrass, knapweed, white pine blister rust)."
mountains_rocky["Invasive Species"]["Data Sources"] = [
    "Vegetation surveys.",
    "Forest health monitoring data.",
    "Research studies.",
    "Land management agency data."
]
mountains_rocky["Invasive Species"]["Impact on Area"] = "Changes in vegetation composition and structure; altered fire regimes (e.g., cheatgrass); impacts on forest health (e.g., white pine blister rust)."
mountains_rocky["Invasive Species"]["Impact on Biodiversity"] = "Competition with native plants; altered habitat structure; reduced resources for native fauna; increased tree mortality (for some invasive pathogens)."
mountains_rocky["Invasive Species"]["Influenced By"] = [
    "Disturbance (e.g., fire, logging, grazing)",
    "Climate Change",
    "Introduction (intentional or accidental)"
]
mountains_rocky["Invasive Species"]["Influences"] = [
"Mountains (Rocky) - Ecosystem Processes",
    "Mountains (Rocky) - Fire Regimes"
]
mountains_rocky["Invasive Species"]["Logic Description"] = "Invasive species are altering ecosystems, increasing fire risk in some areas, and impacting native biodiversity."
mountains_rocky["Invasive Species"]["Impact Function"] = "impact_invasive_species_rocky"

mountains_rocky["Air Pollution"]["Metric"] = "Concentrations of pollutants (e.g., ozone, nitrogen oxides, particulate matter) in air and precipitation; deposition rates."
mountains_rocky["Air Pollution"]["Data Sources"] = [
    "Air quality monitoring networks (e.g., EPA's Clean Air Status and Trends Network - CASTNET).",
    "National Park Service air quality data.",
    "Research studies."
]
mountains_rocky["Air Pollution"]["Impact on Area"] = "Reduced visibility; impacts on sensitive vegetation; soil and water acidification (in some areas); nutrient imbalances."
mountains_rocky["Air Pollution"]["Impact on Biodiversity"] = "Damage to sensitive plant species; changes in plant community composition; impacts on aquatic ecosystems."
mountains_rocky["Air Pollution"]["Influenced By"] = [
    "Industrial Emissions (local and long-range transport)",
    "Vehicle Emissions",
    "Agricultural Activities",
    "Urban Areas"
]
mountains_rocky["Air Pollution"]["Influences"] = [
"Mountains (Rocky) - Ecosystem Health",
    "Mountains (Rocky) - Water Quality"
]
mountains_rocky["Air Pollution"]["Logic Description"] = "Air pollution, originating from both local and distant sources, can impact high-elevation ecosystems in the Rocky Mountains."
mountains_rocky["Air Pollution"]["Impact Function"] = "impact_air_pollution_rocky"

# --- Tundra (Alpine) ---
tundra_alpine = all_stressors_data["Alpine Tundra"]

tundra_alpine["Temperature Increase"]["Metric"] = "Average Annual Temperature Increase (°C)"
tundra_alpine["Temperature Increase"]["Data Sources"] = [
    "Climate Models.",
    "Historical Records (mountain weather stations)."
]
tundra_alpine["Temperature Increase"]["Impact on Area"] = "Indirect; changes in snowpack, glacier retreat."
tundra_alpine["Temperature Increase"]["Impact on Biodiversity"] = "Species shifts (upslope).; Increased stress.; Phenology changes.; Increased risk of extinction for high-elevation specialists."
tundra_alpine["Temperature Increase"]["Influenced By"] = [
    "Global GHG emissions."
]
tundra_alpine["Temperature Increase"]["Influences"] = [
    "Tundra (Alpine) - Changes in Precipitation",
    "Tundra (Alpine) - Glacier Retreat",
    "Tundra (Alpine) - Snowpack"
]
tundra_alpine["Temperature Increase"]["Logic Description"] = "Similar to Arctic Tundra, but with even greater risk of species extinctions due to limited 'upward' movement. \"Mountain top extinction.\""
tundra_alpine["Temperature Increase"]["Impact Function"] = "impact_temperature_increase_alpine_tundra"

tundra_alpine["Changes in Precipitation"]["Metric"] = "change in annual precipitation, snowpack"
tundra_alpine["Changes in Precipitation"]["Data Sources"] = [
"Climate Models",
    "Historical Records"
]
tundra_alpine["Changes in Precipitation"]["Impact on Area"] = "Indirect - water"
tundra_alpine["Changes in Precipitation"]["Impact on Biodiversity"] = "Changes in vegetation; Altered streamflow."
tundra_alpine["Changes in Precipitation"]["Influenced By"] = [
    "Global GHG"
]
tundra_alpine["Changes in Precipitation"]["Influences"] = [
    "Tundra (Alpine) - Water Availability"
]
tundra_alpine["Changes in Precipitation"]["Logic Description"] = "Changes in snowpack are particularly critical, affecting water availability throughout the year."
tundra_alpine["Changes in Precipitation"]["Impact Function"] = "impact_precipitation_changes_alpine_tundra"

tundra_alpine["Infrastructure Development"]["Metric"] = "Road density; area affected by ski resorts, tourism, etc."
tundra_alpine["Infrastructure Development"]["Data Sources"] = [
    "Government statistics",
    "Remote sensing"
]
tundra_alpine["Infrastructure Development"]["Impact on Area"] = "Habitat fragmentation; direct loss."
tundra_alpine["Infrastructure Development"]["Impact on Biodiversity"] = "Habitat loss and fragmentation; Disturbance"
tundra_alpine["Infrastructure Development"]["Influenced By"] = [
    "Economic growth (tourism).",
    "Government policies."
]
tundra_alpine["Infrastructure Development"]["Influences"] = [
    "Tundra (Alpine) - Localized Pollution",
    "Tundra (Alpine) - Invasive Species"
]
tundra_alpine["Infrastructure Development"]["Logic Description"] = "Tourism and recreation infrastructure (ski resorts, roads) are major drivers of habitat loss and fragmentation."
tundra_alpine["Infrastructure Development"]["Impact Function"] = "impact_infrastructure_development_alpine_tundra"

tundra_alpine["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., nitrogen, heavy metals) in air, water, soil, and biota."
tundra_alpine["Pollution"]["Data Sources"] = [
"Environmental monitoring programs.",
    "Research studies."
]
tundra_alpine["Pollution"]["Impact on Area"] = "Contamination."
tundra_alpine["Pollution"]["Impact on Biodiversity"] = "Toxic effects on wildlife and plants.; Reduced reproductive success."
tundra_alpine["Pollution"]["Influenced By"] = [
    "Tundra (Alpine) - Long-Range Transport of Pollutants",
    "Tundra (Alpine) - Local Sources"
]
tundra_alpine["Pollution"]["Influences"] = [
    "Tundra (Alpine) - Wildlife Health",
    "Tundra (Alpine) - Water Quality"
]
tundra_alpine["Pollution"]["Logic Description"] = "Similar to Arctic Tundra, with both long-range and local sources of pollution. Nitrogen deposition from air pollution is a particular concern in some areas."
tundra_alpine["Pollution"]["Impact Function"] = "impact_pollution_alpine_tundra"

tundra_alpine["Overgrazing"]["Metric"] = "Livestock density; vegetation cover and composition."
tundra_alpine["Overgrazing"]["Data Sources"] = [
"Agricultural statistics.",
"Vegetation surveys."
]
tundra_alpine["Overgrazing"]["Impact on Area"] = "Changes in vegetation; soil erosion."
tundra_alpine["Overgrazing"]["Impact on Biodiversity"] = "Loss of palatable plant species.; Spread of unpalatable or invasive species.; Soil Compaction"
tundra_alpine["Overgrazing"]["Influenced By"] = [
        "Tundra (Alpine) - Livestock Management Practices"
]
tundra_alpine["Overgrazing"]["Influences"] = [
    "Tundra (Alpine) - Vegetation Changes"
]
tundra_alpine["Overgrazing"]["Logic Description"] = "Overgrazing by livestock (sheep, goats, cattle) can damage fragile alpine vegetation and lead to soil erosion. This is more of a concern in some mountain ranges than others."
tundra_alpine["Overgrazing"]["Impact Function"] = "impact_overgrazing_alpine_tundra"

tundra_alpine["Invasive Species"]["Metric"] = "Distribution and abundance of invasive species (plants, insects, etc.)."
tundra_alpine["Invasive Species"]["Data Sources"] = [
    "Research studies.",
"Monitoring programs (where they exist)."
]
tundra_alpine["Invasive Species"]["Impact on Area"] = "Potential for changes in vegetation composition."
tundra_alpine["Invasive Species"]["Impact on Biodiversity"] = "Competition with native species.; Alteration of ecosystem processes."
tundra_alpine["Invasive Species"]["Influenced By"] = [
"Tundra (Alpine) - Climate Change",
"Tundra (Alpine) - Disturbance",
    "Increased Human activity"
]
tundra_alpine["Invasive Species"]["Influences"] = [
"Tundra (Alpine) - Native Communities"
]
tundra_alpine["Invasive Species"]["Logic Description"] = "While currently less of a widespread problem than in many other biomes, invasive species pose an increasing threat as the climate warms."
tundra_alpine["Invasive Species"]["Impact Function"] = "impact_invasive_species_alpine_tundra"

# --- Tundra (Arctic) ---
tundra_arctic = all_stressors_data["Arctic Tundra"]

tundra_arctic["Infrastructure Development"]["Metric"] = "Road density (km/km²); area affected by resource extraction (oil, gas, mining) (ha/year); area affected by settlements and other infrastructure (ha/year)."
tundra_arctic["Infrastructure Development"]["Data Sources"] = [
    "Government statistics (national and regional).",
    "Remote sensing data.",
    "Industry reports.",
     "Research publications."
]
tundra_arctic["Infrastructure Development"]["Impact on Area"] = "Habitat fragmentation; direct loss of habitat due to resource extraction and infrastructure; permafrost degradation."
tundra_arctic["Infrastructure Development"]["Impact on Biodiversity"] = "Habitat loss and fragmentation.; Disruption of migration routes (e.g., caribou).; Disturbance to breeding and nesting sites (e.g., birds).; Pollution from resource extraction activities.; Increased human presence and activity."
tundra_arctic["Infrastructure Development"]["Influenced By"] = [
    "Tundra (Arctic) - Economic Growth",
   "Tundra (Arctic) - Geopolitical Factors",
    "Tundra (Arctic) - Government Policies",
   "Tundra (Arctic) - Global Commodity Prices",
   "Tundra (Arctic) - Technological Advancements"
]
tundra_arctic["Infrastructure Development"]["Influences"] = [
    "Tundra (Arctic) - Permafrost Thaw",
   "Tundra (Arctic) - Pollution",
    "Tundra (Arctic) - Wildlife disturbance"
]
tundra_arctic["Infrastructure Development"]["Logic Description"] = "Infrastructure development, primarily related to resource extraction, fragments the fragile tundra landscape, disrupts wildlife, and can accelerate permafrost thaw. The impacts can be long-lasting due to the slow recovery rates of tundra ecosystems."
tundra_arctic["Infrastructure Development"]["Impact Function"] = "impact_infrastructure_development_arctic_tundra"

tundra_arctic["Temperature Increase"]["Metric"] = "Average annual temperature increase (°C) (warming is occurring at a much faster rate in the Arctic than the global average - \"Arctic Amplification\")."
tundra_arctic["Temperature Increase"]["Data Sources"] = [
   "Climate models (global and regional).",
     "Historical temperature records (from weather stations and ice cores).",
  "Remote sensing data (e.g., measuring surface temperature)."
]
tundra_arctic["Temperature Increase"]["Impact on Area"] = "Indirect; widespread permafrost thaw; changes in vegetation cover."
tundra_arctic["Temperature Increase"]["Impact on Biodiversity"] = "Shifts in species distributions (northward and upslope, with boreal species encroaching on tundra).; Increased stress on cold-adapted species.; Changes in phenology (timing of biological events, e.g., plant flowering, insect emergence, bird migration).; Increased risk of shrubification (expansion of shrubs into tundra).; Changes in snow cover, affecting insulation and albedo (reflectivity).; Increased decomposition rates, leading to greenhouse gas release."
tundra_arctic["Temperature Increase"]["Influenced By"] = [
    "Global Greenhouse Gas Emissions",
     "Tundra (Arctic) - Loss of Sea Ice",
  "Tundra (Arctic) - Permafrost Thaw"
]
tundra_arctic["Temperature Increase"]["Influences"] = [
 "Tundra (Arctic) - Permafrost Thaw",
 "Tundra (Arctic) - Changes in Precipitation",
  "Tundra (Arctic) - Sea Ice Loss",
  "Tundra (Arctic) - Shrubification"
]
tundra_arctic["Temperature Increase"]["Logic Description"] = "Rapid warming in the Arctic, driven by global greenhouse gas emissions and amplified by feedback loops (sea ice loss, permafrost thaw), is causing profound changes to the tundra ecosystem, including shifts in species distributions, permafrost degradation, and changes in vegetation cover."
tundra_arctic["Temperature Increase"]["Impact Function"] = "impact_temperature_increase_arctic_tundra"

tundra_arctic["Changes in Precipitation"]["Metric"] = "Change in annual precipitation (mm/year); changes in snowfall amount and timing; changes in rain-on-snow events."
tundra_arctic["Changes in Precipitation"]["Data Sources"] = [
  "Climate models.",
     "Historical weather records.",
  "Remote sensing (e.g., measuring snow cover)."
]
tundra_arctic["Changes in Precipitation"]["Impact on Area"] = "Indirect; changes in snow cover, permafrost, and hydrology."
tundra_arctic["Changes in Precipitation"]["Impact on Biodiversity"] = "Changes in vegetation composition (favoring species adapted to wetter or drier conditions). Impacts on animal populations that depend on snow cover for insulation or foraging (e.g., lemmings, caribou).; Changes in the timing and extent of snowmelt, affecting water availability.; Increased frequency of rain-on-snow events, which can create ice layers that prevent animals from accessing food."
tundra_arctic["Changes in Precipitation"]["Influenced By"] = [
 "Global Greenhouse Gas Emissions",
   "Tundra (Arctic) - Temperature Increase"
]
tundra_arctic["Changes in Precipitation"]["Influences"] = [
     "Tundra (Arctic) - Permafrost Thaw",
  "Tundra (Arctic) - Vegetation Changes",
   "Tundra (Arctic) - Wildlife populations"
]
tundra_arctic["Changes in Precipitation"]["Logic Description"] = "Changes in precipitation patterns, including changes in the amount and timing of snowfall and rainfall, as well as increased rain-on-snow events, impact snow cover, permafrost, hydrology, and vegetation, with cascading effects on wildlife."
tundra_arctic["Changes in Precipitation"]["Impact Function"] = "impact_precipitation_changes_arctic_tundra"

tundra_arctic["Permafrost Thaw"]["Metric"] = "Active layer thickness (cm); area of permafrost degradation (ha); ground subsidence (cm); thermokarst lake formation (area, number)."
tundra_arctic["Permafrost Thaw"]["Data Sources"] = [
    "Field measurements (e.g., using probes to measure active layer thickness).",
 "Remote sensing (e.g., using radar to measure ground subsidence).",
   "Climate models.",
   "Geographic Information Systems (GIS) analysis."
]
tundra_arctic["Permafrost Thaw"]["Impact on Area"] = "Changes in ground stability; altered hydrology; release of greenhouse gases; formation of thermokarst lakes."
tundra_arctic["Permafrost Thaw"]["Impact on Biodiversity"] = "Changes in vegetation composition (e.g., shift from dry tundra to wetlands).; Loss of habitat for some species and creation of new habitat for others.; Impacts on infrastructure (roads, buildings, pipelines).; Release of methane and carbon dioxide (positive feedback to climate change).; Changes in water quality in lakes and rivers."
tundra_arctic["Permafrost Thaw"]["Influenced By"] = [
   "Tundra (Arctic) - Temperature Increase",
  "Tundra (Arctic) - Changes in Precipitation",
   "Tundra (Arctic) - Wildfires",
    "Tundra (Arctic) - Infrastructure Development"
]
tundra_arctic["Permafrost Thaw"]["Influences"] = [
  "Global Climate Change",
 "Tundra (Arctic) - Hydrology",
   "Tundra (Arctic) - Vegetation Changes",
  "Tundra (Arctic) - Coastal Erosion"
]
tundra_arctic["Permafrost Thaw"]["Logic Description"] = "Permafrost thaw, driven primarily by warming temperatures, is a major and widespread stressor in the Arctic Tundra. It leads to ground instability, altered hydrology, the release of large amounts of greenhouse gases (methane and carbon dioxide), and changes in vegetation, creating a positive feedback loop that accelerates climate change."
tundra_arctic["Permafrost Thaw"]["Impact Function"] = "impact_permafrost_thaw_arctic_tundra"

tundra_arctic["Sea Ice Loss (indirect)"]["Metric"] = "Sea ice extent (million km²); sea ice thickness (m); sea ice duration (days)."
tundra_arctic["Sea Ice Loss (indirect)"]["Data Sources"] = [
 "Satellite observations (e.g., from the National Snow and Ice Data Center - NSIDC).",
  "Climate models."
]
tundra_arctic["Sea Ice Loss (indirect)"]["Impact on Area"] = "Primarily impacts coastal tundra ecosystems; also influences regional climate."
tundra_arctic["Sea Ice Loss (indirect)"]["Impact on Biodiversity"] = "Impacts on marine mammals (e.g., polar bears, seals) that depend on sea ice for hunting and breeding.; Changes in coastal erosion rates.; Indirect impacts on terrestrial species through altered climate patterns.; Increased human access to coastal areas (e.g., for shipping, resource extraction)."
tundra_arctic["Sea Ice Loss (indirect)"]["Influenced By"] = [
      "Tundra (Arctic) - Temperature Increase",
   "Tundra (Arctic) - Changes in Ocean Currents"
]
tundra_arctic["Sea Ice Loss (indirect)"]["Influences"] = [
   "Tundra (Arctic) - Regional Climate",
  "Tundra (Arctic) - Coastal Erosion",
   "Marine Ecosystems (impacts extend beyond the tundra)."
]
tundra_arctic["Sea Ice Loss (indirect)"]["Logic Description"] = "Sea ice loss, while primarily affecting marine ecosystems, has significant indirect impacts on coastal tundra ecosystems and influences regional climate patterns, further exacerbating warming."
tundra_arctic["Sea Ice Loss (indirect)"]["Impact Function"] = "impact_sea_ice_loss_arctic_tundra"

tundra_arctic["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., heavy metals, persistent organic pollutants (POPs), oil) in air, water, soil, and biota."
tundra_arctic["Pollution"]["Data Sources"] = [
 "Environmental monitoring programs (e.g., Arctic Monitoring and Assessment Programme - AMAP).",
   "Research studies."
]
tundra_arctic["Pollution"]["Impact on Area"] = "Contamination of soil, water, and air."
tundra_arctic["Pollution"]["Impact on Biodiversity"] = "Toxic effects on wildlife (e.g., bioaccumulation of pollutants in the food chain).; Reduced reproductive success.; Increased susceptibility to disease."
tundra_arctic["Pollution"]["Influenced By"] = [
     "Tundra (Arctic) - Long-Range Transport of Pollutants",
 "Tundra (Arctic) - Local Sources"
]
tundra_arctic["Pollution"]["Influences"] = [
   "Tundra (Arctic) - Wildlife Health"
]
tundra_arctic["Pollution"]["Logic Description"] = "The Arctic Tundra receives pollutants from both local sources (resource extraction, shipping) and long-range transport from industrial areas around the globe. These pollutants can accumulate in the food chain, impacting wildlife health."
tundra_arctic["Pollution"]["Impact Function"] = "impact_pollution_arctic_tundra"

tundra_arctic["Invasive Species"]["Metric"] = "Distribution and abundance of invasive species (plants, insects, etc.).  Currently less of a problem than in many other biomes, but increasing with climate change and development."
tundra_arctic["Invasive Species"]["Data Sources"] = [
       "Research studies.",
     "Monitoring programs (where they exist)."
]
tundra_arctic["Invasive Species"]["Impact on Area"] = "Potential for changes in vegetation composition."
tundra_arctic["Invasive Species"]["Impact on Biodiversity"] = "Competition with native species.; Alteration of ecosystem processes."
tundra_arctic["Invasive Species"]["Influenced By"] = [
      "Tundra (Arctic) - Climate Change",
        "Tundra (Arctic) - Disturbance",
      "Tundra (Arctic) - Increased Human activity"
]
tundra_arctic["Invasive Species"]["Influences"] = [
   "Tundra (Arctic) - Native Plant Communities"
]
tundra_arctic["Invasive Species"]["Logic Description"] = "While currently less of a widespread problem than in many other biomes, invasive species pose an increasing threat to the Arctic Tundra as the climate warms and human activity increases."
tundra_arctic["Invasive Species"]["Impact Function"] = "impact_invasive_species_arctic_tundra"

tundra_arctic["Economic Growth"]["Metric"] = "GDP, resource extraction activity."
tundra_arctic["Economic Growth"]["Data Sources"] =  "Economic data."
tundra_arctic["Economic Growth"]["Impact on Area"] = "Increased pressure on resources."
tundra_arctic["Economic Growth"]["Impact on Biodiversity"] =  "Habitat loss, disturbance."
tundra_arctic["Economic Growth"]["Influenced By"] = ["Global demand for resources"]
tundra_arctic["Economic Growth"]["Influences"] = [
    "Tundra (Arctic) - Infrastructure Development"
]
tundra_arctic["Economic Growth"]["Logic Description"] = "Economic growth drives resource extraction."
tundra_arctic["Economic Growth"]["Impact Function"] = "impact_economic_growth_arctic_tundra"

tundra_arctic["Geopolitical Factors"]["Metric"] = "International agreements, military activity"
tundra_arctic["Geopolitical Factors"]["Data Sources"] = ["News Reports, government documents"]
tundra_arctic["Geopolitical Factors"]["Impact on Area"] = "Variable, can influence resource development, conservation efforts."
tundra_arctic["Geopolitical Factors"]["Impact on Biodiversity"] = "Variable."
tundra_arctic["Geopolitical Factors"]["Influenced By"] = ["Global politics"]
tundra_arctic["Geopolitical Factors"]["Influences"] = [
     "Tundra (Arctic) - Infrastructure Development"
]
tundra_arctic["Geopolitical Factors"]["Logic Description"] = "Geopolitics can influence Arctic development."
tundra_arctic["Geopolitical Factors"]["Impact Function"] = "impact_geopolitical_factors_arctic_tundra"

tundra_arctic["Government Policies"]["Metric"] = "Resource management regulations, environmental protections"
tundra_arctic["Government Policies"]["Data Sources"] = ["Policy documents"]
tundra_arctic["Government Policies"]["Impact on Area"] = "Variable"
tundra_arctic["Government Policies"]["Impact on Biodiversity"] = "Variable"
tundra_arctic["Government Policies"]["Influenced By"] = [
 "Politics",
  "Economics"
]
tundra_arctic["Government Policies"]["Influences"] = [
 "Tundra (Arctic) - Infrastructure Development"
]
tundra_arctic["Government Policies"]["Logic Description"] = "Government policy shapes resource use."
tundra_arctic["Government Policies"]["Impact Function"] = "impact_government_policies_arctic_tundra"

tundra_arctic["Global Commodity Prices"]["Metric"] = "Prices of oil, gas, minerals."
tundra_arctic["Global Commodity Prices"]["Data Sources"] = ["Economic Data"]
tundra_arctic["Global Commodity Prices"]["Impact on Area"] = "Influences the economic viability of resource extraction."
tundra_arctic["Global Commodity Prices"]["Impact on Biodiversity"] = "Indirect, through impacts on development."
tundra_arctic["Global Commodity Prices"]["Influenced By"] = ["Global markets."]
tundra_arctic["Global Commodity Prices"]["Influences"] = ["Tundra (Arctic) - Infrastructure Development"]
tundra_arctic["Global Commodity Prices"]["Logic Description"] = "Commodity prices influence resource extraction."
tundra_arctic["Global Commodity Prices"]["Impact Function"] = "impact_global_commodity_prices_arctic_tundra"

tundra_arctic["Technological Advancements"]["Metric"] = "Development of new technologies for resource extraction, transportation."
tundra_arctic["Technological Advancements"]["Data Sources"] = [
    "Industry reports, research publications."
]
tundra_arctic["Technological Advancements"]["Impact on Area"] = "Can make resource extraction more feasible or less impactful."
tundra_arctic["Technological Advancements"]["Impact on Biodiversity"] = "Variable"
tundra_arctic["Technological Advancements"]["Influenced By"] = ["Research and development."]
tundra_arctic["Technological Advancements"]["Influences"] = [
     "Tundra (Arctic) - Infrastructure Development"
]
tundra_arctic["Technological Advancements"]["Logic Description"] = "Technology can change the feasibility of resource extraction."
tundra_arctic["Technological Advancements"]["Impact Function"] = "impact_technological_advancements_arctic_tundra"

tundra_arctic["Long-Range Transport of Pollutants"]["Metric"] = "Concentrations of pollutants in air, water, ice."
tundra_arctic["Long-Range Transport of Pollutants"]["Data Sources"] = [
  "Environmental monitoring programs (AMAP)"
]
tundra_arctic["Long-Range Transport of Pollutants"]["Impact on Area"] = "Widespread contamination."
tundra_arctic["Long-Range Transport of Pollutants"]["Impact on Biodiversity"] = "Toxic effects on wildlife."
tundra_arctic["Long-Range Transport of Pollutants"]["Influenced By"] = [
  "Industrial activity in other regions."
]
tundra_arctic["Long-Range Transport of Pollutants"]["Influences"] = [
    "Tundra (Arctic) - Pollution"
]
tundra_arctic["Long-Range Transport of Pollutants"]["Logic Description"] = "Pollutants travel long distances to the Arctic."
tundra_arctic["Long-Range Transport of Pollutants"]["Impact Function"] = "impact_long_range_transport_arctic_tundra"

tundra_arctic["Local Sources"]["Metric"] = "Pollutant emissions from local activities."
tundra_arctic["Local Sources"]["Data Sources"] = [
    "Environmental monitoring."
    ]
tundra_arctic["Local Sources"]["Impact on Area"] = "Localized pollution."
tundra_arctic["Local Sources"]["Impact on Biodiversity"] = "Impacts on wildlife."
tundra_arctic["Local Sources"]["Influenced By"] = [
    "Tundra (Arctic) - Infrastructure Development"
]
tundra_arctic["Local Sources"]["Influences"] = [
      "Tundra (Arctic) - Pollution"
]
tundra_arctic["Local Sources"]["Logic Description"] = "Local activities contribute to pollution."
tundra_arctic["Local Sources"]["Impact Function"] = "impact_local_sources_arctic_tundra"

tundra_arctic["Disturbance"]["Metric"] = "Area and frequency"
tundra_arctic["Disturbance"]["Data Sources"] = ["Field Observations, remote sensing"]
tundra_arctic["Disturbance"]["Impact on Area"] = "Varies"
tundra_arctic["Disturbance"]["Impact on Biodiversity"] = "Variable"
tundra_arctic["Disturbance"]["Influenced By"] = [
    "Many"
]
tundra_arctic["Disturbance"]["Influences"] = [
 "Tundra (Arctic) - Invasive Species"
]
tundra_arctic["Disturbance"]["Logic Description"] = "General category for various disturbances."
tundra_arctic["Disturbance"]["Impact Function"] = "impact_disturbance_arctic_tundra"

tundra_arctic["Increased Human Activity"]["Metric"] = "Population, tourism, shipping traffic"
tundra_arctic["Increased Human Activity"]["Data Sources"] = [
    "Various"
]
tundra_arctic["Increased Human Activity"]["Impact on Area"] = "Disturbance, pollution"
tundra_arctic["Increased Human Activity"]["Impact on Biodiversity"] = "Impacts on wildlife"
tundra_arctic["Increased Human Activity"]["Influenced By"] = [
    "Many"
]
tundra_arctic["Increased Human Activity"]["Influences"] = [
   "Tundra (Arctic) - Invasive Species"
]
tundra_arctic["Increased Human Activity"]["Logic Description"] = "Increasing human presence has impacts."
tundra_arctic["Increased Human Activity"]["Impact Function"] = "impact_human_activity_arctic_tundra"

tundra_arctic["Native Plant Communities"]["Metric"] = "Plant species composition, abundance"
tundra_arctic["Native Plant Communities"]["Data Sources"] = ["Field Surveys"]
tundra_arctic["Native Plant Communities"]["Impact on Area"] = "Overall ecosystem structure"
tundra_arctic["Native Plant Communities"]["Impact on Biodiversity"] = "Interactions with other species."
tundra_arctic["Native Plant Communities"]["Influenced By"] = [
"Tundra (Arctic) - Invasive Species"
]
tundra_arctic["Native Plant Communities"]["Influences"] = [
        "Many"
]
tundra_arctic["Native Plant Communities"]["Logic Description"] = "Native plants are the foundation of the ecosystem."
tundra_arctic["Native Plant Communities"]["Impact Function"] = "impact_plant_communities_arctic_tundra"

tundra_arctic["Hydrology"]["Metric"] = "Water flow, water levels."
tundra_arctic["Hydrology"]["Data Sources"] = [
     "Hydrological monitoring data"
]
tundra_arctic["Hydrology"]["Impact on Area"] = "Water availability, wetland extent"
tundra_arctic["Hydrology"]["Impact on Biodiversity"] = "Impacts on aquatic and wetland species"
tundra_arctic["Hydrology"]["Influenced By"] = [
    "Tundra (Arctic) - Permafrost Thaw"
]
tundra_arctic["Hydrology"]["Influences"] = [
   "Many, Varies"
]
tundra_arctic["Hydrology"]["Logic Description"] = "Water flow is fundamental."
tundra_arctic["Hydrology"]["Impact Function"] = "impact_hydrology_arctic_tundra"

tundra_arctic["Vegetation Changes"]["Metric"] = "Plant community composition, abundance"
tundra_arctic["Vegetation Changes"]["Data Sources"] = ["Field Surveys","Remote Sensing"]
tundra_arctic["Vegetation Changes"]["Impact on Area"] = "Habitat structure"
tundra_arctic["Vegetation Changes"]["Impact on Biodiversity"] = "Altered species interactions."
tundra_arctic["Vegetation Changes"]["Influenced By"] = [
  "Tundra (Arctic) - Permafrost Thaw"
]
tundra_arctic["Vegetation Changes"]["Influences"] = [
   "Many, Varies"
]
tundra_arctic["Vegetation Changes"]["Logic Description"] = "Vegetation changes reflect other stressors."
tundra_arctic["Vegetation Changes"]["Impact Function"] = "impact_vegetation_changes_arctic_tundra"

tundra_arctic["Coastal Erosion"]["Metric"] = "Rate of shoreline retreat"
tundra_arctic["Coastal Erosion"]["Data Sources"] = [
     "Remote Sensing",
  "Field measurements"
]
tundra_arctic["Coastal Erosion"]["Impact on Area"] = "Land Loss"
tundra_arctic["Coastal Erosion"]["Impact on Biodiversity"] = "Habitat loss"
tundra_arctic["Coastal Erosion"]["Influenced By"] = [
    "Tundra (Arctic) - Permafrost Thaw",
    "Tundra (Arctic) - Sea Ice Loss"
]
tundra_arctic["Coastal Erosion"]["Influences"] = [
        "Many, varies"
]
tundra_arctic["Coastal Erosion"]["Logic Description"] = "Erosion is a major issue in coastal areas"
tundra_arctic["Coastal Erosion"]["Impact Function"] = "impact_coastal_erosion_arctic_tundra"

tundra_arctic["Regional Climate"]["Metric"] = "Temperature, precipitation, wind patterns"
tundra_arctic["Regional Climate"]["Data Sources"] = [
     "Climate data."
]
tundra_arctic["Regional Climate"]["Impact on Area"] = "Overall climate conditions"
tundra_arctic["Regional Climate"]["Impact on Biodiversity"] = "Many Impacts"
tundra_arctic["Regional Climate"]["Influenced By"] = [
        "Tundra (Arctic) - Sea Ice Loss"
]
tundra_arctic["Regional Climate"]["Influences"] = [
    "Many"
]
tundra_arctic["Regional Climate"]["Logic Description"] = "Regional climate drives local conditions."
tundra_arctic["Regional Climate"]["Impact Function"] = "impact_regional_climate_arctic_tundra"

tundra_arctic["Shrubification"]["Metric"] = "Shrub cover and abundance."
tundra_arctic["Shrubification"]["Data Sources"] = [
   "Remote sensing",
    "Field surveys."
]
tundra_arctic["Shrubification"]["Impact on Area"] = "Changes in vegetation structure and albedo."
tundra_arctic["Shrubification"]["Impact on Biodiversity"] = "Impacts on species that prefer open tundra.; Changes in snow cover and permafrost."
tundra_arctic["Shrubification"]["Influenced By"] = [
  "Tundra (Arctic) - Temperature Increase"
]
tundra_arctic["Shrubification"]["Influences"] = [
 "Many"
]
tundra_arctic["Shrubification"]["Logic Description"] = "Expansion of shrubs is a major vegetation change."
tundra_arctic["Shrubification"]["Impact Function"] = "impact_shrubification_arctic_tundra"

tundra_arctic["Wildlife Disturbance"]["Metric"] = "Frequency and intensity of human disturbance to wildlife."
tundra_arctic["Wildlife Disturbance"]["Data Sources"] = ["Research Studies"]
tundra_arctic["Wildlife Disturbance"]["Impact on Area"] = "Indirect, through impacts on animal behavior and populations."
tundra_arctic["Wildlife Disturbance"]["Impact on Biodiversity"] = "Altered behavior, reduced reproductive success, increased stress."
tundra_arctic["Wildlife Disturbance"]["Influenced By"] = [
   "Tundra (Arctic) - Infrastructure Development"
]
tundra_arctic["Wildlife Disturbance"]["Influences"] = [
    "Tundra (Arctic) - Population Dynamics"
]
tundra_arctic["Wildlife Disturbance"]["Logic Description"] = "Human disturbance affects wildlife."
tundra_arctic["Wildlife Disturbance"]["Impact Function"] = "impact_wildlife_disturbance_arctic_tundra"

tundra_arctic["Wildlife Populations"]["Metric"] = "Population sizes and distributions of key species."
tundra_arctic["Wildlife Populations"]["Data Sources"] = [
        "Wildlife surveys"
]
tundra_arctic["Wildlife Populations"]["Impact on Area"] = "Indirect"
tundra_arctic["Wildlife Populations"]["Impact on Biodiversity"] = "Ecosystem Function."
tundra_arctic["Wildlife Populations"]["Influenced By"] = [
        "Tundra (Arctic) - Changes in Precipitation"
]
tundra_arctic["Wildlife Populations"]["Influences"] = [
       "Many"
]
tundra_arctic["Wildlife Populations"]["Logic Description"] = "Wildlife populations are affected by many stressors."
tundra_arctic["Wildlife Populations"]["Impact Function"] = "impact_wildlife_populations_arctic_tundra"

tundra_arctic["Wildlife Health"]["Metric"] = "Disease prevalence, mortality rates."
tundra_arctic["Wildlife Health"]["Data Sources"] = ["Wildlife monitoring programs"]
tundra_arctic["Wildlife Health"]["Impact on Area"] = "Indirect, through population impacts."
tundra_arctic["Wildlife Health"]["Impact on Biodiversity"] = "Population Declines"
tundra_arctic["Wildlife Health"]["Influenced By"] = [
  "Tundra (Arctic) - Pollution"
]
tundra_arctic["Wildlife Health"]["Influences"] = [
 "Tundra (Arctic) - Population Dynamics"
]
tundra_arctic["Wildlife Health"]["Logic Description"] = "Overall Health"
tundra_arctic["Wildlife Health"]["Impact Function"] = "impact_wildlife_health_arctic_tundra"

# --- Wetlands (Camargue) ---
camargue = all_stressors_data["Camargue Wetlands"]

camargue["Altered Hydrology"]["Metric"] = "Water levels in the Rhone River and in the Camargue's lagoons and marshes; salinity levels; water flow rates; water management interventions (sluice gate operations, pumping)."
camargue["Altered Hydrology"]["Data Sources"] = [
    "French government agencies (e.g., Agence de l'eau Rhône Méditerranée Corse).",
    "Research institutions (e.g., Tour du Valat research center).",
    "Remote sensing data.",
   "Hydrological models."
]
camargue["Altered Hydrology"]["Impact on Area"] = "Changes in the extent and distribution of different wetland habitats (freshwater marshes, brackish lagoons, salt marshes, salt pans)."
camargue["Altered Hydrology"]["Impact on Biodiversity"] = "Impacts on bird populations (breeding, feeding, migration - the Camargue is a *major* bird area).; Changes in plant communities (due to altered salinity).; Impacts on fish and invertebrate communities."
camargue["Altered Hydrology"]["Influenced By"] = [
    "Wetlands (Camargue) - Water Management Practices",
    "Upstream Water Use (along the Rhone)",
   "Wetlands (Camargue) - Rice Cultivation",
    "Wetlands (Camargue) - Climate Change",
   "Wetlands (Camargue) - Sea Level Rise"
]
camargue["Altered Hydrology"]["Influences"] = [
    "Wetlands (Camargue) - Salinity Levels",
  "Wetlands (Camargue) - Habitat Availability",
    "Wetlands (Camargue) - Water Quality"
]
camargue["Altered Hydrology"]["Logic Description"] = "The Camargue's hydrology is heavily managed, with a complex system of canals, sluices, and pumping stations. Changes in water management, upstream water use, and climate change can significantly alter water levels, salinity, and habitat distribution. This requires constant management to balance human needs and ecological requirements."
camargue["Altered Hydrology"]["Impact Function"] = "impact_altered_hydrology_camargue"

camargue["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., nutrients, pesticides, heavy metals) in water, sediment, and biota."
camargue["Pollution"]["Data Sources"] = [
 "Water quality monitoring programs (French government agencies, research institutions).",
    "Research studies."
]
camargue["Pollution"]["Impact on Area"] = "Degradation of water quality."
camargue["Pollution"]["Impact on Biodiversity"] = "Eutrophication (nutrient enrichment); toxic effects on wildlife; impacts on food webs."
camargue["Pollution"]["Influenced By"] = [
  "Wetlands (Camargue) - Agricultural Runoff",
  "Industrial Discharge (upstream along the Rhone)",
    "Urban Runoff"
]
camargue["Pollution"]["Influences"] = [
  "Wetlands (Camargue) - Water Quality",
    "Wetlands (Camargue) - Wildlife Health"
]
camargue["Pollution"]["Logic Description"] = "Pollution from agriculture, industry, and urban areas can degrade water quality and impact the Camargue's ecosystems."
camargue["Pollution"]["Impact Function"] = "impact_pollution_camargue"

camargue["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality); sea level rise (mm/year)."
camargue["Climate Change"]["Data Sources"] = [
   "Climate models.",
   "Historical weather records.",
     "Tide gauge data."
]
camargue["Climate Change"]["Impact on Area"] = "Coastal erosion and inundation due to sea level rise; changes in salinity; increased risk of drought."
camargue["Climate Change"]["Impact on Biodiversity"] = "Shifts in species distributions; increased stress on wildlife; changes in phenology; loss of coastal habitats."
camargue["Climate Change"]["Influenced By"] = ["Global GHG"]
camargue["Climate Change"]["Influences"] = [
     "Wetlands (Camargue) - Sea Level Rise",
    "Wetlands (Camargue) - Water Availability",
     "Wetlands (Camargue) - Altered Hydrology"
]
camargue["Climate Change"]["Logic Description"] = "Climate change is impacting the Camargue through sea level rise, altered precipitation patterns, and increased temperatures."
camargue["Climate Change"]["Impact Function"] = "impact_climate_change_camargue"

camargue["Invasive Species"]["Metric"] = "Distribution and abundance of key invasive species (e.g., *Ludwigia* spp. (water primrose), *Procambarus clarkii* (red swamp crayfish))."
camargue["Invasive Species"]["Data Sources"] = [
  "Field surveys.",
    "Research studies.",
   "Monitoring programs by local authorities."
]
camargue["Invasive Species"]["Impact on Area"] = "Changes in vegetation composition and structure; altered hydrology (in some cases)."
camargue["Invasive Species"]["Impact on Biodiversity"] = "Competition with native plants; predation on native invertebrates and fish; alteration of habitat structure."
camargue["Invasive Species"]["Influenced By"] = [
    "Introduction through human activities (e.g., aquaculture, ballast water).",
  "Wetlands (Camargue) - Altered Hydrology",
   "Wetlands (Camargue) - Climate Change"
]
camargue["Invasive Species"]["Influences"] = [
    "Wetlands (Camargue) - Native Species",
   "Wetlands (Camargue) - Ecosystem Functioning"
]
camargue["Invasive Species"]["Logic Description"] = "Invasive species, particularly aquatic plants and invertebrates, can outcompete native species and alter ecosystem processes in the Camargue."
camargue["Invasive Species"]["Impact Function"] = "impact_invasive_species_camargue"

camargue["Tourism"]["Metric"] = "Number of tourists visiting the Camargue per year; development of tourism infrastructure."
camargue["Tourism"]["Data Sources"] = [
    "Tourism statistics (regional and national).",
  "Reports from local authorities."
]
camargue["Tourism"]["Impact on Area"] = "Localized disturbance to habitats; pressure on infrastructure (e.g., water supply, waste management)."
camargue["Tourism"]["Impact on Biodiversity"] = "Disturbance to wildlife, particularly breeding birds; habitat degradation (e.g., trampling of vegetation)."
camargue["Tourism"]["Influenced By"] = [
   "Economic Factors",
     "Accessibility",
   "Marketing and Promotion"
]
camargue["Tourism"]["Influences"] = [
 "Wetlands (Camargue) - Wildlife Disturbance",
  "Wetlands (Camargue) - Pollution (waste)"
]
camargue["Tourism"]["Logic Description"] = "Tourism, while economically important, can put pressure on the Camargue's fragile ecosystems, particularly through disturbance to wildlife and habitat degradation."
camargue["Tourism"]["Impact Function"] = "impact_tourism_camargue"

camargue["Sea Level Rise"]["Metric"] = "Rate of sea level rise (mm/year) relative to land elevation."
camargue["Sea Level Rise"]["Data Sources"] = [
   "Tide gauge records.",
   "Satellite altimetry.",
   "Climate models."
]
camargue["Sea Level Rise"]["Impact on Area"] = "Coastal erosion and inundation; saltwater intrusion into freshwater wetlands."
camargue["Sea Level Rise"]["Impact on Biodiversity"] = "Loss of coastal habitats; shifts in species distributions; increased stress on freshwater species."
camargue["Sea Level Rise"]["Influenced By"] = [
   "Wetlands (Camargue) - Climate Change"
]
camargue["Sea Level Rise"]["Influences"] = [
 "Wetlands (Camargue) - Altered Hydrology",
  "Wetlands (Camargue) - Coastal Erosion"
]
camargue["Sea Level Rise"]["Logic Description"] = "Sea level rise is a significant threat to the low-lying Camargue, leading to coastal erosion, inundation, and saltwater intrusion."
camargue["Sea Level Rise"]["Impact Function"] = "impact_sea_level_rise_camargue"

camargue["Agriculture"]["Metric"] = "Area under agricultural production; types of crops grown (rice, etc.); use of fertilizers and pesticides."
camargue["Agriculture"]["Data Sources"] = [
 "Agricultural statistics (France).",
    "Remote sensing data.",
     "Research studies."
]
camargue["Agriculture"]["Impact on Area"] = "Conversion of wetlands to agricultural land; altered hydrology (irrigation and drainage); pollution from runoff."
camargue["Agriculture"]["Impact on Biodiversity"] = "Habitat loss; impacts on water quality; pesticide exposure to wildlife."
camargue["Agriculture"]["Influenced By"] = [
     "Economic Factors (market prices for crops).",
    "Agricultural Policies (subsidies, regulations).",
    "Water Availability"
]
camargue["Agriculture"]["Influences"] = [
    "Wetlands (Camargue) - Land-Use Change",
 "Wetlands (Camargue) - Altered Hydrology",
  "Wetlands (Camargue) - Pollution"
]
camargue["Agriculture"]["Logic Description"] = "Agriculture, particularly rice cultivation, is a major land use in and around the Camargue, impacting water resources, hydrology, and water quality."
camargue["Agriculture"]["Impact Function"] = "impact_agriculture_camargue"

# --- Wetlands (Danube Delta) ---
danube_delta = all_stressors_data["Danube Delta Wetlands"]

danube_delta["Altered Hydrology"]["Metric"] = "Water levels in the Danube River and in the delta's channels, lakes, and marshes; water flow rates; water management interventions (dams, canals, embankments)."
danube_delta["Altered Hydrology"]["Data Sources"] = [
    "Romanian government agencies (e.g., Danube Delta National Institute for Research and Development).",
    "International Commission for the Protection of the Danube River (ICPDR).",
    "Research institutions.",
    "Remote sensing data."
]
danube_delta["Altered Hydrology"]["Impact on Area"] = "Changes in the extent and distribution of different wetland habitats (freshwater marshes, reed beds, floating reed islands, lakes, channels)."
danube_delta["Altered Hydrology"]["Impact on Biodiversity"] = "Impacts on bird populations (breeding, feeding, migration - the Danube Delta is a *crucially important* bird area).; Changes in plant communities.; Impacts on fish populations (spawning, migration).; Impacts on other aquatic organisms (e.g., amphibians, invertebrates)."
danube_delta["Altered Hydrology"]["Influenced By"] = [
    "Upstream Dams (on the Danube and its tributaries)",
    "Water Management Practices within the Delta (canals, embankments)",
    "Agricultural Practices",
    "Climate Change"
]
danube_delta["Altered Hydrology"]["Influences"] = [
"Wetlands (Danube Delta) - Habitat Availability",
"Wetlands (Danube Delta) - Water Quality",
"Wetlands (Danube Delta) - Sedimentation"
]
danube_delta["Altered Hydrology"]["Logic Description"] = "The Danube Delta's hydrology has been significantly altered by dams upstream on the Danube River and by canals and embankments within the delta itself.  These changes affect water levels, flow rates, and sediment deposition, impacting the delta's ecosystems."
danube_delta["Altered Hydrology"]["Impact Function"] = "impact_altered_hydrology_danube_delta"

danube_delta["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., nutrients, pesticides, heavy metals, industrial chemicals) in water, sediment, and biota."
danube_delta["Pollution"]["Data Sources"] = [
    "Water quality monitoring programs (Romanian government agencies, ICPDR).",
    "Research studies."
]
danube_delta["Pollution"]["Impact on Area"] = "Degradation of water quality; contamination of sediments."
danube_delta["Pollution"]["Impact on Biodiversity"] = "Eutrophication (nutrient enrichment); toxic effects on wildlife; impacts on food webs."
danube_delta["Pollution"]["Influenced By"] = [
"Agricultural Runoff (from the Danube River basin)",
    "Industrial Discharge (upstream on the Danube and its tributaries)",
    "Untreated Sewage (from settlements in and around the delta)",
    "Shipping Activities"
]
danube_delta["Pollution"]["Influences"] = [
"Wetlands (Danube Delta) - Water Quality",
"Wetlands (Danube Delta) - Wildlife Health",
"Wetlands (Danube Delta) - Eutrophication"
]
danube_delta["Pollution"]["Logic Description"] = "Pollution from agriculture, industry, sewage, and shipping in the Danube River basin impacts the water quality of the Danube Delta."
danube_delta["Pollution"]["Impact Function"] = "impact_pollution_danube_delta"

danube_delta["Eutrophication"]["Metric"] = "Nutrient levels (nitrogen, phosphorus) in water; chlorophyll-a concentrations; frequency and extent of algal blooms."
danube_delta["Eutrophication"]["Data Sources"] = [
"Water quality monitoring programs.",
"Remote sensing data (detecting algal blooms).",
    "Research studies."
]
danube_delta["Eutrophication"]["Impact on Area"] = "Algal blooms; reduced oxygen levels in the water (hypoxia or anoxia); changes in water clarity."
danube_delta["Eutrophication"]["Impact on Biodiversity"] = "Loss of aquatic plants; fish kills; changes in species composition; impacts on food webs."
danube_delta["Eutrophication"]["Influenced By"] = [
"Wetlands (Danube Delta) - Agricultural Runoff",
"Wetlands (Danube Delta) - Untreated Sewage"
]
danube_delta["Eutrophication"]["Influences"] = [
    "Wetlands (Danube Delta) - Water Quality",
    "Wetlands (Danube Delta) - Fish Populations",
"Wetlands (Danube Delta) - Ecosystem Function"
]
danube_delta["Eutrophication"]["Logic Description"] = "Eutrophication, caused by excessive nutrient inputs (primarily nitrogen and phosphorus) from agriculture and sewage, is a major problem in the Danube Delta, leading to algal blooms, oxygen depletion, and impacts on aquatic life."
danube_delta["Eutrophication"]["Impact Function"] = "impact_eutrophication_danube_delta"

danube_delta["Invasive Species"]["Metric"] = "Distribution and abundance of key invasive species (e.g., *Rapana venosa* (veined rapa whelk), *Ameiurus melas* (black bullhead catfish), *Cyprinus carpio* (common carp) - although carp's status is debated)."
danube_delta["Invasive Species"]["Data Sources"] = [
"Field surveys.",
"Research studies.",
"Fisheries data."
]
danube_delta["Invasive Species"]["Impact on Area"] = "Changes in species composition; altered food webs."
danube_delta["Invasive Species"]["Impact on Biodiversity"] = "Competition with native species; predation on native species; alteration of habitat structure."
danube_delta["Invasive Species"]["Influenced By"] = [
"Introduction through human activities (e.g., ballast water, aquaculture).",
"Wetlands (Danube Delta) - Altered Hydrology",
"Wetlands (Danube Delta) - Climate Change"
]
danube_delta["Invasive Species"]["Influences"] = [
"Wetlands (Danube Delta) - Native Species",
"Wetlands (Danube Delta) - Ecosystem Functioning"
]
danube_delta["Invasive Species"]["Logic Description"] = "Invasive species can outcompete native species, alter food webs, and disrupt ecosystem processes in the Danube Delta."
danube_delta["Invasive Species"]["Impact Function"] = "impact_invasive_species_danube_delta"

danube_delta["Overfishing"]["Metric"] = "Fish catch data; fish stock assessments; fishing effort."
danube_delta["Overfishing"]["Data Sources"] = [
"Fisheries statistics (Romanian government agencies).",
"Research studies.",
    "Stock assessments."
]
danube_delta["Overfishing"]["Impact on Area"] = "Decline in fish populations."
danube_delta["Overfishing"]["Impact on Biodiversity"] = "Impacts on targeted fish species; changes in fish community structure; impacts on food webs (e.g., affecting bird populations that feed on fish)."
danube_delta["Overfishing"]["Influenced By"] = [
"Fishing Pressure (legal and illegal)",
"Lack of Effective Fisheries Management",
"Economic Factors"
]
danube_delta["Overfishing"]["Influences"] = [
"Wetlands (Danube Delta) - Fish Populations",
    "Wetlands (Danube Delta) - Food Web Structure"
]
danube_delta["Overfishing"]["Logic Description"] = "Overfishing, both legal and illegal, can deplete fish stocks and disrupt the food web in the Danube Delta."
danube_delta["Overfishing"]["Impact Function"] = "impact_overfishing_danube_delta"

danube_delta["Tourism and Recreation"]["Metric"] = "Number of tourists visiting the delta per year; development of tourism infrastructure (e.g., hotels, boats)."
danube_delta["Tourism and Recreation"]["Data Sources"] = [
"Tourism statistics.",
"Reports from local authorities."
]
danube_delta["Tourism and Recreation"]["Impact on Area"] = "Localized disturbance to habitats; pressure on infrastructure (e.g., waste management)."
danube_delta["Tourism and Recreation"]["Impact on Biodiversity"] = "Disturbance to wildlife, particularly breeding birds; habitat degradation; pollution from boats."
danube_delta["Tourism and Recreation"]["Influenced By"] = [
"Economic Factors",
"Accessibility",
"Marketing and Promotion"
]
danube_delta["Tourism and Recreation"]["Influences"] = [
"Wetlands (Danube Delta) - Wildlife Disturbance",
"Wetlands (Danube Delta) - Pollution"
]
danube_delta["Tourism and Recreation"]["Logic Description"] = "Tourism, while providing economic benefits, can also put pressure on the Danube Delta's ecosystems, particularly through disturbance to wildlife and habitat degradation."
danube_delta["Tourism and Recreation"]["Impact Function"] = "impact_tourism_recreation_danube_delta"

danube_delta["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality); sea level rise (mm/year - relevant for the coastal parts of the delta)."
danube_delta["Climate Change"]["Data Sources"] = [
"Climate models.",
"Historical weather records.",
    "Sea level data."
]
danube_delta["Climate Change"]["Impact on Area"] = "Changes in water availability; increased risk of drought; potential for saltwater intrusion; coastal erosion."
danube_delta["Climate Change"]["Impact on Biodiversity"] = "Shifts in species distributions; increased stress on wildlife; changes in phenology; loss of coastal habitats."
danube_delta["Climate Change"]["Influenced By"] = ["Global GHG"]
danube_delta["Climate Change"]["Influences"] = [
"Wetlands (Danube Delta) - Altered Hydrology",
"Wetlands (Danube Delta) - Water Availability",
"Wetlands (Danube Delta) - Sea Level Rise (indirect)"
]
danube_delta["Climate Change"]["Logic Description"] = "Climate change is expected to impact the Danube Delta through altered precipitation patterns, increased temperatures, and potential sea level rise."
danube_delta["Climate Change"]["Impact Function"] = "impact_climate_change_danube_delta"

danube_delta["Agriculture"]["Metric"] = "Area under agricultural use within the delta (though limited now, historical impacts and surrounding areas are relevant). Use of fertilizers and pesticides in the Danube basin."
danube_delta["Agriculture"]["Data Sources"] = [
"Agricultural statistics.",
"Remote Sensing.",
"Research studies."
]
danube_delta["Agriculture"]["Impact on Area"] = "Historical conversion of wetlands to agricultural land. Runoff contributes to pollution."
danube_delta["Agriculture"]["Impact on Biodiversity"] = "Habitat Loss. Water quality degradation, impacting aquatic life."
danube_delta["Agriculture"]["Influenced By"] = [
"Agricultural policies in the Danube River Basin."
]
danube_delta["Agriculture"]["Influences"] = [
"Wetlands (Danube Delta) - Eutrophication",
    "Wetlands (Danube Delta) - Pollution"
]
danube_delta["Agriculture"]["Logic Description"] = "While large-scale agriculture *within* the delta is now limited due to its protected status, past conversions and ongoing agriculture in the wider Danube basin significantly contribute to nutrient and pesticide pollution affecting the delta's health."
danube_delta["Agriculture"]["Impact Function"] = "impact_agriculture_danube_delta"

# --- Wetlands (Everglades) ---
everglades = all_stressors_data["Everglades Wetlands"]

everglades["Altered Hydrology"]["Metric"] = "Water levels (depth, duration, timing of flooding); water flow rates; water distribution across the Everglades landscape; salinity in coastal areas."
everglades["Altered Hydrology"]["Data Sources"] = [
    "South Florida Water Management District (SFWMD) data.",
    "US Geological Survey (USGS) data.",
    "Everglades National Park data.",
    "Research publications.",
    "Remote sensing data."
]
everglades["Altered Hydrology"]["Impact on Area"] = "Changes in the extent and distribution of different wetland habitats (sawgrass marshes, sloughs, tree islands, mangrove forests); altered hydroperiods (duration of flooding)."
everglades["Altered Hydrology"]["Impact on Biodiversity"] = "Impacts on wading bird populations (nesting, foraging).; Impacts on fish and invertebrate communities.; Changes in plant communities.; Impacts on alligators and other reptiles and amphibians.; Increased vulnerability to invasive species."
everglades["Altered Hydrology"]["Influenced By"] = [
    "Water Management Practices (canals, levees, pumps, water control structures)",
    "Upstream Water Use (agriculture, urban development)",
    "Wetlands (Everglades) - Climate Change",
    "Wetlands (Everglades) - Sea Level Rise"
]
everglades["Altered Hydrology"]["Influences"] = [
"Wetlands (Everglades) - Habitat Availability",
"Wetlands (Everglades) - Water Quality",
"Wetlands (Everglades) - Nutrient Cycling",
"Wetlands (Everglades) - Invasive Species Spread"
]
everglades["Altered Hydrology"]["Logic Description"] = "The Everglades' hydrology has been drastically altered by a complex system of canals, levees, and water control structures built for flood control and water supply. This has disrupted the natural sheet flow of water across the landscape, leading to significant ecological impacts. Restoration efforts are focused on restoring a more natural hydrology."
everglades["Altered Hydrology"]["Impact Function"] = "impact_altered_hydrology_everglades"

everglades["Nutrient Pollution"]["Metric"] = "Concentrations of phosphorus and nitrogen in water and sediment; total phosphorus (TP) is a *key* indicator in the Everglades."
everglades["Nutrient Pollution"]["Data Sources"] = [
    "SFWMD water quality monitoring data.",
    "USGS water quality data.",
"Research publications.",
    "Everglades National Park"
]
everglades["Nutrient Pollution"]["Impact on Area"] = "Eutrophication; changes in water quality; altered nutrient cycling."
everglades["Nutrient Pollution"]["Impact on Biodiversity"] = "Shift from sawgrass-dominated marshes to cattail-dominated marshes (due to phosphorus enrichment); impacts on periphyton communities (a critical food source); impacts on aquatic invertebrates and fish.; Reduced oxygen levels."
everglades["Nutrient Pollution"]["Influenced By"] = [
    "Wetlands (Everglades) - Agricultural Runoff",
    "Urban Runoff",
"Atmospheric Deposition"
]
everglades["Nutrient Pollution"]["Influences"] = [
    "Wetlands (Everglades) - Water Quality",
"Wetlands (Everglades) - Plant Communities (cattail expansion)",
"Wetlands (Everglades) - Ecosystem Function"
]
everglades["Nutrient Pollution"]["Logic Description"] = "Nutrient pollution, particularly phosphorus from agricultural runoff, is a *major* threat to the Everglades. The Everglades is naturally a low-nutrient ecosystem, and even small increases in phosphorus can lead to significant ecological changes, such as the expansion of cattails at the expense of sawgrass."
everglades["Nutrient Pollution"]["Impact Function"] = "impact_nutrient_pollution_everglades"

everglades["Invasive Species"]["Metric"] = "Distribution and abundance of key invasive species (e.g., *Melaleuca quinquenervia* (melaleuca), *Schinus terebinthifolius* (Brazilian pepper), *Lygodium microphyllum* (Old World climbing fern), *Python bivittatus* (Burmese python))."
everglades["Invasive Species"]["Data Sources"] = [
"Field surveys.",
"Remote sensing data.",
"Research studies.",
"Everglades National Park",
"Control program data (e.g., from agencies managing invasive species)."
]
everglades["Invasive Species"]["Impact on Area"] = "Changes in vegetation structure and composition; altered fire regimes; altered hydrology (in some cases)."
everglades["Invasive Species"]["Impact on Biodiversity"] = "Competition with native plants; predation on native animals (e.g., Burmese pythons); alteration of habitat structure; impacts on food webs."
everglades["Invasive Species"]["Influenced By"] = [
    "Introduction through human activities (e.g., ornamental plant trade, pet trade).",
"Wetlands (Everglades) - Altered Hydrology",
"Wetlands (Everglades) - Disturbance",
"Wetlands (Everglades) - Climate Change"
]
everglades["Invasive Species"]["Influences"] = [
"Wetlands (Everglades) - Native Species",
"Wetlands (Everglades) - Ecosystem Processes",
"Wetlands (Everglades) - Fire Regimes"
]
everglades["Invasive Species"]["Logic Description"] = "Invasive species, both plants and animals, pose a significant threat to the Everglades, outcompeting native species, altering habitat, and disrupting ecosystem processes.  The Burmese python is a particularly high-profile example of an impactful invasive predator."
everglades["Invasive Species"]["Impact Function"] = "impact_invasive_species_everglades"

everglades["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality); increased frequency and intensity of extreme weather events (e.g., hurricanes, droughts)."
everglades["Climate Change"]["Data Sources"] = [
"Climate models.",
"Historical weather records.",
"Research publications."
]
everglades["Climate Change"]["Impact on Area"] = "Changes in water availability; increased risk of wildfires; increased vulnerability to saltwater intrusion."
everglades["Climate Change"]["Impact on Biodiversity"] = "Shifts in species distributions; increased stress on wildlife; changes in phenology; increased risk of extreme events."
everglades["Climate Change"]["Influenced By"] = ["Global GHG"]
everglades["Climate Change"]["Influences"] = [
"Wetlands (Everglades) - Sea Level Rise",
"Wetlands (Everglades) - Altered Hydrology",
"Wetlands (Everglades) - Fire Regimes"
]
everglades["Climate Change"]["Logic Description"] = "Climate change is expected to impact the Everglades through altered precipitation patterns, increased temperatures, increased frequency of extreme events, and sea level rise."
everglades["Climate Change"]["Impact Function"] = "impact_climate_change_everglades"

everglades["Sea Level Rise"]["Metric"] = "Rate of sea level rise (mm/year) relative to land elevation; saltwater intrusion into coastal aquifers and wetlands."
everglades["Sea Level Rise"]["Data Sources"] = [
"Tide gauge records.",
"Satellite altimetry.",
"Research publications.",
"USGS",
"NOAA"
]
everglades["Sea Level Rise"]["Impact on Area"] = "Coastal erosion and inundation; saltwater intrusion into freshwater wetlands and aquifers; loss of coastal habitats (e.g., mangrove forests)."
everglades["Sea Level Rise"]["Impact on Biodiversity"] = "Loss of coastal habitats; shifts in species distributions (e.g., mangroves moving inland); increased stress on freshwater species; impacts on nesting sites for sea turtles and crocodiles."
everglades["Sea Level Rise"]["Influenced By"] = [
"Wetlands (Everglades) - Climate Change"
]
everglades["Sea Level Rise"]["Influences"] = [
"Wetlands (Everglades) - Altered Hydrology",
"Wetlands (Everglades) - Coastal Habitats",
"Wetlands (Everglades) - Water Quality (salinity)"
]
everglades["Sea Level Rise"]["Logic Description"] = "Sea level rise is a *major* threat to the low-lying Everglades, leading to saltwater intrusion, coastal erosion, and loss of coastal habitats.  This is one of the most significant long-term threats."
everglades["Sea Level Rise"]["Impact Function"] = "impact_sea_level_rise_everglades"

everglades["Urban Development"]["Metric"] = "Area of urban and suburban development adjacent to the Everglades; population growth in South Florida; impervious surface area."
everglades["Urban Development"]["Data Sources"] = [
"Land-use planning data (county and state level).",
"Census data.",
"Remote sensing data."
]
everglades["Urban Development"]["Impact on Area"] = "Habitat loss and fragmentation along the edges of the Everglades; increased demand for water; increased runoff and pollution."
everglades["Urban Development"]["Impact on Biodiversity"] = "Habitat loss; disruption of wildlife movement; increased human-wildlife conflict; introduction of invasive species."
everglades["Urban Development"]["Influenced By"] = [
"Population Growth (in South Florida)",
"Economic Development"
]
everglades["Urban Development"]["Influences"] = [
"Wetlands (Everglades) - Water Demand",
"Wetlands (Everglades) - Habitat Fragmentation",
"Wetlands (Everglades) - Pollution"
]
everglades["Urban Development"]["Logic Description"] = "Urban development along the boundaries of the Everglades puts pressure on the ecosystem through habitat loss, increased water demand, and pollution."
everglades["Urban Development"]["Impact Function"] = "impact_urban_development_everglades"

everglades["Agricultural Runoff"]["Metric"] = "Nutrient (esp Total Phosphorus) and Pesticide Concentrations."
everglades["Agricultural Runoff"]["Data Sources"] = [
    "SFWMD water quality monitoring data.",
    "USGS water quality data.",
    "Research publications."
]
everglades["Agricultural Runoff"]["Impact on Area"] = "Water Quality Degredation"
everglades["Agricultural Runoff"]["Impact on Biodiversity"] = "Eutrophication; Plant community changes"
everglades["Agricultural Runoff"]["Influenced By"] = [
"Agricultural Practices"
]
everglades["Agricultural Runoff"]["Influences"] = [
"Wetlands (Everglades) - Nutrient Pollution"
]
everglades["Agricultural Runoff"]["Logic Description"] = "Agricultural runoff contributes significant nutrients."
everglades["Agricultural Runoff"]["Impact Function"] = "impact_agricultural_runoff_everglades"

# --- Wetlands (Inner Niger Delta) ---
inner_niger_delta = all_stressors_data["Inner Niger Delta Wetlands"]

inner_niger_delta["Altered Hydrology"]["Metric"] = "Changes in water levels, flooding patterns (extent, duration, timing), and river flow in the Niger River and its tributaries."
inner_niger_delta["Altered Hydrology"]["Data Sources"] = [
   "Hydrological monitoring data (river gauges - often limited in the region).",
    "Remote sensing data (satellite imagery, measuring inundation extent).",
     "Research studies.",
    "Reports from local communities and authorities."
]
inner_niger_delta["Altered Hydrology"]["Impact on Area"] = "Changes in the extent and duration of flooding, affecting the size and distribution of different wetland habitats."
inner_niger_delta["Altered Hydrology"]["Impact on Biodiversity"] = "Impacts on fish populations (spawning, migration, recruitment); Impacts on waterbird populations (breeding, feeding); Impacts on aquatic invertebrates; Changes in vegetation communities (e.g., shifts between flooded grasslands, floating vegetation, and dry land)."
inner_niger_delta["Altered Hydrology"]["Influenced By"] = [
    "Wetlands (Inner Niger Delta) - Upstream Dam Construction",
    "Wetlands (Inner Niger Delta) - Climate Change",
   "Wetlands (Inner Niger Delta) - Water Diversion",
  "Deforestation in the watershed"
]
inner_niger_delta["Altered Hydrology"]["Influences"] = [
 "Wetlands (Inner Niger Delta) - Habitat Availability",
   "Wetlands (Inner Niger Delta) - Water Quality"
]
inner_niger_delta["Altered Hydrology"]["Logic Description"] = "The Inner Niger Delta's ecosystem is fundamentally driven by the annual flood pulse of the Niger River.  Upstream dams, water diversions for irrigation, and climate change are all altering this natural hydrological cycle, with significant impacts on the extent, duration, and timing of flooding.  This, in turn, affects all aspects of the wetland ecosystem."
inner_niger_delta["Altered Hydrology"]["Impact Function"] = "impact_altered_hydrology_inner_niger_delta"

inner_niger_delta["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality); increased frequency and severity of drought."
inner_niger_delta["Climate Change"]["Data Sources"] = [
   "Climate models.",
    "Historical weather records.",
   "Research publications."
]
inner_niger_delta["Climate Change"]["Impact on Area"] = "Indirect; changes in water availability, potentially reducing the size of the wetland."
inner_niger_delta["Climate Change"]["Impact on Biodiversity"] = "Increased stress on plants and animals due to higher temperatures and reduced water availability; shifts in species distributions; changes in phenology."
inner_niger_delta["Climate Change"]["Influenced By"] = [
 "Global Greenhouse Gas Emissions"
]
inner_niger_delta["Climate Change"]["Influences"] = [
 "Wetlands (Inner Niger Delta) - Water Availability",
  "Wetlands (Inner Niger Delta) - Altered Hydrology",
   "Wetlands (Inner Niger Delta) - Wildfires (potentially)"
]
inner_niger_delta["Climate Change"]["Logic Description"] = "Climate change is projected to increase temperatures and alter rainfall patterns in the region, leading to increased water stress and potentially exacerbating the impacts of other stressors on the Inner Niger Delta."
inner_niger_delta["Climate Change"]["Impact Function"] = "impact_climate_change_inner_niger_delta"

inner_niger_delta["Overfishing"]["Metric"] = "Fish catches (tonnes/year); fish population sizes and species composition; fishing effort."
inner_niger_delta["Overfishing"]["Data Sources"] = [
   "Fisheries data (often limited and unreliable).",
     "Local community knowledge.",
     "Research studies."
]
inner_niger_delta["Overfishing"]["Impact on Area"] = "Not directly applicable (affects fish populations, not area)."
inner_niger_delta["Overfishing"]["Impact on Biodiversity"] = "Decline of fish stocks; changes in fish community structure; impacts on the food web (including birds and other animals that depend on fish)."
inner_niger_delta["Overfishing"]["Influenced By"] = [
   "Wetlands (Inner Niger Delta) - Population Growth",
   "Wetlands (Inner Niger Delta) - Poverty and Food Insecurity",
   "Fishing Practices (use of unsustainable methods)",
    "Lack of Effective Fisheries Management"
]
inner_niger_delta["Overfishing"]["Influences"] = [
  "Wetlands (Inner Niger Delta) - Fish Populations",
   "Wetlands (Inner Niger Delta) - Food Web"
]
inner_niger_delta["Overfishing"]["Logic Description"] = "Overfishing, driven by population growth, poverty, and unsustainable fishing practices, is a significant threat to the fish populations of the Inner Niger Delta, impacting both biodiversity and local livelihoods."
inner_niger_delta["Overfishing"]["Impact Function"] = "impact_overfishing_inner_niger_delta"

inner_niger_delta["Population Growth"]["Metric"] = "Human population size and density in and around the Inner Niger Delta; rate of population growth."
inner_niger_delta["Population Growth"]["Data Sources"] = [
  "Census data.",
    "Demographic projections."
]
inner_niger_delta["Population Growth"]["Impact on Area"] = "Increased pressure on natural resources (water, land, fish, fuelwood)."
inner_niger_delta["Population Growth"]["Impact on Biodiversity"] = "Increased demand for resources leads to overexploitation (fishing, grazing, deforestation); habitat loss and degradation."
inner_niger_delta["Population Growth"]["Influenced By"] = [
   "Socioeconomic factors",
    "Migration patterns"
]
inner_niger_delta["Population Growth"]["Influences"] = [
    "Wetlands (Inner Niger Delta) - Overfishing",
  "Wetlands (Inner Niger Delta) - Overgrazing",
  "Wetlands (Inner Niger Delta) - Deforestation",
 "Wetlands (Inner Niger Delta) - Water Diversion",
  "Wetlands (Inner Niger Delta) - Land-Use Change"
]
inner_niger_delta["Population Growth"]["Logic Description"] = "High population growth in the region is a major underlying driver of many stressors, increasing pressure on the Inner Niger Delta's resources."
inner_niger_delta["Population Growth"]["Impact Function"] = "impact_population_growth_inner_niger_delta"

inner_niger_delta["Overgrazing"]["Metric"] = "Livestock density (animals/km²); vegetation cover and composition; soil erosion."
inner_niger_delta["Overgrazing"]["Data Sources"] = [
 "Agricultural statistics.",
  "Vegetation surveys.",
   "Remote sensing data."
]
inner_niger_delta["Overgrazing"]["Impact on Area"] = "Degradation of grasslands and other vegetation; soil erosion; reduced water infiltration."
inner_niger_delta["Overgrazing"]["Impact on Biodiversity"] = "Loss of palatable plant species; changes in plant community composition; impacts on wildlife that depend on grasslands."
inner_niger_delta["Overgrazing"]["Influenced By"] = [
     "Wetlands (Inner Niger Delta) - Livestock Management Practices",
 "Wetlands (Inner Niger Delta) - Population Growth",
 "Climate Variability (drought)"
]
inner_niger_delta["Overgrazing"]["Influences"] = [
     "Wetlands (Inner Niger Delta) - Soil Erosion",
    "Wetlands (Inner Niger Delta) - Desertification (in surrounding areas)",
    "Wetlands (Inner Niger Delta) - Vegetation Changes"
]
inner_niger_delta["Overgrazing"]["Logic Description"] = "Overgrazing by livestock, particularly during the dry season when animals concentrate around water sources, is a significant problem, leading to vegetation degradation and soil erosion."
inner_niger_delta["Overgrazing"]["Impact Function"] = "impact_overgrazing_inner_niger_delta"

inner_niger_delta["Deforestation"]["Metric"] = "Area of forest cleared (ha/year), particularly in the floodplain and surrounding areas."
inner_niger_delta["Deforestation"]["Data Sources"] = [
  "Remote sensing data.",
 "Local reports.",
  "Research studies."
]
inner_niger_delta["Deforestation"]["Impact on Area"] = "Loss of trees within and around the delta."
inner_niger_delta["Deforestation"]["Impact on Biodiversity"] = "Loss of habitat for birds and other wildlife.; Increased soil erosion and sedimentation in the delta.; Reduced availability of fuelwood (impacting local communities)."
inner_niger_delta["Deforestation"]["Influenced By"] = [
  "Wetlands (Inner Niger Delta) - Population Growth",
   "Fuelwood Collection",
   "Agricultural Expansion"
]
inner_niger_delta["Deforestation"]["Influences"] = [
  "Wetlands (Inner Niger Delta) - Water Quality (through increased sedimentation)",
   "Wetlands (Inner Niger Delta) - Habitat Availability"
]
inner_niger_delta["Deforestation"]["Logic Description"] = "Deforestation, driven by population growth and agricultural expansion, is impacting both biodiversity and the livelihoods of communities that depend on forest resources."
inner_niger_delta["Deforestation"]["Impact Function"] = "impact_deforestation_inner_niger_delta"

inner_niger_delta["Water Diversion"]["Metric"] = "Volume of water diverted from the Niger River and its tributaries for irrigation and other uses (m³/year)."
inner_niger_delta["Water Diversion"]["Data Sources"] = [
 "Water management records (Mali and other upstream countries).",
    "Research studies."
]
inner_niger_delta["Water Diversion"]["Impact on Area"] = "Reduced inflow to the Inner Niger Delta, shrinking the flooded area and impacting wetland habitats."
inner_niger_delta["Water Diversion"]["Impact on Biodiversity"] = "Impacts on fish, birds, and other wildlife that depend on the annual flood pulse; changes in vegetation communities."
inner_niger_delta["Water Diversion"]["Influenced By"] = [
  "Upstream Irrigation Projects",
  "Population Growth",
   "Agricultural Policies"
]
inner_niger_delta["Water Diversion"]["Influences"] = [
 "Wetlands (Inner Niger Delta) - Altered Hydrology",
 "Wetlands (Inner Niger Delta) - Habitat Availability"
]
inner_niger_delta["Water Diversion"]["Logic Description"] = "Water diversions for irrigation and other uses, both upstream and within the delta, reduce the amount of water reaching the Inner Niger Delta, impacting its size and ecological function."
inner_niger_delta["Water Diversion"]["Impact Function"] = "impact_water_diversion_inner_niger_delta"

inner_niger_delta["Pollution"]["Metric"] = "Concentrations of pollutants in water and sediment."
inner_niger_delta["Pollution"]["Data Sources"] = [
    "Limited water quality data",
    "Research Studies"
]
inner_niger_delta["Pollution"]["Impact on Area"] = "Degraded water quality."
inner_niger_delta["Pollution"]["Impact on Biodiversity"] = "Impacts on fish and other aquatic life."
inner_niger_delta["Pollution"]["Influenced By"] = [
 "Agricultural Runoff",
    "Urban Waste"
]
inner_niger_delta["Pollution"]["Influences"] = [
     "Wetlands (Inner Niger Delta) - Water Quality"
]
inner_niger_delta["Pollution"]["Logic Description"] = "Pollution, though less well-studied than some other stressors, is a growing concern."
inner_niger_delta["Pollution"]["Impact Function"] = "impact_pollution_inner_niger_delta"

# --- Wetlands (Mesopotamian Marshes) ---
mesopotamian_marshes = all_stressors_data["Mesopotamian Marshes Wetlands"]

mesopotamian_marshes["Water Diversion"]["Metric"] = "Water flow rates in the Tigris and Euphrates rivers; water levels in the marshes; area of marshland inundated."
mesopotamian_marshes["Water Diversion"]["Data Sources"] = [
    "Iraqi government data (Ministry of Water Resources).",
    "Turkish government data (Ministry of Agriculture and Forestry).",
    "Syrian government data.",
    "Remote sensing data (satellite imagery).",
    "Research publications.",
    "United Nations reports (e.g., UNEP)."
]
mesopotamian_marshes["Water Diversion"]["Impact on Area"] = "*Drastic* reduction in the extent of the marshes (historically, the *major* stressor).  Large areas have been completely desiccated."
mesopotamian_marshes["Water Diversion"]["Impact on Biodiversity"] = "Massive habitat loss for marsh-dependent species (fish, birds, mammals, invertebrates).  Near-collapse of the traditional Marsh Arab way of life.  Loss of biodiversity and ecosystem services."
mesopotamian_marshes["Water Diversion"]["Influenced By"] = [
    "Wetlands (Mesopotamian Marshes) - Upstream Dam Construction",
    "Irrigation Projects (in Turkey, Syria, and Iraq)",
    "Government Policies (water management)",
    "Past Drainage Projects (intentional draining of the marshes under Saddam Hussein)"
]
mesopotamian_marshes["Water Diversion"]["Influences"] = [
     "Wetlands (Mesopotamian Marshes) - Habitat Availability",
    "Wetlands (Mesopotamian Marshes) - Salinization",
    "Wetlands (Mesopotamian Marshes) - Water Quality"
]
mesopotamian_marshes["Water Diversion"]["Logic Description"] = "The Mesopotamian Marshes have been drastically reduced in size due to massive water diversions from the Tigris and Euphrates rivers, primarily for upstream dam construction and irrigation projects. Intentional drainage of the marshes also played a significant role historically. This is one of the most significant cases of wetland loss globally."
mesopotamian_marshes["Water Diversion"]["Impact Function"] = "impact_water_diversion_mesopotamian_marshes"

mesopotamian_marshes["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., salts, heavy metals, pesticides, oil) in water, sediment, and biota."
mesopotamian_marshes["Pollution"]["Data Sources"] = [
    "Water quality monitoring data (limited availability).",
   "Research studies."
]
mesopotamian_marshes["Pollution"]["Impact on Area"] = "Degradation of water quality."
mesopotamian_marshes["Pollution"]["Impact on Biodiversity"] = "Toxic effects on wildlife; impacts on food webs; impacts on human health (for Marsh Arabs)."
mesopotamian_marshes["Pollution"]["Influenced By"] = [
  "Agricultural Runoff (upstream)",
   "Industrial Discharge (upstream)",
   "Oil Industry Activities",
  "Untreated Sewage",
 "Military Activities (past conflicts)"
]
mesopotamian_marshes["Pollution"]["Influences"] = [
    "Wetlands (Mesopotamian Marshes) - Water Quality",
   "Wetlands (Mesopotamian Marshes) - Wildlife Health",
  "Human Health"
]
mesopotamian_marshes["Pollution"]["Logic Description"] = "Pollution from upstream agriculture, industry, oil activities, and untreated sewage degrades water quality in the marshes, impacting wildlife and human health."
mesopotamian_marshes["Pollution"]["Impact Function"] = "impact_pollution_mesopotamian_marshes"

mesopotamian_marshes["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality); increased frequency of drought."
mesopotamian_marshes["Climate Change"]["Data Sources"] = [
    "Climate models",
   "Historical weather records."
]
mesopotamian_marshes["Climate Change"]["Impact on Area"] = "Increased evaporation rates; reduced water availability; exacerbation of existing water stress."
mesopotamian_marshes["Climate Change"]["Impact on Biodiversity"] = "Increased stress on marsh ecosystems; potential shifts in species distributions."
mesopotamian_marshes["Climate Change"]["Influenced By"] = ["Global GHG"]
mesopotamian_marshes["Climate Change"]["Influences"] = [
  "Wetlands (Mesopotamian Marshes) - Water Availability"
]
mesopotamian_marshes["Climate Change"]["Logic Description"] = "Climate change is projected to increase temperatures and potentially reduce rainfall in the region, further exacerbating water scarcity and stress on the marshes."
mesopotamian_marshes["Climate Change"]["Impact Function"] = "impact_climate_change_mesopotamian_marshes"

mesopotamian_marshes["Salinization"]["Metric"] = "Salt concentrations in water and soil."
mesopotamian_marshes["Salinization"]["Data Sources"] = [
    "Water and soil quality monitoring data.",
   "Research studies."
]
mesopotamian_marshes["Salinization"]["Impact on Area"] = "Degradation of water and soil quality; reduced suitability for freshwater species."
mesopotamian_marshes["Salinization"]["Impact on Biodiversity"] = "Impacts on freshwater plants and animals; shifts in species composition towards more salt-tolerant species."
mesopotamian_marshes["Salinization"]["Influenced By"] = [
   "Wetlands (Mesopotamian Marshes) - Reduced Freshwater Inflow",
    "Wetlands (Mesopotamian Marshes) - Water Diversion",
    "Irrigation Practices (leading to salt buildup in soils)"
]
mesopotamian_marshes["Salinization"]["Influences"] = [
   "Wetlands (Mesopotamian Marshes) - Water Quality",
    "Wetlands (Mesopotamian Marshes) - Soil Quality"
]
mesopotamian_marshes["Salinization"]["Logic Description"] = "Reduced freshwater inflow to the marshes, due to upstream water diversions and climate change, is leading to increased salinity, impacting freshwater species and overall ecosystem health."
mesopotamian_marshes["Salinization"]["Impact Function"] = "impact_salinization_mesopotamian_marshes"

mesopotamian_marshes["Upstream Dam Construction"]["Metric"] = "Number and capacity of dams on the Tigris and Euphrates rivers; changes in water flow and sediment transport."
mesopotamian_marshes["Upstream Dam Construction"]["Data Sources"] = [
    "Government reports (Turkey, Syria, Iran, Iraq).",
   "International organizations (e.g., UN agencies).",
    "Research publications."
]
mesopotamian_marshes["Upstream Dam Construction"]["Impact on Area"] = "*Drastic* reduction in water flow to the marshes; altered sediment delivery."
mesopotamian_marshes["Upstream Dam Construction"]["Impact on Biodiversity"] = "Loss of wetland habitat; impacts on fish migration and spawning; changes in vegetation communities."
mesopotamian_marshes["Upstream Dam Construction"]["Influenced By"] = [
 "Water Resource Management Policies (in upstream countries)",
    "Hydropower Development",
   "Irrigation Projects"
]
mesopotamian_marshes["Upstream Dam Construction"]["Influences"] = [
     "Wetlands (Mesopotamian Marshes) - Water Diversion",
    "Wetlands (Mesopotamian Marshes) - Altered Hydrology",
 "Wetlands (Mesopotamian Marshes) - Sedimentation"
]
mesopotamian_marshes["Upstream Dam Construction"]["Logic Description"] = "Extensive dam construction on the Tigris and Euphrates rivers in Turkey, Syria, and Iraq has drastically reduced water flow to the Mesopotamian Marshes, leading to their desiccation. This is the *primary* driver of the changes to the marshes."
mesopotamian_marshes["Upstream Dam Construction"]["Impact Function"] = "impact_upstream_dam_construction_mesopotamian_marshes"

# --- Wetlands (Okavango Delta) ---
okavango_delta = all_stressors_data["Okavango Delta Wetlands"]

okavango_delta["Water Diversion"]["Metric"] = "Amount of water extracted from the Okavango River system upstream of the delta (cubic meters/year)."
okavango_delta["Water Diversion"]["Data Sources"] = [
    "Government data (Botswana, Namibia, Angola).",
    "International agreements (e.g., OKACOM - Permanent Okavango River Basin Water Commission).",
   "Research studies."
]
okavango_delta["Water Diversion"]["Impact on Area"] = "Reduced inflow to the delta, potentially shrinking the flooded area."
okavango_delta["Water Diversion"]["Impact on Biodiversity"] = "Impacts on fish populations.; Impacts on wading bird populations.; Changes in vegetation communities.; Reduced habitat availability for wildlife."
okavango_delta["Water Diversion"]["Influenced By"] = [
        "Wetlands (Okavango Delta) - Upstream Water Demand",
     "Wetlands (Okavango Delta) - Government Policies"
]
okavango_delta["Water Diversion"]["Influences"] = [
        "Wetlands (Okavango Delta) - Habitat Availability"
]
okavango_delta["Water Diversion"]["Logic Description"] = "The Okavango Delta is dependent on inflows from the Okavango River. Increased water extraction upstream, for agriculture and other uses, could significantly reduce the amount of water reaching the delta, impacting its size and ecological function."
okavango_delta["Water Diversion"]["Impact Function"] = "impact_water_diversion_okavango_delta"

okavango_delta["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality)."
okavango_delta["Climate Change"]["Data Sources"] = [
 "Climate Models",
  "Historical Records"
]
okavango_delta["Climate Change"]["Impact on Area"] = "Indirect, through changes in water balance."
okavango_delta["Climate Change"]["Impact on Biodiversity"] = "Shifts in species; Increased stress.; Changes in phenology."
okavango_delta["Climate Change"]["Influenced By"] = [
    "Global GHG"
]
okavango_delta["Climate Change"]["Influences"] = [
        "Wetlands (Okavango Delta) - Hydrology"
]
okavango_delta["Climate Change"]["Logic Description"] = "Climate change is expected to alter temperature and precipitation patterns in the Okavango Basin, potentially impacting the delta's hydrology and biodiversity."
okavango_delta["Climate Change"]["Impact Function"] = "impact_climate_change_okavango_delta"

okavango_delta["Pollution"]["Metric"] = "Concentration of pollutants in water and sediment."
okavango_delta["Pollution"]["Data Sources"] = [
    "Water quality monitoring.",
    "Research studies."
]
okavango_delta["Pollution"]["Impact on Area"] = "Water quality degradation."
okavango_delta["Pollution"]["Impact on Biodiversity"] = "Toxic effects.; Impacts on food webs."
okavango_delta["Pollution"]["Influenced By"] = [
        "Wetlands (Okavango Delta) - Tourism",
        "Wetlands (Okavango Delta) - Agricultural Runoff",
       "Wetlands (Okavango Delta) - Upstream Development"
]
okavango_delta["Pollution"]["Influences"] = [
     "Wetlands (Okavango Delta) - Water Quality",
   "Wetlands (Okavango Delta) - Wildlife Health"
]
okavango_delta["Pollution"]["Logic Description"] = "While currently relatively pristine, the Okavango Delta is vulnerable to pollution from tourism, agriculture, and upstream development."
okavango_delta["Pollution"]["Impact Function"] = "impact_pollution_okavango_delta"

okavango_delta["Overfishing"]["Metric"] = "Fish catches (tonnes/year); fish population sizes."
okavango_delta["Overfishing"]["Data Sources"] = [
    "Fisheries data (where available).",
        "Research studies."
]
okavango_delta["Overfishing"]["Impact on Area"] = "N/A"
okavango_delta["Overfishing"]["Impact on Biodiversity"] = "Decline of fish populations.; Impacts on the food web (e.g., on fish-eating birds and mammals)."
okavango_delta["Overfishing"]["Influenced By"] = [
     "Wetlands (Okavango Delta) - Population Growth",
      "Fishing Practices"
]
okavango_delta["Overfishing"]["Influences"] = [
     "Wetlands (Okavango Delta) - Fish Populations",
       "Wetlands (Okavango Delta) - Food Web"
]
okavango_delta["Overfishing"]["Logic Description"] = "Overfishing can deplete fish stocks, impacting the food web."
okavango_delta["Overfishing"]["Impact Function"] = "impact_overfishing_okavango_delta"

okavango_delta["Invasive Species"]["Metric"] = "Abundance/distribution of key invasive species."
okavango_delta["Invasive Species"]["Data Sources"] = [
       "Research",
       "Monitoring"
]
okavango_delta["Invasive Species"]["Impact on Area"] = "Changes in vegetation (e.g., aquatic weeds)."
okavango_delta["Invasive Species"]["Impact on Biodiversity"] = "Competition with native species.; Alteration of habitat."
okavango_delta["Invasive Species"]["Influenced By"] = [
   "Wetlands (Okavango Delta) - Human Activities",
   "Wetlands (Okavango Delta) - Climate Change"
]
okavango_delta["Invasive Species"]["Influences"] = [
        "Wetlands (Okavango Delta) - Native Species"
]
okavango_delta["Invasive Species"]["Logic Description"] = "Invasive aquatic plants (e.g., Salvinia molesta) can clog waterways and reduce habitat quality."
okavango_delta["Invasive Species"]["Impact Function"] = "impact_invasive_species_okavango_delta"

okavango_delta["Upstream Water Demand"]["Metric"] = "Water use by sector (agriculture, urban, etc.) upstream of the delta."
okavango_delta["Upstream Water Demand"]["Data Sources"] = ["Government data (Angola, Namibia)."]
okavango_delta["Upstream Water Demand"]["Impact on Area"] = "Reduced inflow to the delta."
okavango_delta["Upstream Water Demand"]["Impact on Biodiversity"] = "Habitat loss"
okavango_delta["Upstream Water Demand"]["Influenced By"] = [
    "Population growth",
  "Economic Development"
]
okavango_delta["Upstream Water Demand"]["Influences"] = [
      "Wetlands (Okavango Delta) - Water Diversion"
]
okavango_delta["Upstream Water Demand"]["Logic Description"] = "Upstream water use reduces inflow."
okavango_delta["Upstream Water Demand"]["Impact Function"] = "impact_upstream_water_demand_okavango_delta"

okavango_delta["Government Policies"]["Metric"] = "Water management policies, conservation regulations."
okavango_delta["Government Policies"]["Data Sources"] = [
     "Policy documents, legal frameworks."
]
okavango_delta["Government Policies"]["Impact on Area"] = "Variable, can be positive or negative."
okavango_delta["Government Policies"]["Impact on Biodiversity"] = "Variable, can be positive or negative."
okavango_delta["Government Policies"]["Influenced By"] = [
     "Politics",
  "Economics",
   "International agreements"
]
okavango_delta["Government Policies"]["Influences"] = [
     "Wetlands (Okavango Delta) - Water Diversion"
]
okavango_delta["Government Policies"]["Logic Description"] = "Government policy shapes resource management."
okavango_delta["Government Policies"]["Impact Function"] = "impact_government_policies_okavango_delta"

okavango_delta["Tourism"]["Metric"] = "Number of tourists, infrastructure development."
okavango_delta["Tourism"]["Data Sources"] = ["Tourism statistics"]
okavango_delta["Tourism"]["Impact on Area"] = "Localized impacts, potential for pollution and disturbance."
okavango_delta["Tourism"]["Impact on Biodiversity"] = "Disturbance to wildlife."
okavango_delta["Tourism"]["Influenced By"] = [
    "Economic factors",
 "Accessibility"
]
okavango_delta["Tourism"]["Influences"] = [
     "Wetlands (Okavango Delta) - Pollution"
]
okavango_delta["Tourism"]["Logic Description"] = "Tourism impacts."
okavango_delta["Tourism"]["Impact Function"] = "impact_tourism_okavango_delta"

okavango_delta["Agricultural Runoff"]["Metric"] = "Nutrient and pesticide concentrations in water."
okavango_delta["Agricultural Runoff"]["Data Sources"] = ["Water quality monitoring data."]
okavango_delta["Agricultural Runoff"]["Impact on Area"] = "Water quality degradation."
okavango_delta["Agricultural Runoff"]["Impact on Biodiversity"] = "Potential for eutrophication and toxic effects."
okavango_delta["Agricultural Runoff"]["Influenced By"] = [
   "Agricultural practices upstream."
]
okavango_delta["Agricultural Runoff"]["Influences"] = [
  "Wetlands (Okavango Delta) - Pollution"
]
okavango_delta["Agricultural Runoff"]["Logic Description"] = "Runoff from agricultural areas."
okavango_delta["Agricultural Runoff"]["Impact Function"] = "impact_agricultural_runoff_okavango_delta"

# --- Wetlands (Pantanal) ---
pantanal = all_stressors_data["Pantanal Wetlands"]

pantanal["Land-Use Change"]["Metric"] = "Area converted to agriculture (primarily cattle ranching) and other land uses (ha/year)."
pantanal["Land-Use Change"]["Data Sources"] = [
    "Remote sensing data.",
    "Brazilian, Bolivian, and Paraguayan government data.",
     "Research publications."
]
pantanal["Land-Use Change"]["Impact on Area"] = "Loss of wetland and savanna habitat; fragmentation."
pantanal["Land-Use Change"]["Impact on Biodiversity"] = "Habitat loss and fragmentation.; Impacts on wildlife populations (e.g., jaguars, giant anteaters, hyacinth macaws).; Increased human-wildlife conflict."
pantanal["Land-Use Change"]["Influenced By"] = [
    "Wetlands (Pantanal) - Agricultural Expansion",
    "Wetlands (Pantanal) - Economic Growth",
   "Wetlands (Pantanal) - Government Policies",
    "Wetlands (Pantanal) - Infrastructure Development"
]
pantanal["Land-Use Change"]["Influences"] = [
"Wetlands (Pantanal) - Habitat Fragmentation"
]
pantanal["Land-Use Change"]["Logic Description"] = "Conversion of Pantanal habitat to cattle pasture is a growing threat, leading to habitat loss and fragmentation."
pantanal["Land-Use Change"]["Impact Function"] = "impact_land_use_change_pantanal"

pantanal["Altered Hydrology"]["Metric"] = "Changes in water levels, flooding patterns, and river flow."
pantanal["Altered Hydrology"]["Data Sources"] = [
    "Hydrological monitoring data (river gauges).",
     "Remote sensing data.",
    "Research studies."
]
pantanal["Altered Hydrology"]["Impact on Area"] = "Changes in the extent and duration of flooding, affecting wetland habitats."
pantanal["Altered Hydrology"]["Impact on Biodiversity"] = "Impacts on fish populations (spawning and migration).; Impacts on aquatic invertebrates.; Impacts on wading bird populations.; Changes in vegetation communities."
pantanal["Altered Hydrology"]["Influenced By"] = [
  "Wetlands (Pantanal) - Upstream Dam Construction",
 "Wetlands (Pantanal) - Climate Change",
  "Wetlands (Pantanal) - Deforestation",
 "Wetlands (Pantanal) - Water Diversion"
]
pantanal["Altered Hydrology"]["Influences"] = [
       "Wetlands (Pantanal) - Habitat Availability"
]
pantanal["Altered Hydrology"]["Logic Description"] = "The Pantanal's ecology is driven by its annual flood pulse. Dams, climate change, and deforestation are altering this."
pantanal["Altered Hydrology"]["Impact Function"] = "impact_altered_hydrology_pantanal"

pantanal["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., mercury, pesticides, sediment) in water and sediments."
pantanal["Pollution"]["Data Sources"] = [
    "Water quality monitoring data.",
  "Research studies."
]
pantanal["Pollution"]["Impact on Area"] = "Water quality degradation."
pantanal["Pollution"]["Impact on Biodiversity"] = "Toxic effects on wildlife (e.g., mercury contamination in fish).; Impacts on aquatic food webs."
pantanal["Pollution"]["Influenced By"] = [
  "Wetlands (Pantanal) - Mining Activities",
   "Wetlands (Pantanal) - Agricultural Runoff",
 "Wetlands (Pantanal) - Deforestation"
]
pantanal["Pollution"]["Influences"] = [
    "Wetlands (Pantanal) - Water Quality",
  "Wetlands (Pantanal) - Wildlife Health"
]
pantanal["Pollution"]["Logic Description"] = "Pollution from mining, agriculture, and deforestation degrades water quality and impacts wildlife."
pantanal["Pollution"]["Impact Function"] = "impact_pollution_pantanal"

pantanal["Climate Change"]["Metric"] = "Temperature, Precipitation, increased frequency of extreme weather events."
pantanal["Climate Change"]["Data Sources"] = [
   "Climate models",
   "Historical data"
]
pantanal["Climate Change"]["Impact on Area"] = "Indirect"
pantanal["Climate Change"]["Impact on Biodiversity"] = "Shifts in Species; Increased stress.; Changes in phenology."
pantanal["Climate Change"]["Influenced By"] = [
"Global GHG"
]
pantanal["Climate Change"]["Influences"] = [
    "Wetlands (Pantanal) - Hydrology",
   "Wetlands (Pantanal) - Wildfires"
]
pantanal["Climate Change"]["Logic Description"] = "Climate change impacts"
pantanal["Climate Change"]["Impact Function"] = "impact_climate_change_pantanal"

pantanal["Wildfires"]["Metric"] = "Number of fires, and area burned."
pantanal["Wildfires"]["Data Sources"] = [
    "Remote Sensing",
   "Local Reports"
]
pantanal["Wildfires"]["Impact on Area"] = "Direct loss"
pantanal["Wildfires"]["Impact on Biodiversity"] = "Mortality; Habitat loss"
pantanal["Wildfires"]["Influenced By"] = [
    "Wetlands (Pantanal) - Deforestation",
"Wetlands (Pantanal) - Temperature",
"Wetlands (Pantanal) - Changes in Precipitation",
"Wetlands (Pantanal) - Human Activities."
]
pantanal["Wildfires"]["Influences"] = [
   "Wetlands (Pantanal) - Air Quality"
]
pantanal["Wildfires"]["Logic Description"] = "Wildfires exacerbated by human activities and climate."
pantanal["Wildfires"]["Impact Function"] = "impact_wildfires_pantanal"

pantanal["Agricultural Expansion"]["Metric"] = "Area converted to agriculture"
pantanal["Agricultural Expansion"]["Data Sources"] = ["Remote Sensing", "Government Data"]
pantanal["Agricultural Expansion"]["Impact on Area"] = "Habitat Loss"
pantanal["Agricultural Expansion"]["Impact on Biodiversity"] = "Species loss"
pantanal["Agricultural Expansion"]["Influenced By"] = ["Global Demand"]
pantanal["Agricultural Expansion"]["Influences"] = [
      "Wetlands (Pantanal) - Land-Use Change"
]
pantanal["Agricultural Expansion"]["Logic Description"] = "Demand for agricultural land."
pantanal["Agricultural Expansion"]["Impact Function"] = "impact_agricultural_expansion_pantanal"

pantanal["Economic Growth"]["Metric"] = "GDP, etc."
pantanal["Economic Growth"]["Data Sources"] = ["Economic indicators"]
pantanal["Economic Growth"]["Impact on Area"] = "Indirect, via increased resource demand"
pantanal["Economic Growth"]["Impact on Biodiversity"] = "Habitat Loss"
pantanal["Economic Growth"]["Influenced By"] = ["Global Markets"]
pantanal["Economic Growth"]["Influences"] = [
     "Wetlands (Pantanal) - Land-Use Change",
     "Wetlands (Pantanal) - Agricultural Expansion",
   "Wetlands (Pantanal) - Infrastructure Development"
]
pantanal["Economic Growth"]["Logic Description"] = "Economic development pressures."
pantanal["Economic Growth"]["Impact Function"] = "impact_economic_growth_pantanal"

pantanal["Government Policies"]["Metric"] = "Land use regulations, environmental protections"
pantanal["Government Policies"]["Data Sources"] = ["Policy Documents"]
pantanal["Government Policies"]["Impact on Area"] = "Variable"
pantanal["Government Policies"]["Impact on Biodiversity"] = "Variable"
pantanal["Government Policies"]["Influenced By"] = [
 "Politics",
  "Economics"
]
pantanal["Government Policies"]["Influences"] = [
      "Wetlands (Pantanal) - Land-Use Change"
]
pantanal["Government Policies"]["Logic Description"] = "Policy can have positive or negative impacts."
pantanal["Government Policies"]["Impact Function"] = "impact_government_policies_pantanal"

pantanal["Infrastructure Development"]["Metric"] = "Roads, dams, etc."
pantanal["Infrastructure Development"]["Data Sources"] = ["Government Records"]
pantanal["Infrastructure Development"]["Impact on Area"] = "Fragmentation"
pantanal["Infrastructure Development"]["Impact on Biodiversity"] = "Habitat Loss"
pantanal["Infrastructure Development"]["Influenced By"] = [
      "Wetlands (Pantanal) - Economic Growth"
]
pantanal["Infrastructure Development"]["Influences"] = [
  "Wetlands (Pantanal) - Habitat Fragmentation",
 "Wetlands (Pantanal) - Land Use Change"
]
pantanal["Infrastructure Development"]["Logic Description"] = "Infrastructure projects can damage habitat."
pantanal["Infrastructure Development"]["Impact Function"] = "impact_infrastructure_development_pantanal"

pantanal["Upstream Dam Construction"]["Metric"] = "Number and capacity of upstream dams."
pantanal["Upstream Dam Construction"]["Data Sources"] = ["Government records", "Research"]
pantanal["Upstream Dam Construction"]["Impact on Area"] = "Altered hydrology."
pantanal["Upstream Dam Construction"]["Impact on Biodiversity"] = "Impacts on flooding and species."
pantanal["Upstream Dam Construction"]["Influenced By"] = ["Energy demand", "Water management"]
pantanal["Upstream Dam Construction"]["Influences"] = ["Wetlands (Pantanal) - Altered Hydrology"]
pantanal["Upstream Dam Construction"]["Logic Description"] = "Dams upstream affect water flow to the Pantanal."
pantanal["Upstream Dam Construction"]["Impact Function"] = "impact_upstream_dam_construction_pantanal"

pantanal["Deforestation"]["Metric"] = "Area of forest cleared (ha/year)."
pantanal["Deforestation"]["Data Sources"] = [
    "Remote sensing",
    "Government data"
    ]
pantanal["Deforestation"]["Impact on Area"] = "Reduced forest cover."
pantanal["Deforestation"]["Impact on Biodiversity"] = "Habitat loss and fragmentation."
pantanal["Deforestation"]["Influenced By"] = [
"Agricultural expansion",
"Land-use change"
]
pantanal["Deforestation"]["Influences"] = [
"Wetlands (Pantanal) - Altered Hydrology",
"Wetlands (Pantanal) - Pollution",
"Wetlands (Pantanal) - Wildfires"
]
pantanal["Deforestation"]["Logic Description"] = "Deforestation contributes to various other stressors."
pantanal["Deforestation"]["Impact Function"] = "impact_deforestation_pantanal"

pantanal["Water Diversion"]["Metric"] = "Volume of water diverted."
pantanal["Water Diversion"]["Data Sources"] = [
"Government records.",
"Research studies."
]
pantanal["Water Diversion"]["Impact on Area"] = "Reduced water flow."
pantanal["Water Diversion"]["Impact on Biodiversity"] = "Impacts to aquatic species"
pantanal["Water Diversion"]["Influenced By"] = [
"Agriculture",
"Upstream water demand"
]
pantanal["Water Diversion"]["Influences"] = [
"Wetlands (Pantanal) - Altered Hydrology"
]
pantanal["Water Diversion"]["Logic Description"] = "Water extraction reduces the Pantanal's flood pulse."
pantanal["Water Diversion"]["Impact Function"] = "impact_water_diversion_pantanal"

pantanal["Mining Activities"]["Metric"] = "Number of mines and area affected; pollutant levels."
pantanal["Mining Activities"]["Data Sources"] = [
"Government records",
"Research studies."
]
pantanal["Mining Activities"]["Impact on Area"] = "Pollution; habitat destruction."
pantanal["Mining Activities"]["Impact on Biodiversity"] = "Toxic effects on wildlife."
pantanal["Mining Activities"]["Influenced By"] = [
"Economic factors"
]
pantanal["Mining Activities"]["Influences"] = [
"Wetlands (Pantanal) - Pollution"
]
pantanal["Mining Activities"]["Logic Description"] = "Mining releases pollutants into the environment."
pantanal["Mining Activities"]["Impact Function"] = "impact_mining_activities_pantanal"

pantanal["Agricultural Runoff"]["Metric"] = "Nutrient and pesticide concentrations in water."
pantanal["Agricultural Runoff"]["Data Sources"] = ["Water quality monitoring."]
pantanal["Agricultural Runoff"]["Impact on Area"] = "Water quality degradation."
pantanal["Agricultural Runoff"]["Impact on Biodiversity"] = "Eutrophication; toxic effects."
pantanal["Agricultural Runoff"]["Influenced By"] = [
"Agricultural practices"
]
pantanal["Agricultural Runoff"]["Influences"] = [
"Wetlands (Pantanal) - Pollution"
]
pantanal["Agricultural Runoff"]["Logic Description"] = "Runoff carries pollutants from agricultural areas."
pantanal["Agricultural Runoff"]["Impact Function"] = "impact_agricultural_runoff_pantanal"

pantanal["Wildlife Health"]["Metric"] = "Disease prevalence, mortality rates, contaminant levels in wildlife."
pantanal["Wildlife Health"]["Data Sources"] = [
"Wildlife monitoring data",
"Research studies."
]
pantanal["Wildlife Health"]["Impact on Area"] = "Indirect, through impacts on populations."
pantanal["Wildlife Health"]["Impact on Biodiversity"] = "Population declines."
pantanal["Wildlife Health"]["Influenced By"] = [
"Wetlands (Pantanal) - Pollution"
]
pantanal["Wildlife Health"]["Influences"] = [
"Population Dynamics"
]
pantanal["Wildlife Health"]["Logic Description"] = "Wildlife health is an indicator of overall ecosystem health."
pantanal["Wildlife Health"]["Impact Function"] = "impact_wildlife_health_pantanal"

pantanal["Temperature"]["Metric"] = "Average and extreme temperatures."
pantanal["Temperature"]["Data Sources"] = [
"Climate data"
]
pantanal["Temperature"]["Impact on Area"] = "Indirect."
pantanal["Temperature"]["Impact on Biodiversity"] = "Species stress"
pantanal["Temperature"]["Influenced By"] = [
"Wetlands (Pantanal) - Climate Change"
]
pantanal["Temperature"]["Influences"] = [
"Wetlands (Pantanal) - Wildfires"
]
pantanal["Temperature"]["Logic Description"] = "Temperature is a key environmental variable."
pantanal["Temperature"]["Impact Function"] = "impact_temperature_pantanal"

pantanal["Changes in Precipitation"]["Metric"] = "Rainfall amount, seasonality."
pantanal["Changes in Precipitation"]["Data Sources"] = [
"Climate data"
]
pantanal["Changes in Precipitation"]["Impact on Area"] = "Water availability."
pantanal["Changes in Precipitation"]["Impact on Biodiversity"] = "Impacts many species."
pantanal["Changes in Precipitation"]["Influenced By"] = [
"Wetlands (Pantanal) - Climate Change"
]
pantanal["Changes in Precipitation"]["Influences"] = [
"Wetlands (Pantanal) - Wildfires"
]
pantanal["Changes in Precipitation"]["Logic Description"] = "Rainfall patterns are crucial for wetlands."
pantanal["Changes in Precipitation"]["Impact Function"] = "impact_precipitation_changes_pantanal"

pantanal["Human Activities"]["Metric"] = "Varies."
pantanal["Human Activities"]["Data Sources"] = [
"Varies."
]
pantanal["Human Activities"]["Impact on Area"] = "Variable."
pantanal["Human Activities"]["Impact on Biodiversity"] = "Variable."
pantanal["Human Activities"]["Influenced By"] = [
"Many factors."
]
pantanal["Human Activities"]["Influences"] = [
"Wetlands (Pantanal) - Wildfires"
]
pantanal["Human Activities"]["Logic Description"] = "General category for human impacts."
pantanal["Human Activities"]["Impact Function"] = "impact_human_activities_pantanal"

pantanal["Air Quality"]["Metric"] = "Air pollution levels."
pantanal["Air Quality"]["Data Sources"] = [
"Air quality monitoring."
]
pantanal["Air Quality"]["Impact on Area"] = "Air quality."
pantanal["Air Quality"]["Impact on Biodiversity"] = "Respiratory issues."
pantanal["Air Quality"]["Influenced By"] = [
"Wetlands (Pantanal) - Wildfires"
]
pantanal["Air Quality"]["Influences"] = [
"Human and Wildlife health"
]
pantanal["Air Quality"]["Logic Description"] = "Air quality, often linked to fires."
pantanal["Air Quality"]["Impact Function"] = "impact_air_quality_pantanal"

pantanal["Habitat Availability"]["Metric"] = "Extent of suitable habitat."
pantanal["Habitat Availability"]["Data Sources"] = ["Remote Sensing"]
pantanal["Habitat Availability"]["Impact on Area"] = "Directly related"
pantanal["Habitat Availability"]["Impact on Biodiversity"] = "Crucial for species survival"
pantanal["Habitat Availability"]["Influenced By"] = [
"Wetlands (Pantanal) - Altered Hydrology",
"Wetlands (Pantanal) - Land-Use Change"
]
pantanal["Habitat Availability"]["Influences"] = [
"Many"
]
pantanal["Habitat Availability"]["Logic Description"] = "Habitat is fundamental"
pantanal["Habitat Availability"]["Impact Function"] = "impact_habitat_availability_pantanal"

pantanal["Water Quality"]["Metric"] = "Various water quality parameters."
pantanal["Water Quality"]["Data Sources"] = [
"Water monitoring."
]
pantanal["Water Quality"]["Impact on Area"] = "Overall water quality."
pantanal["Water Quality"]["Impact on Biodiversity"] = "Impacts aquatic life."
pantanal["Water Quality"]["Influenced By"] = [
"Wetlands (Pantanal) - Pollution"
]
pantanal["Water Quality"]["Influences"] = [
"Many."
]
pantanal["Water Quality"]["Logic Description"] = "Water quality affects everything."
pantanal["Water Quality"]["Impact Function"] = "impact_water_quality_pantanal"

pantanal["Habitat Fragmentation"]["Metric"] = "Patch size, connectivity."
pantanal["Habitat Fragmentation"]["Data Sources"] = ["Remote Sensing"]
pantanal["Habitat Fragmentation"]["Impact on Area"] = "Increased fragmentation."
pantanal["Habitat Fragmentation"]["Impact on Biodiversity"] = "Reduced movement, genetic isolation."
pantanal["Habitat Fragmentation"]["Influenced By"] = [
"Wetlands (Pantanal) - Land-Use Change",
"Wetlands (Pantanal) - Infrastructure Development"
]
pantanal["Habitat Fragmentation"]["Influences"] = [
"Population dynamics"
]
pantanal["Habitat Fragmentation"]["Logic Description"] = "Fragmentation reduces connectivity."
pantanal["Habitat Fragmentation"]["Impact Function"] = "impact_habitat_fragmentation_pantanal"

pantanal["Global Demand"]["Metric"] = "Demand for agricultural products, minerals."
pantanal["Global Demand"]["Data Sources"] = ["Economic Data"]
pantanal["Global Demand"]["Impact on Area"] = "Indirect, drives resource extraction."
pantanal["Global Demand"]["Impact on Biodiversity"] = "Indirect, through habitat loss."
pantanal["Global Demand"]["Influenced By"] = ["Global markets"]
pantanal["Global Demand"]["Influences"] = [
"Wetlands (Pantanal) - Agricultural Expansion"
]
pantanal["Global Demand"]["Logic Description"] = "Global demand affects local land use."
pantanal["Global Demand"]["Impact Function"] = "impact_global_demand_pantanal"

pantanal["Water Demand"]["Metric"] = "Water usage by different sectors"
pantanal["Water Demand"]["Data Sources"] = [
"Government records."
]
pantanal["Water Demand"]["Impact on Area"] = "Water availability in the Pantanal"
pantanal["Water Demand"]["Impact on Biodiversity"] = "Habitat Loss"
pantanal["Water Demand"]["Influenced By"] = [
"Upstream water use",
"Population growth"
]
pantanal["Water Demand"]["Influences"] = [
"Wetlands (Pantanal) - Water Diversion"
]
pantanal["Water Demand"]["Logic Description"] = "Competition for water resources."
pantanal["Water Demand"]["Impact Function"] = "impact_water_demand_pantanal"

pantanal["Politics"]["Metric"] = "Political stability, governance."
pantanal["Politics"]["Data Sources"] = ["News reports, political analysis."]
pantanal["Politics"]["Impact on Area"] = "Variable, can influence policy."
pantanal["Politics"]["Impact on Biodiversity"] = "Variable, depending on policies."
pantanal["Politics"]["Influenced By"] = ["Many factors."]
pantanal["Politics"]["Influences"] = [
"Wetlands (Pantanal) - Government Policies"
]
pantanal["Politics"]["Logic Description"] = "Politics influence policy decisions."
pantanal["Politics"]["Impact Function"] = "impact_politics_pantanal"

pantanal["Energy Demand"]["Metric"] = "Demand for Hydropower."
pantanal["Energy Demand"]["Data Sources"] = [
"Energy reports."
]
pantanal["Energy Demand"]["Impact on Area"] = "Pressure for Dam Development"
pantanal["Energy Demand"]["Impact on Biodiversity"] = "Altered Hydrology."
pantanal["Energy Demand"]["Influenced By"] = [
"Economic Growth"
]
pantanal["Energy Demand"]["Influences"] = [
"Wetlands (Pantanal) - Upstream Dam Construction"
]
pantanal["Energy Demand"]["Logic Description"] = "Demand of energy (Hydropower in particular)"
pantanal["Energy Demand"]["Impact Function"] = "impact_energy_demand_pantanal"

# --- Wetlands (Sundarbans) ---
sundarbans = all_stressors_data["Sundarbans Wetlands"]

sundarbans["Sea Level Rise"]["Metric"] = "Relative sea level rise (mm/year); rate of land subsidence (mm/year)."
sundarbans["Sea Level Rise"]["Data Sources"] = [
"Tide gauge records (Bangladesh and India).",
"Satellite altimetry.",
"Research studies on subsidence.",
"IPCC reports."
]
sundarbans["Sea Level Rise"]["Impact on Area"] = "Major loss of land area due to inundation. The Sundarbans is extremely vulnerable to sea level rise.; Increased salinity intrusion into freshwater areas.;Coastal Erosion"
sundarbans["Sea Level Rise"]["Impact on Biodiversity"] = "Loss of mangrove habitat (mangroves are the defining feature of the Sundarbans).; Impacts on the Bengal tiger population (loss of habitat, increased human-wildlife conflict).; Impacts on other wildlife (e.g., deer, crocodiles, birds, fish).; Changes in species distributions."
sundarbans["Sea Level Rise"]["Influenced By"] = [
"Wetlands (Sundarbans) - Climate Change",
"Local Land Subsidence" #Not Defined - need template
]
sundarbans["Sea Level Rise"]["Influences"] = [
"Wetlands (Sundarbans) - Salinity Intrusion",
"Wetlands (Sundarbans) - Habitat Availability",
"Wetlands (Sundarbans) - Coastal Erosion"
]
sundarbans["Sea Level Rise"]["Logic Description"] = "The Sundarbans, a low-lying delta region, is one of the most vulnerable places on Earth to sea level rise. Inundation and increased salinity are major threats to the mangrove ecosystem and its biodiversity."
sundarbans["Sea Level Rise"]["Impact Function"] = "impact_sea_level_rise_sundarbans"

sundarbans["Salinity Intrusion"]["Metric"] = "Salinity levels in water and soil (parts per thousand - ppt)."
sundarbans["Salinity Intrusion"]["Data Sources"] = [
"Water quality monitoring data (Bangladesh and India).",
"Research studies."
]
sundarbans["Salinity Intrusion"]["Impact on Area"] = "Changes in the distribution of different mangrove species (some are more salt-tolerant than others)."
sundarbans["Salinity Intrusion"]["Impact on Biodiversity"] = "Impacts on freshwater-dependent species.; Changes in plant communities.; Impacts on fisheries."
sundarbans["Salinity Intrusion"]["Influenced By"] = [
"Wetlands (Sundarbans) - Sea Level Rise",
"Wetlands (Sundarbans) - Reduced Freshwater Flow"
]
sundarbans["Salinity Intrusion"]["Influences"] = [
"Wetlands (Sundarbans) - Water Quality",
"Wetlands (Sundarbans) - Habitat Availability",
"Wetlands (Sundarbans) - Freshwater Availability"
]
sundarbans["Salinity Intrusion"]["Logic Description"] = "Sea level rise and reduced freshwater flow from rivers lead to increased salinity intrusion, impacting both the mangrove ecosystem and human populations who depend on freshwater resources."
sundarbans["Salinity Intrusion"]["Impact Function"] = "impact_salinity_intrusion_sundarbans"

sundarbans["Climate Change"]["Metric"] = "Temperature increase; changes in precipitation; cyclone frequency/intensity."
sundarbans["Climate Change"]["Data Sources"] = [
"Climate models.",
"Historical weather records."
]
sundarbans["Climate Change"]["Impact on Area"] = "Indirect (sea level rise, cyclones, altered rainfall).."
sundarbans["Climate Change"]["Impact on Biodiversity"] = "Increased stress, species shifts."
sundarbans["Climate Change"]["Influenced By"] = [
"Global Greenhouse Gas Emissions"
]
sundarbans["Climate Change"]["Influences"] = [
"Wetlands (Sundarbans) - Sea Level Rise",
"Wetlands (Sundarbans) - Cyclone Frequency and Intensity",
"Wetlands (Sundarbans) - Reduced Freshwater Flow"
]
sundarbans["Climate Change"]["Logic Description"] = "Climate change drives sea level rise, more intense cyclones, and altered rainfall patterns, all major threats to the Sundarbans."
sundarbans["Climate Change"]["Impact Function"] = "impact_climate_change_sundarbans"

sundarbans["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., heavy metals, oil, plastics) in water, sediment, and biota."
sundarbans["Pollution"]["Data Sources"] = [
"Water quality monitoring data.",
"Research studies."
]
sundarbans["Pollution"]["Impact on Area"] = "Degradation of water quality."
sundarbans["Pollution"]["Impact on Biodiversity"] = "Toxic effects on wildlife.; Impacts on fisheries.; Impacts on human health."
sundarbans["Pollution"]["Influenced By"] = [
"Industrial Discharge (from India and Bangladesh)",
"Shipping Activities (oil spills and discharge)",
"Agricultural Runoff",
"Untreated Sewage"
]
sundarbans["Pollution"]["Influences"] = [
"Wetlands (Sundarbans) - Water Quality",
"Wetlands (Sundarbans) - Wildlife Health"
]
sundarbans["Pollution"]["Logic Description"] = "Pollution from industrial discharge, shipping, agriculture, and sewage degrades water quality, harming wildlife and impacting human health."
sundarbans["Pollution"]["Impact Function"] = "impact_pollution_sundarbans"

sundarbans["Overexploitation of Resources"]["Metric"] = "Fish catches; timber harvesting rates; honey collection rates."
sundarbans["Overexploitation of Resources"]["Data Sources"] = [
"Fisheries data.",
"Forestry data.",
"Research studies."
]
sundarbans["Overexploitation of Resources"]["Impact on Area"] = "Depletion of natural resources."
sundarbans["Overexploitation of Resources"]["Impact on Biodiversity"] = "Decline in fish populations.; Loss of mangrove trees (due to illegal logging).; Impacts on wildlife that depend on those resources."
sundarbans["Overexploitation of Resources"]["Influenced By"] = [
"Population Growth",
"Poverty",
"Lack of Alternative Livelihoods"
]
sundarbans["Overexploitation of Resources"]["Influences"] = [
"Resource Availability"
]
sundarbans["Overexploitation of Resources"]["Logic Description"] = "Unsustainable harvesting of fish, timber, and other resources depletes stocks and impacts the ecosystem."
sundarbans["Overexploitation of Resources"]["Impact Function"] = "impact_overexploitation_resources_sundarbans"

sundarbans["Cyclone Frequency and Intensity"]["Metric"] = "Number of cyclones making landfall; wind speeds; storm surge height."
sundarbans["Cyclone Frequency and Intensity"]["Data Sources"] = [
"Meteorological data (India and Bangladesh).",
"Historical records."
]
sundarbans["Cyclone Frequency and Intensity"]["Impact on Area"] = "Coastal erosion.; Flooding.; Damage to infrastructure.; Salinization."
sundarbans["Cyclone Frequency and Intensity"]["Impact on Biodiversity"] = "Damage to mangrove forests.; Wildlife mortality.; Habitat loss."
sundarbans["Cyclone Frequency and Intensity"]["Influenced By"] = [
"Wetlands (Sundarbans) - Climate Change"
]
sundarbans["Cyclone Frequency and Intensity"]["Influences"] = [
"Wetlands (Sundarbans) - Coastal Erosion"
]
sundarbans["Cyclone Frequency and Intensity"]["Logic Description"] = "The Sundarbans is highly vulnerable to cyclones, and climate change may increase their frequency and intensity.  Cyclones cause widespread damage to infrastructure, ecosystems, and human communities."
sundarbans["Cyclone Frequency and Intensity"]["Impact Function"] = "impact_cyclone_frequency_intensity_sundarbans"

sundarbans["Reduced Freshwater Flow"]["Metric"] = "Water flow rates in the rivers that feed the Sundarbans (e.g., the Ganges)."
sundarbans["Reduced Freshwater Flow"]["Data Sources"] = ["Hydrological data (India and Bangladesh)."]
sundarbans["Reduced Freshwater Flow"]["Impact on Area"] = "Increased salinity intrusion; reduced sediment deposition (which helps maintain the delta)."
sundarbans["Reduced Freshwater Flow"]["Impact on Biodiversity"] = "Impacts on freshwater-dependent species; changes in plant communities."
sundarbans["Reduced Freshwater Flow"]["Influenced By"] = [
"Upstream water diversions and dams.",
"Wetlands (Sundarbans) - Climate Change"
]
sundarbans["Reduced Freshwater Flow"]["Influences"] = [
"Wetlands (Sundarbans) - Salinity Intrusion",
"Wetlands (Sundarbans) - Sedimentation"
]
sundarbans["Reduced Freshwater Flow"]["Logic Description"] = "Reduced freshwater flow, due to upstream water diversions and climate change, exacerbates salinity problems and affects sediment deposition in the Sundarbans."
sundarbans["Reduced Freshwater Flow"]["Impact Function"] = "impact_reduced_freshwater_flow_sundarbans"

# --- Deserts (Arabian) ---
arabian_desert = all_stressors_data["Arabian Deserts"]

arabian_desert["Overgrazing"]["Metric"] = "Livestock density (animals/km²); vegetation cover and composition; soil erosion."
arabian_desert["Overgrazing"]["Data Sources"] = [
"Agricultural statistics (from Arabian Peninsula countries).",
"Remote sensing data (vegetation indices).",
"Research studies."
]
arabian_desert["Overgrazing"]["Impact on Area"] = "Degradation of vegetation; soil erosion; reduced water infiltration."
arabian_desert["Overgrazing"]["Impact on Biodiversity"] = "Loss of palatable plant species.; Changes in plant community composition.; Impacts on desert wildlife (e.g., gazelles, oryx).; Increased competition for scarce resources."
arabian_desert["Overgrazing"]["Influenced By"] = [
"Livestock Management Practices",
"Population Growth (human and livestock)",
"Climate Variability (drought)",
"Lack of Land-Use Planning"
]
arabian_desert["Overgrazing"]["Influences"] = [
"Deserts (Arabian) - Desertification",
"Deserts (Arabian) - Soil Degradation",
"Deserts (Arabian) - Water Availability"
]
arabian_desert["Overgrazing"]["Logic Description"] = "Overgrazing by livestock (camels, sheep, goats) is a *major* stressor in the Arabian Desert, leading to vegetation degradation, soil erosion, and reduced biodiversity."
arabian_desert["Overgrazing"]["Impact Function"] = "impact_overgrazing_arabian_desert"

arabian_desert["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality); increased frequency and intensity of heatwaves and droughts."
arabian_desert["Climate Change"]["Data Sources"] = [
"Climate models.",
"Historical weather records.",
"Research publications."
]
arabian_desert["Climate Change"]["Impact on Area"] = "Increased temperatures, making the desert even hotter. Reduced and more erratic rainfall, exacerbating water scarcity. Increased frequency and severity of heat waves and droughts."
arabian_desert["Climate Change"]["Impact on Biodiversity"] = "Increased stress on desert plants and animals.; Shifts in species distributions.; Potential for local extinctions.; Impacts on water-dependent species."
arabian_desert["Climate Change"]["Influenced By"] = ["Global GHG"]
arabian_desert["Climate Change"]["Influences"] = [
"Deserts (Arabian) - Water Scarcity",
"Deserts (Arabian) - Desertification",
"Deserts (Arabian) - Heat Stress (on organisms)"
]
arabian_desert["Climate Change"]["Logic Description"] = "Climate change is exacerbating the already harsh conditions of the Arabian Desert, increasing temperatures, reducing rainfall, and leading to more frequent extreme weather events."
arabian_desert["Climate Change"]["Impact Function"] = "impact_climate_change_arabian_desert"

arabian_desert["Water Scarcity"]["Metric"] = "Groundwater levels; water extraction rates; water availability per capita."
arabian_desert["Water Scarcity"]["Data Sources"] = [
"Groundwater monitoring data.",
"Water resource assessments.",
"Government reports."
]
arabian_desert["Water Scarcity"]["Impact on Area"] = "Depletion of groundwater resources.; Reduced water availability for oases and other water-dependent ecosystems."
arabian_desert["Water Scarcity"]["Impact on Biodiversity"] = "Impacts on water-dependent species (plants, animals, and microorganisms).; Increased competition for water resources."
arabian_desert["Water Scarcity"]["Influenced By"] = [
"Deserts (Arabian) - Climate Change",
"Population Growth",
"Agricultural Water Use",
"Industrial Water Use",
"Urban Water Use"
]
arabian_desert["Water Scarcity"]["Influences"] = [
"Deserts (Arabian) - Desertification",
"Deserts (Arabian) - Human Well-being"
]
arabian_desert["Water Scarcity"]["Logic Description"] = "Water scarcity is a *critical* issue in the Arabian Desert.  Groundwater is the primary source of water, and it is being depleted at an unsustainable rate due to increasing demand from population growth, agriculture, and industry."
arabian_desert["Water Scarcity"]["Impact Function"] = "impact_water_scarcity_arabian_desert"

arabian_desert["Desertification"]["Metric"] = "Expansion of desert-like conditions; loss of vegetation cover; soil degradation; increased dust storms."
arabian_desert["Desertification"]["Data Sources"] = [
"Remote sensing data (vegetation indices, land cover change).",
"Soil surveys.",
"Research studies."
]
arabian_desert["Desertification"]["Impact on Area"] = "Loss of productive land.; Increased dust storms, impacting air quality and human health."
arabian_desert["Desertification"]["Impact on Biodiversity"] = "Loss of habitat for desert plants and animals.; Changes in species composition."
arabian_desert["Desertification"]["Influenced By"] = [
"Deserts (Arabian) - Overgrazing",
"Deserts (Arabian) - Climate Change",
"Deserts (Arabian) - Water Scarcity",
"Deserts (Arabian) - Deforestation (limited, but can occur in some areas)",
"Deserts (Arabian) - Unsustainable Land Management Practices"
]
arabian_desert["Desertification"]["Influences"] = [
"Deserts (Arabian) - Soil Degradation",
"Deserts (Arabian) - Air Quality (dust storms)"
]
arabian_desert["Desertification"]["Logic Description"] = "Desertification is the process by which fertile land turns into desert.  In the Arabian Desert, this is primarily driven by overgrazing, climate change, and unsustainable land management practices."
arabian_desert["Desertification"]["Impact Function"] = "impact_desertification_arabian_desert"

arabian_desert["Urbanization"]["Metric"] = "Urban area expansion; population growth in cities; infrastructure development."
arabian_desert["Urbanization"]["Data Sources"] = [
"Urban planning data.",
"Census data.",
"Remote sensing data."
]
arabian_desert["Urbanization"]["Impact on Area"] = "Loss of desert habitat; fragmentation of habitat."
arabian_desert["Urbanization"]["Impact on Biodiversity"] = "Habitat loss and fragmentation.; Increased human-wildlife conflict.; Impacts on wildlife movement.; Increased disturbance."
arabian_desert["Urbanization"]["Influenced By"] = [
"Population Growth",
"Economic Development"
]
arabian_desert["Urbanization"]["Influences"] = [
"Deserts (Arabian) - Habitat Loss",
"Deserts (Arabian) - Water Demand",
"Deserts (Arabian) - Pollution"
]
arabian_desert["Urbanization"]["Logic Description"] = "Rapid urbanization in some parts of the Arabian Desert is leading to habitat loss, increased water demand, and pollution."
arabian_desert["Urbanization"]["Impact Function"] = "impact_urbanization_arabian_desert"

arabian_desert["Off-Road Vehicle Use"]["Metric"] = "Area affected by off-road vehicle tracks; frequency of off-road vehicle use."
arabian_desert["Off-Road Vehicle Use"]["Data Sources"] = [
"Remote sensing data.",
"Field surveys.",
"Reports from protected areas."
]
arabian_desert["Off-Road Vehicle Use"]["Impact on Area"] = "Soil compaction.; Damage to vegetation.; Disturbance to wildlife."
arabian_desert["Off-Road Vehicle Use"]["Impact on Biodiversity"] = "Disturbance to desert animals (e.g., reptiles, birds, mammals).; Damage to fragile desert vegetation (e.g., cryptobiotic soil crusts).; Increased soil erosion."
arabian_desert["Off-Road Vehicle Use"]["Influenced By"] = [
"Tourism",
"Recreational Activities",
"Lack of Regulation"
]
arabian_desert["Off-Road Vehicle Use"]["Influences"] = [
"Deserts (Arabian) - Soil Degradation",
"Deserts (Arabian) - Wildlife Disturbance"
]
arabian_desert["Off-Road Vehicle Use"]["Logic Description"] = "Unregulated off-road vehicle use can cause significant damage to fragile desert ecosystems, impacting soil, vegetation, and wildlife."
arabian_desert["Off-Road Vehicle Use"]["Impact Function"] = "impact_off_road_vehicle_use_arabian_desert"

arabian_desert["Oil and Gas Extraction"]["Metric"] = "Area affected by oil and gas infrastructure (wells, pipelines, roads); oil spills and leaks."
arabian_desert["Oil and Gas Extraction"]["Data Sources"] = [
"Industry data.",
"Government reports.",
"Remote sensing data."
]
arabian_desert["Oil and Gas Extraction"]["Impact on Area"] = "Habitat loss and fragmentation.; Pollution from spills and leaks.; Noise pollution."
arabian_desert["Oil and Gas Extraction"]["Impact on Biodiversity"] = "Habitat loss and fragmentation.; Toxic effects of oil spills on wildlife.; Disturbance to wildlife from noise and human activity."
arabian_desert["Oil and Gas Extraction"]["Influenced By"] = [
"Global Energy Demand",
"Economic Factors",
"Geopolitical Factors"
]
arabian_desert["Oil and Gas Extraction"]["Influences"] = [
"Deserts (Arabian) - Habitat Fragmentation",
"Deserts (Arabian) - Pollution",
"Deserts (Arabian) - Water Contamination (potential)"
]
arabian_desert["Oil and Gas Extraction"]["Logic Description"] = "The Arabian Desert is a major oil and gas producing region. Extraction activities can lead to habitat loss, pollution, and disturbance to wildlife."
arabian_desert["Oil and Gas Extraction"]["Impact Function"] = "impact_oil_and_gas_extraction_arabian_desert"

# --- Deserts (Atacama) ---
atacama_desert = all_stressors_data["Atacama Deserts"]

atacama_desert["Mining Activities"]["Metric"] = "Area affected by mining operations (hectares); water consumption by mining (cubic meters/year); concentrations of pollutants (e.g., heavy metals) in water and soil."
atacama_desert["Mining Activities"]["Data Sources"] = [
"Chilean government data (e.g., Ministry of Mining, COCHILCO - Chilean Copper Commission).",
"Mining company reports.",
"Research studies.",
"Remote sensing data."
]
atacama_desert["Mining Activities"]["Impact on Area"] = "Extensive habitat loss and alteration. The Atacama is a major mining region (copper, lithium, nitrates).; Water extraction, leading to depletion of scarce water resources.; Pollution from tailings and waste disposal.; Dust generation."
atacama_desert["Mining Activities"]["Impact on Biodiversity"] = "Impacts on unique desert flora and fauna adapted to extreme aridity.; Impacts on microbial communities in soils and salt flats.; Water contamination affecting wildlife.; Habitat loss."
atacama_desert["Mining Activities"]["Influenced By"] = [
"Global Demand for Minerals (copper, lithium, etc.)",
"Economic Factors",
"Government Policies (Chile)"
]
atacama_desert["Mining Activities"]["Influences"] = [
"Deserts (Atacama) - Water Scarcity",
"Deserts (Atacama) - Pollution",
"Deserts (Atacama) - Habitat Loss"
]
atacama_desert["Mining Activities"]["Logic Description"] = "Mining is the *dominant* economic activity in the Atacama Desert, and it has significant environmental impacts, particularly on water resources, habitat, and pollution levels."
atacama_desert["Mining Activities"]["Impact Function"] = "impact_mining_activities_atacama_desert"

atacama_desert["Water Scarcity"]["Metric"] = "Groundwater levels; water extraction rates; water availability for different users (mining, agriculture, human consumption)."
atacama_desert["Water Scarcity"]["Data Sources"] = [
"Chilean government data (DGA - Dirección General de Aguas).",
"Research studies."
]
atacama_desert["Water Scarcity"]["Impact on Area"] = "Depletion of groundwater aquifers.; Reduced water availability for oases and other fragile ecosystems.; Conflicts over water resources."
atacama_desert["Water Scarcity"]["Impact on Biodiversity"] = "Impacts on water-dependent species (e.g., flamingos in salt flats, vegetation in oases).; Increased stress on desert ecosystems."
atacama_desert["Water Scarcity"]["Influenced By"] = [
"Deserts (Atacama) - Mining Activities",
"Deserts (Atacama) - Climate Change",
"Agricultural Water Use (limited, but present in some areas)",
"Population Growth (in some areas)"
]
atacama_desert["Water Scarcity"]["Influences"] = [
"Deserts (Atacama) - Habitat Availability",
"Deserts (Atacama) - Ecosystem Functioning"
]
atacama_desert["Water Scarcity"]["Logic Description"] = "Water scarcity is *extremely* severe in the Atacama Desert, one of the driest places on Earth.  Competition for water resources between mining, agriculture, and ecosystems is a major issue."
atacama_desert["Water Scarcity"]["Impact Function"] = "impact_water_scarcity_atacama_desert"

atacama_desert["Climate Change"]["Metric"] = "Temperature increase; changes in precipitation (even small changes are significant in this hyperarid environment); glacier retreat in the Andes (which affects water supply to some areas)."
atacama_desert["Climate Change"]["Data Sources"] = [
"Climate models.",
"Historical weather records."
]
atacama_desert["Climate Change"]["Impact on Area"] = "Increased temperatures. Changes in precipitation. Glacier retreat. All impacting water and already limited life"
atacama_desert["Climate Change"]["Impact on Biodiversity"] = "Increased stress, potential local extinctions, impacts to unique species"
atacama_desert["Climate Change"]["Influenced By"] = [
"Global GHG"
]
atacama_desert["Climate Change"]["Influences"] = [
"Deserts (Atacama) - Water Scarcity"
]
atacama_desert["Climate Change"]["Logic Description"] = "Climate change effects in an already extreme location."
atacama_desert["Climate Change"]["Impact Function"] = "impact_climate_change_atacama_desert"

atacama_desert["Tourism"]["Metric"] = "Number of tourists visiting the Atacama per year; development of tourism infrastructure (hotels, roads, etc.)."
atacama_desert["Tourism"]["Data Sources"] = [
"Chilean tourism statistics.",
"Local government data."
]
atacama_desert["Tourism"]["Impact on Area"] = "Localized impacts around tourist hotspots (e.g., San Pedro de Atacama).; Increased water demand.; Waste generation.; Disturbance to fragile landscapes."
atacama_desert["Tourism"]["Impact on Biodiversity"] = "Disturbance to wildlife (e.g., flamingos, vicuñas).; Potential for introduction of invasive species.; Impacts on fragile desert vegetation."
atacama_desert["Tourism"]["Influenced By"] = [
"Economic Factors",
"Accessibility",
"Marketing and Promotion"
]
atacama_desert["Tourism"]["Influences"] = [
"Deserts (Atacama) - Water Demand",
"Deserts (Atacama) - Waste Generation",
"Deserts (Atacama) - Wildlife Disturbance"
]
atacama_desert["Tourism"]["Logic Description"] = "Tourism is a growing industry in the Atacama, bringing economic benefits but also putting pressure on fragile ecosystems and resources."
atacama_desert["Tourism"]["Impact Function"] = "impact_tourism_atacama_desert"

atacama_desert["Light Pollution"]["Metric"] = "Sky brightness measurements; area affected by artificial light at night."
atacama_desert["Light Pollution"]["Data Sources"] = [
"Light pollution maps.",
"Research studies (astronomical observatories are *very* sensitive to light pollution)."
]
atacama_desert["Light Pollution"]["Impact on Area"] = "Degradation of the exceptionally dark night skies, impacting astronomical observations. The Atacama is a *world-renowned* site for astronomy."
atacama_desert["Light Pollution"]["Impact on Biodiversity"] = "Potential impacts on nocturnal animals (disruption of behavior, navigation, etc.).  This is less well-studied than astronomical impacts, but is a growing concern."
atacama_desert["Light Pollution"]["Influenced By"] = [
"Urbanization (in the Atacama and surrounding areas)",
"Mining Activities",
"Tourism Development"
]
atacama_desert["Light Pollution"]["Influences"] = [
"Astronomical Observations",
"Deserts (Atacama) - Nocturnal Wildlife"
]
atacama_desert["Light Pollution"]["Logic Description"] = "The Atacama Desert is famous for its clear, dark skies, making it ideal for astronomical observations.  Light pollution from growing cities, mining operations, and tourism is a threat to this valuable resource."
atacama_desert["Light Pollution"]["Impact Function"] = "impact_light_pollution_atacama_desert"

atacama_desert["Off-Road Vehicle Use"]["Metric"] = "Area of tracks; frequency of off-road."
atacama_desert["Off-Road Vehicle Use"]["Data Sources"] = [
"Remote sensing.",
"Field surveys."
]
atacama_desert["Off-Road Vehicle Use"]["Impact on Area"] = "Soil compaction.; Damage to vegetation and soil crusts.; Disturbance to wildlife."
atacama_desert["Off-Road Vehicle Use"]["Impact on Biodiversity"] = "Disturbance and habitat damage"
atacama_desert["Off-Road Vehicle Use"]["Influenced By"] = [
"Tourism",
"Mining exploration",
"Recreational activities."
]
atacama_desert["Off-Road Vehicle Use"]["Influences"] = [
"Deserts (Atacama) - Soil Degradation"
]
atacama_desert["Off-Road Vehicle Use"]["Logic Description"] = "Off-road vehicle use impacts sensitive landscapes"
atacama_desert["Off-Road Vehicle Use"]["Impact Function"] = "impact_off_road_vehicle_use_atacama_desert"

# --- Deserts (Australian) ---
australian_deserts = all_stressors_data["Australian Deserts"]

australian_deserts["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality); increased frequency and severity of drought and heatwaves."
australian_deserts["Climate Change"]["Data Sources"] = [
"Climate models (global and regional).",
"Historical weather records (Bureau of Meteorology).",
"Research publications."
]
australian_deserts["Climate Change"]["Impact on Area"] = "Increased aridity; potential for expansion of desert areas; changes in vegetation distribution."
australian_deserts["Climate Change"]["Impact on Biodiversity"] = "Increased stress on desert-adapted species, potentially exceeding their tolerance limits.; Shifts in species distributions.; Impacts on water sources, affecting wildlife."
australian_deserts["Climate Change"]["Influenced By"] = ["Global GHG"]
australian_deserts["Climate Change"]["Influences"] = [
"Deserts (Australian) - Water Availability",
"Deserts (Australian) - Fire Regimes",
"Deserts (Australian) - Desertification"
]
australian_deserts["Climate Change"]["Logic Description"] = "Australian deserts, already hot and dry, are highly vulnerable to climate change. Increased temperatures, changes in rainfall, and more frequent heatwaves and droughts will stress ecosystems."
australian_deserts["Climate Change"]["Impact Function"] = "impact_climate_change_australian_deserts"

australian_deserts["Overgrazing"]["Metric"] = "Livestock density (sheep, cattle); density of feral herbivores (e.g., rabbits, goats, camels); vegetation cover and composition; soil erosion."
australian_deserts["Overgrazing"]["Data Sources"] = [
"Agricultural statistics.",
"Rangeland monitoring data.",
"Research publications."
]
australian_deserts["Overgrazing"]["Impact on Area"] = "Degradation of vegetation; soil erosion; reduced water infiltration; changes in plant community composition."
australian_deserts["Overgrazing"]["Impact on Biodiversity"] = "Loss of palatable plant species.; Spread of unpalatable or invasive species.; Soil compaction, impacting soil organisms.; Competition between livestock, feral herbivores, and native herbivores."
australian_deserts["Overgrazing"]["Influenced By"] = [
"Livestock Management Practices",
"Feral Animal Populations",
"Land Tenure and Access Rights"
]
australian_deserts["Overgrazing"]["Influences"] = [
"Deserts (Australian) - Soil Degradation",
"Deserts (Australian) - Desertification",
"Deserts (Australian) - Invasive Species"
]
australian_deserts["Overgrazing"]["Logic Description"] = "Overgrazing by livestock and feral herbivores (rabbits, goats, camels) is a *widespread* and significant problem in Australian deserts, leading to vegetation degradation, soil erosion, and biodiversity loss."
australian_deserts["Overgrazing"]["Impact Function"] = "impact_overgrazing_australian_deserts"

australian_deserts["Invasive Species"]["Metric"] = "Abundance and distribution of key invasive species (e.g., buffel grass, *Opuntia* spp. (prickly pear), rabbits, cats, foxes, camels)."
australian_deserts["Invasive Species"]["Data Sources"] = [
"Government reports and databases (e.g., from the Department of Agriculture, Water and the Environment).",
"Research publications.",
"Field surveys."
]
australian_deserts["Invasive Species"]["Impact on Area"] = "Changes in vegetation composition and structure; altered fire regimes; competition with native species."
australian_deserts["Invasive Species"]["Impact on Biodiversity"] = "Competition with native plants (e.g., buffel grass outcompetes native grasses).; Predation on native animals (cats and foxes).; Altered fire regimes (buffel grass increases fire intensity).; Impacts on soil properties."
australian_deserts["Invasive Species"]["Influenced By"] = [
"Historical Introductions",
"Disturbance (e.g., overgrazing, fire)",
"Deserts (Australian) - Climate Change (may favor some invasives)"
]
australian_deserts["Invasive Species"]["Influences"] = [
"Deserts (Australian) - Fire Regimes",
"Deserts (Australian) - Native Species Populations"
]
australian_deserts["Invasive Species"]["Logic Description"] = "Invasive species, both plants (e.g., buffel grass) and animals (e.g., rabbits, cats, foxes, camels), are a *major* threat to Australian desert ecosystems, outcompeting native species, altering fire regimes, and causing significant ecological damage."
australian_deserts["Invasive Species"]["Impact Function"] = "impact_invasive_species_australian_deserts"

australian_deserts["Feral Animals"]["Metric"] = "Population densities of feral animals (e.g., camels, rabbits, cats, foxes, goats, horses)."
australian_deserts["Feral Animals"]["Data Sources"] = [
"Government reports and control programs.",
"Research publications.",
"Aerial surveys."
]
australian_deserts["Feral Animals"]["Impact on Area"] = "Overgrazing; predation; habitat destruction."
australian_deserts["Feral Animals"]["Impact on Biodiversity"] = "Decline of native plant species due to overgrazing.; Predation on native animals.; Competition with native herbivores.; Spread of diseases."
australian_deserts["Feral Animals"]["Influenced By"] = [
"Historical Introductions",
"Lack of Natural Predators (for some species)",
"Availability of Water Sources"
]
australian_deserts["Feral Animals"]["Influences"] = [
"Deserts (Australian) - Overgrazing",
"Deserts (Australian) - Native Species Populations"
]
australian_deserts["Feral Animals"]["Logic Description"] = "Feral animals, such as camels, rabbits, cats, foxes, and goats, have a devastating impact on Australian desert ecosystems through overgrazing, predation, and habitat destruction."
australian_deserts["Feral Animals"]["Impact Function"] = "impact_feral_animals_australian_deserts"

australian_deserts["Fire Regimes"]["Metric"] = "Fire frequency (return interval); fire intensity; area burned; seasonality of fires."
australian_deserts["Fire Regimes"]["Data Sources"] = [
"Remote sensing data (fire scars).",
"Government agency reports (fire management agencies).",
"Research publications."
]
australian_deserts["Fire Regimes"]["Impact on Area"] = "Changes in vegetation structure and composition. Some areas are adapted to fire, while others are highly sensitive."
australian_deserts["Fire Regimes"]["Impact on Biodiversity"] = "Changes in species composition. Increased fire frequency and intensity, often linked to invasive grasses, can be detrimental to fire-sensitive species. Altered habitat structure."
australian_deserts["Fire Regimes"]["Influenced By"] = [
"Deserts (Australian) - Climate Change",
"Deserts (Australian) - Invasive Species (e.g., buffel grass)",
"Land Management Practices",
"Human Ignitions"
]
australian_deserts["Fire Regimes"]["Influences"] = [
"Deserts (Australian) - Vegetation Structure"
]
australian_deserts["Fire Regimes"]["Logic Description"] = "Changes in fire regimes, often linked to invasive grasses and climate change, can have significant impacts on Australian desert ecosystems. Some areas are experiencing more frequent and intense fires, while others may have altered fire seasonality."
australian_deserts["Fire Regimes"]["Impact Function"] = "impact_fire_regimes_australian_deserts"

australian_deserts["Mining"]["Metric"] = "Area affected by mining operations (ha); water use by mining; pollution levels (e.g., heavy metals)."
australian_deserts["Mining"]["Data Sources"] = [
"Mining company reports.",
"Government data (mining leases, environmental approvals).",
"Research publications."
]
australian_deserts["Mining"]["Impact on Area"] = "Habitat destruction; water extraction; pollution (e.g., dust, heavy metals)."
australian_deserts["Mining"]["Impact on Biodiversity"] = "Loss of habitat; impacts on water resources; toxic effects of pollutants."
australian_deserts["Mining"]["Influenced By"] = [
"Global Demand for Minerals",
"Economic Factors",
"Government Policies"
]
australian_deserts["Mining"]["Influences"] = [
"Deserts (Australian) - Water Resources",
"Deserts (Australian) - Pollution",
"Deserts (Australian) - Habitat Loss"
]
australian_deserts["Mining"]["Logic Description"] = "Mining activities can have significant impacts on desert ecosystems, particularly through habitat destruction, water extraction, and pollution."
australian_deserts["Mining"]["Impact Function"] = "impact_mining_australian_deserts"

australian_deserts["Tourism"]["Metric"] = "Number of tourists visiting desert areas; development of tourism infrastructure."
australian_deserts["Tourism"]["Data Sources"] = [
"Tourism statistics.",
"Reports from national parks and protected areas."
]
australian_deserts["Tourism"]["Impact on Area"] = "Localized impacts around tourist sites; potential for increased pressure on water resources."
australian_deserts["Tourism"]["Impact on Biodiversity"] = "Disturbance to wildlife; damage to fragile vegetation; introduction of invasive species."
australian_deserts["Tourism"]["Influenced By"] = [
"Accessibility",
"Marketing and Promotion"
]
australian_deserts["Tourism"]["Influences"] = [
"Deserts (Australian) - Wildlife Disturbance"
]
australian_deserts["Tourism"]["Logic Description"] = "Tourism, while economically beneficial, can put pressure on fragile desert ecosystems if not managed sustainably."
australian_deserts["Tourism"]["Impact Function"] = "impact_tourism_australian_deserts"

australian_deserts["Water Extraction"]["Metric"] = "Volume of groundwater extracted (ML/year); changes in groundwater levels."
australian_deserts["Water Extraction"]["Data Sources"] = [
"Government water resource data.",
"Research publications."
]
australian_deserts["Water Extraction"]["Impact on Area"] = "Depletion of groundwater resources; impacts on water-dependent ecosystems (e.g., springs, soaks)."
australian_deserts["Water Extraction"]["Impact on Biodiversity"] = "Loss of water sources for wildlife; impacts on vegetation."
australian_deserts["Water Extraction"]["Influenced By"] = [
"Agricultural Water Use",
"Mining Water Use",
"Human Consumption"
]
australian_deserts["Water Extraction"]["Influences"] = [
"Deserts (Australian) - Water Availability"
]
australian_deserts["Water Extraction"]["Logic Description"] = "Groundwater extraction for agriculture, mining, and human consumption can deplete water resources and impact desert ecosystems."
australian_deserts["Water Extraction"]["Impact Function"] = "impact_water_extraction_australian_deserts"

# --- Deserts (Chihuahuan) ---
chihuahuan_desert = all_stressors_data["Chihuahuan Deserts"]

chihuahuan_desert["Overgrazing"]["Metric"] = "Livestock density; vegetation cover and composition; soil erosion indicators."
chihuahuan_desert["Overgrazing"]["Data Sources"] = [
"Agricultural statistics (US and Mexico).",
"Rangeland assessments.",
"Research publications."
]
chihuahuan_desert["Overgrazing"]["Impact on Area"] = "Vegetation degradation; soil erosion; reduced water infiltration."
chihuahuan_desert["Overgrazing"]["Impact on Biodiversity"] = "Loss of palatable plant species; shift towards less palatable shrubs; impacts on desert wildlife."
chihuahuan_desert["Overgrazing"]["Influenced By"] = [
"Livestock Management Practices",
"Land Tenure and Access Rights",
"Economic Factors"
]
chihuahuan_desert["Overgrazing"]["Influences"] = [
"Deserts (Chihuahuan) - Desertification",
"Deserts (Chihuahuan) - Shrub Encroachment"
]
chihuahuan_desert["Overgrazing"]["Logic Description"] = "Overgrazing by livestock is a significant problem in the Chihuahuan Desert, leading to vegetation degradation and soil erosion. This can also exacerbate shrub encroachment."
chihuahuan_desert["Overgrazing"]["Impact Function"] = "impact_overgrazing_chihuahuan_desert"

chihuahuan_desert["Climate Change"]["Metric"] = "Temperature increase; changes in precipitation; drought frequency and intensity."
chihuahuan_desert["Climate Change"]["Data Sources"] = [
"Climate models.",
"Historical weather records.",
"Research publications."
]
chihuahuan_desert["Climate Change"]["Impact on Area"] = "Increased temperatures, potential for decreased precipitation; increased aridity."
chihuahuan_desert["Climate Change"]["Impact on Biodiversity"] = "Increased water stress on plants and animals.; Shifts in species distributions.; Potential for local extinctions."
chihuahuan_desert["Climate Change"]["Influenced By"] = ["Global GHG"]
chihuahuan_desert["Climate Change"]["Influences"] = [
"Deserts (Chihuahuan) - Water Scarcity"
]
chihuahuan_desert["Climate Change"]["Logic Description"] = "Climate change is exacerbating arid conditions, making the Chihuahuan Desert even hotter and drier."
chihuahuan_desert["Climate Change"]["Impact Function"] = "impact_climate_change_chihuahuan_desert"

chihuahuan_desert["Water Scarcity"]["Metric"] = "Groundwater levels; surface water availability; water extraction rates."
chihuahuan_desert["Water Scarcity"]["Data Sources"] = [
"Water resource assessments (US and Mexico).",
"Groundwater monitoring data.",
"Research publications."
]
chihuahuan_desert["Water Scarcity"]["Impact on Area"] = "Depletion of water resources.; Reduced water availability for ecosystems and human use."
chihuahuan_desert["Water Scarcity"]["Impact on Biodiversity"] = "Impacts on water-dependent species.; Increased competition for water."
chihuahuan_desert["Water Scarcity"]["Influenced By"] = [
"Deserts (Chihuahuan) - Climate Change",
"Agricultural Water Use",
"Urban Water Demand",
"Population Growth"
]
chihuahuan_desert["Water Scarcity"]["Influences"] = [
"Deserts (Chihuahuan) - Ecosystem Functioning"
]
chihuahuan_desert["Water Scarcity"]["Logic Description"] = "Water scarcity is a major issue in the Chihuahuan Desert, driven by climate change, agriculture, and urban demand."
chihuahuan_desert["Water Scarcity"]["Impact Function"] = "impact_water_scarcity_chihuahuan_desert"

chihuahuan_desert["Shrub Encroachment"]["Metric"] = "Increase in the abundance and cover of woody shrubs (e.g., creosote bush, mesquite) at the expense of grasses."
chihuahuan_desert["Shrub Encroachment"]["Data Sources"] = [
"Remote sensing data (vegetation indices).",
"Long-term vegetation monitoring plots.",
"Research publications."
]
chihuahuan_desert["Shrub Encroachment"]["Impact on Area"] = "Shift from grasslands to shrublands.; Changes in soil properties.; Reduced forage availability for livestock."
chihuahuan_desert["Shrub Encroachment"]["Impact on Biodiversity"] = "Loss of grassland habitat.; Impacts on grassland-dependent species.; Altered fire regimes."
chihuahuan_desert["Shrub Encroachment"]["Influenced By"] = [
"Deserts (Chihuahuan) - Overgrazing",
"Deserts (Chihuahuan) - Fire Suppression",
"Deserts (Chihuahuan) - Climate Change (potentially)"
]
chihuahuan_desert["Shrub Encroachment"]["Influences"] = [
"Deserts (Chihuahuan) - Ecosystem Structure and Function"
]
chihuahuan_desert["Shrub Encroachment"]["Logic Description"] = "Shrub encroachment, the expansion of woody shrubs into grasslands, is a widespread phenomenon in the Chihuahuan Desert, driven by overgrazing, fire suppression, and potentially climate change."
chihuahuan_desert["Shrub Encroachment"]["Impact Function"] = "impact_shrub_encroachment_chihuahuan_desert"

chihuahuan_desert["Urbanization"]["Metric"] = "Urban area expansion; population growth in cities."
chihuahuan_desert["Urbanization"]["Data Sources"] = [
"Urban planning data.",
"Census data.",
"Remote sensing data."
]
chihuahuan_desert["Urbanization"]["Impact on Area"] = "Habitat loss and fragmentation."
chihuahuan_desert["Urbanization"]["Impact on Biodiversity"] = "Loss of habitat; increased human-wildlife conflict; disturbance to wildlife."
chihuahuan_desert["Urbanization"]["Influenced By"] = [
"Population Growth",
"Economic Development"
]
chihuahuan_desert["Urbanization"]["Influences"] = [
"Deserts (Chihuahuan) - Habitat Loss",
"Deserts (Chihuahuan) - Water Demand"
]
chihuahuan_desert["Urbanization"]["Logic Description"] = "Urban expansion in and around the Chihuahuan Desert leads to habitat loss and increased demand for resources."
chihuahuan_desert["Urbanization"]["Impact Function"] = "impact_urbanization_chihuahuan_desert"

chihuahuan_desert["Mining"]["Metric"] = "Area affected by mining; water use; pollution."
chihuahuan_desert["Mining"]["Data Sources"] = [
"Mining company reports",
"Government data"
]
chihuahuan_desert["Mining"]["Impact on Area"] = "Habitat destruction; water extraction and pollution."
chihuahuan_desert["Mining"]["Impact on Biodiversity"] = "Habitat loss; toxic effects of pollutants."
chihuahuan_desert["Mining"]["Influenced By"] = [
"Global Demand for Minerals",
"Economic Factors"
]
chihuahuan_desert["Mining"]["Influences"] = [
"Deserts (Chihuahuan) - Water Resources",
"Deserts (Chihuahuan) - Pollution"
]
chihuahuan_desert["Mining"]["Logic Description"] = "Mining activities can have localized but significant impacts."
chihuahuan_desert["Mining"]["Impact Function"] = "impact_mining_chihuahuan_desert"

chihuahuan_desert["Agricultural Expansion"]["Metric"] = "Area converted to agriculture."
chihuahuan_desert["Agricultural Expansion"]["Data Sources"] = [
"Remote sensing.",
"Agricultural statistics."
]
chihuahuan_desert["Agricultural Expansion"]["Impact on Area"] = "Habitat loss; increased water demand."
chihuahuan_desert["Agricultural Expansion"]["Impact on Biodiversity"] = "Habitat loss; impacts from water use and pollution."
chihuahuan_desert["Agricultural Expansion"]["Influenced By"] = [
"Economic Factors",
"Population Growth"
]
chihuahuan_desert["Agricultural Expansion"]["Influences"] = [
"Deserts (Chihuahuan) - Water Resources",
"Deserts (Chihuahuan) - Land Use Change"
]
chihuahuan_desert["Agricultural Expansion"]["Logic Description"] = "Agricultural expansion puts pressure on desert ecosystems."
chihuahuan_desert["Agricultural Expansion"]["Impact Function"] = "impact_agricultural_expansion_chihuahuan_desert"

# --- Deserts (Gobi) ---
gobi_desert = all_stressors_data["Gobi Deserts"]

gobi_desert["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality); increased frequency and severity of drought; increased frequency of extreme heat events."
gobi_desert["Climate Change"]["Data Sources"] = [
"Climate models (global and regional).",
"Historical weather records (sparse in some areas).",
"Research publications."
]
gobi_desert["Climate Change"]["Impact on Area"] = "Increased aridity; potential for expansion of desert areas; increased frequency and intensity of dust storms."
gobi_desert["Climate Change"]["Impact on Biodiversity"] = "Increased stress on desert-adapted species; shifts in species distributions; potential for local extinctions; impacts on water sources."
gobi_desert["Climate Change"]["Influenced By"] = ["Global Greenhouse Gas Emissions"]
gobi_desert["Climate Change"]["Influences"] = [
"Deserts (Gobi) - Water Scarcity",
"Deserts (Gobi) - Desertification",
"Deserts (Gobi) - Dust Storms"
]
gobi_desert["Climate Change"]["Logic Description"] = "The Gobi Desert is highly vulnerable to climate change. Increased temperatures, changes in precipitation, and more frequent droughts will exacerbate existing pressures."
gobi_desert["Climate Change"]["Impact Function"] = "impact_climate_change_gobi_desert"

gobi_desert["Overgrazing"]["Metric"] = "Livestock density (animals/km²); vegetation cover and composition; soil erosion rates."
gobi_desert["Overgrazing"]["Data Sources"] = [
"Agricultural statistics (Mongolia and China).",
"Vegetation surveys.",
"Remote sensing data.",
"Research publications."
]
gobi_desert["Overgrazing"]["Impact on Area"] = "Degradation of vegetation; soil erosion; reduced water infiltration; desertification."
gobi_desert["Overgrazing"]["Impact on Biodiversity"] = "Loss of palatable plant species.; Changes in plant community composition.; Impacts on wildlife that depend on grasslands.; Soil compaction."
gobi_desert["Overgrazing"]["Influenced By"] = [
"Livestock Management Practices",
"Population Growth (of livestock and humans)",
"Economic Factors"
]
gobi_desert["Overgrazing"]["Influences"] = [
"Deserts (Gobi) - Desertification",
"Deserts (Gobi) - Soil Degradation"
]
gobi_desert["Overgrazing"]["Logic Description"] = "Overgrazing by livestock (sheep, goats, camels, cattle) is a *major* driver of land degradation and desertification in the Gobi Desert."
gobi_desert["Overgrazing"]["Impact Function"] = "impact_overgrazing_gobi_desert"

gobi_desert["Desertification"]["Metric"] = "Expansion of desert-like conditions; loss of vegetation cover; soil degradation; increased dust storm frequency."
gobi_desert["Desertification"]["Data Sources"] = [
"Remote sensing data (vegetation indices, land cover change).",
"Soil surveys.",
"Research studies.",
"Climate data."
]
gobi_desert["Desertification"]["Impact on Area"] = "Loss of productive land; reduced carrying capacity for livestock and wildlife."
gobi_desert["Desertification"]["Impact on Biodiversity"] = "Loss of habitat; changes in species composition; decline of native species."
gobi_desert["Desertification"]["Influenced By"] = [
"Deserts (Gobi) - Overgrazing",
"Deserts (Gobi) - Climate Change",
"Unsustainable Land Management Practices",
"Deforestation (in some areas)"
]
gobi_desert["Desertification"]["Influences"] = [
"Deserts (Gobi) - Dust Storms",
"Deserts (Gobi) - Soil Degradation",
"Deserts (Gobi) - Water Scarcity"
]
gobi_desert["Desertification"]["Logic Description"] = "Desertification, the process by which fertile land becomes desert, is a serious threat in the Gobi, driven by a combination of overgrazing, climate change, and unsustainable land management."
gobi_desert["Desertification"]["Impact Function"] = "impact_desertification_gobi_desert"

gobi_desert["Mining"]["Metric"] = "Area affected by mining operations (ha); water use by mining; pollution levels (e.g., heavy metals, dust)."
gobi_desert["Mining"]["Data Sources"] = [
"Government mining records (Mongolia and China).",
"Environmental Impact Assessments (EIAs).",
"Research publications.",
"Remote Sensing"
]
gobi_desert["Mining"]["Impact on Area"] = "Habitat destruction; water extraction and pollution; air pollution (dust)."
gobi_desert["Mining"]["Impact on Biodiversity"] = "Loss of habitat; toxic effects of pollutants on wildlife; impacts on water resources."
gobi_desert["Mining"]["Influenced By"] = [
"Global Demand for Minerals (e.g., coal, copper, gold).",
"Government Policies",
"Economic Factors"
]
gobi_desert["Mining"]["Influences"] = [
"Deserts (Gobi) - Water Resources",
"Deserts (Gobi) - Pollution",
"Deserts (Gobi) - Habitat Loss"
]
gobi_desert["Mining"]["Logic Description"] = "Mining is a growing industry in the Gobi Desert, with significant potential impacts on fragile ecosystems and scarce water resources."
gobi_desert["Mining"]["Impact Function"] = "impact_mining_gobi_desert"

gobi_desert["Infrastructure Development"]["Metric"] = "Road density (km/km²); area affected by infrastructure projects (e.g., railways, pipelines)."
gobi_desert["Infrastructure Development"]["Data Sources"] = [
"Government infrastructure plans.",
"Remote sensing data.",
"Research publications."
]
gobi_desert["Infrastructure Development"]["Impact on Area"] = "Habitat fragmentation; direct habitat loss; increased access to remote areas."
gobi_desert["Infrastructure Development"]["Impact on Biodiversity"] = "Habitat fragmentation; disruption of wildlife movement; increased human disturbance; potential for increased poaching and illegal wildlife trade."
gobi_desert["Infrastructure Development"]["Influenced By"] = [
"Economic Development",
"Resource Extraction",
"Geopolitical Factors (e.g., Belt and Road Initiative)"
]
gobi_desert["Infrastructure Development"]["Influences"] = [
"Deserts (Gobi) - Habitat Fragmentation"
]
gobi_desert["Infrastructure Development"]["Logic Description"] = "Infrastructure development, particularly roads and railways, can fragment desert habitats and increase human access, leading to various negative impacts."
gobi_desert["Infrastructure Development"]["Impact Function"] = "impact_infrastructure_development_gobi_desert"

gobi_desert["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., heavy metals, dust) in air, water, and soil."
gobi_desert["Pollution"]["Data Sources"] = [
"Air and water quality monitoring data (limited availability).",
"Research studies."
]
gobi_desert["Pollution"]["Impact on Area"] = "Degradation of air, water, and soil quality."
gobi_desert["Pollution"]["Impact on Biodiversity"] = "Toxic effects on wildlife and plants; impacts on water resources."
gobi_desert["Pollution"]["Influenced By"] = [
"Deserts (Gobi) - Mining Activities",
"Industrial Activities",
"Deserts (Gobi) - Dust Storms (natural, but exacerbated by land degradation)",
"Long-Range Transport of Pollutants"
]
gobi_desert["Pollution"]["Influences"] = [
"Deserts (Gobi) - Air Quality",
"Deserts (Gobi) - Water Quality",
"Deserts (Gobi) - Wildlife Health"
]
gobi_desert["Pollution"]["Logic Description"] = "Pollution from mining, industry, and dust storms can impact air and water quality in the Gobi Desert."
gobi_desert["Pollution"]["Impact Function"] = "impact_pollution_gobi_desert"

# --- Deserts (Kalahari) ---
kalahari_desert = all_stressors_data["Kalahari Deserts"]


kalahari_desert["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality); increased frequency and severity of drought."
kalahari_desert["Climate Change"]["Data Sources"] = [
"Climate models (global and regional).",
"Historical weather records.",
"Research publications."
]
kalahari_desert["Climate Change"]["Impact on Area"] = "Increased aridity; potential for further desertification; changes in vegetation distribution."
kalahari_desert["Climate Change"]["Impact on Biodiversity"] = "Increased stress on desert-adapted species; shifts in species distributions; potential for local extinctions; impacts on water sources."
kalahari_desert["Climate Change"]["Influenced By"] = ["Global GHG"]
kalahari_desert["Climate Change"]["Influences"] = [
"Deserts (Kalahari) - Water Scarcity",
"Deserts (Kalahari) - Bush Encroachment (potentially)",
"Deserts (Kalahari) - Wildfires (potentially)"
]
kalahari_desert["Climate Change"]["Logic Description"] = "The Kalahari, while already a dry environment, is vulnerable to the impacts of climate change, including increased temperatures, altered rainfall patterns, and more frequent droughts."
kalahari_desert["Climate Change"]["Impact Function"] = "impact_climate_change_kalahari_desert"

kalahari_desert["Overgrazing"]["Metric"] = "Livestock density (animals/km²); vegetation cover and composition; soil erosion; bush encroachment rates."
kalahari_desert["Overgrazing"]["Data Sources"] = [
"Agricultural statistics (Botswana, Namibia, South Africa).",
"Vegetation surveys.",
"Remote sensing data.",
"Research publications."
]
kalahari_desert["Overgrazing"]["Impact on Area"] = "Degradation of grasslands and savannas; soil erosion; bush encroachment (increase in woody shrub density at the expense of grasses)."
kalahari_desert["Overgrazing"]["Impact on Biodiversity"] = "Loss of palatable plant species; changes in plant community composition; reduced habitat quality for native herbivores; soil compaction."
kalahari_desert["Overgrazing"]["Influenced By"] = [
"Livestock Management Practices",
"Land Tenure Systems",
"Population Growth (human and livestock)",
"Economic Factors"
]
kalahari_desert["Overgrazing"]["Influences"] = [
"Deserts (Kalahari) - Bush Encroachment",
"Deserts (Kalahari) - Soil Degradation",
"Deserts (Kalahari) - Desertification"
]
kalahari_desert["Overgrazing"]["Logic Description"] = "Overgrazing by livestock (cattle, goats) is a *major* problem in the Kalahari, contributing to land degradation, bush encroachment, and biodiversity loss."
kalahari_desert["Overgrazing"]["Impact Function"] = "impact_overgrazing_kalahari_desert"

kalahari_desert["Bush Encroachment"]["Metric"] = "Increase in the density and cover of woody shrubs (e.g., *Acacia* species, *Terminalia sericea*).",
kalahari_desert["Bush Encroachment"]["Data Sources"]=[
"Remote sensing data (vegetation indices, time series analysis).",
"Vegetation surveys.",
"Research publications."
]
kalahari_desert["Bush Encroachment"]["Impact on Area"] = "Shift from grassland/savanna ecosystems to shrub-dominated ecosystems; reduced grazing land."
kalahari_desert["Bush Encroachment"]["Impact on Biodiversity"] = "Loss of habitat for grazing animals (both livestock and wildlife). Changes in species composition; reduced grass cover."
kalahari_desert["Bush Encroachment"]["Influenced By"] = [
"Deserts (Kalahari) - Overgrazing",
"Fire Suppression",
"Deserts (Kalahari) - Climate Change (potentially)"
]
kalahari_desert["Bush Encroachment"]["Influences"] = [
"Deserts (Kalahari) - Habitat Loss",
"Deserts (Kalahari) - Grazing Capacity"
]
kalahari_desert["Bush Encroachment"]["Logic Description"] = "Bush encroachment, the increase in woody shrub density, is a significant form of land degradation in the Kalahari, often linked to overgrazing and altered fire regimes. It reduces the carrying capacity for grazing animals."
kalahari_desert["Bush Encroachment"]["Impact Function"] = "impact_bush_encroachment_kalahari_desert"

kalahari_desert["Water Extraction"]["Metric"] = "Volume of groundwater extracted (m³/year); changes in groundwater levels; number of boreholes."
kalahari_desert["Water Extraction"]["Data Sources"] = [
"Government water resource data (Botswana, Namibia, South Africa).",
"Research publications."
]
kalahari_desert["Water Extraction"]["Impact on Area"] = "Depletion of groundwater resources; potential impacts on water-dependent ecosystems (e.g., pans, dry riverbeds)."
kalahari_desert["Water Extraction"]["Impact on Biodiversity"] = "Impacts on wildlife and vegetation that depend on groundwater sources; increased competition for water."
kalahari_desert["Water Extraction"]["Influenced By"] = [
"Agricultural Water Use (irrigation, livestock watering)",
"Human Population Growth",
"Mining Activities",
"Climate Change (reduced recharge)"
]
kalahari_desert["Water Extraction"]["Influences"] = [
"Deserts (Kalahari) - Water Availability"
]
kalahari_desert["Water Extraction"]["Logic Description"] = "Groundwater extraction, primarily for livestock watering and human consumption, is a growing concern in the Kalahari, as it can deplete aquifers and impact water-dependent ecosystems."
kalahari_desert["Water Extraction"]["Impact Function"] = "impact_water_extraction_kalahari_desert"

kalahari_desert["Land-Use Change"]["Metric"] = "Area converted to other land uses (e.g., settlements, infrastructure, agriculture) (ha/year)."
kalahari_desert["Land-Use Change"]["Data Sources"] = [
"Remote sensing data",
"Land-use planning records.",
"Research publications"
]
kalahari_desert["Land-Use Change"]["Impact on Area"] = "Habitat loss and fragmentation."
kalahari_desert["Land-Use Change"]["Impact on Biodiversity"] = "Loss of habitat; disruption of wildlife movement; increased human-wildlife conflict."
kalahari_desert["Land-Use Change"]["Influenced By"] = [
"Population Growth",
"Economic Development",
"Government Policies"
]
kalahari_desert["Land-Use Change"]["Influences"] = [
"Deserts (Kalahari) - Habitat Fragmentation"
]
kalahari_desert["Land-Use Change"]["Logic Description"] = "Land-use change, although currently less extensive than in some other deserts, is a growing threat, particularly around settlements and areas with potential for agriculture."
kalahari_desert["Land-Use Change"]["Impact Function"] = "impact_land_use_change_kalahari_desert"

kalahari_desert["Tourism"]["Metric"] = "Number of tourists visiting protected areas; development of tourism infrastructure."
kalahari_desert["Tourism"]["Data Sources"] = [
"Tourism statistics (Botswana, Namibia, South Africa).",
"Reports from national parks and protected areas."
]
kalahari_desert["Tourism"]["Impact on Area"] = "Localized impacts around tourist facilities; potential for increased pressure on water resources."
kalahari_desert["Tourism"]["Impact on Biodiversity"] = "Disturbance to wildlife; habitat degradation (e.g., from off-road driving); potential for introduction of invasive species."
kalahari_desert["Tourism"]["Influenced By"] = [
"Economic Opportunities",
"Marketing and Promotion",
"Accessibility"
]
kalahari_desert["Tourism"]["Influences"] = [
"Deserts (Kalahari) - Wildlife Disturbance",
"Deserts (Kalahari) - Water Resources"
]
kalahari_desert["Tourism"]["Logic Description"] = "Tourism, while providing economic benefits, can also put pressure on fragile desert ecosystems if not managed sustainably."
kalahari_desert["Tourism"]["Impact Function"] = "impact_tourism_kalahari_desert"

# --- Deserts (Mojave) ---
mojave_desert = all_stressors_data["Mojave Deserts"]

mojave_desert["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality); increased frequency and severity of drought and heatwaves."
mojave_desert["Climate Change"]["Data Sources"] = [
"Climate models (global and regional).",
"Historical weather records.",
"Research publications."
]
mojave_desert["Climate Change"]["Impact on Area"] = "Increased aridity; potential for expansion of desert areas; changes in vegetation distribution."
mojave_desert["Climate Change"]["Impact on Biodiversity"] = "Increased stress on desert-adapted species, potentially exceeding their tolerance limits.; Shifts in species distributions; potential for local extinctions; impacts on water sources."
mojave_desert["Climate Change"]["Influenced By"] = ["Global GHG"]
mojave_desert["Climate Change"]["Influences"] = [
"Deserts (Mojave) - Water Scarcity",
"Deserts (Mojave) - Wildfires (potentially)",
"Deserts (Mojave) - Invasive Species (potentially)"
]
mojave_desert["Climate Change"]["Logic Description"] = "The Mojave Desert is highly vulnerable to climate change, with projections for increased temperatures, altered precipitation patterns, and more frequent and severe droughts."
mojave_desert["Climate Change"]["Impact Function"] = "impact_climate_change_mojave_desert"

mojave_desert["Water Extraction"]["Metric"] = "Groundwater levels; water extraction rates (m³/year); water use by different sectors."
mojave_desert["Water Extraction"]["Data Sources"] = [
"USGS water resource data.",
"California Department of Water Resources data.",
"Nevada Division of Water Resources data.",
"Research publications."
]
mojave_desert["Water Extraction"]["Impact on Area"] = "Depletion of groundwater aquifers; reduced water availability for springs and seeps; impacts on desert wetlands."
mojave_desert["Water Extraction"]["Impact on Biodiversity"] = "Loss of water sources for wildlife; decline of vegetation dependent on groundwater; impacts on aquatic and riparian ecosystems."
mojave_desert["Water Extraction"]["Influenced By"] = [
"Urban Water Demand (Las Vegas, other cities)",
"Agricultural Water Use (in some areas)",
"Mining Activities",
"Population Growth"
]
mojave_desert["Water Extraction"]["Influences"] = [
"Deserts (Mojave) - Water Availability",
"Deserts (Mojave) - Habitat Loss"
]
mojave_desert["Water Extraction"]["Logic Description"] = "Groundwater extraction, primarily for urban and agricultural use, is a major threat to water resources in the Mojave Desert, impacting springs, seeps, and other water-dependent ecosystems."
mojave_desert["Water Extraction"]["Impact Function"] = "impact_water_extraction_mojave_desert"

mojave_desert["Land-Use Change"]["Metric"] = "Area converted to urban development, agriculture, solar energy facilities, or other land uses (ha/year)."
mojave_desert["Land-Use Change"]["Data Sources"] = [
"Remote sensing data.",
"Land-use planning documents (county and city level).",
"USGS National Land Cover Database (NLCD).",
"Research publications."
]
mojave_desert["Land-Use Change"]["Impact on Area"] = "Habitat loss and fragmentation; increased pressure on remaining natural areas."
mojave_desert["Land-Use Change"]["Impact on Biodiversity"] = "Loss of habitat for desert species (e.g., desert tortoise, Mojave ground squirrel); disruption of wildlife movement; increased human-wildlife conflict."
mojave_desert["Land-Use Change"]["Influenced By"] = [
"Urban Sprawl (Las Vegas and other cities)",
"Renewable Energy Development (large-scale solar).",
"Agricultural Expansion (in some areas)",
"Mining Activities",
"Infrastructure Development"
]
mojave_desert["Land-Use Change"]["Influences"] = [
"Deserts (Mojave) - Habitat Fragmentation"
]
mojave_desert["Land-Use Change"]["Logic Description"] = "Land-use change, driven by urban sprawl, renewable energy development, and other factors, is leading to habitat loss and fragmentation in the Mojave Desert."
mojave_desert["Land-Use Change"]["Impact Function"] = "impact_land_use_change_mojave_desert"

mojave_desert["Invasive Species"]["Metric"] = "Abundance and distribution of key invasive species (e.g., cheatgrass, red brome, tamarisk)."
mojave_desert["Invasive Species"]["Data Sources"] = [
"Vegetation surveys.",
"Research studies.",
"Land management agency data (e.g., BLM, National Park Service)."
]
mojave_desert["Invasive Species"]["Impact on Area"] = "Changes in vegetation composition and structure; altered fire regimes."
mojave_desert["Invasive Species"]["Impact on Biodiversity"] = "Competition with native desert plants; increased fire frequency and intensity (due to invasive annual grasses); altered habitat for wildlife."
mojave_desert["Invasive Species"]["Influenced By"] = [
"Disturbance (e.g., off-road vehicle use, grazing, development)",
"Deserts (Mojave) - Climate Change",
"Introduction through human activities"
]
mojave_desert["Invasive Species"]["Influences"] = [
"Deserts (Mojave) - Fire Regimes",
"Deserts (Mojave) - Native Plant Communities"
]
mojave_desert["Invasive Species"]["Logic Description"] = "Invasive plants, particularly annual grasses, are altering fire regimes and outcompeting native desert vegetation in the Mojave."
mojave_desert["Invasive Species"]["Impact Function"] = "impact_invasive_species_mojave_desert"

mojave_desert["Off-Road Vehicle Use"]["Metric"] = "Area affected by off-road vehicle use; density of trails; frequency of use."
mojave_desert["Off-Road Vehicle Use"]["Data Sources"] = [
"Remote sensing data.",
"BLM data (on designated OHV areas).",
"Research studies."
]
mojave_desert["Off-Road Vehicle Use"]["Impact on Area"] = "Soil compaction; damage to vegetation (crushing plants, creating tracks); disturbance to wildlife; increased erosion; spread of invasive species."
mojave_desert["Off-Road Vehicle Use"]["Impact on Biodiversity"] = "Damage to fragile desert soils and vegetation (including cryptobiotic soil crusts).; Disturbance to desert animals (e.g., desert tortoise).; Spread of invasive species along trails."
mojave_desert["Off-Road Vehicle Use"]["Influenced By"] = [
"Recreational Activities",
"Lack of Enforcement of Regulations"
]
mojave_desert["Off-Road Vehicle Use"]["Influences"] = [
"Deserts (Mojave) - Soil Degradation",
"Deserts (Mojave) - Invasive Species",
"Deserts (Mojave) - Wildlife Disturbance"
]
mojave_desert["Off-Road Vehicle Use"]["Logic Description"] = "Off-road vehicle use is a significant stressor in the Mojave Desert, causing widespread damage to fragile soils, vegetation, and wildlife."
mojave_desert["Off-Road Vehicle Use"]["Impact Function"] = "impact_off_road_vehicle_use_mojave_desert"

mojave_desert["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., air pollutants, heavy metals) in air, water, and soil."
mojave_desert["Pollution"]["Data Sources"] = [
"Air and water quality monitoring data.",
"Research studies."
]
mojave_desert["Pollution"]["Impact on Area"] = "Degradation of air and water quality."
mojave_desert["Pollution"]["Impact on Biodiversity"] = "Toxic effects on plants and animals; impacts on sensitive desert ecosystems."
mojave_desert["Pollution"]["Influenced By"] = [
"Urban Areas (air pollution)",
"Deserts (Mojave) - Mining Activities",
"Industrial Activities",
"Agricultural Runoff"
]
mojave_desert["Pollution"]["Influences"] = [
"Deserts (Mojave) - Air Quality",
"Deserts (Mojave) - Water Quality"
]
mojave_desert["Pollution"]["Logic Description"] = "Pollution from urban areas, mining, and other sources can impact air and water quality in the Mojave Desert."
mojave_desert["Pollution"]["Impact Function"] = "impact_pollution_mojave_desert"

mojave_desert["Military Activities"]["Metric"] = "Area used for military training; frequency and intensity of military exercises."
mojave_desert["Military Activities"]["Data Sources"] = [
"Department of Defense data.",
"Research studies."
]
mojave_desert["Military Activities"]["Impact on Area"] = "Habitat disturbance and destruction; soil compaction; noise pollution; potential for chemical contamination."
mojave_desert["Military Activities"]["Impact on Biodiversity"] = "Disturbance to wildlife; habitat loss; potential for toxic effects from chemicals."
mojave_desert["Military Activities"]["Influenced By"] = [
"National Security Concerns",
"Military Training Requirements"
]
mojave_desert["Military Activities"]["Influences"] = [
"Deserts (Mojave) - Habitat Loss",
"Deserts (Mojave) - Pollution"
]
mojave_desert["Military Activities"]["Logic Description"] = "Large areas of the Mojave Desert are used for military training, which can cause significant habitat disturbance and other environmental impacts."
mojave_desert["Military Activities"]["Impact Function"] = "impact_military_activities_mojave_desert"

# --- Deserts (Namib) ---
namib_desert = all_stressors_data["Namib Deserts"]

namib_desert["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, which is already extremely low); changes in fog frequency and intensity."
namib_desert["Climate Change"]["Data Sources"] = [
"Climate models (global and regional).",
"Historical weather records (limited).",
"Research publications (specifically on Namib climate and fog)."
]
namib_desert["Climate Change"]["Impact on Area"] = "Increased aridity; potential shifts in the distribution of fog-dependent ecosystems."
namib_desert["Climate Change"]["Impact on Biodiversity"] = "Increased stress on desert-adapted species; potential impacts on fog-dependent species (e.g., beetles, lichens); shifts in species distributions."
namib_desert["Climate Change"]["Influenced By"] = ["Global GHG"]
namib_desert["Climate Change"]["Influences"] = [
"Deserts (Namib) - Water Availability",
"Deserts (Namib) - Fog Dynamics"
]
namib_desert["Climate Change"]["Logic Description"] = "The Namib Desert is one of the oldest and driest deserts in the world. Climate change is projected to make it even hotter and potentially alter the crucial fog patterns that many species depend on."
namib_desert["Climate Change"]["Impact Function"] = "impact_climate_change_namib_desert"

namib_desert["Mining"]["Metric"] = "Area affected by mining operations (ha); water use by mining; pollution levels (e.g., heavy metals, dust)."
namib_desert["Mining"]["Data Sources"] = [
"Mining company reports (e.g., Rössing Uranium).",
"Namibian government data (Ministry of Mines and Energy).",
"Environmental Impact Assessments (EIAs).",
"Research publications."
]
namib_desert["Mining"]["Impact on Area"] = "Habitat destruction; water extraction (in a water-scarce environment); pollution (dust, heavy metals)."
namib_desert["Mining"]["Impact on Biodiversity"] = "Loss of habitat; toxic effects of pollutants on wildlife; impacts on fragile desert ecosystems."
namib_desert["Mining"]["Influenced By"] = [
"Global Demand for Minerals (e.g., uranium, diamonds).",
"Government Policies (Namibia).",
"Economic Factors"
]
namib_desert["Mining"]["Influences"] = [
"Deserts (Namib) - Water Resources",
"Deserts (Namib) - Pollution",
"Deserts (Namib) - Habitat Loss"
]
namib_desert["Mining"]["Logic Description"] = "Mining, particularly for uranium and diamonds, is a significant economic activity in Namibia and poses environmental risks to the Namib Desert."
namib_desert["Mining"]["Impact Function"] = "impact_mining_namib_desert"

namib_desert["Coastal Development"]["Metric"] = "Area of coastline developed (km or ha); infrastructure development (ports, roads)."
namib_desert["Coastal Development"]["Data Sources"] = [
"Namibian government data.",
"Remote sensing data.",
"Research publications."
]
namib_desert["Coastal Development"]["Impact on Area"] = "Habitat loss and fragmentation; disturbance to coastal ecosystems."
namib_desert["Coastal Development"]["Impact on Biodiversity"] = "Impacts on coastal species (e.g., birds, seals, lichens); disruption of ecological processes."
namib_desert["Coastal Development"]["Influenced By"] = [
"Economic Development (e.g., ports, fisheries).",
"Population Growth (in coastal towns).",
"Tourism (though often focused on protected areas)"
]
namib_desert["Coastal Development"]["Influences"] = [
"Deserts (Namib) - Habitat Loss",
"Deserts (Namib) - Pollution"
]
namib_desert["Coastal Development"]["Logic Description"] = "Coastal development, including port expansion and other infrastructure, can impact coastal desert habitats and biodiversity."
namib_desert["Coastal Development"]["Impact Function"] = "impact_coastal_development_namib_desert"

namib_desert["Off-Road Driving"]["Metric"] = "Area affected by off-road vehicle tracks; frequency of off-road driving."
namib_desert["Off-Road Driving"]["Data Sources"] = [
"Remote sensing data.",
"Field surveys.",
"Reports from national parks and protected areas."
]
namib_desert["Off-Road Driving"]["Impact on Area"] = "Damage to fragile desert vegetation and soil crusts; soil compaction; disturbance to wildlife."
namib_desert["Off-Road Driving"]["Impact on Biodiversity"] = "Impacts on slow-growing lichens and other desert plants; disturbance to desert animals; habitat degradation."
namib_desert["Off-Road Driving"]["Influenced By"] = [
"Tourism",
"Recreational Activities",
"Mining Exploration",
"Lack of Enforcement of Regulations"
]
namib_desert["Off-Road Driving"]["Influences"] = [
"Deserts (Namib) - Soil Degradation",
"Deserts (Namib) - Habitat Damage"
]
namib_desert["Off-Road Driving"]["Logic Description"] = "Off-road driving, often associated with tourism and mining exploration, can cause significant and long-lasting damage to fragile desert ecosystems."
namib_desert["Off-Road Driving"]["Impact Function"] = "impact_off_road_driving_namib_desert"

namib_desert["Water Extraction"]["Metric"] = "Volume of groundwater extracted (m³/year); changes in groundwater levels."
namib_desert["Water Extraction"]["Data Sources"] = [
"Namibian government data (Department of Water Affairs).",
"Research publications."
]
namib_desert["Water Extraction"]["Impact on Area"] = "Depletion of groundwater resources; impacts on water-dependent ecosystems."
namib_desert["Water Extraction"]["Impact on Biodiversity"] = "Impacts on species that rely on groundwater sources (e.g., springs, oases); increased water stress on vegetation."
namib_desert["Water Extraction"]["Influenced By"] = [
"Mining Activities",
"Human Consumption",
"Climate Change (reduced recharge)"
]
namib_desert["Water Extraction"]["Influences"] = [
"Deserts (Namib) - Water Availability"
]
namib_desert["Water Extraction"]["Logic Description"] = "Groundwater extraction, even in a hyper-arid environment like the Namib, can impact scarce water resources and the ecosystems that depend on them."
namib_desert["Water Extraction"]["Impact Function"] = "impact_water_extraction_namib_desert"

# --- Deserts (Sahara) ---
sahara_desert = all_stressors_data["Sahara Deserts"]

sahara_desert["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality); increased frequency and severity of drought."
sahara_desert["Climate Change"]["Data Sources"] = [
"Climate models (global and regional).",
"Historical weather records (sparse in many areas).",
"Research publications."
]
sahara_desert["Climate Change"]["Impact on Area"] = "Increased aridity, potentially one of the largest changes on Earth; further expansion of desert areas; increased frequency and intensity of heatwaves."
sahara_desert["Climate Change"]["Impact on Biodiversity"] = "Extreme stress on already highly adapted species; shifts in species distributions; increased risk of local extinctions; impacts on oases and other water-dependent ecosystems."
sahara_desert["Climate Change"]["Influenced By"] = ["Global GHG"]
sahara_desert["Climate Change"]["Influences"] = [
"Deserts (Sahara) - Water Scarcity",
"Deserts (Sahara) - Desertification",
"Deserts (Sahara) - Dust Storms"
]
sahara_desert["Climate Change"]["Logic Description"] = "The Sahara Desert, already the largest hot desert in the world, is highly vulnerable to climate change, with projections for significantly increased temperatures and altered precipitation patterns."
sahara_desert["Climate Change"]["Impact Function"] = "impact_climate_change_sahara_desert"

sahara_desert["Desertification"]["Metric"] = "Expansion of desert-like conditions; loss of vegetation cover; soil degradation; increased dust storm frequency."
sahara_desert["Desertification"]["Data Sources"] = [
"Remote sensing data (vegetation indices, land cover change).",
"Soil surveys.",
"Research studies.",
"Climate records."
]
sahara_desert["Desertification"]["Impact on Area"] = "Loss of productive land (particularly on the margins of the desert); reduced carrying capacity for livestock and human populations."
sahara_desert["Desertification"]["Impact on Biodiversity"] = "Loss of habitat; changes in species composition; decline of native species; impacts on the already sparse vegetation."
sahara_desert["Desertification"]["Influenced By"] = [
"Deserts (Sahara) - Climate Change",
"Deserts (Sahara) - Overgrazing",
"Unsustainable Land Management Practices",
"Population Pressure (in some areas)"
]
sahara_desert["Desertification"]["Influences"] = [
"Deserts (Sahara) - Dust Storms",
"Deserts (Sahara) - Soil Degradation"
]
sahara_desert["Desertification"]["Logic Description"] = "Desertification, driven by climate change and human activities, is a major concern on the fringes of the Sahara, where fragile ecosystems are vulnerable to degradation."
sahara_desert["Desertification"]["Impact Function"] = "impact_desertification_sahara_desert"

sahara_desert["Overgrazing"]["Metric"] = "Livestock density; vegetation cover and composition; soil erosion indicators (limited due to the already sparse vegetation in many areas)."
sahara_desert["Overgrazing"]["Data Sources"] = [
"Agricultural statistics (from countries bordering the Sahara).",
"Remote sensing data (limited utility in very sparsely vegetated areas).",
"Research studies (focused on specific regions)."
]
sahara_desert["Overgrazing"]["Impact on Area"] = "Further degradation of already sparse vegetation, especially around oases and water sources; soil erosion; contributes to desertification."
sahara_desert["Overgrazing"]["Impact on Biodiversity"] = "Impacts on remaining vegetation; competition between livestock and native herbivores; increased pressure on scarce resources."
sahara_desert["Overgrazing"]["Influenced By"] = [
"Livestock Management Practices",
"Population Pressure (in some areas)",
"Access to Water Sources"
]
sahara_desert["Overgrazing"]["Influences"] = [
"Deserts (Sahara) - Desertification",
"Deserts (Sahara) - Soil Degradation"
]
sahara_desert["Overgrazing"]["Logic Description"] = "Overgrazing, particularly around oases and water sources, exacerbates land degradation and desertification in the Sahara."
sahara_desert["Overgrazing"]["Impact Function"] = "impact_overgrazing_sahara_desert"

sahara_desert["Water Scarcity"]["Metric"] = "Groundwater levels; water extraction rates; availability of surface water (extremely limited)."
sahara_desert["Water Scarcity"]["Data Sources"] = [
"Groundwater monitoring data (sparse in many areas).",
"Research studies."
]
sahara_desert["Water Scarcity"]["Impact on Area"] = "Depletion of groundwater resources; impacts on oases (which are crucial for human and animal populations).  Water scarcity is a *defining characteristic* of the Sahara."
sahara_desert["Water Scarcity"]["Impact on Biodiversity"] = "Extreme water stress on all life; impacts on species dependent on oases and other limited water sources."
sahara_desert["Water Scarcity"]["Influenced By"] = [
"Deserts (Sahara) - Climate Change",
"Water Extraction (for human use and, in some cases, agriculture)",
"Population Growth (in some areas)"
]
sahara_desert["Water Scarcity"]["Influences"] = [
"Deserts (Sahara) - Human and Animal Survival"
]
sahara_desert["Water Scarcity"]["Logic Description"] = "Water scarcity is an *inherent* and extreme challenge in the Sahara Desert. Climate change and increasing water demand are exacerbating this challenge."
sahara_desert["Water Scarcity"]["Impact Function"] = "impact_water_scarcity_sahara_desert"

sahara_desert["Land-Use Change"]["Metric"] = "Area converted to other land uses (limited, but includes oil/gas extraction, some agriculture near oases, and infrastructure)."
sahara_desert["Land-Use Change"]["Data Sources"] = [
"Remote sensing data.",
"Government reports (e.g., on oil and gas development).",
"Research publications."
]
sahara_desert["Land-Use Change"]["Impact on Area"] = "Localized habitat loss and fragmentation (though overall land-use change is less extensive than in many other deserts due to the Sahara's harsh conditions)."
sahara_desert["Land-Use Change"]["Impact on Biodiversity"] = "Impacts on fragile ecosystems; potential for pollution and disturbance."
sahara_desert["Land-Use Change"]["Influenced By"] = [
"Oil and Gas Exploration and Extraction",
"Infrastructure Development (roads, pipelines)",
"Agricultural Expansion (limited, near oases)"
]
sahara_desert["Land-Use Change"]["Influences"] = [
"Deserts (Sahara) - Habitat Loss"
]
sahara_desert["Land-Use Change"]["Logic Description"] = "While large-scale land-use change is limited by the Sahara's extreme environment, localized changes (oil/gas, infrastructure) can have significant impacts."
sahara_desert["Land-Use Change"]["Impact Function"] = "impact_land_use_change_sahara_desert"

sahara_desert["Dust Storms"]["Metric"] = "Frequency and intensity of dust storms; dust concentration in the atmosphere; area affected by dust deposition."
sahara_desert["Dust Storms"]["Data Sources"] = [
"Satellite data (dust detection).",
"Meteorological data.",
"Research publications."
]
sahara_desert["Dust Storms"]["Impact on Area"] = "Reduced visibility; impacts on air quality; soil erosion; transport of dust (and associated nutrients and pollutants) over long distances."
sahara_desert["Dust Storms"]["Impact on Biodiversity"] = "Impacts on plant growth (reduced sunlight); potential impacts on animal health (respiratory problems); can fertilize distant ecosystems (e.g., the Amazon rainforest)."
sahara_desert["Dust Storms"]["Influenced By"] = [
"Deserts (Sahara) - Climate Change",
"Deserts (Sahara) - Desertification",
"Wind Patterns"
]
sahara_desert["Dust Storms"]["Influences"] = [
"Global Climate Patterns",
"Air Quality (globally)",
"Ocean Fertilization"
]
sahara_desert["Dust Storms"]["Logic Description"] = "The Sahara Desert is the world's largest source of dust. Dust storms are a natural phenomenon, but they can be exacerbated by climate change and desertification."
sahara_desert["Dust Storms"]["Impact Function"] = "impact_dust_storms_sahara_desert"

sahara_desert["Political Instability"]["Metric"] = "Incidence of conflict; governance indicators; security risks."
sahara_desert["Political Instability"]["Data Sources"] = [
"News reports.",
"Political risk assessments.",
"Reports from international organizations (e.g., UN)."
]
sahara_desert["Political Instability"]["Impact on Area"] = "Disruption of conservation efforts; increased difficulty in managing natural resources; potential for increased illegal activities (e.g., poaching, resource exploitation)."
sahara_desert["Political Instability"]["Impact on Biodiversity"] = "Indirect impacts through reduced conservation efforts and increased resource exploitation."
sahara_desert["Political Instability"]["Influenced By"] = [
"Complex socio-political factors",
"Economic factors",
"Historical factors"
]
sahara_desert["Political Instability"]["Influences"] = [
"Resource Management",
"Conservation Efforts"
]
sahara_desert["Political Instability"]["Logic Description"] = "Political instability and conflict in parts of the Sahara region can hinder conservation efforts and exacerbate environmental problems."
sahara_desert["Political Instability"]["Impact Function"] = "impact_political_instability_sahara_desert"

# --- Deserts (Sonoran) ---
sonoran_desert = all_stressors_data["Sonoran Deserts"]

sonoran_desert["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality); increased frequency and severity of drought and heatwaves."
sonoran_desert["Climate Change"]["Data Sources"] = [
"Climate models (global and regional).",
"Historical weather records.",
"Research publications."
]
sonoran_desert["Climate Change"]["Impact on Area"] = "Increased aridity; potential shifts in vegetation zones; increased fire risk in some areas."
sonoran_desert["Climate Change"]["Impact on Biodiversity"] = "Increased stress on desert-adapted species; potential for range shifts and local extinctions; impacts on water sources."
sonoran_desert["Climate Change"]["Influenced By"] = ["Global GHG"]
sonoran_desert["Climate Change"]["Influences"] = [
"Deserts (Sonoran) - Water Scarcity",
"Deserts (Sonoran) - Wildfires (in higher-elevation areas)"
]
sonoran_desert["Climate Change"]["Logic Description"] = "The Sonoran Desert, already a hot and dry environment, is vulnerable to climate change, with projections for increased temperatures, altered rainfall patterns, and more extreme events."
sonoran_desert["Climate Change"]["Impact Function"] = "impact_climate_change_sonoran_desert"

sonoran_desert["Water Extraction"]["Metric"] = "Groundwater levels; water extraction rates (m³/year); water use by different sectors (agriculture, urban, mining)."
sonoran_desert["Water Extraction"]["Data Sources"] = [
"USGS water resource data.",
"Arizona Department of Water Resources data.",
"Mexican government data (CONAGUA).",
"Research publications."
]
sonoran_desert["Water Extraction"]["Impact on Area"] = "Depletion of groundwater resources; reduced water availability for springs, streams, and riparian habitats."
sonoran_desert["Water Extraction"]["Impact on Biodiversity"] = "Impacts on water-dependent species (e.g., fish, amphibians, riparian vegetation); increased competition for water; habitat loss."
sonoran_desert["Water Extraction"]["Influenced By"] = [
"Agricultural Water Use",
"Urban Water Demand (Phoenix, Tucson, Hermosillo, etc.)",
"Mining Activities"
]
sonoran_desert["Water Extraction"]["Influences"] = [
"Deserts (Sonoran) - Water Availability",
"Deserts (Sonoran) - Riparian Habitat Loss"
]
sonoran_desert["Water Extraction"]["Logic Description"] = "Groundwater extraction, primarily for agriculture and urban use, is a major threat to water resources in the Sonoran Desert, impacting both human populations and desert ecosystems."
sonoran_desert["Water Extraction"]["Impact Function"] = "impact_water_extraction_sonoran_desert"

sonoran_desert["Land-Use Change"]["Metric"] = "Area converted to agriculture, urban development, or other land uses (ha/year)."
sonoran_desert["Land-Use Change"]["Data Sources"] = [
"Remote sensing data.",
"Land-use planning documents.",
"USGS National Land Cover Database (NLCD).",
"Research publications."
]
sonoran_desert["Land-Use Change"]["Impact on Area"] = "Habitat loss and fragmentation; increased pressure on remaining natural areas."
sonoran_desert["Land-Use Change"]["Impact on Biodiversity"] = "Loss of habitat for desert species (e.g., saguaro cactus, desert tortoise); disruption of wildlife movement; increased human-wildlife conflict."
sonoran_desert["Land-Use Change"]["Influenced By"] = [
"Urban Sprawl (Phoenix, Tucson, and other cities)",
"Agricultural Expansion",
"Infrastructure Development (roads, pipelines)",
"Deserts (Sonoran) - Border Wall Impacts"
]
sonoran_desert["Land-Use Change"]["Influences"] = [
"Deserts (Sonoran) - Habitat Fragmentation"
]
sonoran_desert["Land-Use Change"]["Logic Description"] = "Land-use change, driven by urban sprawl, agriculture, and infrastructure development, is leading to habitat loss and fragmentation in the Sonoran Desert."
sonoran_desert["Land-Use Change"]["Impact Function"] = "impact_land_use_change_sonoran_desert"

sonoran_desert["Invasive Species"]["Metric"] = "Abundance and distribution of key invasive species (e.g., buffelgrass, fountain grass)."
sonoran_desert["Invasive Species"]["Data Sources"] = [
"Vegetation surveys.",
"Research studies.",
"Land management agency data."
]
sonoran_desert["Invasive Species"]["Impact on Area"] = "Changes in vegetation composition and structure; altered fire regimes (buffelgrass in particular)."
sonoran_desert["Invasive Species"]["Impact on Biodiversity"] = "Competition with native desert plants; increased fire frequency and intensity (buffelgrass); impacts on wildlife habitat."
sonoran_desert["Invasive Species"]["Influenced By"] = [
"Disturbance (e.g., grazing, off-road vehicle use, development).",
"Deserts (Sonoran) - Climate Change (may favor some invasives).",
"Intentional and Accidental Introductions"
]
sonoran_desert["Invasive Species"]["Influences"] = [
"Deserts (Sonoran) - Fire Regimes",
"Deserts (Sonoran) - Native Plant Communities"
]
sonoran_desert["Invasive Species"]["Logic Description"] = "Invasive plants, particularly buffelgrass, are a major threat to the Sonoran Desert, outcompeting native species and dramatically increasing fire risk."
sonoran_desert["Invasive Species"]["Impact Function"] = "impact_invasive_species_sonoran_desert"

sonoran_desert["Urbanization"]["Metric"] = "Urban area expansion; population growth in cities; road density."
sonoran_desert["Urbanization"]["Data Sources"] = [
"Urban planning data.",
"Census data.",
"Remote sensing."
]
sonoran_desert["Urbanization"]["Impact on Area"] = "Habitat loss and fragmentation; increased demand for water resources."
sonoran_desert["Urbanization"]["Impact on Biodiversity"] = "Loss of habitat; impacts on wildlife; increased human-wildlife conflict; urban heat island effect."
sonoran_desert["Urbanization"]["Influenced By"] = [
"Population Growth",
"Economic Development"
]
sonoran_desert["Urbanization"]["Influences"] = [
"Deserts (Sonoran) - Habitat Loss",
"Deserts (Sonoran) - Water Scarcity"
]
sonoran_desert["Urbanization"]["Logic Description"] = "Urban sprawl, particularly in cities like Phoenix and Tucson, is a growing threat to the Sonoran Desert, leading to habitat loss and increased demand for water."
sonoran_desert["Urbanization"]["Impact Function"] = "impact_urbanization_sonoran_desert"

sonoran_desert["Border Wall Impacts"]["Metric"] = "Length of border wall constructed; area directly impacted; disruption of wildlife movement corridors."
sonoran_desert["Border Wall Impacts"]["Data Sources"] = [
"Government reports (e.g., U.S. Customs and Border Protection).",
"Research studies.",
"Remote sensing data."
]
sonoran_desert["Border Wall Impacts"]["Impact on Area"] = "Habitat fragmentation; barrier to wildlife movement."
sonoran_desert["Border Wall Impacts"]["Impact on Biodiversity"] = "Disruption of migration routes and gene flow for wildlife (e.g., jaguars, pronghorn, bighorn sheep); isolation of populations; increased mortality."
sonoran_desert["Border Wall Impacts"]["Influenced By"] = [
"Political Decisions",
"Security Concerns"
]
sonoran_desert["Border Wall Impacts"]["Influences"] = [
"Deserts (Sonoran) - Habitat Fragmentation",
"Deserts (Sonoran) - Wildlife Movement"
]
sonoran_desert["Border Wall Impacts"]["Logic Description"] = "The construction of a wall along the U.S.-Mexico border fragments habitat and blocks wildlife movement corridors, impacting species that range across the border."
sonoran_desert["Border Wall Impacts"]["Impact Function"] = "impact_border_wall_impacts_sonoran_desert"

# --- Agroforestry ---
agroforestry = all_stressors_data["Agroforestry"]

agroforestry["Land Use Change"]["Metric"] = "Conversion of natural forest or other land cover types to agroforestry systems; conversion of agroforestry to other land uses (e.g., monoculture agriculture, urban development)."
agroforestry["Land Use Change"]["Data Sources"] = [
"Remote sensing data (satellite imagery, aerial photography).",
"Land use/land cover maps.",
"Agricultural statistics.",
"Research publications."
]
agroforestry["Land Use Change"]["Impact on Area"] = "Changes in land cover and landscape structure.  Can be *positive* (e.g., converting degraded land to agroforestry) or *negative* (e.g., converting forest to a simplified agroforestry system)."
agroforestry["Land Use Change"]["Impact on Biodiversity"] = "Depends on the type of agroforestry system and the previous land use. Agroforestry can *increase* biodiversity compared to monoculture agriculture, but may *decrease* it compared to natural forest. Can provide habitat for some species, but may not support specialized forest species."
agroforestry["Land Use Change"]["Influenced By"] = [
"Agroforestry - Economic Incentives",
"Agroforestry - Government Policies",
"Agroforestry - Population Pressure",
"Agroforestry - Climate Change"
]
agroforestry["Land Use Change"]["Influences"] = [
"Habitat availability (for some species)." #Generic influence.
]
agroforestry["Land Use Change"]["Logic Description"] = "Conversion of land *to* or *from* agroforestry can have significant impacts on biodiversity and ecosystem services, depending on the context.  Agroforestry can be more sustainable than intensive agriculture, but less biodiverse than natural forest."
agroforestry["Land Use Change"]["Impact Function"] = "impact_land_use_change_agroforestry"

agroforestry["Management Practices"]["Metric"] = "Tree density; species composition; use of fertilizers and pesticides; pruning and thinning practices; soil management practices."
agroforestry["Management Practices"]["Data Sources"] = [
"Field surveys.",
"Agricultural statistics.",
"Research publications."
]
agroforestry["Management Practices"]["Impact on Area"] = "Influences the structure and function of the agroforestry system."
agroforestry["Management Practices"]["Impact on Biodiversity"] = "Species diversity of trees and understory plants.; Habitat quality for wildlife.; Soil health and nutrient cycling."
agroforestry["Management Practices"]["Influenced By"] = [
"Agroforestry - Farmer Knowledge and Skills",
"Agroforestry - Economic Factors",
"Agroforestry - Access to Resources",
"Agroforestry - Government Policies and Extension Services"
]
agroforestry["Management Practices"]["Influences"] = [
"Agroforestry - Soil Degradation",
"Agroforestry - Water Quality",
"Agroforestry - Pest and Disease Outbreaks",
"Agroforestry - Carbon Sequestration"
]
agroforestry["Management Practices"]["Logic Description"] = "The specific management practices used in an agroforestry system (e.g., tree species selection, planting density, pruning, fertilization) have a major influence on its biodiversity, productivity, and ecosystem services."
agroforestry["Management Practices"]["Impact Function"] = "impact_management_practices_agroforestry"

agroforestry["Climate Change"]["Metric"] = "Changes in temperature, precipitation, and extreme weather events."
agroforestry["Climate Change"]["Data Sources"] = [
"Climate models.",
"Historical weather data."
]
agroforestry["Climate Change"]["Impact on Area"] = "Changes in growing conditions."
agroforestry["Climate Change"]["Impact on Biodiversity"] = "May affect the suitability of certain tree and crop species.;   Increased stress on plants and animals.;     Changes in pest and disease dynamics."
agroforestry["Climate Change"]["Influenced By"] = [
"Global Greenhouse Gas Emissions"
]
agroforestry["Climate Change"]["Influences"] = [
"Agroforestry - Water Availability",
"Agroforestry - Pest and Disease Outbreaks",
"Agroforestry - Tree and Crop Productivity"
]
agroforestry["Climate Change"]["Logic Description"] = "Climate change can alter growing conditions, making some agroforestry systems less viable or requiring adaptation."
agroforestry["Climate Change"]["Impact Function"] = "impact_climate_change_agroforestry"

agroforestry["Pest and Disease Outbreaks"]["Metric"] = "Incidence and severity of pest and disease outbreaks."
agroforestry["Pest and Disease Outbreaks"]["Data Sources"] = [
"Field surveys.",
"Agricultural statistics.",
"Research publications."
]
agroforestry["Pest and Disease Outbreaks"]["Impact on Area"] = "Reduced tree and crop productivity; economic losses."
agroforestry["Pest and Disease Outbreaks"]["Impact on Biodiversity"] = "Can impact both crop and non-crop species."
agroforestry["Pest and Disease Outbreaks"]["Influenced By"] = [
"Agroforestry - Management Practices",
"Agroforestry - Climate Change",
"Agroforestry - Introduction of Exotic Species"
]
agroforestry["Pest and Disease Outbreaks"]["Influences"] = [
"Agroforestry - Tree and Crop Productivity"
]
agroforestry["Pest and Disease Outbreaks"]["Logic Description"] = "Pest and disease outbreaks can damage or kill trees and crops in agroforestry systems."
agroforestry["Pest and Disease Outbreaks"]["Impact Function"] = "impact_pest_and_disease_outbreaks_agroforestry"

agroforestry["Soil Degradation"]["Metric"] = "Soil organic matter content; soil erosion rate; nutrient depletion; soil compaction."
agroforestry["Soil Degradation"]["Data Sources"] = [
"Soil surveys.",
"Research publications."
]
agroforestry["Soil Degradation"]["Impact on Area"] = "Reduced soil fertility and productivity."
agroforestry["Soil Degradation"]["Impact on Biodiversity"] = "Impacts on soil organisms."
agroforestry["Soil Degradation"]["Influenced By"] = [
"Agroforestry - Management Practices",
"Agroforestry - Overgrazing",
"Agroforestry - Erosion"
]
agroforestry["Soil Degradation"]["Influences"] = [
"Agroforestry - Tree and Crop Productivity",
"Agroforestry - Water Quality"
]
agroforestry["Soil Degradation"]["Logic Description"] = "Soil degradation can reduce the productivity and sustainability of agroforestry systems."
agroforestry["Soil Degradation"]["Impact Function"] = "impact_soil_degradation_agroforestry"

agroforestry["Water Availability"]["Metric"] = "Rainfall amount and distribution, soil moisture content, access to irrigation."
agroforestry["Water Availability"]["Data Sources"] = [
"Weather data",
"Hydrological models."
]
agroforestry["Water Availability"]["Impact on Area"] = "Affects tree and crop growth."
agroforestry["Water Availability"]["Impact on Biodiversity"] = "Water stress can impact both plants and animals."
agroforestry["Water Availability"]["Influenced By"] = [
"Agroforestry - Climate Change",
"Agroforestry - Water Use"
]
agroforestry["Water Availability"]["Influences"] = [
"Agroforestry - Tree and Crop Productivity",
]
agroforestry["Water Availability"]["Logic Description"] = "Water availability is essential for plant growth and overall system productivity."
agroforestry["Water Availability"]["Impact Function"] = "impact_water_availability_agroforestry"

agroforestry["Market Access"]["Metric"] = "Access to markets for agroforestry products."
agroforestry["Market Access"]["Data Sources"] = ["Economic data", "Surveys"]
agroforestry["Market Access"]["Impact on Area"] = "Influences the economic viability"
agroforestry["Market Access"]["Impact on Biodiversity"] = "Indirect - may influence farmer decisions about crop/tree selection."
agroforestry["Market Access"]["Influenced By"] = ["Economic factors, infrastructure."]
agroforestry["Market Access"]["Influences"] = [
"Agroforestry - Economic Incentives"
]
agroforestry["Market Access"]["Logic Description"] = "Market access is crucial for the economic success."
agroforestry["Market Access"]["Impact Function"] = "impact_market_access_agroforestry"

agroforestry["Farmer Knowledge and Skills"]["Metric"] = "Level of farmer knowledge about agroforestry practices."
agroforestry["Farmer Knowledge and Skills"]["Data Sources"] = ["Surveys", "Research"]
agroforestry["Farmer Knowledge and Skills"]["Impact on Area"] = "Influences management decisions."
agroforestry["Farmer Knowledge and Skills"]["Impact on Biodiversity"] = "Can influence the success of the system in supporting biodiversity"
agroforestry["Farmer Knowledge and Skills"]["Influenced By"] = [ "Education, extension services."]
agroforestry["Farmer Knowledge and Skills"]["Influences"] = ["Agroforestry - Management Practices."]
agroforestry["Farmer Knowledge and Skills"]["Logic Description"] = "Farmer knowledge is crucial for effective agroforestry."
agroforestry["Farmer Knowledge and Skills"]["Impact Function"] = "impact_farmer_knowledge_skills_agroforestry"


agroforestry["Economic Incentives"]["Metric"] = "Prices for agroforestry products, subsidies, etc."
agroforestry["Economic Incentives"]["Data Sources"] = ["Economic data"]
agroforestry["Economic Incentives"]["Impact on Area"] = "Influences farmer decisions"
agroforestry["Economic Incentives"]["Impact on Biodiversity"] = "Indirect - influences management practices."
agroforestry["Economic Incentives"]["Influenced By"] = ["Agroforestry - Market Access"]
agroforestry["Economic Incentives"]["Influences"] = [
"Agroforestry - Management Practices",
"Agroforestry - Land Use Change"
]
agroforestry["Economic Incentives"]["Logic Description"] = "Economic incentives influence farmer decisions."
agroforestry["Economic Incentives"]["Impact Function"] = "impact_economic_incentives_agroforestry"

agroforestry["Government Policies"]["Metric"] = "Regulations, subsidies, land tenure policies"
agroforestry["Government Policies"]["Data Sources"] = ["Policy documents"]
agroforestry["Government Policies"]["Impact on Area"] = "Variable"
agroforestry["Government Policies"]["Impact on Biodiversity"] = "Variable"
agroforestry["Government Policies"]["Influenced By"] = ["Politics, economics"]
agroforestry["Government Policies"]["Influences"] = [
"Agroforestry - Land Use Change",
"Agroforestry - Management Practices"
]
agroforestry["Government Policies"]["Logic Description"] = "Policies can promote or hinder agroforestry."
agroforestry["Government Policies"]["Impact Function"] = "impact_government_policies_agroforestry"

agroforestry["Population Pressure"]["Metric"] = "Population density, land scarcity"
agroforestry["Population Pressure"]["Data Sources"] = ["Census data"]
agroforestry["Population Pressure"]["Impact on Area"] = "Can lead to land conversion and intensification."
agroforestry["Population Pressure"]["Impact on Biodiversity"] = "Variable, depends on how land use changes."
agroforestry["Population Pressure"]["Influenced By"] = ["Socioeconomic factors."]
agroforestry["Population Pressure"]["Influences"] = [
"Agroforestry - Land Use Change"
]
agroforestry["Population Pressure"]["Logic Description"] = "Population pressure influences land use."
agroforestry["Population Pressure"]["Impact Function"] = "impact_population_pressure_agroforestry"

agroforestry["Access to Resources"]["Metric"] = "Availability of planting materials, fertilizers, tools, credit."
agroforestry["Access to Resources"]["Data Sources"] = [
"Surveys",
"Research studies."
]
agroforestry["Access to Resources"]["Impact on Area"] = "Influences the ability of farmers to implement agroforestry."
agroforestry["Access to Resources"]["Impact on Biodiversity"] = "Indirect, through impacts on management practices."
agroforestry["Access to Resources"]["Influenced By"] = [
"Economic factors",
"Government policies."
]
agroforestry["Access to Resources"]["Influences"] = [
"Agroforestry - Management Practices"
]
agroforestry["Access to Resources"]["Logic Description"] = "Resources are needed to implement agroforestry."
agroforestry["Access to Resources"]["Impact Function"] = "impact_access_to_resources_agroforestry"

agroforestry["Carbon Sequestration"]["Metric"] = "Amount of carbon stored in trees and soil."
agroforestry["Carbon Sequestration"]["Data Sources"] = [
"Field measurements",
"Models."
]
agroforestry["Carbon Sequestration"]["Impact on Area"] = "Positive - contributes to climate change mitigation."
agroforestry["Carbon Sequestration"]["Impact on Biodiversity"] = "Indirect - helps mitigate climate change, which benefits biodiversity in the long run."
agroforestry["Carbon Sequestration"]["Influenced By"] = [
"Agroforestry - Management Practices"
]
agroforestry["Carbon Sequestration"]["Influences"] = [
"Global climate change (mitigation)."
]
agroforestry["Carbon Sequestration"]["Logic Description"] = "Agroforestry can sequester carbon, helping to mitigate climate change."
agroforestry["Carbon Sequestration"]["Impact Function"] = "impact_carbon_sequestration_agroforestry"

agroforestry["Tree and Crop Productivity"]["Metric"] = "Yields of trees and crops."
agroforestry["Tree and Crop Productivity"]["Data Sources"] = [
"Field measurements.",
"Agricultural statistics."
]
agroforestry["Tree and Crop Productivity"]["Impact on Area"] = "Economic viability of agroforestry."
agroforestry["Tree and Crop Productivity"]["Impact on Biodiversity"] = "Indirect."
agroforestry["Tree and Crop Productivity"]["Influenced By"] = [
"Many, Varies"
]
agroforestry["Tree and Crop Productivity"]["Influences"] = [
"Livelihoods."
]
agroforestry["Tree and Crop Productivity"]["Logic Description"] = "Productivity is key for economic viability"
agroforestry["Tree and Crop Productivity"]["Impact Function"] = "impact_tree_and_crop_productivity_agroforestry"

agroforestry["Introduction of Exotic Species"]["Metric"] = "Number and abundance of exotic tree/crop"
agroforestry["Introduction of Exotic Species"]["Data Sources"] = [
"Field surveys"
]
agroforestry["Introduction of Exotic Species"]["Impact on Area"] = "Can be positive (if well-managed) or negative (if invasive)."
agroforestry["Introduction of Exotic Species"]["Impact on Biodiversity"] = "Potential for negative impacts if species become invasive."
agroforestry["Introduction of Exotic Species"]["Influenced By"] = [
"Agroforestry - Management Practices"
]
agroforestry["Introduction of Exotic Species"]["Influences"] = [
"Agroforestry - Pest and Disease Outbreaks"
]
agroforestry["Introduction of Exotic Species"]["Logic Description"] = "Exotic species can be beneficial or detrimental."
agroforestry["Introduction of Exotic Species"]["Impact Function"] = "impact_introduction_of_exotic_species_agroforestry"

agroforestry["Erosion"]["Metric"] = "Soil Loss"
agroforestry["Erosion"]["Data Sources"] = [
"Field measurements",
"Models"
]
agroforestry["Erosion"]["Impact on Area"] = "Reduces soil fertility."
agroforestry["Erosion"]["Impact on Biodiversity"] = "Negative impacts"
agroforestry["Erosion"]["Influenced By"] = [
"Agroforestry - Soil Degradation"
]
agroforestry["Erosion"]["Influences"] = [
"Agroforestry - Soil Degradation"
]
agroforestry["Erosion"]["Logic Description"] = "Loss of soil."
agroforestry["Erosion"]["Impact Function"] = "impact_erosion_agroforestry"

agroforestry["Water Use"]["Metric"] = "Water consumption by trees and crops."
agroforestry["Water Use"]["Data Sources"] = [
"Field measurements",
"Models"
]
agroforestry["Water Use"]["Impact on Area"] = "Water balance"
agroforestry["Water Use"]["Impact on Biodiversity"] = "Can impact downstream water availability."
agroforestry["Water Use"]["Influenced By"] = [
"Agroforestry - Climate Change",
"Species Choices"
]
agroforestry["Water Use"]["Influences"] = [
"Agroforestry - Water Availability"
]
agroforestry["Water Use"]["Logic Description"] = "Water Use"
agroforestry["Water Use"]["Impact Function"] = "impact_water_use_agroforestry"

# --- Aquaculture ---
aquaculture = all_stressors_data["Aquaculture"]

aquaculture["Water Pollution"]["Metric"] = "Concentrations of nutrients (nitrogen, phosphorus), organic matter, and other pollutants (e.g., antibiotics, pesticides, antifoulants) in effluent from aquaculture facilities."
aquaculture["Water Pollution"]["Data Sources"] = [
"Water quality monitoring data from aquaculture farms (often required by regulations).",
"Government environmental agencies.",
"Research studies."
]
aquaculture["Water Pollution"]["Impact on Area"] = "Degradation of water quality in surrounding water bodies."
aquaculture["Water Pollution"]["Impact on Biodiversity"] = "Eutrophication (nutrient enrichment) leading to algal blooms and oxygen depletion in receiving waters. Toxic effects of pollutants on aquatic organisms. Impacts on wild fish populations and other wildlife."
aquaculture["Water Pollution"]["Influenced By"] = [
"Aquaculture - Feed Type and Management",
"Aquaculture - Stocking Density",
"Aquaculture - Waste Management Practices",
"Aquaculture - Water Exchange Rates",
"Aquaculture - Use of Antibiotics and Other Chemicals"
]
aquaculture["Water Pollution"]["Influences"] = [
"Eutrophication (in receiving waters).",
"Water Quality (in surrounding ecosystems).",
"Disease Outbreaks (in wild populations - potentially)."
]
aquaculture["Water Pollution"]["Logic Description"] = "Aquaculture facilities can release significant amounts of pollutants into the surrounding environment, including excess nutrients, organic matter, antibiotics, pesticides, and antifouling agents. This pollution can degrade water quality and harm aquatic life."
aquaculture["Water Pollution"]["Impact Function"] = "impact_water_pollution_aquaculture"

aquaculture["Habitat Conversion"]["Metric"] = "Area of natural habitats (e.g., mangroves, seagrass beds, wetlands) converted to aquaculture ponds (ha/year)."
aquaculture["Habitat Conversion"]["Data Sources"] = [
"Remote sensing data.",
"Government statistics (aquaculture development).",
"Reports from environmental organizations."
]
aquaculture["Habitat Conversion"]["Impact on Area"] = "Loss of important coastal and wetland habitats."
aquaculture["Habitat Conversion"]["Impact on Biodiversity"] = "Major loss of habitat for many species (especially mangroves and other coastal wetlands).; Reduced nursery grounds for wild fish and shellfish.; Loss of coastal protection (if mangroves are removed).; Loss of carbon sequestration."
aquaculture["Habitat Conversion"]["Influenced By"] = [
"Aquaculture - Demand for Aquaculture Products",
"Aquaculture - Economic Incentives",
"Aquaculture - Government Policies",
"Aquaculture - Land Availability"
]
aquaculture["Habitat Conversion"]["Influences"] = [
"Habitat Loss (the primary impact).",
"Coastal Erosion (if mangroves are removed)."
]
aquaculture["Habitat Conversion"]["Logic Description"] = "The conversion of natural habitats, particularly mangroves, seagrass beds, and other coastal wetlands, to aquaculture ponds is a major environmental impact, leading to significant biodiversity loss and ecosystem degradation."
aquaculture["Habitat Conversion"]["Impact Function"] = "impact_habitat_conversion_aquaculture"

aquaculture["Disease Outbreaks"]["Metric"] = "Frequency and severity of disease outbreaks in aquaculture facilities; use of antibiotics and other chemicals."
aquaculture["Disease Outbreaks"]["Data Sources"] = [
"Aquaculture industry reports.",
"Veterinary records.",
"Research studies."
]
aquaculture["Disease Outbreaks"]["Impact on Area"] = "Can lead to the release of pathogens and chemicals into the environment."
aquaculture["Disease Outbreaks"]["Impact on Biodiversity"] = "Disease outbreaks can spread from farmed fish to wild fish populations.; Use of antibiotics can lead to antibiotic resistance in bacteria.; Use of other chemicals can have toxic effects on non-target organisms."
aquaculture["Disease Outbreaks"]["Influenced By"] = [
"Aquaculture - Stocking Density",
"Aquaculture - Water Quality",
"Aquaculture - Feed Quality",
"Aquaculture - Introduction of Non-Native Species",
"Aquaculture - Biosecurity Measures"
]
aquaculture["Disease Outbreaks"]["Influences"] = [
"Aquaculture - Water Pollution",
"Wild Fish Populations (potential for disease transmission)."
]
aquaculture["Disease Outbreaks"]["Logic Description"] = "Disease outbreaks are common in aquaculture facilities due to high stocking densities and stress. These can lead to antibiotic use and potentially spread to wild populations."
aquaculture["Disease Outbreaks"]["Impact Function"] = "impact_disease_outbreaks_aquaculture"

aquaculture["Escaped Fish"]["Metric"] = "Number and frequency of escape events; genetic makeup of escaped fish."
aquaculture["Escaped Fish"]["Data Sources"] = [
"Aquaculture facility reports",
"Research studies"
]
aquaculture["Escaped Fish"]["Impact on Area"] = "Introduction of non-native or genetically modified organisms."
aquaculture["Escaped Fish"]["Impact on Biodiversity"] = "Competition with and predation on wild fish.; Genetic impacts on wild populations (if interbreeding occurs).; Spread of diseases."
aquaculture["Escaped Fish"]["Influenced By"] = [
"Aquaculture - Management Practices",
"Storm events.",
"Infrastructure failures."
]
aquaculture["Escaped Fish"]["Influences"] = [
"Wild Fish Populations (genetics, competition, disease)."
]
aquaculture["Escaped Fish"]["Logic Description"] = "Escaped farmed fish can impact wild populations through competition, predation, disease transmission, and genetic mixing."
aquaculture["Escaped Fish"]["Impact Function"] = "impact_escaped_fish_aquaculture"

aquaculture["Introduction of Non-Native Species"]["Metric"] = "Number of non-native species used in aquaculture."
aquaculture["Introduction of Non-Native Species"]["Data Sources"] = [
"Aquaculture industry records.",
"Government permits."
]
aquaculture["Introduction of Non-Native Species"]["Impact on Area"] = "Potential for establishment of invasive populations if species escape."
aquaculture["Introduction of Non-Native Species"]["Impact on Biodiversity"] = "Competition with, predation on, and displacement of native species."
aquaculture["Introduction of Non-Native Species"]["Influenced By"] = [
"Economic factors (selection of fast-growing species).",
"Lack of regulations."
]
aquaculture["Introduction of Non-Native Species"]["Influences"] = [
"Aquaculture - Escaped Fish",
"Native species."
]
aquaculture["Introduction of Non-Native Species"]["Logic Description"] = "The use of non-native species in aquaculture carries the risk of escapes and establishment of invasive populations."
aquaculture["Introduction of Non-Native Species"]["Impact Function"] = "impact_introduction_non_native_species_aquaculture"

aquaculture["Feed Sourcing"]["Metric"] = "Source and sustainability of fish feed ingredients (e.g., fishmeal, soy); amount of feed used per unit of production."
aquaculture["Feed Sourcing"]["Data Sources"] = [
"Aquaculture industry reports.",
"Research studies.",
"Life cycle assessments (LCAs)."
]
aquaculture["Feed Sourcing"]["Impact on Area"] = "Indirect, through impacts on wild fish populations and other ecosystems."
aquaculture["Feed Sourcing"]["Impact on Biodiversity"] = "Overfishing of \"forage fish\" (small pelagic fish used to make fishmeal and fish oil) can impact marine food webs.; Deforestation and habitat conversion for soy production (if soy is used in feed)."
aquaculture["Feed Sourcing"]["Influenced By"] = [
"Aquaculture - Demand for Fish Feed",
"Aquaculture - Feed Formulation Practices",
"Aquaculture - Availability and Cost of Sustainable Feed Ingredients"
]
aquaculture["Feed Sourcing"]["Influences"] = [
"Overfishing",
"Deforestation"
]
aquaculture["Feed Sourcing"]["Logic Description"] = "The production of feed for aquaculture can have significant environmental impacts, particularly if it relies on unsustainable sources of fishmeal/oil or soy."
aquaculture["Feed Sourcing"]["Impact Function"] = "impact_feed_sourcing_aquaculture"

aquaculture["Genetic Impacts"]["Metric"] = "Genetic diversity of farmed and wild populations."
aquaculture["Genetic Impacts"]["Data Sources"] = [
"Genetic Studies"
]
aquaculture["Genetic Impacts"]["Impact on Area"] = "N/A"
aquaculture["Genetic Impacts"]["Impact on Biodiversity"] = "Reduced genetic diversity in wild if interbreeding."
aquaculture["Genetic Impacts"]["Influenced By"] = [
"Aquaculture - Escaped Fish",
"Breeding Programs."
]
aquaculture["Genetic Impacts"]["Influences"] = [
"Wild Fish populations"
]
aquaculture["Genetic Impacts"]["Logic Description"] = "The genetics of farmed fish can impact wild populations if escapes and interbreeding occur."
aquaculture["Genetic Impacts"]["Impact Function"] = "impact_genetic_impacts_aquaculture"

# --- Intensive Croplands ---
intensive_croplands = all_stressors_data["Intensive Croplands"]

intensive_croplands["Land-Use Change"]["Metric"] = "Area of natural ecosystems converted to croplands (ha/year)."
intensive_croplands["Land-Use Change"]["Data Sources"] = [
"Remote sensing data (satellite imagery).",
"Agricultural statistics (from national governments and international organizations like FAO).",
"Land-use/land-cover maps."
]
intensive_croplands["Land-Use Change"]["Impact on Area"] = "Direct loss of natural habitats (forests, grasslands, wetlands).  This is a *historical* driver, and ongoing in some regions."
intensive_croplands["Land-Use Change"]["Impact on Biodiversity"] = "Significant loss of biodiversity due to habitat conversion.  Croplands support far fewer species than natural ecosystems."
intensive_croplands["Land-Use Change"]["Influenced By"] = [
"Intensive Croplands - Agricultural Expansion"
]
intensive_croplands["Land-Use Change"]["Influences"] = [
"Habitat Loss" # Generic influence
]
intensive_croplands["Land-Use Change"]["Logic Description"] = "The conversion of natural ecosystems to intensive croplands is a major driver of habitat loss and biodiversity decline globally."
intensive_croplands["Land-Use Change"]["Impact Function"] = "impact_land_use_change_intensive_croplands"

intensive_croplands["Soil Degradation"]["Metric"] = "Soil organic matter content (%); soil erosion rate (tonnes/ha/year); nutrient depletion (N, P, K levels); soil compaction; salinization (in irrigated areas)."
intensive_croplands["Soil Degradation"]["Data Sources"] = [
"Soil surveys.",
"Research studies.",
"Agricultural extension publications."
]
intensive_croplands["Soil Degradation"]["Impact on Area"] = "Reduced soil fertility and productivity; increased need for fertilizers; potential for land abandonment in severe cases."
intensive_croplands["Soil Degradation"]["Impact on Biodiversity"] = "Loss of soil biodiversity (microorganisms, invertebrates); reduced habitat quality for soil-dwelling organisms."
intensive_croplands["Soil Degradation"]["Influenced By"] = [
"Intensive Croplands - Intensive Tillage",
"Intensive Croplands - Monoculture Cropping",
"Intensive Croplands - Overuse of Fertilizers and Pesticides",
"Intensive Croplands - Removal of Crop Residues",
"Intensive Croplands - Lack of Cover Crops",
"Intensive Croplands - Soil Erosion"
]
intensive_croplands["Soil Degradation"]["Influences"] = [
"Intensive Croplands - Water Pollution",
"Intensive Croplands - Crop Yields",
"Intensive Croplands - Fertilizer Use"
]
intensive_croplands["Soil Degradation"]["Logic Description"] = "Intensive agricultural practices can lead to soil degradation through erosion, nutrient depletion, compaction, loss of organic matter, and salinization (in irrigated areas)."
intensive_croplands["Soil Degradation"]["Impact Function"] = "impact_soil_degradation_intensive_croplands"

intensive_croplands["Water Pollution"]["Metric"] = "Concentrations of nutrients (nitrogen, phosphorus), pesticides, and sediment in water bodies near agricultural areas."
intensive_croplands["Water Pollution"]["Data Sources"] = [
"Water quality monitoring programs.",
"Research studies.",
"Government environmental agencies."
]
intensive_croplands["Water Pollution"]["Impact on Area"] = "Contamination of surface water and groundwater."
intensive_croplands["Water Pollution"]["Impact on Biodiversity"] = "Eutrophication of aquatic ecosystems; toxic effects of pesticides on aquatic life; impacts on human health (through drinking water contamination)."
intensive_croplands["Water Pollution"]["Influenced By"] = [
"Intensive Croplands - Agricultural Runoff",
"Intensive Croplands - Overuse of Fertilizers and Pesticides",
"Intensive Croplands - Soil Erosion",
"Intensive Croplands - Irrigation Practices"
]
intensive_croplands["Water Pollution"]["Influences"] = [
"Aquatic Ecosystems - Eutrophication",
"Aquatic Ecosystems - Pollution",
"Human Health"
]
intensive_croplands["Water Pollution"]["Logic Description"] = "Agricultural runoff from intensive croplands is a major source of water pollution, carrying excess nutrients, pesticides, and sediment into rivers, lakes, and coastal waters."
intensive_croplands["Water Pollution"]["Impact Function"] = "impact_water_pollution_intensive_croplands"

intensive_croplands["Pesticide Use"]["Metric"] = "Amount and type of pesticides applied (kg/ha/year); concentrations of pesticides in soil, water, and biota."
intensive_croplands["Pesticide Use"]["Data Sources"] = [
"Agricultural statistics.",
"Pesticide sales data.",
"Environmental monitoring programs.",
"Research studies."
]
intensive_croplands["Pesticide Use"]["Impact on Area"] = "Contamination of soil, water, and air."
intensive_croplands["Pesticide Use"]["Impact on Biodiversity"] = "Non-target effects: Pesticides can harm beneficial insects (pollinators, natural enemies of pests), birds, mammals, and aquatic organisms.; Development of pesticide resistance in pest populations.; Disruption of food webs."
intensive_croplands["Pesticide Use"]["Influenced By"] = [
"Intensive Croplands - Pest Management Practices",
"Intensive Croplands - Monoculture Cropping",
"Government Regulations"
]
intensive_croplands["Pesticide Use"]["Influences"] = [
"Intensive Croplands - Water Pollution",
"Intensive Croplands - Soil Contamination",
"Pollinator Decline",
"Non-Target Species Mortality"
]
intensive_croplands["Pesticide Use"]["Logic Description"] = "Intensive pesticide use in croplands can contaminate soil and water, harm non-target species, and lead to the development of pesticide resistance in pests."
intensive_croplands["Pesticide Use"]["Impact Function"] = "impact_pesticide_use_intensive_croplands"

intensive_croplands["Habitat Loss"]["Impact Function"] = "impact_habitat_loss_intensive_croplands"
intensive_croplands["Genetic Homogeneity"]["Impact Function"] = "impact_genetic_homogeneity_intensive_croplands"
intensive_croplands["Climate Change"]["Impact Function"] = "impact_climate_change_intensive_croplands"
intensive_croplands["Water Use"]["Impact Function"] = "impact_water_use_intensive_croplands"
intensive_croplands["Energy Use"]["Impact Function"] = "impact_energy_use_intensive_croplands"
intensive_croplands["Soil Erosion"]["Impact Function"] = "impact_soil_erosion_intensive_croplands"
intensive_croplands["Agricultural Expansion"]["Impact Function"] = "impact_agricultural_expansion_intensive_croplands"

# The following are *components* of other stressors, not independent stressors.  They
# should be integrated into the relevant stressor above (e.g., "Intensive Tillage"
# is part of "Soil Degradation"). I'm leaving them here, but commented out, so
# you can see how to integrate them.

# intensive_croplands["Intensive Tillage"] = {} # Part of Soil Degradation
# intensive_croplands["Monoculture Cropping"] = {} # Part of Soil Degradation, Genetic Homogeneity, Pest/Disease Outbreaks
# intensive_croplands["Overuse of Fertilizers and Pesticides"] = {} # Part of Water Pollution, Soil Degradation, Pesticide Use
# intensive_croplands["Removal of Crop Residues"] = {} # Part of Soil Degradation
# intensive_croplands["Lack of Cover Crops"] = {} # Part of Soil Degradation, Soil Erosion
# intensive_croplands["Irrigation Practices"] = {} # Part of Water Use, Water Pollution
# intensive_croplands["Pest and Disease Outbreaks"] = {} # Influenced by Genetic Homogeneity, Monoculture, Climate Change
# intensive_croplands["Soil Contamination"] = {} # Part of Pollution, Soil Degradation
# intensive_croplands["Loss of Soil Fertility"] = {} # Consequence of Soil Degradation
# intensive_croplands["Farming Practices"] = {} # Too general - break down into specific practices

# --- Pastoral Lands ---
pastoral_lands = all_stressors_data["Pastoral Lands"]

pastoral_lands["Overgrazing"]["Metric"] = "Livestock density (animals per unit area); vegetation cover and composition; soil erosion rates; presence of indicator species (e.g., unpalatable plants)."
pastoral_lands["Overgrazing"]["Data Sources"] = [
"Livestock censuses.",
"Rangeland health assessments.",
"Vegetation surveys.",
"Remote sensing data.",
"Research publications."
]
pastoral_lands["Overgrazing"]["Impact on Area"] = "Reduced vegetation cover; increased soil erosion; changes in plant species composition (shift towards less palatable or more grazing-tolerant species); land degradation; desertification (in extreme cases)."
pastoral_lands["Overgrazing"]["Impact on Biodiversity"] = "Loss of palatable plant species; decline of native herbivores that compete with livestock; impacts on soil organisms; habitat degradation for wildlife."
pastoral_lands["Overgrazing"]["Influenced By"] = [
"Pastoral Lands - Stocking Rates",
"Pastoral Lands - Grazing Management Practices",
"Pastoral Lands - Climate Variability",
"Pastoral Lands - Land Tenure and Access Rights",
"Pastoral Lands - Socioeconomic Factors"
]
pastoral_lands["Overgrazing"]["Influences"] = [
"Pastoral Lands - Soil Degradation",
"Pastoral Lands - Desertification",
"Pastoral Lands - Water Quality",
"Pastoral Lands - Invasive Species"
]
pastoral_lands["Overgrazing"]["Logic Description"] = "Overgrazing occurs when the number of livestock (or other herbivores) exceeds the carrying capacity of the land, leading to a decline in vegetation cover, soil degradation, and negative impacts on biodiversity."
pastoral_lands["Overgrazing"]["Impact Function"] = "impact_overgrazing_pastoral_lands"

pastoral_lands["Climate Change"]["Metric"] = "Changes in temperature, precipitation, and the frequency/intensity of extreme weather events (e.g., droughts, floods)."
pastoral_lands["Climate Change"]["Data Sources"] = [
"Climate models.",
"Historical weather records.",
"Research publications."
]
pastoral_lands["Climate Change"]["Impact on Area"] = "Changes in growing conditions; increased aridity in some regions; increased risk of desertification; altered water availability."
pastoral_lands["Climate Change"]["Impact on Biodiversity"] = "Shifts in species distributions; increased stress on plants and animals; increased vulnerability to other stressors (e.g., overgrazing, invasive species)."
pastoral_lands["Climate Change"]["Influenced By"] = [
"Global Greenhouse Gas Emissions"
]
pastoral_lands["Climate Change"]["Influences"] = [
"Pastoral Lands - Water Availability",
"Pastoral Lands - Forage Production",
"Pastoral Lands - Desertification",
"Pastoral Lands - Wildfires"
]
pastoral_lands["Climate Change"]["Logic Description"] = "Climate change is altering temperature and precipitation patterns, impacting water availability, forage production, and the overall sustainability of pastoral systems. Increased frequency and severity of droughts are a particular concern."
pastoral_lands["Climate Change"]["Impact Function"] = "impact_climate_change_pastoral_lands"

pastoral_lands["Land Use Change"]["Metric"] = "Area of pastoral land converted to other uses (e.g., cropland, settlements, infrastructure); fragmentation of grazing lands."
pastoral_lands["Land Use Change"]["Data Sources"] = [
"Remote sensing data.",
"Land-use planning records.",
"Government statistics.",
"Research publications."
]
pastoral_lands["Land Use Change"]["Impact on Area"] = "Reduction in the area available for grazing; increased pressure on remaining grazing lands."
pastoral_lands["Land Use Change"]["Impact on Biodiversity"] = "Habitat loss and fragmentation; disruption of wildlife migration routes; increased human-wildlife conflict."
pastoral_lands["Land Use Change"]["Influenced By"] = [
"Agricultural Expansion",
"Population Growth",
"Urbanization",
"Infrastructure Development",
"Government Policies"
]
pastoral_lands["Land Use Change"]["Influences"] = [
"Pastoral Lands - Habitat Fragmentation",
"Pastoral Lands - Overgrazing (by concentrating livestock)"
]
pastoral_lands["Land Use Change"]["Logic Description"] = "Conversion of pastoral lands to other uses, such as agriculture, settlements, and infrastructure, reduces the area available for grazing and fragments habitats."
pastoral_lands["Land Use Change"]["Impact Function"] = "impact_land_use_change_pastoral_lands"

pastoral_lands["Soil Degradation"]["Metric"] = "Soil organic matter content; soil erosion rate; nutrient depletion; soil compaction; salinization (in some areas)."
pastoral_lands["Soil Degradation"]["Data Sources"] = [
"Soil surveys.",
"Research publications.",
"Remote sensing data."
]
pastoral_lands["Soil Degradation"]["Impact on Area"] = "Reduced soil fertility and productivity; reduced water infiltration; increased runoff; desertification (in severe cases)."
pastoral_lands["Soil Degradation"]["Impact on Biodiversity"] = "Loss of soil biodiversity; reduced habitat quality for plants and animals; impacts on water quality."
pastoral_lands["Soil Degradation"]["Influenced By"] = [
"Pastoral Lands - Overgrazing",
"Pastoral Lands - Climate Change",
"Poor Land Management Practices"
]
pastoral_lands["Soil Degradation"]["Influences"] = [
"Pastoral Lands - Desertification",
"Pastoral Lands - Forage Production",
"Pastoral Lands - Water Quality"
]
pastoral_lands["Soil Degradation"]["Logic Description"] = "Soil degradation, often caused by overgrazing and unsustainable land management practices, reduces the productivity of pastoral lands and contributes to desertification."
pastoral_lands["Soil Degradation"]["Impact Function"] = "impact_soil_degradation_pastoral_lands"

pastoral_lands["Water Availability"]["Metric"] = "Rainfall amount and distribution; access to water sources (wells, rivers, ponds); groundwater levels."
pastoral_lands["Water Availability"]["Data Sources"] = [
"Weather data.",
"Hydrological data.",
"Groundwater monitoring data.",
"Research publications."
]
pastoral_lands["Water Availability"]["Impact on Area"] = "Affects forage production and livestock carrying capacity; influences grazing patterns."
pastoral_lands["Water Availability"]["Impact on Biodiversity"] = "Impacts both plants and animals; water stress can lead to mortality and changes in species distributions; competition for water resources."
pastoral_lands["Water Availability"]["Influenced By"] = [
"Pastoral Lands - Climate Change",
"Pastoral Lands - Water Extraction",
"Land Degradation (reduced infiltration)"
]
pastoral_lands["Water Availability"]["Influences"] = [
"Pastoral Lands - Forage Production",
"Livestock and Wildlife Survival",
"Pastoral Livelihoods"
]
pastoral_lands["Water Availability"]["Logic Description"] = "Water availability is a critical limiting factor in pastoral systems, influencing forage production, livestock and wildlife survival, and human livelihoods."
pastoral_lands["Water Availability"]["Impact Function"] = "impact_water_availability_pastoral_lands"

pastoral_lands["Invasive Species"]["Metric"] = "Abundance and distribution of invasive plant species (e.g., certain grasses, shrubs, trees)."
pastoral_lands["Invasive Species"]["Data Sources"] = [
"Vegetation surveys.",
"Remote sensing data.",
"Research publications."
]
pastoral_lands["Invasive Species"]["Impact on Area"] = "Changes in vegetation composition and structure; reduced forage quality; altered fire regimes (in some cases)."
pastoral_lands["Invasive Species"]["Impact on Biodiversity"] = "Competition with native plants; reduced habitat quality for native herbivores; altered ecosystem processes."
pastoral_lands["Invasive Species"]["Influenced By"] = [
"Pastoral Lands - Overgrazing",
"Disturbance",
"Climate Change",
"Introduction through human activities"
]
pastoral_lands["Invasive Species"]["Influences"] = [
"Pastoral Lands - Forage Production",
"Pastoral Lands - Fire Regimes",
"Native Plant Communities"
]
pastoral_lands["Invasive Species"]["Logic Description"] = "Invasive plant species can outcompete native forage species, reduce the carrying capacity of pastoral lands, and alter ecosystem processes."
pastoral_lands["Invasive Species"]["Impact Function"] = "impact_invasive_species_pastoral_lands"

pastoral_lands["Socioeconomic Factors"]["Metric"] = "Poverty levels; access to markets; access to education and healthcare; land tenure security; conflict."
pastoral_lands["Socioeconomic Factors"]["Data Sources"] = [
"Socioeconomic surveys.",
"Government statistics.",
"Research publications."
]
pastoral_lands["Socioeconomic Factors"]["Impact on Area"] = "Influences land management practices and resource use patterns."
pastoral_lands["Socioeconomic Factors"]["Impact on Biodiversity"] = "Indirect; can contribute to overgrazing, unsustainable resource use, and human-wildlife conflict."
pastoral_lands["Socioeconomic Factors"]["Influenced By"] = [
"Many complex factors."
]
pastoral_lands["Socioeconomic Factors"]["Influences"] = [
"Pastoral Lands - Overgrazing",
"Pastoral Lands - Land-Use Change",
"Pastoral Lands - Resource Use"
]
pastoral_lands["Socioeconomic Factors"]["Logic Description"] = "Socioeconomic factors, such as poverty, market access, and land tenure security, can significantly influence how pastoralists manage their land and resources, with consequences for the environment."
pastoral_lands["Socioeconomic Factors"]["Impact Function"] = "impact_socioeconomic_factors_pastoral_lands"

pastoral_lands["Stocking Rates"]["Impact Function"] = "impact_stocking_rates_pastoral_lands"
pastoral_lands["Grazing Management Practices"]["Impact Function"] = "impact_grazing_management_practices_pastoral_lands"
pastoral_lands["Climate Variability"]["Impact Function"] = "impact_climate_variability_pastoral_lands"
pastoral_lands["Land Tenure and Access Rights"]["Impact Function"] = "impact_land_tenure_access_rights_pastoral_lands"
pastoral_lands["Desertification"]["Impact Function"] = "impact_desertification_pastoral_lands"
pastoral_lands["Water Quality"]["Impact Function"] = "impact_water_quality_pastoral_lands"
pastoral_lands["Wildfires"]["Impact Function"] = "impact_wildfires_pastoral_lands"
pastoral_lands["Forage Production"]["Impact Function"] = "impact_forage_production_pastoral_lands"
pastoral_lands["Vegetation Changes"]["Impact Function"] = "impact_vegetation_changes_pastoral_lands"

# --- Plantations ---
plantations = all_stressors_data["Plantations"]

plantations["Monoculture"]["Metric"] = "Area planted with a single species (ha); lack of genetic diversity within the planted species; tree species composition (if relevant)."
plantations["Monoculture"]["Data Sources"] = [
"Plantation inventories (if available).",
"Remote sensing data.",
"Research publications.",
"Industry reports."
]
plantations["Monoculture"]["Impact on Area"] = "Creates a highly simplified, homogenous ecosystem."
plantations["Monoculture"]["Impact on Biodiversity"] = "Very low biodiversity compared to natural forests or diverse agroforestry systems. Provides limited habitat for most native species. Increased vulnerability to pests and diseases."
plantations["Monoculture"]["Influenced By"] = [
"Economic Factors: Efficiency of management and harvesting.",
"Demand for Specific Products: (e.g., pulpwood, palm oil, rubber, timber).",
"Government Policies (e.g., subsidies for certain crops)."
]
plantations["Monoculture"]["Influences"] = [
"Plantations - Pest and Disease Outbreaks",
"Plantations - Soil Degradation (in some cases)"
]
plantations["Monoculture"]["Logic Description"] = "Monoculture plantations, by definition, lack biodiversity.  This makes them highly vulnerable to pests and diseases and provides limited habitat for native wildlife."
plantations["Monoculture"]["Impact Function"] = "impact_monoculture_plantations"

plantations["Land Conversion"]["Metric"] = "Area of natural forest or other ecosystems converted to plantations (ha/year)."
plantations["Land Conversion"]["Data Sources"] = [
"Remote sensing data.",
"Land-use change data.",
"Government statistics.",
"NGO reports (e.g., for oil palm in Southeast Asia).",
"Forestry company reports"
]
plantations["Land Conversion"]["Impact on Area"] = "Loss of natural habitats (e.g., rainforests, peatlands, grasslands)."
plantations["Land Conversion"]["Impact on Biodiversity"] = "Major loss of biodiversity due to habitat destruction; fragmentation of remaining natural habitats."
plantations["Land Conversion"]["Influenced By"] = [
"Demand for Plantation Products (e.g., pulpwood, palm oil, rubber, timber).",
"Economic Factors: Profitability of plantation crops.",
"Government Policies: Land-use planning, subsidies.",
"Land Availability"
]
plantations["Land Conversion"]["Influences"] = [
"Habitat Loss (the primary impact).",
"Deforestation (if forests are cleared).",
"Peatland Degradation (if plantations are established on peatlands)."
]
plantations["Land Conversion"]["Logic Description"] = "The establishment of plantations often involves clearing natural forests or other valuable ecosystems, leading to significant biodiversity loss and habitat fragmentation. This is a major concern in many tropical regions."
plantations["Land Conversion"]["Impact Function"] = "impact_land_conversion_plantations"

plantations["Pesticide Use"]["Metric"] = "Amount of pesticides applied (kg/ha/year); types of pesticides used; concentrations of pesticides in soil, water, and biota."
plantations["Pesticide Use"]["Data Sources"] = [
"Agricultural statistics (often limited).",
"Company reports (some companies disclose pesticide use).",
"Research studies.",
"Water quality monitoring data."
]
plantations["Pesticide Use"]["Impact on Area"] = "Contamination of soil and water."
plantations["Pesticide Use"]["Impact on Biodiversity"] = "Non-target effects: Pesticides can harm beneficial insects, birds, amphibians, and other wildlife.; Development of pesticide resistance in pest populations.; Water pollution, impacting aquatic ecosystems."
plantations["Pesticide Use"]["Influenced By"] = [
"Plantations - Pest Management Practices",
"Plantations - Monoculture",
"Government Regulations"
]
plantations["Pesticide Use"]["Influences"] = [
"Plantations - Water Pollution",
"Plantations - Soil Contamination",
"Non-Target Species Mortality"
]
plantations["Pesticide Use"]["Logic Description"] = "Intensive pesticide use in plantations can contaminate soil and water, harming non-target species and potentially leading to the development of pesticide resistance."
plantations["Pesticide Use"]["Impact Function"] = "impact_pesticide_use_plantations"

plantations["Fertilizer Use"]["Metric"] = "Amount of fertilizers applied (kg/ha/year); types of fertilizers used; nutrient concentrations in soil and water."
plantations["Fertilizer Use"]["Data Sources"] = [
"Agricultural statistics (often limited).",
"Company reports (some companies disclose fertilizer use).",
"Research studies.",
"Water quality monitoring data."
]
plantations["Fertilizer Use"]["Impact on Area"] = "Soil and water pollution; eutrophication of waterways."
plantations["Fertilizer Use"]["Impact on Biodiversity"] = "Nutrient runoff can lead to algal blooms and oxygen depletion in aquatic ecosystems; changes in soil nutrient balance can impact plant communities."
plantations["Fertilizer Use"]["Influenced By"] = [
"Plantations - Management Practices",
"Plantations - Monoculture",
"Government Policies"
]
plantations["Fertilizer Use"]["Influences"] = [
"Plantations - Water Pollution",
"Plantations - Soil Degradation (in the long term)",
"Eutrophication"
]
plantations["Fertilizer Use"]["Logic Description"] = "Intensive fertilizer use in plantations can lead to nutrient runoff, polluting waterways and causing eutrophication."
plantations["Fertilizer Use"]["Impact Function"] = "impact_fertilizer_use_plantations"

plantations["Water Use"]["Metric"] = "Volume of water used for irrigation (m³/ha/year); impacts on water availability (especially in water-scarce regions)."
plantations["Water Use"]["Data Sources"] = [
"Water usage records (where available).",
"Research studies.",
"Hydrological models."
]
plantations["Water Use"]["Impact on Area"] = "Can deplete water resources, particularly groundwater."
plantations["Water Use"]["Impact on Biodiversity"] = "Impacts on aquatic ecosystems if water is diverted from rivers or groundwater is depleted."
plantations["Water Use"]["Influenced By"] = [
"Plantation Crop Type (some require more water than others).",
"Climate",
"Irrigation Practices"
]
plantations["Water Use"]["Influences"] = [
"Water Availability"
]
plantations["Water Use"]["Logic Description"] = "Plantations, particularly those in drier regions or those growing water-intensive crops, can put significant pressure on water resources."
plantations["Water Use"]["Impact Function"] = "impact_water_use_plantations"

plantations["Soil Erosion"]["Metric"] = "Soil loss rate (tonnes/ha/year)."
plantations["Soil Erosion"]["Data Sources"] = [
"Field measurements.",
"Erosion models.",
"Remote sensing data."
]
plantations["Soil Erosion"]["Impact on Area"] = "Loss of topsoil; reduced soil fertility; sedimentation of waterways."
plantations["Soil Erosion"]["Impact on Biodiversity"] = "Impacts on soil organisms; water pollution from sediment."
plantations["Soil Erosion"]["Influenced By"] = [
"Plantations - Deforestation (removal of natural vegetation cover).",
"Plantations - Management Practices (e.g., tillage, lack of cover crops).",
"Slope and Soil Type."
]
plantations["Soil Erosion"]["Influences"] = [
"Plantations - Soil Degradation",
"Plantations - Water Pollution"
]
plantations["Soil Erosion"]["Logic Description"] = "Soil erosion can be a significant problem in plantations, particularly on slopes and where vegetation cover is removed."
plantations["Soil Erosion"]["Impact Function"] = "impact_soil_erosion_plantations"

plantations["Climate Change"]["Metric"] = "Changes in temperature, precipitation, and the frequency/intensity of extreme weather events."
plantations["Climate Change"]["Data Sources"] = [
"Climate models.",
"Historical weather data."
]
plantations["Climate Change"]["Impact on Area"] = "Changes in growing conditions; increased risk of drought, floods, and wildfires."
plantations["Climate Change"]["Impact on Biodiversity"] = "May make some areas unsuitable for certain plantation crops; increased stress on trees and crops; changes in pest and disease dynamics."
plantations["Climate Change"]["Influenced By"] = ["Global GHG"]
plantations["Climate Change"]["Influences"] = [
"Plantations - Water Availability",
"Plantations - Pest and Disease Outbreaks",
"Plantations - Wildfires"
]
plantations["Climate Change"]["Logic Description"] = "Climate change can impact plantation productivity and increase the risk of extreme events."
plantations["Climate Change"]["Impact Function"] = "impact_climate_change_plantations"

plantations["Pest and Disease Outbreaks"]["Metric"] = "Incidence and severity of pest and disease outbreaks; economic losses."
plantations["Pest and Disease Outbreaks"]["Data Sources"] = [
"Plantation monitoring data.",
"Research studies.",
"Forestry/agricultural reports."
]
plantations["Pest and Disease Outbreaks"]["Impact on Area"] = "Reduced tree/crop growth and survival; economic losses."
plantations["Pest and Disease Outbreaks"]["Impact on Biodiversity"] = "Can impact non-target species if pesticides are used extensively."
plantations["Pest and Disease Outbreaks"]["Influenced By"] = [
"Plantations - Monoculture",
"Plantations - Climate Change",
"Introduction of Exotic Species",
"Plantations - Management Practices"
]
plantations["Pest and Disease Outbreaks"]["Influences"] = [
"Plantations - Pesticide Use"
]
plantations["Pest and Disease Outbreaks"]["Logic Description"] = "Monoculture plantations are particularly vulnerable to pest and disease outbreaks due to the lack of genetic diversity and the high density of host plants/trees."
plantations["Pest and Disease Outbreaks"]["Impact Function"] = "impact_pest_and_disease_outbreaks_plantations"

plantations["Soil Degradation"]["Metric"] = "Soil organic matter content; nutrient depletion; soil compaction; salinization (in some cases)."
plantations["Soil Degradation"]["Data Sources"] = [
"Soil surveys.",
"Research studies."
]
plantations["Soil Degradation"]["Impact on Area"] = "Reduced soil fertility and productivity; increased need for fertilizers."
plantations["Soil Degradation"]["Impact on Biodiversity"] = "Impacts on soil organisms; reduced habitat quality."
plantations["Soil Degradation"]["Influenced By"] = [
"Plantations - Monoculture",
"Plantations - Intensive Harvesting",
"Plantations - Overuse of Fertilizers",
"Plantations - Soil Erosion"
]
plantations["Soil Degradation"]["Influences"] = [
"Plantations - Tree and Crop Productivity",
"Plantations - Water Pollution"
]
plantations["Soil Degradation"]["Logic Description"] = "Intensive plantation management can lead to soil degradation, reducing long-term productivity."
plantations["Soil Degradation"]["Impact Function"] = "impact_soil_degradation_plantations"

# --- Urban Ecosystems ---
urban_ecosystems = all_stressors_data["Urban Ecosystems"]

urban_ecosystems["Habitat Loss and Fragmentation"]["Metric"] = "Area of natural habitat converted to urban land use (ha/year); patch size and connectivity of remaining natural areas."
urban_ecosystems["Habitat Loss and Fragmentation"]["Data Sources"] = [
"Remote sensing data (satellite imagery).",
"Land use/land cover maps.",
"City planning data.",
"Geographic Information Systems (GIS) analysis."
]
urban_ecosystems["Habitat Loss and Fragmentation"]["Impact on Area"] = "Reduction in the amount and connectivity of natural habitat within urban areas."
urban_ecosystems["Habitat Loss and Fragmentation"]["Impact on Biodiversity"] = "Loss of species diversity.; Disruption of ecological processes.; Increased dominance of urban-adapted species.; Reduced genetic diversity within remaining populations."
urban_ecosystems["Habitat Loss and Fragmentation"]["Influenced By"] = [
"Urban Ecosystems - Urban Sprawl",
"Urban Ecosystems - Population Growth",
"Urban Ecosystems - Economic Development",
"Urban Ecosystems - Infrastructure Development"
]
urban_ecosystems["Habitat Loss and Fragmentation"]["Influences"] = [
"Exacerbates the impacts of many other stressors."
]
urban_ecosystems["Habitat Loss and Fragmentation"]["Logic Description"] = "Urban development directly replaces natural habitats with buildings, roads, and other infrastructure, leading to habitat loss and fragmentation. This is the *foundational* stressor in urban areas."
urban_ecosystems["Habitat Loss and Fragmentation"]["Impact Function"] = "impact_habitat_loss_fragmentation_urban"

urban_ecosystems["Urban Heat Island Effect"]["Metric"] = "Temperature difference between urban areas and surrounding rural areas (°C)."
urban_ecosystems["Urban Heat Island Effect"]["Data Sources"] = [
"Temperature measurements (weather stations, remote sensing).",
"Climate models."
]
urban_ecosystems["Urban Heat Island Effect"]["Impact on Area"] = "Increased temperatures in urban areas, particularly during heat waves."
urban_ecosystems["Urban Heat Island Effect"]["Impact on Biodiversity"] = "Stress on heat-sensitive species (plants and animals).; Changes in species distributions.; Increased energy consumption (for cooling).; Impacts on human health."
urban_ecosystems["Urban Heat Island Effect"]["Influenced By"] = [
"Urban Ecosystems - Loss of Vegetation",
"Urban Ecosystems - Impervious Surfaces",
"Urban Ecosystems - Anthropogenic Heat Release"
]
urban_ecosystems["Urban Heat Island Effect"]["Influences"] = [
"Local Climate",
"Energy Consumption",
"Human Health"
]
urban_ecosystems["Urban Heat Island Effect"]["Logic Description"] = "Urban areas tend to be warmer than surrounding rural areas due to the replacement of vegetation with heat-absorbing surfaces (buildings, roads) and human activities that release heat."
urban_ecosystems["Urban Heat Island Effect"]["Impact Function"] = "impact_urban_heat_island_urban"

urban_ecosystems["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., air pollutants, water pollutants, noise, light) in air, water, and soil."
urban_ecosystems["Pollution"]["Data Sources"] = [
"Air and water quality monitoring data.",
"Noise level measurements.",
"Light pollution maps.",
"Research studies."
]
urban_ecosystems["Pollution"]["Impact on Area"] = "Degradation of air, water, and soil quality."
urban_ecosystems["Pollution"]["Impact on Biodiversity"] = "Toxic effects on wildlife and plants.; Disruption of behavior (e.g., due to noise and light).; Impacts on human health."
urban_ecosystems["Pollution"]["Influenced By"] = [
"Urban Ecosystems - Industrial Activity",
"Urban Ecosystems - Transportation",
"Urban Ecosystems - Waste Disposal",
"Urban Ecosystems - Construction"
]
urban_ecosystems["Pollution"]["Influences"] = [
"Urban Ecosystems - Water Quality",
"Urban Ecosystems - Air Quality",
"Urban Ecosystems - Wildlife Health"
]
urban_ecosystems["Pollution"]["Logic Description"] = "Urban areas are sources of various pollutants that can degrade environmental quality and impact both wildlife and human health."
urban_ecosystems["Pollution"]["Impact Function"] = "impact_pollution_urban"

urban_ecosystems["Altered Hydrology"]["Metric"] = "Impervious surface area (%); stormwater runoff volume; streamflow patterns."
urban_ecosystems["Altered Hydrology"]["Data Sources"] = [
"Hydrological models.",
"Streamflow measurements.",
"Impervious surface maps."
]
urban_ecosystems["Altered Hydrology"]["Impact on Area"] = "Increased stormwater runoff; reduced groundwater recharge; altered streamflow."
urban_ecosystems["Altered Hydrology"]["Impact on Biodiversity"] = "Erosion and sedimentation in streams; flooding; impacts on aquatic ecosystems."
urban_ecosystems["Altered Hydrology"]["Influenced By"] = [
"Urban Ecosystems - Impervious Surfaces",
"Urban Ecosystems - Urban Sprawl",
"Urban Ecosystems - Stormwater Management Practices"
]
urban_ecosystems["Altered Hydrology"]["Influences"] = [
"Urban Ecosystems - Water Quality",
"Urban Ecosystems - Flooding"
]
urban_ecosystems["Altered Hydrology"]["Logic Description"] = "Urban development increases impervious surfaces, leading to altered hydrology, increased runoff, and impacts on aquatic ecosystems."
urban_ecosystems["Altered Hydrology"]["Impact Function"] = "impact_altered_hydrology_urban"

urban_ecosystems["Invasive Species"]["Metric"] = "Abundance and distribution of invasive plant and animal species."
urban_ecosystems["Invasive Species"]["Data Sources"] = [
"Urban biodiversity surveys",
"Research studies."
]
urban_ecosystems["Invasive Species"]["Impact on Area"] = "Changes in vegetation composition; impacts on urban green spaces."
urban_ecosystems["Invasive Species"]["Impact on Biodiversity"] = "Competition with native species; predation on native species; alteration of habitat structure."
urban_ecosystems["Invasive Species"]["Influenced By"] = [
"Urban Ecosystems - Introduction (intentional and accidental).",
"Urban Ecosystems - Disturbance",
"Climate Change"
]
urban_ecosystems["Invasive Species"]["Influences"] = [
"Native species"
]
urban_ecosystems["Invasive Species"]["Logic Description"] = "Invasive species can thrive in urban environments, outcompeting native species and altering ecosystems."
urban_ecosystems["Invasive Species"]["Impact Function"] = "impact_invasive_species_urban"
urban_ecosystems["Urban Sprawl"]["Metric"] = "Rate of urban expansion (ha/year); loss of natural habitat at the urban fringe."
urban_ecosystems["Urban Sprawl"]["Data Sources"] = [
"Remote sensing data (satellite imagery).",
"Land-use change data.",
"City planning records."
]
urban_ecosystems["Urban Sprawl"]["Impact on Area"] = "Conversion of natural habitats and agricultural land to urban land uses."
urban_ecosystems["Urban Sprawl"]["Impact on Biodiversity"] = "Habitat loss and fragmentation; increased pressure on remaining natural areas."
urban_ecosystems["Urban Sprawl"]["Influenced By"] = [
"Urban Ecosystems - Population Growth",
"Urban Ecosystems - Economic Development",
"Transportation Infrastructure",
"Land-Use Policies"
]
urban_ecosystems["Urban Sprawl"]["Influences"] = [
"Urban Ecosystems - Habitat Loss and Fragmentation",
"Increased resource consumption"
]
urban_ecosystems["Urban Sprawl"]["Logic Description"] = "Urban sprawl, the outward expansion of urban areas, is a major driver of habitat loss and fragmentation."
urban_ecosystems["Urban Sprawl"]["Impact Function"] = "impact_urban_sprawl_urban"

urban_ecosystems["Population Growth"]["Metric"] = "Population size and density within urban areas; rate of population growth."
urban_ecosystems["Population Growth"]["Data Sources"] = [
"Census data.",
"Demographic projections."
]
urban_ecosystems["Population Growth"]["Impact on Area"] = "Increased demand for housing, infrastructure, and resources."
urban_ecosystems["Population Growth"]["Impact on Biodiversity"] = "Indirect; increased pressure on natural resources and ecosystems."
urban_ecosystems["Population Growth"]["Influenced By"] = [
"Economic Opportunities",
"Migration Patterns",
"Social Factors"
]
urban_ecosystems["Population Growth"]["Influences"] = [
"Urban Ecosystems - Urban Sprawl",
"Urban Ecosystems - Resource Consumption",
"Urban Ecosystems - Pollution"
]
urban_ecosystems["Population Growth"]["Logic Description"] = "Population growth in urban areas increases the demand for resources and puts pressure on surrounding ecosystems."
urban_ecosystems["Population Growth"]["Impact Function"] = "impact_population_growth_urban"

urban_ecosystems["Economic Development"]["Metric"] = "Economic growth rate; types of economic activities; industrial development."
urban_ecosystems["Economic Development"]["Data Sources"] = [
"Economic data (GDP, employment, etc.).",
"Business and industry reports."
]
urban_ecosystems["Economic Development"]["Impact on Area"] = "Variable; can lead to increased development pressure, but can also drive investment in green infrastructure."
urban_ecosystems["Economic Development"]["Impact on Biodiversity"] = "Variable; depends on the type of development and the environmental regulations in place."
urban_ecosystems["Economic Development"]["Influenced By"] = [
"Many factors (global, national, and local)"
]
urban_ecosystems["Economic Development"]["Influences"] = [
"Urban Ecosystems - Land-Use Change",
"Urban Ecosystems - Infrastructure Development",
"Urban Ecosystems - Pollution"
]
urban_ecosystems["Economic Development"]["Logic Description"] = "Economic development can drive urban expansion and increase pressure on natural resources, but can also provide opportunities for sustainable solutions."
urban_ecosystems["Economic Development"]["Impact Function"] = "impact_economic_development_urban"

urban_ecosystems["Infrastructure Development"]["Metric"] = "Road density (km/km²); building density; area covered by impervious surfaces; water and energy infrastructure."
urban_ecosystems["Infrastructure Development"]["Data Sources"] = [
"City planning data.",
"Transportation data.",
"Remote sensing data."
]
urban_ecosystems["Infrastructure Development"]["Impact on Area"] = "Habitat fragmentation; increased impervious surfaces; altered hydrology."
urban_ecosystems["Infrastructure Development"]["Impact on Biodiversity"] = "Habitat loss; disruption of ecological corridors; impacts on aquatic ecosystems due to altered runoff patterns."
urban_ecosystems["Infrastructure Development"]["Influenced By"] = [
"Urban Ecosystems - Population Growth",
"Urban Ecosystems - Economic Development",
"Urban Ecosystems - Urban Sprawl",
"Government Policies"
]
urban_ecosystems["Infrastructure Development"]["Influences"] = [
"Urban Ecosystems - Habitat Loss and Fragmentation",
"Urban Ecosystems - Altered Hydrology",
"Urban Ecosystems - Urban Heat Island Effect"
]
urban_ecosystems["Infrastructure Development"]["Logic Description"] = "Infrastructure development, particularly roads and buildings, fragments habitats, increases impervious surfaces, and alters hydrology."
urban_ecosystems["Infrastructure Development"]["Impact Function"] = "impact_infrastructure_development_urban"

urban_ecosystems["Loss of Vegetation"]["Metric"] = "Tree canopy cover (%); area of green space (ha); vegetation biomass."
urban_ecosystems["Loss of Vegetation"]["Data Sources"] = [
"Remote sensing data.",
"City green space inventories.",
"Research studies."
]
urban_ecosystems["Loss of Vegetation"]["Impact on Area"] = "Reduced urban green space; increased urban heat island effect; reduced air quality; reduced carbon sequestration."
urban_ecosystems["Loss of Vegetation"]["Impact on Biodiversity"] = "Loss of habitat for urban wildlife; reduced connectivity between green spaces."
urban_ecosystems["Loss of Vegetation"]["Influenced By"] = [
"Urban Ecosystems - Urban Sprawl",
"Urban Ecosystems - Infrastructure Development"
]
urban_ecosystems["Loss of Vegetation"]["Influences"] = [
"Urban Ecosystems - Urban Heat Island Effect",
"Urban Ecosystems - Air Quality",
"Urban Ecosystems - Habitat Availability"
]
urban_ecosystems["Loss of Vegetation"]["Logic Description"] = "Loss of vegetation cover in urban areas reduces ecosystem services, such as cooling, air purification, and carbon sequestration, and impacts biodiversity."
urban_ecosystems["Loss of Vegetation"]["Impact Function"] = "impact_loss_of_vegetation_urban"

urban_ecosystems["Impervious Surfaces"]["Metric"] = "Percentage of land area covered by impervious surfaces (roads, buildings, parking lots)."
urban_ecosystems["Impervious Surfaces"]["Data Sources"] = [
"Remote sensing data.",
"GIS analysis.",
"Land cover data."
]
urban_ecosystems["Impervious Surfaces"]["Impact on Area"] = "Increased surface runoff; reduced groundwater recharge; altered streamflow patterns; urban heat island effect."
urban_ecosystems["Impervious Surfaces"]["Impact on Biodiversity"] = "Impacts on aquatic ecosystems due to altered hydrology and increased pollution; contributes to the urban heat island effect."
urban_ecosystems["Impervious Surfaces"]["Influenced By"] = [
"Urban Ecosystems - Urban Sprawl",
"Urban Ecosystems - Infrastructure Development"
]
urban_ecosystems["Impervious Surfaces"]["Influences"] = [
"Urban Ecosystems - Altered Hydrology",
"Urban Ecosystems - Urban Heat Island Effect",
"Urban Ecosystems - Water Quality"
]
urban_ecosystems["Impervious Surfaces"]["Logic Description"] = "Impervious surfaces prevent water from infiltrating into the ground, leading to increased runoff, reduced groundwater recharge, and altered streamflow patterns."
urban_ecosystems["Impervious Surfaces"]["Impact Function"] = "impact_impervious_surfaces_urban"

urban_ecosystems["Anthropogenic Heat Release"]["Metric"] = "Heat released from human activities (vehicles, industry, buildings) (watts per square meter - W/m²)."
urban_ecosystems["Anthropogenic Heat Release"]["Data Sources"] = [
"Energy consumption data.",
"Traffic data.",
"Industrial activity data.",
"Research studies; models."
]
urban_ecosystems["Anthropogenic Heat Release"]["Impact on Area"] = "Contributes to the urban heat island effect."
urban_ecosystems["Anthropogenic Heat Release"]["Impact on Biodiversity"] = "Indirect, through contribution to increased temperatures."
urban_ecosystems["Anthropogenic Heat Release"]["Influenced By"] = [
"Urban Ecosystems - Energy Consumption",
"Urban Ecosystems - Transportation",
"Urban Ecosystems - Industrial Activity",
"Building Design and Materials"
]
urban_ecosystems["Anthropogenic Heat Release"]["Influences"] = [
"Urban Ecosystems - Urban Heat Island Effect"
]
urban_ecosystems["Anthropogenic Heat Release"]["Logic Description"] = "Human activities, such as transportation, industry, and building heating/cooling, release heat into the urban environment, contributing to the urban heat island effect."
urban_ecosystems["Anthropogenic Heat Release"]["Impact Function"] = "impact_anthropogenic_heat_release_urban"

urban_ecosystems["Industrial Activity"]["Metric"] = "Number and type of industrial facilities; industrial emissions; waste generation."
urban_ecosystems["Industrial Activity"]["Data Sources"] = [
"Industrial permits and licenses.",
"Emissions inventories.",
"Environmental monitoring data."
]
urban_ecosystems["Industrial Activity"]["Impact on Area"] = "Air, water, and soil pollution; habitat degradation."
urban_ecosystems["Industrial Activity"]["Impact on Biodiversity"] = "Toxic effects on wildlife and plants; habitat loss or degradation."
urban_ecosystems["Industrial Activity"]["Influenced By"] = [
"Economic Development",
"Government Regulations"
]
urban_ecosystems["Industrial Activity"]["Influences"] = [
"Urban Ecosystems - Pollution",
"Urban Ecosystems - Water Quality",
"Urban Ecosystems - Air Quality"
]
urban_ecosystems["Industrial Activity"]["Logic Description"] = "Industrial activity can be a major source of pollution in urban areas, impacting air, water, and soil quality."
urban_ecosystems["Industrial Activity"]["Impact Function"] = "impact_industrial_activity_urban"

urban_ecosystems["Transportation"]["Metric"] = "Vehicle miles traveled (VMT); vehicle emissions; road density; traffic congestion."
urban_ecosystems["Transportation"]["Data Sources"] = [
"Traffic data.",
"Vehicle emissions data.",
"Transportation planning data."
]
urban_ecosystems["Transportation"]["Impact on Area"] = "Air pollution; noise pollution; habitat fragmentation (due to roads)."
urban_ecosystems["Transportation"]["Impact on Biodiversity"] = "Impacts on wildlife from air pollution, noise, and vehicle collisions; barrier effects of roads."
urban_ecosystems["Transportation"]["Influenced By"] = [
"Urban Form",
"Transportation Infrastructure",
"Public Transportation Availability",
"Fuel Prices",
"Commuting Patterns"
]
urban_ecosystems["Transportation"]["Influences"] = [
"Urban Ecosystems - Air Quality",
"Urban Ecosystems - Noise Pollution",
"Urban Ecosystems - Habitat Fragmentation"
]
urban_ecosystems["Transportation"]["Logic Description"] = "Transportation is a major source of air and noise pollution in urban areas, and roads can fragment habitats and create barriers to wildlife movement."
urban_ecosystems["Transportation"]["Impact Function"] = "impact_transportation_urban"

urban_ecosystems["Waste Disposal"]["Metric"] = "Amount of solid waste generated; waste management practices (landfilling, incineration, recycling); presence of illegal dumping."
urban_ecosystems["Waste Disposal"]["Data Sources"] = [
"Municipal waste management data.",
"Research studies."
]
urban_ecosystems["Waste Disposal"]["Impact on Area"] = "Landfill space consumption; potential for soil and water contamination; air pollution from incineration."
urban_ecosystems["Waste Disposal"]["Impact on Biodiversity"] = "Pollution from landfills and incinerators can impact wildlife; plastic waste can harm animals."
urban_ecosystems["Waste Disposal"]["Influenced By"] = [
"Consumption Patterns",
"Waste Management Policies",
"Recycling Rates",
"Population Size"
]
urban_ecosystems["Waste Disposal"]["Influences"] = [
"Urban Ecosystems - Pollution"
]
urban_ecosystems["Waste Disposal"]["Logic Description"] = "Waste disposal practices can have significant environmental impacts, including land use, pollution, and greenhouse gas emissions."
urban_ecosystems["Waste Disposal"]["Impact Function"] = "impact_waste_disposal_urban"

urban_ecosystems["Construction"]["Metric"] = "Building activity, demolition activity; use of construction materials."
urban_ecosystems["Construction"]["Data Sources"] = [
"Building permits.",
"Construction industry data."
]
urban_ecosystems["Construction"]["Impact on Area"] = "Habitat loss; noise and air pollution; generation of construction waste."
urban_ecosystems["Construction"]["Impact on Biodiversity"] = "Disturbance to wildlife; habitat destruction."
urban_ecosystems["Construction"]["Influenced By"] = [
"Urban Ecosystems - Economic Development",
"Urban Ecosystems - Population Growth"
]
urban_ecosystems["Construction"]["Influences"] = [
"Urban Ecosystems - Pollution",
"Urban Ecosystems - Habitat Loss and Fragmentation"
]
urban_ecosystems["Construction"]["Logic Description"] = "Construction activities can cause significant environmental disturbance, including habitat loss, noise and air pollution, and waste generation."
urban_ecosystems["Construction"]["Impact Function"] = "impact_construction_urban"

# --- Abyssal Plains ---
abyssal_plains = all_stressors_data["Abyssal Plains"]

abyssal_plains["Deep-Sea Mining"]["Metric"] = "Area of seabed licensed for exploration or exploitation (km²); amount of sediment plume generated; duration and intensity of mining activity."
abyssal_plains["Deep-Sea Mining"]["Data Sources"] = [
"International Seabed Authority (ISA) data.",
"Mining company reports (often limited).",
"Research publications.",
"Environmental Impact Assessments (EIAs)."
]
abyssal_plains["Deep-Sea Mining"]["Impact on Area"] = "Physical destruction of seabed habitat; creation of sediment plumes that can spread over large areas."
abyssal_plains["Deep-Sea Mining"]["Impact on Biodiversity"] = "Loss of unique and poorly understood deep-sea species; disruption of ecosystem processes; potential long-term impacts on benthic communities."
abyssal_plains["Deep-Sea Mining"]["Influenced By"] = [
"Demand for Minerals (e.g., polymetallic nodules, seafloor massive sulfides).",
"Technological Developments",
"International Regulations (ISA).",
"Economic Feasibility"
]
abyssal_plains["Deep-Sea Mining"]["Influences"] = [
"Habitat Destruction (the primary impact).",
"Sediment Plumes",
"Potential release of toxins"
]
abyssal_plains["Deep-Sea Mining"]["Logic Description"] = "Deep-sea mining is an emerging threat to abyssal plain ecosystems, involving the physical removal of seabed resources and the creation of large sediment plumes."
abyssal_plains["Deep-Sea Mining"]["Impact Function"] = "impact_deep_sea_mining_abyssal"

abyssal_plains["Climate Change"]["Metric"] = "Changes in ocean temperature, salinity, and circulation patterns; changes in sea level."
abyssal_plains["Climate Change"]["Data Sources"] = [
"Climate models.",
"Oceanographic observations (e.g., Argo floats).",
"Research publications."
]
abyssal_plains["Climate Change"]["Impact on Area"] = "Warming of deep ocean waters (although less pronounced than at the surface); changes in ocean currents; potential impacts on nutrient supply."
abyssal_plains["Climate Change"]["Impact on Biodiversity"] = "Potential impacts on deep-sea species, many of which are adapted to very stable conditions. Changes in food supply (from the surface) could also have significant effects."
abyssal_plains["Climate Change"]["Influenced By"] = [
"Global Greenhouse Gas Emissions"
]
abyssal_plains["Climate Change"]["Influences"] = [
"Ocean Circulation",
"Food Supply to Deep Sea"
]
abyssal_plains["Climate Change"]["Logic Description"] = "Although the deep ocean is relatively buffered from rapid changes, climate change is still expected to impact abyssal plains through warming, changes in circulation, and alterations in food supply."
abyssal_plains["Climate Change"]["Impact Function"] = "impact_climate_change_abyssal"

abyssal_plains["Plastic Pollution"]["Metric"] = "Concentration of microplastics and macroplastics in sediments and water column."
abyssal_plains["Plastic Pollution"]["Data Sources"] = [
"Research surveys using trawls and sediment cores.",
"Scientific publications."
]
abyssal_plains["Plastic Pollution"]["Impact on Area"] = "Accumulation of plastic debris on the seafloor."
abyssal_plains["Plastic Pollution"]["Impact on Biodiversity"] = "Ingestion of microplastics by deep-sea organisms; entanglement in plastic debris; potential toxic effects of plastic additives."
abyssal_plains["Plastic Pollution"]["Influenced By"] = [
"Global Plastic Production and Consumption",
"Waste Management Practices",
"Ocean Currents"
]
abyssal_plains["Plastic Pollution"]["Influences"] = [
"Deep-Sea Organism Health"
]
abyssal_plains["Plastic Pollution"]["Logic Description"] = "Plastic pollution, particularly microplastics, is accumulating in even the most remote deep-sea environments, including abyssal plains."
abyssal_plains["Plastic Pollution"]["Impact Function"] = "impact_plastic_pollution_abyssal"

abyssal_plains["Sedimentation"]["Metric"] = "Changes in sedimentation rates."
abyssal_plains["Sedimentation"]["Data Sources"] = ["Sediment cores"]
abyssal_plains["Sedimentation"]["Impact on Area"] = "Burial"
abyssal_plains["Sedimentation"]["Impact on Biodiversity"] = "Smothering"
abyssal_plains["Sedimentation"]["Influenced By"] = ["Abyssal Plains - Deep-Sea Mining"]
abyssal_plains["Sedimentation"]["Influences"] = ["Benthic Communities"]
abyssal_plains["Sedimentation"]["Logic Description"] = "Changes in sedimentation."
abyssal_plains["Sedimentation"]["Impact Function"] = "impact_sedimentation_abyssal"

abyssal_plains["Ocean Acidification"]["Metric"] = "Decrease in seawater pH; changes in carbonate saturation state."
abyssal_plains["Ocean Acidification"]["Data Sources"] = [
"Oceanographic measurements.",
"Climate models.",
"Research publications."
]
abyssal_plains["Ocean Acidification"]["Impact on Area"] = "Although the deep ocean is less affected than surface waters, acidification is still occurring."
abyssal_plains["Ocean Acidification"]["Impact on Biodiversity"] = "Potential impacts on deep-sea organisms, particularly those with calcium carbonate shells or skeletons.  The effects are poorly understood."
abyssal_plains["Ocean Acidification"]["Influenced By"] = [
"Atmospheric CO2 Concentrations"
]
abyssal_plains["Ocean Acidification"]["Influences"] = [
"Calcifying Organisms"
]
abyssal_plains["Ocean Acidification"]["Logic Description"] = "Ocean acidification, caused by the absorption of excess CO2 from the atmosphere, is a long-term threat to marine ecosystems, including the deep sea."
abyssal_plains["Ocean Acidification"]["Impact Function"] = "impact_ocean_acidification_abyssal"

abyssal_plains["Bottom Trawling"]["Metric"] = "Area of seabed trawled; frequency of trawling."
abyssal_plains["Bottom Trawling"]["Data Sources"] = [
"Fishing vessel tracking data (VMS).",
"Fisheries observer data.",
"Research surveys."
]
abyssal_plains["Bottom Trawling"]["Impact on Area"] = "Physical disturbance of the seabed; destruction of benthic habitats."
abyssal_plains["Bottom Trawling"]["Impact on Biodiversity"] = "High mortality of benthic organisms (e.g., deep-sea corals, sponges, invertebrates); damage to habitat structure; long recovery times."
abyssal_plains["Bottom Trawling"]["Influenced By"] = [
"Fishing Practices",
"Demand for Seafood",
"Fisheries Management Regulations"
]
abyssal_plains["Bottom Trawling"]["Influences"] = [
"Habitat Destruction",
"Benthic Community Structure",
"Bycatch"
]
abyssal_plains["Bottom Trawling"]["Logic Description"] = "Although less frequent than on continental shelves, bottom trawling can occur on abyssal plains and has significant impacts on benthic ecosystems due to the slow recovery rates of deep-sea organisms."
abyssal_plains["Bottom Trawling"]["Impact Function"] = "impact_bottom_trawling_abyssal"

# --- Aquatic (African Great Lakes) ---
african_great_lakes = all_stressors_data["African Great Lakes"]

african_great_lakes["Overfishing"]["Metric"] = "Fish catches (tonnes/year); fishing effort (number of boats, fishing days); fish biomass and size structure; catch per unit effort (CPUE)."
african_great_lakes["Overfishing"]["Data Sources"] = [
"National fisheries statistics (Tanzania, Uganda, Kenya, Malawi, etc.).",
"Lake-specific research institutions (e.g., TAFIRI - Tanzania Fisheries Research Institute, NaFIRRI - National Fisheries Resources Research Institute (Uganda)).",
"Research publications."
]
african_great_lakes["Overfishing"]["Impact on Area"] = "Not directly applicable (affects fish populations, not lake area)."
african_great_lakes["Overfishing"]["Impact on Biodiversity"] = "Decline of fish stocks, particularly commercially important species (e.g., Nile perch, tilapia) and endemic cichlids. Changes in fish community structure. Disruption of food webs."
african_great_lakes["Overfishing"]["Influenced By"] = [
"High Fishing Pressure (due to large human populations depending on the lakes for food and livelihoods).",
"Use of Unsustainable Fishing Gear (e.g., small mesh nets).",
"Weak Enforcement of Fisheries Regulations.",
"Poverty and Lack of Alternative Livelihoods."
]
african_great_lakes["Overfishing"]["Influences"] = [
"Aquatic (African Great Lakes) - Fish Populations",
"Aquatic (African Great Lakes) - Food Web Structure"
]
african_great_lakes["Overfishing"]["Logic Description"] = "Overfishing is a *major* threat to the African Great Lakes, driven by high fishing pressure, unsustainable fishing practices, and weak governance. It leads to the decline of fish stocks and disrupts the lake ecosystems."
african_great_lakes["Overfishing"]["Impact Function"] = "impact_overfishing_african_great_lakes"

african_great_lakes["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., nutrients, pesticides, heavy metals, plastics) in water, sediments, and fish tissue."
african_great_lakes["Pollution"]["Data Sources"] = [
"Water quality monitoring programs (often limited).",
"Research studies.",
"Reports from environmental agencies."
]
african_great_lakes["Pollution"]["Impact on Area"] = "Degradation of water quality; contamination of sediments."
african_great_lakes["Pollution"]["Impact on Biodiversity"] = "Toxic effects on aquatic organisms (e.g., fish, invertebrates).; Eutrophication (nutrient enrichment) leading to algal blooms.; Impacts on human health (through consumption of contaminated fish and water)."
african_great_lakes["Pollution"]["Influenced By"] = [
"Agricultural Runoff (fertilizers, pesticides).",
"Urban Runoff (sewage, industrial effluent).",
"Industrial Discharge.",
"Mining Activities (in some areas).",
"Deforestation (increased sediment runoff)."
]
african_great_lakes["Pollution"]["Influences"] = [
"Aquatic (African Great Lakes) - Water Quality",
"Aquatic (African Great Lakes) - Wildlife Health",
"Aquatic (African Great Lakes) - Eutrophication",
"Human Health"
]
african_great_lakes["Pollution"]["Logic Description"] = "Pollution from agriculture, urban areas, industry, and mining activities degrades water quality in the African Great Lakes, impacting aquatic life and human health."
african_great_lakes["Pollution"]["Impact Function"] = "impact_pollution_african_great_lakes"

african_great_lakes["Climate Change"]["Metric"] = "Water temperature (°C); changes in precipitation (mm/year, seasonality); changes in lake levels; changes in stratification patterns."
african_great_lakes["Climate Change"]["Data Sources"] = [
"Climate models.",
"Long-term lake monitoring data (temperature, water levels).",
"Research publications."
]
african_great_lakes["Climate Change"]["Impact on Area"] = "Changes in lake thermal structure; altered water levels; changes in mixing patterns."
african_great_lakes["Climate Change"]["Impact on Biodiversity"] = "Shifts in species distributions.; Increased stress on aquatic organisms.; Changes in phenology.; Impacts on fish spawning and recruitment.; Potential for increased algal blooms."
african_great_lakes["Climate Change"]["Influenced By"] = ["Global GHG"]
african_great_lakes["Climate Change"]["Influences"] = [
"Aquatic (African Great Lakes) - Water Temperature",
"Aquatic (African Great Lakes) - Water Levels",
"Aquatic (African Great Lakes) - Lake Stratification",
"Aquatic (African Great Lakes) - Eutrophication"
]
african_great_lakes["Climate Change"]["Logic Description"] = "Climate change is warming the African Great Lakes, altering water levels, and potentially exacerbating other stressors like eutrophication."
african_great_lakes["Climate Change"]["Impact Function"] = "impact_climate_change_african_great_lakes"

african_great_lakes["Invasive Species"]["Metric"] = "Abundance and distribution of key invasive species (e.g., water hyacinth, Nile perch (in Lake Victoria))."
african_great_lakes["Invasive Species"]["Data Sources"] = [
"Lake monitoring programs.",
"Research studies."
]
african_great_lakes["Invasive Species"]["Impact on Area"] = "Changes in habitat structure (e.g., water hyacinth mats); impacts on water quality and navigation."
african_great_lakes["Invasive Species"]["Impact on Biodiversity"] = "Nile perch (Lake Victoria): Predation on native cichlids, leading to *massive* extinctions.  Water hyacinth: Forms dense mats, blocking sunlight, reducing oxygen levels, and hindering navigation and fishing."
african_great_lakes["Invasive Species"]["Influenced By"] = [
"Intentional Introductions (e.g., Nile perch).",
"Accidental Introductions (e.g., water hyacinth).",
"Altered Environmental Conditions (may favor some invasives).",
"Aquatic (African Great Lakes) - Pollution"
]
african_great_lakes["Invasive Species"]["Influences"] = [
"Aquatic (African Great Lakes) - Native Fish Populations",
"Aquatic (African Great Lakes) - Water Quality",
"Aquatic (African Great Lakes) - Ecosystem Structure"
]
african_great_lakes["Invasive Species"]["Logic Description"] = "Invasive species, such as the water hyacinth and Nile perch (in Lake Victoria), have had devastating impacts on the African Great Lakes, altering ecosystems and causing significant ecological and economic damage."
african_great_lakes["Invasive Species"]["Impact Function"] = "impact_invasive_species_african_great_lakes"

african_great_lakes["Sedimentation"]["Metric"] = "Sediment load in rivers flowing into the lakes; sedimentation rates in the lakes; turbidity."
african_great_lakes["Sedimentation"]["Data Sources"] = [
"River discharge data.",
"Sediment core analysis.",
"Remote sensing data.",
"Research studies."
]
african_great_lakes["Sedimentation"]["Impact on Area"] = "Reduced water clarity; smothering of benthic habitats; infilling of lake areas."
african_great_lakes["Sedimentation"]["Impact on Biodiversity"] = "Impacts on fish spawning grounds; loss of submerged aquatic vegetation; reduced light penetration; harm to benthic organisms."
african_great_lakes["Sedimentation"]["Influenced By"] = [
"Deforestation (in the watersheds of the lakes)",
"Agricultural Practices (poor soil conservation)",
"Land-Use Change (in the watersheds)"
]
african_great_lakes["Sedimentation"]["Influences"] = [
"Aquatic (African Great Lakes) - Water Quality",
"Aquatic (African Great Lakes) - Habitat Loss",
"Aquatic (African Great Lakes) - Lake Ecosystem Health"
]
african_great_lakes["Sedimentation"]["Logic Description"] = "Increased sedimentation, primarily due to deforestation and poor land management practices in the watersheds surrounding the lakes, reduces water clarity, smothers habitats, and impacts aquatic life."
african_great_lakes["Sedimentation"]["Impact Function"] = "impact_sedimentation_african_great_lakes"

african_great_lakes["Eutrophication"]["Metric"] = "Nutrient concentrations (nitrogen, phosphorus); chlorophyll-a concentrations; dissolved oxygen levels."
african_great_lakes["Eutrophication"]["Data Sources"] = [
"Water quality monitoring programs.",
"Research studies."
]
african_great_lakes["Eutrophication"]["Impact on Area"] = "Algal blooms; reduced oxygen levels (hypoxia); reduced water clarity."
african_great_lakes["Eutrophication"]["Impact on Biodiversity"] = "Loss of aquatic plants; fish kills; changes in species composition; impacts on food webs."
african_great_lakes["Eutrophication"]["Influenced By"] = [
"Aquatic (African Great Lakes) - Agricultural Runoff",
"Aquatic (African Great Lakes) - Urban Runoff",
"Aquatic (African Great Lakes) - Deforestation (leading to increased nutrient runoff)"
]
african_great_lakes["Eutrophication"]["Influences"] = [
"Aquatic (African Great Lakes) - Water Quality",
"Aquatic (African Great Lakes) - Fish Populations",
"Aquatic (African Great Lakes) - Ecosystem Function"
]
african_great_lakes["Eutrophication"]["Logic Description"] = "Eutrophication, caused by excessive nutrient inputs from agriculture, urban areas, and deforestation, leads to algal blooms, oxygen depletion, and impacts on aquatic life."
african_great_lakes["Eutrophication"]["Impact Function"] = "impact_eutrophication_african_great_lakes"

# --- Aquatic (Cold-Water Corals) ---
cold_water_corals = all_stressors_data["Cold-Water Corals"]

cold_water_corals["Bottom Trawling"]["Metric"] = "Area of seafloor trawled (km²/year); frequency of trawling in areas with cold-water coral habitats; damage to coral structures."
cold_water_corals["Bottom Trawling"]["Data Sources"] = [
"Fisheries data (often incomplete or lacking spatial detail).",
"Vessel Monitoring System (VMS) data (if available).",
"Underwater surveys (using ROVs, submersibles, or towed cameras).",
"Research publications."
]
cold_water_corals["Bottom Trawling"]["Impact on Area"] = "*Severe* physical destruction of cold-water coral habitats; removal of habitat-forming coral structures."
cold_water_corals["Bottom Trawling"]["Impact on Biodiversity"] = "High mortality of corals and associated species (sponges, fish, invertebrates).; Loss of biodiversity hotspots.; Disruption of deep-sea ecosystems.; *Extremely* slow recovery rates (centuries to millennia)."
cold_water_corals["Bottom Trawling"]["Influenced By"] = [
"Demand for Deep-Sea Fish",
"Fishing Technology",
"Lack of Effective Management and Protection"
]
cold_water_corals["Bottom Trawling"]["Influences"] = [
"Habitat Destruction (the overwhelming impact).",
"Benthic Community Structure"
]
cold_water_corals["Bottom Trawling"]["Logic Description"] = "Bottom trawling is the *single greatest direct threat* to cold-water coral ecosystems. Trawling physically destroys the coral structures, which are very slow-growing and provide habitat for a wide range of species."
cold_water_corals["Bottom Trawling"]["Impact Function"] = "impact_bottom_trawling_cold_water_corals"

cold_water_corals["Climate Change"]["Metric"] = "Changes in deep-sea temperature (°C); changes in ocean currents; changes in oxygen levels; changes in food supply from surface waters."
cold_water_corals["Climate Change"]["Data Sources"] = [
"Climate models.",
"Oceanographic data (sparse in deep-sea environments).",
"Research publications."
]
cold_water_corals["Climate Change"]["Impact on Area"] = "Changes in the physical and chemical environment of deep-sea coral habitats."
cold_water_corals["Climate Change"]["Impact on Biodiversity"] = "Potential shifts in species distributions.; Impacts on physiology and reproduction of corals and associated species.; Changes in food availability."
cold_water_corals["Climate Change"]["Influenced By"] = [
"Global Greenhouse Gas Emissions"
]
cold_water_corals["Climate Change"]["Influences"] = [
"Aquatic (Cold-Water Corals) - Ocean Acidification",
"Aquatic (Cold-Water Corals) - Food Supply"
]
cold_water_corals["Climate Change"]["Logic Description"] = "While less directly impacted by surface warming than shallow-water ecosystems, cold-water corals are still vulnerable to climate change through changes in ocean currents, oxygen levels, food supply, and acidification."
cold_water_corals["Climate Change"]["Impact Function"] = "impact_climate_change_cold_water_corals"

cold_water_corals["Ocean Acidification"]["Metric"] = "Ocean pH; aragonite and calcite saturation states (Ω) in deep water."
cold_water_corals["Ocean Acidification"]["Data Sources"] = [
"Oceanographic data (sparse in deep-sea environments).",
"Research publications.",
"Models."
]
cold_water_corals["Ocean Acidification"]["Impact on Area"] = "Reduced calcification rates in some cold-water coral species; potential for dissolution of coral skeletons in the long term."
cold_water_corals["Ocean Acidification"]["Impact on Biodiversity"] = "Impacts on the ability of some corals to build and maintain their skeletons; potential impacts on other calcifying organisms in the deep sea."
cold_water_corals["Ocean Acidification"]["Influenced By"] = [
"Global Carbon Dioxide Emissions"
]
cold_water_corals["Ocean Acidification"]["Influences"] = [
"Aquatic (Cold-Water Corals) - Coral Growth",
"Aquatic (Cold-Water Corals) - Skeleton Strength"
]
cold_water_corals["Ocean Acidification"]["Logic Description"] = "Ocean acidification, caused by the absorption of CO2 by the ocean, is a threat to cold-water corals, particularly those that build skeletons out of aragonite, which is more soluble than calcite."
cold_water_corals["Ocean Acidification"]["Impact Function"] = "impact_ocean_acidification_cold_water_corals"

cold_water_corals["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., heavy metals, persistent organic pollutants (POPs), plastics) in sediments and coral tissues."
cold_water_corals["Pollution"]["Data Sources"] = [
"Analysis of sediment and coral tissue samples.",
"Research studies."
]
cold_water_corals["Pollution"]["Impact on Area"] = "Contamination of deep-sea habitats."
cold_water_corals["Pollution"]["Impact on Biodiversity"] = "Toxic effects on corals and associated species.; Bioaccumulation of pollutants in the food chain."
cold_water_corals["Pollution"]["Influenced By"] = [
"Long-Range Transport of Pollutants",
"Shipping Activities",
"Dumping",
"Oil and Gas Exploration/Extraction",
"Deep-Sea Mining (potential future threat)"
]
cold_water_corals["Pollution"]["Influences"] = [
"Aquatic (Cold-Water Corals) - Coral Health",
"Aquatic (Cold-Water Corals) - Ecosystem Functioning"
]
cold_water_corals["Pollution"]["Logic Description"] = "Pollution, including heavy metals, persistent organic pollutants, and plastics, can reach even remote deep-sea coral habitats, with potential toxic effects."
cold_water_corals["Pollution"]["Impact Function"] = "impact_pollution_cold_water_corals"

cold_water_corals["Deep-Sea Mining"]["Metric"] = "Area of seabed licensed for exploration or exploitation near cold-water coral habitats."
cold_water_corals["Deep-Sea Mining"]["Data Sources"] = [
"International Seabed Authority (ISA) data.",
"National government data.",
"Research publications."
]
cold_water_corals["Deep-Sea Mining"]["Impact on Area"] = "Potential for direct physical destruction of coral habitats if mining occurs in those areas; sediment plumes."
cold_water_corals["Deep-Sea Mining"]["Impact on Biodiversity"] = "Loss of habitat; smothering by sediment plumes; potential release of toxic substances."
cold_water_corals["Deep-Sea Mining"]["Influenced By"] = [
"Demand for Minerals",
"Technological Developments",
"International Regulations"
]
cold_water_corals["Deep-Sea Mining"]["Influences"] = [
"Aquatic (Cold-Water Corals) - Habitat Destruction"
]
cold_water_corals["Deep-Sea Mining"]["Logic Description"] = "Deep-sea mining is a potential future threat to cold-water corals, particularly if mining targets areas near coral habitats."
cold_water_corals["Deep-Sea Mining"]["Impact Function"] = "impact_deep_sea_mining_cold_water_corals"

cold_water_corals["Oil and Gas Exploration/Extraction"]["Metric"] = "Area of seabed licensed for exploration or extraction; number of oil and gas platforms; frequency of seismic surveys."
cold_water_corals["Oil and Gas Exploration/Extraction"]["Data Sources"] = [
"Government data (licensing).",
"Industry reports.",
"Research publications."
]
cold_water_corals["Oil and Gas Exploration/Extraction"]["Impact on Area"] = "Potential for habitat destruction; noise pollution from seismic surveys; risk of oil spills."
cold_water_corals["Oil and Gas Exploration/Extraction"]["Impact on Biodiversity"] = "Disturbance to marine life from noise; toxic effects of oil spills; physical damage to habitats."
cold_water_corals["Oil and Gas Exploration/Extraction"]["Influenced By"] = [
"Global Energy Demand",
"Economic Factors",
"Government Policies"
]
cold_water_corals["Oil and Gas Exploration/Extraction"]["Influences"] = [
"Aquatic (Cold-Water Corals) - Noise Pollution",
"Aquatic (Cold-Water Corals) - Pollution (oil spills)",
"Aquatic (Cold-Water Corals) - Habitat Destruction"
]
cold_water_corals["Oil and Gas Exploration/Extraction"]["Logic Description"] = "Oil and gas exploration and extraction activities can pose risks to cold-water coral ecosystems through noise pollution, habitat destruction, and potential oil spills."
cold_water_corals["Oil and Gas Exploration/Extraction"]["Impact Function"] = "impact_oil_gas_cold_water_corals"

# --- Aquatic (Great Lakes) ---
great_lakes = all_stressors_data["Great Lakes"]  # Corrected variable name

great_lakes["Pollution"]["Metric"] = "Concentrations of legacy pollutants (e.g., PCBs, mercury), emerging contaminants (e.g., pharmaceuticals, microplastics), and nutrients (phosphorus, nitrogen) in water, sediments, and biota."
great_lakes["Pollution"]["Data Sources"] = [
"Great Lakes Water Quality Agreement (GLWQA) monitoring programs.",
"U.S. Environmental Protection Agency (EPA) Great Lakes National Program Office (GLNPO).",
"Environment and Climate Change Canada.",
"State/provincial environmental agencies.",
"Research publications."
]
great_lakes["Pollution"]["Impact on Area"] = "Degradation of water quality; contamination of sediments and biota; Areas of Concern (AOCs) with severe pollution problems."
great_lakes["Pollution"]["Impact on Biodiversity"] = "Toxic effects on fish, wildlife, and invertebrates; bioaccumulation of contaminants in the food web; impacts on human health (through consumption of fish)."
great_lakes["Pollution"]["Influenced By"] = [
"Industrial Discharges (historical and ongoing).",
"Municipal Wastewater Treatment Plants.",
"Agricultural Runoff.",
"Urban Runoff.",
"Atmospheric Deposition.",
"Contaminated Sediments (legacy pollution)."
]
great_lakes["Pollution"]["Influences"] = [
"Aquatic (Great Lakes) - Water Quality",
"Aquatic (Great Lakes) - Wildlife Health",
"Aquatic (Great Lakes) - Human Health",
"Aquatic (Great Lakes) - Eutrophication"
]
great_lakes["Pollution"]["Logic Description"] = "The Great Lakes have a long history of pollution from industrial, agricultural, and urban sources. While progress has been made in reducing some pollutants, legacy contaminants and emerging threats remain a concern."
great_lakes["Pollution"]["Impact Function"] = "impact_pollution_great_lakes"

great_lakes["Invasive Species"]["Metric"] = "Number of established non-native species; abundance and distribution of key invasive species (e.g., zebra mussels, quagga mussels, sea lamprey)."
great_lakes["Invasive Species"]["Data Sources"] = [
"Great Lakes Aquatic Nonindigenous Species Information System (GLANSIS).",
"U.S. Geological Survey (USGS) Nonindigenous Aquatic Species (NAS) database.",
"Fisheries and Oceans Canada.",
"Research publications."
]
great_lakes["Invasive Species"]["Impact on Area"] = "Widespread impacts throughout the Great Lakes ecosystem."
great_lakes["Invasive Species"]["Impact on Biodiversity"] = "Competition with and predation on native species.; Alteration of food webs.; Changes in habitat structure.; Economic impacts (e.g., on fisheries, infrastructure)."
great_lakes["Invasive Species"]["Influenced By"] = [
"Ballast Water Discharge (from ships).",
"Canals and Waterways (connecting the Great Lakes to other watersheds).",
"Recreational Boating.",
"Intentional or Accidental Introductions."
]
great_lakes["Invasive Species"]["Influences"] = [
"Aquatic (Great Lakes) - Native Species",
"Aquatic (Great Lakes) - Food Web Structure",
"Aquatic (Great Lakes) - Ecosystem Function"
]
great_lakes["Invasive Species"]["Logic Description"] = "Invasive species have had a *profound* impact on the Great Lakes ecosystem. Species like zebra and quagga mussels have altered food webs and water quality, while sea lamprey have decimated native fish populations."
great_lakes["Invasive Species"]["Impact Function"] = "impact_invasive_species_great_lakes"

great_lakes["Climate Change"]["Metric"] = "Water temperature (°C); ice cover duration and extent; changes in precipitation patterns; changes in lake levels; changes in stratification."
great_lakes["Climate Change"]["Data Sources"] = [
"Climate models.",
"Long-term monitoring data (temperature, ice cover, water levels).",
"NOAA Great Lakes Environmental Research Laboratory (GLERL).",
"Research publications."
]
great_lakes["Climate Change"]["Impact on Area"] = "Warming water temperatures; reduced ice cover; changes in lake stratification; more extreme water level fluctuations."
great_lakes["Climate Change"]["Impact on Biodiversity"] = "Shifts in species distributions (favoring warm-water species).; Impacts on fish spawning and recruitment.; Increased stress on cold-water species.; Potential for increased algal blooms."
great_lakes["Climate Change"]["Influenced By"] = ["Global GHG"]
great_lakes["Climate Change"]["Influences"] = [
"Aquatic (Great Lakes) - Water Temperature",
"Aquatic (Great Lakes) - Ice Cover",
"Aquatic (Great Lakes) - Water Levels",
"Aquatic (Great Lakes) - Lake Stratification"
]
great_lakes["Climate Change"]["Logic Description"] = "Climate change is warming the Great Lakes, reducing ice cover, and altering water levels and stratification patterns, with significant impacts on the ecosystem."
great_lakes["Climate Change"]["Impact Function"] = "impact_climate_change_great_lakes"

great_lakes["Coastal Development"]["Metric"] = "Area of coastal wetlands lost or degraded; shoreline hardening (e.g., seawalls, breakwaters); development density along the coast."
great_lakes["Coastal Development"]["Data Sources"] = [
"Remote sensing data.",
"Land-use planning records.",
"Coastal zone management agencies.",
"Research publications."
]
great_lakes["Coastal Development"]["Impact on Area"] = "Loss of coastal wetlands, which provide important habitat and ecosystem services."
great_lakes["Coastal Development"]["Impact on Biodiversity"] = "Loss of habitat for fish, birds, and other wildlife; disruption of coastal processes; reduced water quality."
great_lakes["Coastal Development"]["Influenced By"] = [
"Population Growth (in coastal areas)",
"Economic Development",
"Recreational Demand"
]
great_lakes["Coastal Development"]["Influences"] = [
"Aquatic (Great Lakes) - Habitat Loss",
"Aquatic (Great Lakes) - Water Quality"
]
great_lakes["Coastal Development"]["Logic Description"] = "Coastal development, including the loss of wetlands and shoreline hardening, degrades habitat and impacts water quality in the Great Lakes."
great_lakes["Coastal Development"]["Impact Function"] = "impact_coastal_development_great_lakes"

great_lakes["Water Level Fluctuations"]["Metric"] = "Changes in lake levels (magnitude and frequency); changes in the timing of seasonal water level changes."
great_lakes["Water Level Fluctuations"]["Data Sources"] = [
"Long-term lake level records (from the U.S. Army Corps of Engineers and Canadian Hydrographic Service).",
"Climate models."
]
great_lakes["Water Level Fluctuations"]["Impact on Area"] = "Impacts on coastal infrastructure; changes in wetland areas; impacts on navigation."
great_lakes["Water Level Fluctuations"]["Impact on Biodiversity"] = "Impacts on fish spawning habitat; changes in wetland vegetation; impacts on coastal ecosystems."
great_lakes["Water Level Fluctuations"]["Influenced By"] = [
"Aquatic (Great Lakes) - Climate Change",
"Precipitation Patterns",
"Evaporation Rates",
"Water Management Practices (e.g., diversions)"
]
great_lakes["Water Level Fluctuations"]["Influences"] = [
"Aquatic (Great Lakes) - Coastal Wetlands",
"Aquatic (Great Lakes) - Fish Spawning",
"Aquatic (Great Lakes) - Coastal Processes"
]
great_lakes["Water Level Fluctuations"]["Logic Description"] = "Water level fluctuations, both natural and influenced by climate change and water management, can impact coastal ecosystems and infrastructure."
great_lakes["Water Level Fluctuations"]["Impact Function"] = "impact_water_level_fluctuations_great_lakes"

great_lakes["Overfishing"]["Metric"] = "Fish catches; fishing effort; fish biomass and size structure; catch per unit effort (CPUE)."
great_lakes["Overfishing"]["Data Sources"] = [
"Fisheries management agencies (state/provincial and federal).",
"Research surveys.",
"Commercial fishing records."
]
great_lakes["Overfishing"]["Impact on Area"] = "Not directly applicable (affects fish populations, not area)."
great_lakes["Overfishing"]["Impact on Biodiversity"] = "Historical overfishing led to the collapse of some fish stocks (e.g., lake trout in some areas).; While management has improved, overfishing remains a potential threat to some species."
great_lakes["Overfishing"]["Influenced By"] = [
"Fishing Pressure",
"Fisheries Management Practices",
"Demand for Fish"
]
great_lakes["Overfishing"]["Influences"] = [
"Aquatic (Great Lakes) - Fish Populations",
"Aquatic (Great Lakes) - Food Web Structure"
]
great_lakes["Overfishing"]["Logic Description"] = "Overfishing has historically been a major problem in the Great Lakes, and while management has improved, it remains a concern for some fish populations."
great_lakes["Overfishing"]["Impact Function"] = "impact_overfishing_great_lakes"

great_lakes["Eutrophication"]["Metric"] = "Nutrient concentrations (phosphorus, nitrogen); chlorophyll-a concentrations; dissolved oxygen levels; frequency and extent of algal blooms."
great_lakes["Eutrophication"]["Data Sources"] = [
"Water quality monitoring programs.",
"Research studies.",
"Great Lakes Water Quality Agreement (GLWQA) reports."
]
great_lakes["Eutrophication"]["Impact on Area"] = "Algal blooms; reduced oxygen levels (hypoxia); reduced water clarity; dead zones in some areas (e.g., central basin of Lake Erie)."
great_lakes["Eutrophication"]["Impact on Biodiversity"] = "Impacts on fish and invertebrate communities; loss of submerged aquatic vegetation; changes in species composition."
great_lakes["Eutrophication"]["Influenced By"] = [
"Aquatic (Great Lakes) - Agricultural Runoff",
"Aquatic (Great Lakes) - Urban Runoff",
"Aquatic (Great Lakes) - Atmospheric Deposition"
]
great_lakes["Eutrophication"]["Influences"] = [
"Aquatic (Great Lakes) - Water Quality",
"Aquatic (Great Lakes) - Fish Populations",
"Aquatic (Great Lakes) - Ecosystem Function"
]
great_lakes["Eutrophication"]["Logic Description"] = "Eutrophication, caused by excessive nutrient inputs, leads to algal blooms, oxygen depletion, and impacts on aquatic life, particularly in areas like Lake Erie."
great_lakes["Eutrophication"]["Impact Function"] = "impact_eutrophication_great_lakes"

great_lakes["Habitat Loss"]["Metric"] = "Area of natural habitat lost or degraded; connectivity of remaining habitats."
great_lakes["Habitat Loss"]["Data Sources"] = [
"Land-use change data.",
"Habitat mapping.",
"Research studies."
]
great_lakes["Habitat Loss"]["Impact on Area"] = "Reduced quantity and quality of habitat for fish and wildlife."
great_lakes["Habitat Loss"]["Impact on Biodiversity"] = "Declines in species that rely on specific habitats; loss of biodiversity."
great_lakes["Habitat Loss"]["Influenced By"] = [
"Aquatic (Great Lakes) - Coastal Development",
"Aquatic (Great Lakes) - Urban Sprawl",
"Agricultural Expansion"
]
great_lakes["Habitat Loss"]["Influences"] = [
"Biodiversity in General"
]
great_lakes["Habitat Loss"]["Logic Description"] = "Habitat loss, primarily due to coastal development and other land-use changes, reduces the availability of suitable habitat for fish and wildlife in the Great Lakes region."
great_lakes["Habitat Loss"]["Impact Function"] = "impact_habitat_loss_great_lakes"

# --- Aquatic (Hydrothermal Vents) ---
hydrothermal_vents = all_stressors_data["Hydrothermal Vents"]

hydrothermal_vents["Deep-Sea Mining"]["Metric"] = "Area of vent fields licensed for exploration or exploitation; proximity of mining activities to active vents; metal concentrations."
hydrothermal_vents["Deep-Sea Mining"]["Data Sources"] = [
"International Seabed Authority (ISA) data.",
"Research publications.",
"Environmental Impact Assessments (EIAs)."
]
hydrothermal_vents["Deep-Sea Mining"]["Impact on Area"] = "Potential for direct destruction of vent habitats; potential for disruption of hydrothermal fluid flow; sediment plumes."
hydrothermal_vents["Deep-Sea Mining"]["Impact on Biodiversity"] = "Loss of unique and highly specialized vent fauna (many species are endemic to specific vents or vent fields).; Potential for extinction of species before they are even discovered.; Disruption of chemosynthetic ecosystems."
hydrothermal_vents["Deep-Sea Mining"]["Influenced By"] = [
"Global Demand for Minerals (e.g., copper, zinc, gold, silver).",
"Technological Advancements",
"International Regulations (ISA)"
]
hydrothermal_vents["Deep-Sea Mining"]["Influences"] = [
"Aquatic (Hydrothermal Vents) - Habitat Destruction",
"Aquatic (Hydrothermal Vents) - Water Quality",
"Aquatic (Hydrothermal Vents) - Vent Fluid Chemistry"
]
hydrothermal_vents["Deep-Sea Mining"]["Logic Description"] = "Deep-sea mining at hydrothermal vents poses a *major* threat to these unique and fragile ecosystems. Mining could directly destroy vent habitats and the specialized fauna that depend on them, with potentially irreversible consequences."
hydrothermal_vents["Deep-Sea Mining"]["Impact Function"] = "impact_deep_sea_mining_hydrothermal_vents"

hydrothermal_vents["Climate Change"]["Metric"] = "Changes in deep-sea temperature (°C); changes in ocean currents; changes in oxygen levels; ocean acidification (pH)."
hydrothermal_vents["Climate Change"]["Data Sources"] = [
"Oceanographic data (sparse in deep-sea environments).",
"Climate models.",
"Research publications."
]
hydrothermal_vents["Climate Change"]["Impact on Area"] = "Changes in the physical and chemical properties of the deep-sea environment, potentially affecting vent fluid chemistry and flow."
hydrothermal_vents["Climate Change"]["Impact on Biodiversity"] = "Potential impacts on vent fauna, though the specific effects are poorly understood. Deep-sea species may be less directly sensitive to temperature changes than shallow-water species, but changes in ocean currents, oxygen levels, and acidification could have impacts."
hydrothermal_vents["Climate Change"]["Influenced By"] = ["Global GHG"]
hydrothermal_vents["Climate Change"]["Influences"] = [
"Aquatic (Hydrothermal Vents) - Ocean Acidification",
"Aquatic (Hydrothermal Vents) - Ocean Currents",
"Aquatic (Hydrothermal Vents) - Oxygen Levels"
]
hydrothermal_vents["Climate Change"]["Logic Description"] = "While hydrothermal vent ecosystems are relatively isolated from surface climate changes, large-scale changes in ocean circulation, oxygen levels, and acidification could potentially impact them."
hydrothermal_vents["Climate Change"]["Impact Function"] = "impact_climate_change_hydrothermal_vents"

hydrothermal_vents["Research Activities"]["Metric"] = "Number of research expeditions to vent sites; frequency of sampling; types of sampling methods used; use of submersibles and ROVs."
hydrothermal_vents["Research Activities"]["Data Sources"] = [
"Research cruise reports.",
"Scientific publications.",
"Databases of deep-sea expeditions."
]
hydrothermal_vents["Research Activities"]["Impact on Area"] = "Localized disturbance to vent habitats; potential for damage to vent structures and fauna."
hydrothermal_vents["Research Activities"]["Impact on Biodiversity"] = "Potential impacts on vent fauna from sampling and vehicle operations. While researchers strive to minimize impacts, some disturbance is unavoidable."
hydrothermal_vents["Research Activities"]["Influenced By"] = [
"Scientific Interest in Vents",
"Funding for Deep-Sea Research"
]
hydrothermal_vents["Research Activities"]["Influences"] = [
"Aquatic (Hydrothermal Vents) - Localized Disturbance"
]
hydrothermal_vents["Research Activities"]["Logic Description"] = "Scientific research is essential for understanding hydrothermal vent ecosystems, but research activities themselves can cause some disturbance. Best practices and careful planning are needed to minimize impacts."
hydrothermal_vents["Research Activities"]["Impact Function"] = "impact_research_activities_hydrothermal_vents"

hydrothermal_vents["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., plastic debris, chemical contaminants) in vent fluids, sediments, and organisms."
hydrothermal_vents["Pollution"]["Data Sources"] = [
"Analysis of vent fluid, sediment, and tissue samples.",
"Research publications."
]
hydrothermal_vents["Pollution"]["Impact on Area"] = "Contamination of the vent environment."
hydrothermal_vents["Pollution"]["Impact on Biodiversity"] = "Potential toxic effects on vent fauna, though the extent of this is not well understood."
hydrothermal_vents["Pollution"]["Influenced By"] = [
"Long-Range Transport of Pollutants",
"Deep-Sea Mining (potential future source)",
"Shipping (accidental spills)"
]
hydrothermal_vents["Pollution"]["Influences"] = [
"Aquatic (Hydrothermal Vents) - Vent Fauna Health"
]
hydrothermal_vents["Pollution"]["Logic Description"] = "Pollution, including plastic debris and chemical contaminants, can reach even remote deep-sea environments like hydrothermal vents, with potential impacts on vent fauna."
hydrothermal_vents["Pollution"]["Impact Function"] = "impact_pollution_hydrothermal_vents"

# --- Kelp Forests (Australian) ---
kelp_forests_australian = all_stressors_data["Australian Kelp Forests"]

kelp_forests_australian["Climate Change"]["Metric"] = "Sea surface temperature (SST) (°C); frequency and severity of marine heatwaves; ocean acidification (pH); changes in ocean currents."
kelp_forests_australian["Climate Change"]["Data Sources"] = [
"Australian Bureau of Meteorology (BOM) data.",
"Integrated Marine Observing System (IMOS) data.",
"CSIRO research.",
"Climate models.",
"Research publications."
]
kelp_forests_australian["Climate Change"]["Impact on Area"] = "*Major* kelp forest declines and die-offs, particularly in Western Australia and Tasmania, associated with marine heatwaves."
kelp_forests_australian["Climate Change"]["Impact on Biodiversity"] = "Loss of kelp forest habitat; shifts in species distributions (e.g., range contractions of kelp species, range expansions of warm-water species); changes in community structure; reduced resilience to other stressors."
kelp_forests_australian["Climate Change"]["Influenced By"] = [
"Global Greenhouse Gas Emissions",
"Changes in Ocean Currents (e.g., strengthening of the East Australian Current)"
]
kelp_forests_australian["Climate Change"]["Influences"] = [
"Kelp Forests (Australian) - Marine Heatwaves",
"Kelp Forests (Australian) - Ocean Acidification",
"Kelp Forests (Australian) - Range Shifts"
]
kelp_forests_australian["Climate Change"]["Logic Description"] = "Climate change, particularly ocean warming and marine heatwaves, has caused significant and widespread kelp forest declines in parts of Australia. This is a *major* and ongoing threat."
kelp_forests_australian["Climate Change"]["Impact Function"] = "impact_climate_change_kelp_australian"

kelp_forests_australian["Overgrazing"]["Metric"] = "Sea urchin density (number per square meter); abundance of other herbivorous fish; kelp cover (percentage)."
kelp_forests_australian["Overgrazing"]["Data Sources"] = [
"Underwater surveys.",
"Research studies.",
"Fisheries data (for some urchin species)."
]
kelp_forests_australian["Overgrazing"]["Impact on Area"] = "Formation of urchin barrens (areas devoid of kelp) in some regions."
kelp_forests_australian["Overgrazing"]["Impact on Biodiversity"] = "Loss of kelp forest habitat; reduced biodiversity and ecosystem complexity."
kelp_forests_australian["Overgrazing"]["Influenced By"] = [
"Overfishing of Urchin Predators (e.g., rock lobsters)",
"Kelp Forests (Australian) - Climate Change (warming can favor urchins)",
"Range Shifts of Sea Urchins"
]
kelp_forests_australian["Overgrazing"]["Influences"] = [
"Kelp Forests (Australian) - Urchin Barrens Formation"
]
kelp_forests_australian["Overgrazing"]["Logic Description"] = "Overgrazing by sea urchins (and, in some cases, certain fish species) can lead to the formation of urchin barrens, where kelp forests are replaced by bare rock with low biodiversity."
kelp_forests_australian["Overgrazing"]["Impact Function"] = "impact_overgrazing_kelp_australian"

kelp_forests_australian["Invasive Species"]["Metric"] = "Distribution and abundance of key invasive species (e.g., *Undaria pinnatifida* (Japanese kelp), *Caulerpa taxifolia*)."
kelp_forests_australian["Invasive Species"]["Data Sources"] = [
"Underwater surveys.",
"Research studies.",
"Government reports."
]
kelp_forests_australian["Invasive Species"]["Impact on Area"] = "Competition with native kelp species; alteration of habitat structure."
kelp_forests_australian["Invasive Species"]["Impact on Biodiversity"] = "Can outcompete native kelp and other seaweeds; impacts on associated invertebrate and fish communities."
kelp_forests_australian["Invasive Species"]["Influenced By"] = [
"Shipping (ballast water, hull fouling).",
"Aquaculture.",
"Kelp Forests (Australian) - Climate Change (may favor some invasives)."
]
kelp_forests_australian["Invasive Species"]["Influences"] = [
"Kelp Forests (Australian) - Native Kelp Populations"
]
kelp_forests_australian["Invasive Species"]["Logic Description"] = "Invasive species, such as the Japanese kelp *Undaria pinnatifida*, can outcompete native kelp and alter kelp forest ecosystems."
kelp_forests_australian["Invasive Species"]["Impact Function"] = "impact_invasive_species_kelp_australian"

kelp_forests_australian["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., nutrients, sediments, heavy metals) in coastal waters."
kelp_forests_australian["Pollution"]["Data Sources"] = [
"Water quality monitoring data.",
"Research studies."
]
kelp_forests_australian["Pollution"]["Impact on Area"] = "Reduced water quality; increased turbidity; potential for toxic effects."
kelp_forests_australian["Pollution"]["Impact on Biodiversity"] = "Impacts on kelp growth and survival; impacts on other marine organisms."
kelp_forests_australian["Pollution"]["Influenced By"] = [
"Urban Runoff",
"Industrial Discharge",
"Agricultural Runoff"
]
kelp_forests_australian["Pollution"]["Influences"] = [
"Kelp Forests (Australian) - Water Quality",
"Kelp Forests (Australian) - Kelp Health"
]
kelp_forests_australian["Pollution"]["Logic Description"] = "Pollution from various sources can degrade water quality and impact kelp forest health."
kelp_forests_australian["Pollution"]["Impact Function"] = "impact_pollution_kelp_australian"

kelp_forests_australian["Coastal Development"]["Metric"] = "Area of coastline developed; proximity of development to kelp forests."
kelp_forests_australian["Coastal Development"]["Data Sources"] = [
"Government planning data.",
"Remote sensing data."
]
kelp_forests_australian["Coastal Development"]["Impact on Area"] = "Habitat loss; increased runoff and pollution."
kelp_forests_australian["Coastal Development"]["Impact on Biodiversity"] = "Impacts on kelp forests and associated species due to habitat loss, reduced water quality, and increased disturbance."
kelp_forests_australian["Coastal Development"]["Influenced By"] = [
"Population Growth",
"Urbanization",
"Tourism"
]
kelp_forests_australian["Coastal Development"]["Influences"] = [
"Kelp Forests (Australian) - Water Quality",
"Kelp Forests (Australian) - Habitat Loss"
]
kelp_forests_australian["Coastal Development"]["Logic Description"] = "Coastal development can lead to habitat loss and increased pollution, impacting nearby kelp forests."
kelp_forests_australian["Coastal Development"]["Impact Function"] = "impact_coastal_development_kelp_australian"

# --- Kelp Forests (California) ---
kelp_forests_california = all_stressors_data["California Kelp Forests"]

kelp_forests_california["Climate Change"]["Metric"] = "Sea surface temperature (SST); frequency and intensity of marine heatwaves; upwelling intensity; El Niño-Southern Oscillation (ENSO) events."
kelp_forests_california["Climate Change"]["Data Sources"] = [
"NOAA National Centers for Environmental Information (NCEI).",
"Scripps Institution of Oceanography.",
"California Cooperative Oceanic Fisheries Investigations (CalCOFI).",
"Climate models.",
"Research publications."
]
kelp_forests_california["Climate Change"]["Impact on Area"] = "Major kelp forest declines during marine heatwaves and strong El Niño events.  Changes in kelp distribution and abundance."
kelp_forests_california["Climate Change"]["Impact on Biodiversity"] = "Loss of kelp forest habitat; shifts in species distributions (e.g., northward shifts of warm-water species); changes in community structure.; Reduced resilience to other stressors."
kelp_forests_california["Climate Change"]["Influenced By"] = [
"Global Greenhouse Gas Emissions",
"Changes in Ocean Circulation Patterns",
"ENSO Variability"
]
kelp_forests_california["Climate Change"]["Influences"] = [
"Kelp Forests (California) - Marine Heatwaves",
"Kelp Forests (California) - Ocean Acidification",
"Kelp Forests (California) - Upwelling Patterns",
"Kelp Forests (California) - Range Shifts"
]
kelp_forests_california["Climate Change"]["Logic Description"] = "California kelp forests are highly sensitive to climate change, particularly to warming waters, marine heatwaves, and changes in upwelling patterns, which affect nutrient availability."
kelp_forests_california["Climate Change"]["Impact Function"] = "impact_climate_change_kelp_california"

kelp_forests_california["Overgrazing"]["Metric"] = "Sea urchin density (number per square meter); abundance of other herbivorous fish; kelp cover (percentage); presence/absence of urchin barrens."
kelp_forests_california["Overgrazing"]["Data Sources"] = [
"Underwater surveys.",
"Research studies (e.g., from universities, Reef Check California).",
"Citizen science monitoring programs."
]
kelp_forests_california["Overgrazing"]["Impact on Area"] = "Formation of urchin barrens (areas devoid of kelp) in some regions, particularly where sea urchin predators are depleted."
kelp_forests_california["Overgrazing"]["Impact on Biodiversity"] = "Loss of kelp forest habitat; reduced biodiversity and ecosystem complexity."
kelp_forests_california["Overgrazing"]["Influenced By"] = [
"Kelp Forests (California) - Fishing (removal of urchin predators like sea otters, sheephead, and lobsters).",
"Kelp Forests (California) - Climate Change (warming can favor urchins).",
"Disease Outbreaks (can affect urchin populations)."
]
kelp_forests_california["Overgrazing"]["Influences"] = [
"Kelp Forests (California) - Urchin Barrens Formation"
]
kelp_forests_california["Overgrazing"]["Logic Description"] = "Overgrazing by sea urchins, often exacerbated by the removal of their predators through fishing, can lead to the formation of urchin barrens and the loss of kelp forests."
kelp_forests_california["Overgrazing"]["Impact Function"] = "impact_overgrazing_kelp_california"

kelp_forests_california["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., nutrients, sediments, heavy metals, pesticides, plastics) in coastal waters."
kelp_forests_california["Pollution"]["Data Sources"] = [
"California State Water Resources Control Board.",
"Southern California Coastal Water Research Project (SCCWRP).",
"Research studies."
]
kelp_forests_california["Pollution"]["Impact on Area"] = "Reduced water quality; increased turbidity; potential for toxic effects."
kelp_forests_california["Pollution"]["Impact on Biodiversity"] = "Impacts on kelp growth and survival; impacts on other marine organisms (e.g., filter feeders, fish).; Bioaccumulation of toxins."
kelp_forests_california["Pollution"]["Influenced By"] = [
"Urban Runoff",
"Agricultural Runoff",
"Industrial Discharge",
"Wastewater Treatment Plants",
"Atmospheric Deposition"
]
kelp_forests_california["Pollution"]["Influences"] = [
"Kelp Forests (California) - Water Quality",
"Kelp Forests (California) - Kelp Health"
]
kelp_forests_california["Pollution"]["Logic Description"] = "Pollution from various sources can degrade water quality and impact kelp forest health along the California coast."
kelp_forests_california["Pollution"]["Impact Function"] = "impact_pollution_kelp_california"

kelp_forests_california["Coastal Development"]["Metric"] = "Area of coastline developed; proximity of development to kelp forests; shoreline armoring (e.g., seawalls)."
kelp_forests_california["Coastal Development"]["Data Sources"] = [
"California Coastal Commission.",
"Local government planning departments.",
"Remote sensing data."
]
kelp_forests_california["Coastal Development"]["Impact on Area"] = "Habitat loss; increased runoff and pollution; altered sediment transport."
kelp_forests_california["Coastal Development"]["Impact on Biodiversity"] = "Impacts on kelp forests and associated species due to habitat loss, reduced water quality, and increased disturbance."
kelp_forests_california["Coastal Development"]["Influenced By"] = [
"Population Growth",
"Urbanization",
"Tourism"
]
kelp_forests_california["Coastal Development"]["Influences"] = [
"Kelp Forests (California) - Water Quality",
"Kelp Forests (California) - Habitat Loss"
]
kelp_forests_california["Coastal Development"]["Logic Description"] = "Coastal development can lead to habitat loss and increased pollution, impacting nearby kelp forests in California."
kelp_forests_california["Coastal Development"]["Impact Function"] = "impact_coastal_development_kelp_california"

kelp_forests_california["Ocean Acidification"]["Metric"] = "Ocean pH; aragonite saturation state; carbonate ion concentration."
kelp_forests_california["Ocean Acidification"]["Data Sources"] = [
"Oceanographic monitoring data (e.g., from CalCOFI).",
"Research studies.",
"Models."
]
kelp_forests_california["Ocean Acidification"]["Impact on Area"] = "California is particularly vulnerable to ocean acidification due to upwelling of deep, CO2-rich water."
kelp_forests_california["Ocean Acidification"]["Impact on Biodiversity"] = "Potential impacts on calcifying organisms (e.g., sea urchins, shellfish, coralline algae); may indirectly affect kelp by altering competitive interactions."
kelp_forests_california["Ocean Acidification"]["Influenced By"] = [
"Global Carbon Dioxide Emissions",
"Upwelling Intensity"
]
kelp_forests_california["Ocean Acidification"]["Influences"] = [
"Kelp Forests (California) - Calcifying Organisms"
]
kelp_forests_california["Ocean Acidification"]["Logic Description"] = "Ocean acidification, driven by increased CO2 absorption by the ocean, is a growing threat to marine ecosystems, and the California coast is a region of particular concern due to upwelling."
kelp_forests_california["Ocean Acidification"]["Impact Function"] = "impact_ocean_acidification_kelp_california"

kelp_forests_california["Fishing"]["Metric"] = "Fishing effort (e.g., number of fishing vessels, fishing days); catch of key species (e.g., rockfish, lobsters, sea urchins)."
kelp_forests_california["Fishing"]["Data Sources"] = [
"California Department of Fish and Wildlife (CDFW).",
"Commercial and recreational fishing data."
]
kelp_forests_california["Fishing"]["Impact on Area"] = "Indirect effects on kelp forests through removal of key species in the food web."
kelp_forests_california["Fishing"]["Impact on Biodiversity"] = "Removal of sea urchin predators (e.g., sea otters, sheephead, lobsters) can lead to increased urchin grazing and kelp forest loss (trophic cascade). Removal of kelp forest fish can also impact the ecosystem."
kelp_forests_california["Fishing"]["Influenced By"] = [
"Fishing Regulations",
"Market Demand for Seafood",
"Economic Factors"
]
kelp_forests_california["Fishing"]["Influences"] = [
"Kelp Forests (California) - Overgrazing (by removing urchin predators)",
"Kelp Forests (California) - Food Web Structure"
]
kelp_forests_california["Fishing"]["Logic Description"] = "Fishing, particularly the removal of sea urchin predators, can have significant indirect impacts on kelp forests by altering trophic interactions and potentially leading to overgrazing by urchins."
kelp_forests_california["Fishing"]["Impact Function"] = "impact_fishing_kelp_california"

# --- Kelp Forests (North Atlantic) ---
kelp_forests_north_atlantic = all_stressors_data["North Atlantic Kelp Forests"]

kelp_forests_north_atlantic["Climate Change"]["Metric"] = "Sea surface temperature (SST); frequency and intensity of marine heatwaves; changes in storm frequency and intensity; sea level rise."
kelp_forests_north_atlantic["Climate Change"]["Data Sources"] = [
"NOAA National Centers for Environmental Information (NCEI).",
"Met Office (UK).",
"Fisheries and Oceans Canada.",
"European Environment Agency (EEA).",
"Climate models.",
"Research publications."
]
kelp_forests_north_atlantic["Climate Change"]["Impact on Area"] = "Range shifts in kelp distribution (e.g., northward movement); changes in kelp abundance and growth rates; increased vulnerability to other stressors."
kelp_forests_north_atlantic["Climate Change"]["Impact on Biodiversity"] = "Changes in community structure; impacts on associated species (fish, invertebrates, marine mammals); potential for increased disease outbreaks."
kelp_forests_north_atlantic["Climate Change"]["Influenced By"] = [
"Global Greenhouse Gas Emissions",
"Changes in Ocean Circulation (e.g., North Atlantic Oscillation)"
]
kelp_forests_north_atlantic["Climate Change"]["Influences"] = [
"Kelp Forests (North Atlantic) - Marine Heatwaves",
"Kelp Forests (North Atlantic) - Ocean Acidification",
"Kelp Forests (North Atlantic) - Storm Damage",
"Kelp Forests (North Atlantic) - Range Shifts"
]
kelp_forests_north_atlantic["Climate Change"]["Logic Description"] = "North Atlantic kelp forests are experiencing warming waters, increased storminess, and sea level rise due to climate change, leading to range shifts, changes in abundance, and increased vulnerability to other stressors."
kelp_forests_north_atlantic["Climate Change"]["Impact Function"] = "impact_climate_change_kelp_north_atlantic"

kelp_forests_north_atlantic["Overfishing"]["Metric"] = "Fishing effort; catch of key species (e.g., cod, haddock, lobster); abundance of sea urchin predators."
kelp_forests_north_atlantic["Overfishing"]["Data Sources"] = [
"Fisheries management agencies (e.g., NOAA Fisheries, ICES).",
"Commercial and recreational fishing data.",
"Research surveys."
]
kelp_forests_north_atlantic["Overfishing"]["Impact on Area"] = "Indirect impacts on kelp forests through trophic cascades."
kelp_forests_north_atlantic["Overfishing"]["Impact on Biodiversity"] = "Removal of sea urchin predators (e.g., cod, haddock, lobsters) can lead to increased urchin grazing and kelp forest loss (urchin barrens). Removal of other kelp forest fish can also impact the ecosystem."
kelp_forests_north_atlantic["Overfishing"]["Influenced By"] = [
"Fishing Pressure",
"Fisheries Management Regulations",
"Market Demand"
]
kelp_forests_north_atlantic["Overfishing"]["Influences"] = [
"Kelp Forests (North Atlantic) - Urchin Barrens Formation (via trophic cascade)",
"Kelp Forests (North Atlantic) - Food Web Structure"
]
kelp_forests_north_atlantic["Overfishing"]["Logic Description"] = "Overfishing of key predators, particularly those that control sea urchin populations, can lead to trophic cascades, resulting in urchin overgrazing and the loss of kelp forests in the North Atlantic."
kelp_forests_north_atlantic["Overfishing"]["Impact Function"] = "impact_overfishing_kelp_north_atlantic"

kelp_forests_north_atlantic["Coastal Development"]["Metric"] = "Area of coastline developed; shoreline armoring (e.g., seawalls); proximity of development to kelp forests."
kelp_forests_north_atlantic["Coastal Development"]["Data Sources"] = [
"Government planning data.",
"Remote sensing data.",
"Coastal zone management agencies."
]
kelp_forests_north_atlantic["Coastal Development"]["Impact on Area"] = "Habitat loss; increased runoff and pollution; altered sediment transport."
kelp_forests_north_atlantic["Coastal Development"]["Impact on Biodiversity"] = "Impacts on kelp forests and associated species due to habitat loss, reduced water quality, and increased disturbance."
kelp_forests_north_atlantic["Coastal Development"]["Influenced By"] = [
"Population Growth",
"Urbanization",
"Tourism",
"Industrial Development"
]
kelp_forests_north_atlantic["Coastal Development"]["Influences"] = [
"Kelp Forests (North Atlantic) - Water Quality",
"Kelp Forests (North Atlantic) - Habitat Loss"
]
kelp_forests_north_atlantic["Coastal Development"]["Logic Description"] = "Coastal development leads to habitat loss, increased runoff, and pollution, negatively affecting North Atlantic kelp forests."
kelp_forests_north_atlantic["Coastal Development"]["Impact Function"] = "impact_coastal_development_kelp_north_atlantic"

kelp_forests_north_atlantic["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., nutrients, sediments, heavy metals, plastics) in coastal waters."
kelp_forests_north_atlantic["Pollution"]["Data Sources"] = [
"Water quality monitoring programs (government agencies, research institutions).",
"Research studies."
]
kelp_forests_north_atlantic["Pollution"]["Impact on Area"] = "Reduced water quality; increased turbidity; potential for toxic effects."
kelp_forests_north_atlantic["Pollution"]["Impact on Biodiversity"] = "Impacts on kelp growth and survival; impacts on other marine organisms; bioaccumulation of toxins."
kelp_forests_north_atlantic["Pollution"]["Influenced By"] = [
"Urban Runoff",
"Industrial Discharge",
"Agricultural Runoff",
"Wastewater Treatment Plants",
"Shipping Activities"
]
kelp_forests_north_atlantic["Pollution"]["Influences"] = [
"Kelp Forests (North Atlantic) - Water Quality",
"Kelp Forests (North Atlantic) - Kelp Health"
]
kelp_forests_north_atlantic["Pollution"]["Logic Description"] = "Pollution from a variety of sources degrades water quality and can harm kelp forests and associated organisms in the North Atlantic."
kelp_forests_north_atlantic["Pollution"]["Impact Function"] = "impact_pollution_kelp_north_atlantic"

kelp_forests_north_atlantic["Invasive Species"]["Metric"] = "Distribution and abundance of key invasive species (e.g., *Codium fragile* ssp. *fragile*, *Membranipora membranacea*, *Didemnum vexillum*)."
kelp_forests_north_atlantic["Invasive Species"]["Data Sources"] = [
"Marine monitoring programs.",
"Research studies.",
"Citizen science initiatives."
]
kelp_forests_north_atlantic["Invasive Species"]["Impact on Area"] = "Competition with native kelp species; alteration of habitat structure; fouling of kelp blades."
kelp_forests_north_atlantic["Invasive Species"]["Impact on Biodiversity"] = "Can outcompete native species; alter community structure; impacts on associated species."
kelp_forests_north_atlantic["Invasive Species"]["Influenced By"] = [
"Shipping (ballast water, hull fouling).",
"Aquaculture",
"Climate Change (may favor some invasives)"
]
kelp_forests_north_atlantic["Invasive Species"]["Influences"] = [
"Kelp Forests (North Atlantic) - Native Species",
"Kelp Forests (North Atlantic) - Ecosystem Structure"
]
kelp_forests_north_atlantic["Invasive Species"]["Logic Description"] = "Invasive species, including seaweeds, invertebrates, and tunicates, can negatively impact North Atlantic kelp forests by competing with native species, altering habitat structure, and fouling kelp."
kelp_forests_north_atlantic["Invasive Species"]["Impact Function"] = "impact_invasive_species_kelp_north_atlantic"

kelp_forests_north_atlantic["Ocean Acidification"]["Metric"] = "Ocean pH; aragonite and calcite saturation states."
kelp_forests_north_atlantic["Ocean Acidification"]["Data Sources"] = [
"Oceanographic monitoring data.",
"Research studies.",
"Models."
]
kelp_forests_north_atlantic["Ocean Acidification"]["Impact on Area"] = "Potential impacts on calcifying organisms associated with kelp forests (e.g., coralline algae, shellfish)."
kelp_forests_north_atlantic["Ocean Acidification"]["Impact on Biodiversity"] = "May indirectly affect kelp by altering competitive interactions or impacting associated species.  Direct effects on the dominant kelp species are less clear than for some other calcifying organisms."
kelp_forests_north_atlantic["Ocean Acidification"]["Influenced By"] = [
"Global Carbon Dioxide Emissions"
]
kelp_forests_north_atlantic["Ocean Acidification"]["Influences"] = [
"Kelp Forests (North Atlantic) - Calcifying Organisms"
]
kelp_forests_north_atlantic["Ocean Acidification"]["Logic Description"] = "Ocean acidification, while a global threat, may have more indirect impacts on North Atlantic kelp forests by affecting associated calcifying organisms, rather than directly impacting the dominant kelp species."
kelp_forests_north_atlantic["Ocean Acidification"]["Impact Function"] = "impact_ocean_acidification_kelp_north_atlantic"

# --- Kelp Forests (Pacific Northwest) ---
kelp_forests_pacific_northwest = all_stressors_data["Pacific Northwest Kelp Forests"]

kelp_forests_pacific_northwest["Climate Change"]["Metric"] = "Sea surface temperature (SST); frequency and severity of marine heatwaves; upwelling intensity; El Niño-Southern Oscillation (ENSO) events."
kelp_forests_pacific_northwest["Climate Change"]["Data Sources"] = [
"NOAA National Centers for Environmental Information (NCEI).",
"Fisheries and Oceans Canada.",
"Climate models.",
"Research publications."
]
kelp_forests_pacific_northwest["Climate Change"]["Impact on Area"] = "Reduced kelp growth and survival; potential for die-offs; changes in kelp distribution."
kelp_forests_pacific_northwest["Climate Change"]["Impact on Biodiversity"] = "Loss of kelp forest habitat; shifts in species distributions; changes in community structure; reduced resilience to other stressors."
kelp_forests_pacific_northwest["Climate Change"]["Influenced By"] = [
"Global Greenhouse Gas Emissions",
"Changes in Ocean Circulation Patterns",
"ENSO Variability"
]
kelp_forests_pacific_northwest["Climate Change"]["Influences"] = [
"Kelp Forests (Pacific Northwest) - Marine Heatwaves",
"Kelp Forests (Pacific Northwest) - Ocean Acidification",
"Kelp Forests (Pacific Northwest) - Upwelling Patterns",
"Kelp Forests (Pacific Northwest) - Range Shifts"
]
kelp_forests_pacific_northwest["Climate Change"]["Logic Description"] = "Pacific Northwest kelp forests are sensitive to climate change, particularly to warming waters, marine heatwaves, and changes in upwelling, which affect nutrient availability."
kelp_forests_pacific_northwest["Climate Change"]["Impact Function"] = "impact_climate_change_kelp_pacific_northwest"

kelp_forests_pacific_northwest["Overgrazing"]["Metric"] = "Sea urchin density (number per square meter); kelp cover (percentage); sea otter abundance."
kelp_forests_pacific_northwest["Overgrazing"]["Data Sources"] = [
"Underwater surveys.",
"Research studies.",
"Government monitoring"
]
kelp_forests_pacific_northwest["Overgrazing"]["Impact on Area"] = "Conversion of kelp forests to urchin barrens."
kelp_forests_pacific_northwest["Overgrazing"]["Impact on Biodiversity"] = "Loss of kelp forest habitat; reduced biodiversity and ecosystem complexity."
kelp_forests_pacific_northwest["Overgrazing"]["Influenced By"] = [
"Kelp Forests (Pacific Northwest) - Fishing (removal of urchin predators like sea otters, sheephead, and lobsters).",
"Kelp Forests (Pacific Northwest) - Climate Change (warming can favor urchins).",
"Disease Outbreaks (can affect urchin populations)."
]
kelp_forests_pacific_northwest["Overgrazing"]["Influences"] = [
"Kelp Forests (Pacific Northwest) - Urchin Barrens Formation"
]
kelp_forests_pacific_northwest["Overgrazing"]["Logic Description"] = "The sea otter/urchin/kelp dynamic is crucial. Where sea otters are present and healthy, urchin populations are generally controlled. Where otters are absent or reduced, urchin barrens can form."
kelp_forests_pacific_northwest["Overgrazing"]["Impact Function"] = "impact_overgrazing_kelp_pacific_northwest"

kelp_forests_pacific_northwest["Pollution"]["Metric"] = "Concentrations of pollutants (nutrients, sediments, etc.)."
kelp_forests_pacific_northwest["Pollution"]["Data Sources"] = [
"Water Quality monitoring",
"Research studies"
]
kelp_forests_pacific_northwest["Pollution"]["Impact on Area"] = "Reduced water quality"
kelp_forests_pacific_northwest["Pollution"]["Impact on Biodiversity"] = "Can harm kelp and other organisms."
kelp_forests_pacific_northwest["Pollution"]["Influenced By"] = [
"Runoff",
"Industrial discharge"
]
kelp_forests_pacific_northwest["Pollution"]["Influences"] = [
"Kelp Forests (Pacific Northwest) - Water Quality",
"Kelp Forests (Pacific Northwest) - Kelp Health"
]
kelp_forests_pacific_northwest["Pollution"]["Logic Description"] = "Pollution from various sources."
kelp_forests_pacific_northwest["Pollution"]["Impact Function"] = "impact_pollution_kelp_pacific_northwest"

kelp_forests_pacific_northwest["Coastal Development"]["Metric"] = "Area of coastline developed; shoreline armoring."
kelp_forests_pacific_northwest["Coastal Development"]["Data Sources"] = [
"Government planning data.",
"Remote sensing data."
]
kelp_forests_pacific_northwest["Coastal Development"]["Impact on Area"] = "Habitat loss; increased runoff and pollution."
kelp_forests_pacific_northwest["Coastal Development"]["Impact on Biodiversity"] = "Impacts on kelp forests and associated species."
kelp_forests_pacific_northwest["Coastal Development"]["Influenced By"] = [
"Population Growth",
"Urbanization",
"Tourism"
]
kelp_forests_pacific_northwest["Coastal Development"]["Influences"] = [
"Kelp Forests (Pacific Northwest) - Water Quality",
"Kelp Forests (Pacific Northwest) - Habitat Loss"
]
kelp_forests_pacific_northwest["Coastal Development"]["Logic Description"] = "Coastal development can lead to habitat loss and increased pollution."
kelp_forests_pacific_northwest["Coastal Development"]["Impact Function"] = "impact_coastal_development_kelp_pacific_northwest"

kelp_forests_pacific_northwest["Ocean Acidification"]["Metric"] = "Ocean pH; aragonite saturation state."
kelp_forests_pacific_northwest["Ocean Acidification"]["Data Sources"] = ["Oceanographic monitoring data; research studies; models."]
kelp_forests_pacific_northwest["Ocean Acidification"]["Impact on Area"] = "May indirectly affect kelp by impacting other species, particularly calcifying organisms."
kelp_forests_pacific_northwest["Ocean Acidification"]["Impact on Biodiversity"] = "Potential negative impacts on calcifying organisms that are part of the kelp forest ecosystem, including some urchins and shellfish."
kelp_forests_pacific_northwest["Ocean Acidification"]["Influenced By"] = ["Global Carbon Dioxide Emissions; Upwelling Intensity"]
kelp_forests_pacific_northwest["Ocean Acidification"]["Influences"] = ["Kelp Forests (Pacific Northwest) - Calcifying Organisms"]
kelp_forests_pacific_northwest["Ocean Acidification"]["Logic Description"] = "Ocean acidification, intensified by upwelling, could negatively impact calcifying organisms in the kelp forest food web."
kelp_forests_pacific_northwest["Ocean Acidification"]["Impact Function"] = "impact_ocean_acidification_kelp_pacific_northwest"

kelp_forests_pacific_northwest["Fishing"]["Metric"] = "Fishing effort and catch of key species (rockfish, urchin predators)."
kelp_forests_pacific_northwest["Fishing"]["Data Sources"] = ["Fisheries management agencies", "Research surveys"]
kelp_forests_pacific_northwest["Fishing"]["Impact on Area"] = "Indirect, through food web effects."
kelp_forests_pacific_northwest["Fishing"]["Impact on Biodiversity"] = "Removal of urchin predators can trigger trophic cascades leading to urchin barrens and kelp loss."
kelp_forests_pacific_northwest["Fishing"]["Influenced By"] = ["Fishing regulations, market demand."]
kelp_forests_pacific_northwest["Fishing"]["Influences"] = ["Kelp Forests (Pacific Northwest) - Overgrazing"]
kelp_forests_pacific_northwest["Fishing"]["Logic Description"] = "Overfishing of urchin predators can exacerbate urchin grazing pressure."
kelp_forests_pacific_northwest["Fishing"]["Impact Function"] = "impact_fishing_kelp_pacific_northwest"

# --- Kelp Forests (South American) ---
kelp_forests_south_american = all_stressors_data["South American Kelp Forests"]

kelp_forests_south_american["Climate Change"]["Metric"] = "Sea surface temperature (SST); frequency and intensity of marine heatwaves; changes in upwelling patterns; ocean acidification."
kelp_forests_south_american["Climate Change"]["Data Sources"] = [
"Climate models.",
"Oceanographic data (from Chilean and Argentinian research institutions).",
"Research publications."
]
kelp_forests_south_american["Climate Change"]["Impact on Area"] = "Potential for changes in kelp distribution and abundance; increased stress on kelp."
kelp_forests_south_american["Climate Change"]["Impact on Biodiversity"] = "Shifts in species distributions; impacts on associated species; reduced resilience to other stressors."
kelp_forests_south_american["Climate Change"]["Influenced By"] = ["Global GHG"]
kelp_forests_south_american["Climate Change"]["Influences"] = [
"Kelp Forests (South American) - Ocean Acidification",
"Kelp Forests (South American) - Upwelling Patterns"
]
kelp_forests_south_american["Climate Change"]["Logic Description"] = "Climate change, including warming waters, acidification, and altered upwelling, can impact South American kelp forests."
kelp_forests_south_american["Climate Change"]["Impact Function"] = "impact_climate_change_kelp_south_american"

kelp_forests_south_american["Overfishing"]["Metric"] = "Fishing effort and catch of key species (e.g., fish that prey on sea urchins, or that compete with kelp for resources); sea urchin density; kelp cover."
kelp_forests_south_american["Overfishing"]["Data Sources"] = [
"Fisheries data (Chile and Argentina).",
"Underwater surveys.",
"Research publications."
]
kelp_forests_south_american["Overfishing"]["Impact on Area"] = "Potential for trophic cascades leading to urchin barrens (if key predators are removed)."
kelp_forests_south_american["Overfishing"]["Impact on Biodiversity"] = "Removal of key predators can lead to increased sea urchin grazing and kelp forest loss.; Changes in fish community structure."
kelp_forests_south_american["Overfishing"]["Influenced By"] = [
"Fishing Pressure",
"Fisheries Management Practices"
]
kelp_forests_south_american["Overfishing"]["Influences"] = [
"Kelp Forests (South American) - Overgrazing (by urchins)",
"Kelp Forests (South American) - Trophic Cascades"
]
kelp_forests_south_american["Overfishing"]["Logic Description"] = "Overfishing of species that prey on sea urchins can lead to increased urchin grazing pressure and the loss of kelp forests."
kelp_forests_south_american["Overfishing"]["Impact Function"] = "impact_overfishing_kelp_south_american"

kelp_forests_south_american["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., nutrients, heavy metals, pesticides) in coastal waters."
kelp_forests_south_american["Pollution"]["Data Sources"] = [
"Water quality monitoring data.",
"Research studies."
]
kelp_forests_south_american["Pollution"]["Impact on Area"] = "Reduced water quality; potential for toxic effects."
kelp_forests_south_american["Pollution"]["Impact on Biodiversity"] = "Impacts on kelp growth and survival; impacts on other marine organisms."
kelp_forests_south_american["Pollution"]["Influenced By"] = [
"Coastal Development",
"Industrial Discharge",
"Agricultural Runoff",
"Mining Activities (in some regions)"
]
kelp_forests_south_american["Pollution"]["Influences"] = [
"Kelp Forests (South American) - Water Quality",
"Kelp Forests (South American) - Kelp Health"
]
kelp_forests_south_american["Pollution"]["Logic Description"] = "Pollution from various sources can negatively impact water quality and kelp forest health."
kelp_forests_south_american["Pollution"]["Impact Function"] = "impact_pollution_kelp_south_american"

kelp_forests_south_american["Coastal Development"]["Metric"] = "Area of coastline developed; infrastructure development (e.g., ports, aquaculture facilities)."
kelp_forests_south_american["Coastal Development"]["Data Sources"] = [
"Government data (Chile, Argentina).",
"Remote sensing data.",
"Research publications."
]
kelp_forests_south_american["Coastal Development"]["Impact on Area"] = "Habitat loss; increased runoff and pollution."
kelp_forests_south_american["Coastal Development"]["Impact on Biodiversity"] = "Impacts on kelp forests and associated species due to habitat loss, reduced water quality, and increased disturbance."
kelp_forests_south_american["Coastal Development"]["Influenced By"] = [
"Economic Development",
"Population Growth",
"Aquaculture Expansion"
]
kelp_forests_south_american["Coastal Development"]["Influences"] = [
"Kelp Forests (South American) - Water Quality",
"Kelp Forests (South American) - Habitat Loss"
]
kelp_forests_south_american["Coastal Development"]["Logic Description"] = "Coastal development can lead to habitat loss and increased pollution, impacting nearby kelp forests."
kelp_forests_south_american["Coastal Development"]["Impact Function"] = "impact_coastal_development_kelp_south_american"

kelp_forests_south_american["Sea Urchin Harvesting"]["Metric"] = "Catch of sea urchins (tonnes/year); sea urchin density in harvested and unharvested areas."
kelp_forests_south_american["Sea Urchin Harvesting"]["Data Sources"] = [
"Fisheries data (Chile and Argentina).",
"Research studies."
]
kelp_forests_south_american["Sea Urchin Harvesting"]["Impact on Area"] = "Can potentially reduce grazing pressure on kelp (positive impact on kelp) *if* harvesting is intense enough. Can also be negative, if unregulated"
kelp_forests_south_american["Sea Urchin Harvesting"]["Impact on Biodiversity"] = "Impacts on sea urchin populations; potential for complex effects on kelp forest community structure (can be positive or negative depending on context)."
kelp_forests_south_american["Sea Urchin Harvesting"]["Influenced By"] = [
"Market Demand for Sea Urchins (roe - 'uni')",
"Fisheries Management Practices"
]
kelp_forests_south_american["Sea Urchin Harvesting"]["Influences"] = [
"Kelp Forests (South American) - Overgrazing"
]
kelp_forests_south_american["Sea Urchin Harvesting"]["Logic Description"] = "Sea urchin harvesting, primarily for their roe (uni), can have complex effects on kelp forest ecosystems.  In some cases, it can reduce grazing pressure on kelp, while in others, it can disrupt natural predator-prey relationships."
kelp_forests_south_american["Sea Urchin Harvesting"]["Impact Function"] = "impact_sea_urchin_harvesting_kelp_south_american"

kelp_forests_south_american["Invasive Species"]["Metric"] = "Distribution and abundance of invasive species."
kelp_forests_south_american["Invasive Species"]["Data Sources"] = [
"Research Studies"
]
kelp_forests_south_american["Invasive Species"]["Impact on Area"] = "Changes in community structure."
kelp_forests_south_american["Invasive Species"]["Impact on Biodiversity"] = "Impacts native kelp."
kelp_forests_south_american["Invasive Species"]["Influenced By"] = [
"Human Activities"
]
kelp_forests_south_american["Invasive Species"]["Influences"] = [
"Kelp Forests (South American) - Native Species"
]
kelp_forests_south_american["Invasive Species"]["Logic Description"] = "Invasive species impact on kelp forests"
kelp_forests_south_american["Invasive Species"]["Impact Function"] = "impact_invasive_species_kelp_south_american"

# --- Aquatic (Lake Baikal) ---
lake_baikal = all_stressors_data["Lake Baikal"]

lake_baikal["Climate Change"]["Metric"] = "Water temperature increase (°C); changes in ice cover duration and thickness; changes in stratification patterns; changes in precipitation."
lake_baikal["Climate Change"]["Data Sources"] = [
"Limnological Institute of the Siberian Branch of the Russian Academy of Sciences (LIN SB RAS) - long-term monitoring data.",
"Research publications.",
"Climate models.",
"Historical records."
]
lake_baikal["Climate Change"]["Impact on Area"] = "Warming water temperatures; reduced ice cover duration; altered mixing regimes; potential changes in lake level."
lake_baikal["Climate Change"]["Impact on Biodiversity"] = "Impacts on endemic species (e.g., Baikal seal, omul fish, Epischura baikalensis (a key zooplankton species)).; Shifts in species distributions.; Potential for increased algal blooms.; Changes in food web structure."
lake_baikal["Climate Change"]["Influenced By"] = ["Global Greenhouse Gas Emissions"]
lake_baikal["Climate Change"]["Influences"] = [
"Aquatic (Lake Baikal) - Water Temperature",
"Aquatic (Lake Baikal) - Ice Cover",
"Aquatic (Lake Baikal) - Stratification",
"Aquatic (Lake Baikal) - Eutrophication"
]
lake_baikal["Climate Change"]["Logic Description"] = "Lake Baikal is warming at a rate faster than the global average, leading to reduced ice cover, altered stratification patterns, and potential impacts on its unique endemic biodiversity."
lake_baikal["Climate Change"]["Impact Function"] = "impact_climate_change_lake_baikal"

lake_baikal["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., nutrients, heavy metals, organic pollutants, microplastics) in water, sediments, and biota."
lake_baikal["Pollution"]["Data Sources"] = [
"Limnological Institute SB RAS monitoring data.",
"Research publications.",
"Russian government environmental monitoring data (limited)."
]
lake_baikal["Pollution"]["Impact on Area"] = "Localized pollution hotspots, particularly near industrial areas and settlements."
lake_baikal["Pollution"]["Impact on Biodiversity"] = "Toxic effects on aquatic organisms; bioaccumulation of pollutants; impacts on endemic species."
lake_baikal["Pollution"]["Influenced By"] = [
"Industrial Discharge (historically, the Baikal Pulp and Paper Mill was a major source).",
"Wastewater from Settlements",
"Atmospheric Deposition",
"Tourism"
]
lake_baikal["Pollution"]["Influences"] = [
"Aquatic (Lake Baikal) - Water Quality",
"Aquatic (Lake Baikal) - Wildlife Health"
]
lake_baikal["Pollution"]["Logic Description"] = "Pollution from industrial sources, wastewater, and atmospheric deposition threatens Lake Baikal's water quality and unique biodiversity. The Baikal Pulp and Paper Mill was a major historical source, and although it closed, legacy pollution remains."
lake_baikal["Pollution"]["Impact Function"] = "impact_pollution_lake_baikal"

lake_baikal["Eutrophication"]["Metric"] = "Nutrient concentrations (nitrogen, phosphorus); chlorophyll-a concentrations; algal bloom frequency."
lake_baikal["Eutrophication"]["Data Sources"] = [
"Limnological Institute SB RAS monitoring data.",
"Research publications."
]
lake_baikal["Eutrophication"]["Impact on Area"] = "Localized increases in algal growth, particularly in coastal areas."
lake_baikal["Eutrophication"]["Impact on Biodiversity"] = "Potential for changes in phytoplankton communities; impacts on food webs; concerns about harmful algal blooms (though less common than in many other lakes)."
lake_baikal["Eutrophication"]["Influenced By"] = [
"Wastewater Discharge",
"Agricultural Runoff (limited in the immediate vicinity, but potentially from more distant sources)",
"Aquatic (Lake Baikal) - Climate Change (warming waters can exacerbate nutrient impacts)"
]
lake_baikal["Eutrophication"]["Influences"] = [
"Aquatic (Lake Baikal) - Water Quality",
"Aquatic (Lake Baikal) - Algal Blooms"
]
lake_baikal["Eutrophication"]["Logic Description"] = "While Lake Baikal is generally oligotrophic (nutrient-poor), localized eutrophication due to wastewater discharge and other sources is a concern."
lake_baikal["Eutrophication"]["Impact Function"] = "impact_eutrophication_lake_baikal"

lake_baikal["Overexploitation"]["Metric"] = "Catch data for commercially important fish species (e.g., omul); population estimates of key species."
lake_baikal["Overexploitation"]["Data Sources"] = [
"Fisheries data (Russian government).",
"Research studies."
]
lake_baikal["Overexploitation"]["Impact on Area"] = "Not directly applicable (affects fish populations)."
lake_baikal["Overexploitation"]["Impact on Biodiversity"] = "Decline of commercially important fish stocks (e.g., omul); potential impacts on the food web."
lake_baikal["Overexploitation"]["Influenced By"] = [
"Fishing Pressure (legal and illegal)",
"Lack of Effective Fisheries Management"
]
lake_baikal["Overexploitation"]["Influences"] = [
"Aquatic (Lake Baikal) - Fish Populations"
]
lake_baikal["Overexploitation"]["Logic Description"] = "Overfishing, particularly of the endemic omul, has been a concern in the past, and sustainable fisheries management is crucial."
lake_baikal["Overexploitation"]["Impact Function"] = "impact_overexploitation_lake_baikal"

lake_baikal["Invasive Species"]["Metric"] = "Distribution and abundance of non-native aquatic species."
lake_baikal["Invasive Species"]["Data Sources"] = [
"Limnological Institute SB RAS monitoring data.",
"Research publications."
]
lake_baikal["Invasive Species"]["Impact on Area"] = "Potential for changes in species composition and ecosystem structure."
lake_baikal["Invasive Species"]["Impact on Biodiversity"] = "Competition with native species; predation on native species; potential for disruption of the food web."
lake_baikal["Invasive Species"]["Influenced By"] = [
"Ballast Water Discharge (from ships in the Selenga River and other connected waterways).",
"Climate Change (may favor some invasives)"
]
lake_baikal["Invasive Species"]["Influences"] = [
"Aquatic (Lake Baikal) - Native Species"
]
lake_baikal["Invasive Species"]["Logic Description"] = "While Lake Baikal has relatively few established invasive species compared to some other large lakes, the risk of new introductions remains a concern."
lake_baikal["Invasive Species"]["Impact Function"] = "impact_invasive_species_lake_baikal"

lake_baikal["Tourism"]["Metric"] = "Number of tourists visiting Lake Baikal; development of tourism infrastructure."
lake_baikal["Tourism"]["Data Sources"] = [
"Tourism statistics (Russian government).",
"Research studies."
]
lake_baikal["Tourism"]["Impact on Area"] = "Localized impacts on shoreline habitats; increased pollution (waste, sewage); disturbance to wildlife."
lake_baikal["Tourism"]["Impact on Biodiversity"] = "Disturbance to wildlife (e.g., Baikal seals); potential for introduction of invasive species; habitat degradation."
lake_baikal["Tourism"]["Influenced By"] = [
"Economic Development",
"Accessibility",
"Marketing and Promotion"
]
lake_baikal["Tourism"]["Influences"] = [
"Aquatic (Lake Baikal) - Pollution",
"Aquatic (Lake Baikal) - Wildlife Disturbance"
]
lake_baikal["Tourism"]["Logic Description"] = "Increasing tourism, while economically beneficial, puts pressure on Lake Baikal's fragile ecosystems, particularly through pollution, waste generation, and disturbance to wildlife."
lake_baikal["Tourism"]["Impact Function"] = "impact_tourism_lake_baikal"

# --- Mangroves (Australian) ---
mangroves_australian = all_stressors_data["Australian Mangroves"]

mangroves_australian["Climate Change"]["Metric"] = "Sea level rise (mm/year); sea surface temperature (°C); changes in precipitation (mm/year, seasonality); increased storm intensity and frequency; ocean acidification (pH)."
mangroves_australian["Climate Change"]["Data Sources"] = [
"Australian Bureau of Meteorology (BOM) data.",
"CSIRO research.",
"Climate models (global and regional).",
"IPCC reports.",
"Tide gauge records."
]
mangroves_australian["Climate Change"]["Impact on Area"] = "Coastal inundation and erosion due to sea level rise; changes in mangrove distribution and extent; increased damage from storms."
mangroves_australian["Climate Change"]["Impact on Biodiversity"] = "Loss of mangrove habitat; shifts in mangrove species distributions; increased stress on mangroves and associated fauna; potential impacts on fish, birds, and invertebrates that depend on mangroves."
mangroves_australian["Climate Change"]["Influenced By"] = [
"Global Greenhouse Gas Emissions"
]
mangroves_australian["Climate Change"]["Influences"] = [
"Mangroves (Australian) - Sea Level Rise",
"Mangroves (Australian) - Coastal Erosion",
"Mangroves (Australian) - Storm Damage",
"Mangroves (Australian) - Ocean Acidification"
]
mangroves_australian["Climate Change"]["Logic Description"] = "Climate change, particularly sea level rise, poses a major threat to Australian mangroves. Increased storm intensity, altered rainfall patterns, and ocean acidification also have significant impacts."
mangroves_australian["Climate Change"]["Impact Function"] = "impact_climate_change_mangroves_australian"

mangroves_australian["Coastal Development"]["Metric"] = "Area of mangroves cleared or degraded due to coastal development (ha/year); infrastructure development (ports, roads, urban expansion)."
mangroves_australian["Coastal Development"]["Data Sources"] = [
"Remote sensing data (satellite imagery).",
"Government planning documents (state and local).",
"Environmental impact assessments."
]
mangroves_australian["Coastal Development"]["Impact on Area"] = "Direct loss of mangrove habitat; fragmentation; altered hydrology."
mangroves_australian["Coastal Development"]["Impact on Biodiversity"] = "Habitat loss for many species; reduced nursery grounds for fish and shellfish; loss of coastal protection (mangroves buffer against storms and erosion)."
mangroves_australian["Coastal Development"]["Influenced By"] = [
"Population Growth",
"Urbanization",
"Tourism Development",
"Industrial Development (ports, mining)"
]
mangroves_australian["Coastal Development"]["Influences"] = [
"Mangroves (Australian) - Habitat Loss",
"Mangroves (Australian) - Water Quality",
"Mangroves (Australian) - Coastal Erosion"
]
mangroves_australian["Coastal Development"]["Logic Description"] = "Coastal development, including urban expansion, infrastructure projects, and tourism development, can lead to the direct loss and degradation of mangrove habitats."
mangroves_australian["Coastal Development"]["Impact Function"] = "impact_coastal_development_mangroves_australian"

mangroves_australian["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., nutrients, heavy metals, pesticides, plastics) in water, sediment, and mangrove tissues."
mangroves_australian["Pollution"]["Data Sources"] = [
"Water quality monitoring programs (state and federal agencies).",
"Research studies.",
"Environmental monitoring reports."
]
mangroves_australian["Pollution"]["Impact on Area"] = "Degradation of water and sediment quality; potential impacts on mangrove health."
mangroves_australian["Pollution"]["Impact on Biodiversity"] = "Toxic effects on mangroves and associated fauna; eutrophication (nutrient enrichment); impacts on food webs; plastic pollution entanglement and ingestion."
mangroves_australian["Pollution"]["Influenced By"] = [
"Agricultural Runoff",
"Urban Runoff",
"Industrial Discharge",
"Mining Activities",
"Shipping and Ports"
]
mangroves_australian["Pollution"]["Influences"] = [
"Mangroves (Australian) - Water Quality",
"Mangroves (Australian) - Mangrove Health"
]
mangroves_australian["Pollution"]["Logic Description"] = "Pollution from various sources, including agriculture, urban runoff, industry, and mining, can degrade water quality and impact mangrove ecosystems."
mangroves_australian["Pollution"]["Impact Function"] = "impact_pollution_mangroves_australian"

mangroves_australian["Altered Hydrology"]["Metric"] = "Changes in freshwater inflow; changes in tidal regimes; construction of canals, bunds, and other structures that alter water flow."
mangroves_australian["Altered Hydrology"]["Data Sources"] = [
"Hydrological data (river flow, tidal data).",
"Remote sensing data.",
"Research studies."
]
mangroves_australian["Altered Hydrology"]["Impact on Area"] = "Changes in salinity gradients; altered inundation patterns; changes in sediment deposition."
mangroves_australian["Altered Hydrology"]["Impact on Biodiversity"] = "Impacts on mangrove growth and survival; shifts in mangrove species distributions; changes in habitat suitability for associated fauna."
mangroves_australian["Altered Hydrology"]["Influenced By"] = [
"Upstream Water Diversions (e.g., for agriculture or urban water supply)",
"Coastal Development",
"Climate Change (changes in rainfall and sea level)",
"Construction of canals, bunds, and other structures"
]
mangroves_australian["Altered Hydrology"]["Influences"] = [
"Mangroves (Australian) - Salinity",
"Mangroves (Australian) - Sedimentation",
"Mangroves (Australian) - Habitat Suitability"
]
mangroves_australian["Altered Hydrology"]["Logic Description"] = "Changes in freshwater inflow, tidal regimes, and water flow patterns, due to upstream water diversions, coastal development, and climate change, can significantly impact mangrove ecosystems."
mangroves_australian["Altered Hydrology"]["Impact Function"] = "impact_altered_hydrology_mangroves_australian"

mangroves_australian["Overexploitation"]["Metric"] = "Harvesting rates of mangrove timber, fish, crabs, and other resources."
mangroves_australian["Overexploitation"]["Data Sources"] = [
"Fisheries data.",
"Forestry data (where available).",
"Research studies."
]
mangroves_australian["Overexploitation"]["Impact on Area"] = "Potential for localized degradation of mangrove forests (if timber harvesting is unsustainable)."
mangroves_australian["Overexploitation"]["Impact on Biodiversity"] = "Decline of targeted species (e.g., fish, crabs); impacts on food webs."
mangroves_australian["Overexploitation"]["Influenced By"] = [
"Local Demand for Resources",
"Commercial Exploitation (in some areas)",
"Lack of Enforcement of Regulations"
]
mangroves_australian["Overexploitation"]["Influences"] = [
"Mangroves (Australian) - Resource Availability"
]
mangroves_australian["Overexploitation"]["Logic Description"] = "Overexploitation of mangrove resources, such as timber, fish, and crabs, can lead to resource depletion and ecosystem degradation."
mangroves_australian["Overexploitation"]["Impact Function"] = "impact_overexploitation_mangroves_australian"

# --- Mangroves (East African) ---
mangroves_east_african = all_stressors_data["East African Mangroves"]

mangroves_east_african["Climate Change"]["Metric"] = "Sea level rise (mm/year); sea surface temperature (°C); changes in precipitation; increased storm intensity/frequency; ocean acidification."
mangroves_east_african["Climate Change"]["Data Sources"] = [
"IPCC reports.",
"Climate models.",
"Regional climate studies (East Africa).",
"Tide gauge data.",
"Research publications."
]
mangroves_east_african["Climate Change"]["Impact on Area"] = "Coastal inundation and erosion (sea level rise); changes in mangrove distribution; increased storm damage."
mangroves_east_african["Climate Change"]["Impact on Biodiversity"] = "Loss of mangrove habitat; shifts in species distributions; increased stress on mangroves and associated fauna."
mangroves_east_african["Climate Change"]["Influenced By"] = ["Global Greenhouse Gas Emissions"]
mangroves_east_african["Climate Change"]["Influences"] = [
"Mangroves (East African) - Sea Level Rise",
"Mangroves (East African) - Coastal Erosion",
"Mangroves (East African) - Storm Damage",
"Mangroves (East African) - Ocean Acidification"
]
mangroves_east_african["Climate Change"]["Logic Description"] = "Climate change is a major threat to East African mangroves, particularly through sea level rise, increased storm intensity, and changes in precipitation patterns."
mangroves_east_african["Climate Change"]["Impact Function"] = "impact_climate_change_mangroves_east_african"

mangroves_east_african["Coastal Development"]["Metric"] = "Area of mangroves cleared for development (ha/year); infrastructure projects (ports, roads, aquaculture)."
mangroves_east_african["Coastal Development"]["Data Sources"] = [
"Remote sensing data.",
"Government planning documents.",
"Environmental impact assessments.",
"Research publications."
]
mangroves_east_african["Coastal Development"]["Impact on Area"] = "Direct loss of mangrove habitat; fragmentation; altered hydrology."
mangroves_east_african["Coastal Development"]["Impact on Biodiversity"] = "Habitat loss; reduced nursery grounds for fish; loss of coastal protection."
mangroves_east_african["Coastal Development"]["Influenced By"] = [
"Population Growth",
"Urbanization",
"Tourism Development",
"Aquaculture Expansion",
"Industrial Development"
]
mangroves_east_african["Coastal Development"]["Influences"] = [
"Mangroves (East African) - Habitat Loss",
"Mangroves (East African) - Water Quality",
"Mangroves (East African) - Coastal Erosion"
]
mangroves_east_african["Coastal Development"]["Logic Description"] = "Coastal development leads to the direct loss and degradation of mangrove habitats in East Africa."
mangroves_east_african["Coastal Development"]["Impact Function"] = "impact_coastal_development_mangroves_east_african"

mangroves_east_african["Pollution"]["Metric"] = "Concentrations of pollutants (nutrients, heavy metals, pesticides, plastics) in water and sediments."
mangroves_east_african["Pollution"]["Data Sources"] = [
"Water quality monitoring data.",
"Research studies."
]
mangroves_east_african["Pollution"]["Impact on Area"] = "Degradation of water and sediment quality; potential impacts on mangrove health."
mangroves_east_african["Pollution"]["Impact on Biodiversity"] = "Toxic effects on mangroves and fauna; eutrophication; impacts on food webs; plastic pollution."
mangroves_east_african["Pollution"]["Influenced By"] = [
"Agricultural Runoff",
"Urban Runoff",
"Industrial Discharge",
"Sewage Discharge",
"Mining Activities"
]
mangroves_east_african["Pollution"]["Influences"] = [
"Mangroves (East African) - Water Quality",
"Mangroves (East African) - Mangrove Health"
]
mangroves_east_african["Pollution"]["Logic Description"] = "Pollution from agriculture, urban areas, industry, and sewage discharge degrades water quality and impacts East African mangrove ecosystems."
mangroves_east_african["Pollution"]["Impact Function"] = "impact_pollution_mangroves_east_african"

mangroves_east_african["Overexploitation"]["Metric"] = "Harvesting rates of mangrove timber; catch data for fish, crabs, and other mangrove-associated species."
mangroves_east_african["Overexploitation"]["Data Sources"] = [
"Forestry data (if available).",
"Fisheries data.",
"Local community surveys.",
"Research studies."
]
mangroves_east_african["Overexploitation"]["Impact on Area"] = "Loss of mangrove trees (if timber harvesting is unsustainable); reduced structural complexity."
mangroves_east_african["Overexploitation"]["Impact on Biodiversity"] = "Decline in targeted species (fish, crabs, shellfish); impacts on food webs; loss of habitat structure."
mangroves_east_african["Overexploitation"]["Influenced By"] = [
"Local Demand for Wood (fuelwood, construction)",
"Commercial Exploitation (e.g., for export)",
"Poverty and Lack of Alternative Livelihoods",
"Lack of Enforcement of Regulations"
]
mangroves_east_african["Overexploitation"]["Influences"] = [
"Mangroves (East African) - Resource Availability",
"Mangroves (East African) - Habitat Structure"
]
mangroves_east_african["Overexploitation"]["Logic Description"] = "Overexploitation of mangrove resources, particularly for timber and fisheries, is a significant threat in many parts of East Africa, driven by local demand, commercial interests, and poverty."
mangroves_east_african["Overexploitation"]["Impact Function"] = "impact_overexploitation_mangroves_east_african"

mangroves_east_african["Altered Hydrology"]["Metric"] = "Changes in freshwater inflow; changes in tidal regimes; construction of dams, canals, or other structures that alter water flow."
mangroves_east_african["Altered Hydrology"]["Data Sources"] = [
"Hydrological data (river flow, tidal data).",
"Remote sensing data.",
"Research studies."
]
mangroves_east_african["Altered Hydrology"]["Impact on Area"] = "Changes in salinity gradients; altered inundation patterns; changes in sediment deposition."
mangroves_east_african["Altered Hydrology"]["Impact on Biodiversity"] = "Impacts on mangrove growth and survival; shifts in mangrove species distributions; changes in habitat suitability for associated fauna."
mangroves_east_african["Altered Hydrology"]["Influenced By"] = [
"Upstream Water Diversions (for agriculture or other uses)",
"Coastal Development",
"Dam Construction",
"Climate Change (changes in rainfall)"
]
mangroves_east_african["Altered Hydrology"]["Influences"] = [
"Mangroves (East African) - Salinity",
"Mangroves (East African) - Sedimentation",
"Mangroves (East African) - Habitat Suitability"
]
mangroves_east_african["Altered Hydrology"]["Logic Description"] = "Changes in freshwater inflow and tidal regimes, often due to upstream water diversions, dam construction, or coastal development, can significantly impact mangrove ecosystems in East Africa."
mangroves_east_african["Altered Hydrology"]["Impact Function"] = "impact_altered_hydrology_mangroves_east_african"

# --- Mangroves (Mesoamerican) ---
mangroves_mesoamerican = all_stressors_data["Mesoamerican Mangroves"]

mangroves_mesoamerican["Coastal Development"]["Metric"] = "Area of mangroves converted to tourism infrastructure, urban areas, aquaculture ponds, or other development (ha/year)."
mangroves_mesoamerican["Coastal Development"]["Data Sources"] = [
"Remote sensing data.",
"Government planning and development records (Mexico, Belize, Guatemala, Honduras).",
"Research publications.",
"NGO reports."
]
mangroves_mesoamerican["Coastal Development"]["Impact on Area"] = "*Extensive* loss of mangrove habitat; fragmentation; altered hydrology."
mangroves_mesoamerican["Coastal Development"]["Impact on Biodiversity"] = "Loss of habitat for a wide range of species; reduced nursery grounds for fish and shellfish; loss of coastal protection; reduced carbon sequestration."
mangroves_mesoamerican["Coastal Development"]["Influenced By"] = [
"Tourism Development: A *major* driver, particularly in areas like the Riviera Maya.",
"Aquaculture Expansion (shrimp farming).",
"Urbanization and Population Growth.",
"Infrastructure Development (ports, roads)."
]
mangroves_mesoamerican["Coastal Development"]["Influences"] = [
"Mangroves (Mesoamerican) - Habitat Loss",
"Mangroves (Mesoamerican) - Water Quality",
"Mangroves (Mesoamerican) - Coastal Erosion"
]
mangroves_mesoamerican["Coastal Development"]["Logic Description"] = "Coastal development, particularly for tourism and aquaculture, is a *dominant* threat to Mesoamerican mangroves, leading to widespread habitat loss and degradation."
mangroves_mesoamerican["Coastal Development"]["Impact Function"] = "impact_coastal_development_mangroves_mesoamerican"

mangroves_mesoamerican["Pollution"]["Metric"] = "Concentrations of pollutants (nutrients, pesticides, heavy metals, plastics) in water, sediment, and mangrove tissues."
mangroves_mesoamerican["Pollution"]["Data Sources"] = [
"Water quality monitoring data (often limited).",
"Research studies."
]
mangroves_mesoamerican["Pollution"]["Impact on Area"] = "Degradation of water and sediment quality."
mangroves_mesoamerican["Pollution"]["Impact on Biodiversity"] = "Toxic effects on mangroves and associated fauna; eutrophication; impacts on food webs; plastic pollution."
mangroves_mesoamerican["Pollution"]["Influenced By"] = [
"Agricultural Runoff (fertilizers, pesticides).",
"Urban Runoff (sewage, industrial effluent).",
"Aquaculture Effluent",
"Tourism Activities"
]
mangroves_mesoamerican["Pollution"]["Influences"] = [
"Mangroves (Mesoamerican) - Water Quality",
"Mangroves (Mesoamerican) - Mangrove Health"
]
mangroves_mesoamerican["Pollution"]["Logic Description"] = "Pollution from agriculture, urban areas, tourism, and aquaculture degrades water quality and impacts mangrove ecosystems."
mangroves_mesoamerican["Pollution"]["Impact Function"] = "impact_pollution_mangroves_mesoamerican"

mangroves_mesoamerican["Climate Change"]["Metric"] = "Sea level rise (mm/year); sea surface temperature (°C); changes in precipitation patterns; increased storm intensity."
mangroves_mesoamerican["Climate Change"]["Data Sources"] = [
"Climate models.",
"Tide gauge records.",
"Remote sensing data.",
"Research publications."
]
mangroves_mesoamerican["Climate Change"]["Impact on Area"] = "Coastal inundation and erosion; changes in salinity; increased storm damage."
mangroves_mesoamerican["Climate Change"]["Impact on Biodiversity"] = "Loss of mangrove habitat; shifts in species distributions; increased stress on mangroves and associated fauna."
mangroves_mesoamerican["Climate Change"]["Influenced By"] = ["Global GHG"]
mangroves_mesoamerican["Climate Change"]["Influences"] = [
"Mangroves (Mesoamerican) - Sea Level Rise",
"Mangroves (Mesoamerican) - Coastal Erosion",
"Mangroves (Mesoamerican) - Storm Damage"
]
mangroves_mesoamerican["Climate Change"]["Logic Description"] = "Climate change, particularly sea level rise and increased storm intensity, poses a major threat to Mesoamerican mangroves."
mangroves_mesoamerican["Climate Change"]["Impact Function"] = "impact_climate_change_mangroves_mesoamerican"

mangroves_mesoamerican["Overexploitation"]["Metric"] = "Harvesting rates of mangrove timber, fish, crabs, and other resources."
mangroves_mesoamerican["Overexploitation"]["Data Sources"] = [
"Fisheries data (often limited).",
"Forestry data (often limited).",
"Research studies."
]
mangroves_mesoamerican["Overexploitation"]["Impact on Area"] = "Localized degradation of mangrove forests (if timber harvesting is unsustainable)."
mangroves_mesoamerican["Overexploitation"]["Impact on Biodiversity"] = "Decline of targeted species (fish, crabs, shellfish); impacts on food webs."
mangroves_mesoamerican["Overexploitation"]["Influenced By"] = [
"Local Demand for Resources",
"Poverty and Lack of Alternative Livelihoods",
"Weak Enforcement of Regulations"
]
mangroves_mesoamerican["Overexploitation"]["Influences"] = [
"Mangroves (Mesoamerican) - Resource Availability"
]
mangroves_mesoamerican["Overexploitation"]["Logic Description"] = "Overexploitation of mangrove resources, such as timber and fisheries, can lead to localized degradation and resource depletion."
mangroves_mesoamerican["Overexploitation"]["Impact Function"] = "impact_overexploitation_mangroves_mesoamerican"

mangroves_mesoamerican["Deforestation"]["Metric"] = "Area of mangroves cleared per year (ha/year) (for various purposes)."
mangroves_mesoamerican["Deforestation"]["Data Sources"] = [
"Remote sensing data.",
"Government reports (Mexico, Belize, Guatemala, Honduras).",
"Research publications."
]
mangroves_mesoamerican["Deforestation"]["Impact on Area"] = "Direct loss of mangrove habitat; fragmentation."
mangroves_mesoamerican["Deforestation"]["Impact on Biodiversity"] = "Habitat loss; reduced nursery grounds for fish; loss of coastal protection; carbon emissions."
mangroves_mesoamerican["Deforestation"]["Influenced By"] = [
"Mangroves (Mesoamerican) - Coastal Development",
"Aquaculture Expansion",
"Agriculture",
"Fuelwood Collection"
]
mangroves_mesoamerican["Deforestation"]["Influences"] = [
"Mangroves (Mesoamerican) - Habitat Loss",
"Mangroves (Mesoamerican) - Coastal Erosion"
]
mangroves_mesoamerican["Deforestation"]["Logic Description"] = "Deforestation, driven by coastal development, aquaculture, agriculture, and other factors, is a major threat to Mesoamerican mangroves."
mangroves_mesoamerican["Deforestation"]["Impact Function"] = "impact_deforestation_mangroves_mesoamerican"

mangroves_mesoamerican["Altered Hydrology"]["Metric"] = "Changes in freshwater inflow; changes in tidal regimes."
mangroves_mesoamerican["Altered Hydrology"]["Data Sources"] = [
"Hydrological data (river flow, tidal data).",
"Remote sensing data.",
"Research studies."
]
mangroves_mesoamerican["Altered Hydrology"]["Impact on Area"] = "Changes in salinity gradients; altered inundation patterns."
mangroves_mesoamerican["Altered Hydrology"]["Impact on Biodiversity"] = "Impacts on mangrove growth and survival; shifts in species distributions."
mangroves_mesoamerican["Altered Hydrology"]["Influenced By"] = [
"Upstream Water Diversions",
"Coastal Development",
"Climate Change (changes in rainfall and sea level)"
]
mangroves_mesoamerican["Altered Hydrology"]["Influences"] = [
"Mangroves (Mesoamerican) - Salinity",
"Mangroves (Mesoamerican) - Habitat Suitability"
]
mangroves_mesoamerican["Altered Hydrology"]["Logic Description"] = "Changes in freshwater inflow and tidal regimes, often due to upstream water diversions and coastal development, can impact mangrove ecosystems."
mangroves_mesoamerican["Altered Hydrology"]["Impact Function"] = "impact_altered_hydrology_mangroves_mesoamerican"

# --- Mangroves (Southeast Asian) ---
mangroves_southeast_asian = all_stressors_data["Southeast Asian Mangroves"]

mangroves_southeast_asian["Coastal Development"]["Metric"] = "Area of mangroves converted to urban areas, infrastructure, or other development (ha/year)."
mangroves_southeast_asian["Coastal Development"]["Data Sources"] = [
"Remote sensing data.",
"Government statistics (Indonesia, Malaysia, Thailand, Philippines, Vietnam, etc.).",
"Research publications.",
"Land-use planning documents."
]
mangroves_southeast_asian["Coastal Development"]["Impact on Area"] = "Direct loss of mangrove habitat; fragmentation; altered hydrology."
mangroves_southeast_asian["Coastal Development"]["Impact on Biodiversity"] = "Loss of habitat; reduced nursery grounds for fish and shellfish; loss of coastal protection; reduced carbon sequestration."
mangroves_southeast_asian["Coastal Development"]["Influenced By"] = [
"Population Growth",
"Urbanization",
"Tourism Development",
"Industrial Development (ports, etc.)"
]
mangroves_southeast_asian["Coastal Development"]["Influences"] = [
"Mangroves (Southeast Asian) - Habitat Loss",
"Mangroves (Southeast Asian) - Water Quality",
"Mangroves (Southeast Asian) - Coastal Erosion"
]
mangroves_southeast_asian["Coastal Development"]["Logic Description"] = "Coastal development, driven by population growth, urbanization, tourism, and industrial expansion, is a significant threat to mangroves in Southeast Asia."
mangroves_southeast_asian["Coastal Development"]["Impact Function"] = "impact_coastal_development_mangroves_southeast_asian"

mangroves_southeast_asian["Aquaculture Expansion"]["Metric"] = "Area of mangroves converted to aquaculture ponds (primarily shrimp and fish farms) (ha/year)."
mangroves_southeast_asian["Aquaculture Expansion"]["Data Sources"] = [
"Remote sensing data.",
"Government statistics (aquaculture production).",
"Research publications.",
"NGO reports."
]
mangroves_southeast_asian["Aquaculture Expansion"]["Impact on Area"] = "*Major* driver of mangrove loss in Southeast Asia; direct conversion of mangrove habitat."
mangroves_southeast_asian["Aquaculture Expansion"]["Impact on Biodiversity"] = "Loss of habitat; reduced nursery grounds for fish and shellfish; water pollution from aquaculture effluent; loss of coastal protection and carbon sequestration."
mangroves_southeast_asian["Aquaculture Expansion"]["Influenced By"] = [
"Global Demand for Shrimp and Fish",
"Economic Incentives (profitability of aquaculture)",
"Government Policies (promotion of aquaculture in some countries)",
"Land Availability"
]
mangroves_southeast_asian["Aquaculture Expansion"]["Influences"] = [
"Mangroves (Southeast Asian) - Habitat Loss",
"Mangroves (Southeast Asian) - Deforestation",
"Mangroves (Southeast Asian) - Water Pollution"
]
mangroves_southeast_asian["Aquaculture Expansion"]["Logic Description"] = "Aquaculture expansion, particularly shrimp farming, is the *single largest driver* of mangrove loss in Southeast Asia, with devastating consequences for biodiversity and ecosystem services."
mangroves_southeast_asian["Aquaculture Expansion"]["Impact Function"] = "impact_aquaculture_expansion_mangroves_southeast_asian"

mangroves_southeast_asian["Deforestation"]["Metric"] = "Area of mangroves cleared per year (ha/year) (for timber, charcoal, and other land uses)."
mangroves_southeast_asian["Deforestation"]["Data Sources"] = [
"Remote sensing data.",
"Forestry data (often limited).",
"Research publications.",
"NGO reports."
]
mangroves_southeast_asian["Deforestation"]["Impact on Area"] = "Direct loss of mangrove habitat."
mangroves_southeast_asian["Deforestation"]["Impact on Biodiversity"] = "Habitat loss; reduced nursery grounds; loss of coastal protection; carbon emissions."
mangroves_southeast_asian["Deforestation"]["Influenced By"] = [
"Demand for Timber and Charcoal",
"Mangroves (Southeast Asian) - Coastal Development",
"Mangroves (Southeast Asian) - Aquaculture Expansion",
"Population Growth",
"Poverty and Lack of Alternative Livelihoods"
]
mangroves_southeast_asian["Deforestation"]["Influences"] = [
"Mangroves (Southeast Asian) - Habitat Loss",
"Mangroves (Southeast Asian) - Coastal Erosion"
]
mangroves_southeast_asian["Deforestation"]["Logic Description"] = "Deforestation, driven by multiple factors including coastal development, aquaculture, and demand for wood products, contributes to significant mangrove loss in Southeast Asia."
mangroves_southeast_asian["Deforestation"]["Impact Function"] = "impact_deforestation_mangroves_southeast_asian"

mangroves_southeast_asian["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., nutrients, heavy metals, pesticides, plastics) in water, sediment, and mangrove tissues."
mangroves_southeast_asian["Pollution"]["Data Sources"] = [
"Water quality monitoring data (often limited).",
"Research studies.",
"Reports from environmental agencies."
]
mangroves_southeast_asian["Pollution"]["Impact on Area"] = "Degradation of water and sediment quality; potential impacts on mangrove health."
mangroves_southeast_asian["Pollution"]["Impact on Biodiversity"] = "Toxic effects on mangroves and associated fauna; eutrophication; impacts on food webs; plastic pollution."
mangroves_southeast_asian["Pollution"]["Influenced By"] = [
"Agricultural Runoff",
"Urban Runoff",
"Industrial Discharge",
"Aquaculture Effluent",
"Mangroves (Southeast Asian) - Deforestation (increased erosion)"
]
mangroves_southeast_asian["Pollution"]["Influences"] = [
"Mangroves (Southeast Asian) - Water Quality",
"Mangroves (Southeast Asian) - Mangrove Health"
]
mangroves_southeast_asian["Pollution"]["Logic Description"] = "Pollution from agriculture, urban areas, industry, aquaculture, and deforestation degrades water quality and impacts mangrove ecosystems."
mangroves_southeast_asian["Pollution"]["Impact Function"] = "impact_pollution_mangroves_southeast_asian"

mangroves_southeast_asian["Climate Change"]["Metric"] = "Sea level rise (mm/year); sea surface temperature (°C); changes in precipitation patterns; increased storm intensity."
mangroves_southeast_asian["Climate Change"]["Data Sources"] = [
"Climate models.",
"Tide gauge records.",
"Remote sensing data.",
"Research publications."
]
mangroves_southeast_asian["Climate Change"]["Impact on Area"] = "Coastal inundation and erosion due to sea level rise; changes in salinity; increased damage from storms."
mangroves_southeast_asian["Climate Change"]["Impact on Biodiversity"] = "Loss of mangrove habitat; shifts in species distributions; increased stress on mangroves and associated fauna."
mangroves_southeast_asian["Climate Change"]["Influenced By"] = [
"Global Greenhouse Gas Emissions"
]
mangroves_southeast_asian["Climate Change"]["Influences"] = [
"Mangroves (Southeast Asian) - Sea Level Rise",
"Mangroves (Southeast Asian) - Coastal Erosion",
"Mangroves (Southeast Asian) - Storm Damage"
]
mangroves_southeast_asian["Climate Change"]["Logic Description"] = "Climate change, particularly sea level rise and increased storm intensity, poses a major threat to Southeast Asian mangroves."
mangroves_southeast_asian["Climate Change"]["Impact Function"] = "impact_climate_change_mangroves_southeast_asian"

mangroves_southeast_asian["Overexploitation"]["Metric"] = "Harvesting rates of fish, crabs, shellfish, and other mangrove-associated species; timber harvesting rates."
mangroves_southeast_asian["Overexploitation"]["Data Sources"] = [
"Fisheries data (often limited).",
"Forestry data (often limited).",
"Research studies."
]
mangroves_southeast_asian["Overexploitation"]["Impact on Area"] = "Potential for localized degradation of mangrove forests (if timber harvesting is unsustainable)."
mangroves_southeast_asian["Overexploitation"]["Impact on Biodiversity"] = "Decline of targeted species (fish, crabs, shellfish); impacts on food webs."
mangroves_southeast_asian["Overexploitation"]["Influenced By"] = [
"Local Demand for Resources",
"Commercial Exploitation (in some areas)",
"Poverty and Lack of Alternative Livelihoods"
]
mangroves_southeast_asian["Overexploitation"]["Influences"] = [
"Mangroves (Southeast Asian) - Resource Availability"
]
mangroves_southeast_asian["Overexploitation"]["Logic Description"] = "Overexploitation of mangrove resources, including fisheries and timber, can lead to resource depletion and ecosystem degradation."
mangroves_southeast_asian["Overexploitation"]["Impact Function"] = "impact_overexploitation_mangroves_southeast_asian"

mangroves_southeast_asian["Sedimentation"]["Metric"] = "Changes in sediment delivery to mangrove areas; increased turbidity."
mangroves_southeast_asian["Sedimentation"]["Data Sources"] = [
"Research Studies",
"Remote sensing (for turbidity).",
"Hydrological data."
]
mangroves_southeast_asian["Sedimentation"]["Impact on Area"] = "Can be positive (providing sediment for mangrove growth) or negative (smothering mangroves if excessive)."
mangroves_southeast_asian["Sedimentation"]["Impact on Biodiversity"] = "Can impact mangrove growth and survival; can affect associated species."
mangroves_southeast_asian["Sedimentation"]["Influenced By"] = [
"Mangroves (Southeast Asian) - Deforestation (in upstream areas)",
"Upstream Dam Construction (which can *reduce* sediment delivery)",
"Coastal Development",
"Mining Activities"
]
mangroves_southeast_asian["Sedimentation"]["Influences"] = [
"Mangroves (Southeast Asian) - Water Quality",
"Mangroves (Southeast Asian) - Mangrove Growth"
]
mangroves_southeast_asian["Sedimentation"]["Logic Description"] = "Changes in sediment delivery to mangrove areas, either increases (due to deforestation and erosion) or decreases (due to dams), can significantly impact mangrove ecosystems."
mangroves_southeast_asian["Sedimentation"]["Impact Function"] = "impact_sedimentation_mangroves_southeast_asian"

# --- Mangroves (Sundarbans) ---
sundarbans = all_stressors_data["Sundarbans Mangroves"]

sundarbans["Sea Level Rise"]["Metric"] = "Relative sea level rise (mm/year); rate of land subsidence (mm/year)."
sundarbans["Sea Level Rise"]["Data Sources"] = [
"Tide gauge data (from Bangladesh and India).",
"Satellite altimetry.",
"Research studies on subsidence.",
"IPCC reports."
]
sundarbans["Sea Level Rise"]["Impact on Area"] = "Major loss of land area due to inundation. The Sundarbans is *extremely* vulnerable to sea level rise.; Increased salinity intrusion into freshwater areas.;Coastal Erosion"
sundarbans["Sea Level Rise"]["Impact on Biodiversity"] = "Loss of mangrove habitat (mangroves are the defining feature of the Sundarbans).; Impacts on the Bengal tiger population (loss of habitat, increased human-wildlife conflict).; Impacts on other wildlife (e.g., deer, crocodiles, birds, fish).; Changes in species distributions."
sundarbans["Sea Level Rise"]["Influenced By"] = [
"Mangroves (Sundarbans) - Climate Change",
"Local Land Subsidence" #Not Defined - need template
]
sundarbans["Sea Level Rise"]["Influences"] = [
"Mangroves (Sundarbans) - Salinity Intrusion",
"Mangroves (Sundarbans) - Habitat Availability",
"Mangroves (Sundarbans) - Coastal Erosion"
]
sundarbans["Sea Level Rise"]["Logic Description"] = "The Sundarbans, a low-lying delta region, is one of the most vulnerable places on Earth to sea level rise.  Inundation and increased salinity are major threats to the mangrove ecosystem and its biodiversity."
sundarbans["Sea Level Rise"]["Impact Function"] = "impact_sea_level_rise_sundarbans"

sundarbans["Salinity Intrusion"]["Metric"] = "Salinity levels in water and soil (parts per thousand - ppt)."
sundarbans["Salinity Intrusion"]["Data Sources"] = [
"Water quality monitoring data (Bangladesh and India).",
"Research studies."
]
sundarbans["Salinity Intrusion"]["Impact on Area"] = "Changes in the distribution of different mangrove species (some are more salt-tolerant than others)."
sundarbans["Salinity Intrusion"]["Impact on Biodiversity"] = "Impacts on freshwater-dependent species.; Changes in plant communities.; Impacts on fisheries."
sundarbans["Salinity Intrusion"]["Influenced By"] = [
"Mangroves (Sundarbans) - Sea Level Rise",
"Mangroves (Sundarbans) - Reduced Freshwater Flow",
"Mangroves (Sundarbans) - Climate Change"
]
sundarbans["Salinity Intrusion"]["Influences"] = [
"Mangroves (Sundarbans) - Water Quality",
"Mangroves (Sundarbans) - Habitat Availability",
"Mangroves (Sundarbans) - Freshwater Availability"
]
sundarbans["Salinity Intrusion"]["Logic Description"] = "Sea level rise and reduced freshwater flow from rivers lead to increased salinity intrusion, impacting both the mangrove ecosystem and human populations who depend on freshwater resources."
sundarbans["Salinity Intrusion"]["Impact Function"] = "impact_salinity_intrusion_sundarbans"

sundarbans["Climate Change"]["Metric"] = "Temperature increase; changes in precipitation; cyclone frequency/intensity."
sundarbans["Climate Change"]["Data Sources"] = [
"Climate models.",
"Historical weather records."
]
sundarbans["Climate Change"]["Impact on Area"] = "Indirect - sea level rise, cyclones, altered rainfall."
sundarbans["Climate Change"]["Impact on Biodiversity"] = "Increased stress, species shifts."
sundarbans["Climate Change"]["Influenced By"] = [
"Global GHG"
]
sundarbans["Climate Change"]["Influences"] = [
"Mangroves (Sundarbans) - Sea Level Rise",
"Mangroves (Sundarbans) - Cyclone Frequency and Intensity",
"Mangroves (Sundarbans) - Reduced Freshwater Flow"
]
sundarbans["Climate Change"]["Logic Description"] = "Climate change drives sea level rise, more intense cyclones, and altered rainfall patterns, all major threats to the Sundarbans."
sundarbans["Climate Change"]["Impact Function"] = "impact_climate_change_sundarbans"

sundarbans["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., heavy metals, oil, plastics) in water, sediment, and biota."
sundarbans["Pollution"]["Data Sources"] = [
"Water quality monitoring data.",
"Research studies."
]
sundarbans["Pollution"]["Impact on Area"] = "Degradation of water quality."
sundarbans["Pollution"]["Impact on Biodiversity"] = "Toxic effects on wildlife.; Impacts on fisheries.; Impacts on human health."
sundarbans["Pollution"]["Influenced By"] = [
"Industrial Discharge (from India and Bangladesh)",
"Shipping Activities (oil spills and discharge)",
"Agricultural Runoff",
"Untreated Sewage",
"Tourism"
]
sundarbans["Pollution"]["Influences"] = [
"Mangroves (Sundarbans) - Water Quality",
"Mangroves (Sundarbans) - Wildlife Health"
]
sundarbans["Pollution"]["Logic Description"] = "Pollution from industrial discharge, shipping, agriculture, and sewage degrades water quality, harming wildlife and impacting human health."
sundarbans["Pollution"]["Impact Function"] = "impact_pollution_sundarbans"

sundarbans["Overexploitation of Resources"]["Metric"] = "Fish catches; timber harvesting rates; honey collection rates."
sundarbans["Overexploitation of Resources"]["Data Sources"] = [
"Fisheries data.",
"Forestry data.",
"Research studies."
]
sundarbans["Overexploitation of Resources"]["Impact on Area"] = "Depletion of natural resources."
sundarbans["Overexploitation of Resources"]["Impact on Biodiversity"] = "Decline in fish populations.; Loss of mangrove trees (due to illegal logging).; Impacts on wildlife that depend on those resources."
sundarbans["Overexploitation of Resources"]["Influenced By"] = [
"Population growth",
"Poverty",
"Lack of alternative livelihoods"
]
sundarbans["Overexploitation of Resources"]["Influences"] = [
"Mangroves (Sundarbans) - Resource Availability"
]
sundarbans["Overexploitation of Resources"]["Logic Description"] = "Unsustainable harvesting of fish, timber, and other resources depletes stocks and impacts the ecosystem."
sundarbans["Overexploitation of Resources"]["Impact Function"] = "impact_overexploitation_resources_sundarbans"

sundarbans["Cyclone Frequency and Intensity"]["Metric"] = "Number of cyclones making landfall; wind speeds; storm surge height."
sundarbans["Cyclone Frequency and Intensity"]["Data Sources"] = [
"Meteorological data (India and Bangladesh).",
"Historical records."
]
sundarbans["Cyclone Frequency and Intensity"]["Impact on Area"] = "Coastal erosion.; Flooding.; Damage to infrastructure.; Salinization."
sundarbans["Cyclone Frequency and Intensity"]["Impact on Biodiversity"] = "Damage to mangrove forests.; Wildlife mortality.; Habitat loss."
sundarbans["Cyclone Frequency and Intensity"]["Influenced By"] = [
"Mangroves (Sundarbans) - Climate Change"
]
sundarbans["Cyclone Frequency and Intensity"]["Influences"] = [
"Mangroves (Sundarbans) - Coastal Erosion"
]
sundarbans["Cyclone Frequency and Intensity"]["Logic Description"] = "The Sundarbans is highly vulnerable to cyclones, and climate change may increase their frequency and intensity. Cyclones cause widespread damage to infrastructure, ecosystems, and human communities."
sundarbans["Cyclone Frequency and Intensity"]["Impact Function"] = "impact_cyclone_frequency_intensity_sundarbans"

sundarbans["Reduced Freshwater Flow"]["Metric"] = "Water flow rates in the rivers that feed the Sundarbans (e.g., the Ganges)."
sundarbans["Reduced Freshwater Flow"]["Data Sources"] = ["Hydrological data (India and Bangladesh)."]
sundarbans["Reduced Freshwater Flow"]["Impact on Area"] = "Increased salinity intrusion; reduced sediment deposition (which helps maintain the delta)."
sundarbans["Reduced Freshwater Flow"]["Impact on Biodiversity"] = "Impacts on freshwater-dependent species; changes in plant communities."
sundarbans["Reduced Freshwater Flow"]["Influenced By"] = [
"Upstream water diversions and dams.",
"Mangroves (Sundarbans) - Climate Change"
]
sundarbans["Reduced Freshwater Flow"]["Influences"] = [
"Mangroves (Sundarbans) - Salinity Intrusion",
"Mangroves (Sundarbans) - Sedimentation"
]
sundarbans["Reduced Freshwater Flow"]["Logic Description"] = "Reduced freshwater flow, due to upstream water diversions and climate change, exacerbates salinity problems and affects sediment deposition in the Sundarbans."
sundarbans["Reduced Freshwater Flow"]["Impact Function"] = "impact_reduced_freshwater_flow_sundarbans"

# --- Aquatic (Open Ocean) ---
open_ocean = all_stressors_data["Open Ocean"] # Corrected variable name

open_ocean["Overfishing"]["Metric"] = "Fish catches (tonnes/year); fishing effort (e.g., number of vessels, days at sea); stock assessments (estimates of fish population size and biomass); bycatch (amount of non-target species caught)."
open_ocean["Overfishing"]["Data Sources"] = [
"Fisheries data (reported catches, often incomplete).",
"Stock assessments (conducted by regional fisheries management organizations - RFMOs - and national agencies).",
"Scientific research (e.g., using tagging studies to track fish movements).",
"Observer programs (placing observers on fishing vessels to monitor catches and bycatch)."
]
open_ocean["Overfishing"]["Impact on Area"] = "Not directly applicable (fishing occurs throughout the water column), but affects the entire ecosystem."
open_ocean["Overfishing"]["Impact on Biodiversity"] = "Depletion of fish stocks (target species and bycatch).; Changes in the structure of marine food webs (e.g., removal of top predators).; Impacts on seabirds, marine mammals, and sea turtles (through bycatch and competition for food).; Loss of genetic diversity within fish populations."
open_ocean["Overfishing"]["Influenced By"] = [
"Global Demand for Seafood",
"Fishing Technology",
"Subsidies",
"Illegal, Unreported, and Unregulated (IUU) Fishing",
"Weak Governance and Enforcement"
]
open_ocean["Overfishing"]["Influences"] = [
"Marine Food Webs",
"Ecosystem Functioning"
]
open_ocean["Overfishing"]["Logic Description"] = "Overfishing is a major threat to the open ocean, depleting fish stocks, altering food web structure, and impacting a wide range of marine species."
open_ocean["Overfishing"]["Impact Function"] = "impact_overfishing_open_ocean"

open_ocean["Climate Change"]["Metric"] = "Sea surface temperature (SST) (°C); ocean acidification (pH); changes in ocean currents; changes in stratification (layering of the water column); oxygen minimum zone expansion."
open_ocean["Climate Change"]["Data Sources"] = [
"Climate models.",
"Oceanographic data (buoys, ships, satellites).",
"Historical records."
]
open_ocean["Climate Change"]["Impact on Area"] = "Widespread changes in ocean conditions."
open_ocean["Climate Change"]["Impact on Biodiversity"] = "Shifts in species distributions (as species track suitable temperatures).; Increased stress on marine organisms (due to warming, acidification, and reduced oxygen).; Changes in phenology (timing of biological events).; Impacts on primary productivity (phytoplankton growth).; Increased frequency and intensity of marine heatwaves."
open_ocean["Climate Change"]["Influenced By"] = [
"Global Greenhouse Gas Emissions"
]
open_ocean["Climate Change"]["Influences"] = [
"Aquatic (Open Ocean) - Ocean Acidification",
"Aquatic (Open Ocean) - Ocean Currents",
"Aquatic (Open Ocean) - Stratification",
"Aquatic (Open Ocean) - Oxygen Minimum Zones"
]
open_ocean["Climate Change"]["Logic Description"] = "Climate change is causing widespread and fundamental changes to the open ocean, impacting temperature, acidity, currents, stratification, and oxygen levels, with cascading effects on marine life."
open_ocean["Climate Change"]["Impact Function"] = "impact_climate_change_open_ocean"

open_ocean["Plastic Pollution"]["Metric"] = "Concentrations of plastic debris (macroplastics, microplastics) in surface waters, the water column, and sediments; abundance of plastic ingested by marine organisms."
open_ocean["Plastic Pollution"]["Data Sources"] = [
"Surface water sampling (using nets).",
"Beach surveys.",
"Analysis of the stomach contents of marine animals.",
"Research studies."
]
open_ocean["Plastic Pollution"]["Impact on Area"] = "Widespread contamination of the ocean with plastic."
open_ocean["Plastic Pollution"]["Impact on Biodiversity"] = "Entanglement of marine animals (e.g., seabirds, turtles, marine mammals).; Ingestion of plastic by marine animals (leading to starvation, blockage of digestive tracts, and exposure to toxic chemicals).; Potential for microplastics to accumulate in the food chain.; Transport of invasive species (on plastic debris)."
open_ocean["Plastic Pollution"]["Influenced By"] = [
"Land-Based Sources",
"Shipping Activities",
"Fishing Gear"
]
open_ocean["Plastic Pollution"]["Influences"] = [
"Wildlife mortality"
]
open_ocean["Plastic Pollution"]["Logic Description"] = "Plastic pollution is a pervasive problem in the open ocean, impacting marine life through entanglement, ingestion, and the potential for toxic effects."
open_ocean["Plastic Pollution"]["Impact Function"] = "impact_plastic_pollution_open_ocean"

open_ocean["Chemical Pollution"]["Metric"] = "Concentrations of pollutants (e.g., heavy metals, persistent organic pollutants (POPs), oil) in seawater, sediments, and marine organisms."
open_ocean["Chemical Pollution"]["Data Sources"] = [
"Water quality monitoring programs.",
"Sediment analysis.",
"Analysis of tissues from marine organisms.",
"Research studies."
]
open_ocean["Chemical Pollution"]["Impact on Area"] = "Contamination of the ocean environment."
open_ocean["Chemical Pollution"]["Impact on Biodiversity"] = "Toxic effects on marine organisms (e.g., reproductive impairment, immune suppression).; Bioaccumulation of pollutants in the food chain (leading to higher concentrations in top predators)."
open_ocean["Chemical Pollution"]["Influenced By"] = [
"Industrial Discharge",
"Agricultural Runoff",
"Shipping Activities",
"Atmospheric Deposition"
]
open_ocean["Chemical Pollution"]["Influences"] = [
"Wildlife health"
]
open_ocean["Chemical Pollution"]["Logic Description"] = "Chemical pollution from various sources contaminates the open ocean, impacting marine life through toxic effects and bioaccumulation."
open_ocean["Chemical Pollution"]["Impact Function"] = "impact_chemical_pollution_open_ocean"

open_ocean["Noise Pollution"]["Metric"] = "Ambient noise levels; frequency and intensity of anthropogenic noise."
open_ocean["Noise Pollution"]["Data Sources"] = ["Hydrophones", "Research"]
open_ocean["Noise Pollution"]["Impact on Area"] = "Increased noise levels in the ocean."
open_ocean["Noise Pollution"]["Impact on Biodiversity"] = "Interference with communication; Behavioral changes.; Stress; Hearing damage (in extreme cases)."
open_ocean["Noise Pollution"]["Influenced By"] = [
"Shipping",
"Sonar",
"Seismic surveys",
"Construction"
]
open_ocean["Noise Pollution"]["Influences"] = [
"Marine mammal behavior and communication"
]
open_ocean["Noise Pollution"]["Logic Description"] = "Noise pollution from shipping, sonar, and other human activities can interfere with marine animal communication, navigation, and behavior."
open_ocean["Noise Pollution"]["Impact Function"] = "impact_noise_pollution_open_ocean"

# --- Rivers (Amazon) ---
rivers_amazon = all_stressors_data["Amazon Rivers"]

rivers_amazon["Deforestation"]["Metric"] = "Rate of deforestation in riparian zones and within the Amazon basin (ha/year)."
rivers_amazon["Deforestation"]["Data Sources"] = [
"Remote sensing data (satellite imagery).",
"Brazilian government data (INPE).",
"Research publications."
]
rivers_amazon["Deforestation"]["Impact on Area"] = "Increased sediment runoff into rivers.; Loss of riparian buffer zones."
rivers_amazon["Deforestation"]["Impact on Biodiversity"] = "Degradation of water quality.; Impacts on aquatic life (fish, invertebrates) due to increased sediment and reduced shade.; Loss of habitat for riparian species."
rivers_amazon["Deforestation"]["Influenced By"] = [
"Agriculture Expansion",
"Logging",
"Mining",
"Infrastructure Development"
]
rivers_amazon["Deforestation"]["Influences"] = [
"Rivers (Amazon) - Water Quality",
"Rivers (Amazon) - Sedimentation",
"Rivers (Amazon) - Riparian Habitat"
]
rivers_amazon["Deforestation"]["Logic Description"] = "Deforestation in the Amazon basin, particularly in riparian zones (areas along riverbanks), leads to increased soil erosion and sediment runoff into rivers, degrading water quality and impacting aquatic life."
rivers_amazon["Deforestation"]["Impact Function"] = "impact_deforestation_rivers_amazon"

rivers_amazon["Dam Construction"]["Metric"] = "Number of dams constructed or planned; change in river flow patterns; area of land inundated by reservoirs."
rivers_amazon["Dam Construction"]["Data Sources"] = [
"Government agencies (Brazil, Peru, Bolivia, etc.).",
"Energy company reports.",
"Research publications.",
"NGO reports."
]
rivers_amazon["Dam Construction"]["Impact on Area"] = "Major alteration of river flow; fragmentation of river ecosystems; inundation of large areas of land (including forests and human settlements).; Changes in sediment and nutrient transport downstream."
rivers_amazon["Dam Construction"]["Impact on Biodiversity"] = "Blockage of fish migration routes.; Loss of habitat for riverine species (e.g., river dolphins, turtles).; Changes in downstream ecosystems due to altered flow and sediment/nutrient delivery.; Impacts on aquatic invertebrates."
rivers_amazon["Dam Construction"]["Influenced By"] = [
"Energy Demand",
"Economic Development",
"Government Policies"
]
rivers_amazon["Dam Construction"]["Influences"] = [
"Rivers (Amazon) - River Flow",
"Rivers (Amazon) - Fish Migration",
"Rivers (Amazon) - Habitat Fragmentation",
"Rivers (Amazon) - Sedimentation"
]
rivers_amazon["Dam Construction"]["Logic Description"] = "Dam construction on the Amazon River and its tributaries is a major threat, fragmenting the river system, altering flow patterns, blocking fish migrations, and inundating large areas of land."
rivers_amazon["Dam Construction"]["Impact Function"] = "impact_dam_construction_rivers_amazon"

rivers_amazon["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., mercury, pesticides, sewage, industrial effluent) in water and sediments."
rivers_amazon["Pollution"]["Data Sources"] = [
"Water quality monitoring data (often limited).",
"Research studies.",
"NGO reports."
]
rivers_amazon["Pollution"]["Impact on Area"] = "Degradation of water quality."
rivers_amazon["Pollution"]["Impact on Biodiversity"] = "Toxic effects on aquatic organisms (e.g., mercury poisoning from gold mining).; Impacts on human health (through consumption of contaminated fish).; Eutrophication (from nutrient pollution)."
rivers_amazon["Pollution"]["Influenced By"] = [
"Mining (particularly gold mining).",
"Agriculture (pesticide and fertilizer runoff).",
"Untreated Sewage",
"Industrial Discharge",
"Rivers (Amazon) - Deforestation"
]
rivers_amazon["Pollution"]["Influences"] = [
"Rivers (Amazon) - Water Quality",
"Rivers (Amazon) - Aquatic Life",
"Rivers (Amazon) - Human Health"
]
rivers_amazon["Pollution"]["Logic Description"] = "Pollution from mining, agriculture, sewage, and industry degrades water quality in the Amazon River system, impacting aquatic life and human health."
rivers_amazon["Pollution"]["Impact Function"] = "impact_pollution_rivers_amazon"

rivers_amazon["Climate Change"]["Metric"] = "Changes in precipitation patterns; changes in river discharge; increased frequency and severity of droughts and floods."
rivers_amazon["Climate Change"]["Data Sources"] = [
"Climate models.",
"Hydrological data.",
"Research publications."
]
rivers_amazon["Climate Change"]["Impact on Area"] = "Altered river flow patterns; increased risk of floods and droughts."
rivers_amazon["Climate Change"]["Impact on Biodiversity"] = "Impacts on aquatic species due to changes in water availability and temperature.; Increased stress on freshwater ecosystems."
rivers_amazon["Climate Change"]["Influenced By"] = [
"Global Greenhouse Gas Emissions",
"Rivers (Amazon) - Deforestation (can affect regional rainfall)"
]
rivers_amazon["Climate Change"]["Influences"] = [
"Rivers (Amazon) - River Flow",
"Rivers (Amazon) - Water Temperature",
"Rivers (Amazon) - Flooding and Drought"
]
rivers_amazon["Climate Change"]["Logic Description"] = "Climate change is altering precipitation patterns in the Amazon basin, leading to changes in river flow, increased risk of floods and droughts, and impacts on aquatic ecosystems."
rivers_amazon["Climate Change"]["Impact Function"] = "impact_climate_change_rivers_amazon"

rivers_amazon["Overfishing"]["Metric"] = "Fish catches; fishing effort; stock assessments (if available)."
rivers_amazon["Overfishing"]["Data Sources"] = [
"Fisheries data (often limited).",
"Research studies."
]
rivers_amazon["Overfishing"]["Impact on Area"] = "Not directly area-based, but affects the entire river system."
rivers_amazon["Overfishing"]["Impact on Biodiversity"] = "Decline of commercially important fish species.; Impacts on food webs (e.g., removal of top predators).; Loss of genetic diversity within fish populations."
rivers_amazon["Overfishing"]["Influenced By"] = [
"Population Growth",
"Demand for Fish",
"Lack of Effective Fisheries Management"
]
rivers_amazon["Overfishing"]["Influences"] = [
"Rivers (Amazon) - Fish Populations",
"Rivers (Amazon) - Food Webs"
]
rivers_amazon["Overfishing"]["Logic Description"] = "Overfishing is a threat to the Amazon River's fish populations, impacting biodiversity and the livelihoods of people who depend on fishing."
rivers_amazon["Overfishing"]["Impact Function"] = "impact_overfishing_rivers_amazon"

rivers_amazon["Mining"]["Metric"] = "Number and size of mining operations (legal and illegal); concentrations of mining-related pollutants (e.g., mercury, cyanide) in water and sediments."
rivers_amazon["Mining"]["Data Sources"] = [
"Government data (often incomplete).",
"Remote sensing data.",
"Research studies.",
"NGO reports."
]
rivers_amazon["Mining"]["Impact on Area"] = "Localized but severe pollution of rivers.; Deforestation and habitat destruction."
rivers_amazon["Mining"]["Impact on Biodiversity"] = "Mercury poisoning of aquatic organisms and humans.; Habitat loss and degradation."
rivers_amazon["Mining"]["Influenced By"] = [
"Global Demand for Minerals (gold, etc.)",
"Lack of Enforcement of Environmental Regulations",
"Poverty and Lack of Alternative Livelihoods"
]
rivers_amazon["Mining"]["Influences"] = [
"Rivers (Amazon) - Pollution",
"Rivers (Amazon) - Deforestation",
"Rivers (Amazon) - Water Quality"
]
rivers_amazon["Mining"]["Logic Description"] = "Mining, particularly gold mining, is a major source of pollution in the Amazon River system, releasing mercury and other toxic substances into the water and causing deforestation."
rivers_amazon["Mining"]["Impact Function"] = "impact_mining_rivers_amazon"

# --- Rivers (Danube) ---
danube_river = all_stressors_data["Danube Rivers"]

danube_river["Altered Hydrology"]["Metric"] = "Changes in river flow (magnitude, timing, frequency); water levels; sediment transport; connectivity with floodplains."
danube_river["Altered Hydrology"]["Data Sources"] = [
    "International Commission for the Protection of the Danube River (ICPDR) data.",
    "National hydrological monitoring data (from countries along the Danube).",
"Research publications."
]
danube_river["Altered Hydrology"]["Impact on Area"] = "Changes in river morphology; reduced floodplain inundation; altered sediment dynamics."
danube_river["Altered Hydrology"]["Impact on Biodiversity"] = "Impacts on fish migration (dams are barriers); loss of spawning grounds; changes in aquatic habitats; impacts on floodplain ecosystems."
danube_river["Altered Hydrology"]["Influenced By"] = [
    "Dams and Reservoirs (numerous dams along the Danube and its tributaries)",
    "Channelization (for navigation and flood control)",
    "Water Abstraction (for irrigation, industry, and drinking water)",
    "Land-Use Change in the Catchment (e.g., deforestation)",
    "Rivers (Danube) - Climate Change"
]
danube_river["Altered Hydrology"]["Influences"] = [
    "Rivers (Danube) - Habitat Connectivity",
    "Rivers (Danube) - Fish Migration",
"Rivers (Danube) - Sedimentation",
    "Rivers (Danube) - Water Quality"
]
danube_river["Altered Hydrology"]["Logic Description"] = "The Danube River's hydrology has been significantly altered by dams, channelization, and water abstraction, impacting flow patterns, sediment transport, and connectivity with its floodplains."
danube_river["Altered Hydrology"]["Impact Function"] = "impact_altered_hydrology_danube_river"

danube_river["Pollution"]["Metric"] = "Concentrations of pollutants (nutrients, heavy metals, organic pollutants, pharmaceuticals, microplastics) in water, sediment, and biota."
danube_river["Pollution"]["Data Sources"] = [
    "ICPDR water quality monitoring data.",
"National monitoring programs (of countries along the Danube).",
    "Research publications."
]
danube_river["Pollution"]["Impact on Area"] = "Degradation of water quality; contamination of sediments; impacts on human water use."
danube_river["Pollution"]["Impact on Biodiversity"] = "Eutrophication (nutrient enrichment); toxic effects on aquatic organisms; bioaccumulation of pollutants in the food chain; impacts on sensitive species."
danube_river["Pollution"]["Influenced By"] = [
"Agricultural Runoff (fertilizers, pesticides)",
"Industrial Discharge",
"Municipal Wastewater (untreated or inadequately treated sewage)",
    "Mining Activities (in some parts of the basin)",
    "Shipping"
]
danube_river["Pollution"]["Influences"] = [
"Rivers (Danube) - Water Quality",
"Rivers (Danube) - Aquatic Life Health",
"Human Health (through water use and fish consumption)"
]
danube_river["Pollution"]["Logic Description"] = "The Danube River receives pollution from a wide range of sources throughout its large catchment area, including agriculture, industry, urban areas, and shipping. This pollution degrades water quality and impacts aquatic life."
danube_river["Pollution"]["Impact Function"] = "impact_pollution_danube_river"

danube_river["Navigation"]["Metric"] = "Shipping traffic density; dredging activities; construction of navigation infrastructure (locks, canals)."
danube_river["Navigation"]["Data Sources"] = [
"ICPDR data.",
    "National navigation authorities.",
    "Research publications."
]
danube_river["Navigation"]["Impact on Area"] = "Physical alteration of the river channel; increased turbidity (due to dredging); noise pollution."
danube_river["Navigation"]["Impact on Biodiversity"] = "Disturbance to aquatic habitats; impacts on fish and invertebrates from dredging; potential for introduction of invasive species through ballast water; noise pollution affecting fish and other aquatic life."
danube_river["Navigation"]["Influenced By"] = [
"International Agreements (on navigation on the Danube)",
    "Economic Development (trade and transport)",
    "EU Transport Policy"
]
danube_river["Navigation"]["Influences"] = [
    "Rivers (Danube) - Habitat Modification",
    "Rivers (Danube) - Water Quality (turbidity)",
    "Rivers (Danube) - Invasive Species"
]
danube_river["Navigation"]["Logic Description"] = "Navigation on the Danube River requires ongoing maintenance (dredging) and infrastructure development, which can have significant impacts on the river's ecology."
danube_river["Navigation"]["Impact Function"] = "impact_navigation_danube_river"

danube_river["Invasive Species"]["Metric"] = "Distribution and abundance of key invasive species (e.g., certain fish, mollusks, crustaceans)."
danube_river["Invasive Species"]["Data Sources"] = [
"Research studies.",
"Monitoring programs (often limited)."
]
danube_river["Invasive Species"]["Impact on Area"] = "Changes in species composition and food web structure."
danube_river["Invasive Species"]["Impact on Biodiversity"] = "Competition with native species; predation on native species; alteration of habitats."
danube_river["Invasive Species"]["Influenced By"] = [
"Shipping (ballast water)",
"Canals (connecting the Danube to other river systems)",
"Aquaculture (escaped fish)",
    "Rivers (Danube) - Climate Change"
]
danube_river["Invasive Species"]["Influences"] = [
"Rivers (Danube) - Native Species",
"Rivers (Danube) - Food Web Structure"
]
danube_river["Invasive Species"]["Logic Description"] = "Invasive species, often introduced through shipping and canals, are a growing threat to the Danube River's native biodiversity."
danube_river["Invasive Species"]["Impact Function"] = "impact_invasive_species_danube_river"

danube_river["Climate Change"]["Metric"] = "Changes in water temperature; changes in precipitation patterns; changes in river discharge; increased frequency of extreme events (floods and droughts)."
danube_river["Climate Change"]["Data Sources"] = [
"Climate models.",
"Historical records (temperature, precipitation, river flow).",
    "Research publications."
]
danube_river["Climate Change"]["Impact on Area"] = "Altered flow regimes; increased water temperatures; increased risk of floods and droughts."
danube_river["Climate Change"]["Impact on Biodiversity"] = "Shifts in species distributions; increased stress on aquatic organisms; impacts on fish spawning and migration."
danube_river["Climate Change"]["Influenced By"] = ["Global GHG"]
danube_river["Climate Change"]["Influences"] = [
"Rivers (Danube) - Water Temperature",
"Rivers (Danube) - River Flow",
"Rivers (Danube) - Extreme Events"
]
danube_river["Climate Change"]["Logic Description"] = "Climate change is impacting the Danube River through changes in temperature, precipitation, and river discharge, with consequences for aquatic ecosystems."
danube_river["Climate Change"]["Impact Function"] = "impact_climate_change_danube_river"

danube_river["Overfishing"]["Metric"] = "Fish catches (tonnes/year); fish population sizes and structure; fishing effort."
danube_river["Overfishing"]["Data Sources"] = [
"Fisheries data (often limited).",
"Research studies."
]
danube_river["Overfishing"]["Impact on Area"] = "Not directly applicable, but affects fish populations."
danube_river["Overfishing"]["Impact on Biodiversity"] = "Decline of fish stocks, particularly migratory species like sturgeon; changes in fish community structure."
danube_river["Overfishing"]["Influenced By"] = [
"Fishing Pressure (legal and illegal)",
"Lack of Effective Fisheries Management"
]
danube_river["Overfishing"]["Influences"] = [
"Rivers (Danube) - Fish Populations"
]
danube_river["Overfishing"]["Logic Description"] = "Overfishing is a threat to some fish species in the Danube, particularly sturgeon, which are highly vulnerable due to their late maturity and migratory behavior."
danube_river["Overfishing"]["Impact Function"] = "impact_overfishing_danube_river"

danube_river["Habitat Degradation"]["Metric"] = "Area of riverine and floodplain habitats lost or degraded (ha); changes in habitat quality."
danube_river["Habitat Degradation"]["Data Sources"] = [
"Remote sensing data.",
"Field surveys.",
"Research studies."
]
danube_river["Habitat Degradation"]["Impact on Area"] = "Loss of spawning grounds, nurseries, and feeding areas for fish and other aquatic life; reduced connectivity between habitats."
danube_river["Habitat Degradation"]["Impact on Biodiversity"] = "Decline of species that depend on specific riverine habitats; reduced biodiversity overall."
danube_river["Habitat Degradation"]["Influenced By"] = [
"Rivers (Danube) - Altered Hydrology",
"Rivers (Danube) - Pollution",
"Rivers (Danube) - Navigation",
"Land-Use Change (in the floodplain)"
]
danube_river["Habitat Degradation"]["Influences"] = [
"Rivers (Danube) - Biodiversity"
]
danube_river["Habitat Degradation"]["Logic Description"] = "Habitat degradation, resulting from multiple stressors, is a major threat to the biodiversity of the Danube River and its floodplain."
danube_river["Habitat Degradation"]["Impact Function"] = "impact_habitat_degradation_danube_river"

# --- Rivers (Mississippi) ---
mississippi_river = all_stressors_data["Mississippi Rivers"]

mississippi_river["Agricultural Runoff"]["Metric"] = "Concentrations of nitrogen and phosphorus in the river; size and severity of the hypoxic zone in the Gulf of Mexico."
mississippi_river["Agricultural Runoff"]["Data Sources"] = [
"USGS National Water-Quality Assessment (NAWQA) program.",
"EPA data.",
"State environmental agencies.",
"Research publications."
]
mississippi_river["Agricultural Runoff"]["Impact on Area"] = "*Major* contributor to water quality degradation in the Mississippi River and the Gulf of Mexico."
mississippi_river["Agricultural Runoff"]["Impact on Biodiversity"] = "Eutrophication (nutrient enrichment) in the river and the Gulf of Mexico, leading to algal blooms and hypoxia (dead zones). Impacts on aquatic life in the river and the Gulf."
mississippi_river["Agricultural Runoff"]["Influenced By"] = [
"Agricultural Practices in the Mississippi River Basin (fertilizer use, animal agriculture).",
"Cropping Systems",
"Tile Drainage",
"Lack of Buffer Strips"
]
mississippi_river["Agricultural Runoff"]["Influences"] = [
"Rivers (Mississippi) - Water Quality",
"Gulf of Mexico Hypoxia",
"Rivers (Mississippi) - Eutrophication"
]
mississippi_river["Agricultural Runoff"]["Logic Description"] = "Agricultural runoff, carrying excess nutrients (nitrogen and phosphorus) from fertilizers and animal waste, is the *primary* cause of water quality problems in the Mississippi River and the large hypoxic zone (dead zone) in the Gulf of Mexico."
mississippi_river["Agricultural Runoff"]["Impact Function"] = "impact_agricultural_runoff_mississippi_river"

mississippi_river["Dams and Levees"]["Metric"] = "Number of dams and levees; changes in river flow and sediment transport; loss of floodplain connectivity."
mississippi_river["Dams and Levees"]["Data Sources"] = [
"US Army Corps of Engineers (USACE).",
"USGS data.",
"Research publications."
]
mississippi_river["Dams and Levees"]["Impact on Area"] = "*Major* alteration of the river's hydrology and morphology; reduced sediment delivery to coastal Louisiana; loss of floodplain habitats."
mississippi_river["Dams and Levees"]["Impact on Biodiversity"] = "Blockage of fish migration; loss of spawning grounds; changes in aquatic habitats; impacts on floodplain ecosystems."
mississippi_river["Dams and Levees"]["Influenced By"] = [
"Flood Control",
"Navigation",
"Hydropower Generation"
]
mississippi_river["Dams and Levees"]["Influences"] = [
"Rivers (Mississippi) - River Flow",
"Rivers (Mississippi) - Sediment Transport",
"Rivers (Mississippi) - Habitat Connectivity",
"Coastal Wetland Loss (Louisiana)"
]
mississippi_river["Dams and Levees"]["Logic Description"] = "Extensive dams and levees along the Mississippi River, constructed for flood control and navigation, have significantly altered the river's natural flow regime, sediment transport, and connectivity with its floodplain, with major ecological consequences."
mississippi_river["Dams and Levees"]["Impact Function"] = "impact_dams_levees_mississippi_river"

mississippi_river["Climate Change"]["Metric"] = "Changes in precipitation patterns; changes in river discharge; increased frequency of floods and droughts."
mississippi_river["Climate Change"]["Data Sources"] = [
"Climate models.",
"Historical weather records.",
"USGS streamflow data."
]
mississippi_river["Climate Change"]["Impact on Area"] = "Altered flow regimes; increased risk of extreme events."
mississippi_river["Climate Change"]["Impact on Biodiversity"] = "Impacts on aquatic species due to changes in water availability and temperature; increased stress on riverine ecosystems."
mississippi_river["Climate Change"]["Influenced By"] = ["Global GHG"]
mississippi_river["Climate Change"]["Influences"] = [
"Rivers (Mississippi) - River Flow",
"Rivers (Mississippi) - Water Temperature",
"Rivers (Mississippi) - Extreme Events"
]
mississippi_river["Climate Change"]["Logic Description"] = "Climate change is projected to alter precipitation patterns in the Mississippi River Basin, leading to changes in river flow and increased risk of floods and droughts."
mississippi_river["Climate Change"]["Impact Function"] = "impact_climate_change_mississippi_river"

mississippi_river["Invasive Species"]["Metric"] = "Distribution and abundance of key invasive species (e.g., Asian carp, zebra mussels)."
mississippi_river["Invasive Species"]["Data Sources"] = [
"USGS Nonindigenous Aquatic Species (NAS) database.",
"State natural resource agencies.",
"Research studies."
]
mississippi_river["Invasive Species"]["Impact on Area"] = "Changes in aquatic communities and ecosystem processes."
mississippi_river["Invasive Species"]["Impact on Biodiversity"] = "Competition with native species; predation on native species; alteration of food webs; potential for major ecological disruptions."
mississippi_river["Invasive Species"]["Influenced By"] = [
"Shipping (ballast water).",
"Canals and Waterways.",
"Intentional or Accidental Introductions"
]
mississippi_river["Invasive Species"]["Influences"] = [
"Rivers (Mississippi) - Native Species",
"Rivers (Mississippi) - Ecosystem Function"
]
mississippi_river["Invasive Species"]["Logic Description"] = "Invasive species, such as Asian carp, pose a significant threat to the Mississippi River ecosystem, with the potential to outcompete native species and disrupt food webs."
mississippi_river["Invasive Species"]["Impact Function"] = "impact_invasive_species_mississippi_river"

mississippi_river["Channelization"]["Metric"] = "Length of river channelized; loss of natural meanders and wetlands."
mississippi_river["Channelization"]["Data Sources"] = [
"US Army Corps of Engineers (USACE).",
"Historical maps and records.",
"Remote sensing data."
]
mississippi_river["Channelization"]["Impact on Area"] = "Simplification of river habitat; loss of wetlands and floodplain connectivity; faster flow rates."
mississippi_river["Channelization"]["Impact on Biodiversity"] = "Reduced habitat diversity; impacts on fish and invertebrate communities; loss of spawning and nursery grounds."
mississippi_river["Channelization"]["Influenced By"] = [
"Flood Control",
"Navigation"
]
mississippi_river["Channelization"]["Influences"] = [
"Rivers (Mississippi) - Habitat Loss",
"Rivers (Mississippi) - Hydrology"
]
mississippi_river["Channelization"]["Logic Description"] = "Channelization, straightening and deepening of the river for navigation and flood control, has significantly simplified river habitats and reduced connectivity with floodplains."
mississippi_river["Channelization"]["Impact Function"] = "impact_channelization_mississippi_river"

mississippi_river["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., heavy metals, industrial chemicals, pharmaceuticals) in water, sediment, and biota."
mississippi_river["Pollution"]["Data Sources"] = [
"EPA water quality data.",
"USGS water quality data.",
"State environmental agencies."
]
mississippi_river["Pollution"]["Impact on Area"] = "In addition to agricultural runoff, industrial and urban sources contribute to pollution."
mississippi_river["Pollution"]["Impact on Biodiversity"] = "Toxic effects on aquatic organisms; bioaccumulation of pollutants."
mississippi_river["Pollution"]["Influenced By"] = [
"Industrial Discharge",
"Urban Runoff",
"Wastewater Treatment Plants",
"Legacy Pollutants (from past industrial activities)"
]
mississippi_river["Pollution"]["Influences"] = [
"Rivers (Mississippi) - Water Quality",
"Rivers (Mississippi) - Aquatic Life Health"
]
mississippi_river["Pollution"]["Logic Description"] = "In addition to agricultural runoff, industrial and urban sources contribute to pollution in the Mississippi."
mississippi_river["Pollution"]["Impact Function"] = "impact_pollution_mississippi_river"

mississippi_river["Overfishing"]["Metric"] = "Catch data; population estimates of key species."
mississippi_river["Overfishing"]["Data Sources"] = [
"Fisheries data (state and federal agencies).",
"Research studies."
]
mississippi_river["Overfishing"]["Impact on Area"] = "Not directly applicable, but affects fish populations."
mississippi_river["Overfishing"]["Impact on Biodiversity"] = "Decline of commercially and ecologically important fish species; potential impacts on food web structure."
mississippi_river["Overfishing"]["Influenced By"] = [
"Fishing Pressure",
"Lack of Effective Management"
]
mississippi_river["Overfishing"]["Influences"] = [
"Rivers (Mississippi) - Fish Populations"
]
mississippi_river["Overfishing"]["Logic Description"] = "While not as severe a problem as in some other major rivers, overfishing can still impact certain fish species in the Mississippi."
mississippi_river["Overfishing"]["Impact Function"] = "impact_overfishing_mississippi_river"

# --- Rivers (Murray-Darling) ---
murray_darling_river = all_stressors_data["Murray-Darling Rivers"]

murray_darling_river["Water Extraction"]["Metric"] = "Volume of water extracted for irrigation and other uses (gigalitres/year); river flow rates; water levels in wetlands."
murray_darling_river["Water Extraction"]["Data Sources"] = [
"Murray-Darling Basin Authority (MDBA) data.",
"Australian Bureau of Meteorology (BOM) data.",
"State government water agencies (New South Wales, Victoria, Queensland, South Australia).",
"Research publications."
]
murray_darling_river["Water Extraction"]["Impact on Area"] = "*Drastic* reduction in river flows; drying of wetlands; reduced environmental flows."
murray_darling_river["Water Extraction"]["Impact on Biodiversity"] = "Decline of native fish populations (e.g., Murray cod); impacts on waterbirds; loss of wetland habitats; degradation of riverine ecosystems."
murray_darling_river["Water Extraction"]["Influenced By"] = [
"Irrigated Agriculture: The *dominant* water user in the basin.",
"Government Water Policies: Water allocation and management.",
"Climate Change (reduced inflows)"
]
murray_darling_river["Water Extraction"]["Influences"] = [
"Rivers (Murray-Darling) - River Flow",
"Rivers (Murray-Darling) - Water Availability (the primary impact)",
"Rivers (Murray-Darling) - Wetland Extent",
"Rivers (Murray-Darling) - Salinity"
]
murray_darling_river["Water Extraction"]["Logic Description"] = "Over-extraction of water, primarily for irrigated agriculture, is the *most significant* stressor on the Murray-Darling Basin, leading to drastically reduced river flows, the drying of wetlands, and widespread environmental degradation."
murray_darling_river["Water Extraction"]["Impact Function"] = "impact_water_extraction_murray_darling"

murray_darling_river["Altered Flow Regimes"]["Metric"] = "Changes in the timing, duration, and magnitude of flow events; reduced frequency of floods; altered seasonality of flows."
murray_darling_river["Altered Flow Regimes"]["Data Sources"] = [
"MDBA data.",
"BOM data.",
"Research publications."
]
murray_darling_river["Altered Flow Regimes"]["Impact on Area"] = "Changes in river and wetland habitats; reduced connectivity between river channels and floodplains."
murray_darling_river["Altered Flow Regimes"]["Impact on Biodiversity"] = "Impacts on fish spawning and migration (many native fish need floods to trigger spawning); loss of floodplain wetlands; changes in vegetation communities."
murray_darling_river["Altered Flow Regimes"]["Influenced By"] = [
"Dams and Weirs",
"Rivers (Murray-Darling) - Water Extraction"
]
murray_darling_river["Altered Flow Regimes"]["Influences"] = [
"Rivers (Murray-Darling) - Habitat Connectivity",
"Rivers (Murray-Darling) - Fish Breeding",
"Rivers (Murray-Darling) - Wetland Ecosystems"
]
murray_darling_river["Altered Flow Regimes"]["Logic Description"] = "Dams, weirs, and water extraction have significantly altered the natural flow regime of the rivers in the Murray-Darling Basin, impacting aquatic ecosystems and floodplain wetlands."
murray_darling_river["Altered Flow Regimes"]["Impact Function"] = "impact_altered_flow_regimes_murray_darling"

murray_darling_river["Climate Change"]["Metric"] = "Temperature increase (°C); changes in precipitation (mm/year, seasonality); increased frequency and severity of drought."
murray_darling_river["Climate Change"]["Data Sources"] = [
"Climate models.",
"Historical weather records (BOM).",
"Research publications."
]
murray_darling_river["Climate Change"]["Impact on Area"] = "Increased aridity; reduced water availability; increased risk of extreme events (droughts, floods)."
murray_darling_river["Climate Change"]["Impact on Biodiversity"] = "Increased stress on aquatic ecosystems; shifts in species distributions; potential for increased algal blooms; impacts on waterbirds."
murray_darling_river["Climate Change"]["Influenced By"] = ["Global GHG"]
murray_darling_river["Climate Change"]["Influences"] = [
"Rivers (Murray-Darling) - Water Availability",
"Rivers (Murray-Darling) - Extreme Events"
]
murray_darling_river["Climate Change"]["Logic Description"] = "Climate change is exacerbating existing water stress in the Murray-Darling Basin, leading to reduced water availability and increased frequency of extreme events."
murray_darling_river["Climate Change"]["Impact Function"] = "impact_climate_change_murray_darling"

murray_darling_river["Invasive Species"]["Metric"] = "Distribution and abundance of key invasive species (e.g., common carp, *Gambusia* (mosquitofish))."
murray_darling_river["Invasive Species"]["Data Sources"] = [
"Fish surveys.",
"Research studies.",
"Government reports."
]
murray_darling_river["Invasive Species"]["Impact on Area"] = "Changes in aquatic communities."
murray_darling_river["Invasive Species"]["Impact on Biodiversity"] = "Competition with and predation on native fish; alteration of aquatic habitats; spread of diseases."
murray_darling_river["Invasive Species"]["Influenced By"] = [
"Introduction through human activities.",
"Rivers (Murray-Darling) - Altered Flow Regimes (can favor some invasives).",
"Rivers (Murray-Darling) - Climate Change (may favor some invasives)"
]
murray_darling_river["Invasive Species"]["Influences"] = [
"Rivers (Murray-Darling) - Native Fish Populations"
]
murray_darling_river["Invasive Species"]["Logic Description"] = "Invasive species, such as common carp, are a major problem in the Murray-Darling Basin, impacting native fish and altering aquatic ecosystems."
murray_darling_river["Invasive Species"]["Impact Function"] = "impact_invasive_species_murray_darling"

murray_darling_river["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., nutrients, pesticides, salts) in water and sediments."
murray_darling_river["Pollution"]["Data Sources"] = [
"Water quality monitoring data (state and federal agencies).",
"Research studies."
]
murray_darling_river["Pollution"]["Impact on Area"] = "Degradation of water quality."
murray_darling_river["Pollution"]["Impact on Biodiversity"] = "Impacts on aquatic life; eutrophication (nutrient enrichment); toxic effects of pesticides."
murray_darling_river["Pollution"]["Influenced By"] = [
"Agricultural Runoff",
"Irrigation Practices (leading to salt mobilization)",
"Urban Runoff"
]
murray_darling_river["Pollution"]["Influences"] = [
"Rivers (Murray-Darling) - Water Quality",
"Rivers (Murray-Darling) - Aquatic Life Health"
]
murray_darling_river["Pollution"]["Logic Description"] = "Pollution from agriculture, urban areas, and irrigation practices degrades water quality in the Murray-Darling Basin."
murray_darling_river["Pollution"]["Impact Function"] = "impact_pollution_murray_darling"

murray_darling_river["Salinity"]["Metric"] = "Salt concentration in water and soil (electrical conductivity - EC)."
murray_darling_river["Salinity"]["Data Sources"] = [
"Water quality monitoring data.",
"Soil surveys.",
"Research studies."
]
murray_darling_river["Salinity"]["Impact on Area"] = "Degradation of water and soil quality; reduced agricultural productivity; impacts on infrastructure."
murray_darling_river["Salinity"]["Impact on Biodiversity"] = "Impacts on freshwater species; changes in vegetation communities; loss of aquatic habitat."
murray_darling_river["Salinity"]["Influenced By"] = [
"Irrigation Practices",
"Land Clearing (removal of deep-rooted vegetation)",
"Rivers (Murray-Darling) - Reduced River Flow",
"Groundwater Discharge"
]
murray_darling_river["Salinity"]["Influences"] = [
"Rivers (Murray-Darling) - Water Quality",
"Rivers (Murray-Darling) - Soil Quality",
"Rivers (Murray-Darling) - Aquatic Ecosystems"
]
murray_darling_river["Salinity"]["Logic Description"] = "Salinity, both dryland and irrigation-induced, is a *major* environmental problem in the Murray-Darling Basin, impacting water quality, soil health, and biodiversity."
murray_darling_river["Salinity"]["Impact Function"] = "impact_salinity_murray_darling"

murray_darling_river["Habitat Degradation"]["Metric"] = "Area of riverine and wetland habitats lost or degraded; changes in habitat quality."
murray_darling_river["Habitat Degradation"]["Data Sources"] = [
"Remote sensing data.",
"Field surveys.",
"Research studies."
]
murray_darling_river["Habitat Degradation"]["Impact on Area"] = "Loss of spawning grounds, nurseries, and feeding areas for fish and other aquatic life."
murray_darling_river["Habitat Degradation"]["Impact on Biodiversity"] = "Decline of species that depend on specific riverine habitats; reduced biodiversity overall."
murray_darling_river["Habitat Degradation"]["Influenced By"] = [
"Rivers (Murray-Darling) - Altered Flow Regimes",
"Rivers (Murray-Darling) - Water Extraction",
"Rivers (Murray-Darling) - Pollution",
"Rivers (Murray-Darling) - Salinity",
"Land-Use Change (in the catchment)"
]
murray_darling_river["Habitat Degradation"]["Influences"] = [
"Rivers (Murray-Darling) - Biodiversity"
]
murray_darling_river["Habitat Degradation"]["Logic Description"] = "Habitat degradation, resulting from a combination of stressors, is a major threat to the biodiversity of the Murray-Darling Basin."
murray_darling_river["Habitat Degradation"]["Impact Function"] = "impact_habitat_degradation_murray_darling"

# --- Rivers (Yangtze) ---
yangtze_river = all_stressors_data["Yangtze Rivers"]

yangtze_river["Dam Construction"]["Metric"] = "Number and capacity of dams on the Yangtze and its tributaries; changes in river flow, sediment transport, and water temperature; fragmentation of the river system."
yangtze_river["Dam Construction"]["Data Sources"] = [
"Chinese government data (Ministry of Water Resources, Ministry of Ecology and Environment).",
"Research publications (Chinese and international).",
"Environmental Impact Assessments (EIAs) for dam projects."
]
yangtze_river["Dam Construction"]["Impact on Area"] = "*Profound* alteration of the Yangtze's hydrology and ecology. The Three Gorges Dam is the most prominent example, but there are *many* other dams on the river and its tributaries."
yangtze_river["Dam Construction"]["Impact on Biodiversity"] = "Blockage of fish migration routes (e.g., sturgeon, other migratory fish); changes in downstream flow and sediment delivery, affecting habitats and food webs; loss of riverine and floodplain habitats; increased risk of extinction for endangered species (e.g., Yangtze finless porpoise, Chinese paddlefish - likely extinct); changes in water temperature."
yangtze_river["Dam Construction"]["Influenced By"] = [
"Hydropower Generation",
"Flood Control",
"Navigation",
"Water Supply"
]
yangtze_river["Dam Construction"]["Influences"] = [
"Rivers (Yangtze) - Fish Migration",
"Rivers (Yangtze) - Sediment Transport",
"Rivers (Yangtze) - Habitat Connectivity",
"Rivers (Yangtze) - Water Quality",
"Rivers (Yangtze) - Endangered Species Survival"
]
yangtze_river["Dam Construction"]["Logic Description"] = "The construction of numerous dams, including the massive Three Gorges Dam, has fundamentally altered the Yangtze's hydrology, fragmented the river ecosystem, and blocked fish migration routes, with severe consequences for biodiversity."
yangtze_river["Dam Construction"]["Impact Function"] = "impact_dam_construction_yangtze_river"

yangtze_river["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., nutrients, heavy metals, organic pollutants, microplastics) in water, sediment, and biota."
yangtze_river["Pollution"]["Data Sources"] = [
"Chinese government environmental monitoring data (Ministry of Ecology and Environment).",
"Research publications."
]
yangtze_river["Pollution"]["Impact on Area"] = "Severe water quality degradation in many parts of the river."
yangtze_river["Pollution"]["Impact on Biodiversity"] = "Toxic effects on aquatic organisms.; Eutrophication.; Impacts on human health (through drinking water and fish consumption).; Bioaccumulation of pollutants."
yangtze_river["Pollution"]["Influenced By"] = [
"Industrial Discharge (from numerous factories along the river)",
"Agricultural Runoff (fertilizers, pesticides)",
"Urban Sewage (from large cities along the river)",
"Mining Activities",
"Shipping"
]
yangtze_river["Pollution"]["Influences"] = [
"Rivers (Yangtze) - Water Quality",
"Rivers (Yangtze) - Aquatic Life Health",
"Human Health"
]
yangtze_river["Pollution"]["Logic Description"] = "The Yangtze River is one of the most polluted rivers in the world, receiving vast amounts of industrial, agricultural, and urban waste, leading to severe water quality degradation and impacts on aquatic life."
yangtze_river["Pollution"]["Impact Function"] = "impact_pollution_yangtze_river"

yangtze_river["Overfishing"]["Metric"] = "Fish catches; fish population sizes and structure; fishing effort."
yangtze_river["Overfishing"]["Data Sources"] = [
"Fisheries data (often limited).",
"Research studies."
]
yangtze_river["Overfishing"]["Impact on Area"] = "Not directly applicable (affects fish populations, not area)."
yangtze_river["Overfishing"]["Impact on Biodiversity"] = "Decline of fish stocks, including many endemic species.; Disruption of the food web."
yangtze_river["Overfishing"]["Influenced By"] = [
"High Fishing Pressure",
"Destructive Fishing Practices",
"Habitat Degradation (from other stressors)"
]
yangtze_river["Overfishing"]["Influences"] = [
"Rivers (Yangtze) - Fish Populations",
"Rivers (Yangtze) - Food Web Structure"
]
yangtze_river["Overfishing"]["Logic Description"] = "Overfishing, combined with other stressors, has severely depleted fish populations in the Yangtze River."
yangtze_river["Overfishing"]["Impact Function"] = "impact_overfishing_yangtze_river"

yangtze_river["Invasive Species"]["Metric"] = "Distribution and abundance of invasive aquatic species (e.g., certain fish, plants, invertebrates)."
yangtze_river["Invasive Species"]["Data Sources"] = [
"Research studies.",
"Monitoring programs (often limited)."
]
yangtze_river["Invasive Species"]["Impact on Area"] = "Changes in aquatic communities and ecosystem processes."
yangtze_river["Invasive Species"]["Impact on Biodiversity"] = "Competition with native species.; Predation on native species.; Alteration of habitats."
yangtze_river["Invasive Species"]["Influenced By"] = [
"Shipping (ballast water)",
"Aquaculture (escaped fish)",
"Intentional or Accidental Introductions"
]
yangtze_river["Invasive Species"]["Influences"] = [
"Rivers (Yangtze) - Native Species",
"Rivers (Yangtze) - Ecosystem Function"
]
yangtze_river["Invasive Species"]["Logic Description"] = "Invasive species are a growing threat to the Yangtze River's native biodiversity."
yangtze_river["Invasive Species"]["Impact Function"] = "impact_invasive_species_yangtze_river"

yangtze_river["Climate Change"]["Metric"] = "Changes in water temperature; changes in precipitation patterns; changes in river discharge; increased frequency of extreme events."
yangtze_river["Climate Change"]["Data Sources"] = [
"Climate models.",
"Historical records (temperature, precipitation, river flow).",
"Research publications."
]
yangtze_river["Climate Change"]["Impact on Area"] = "Altered flow regimes; increased water temperatures; increased risk of floods and droughts."
yangtze_river["Climate Change"]["Impact on Biodiversity"] = "Shifts in species distributions.; Increased stress on aquatic organisms.; Impacts on fish spawning and migration."
yangtze_river["Climate Change"]["Influenced By"] = ["Global GHG"]
yangtze_river["Climate Change"]["Influences"] = [
"Rivers (Yangtze) - Water Temperature",
"Rivers (Yangtze) - River Flow",
"Rivers (Yangtze) - Extreme Events"
]
yangtze_river["Climate Change"]["Logic Description"] = "Climate change is impacting the Yangtze River through altered precipitation patterns, increased temperatures, and changes in river flow, further stressing an already degraded ecosystem."
yangtze_river["Climate Change"]["Impact Function"] = "impact_climate_change_yangtze_river"

yangtze_river["Shipping"]["Metric"] = "Vessel traffic density; frequency of accidents (e.g., oil spills); noise pollution."
yangtze_river["Shipping"]["Data Sources"] = [
"Maritime authorities.",
"Port statistics.",
"Research studies."
]
yangtze_river["Shipping"]["Impact on Area"] = "Water pollution (oil spills, discharge of waste); noise pollution; physical disturbance of the riverbed (in some areas)."
yangtze_river["Shipping"]["Impact on Biodiversity"] = "Impacts on aquatic life from pollution and noise; disturbance to endangered species (e.g., Yangtze finless porpoise)."
yangtze_river["Shipping"]["Influenced By"] = [
"Economic Activity",
"Trade",
"Navigation Infrastructure"
]
yangtze_river["Shipping"]["Influences"] = [
"Rivers (Yangtze) - Water Quality",
"Rivers (Yangtze) - Noise Pollution",
"Rivers (Yangtze) - Wildlife Disturbance"
]
yangtze_river["Shipping"]["Logic Description"] = "The Yangtze River is a major shipping route, and heavy vessel traffic contributes to pollution, noise, and disturbance to aquatic life."
yangtze_river["Shipping"]["Impact Function"] = "impact_shipping_yangtze_river"

yangtze_river["Sand Mining"]["Metric"] = "Volume of sand extracted from the riverbed (m³/year)."
yangtze_river["Sand Mining"]["Data Sources"] = [
"Government data (often limited).",
"Research studies.",
"Remote sensing (detecting dredging activity)."
]
yangtze_river["Sand Mining"]["Impact on Area"] = "Alteration of the riverbed; increased turbidity; changes in sediment transport."
yangtze_river["Sand Mining"]["Impact on Biodiversity"] = "Destruction of benthic habitats; impacts on fish spawning grounds; impacts on invertebrates."
yangtze_river["Sand Mining"]["Influenced By"] = [
"Construction Industry: Demand for sand and gravel.",
"Lack of Regulation and Enforcement"
]
yangtze_river["Sand Mining"]["Influences"] = [
"Rivers (Yangtze) - Riverbed Morphology",
"Rivers (Yangtze) - Water Quality (turbidity)",
"Rivers (Yangtze) - Benthic Habitats"
]
yangtze_river["Sand Mining"]["Logic Description"] = "Extensive sand mining in the Yangtze River and its connected lakes (e.g., Poyang Lake, Dongting Lake) is causing significant damage to riverbed habitats and impacting aquatic life."
yangtze_river["Sand Mining"]["Impact Function"] = "impact_sand_mining_yangtze_river"

# --- Salt Marshes (Australian) ---
salt_marshes_australian = all_stressors_data["Australian Salt Marshes"]

salt_marshes_australian["Climate Change"]["Metric"] = "Sea level rise (mm/year); changes in temperature (°C); changes in rainfall patterns; increased frequency of extreme events (storms, floods)."
salt_marshes_australian["Climate Change"]["Data Sources"] = [
"Australian Bureau of Meteorology (BOM) data.",
"CSIRO research.",
"Climate models.",
"Tide gauge records.",
"Research publications."
]
salt_marshes_australian["Climate Change"]["Impact on Area"] = "Coastal inundation and erosion; landward migration of salt marshes (where possible); saltwater intrusion into adjacent ecosystems."
salt_marshes_australian["Climate Change"]["Impact on Biodiversity"] = "Loss of salt marsh habitat; changes in species distributions; increased stress on salt marsh plants and animals. Potential for 'coastal squeeze' where landward migration is blocked by development."
salt_marshes_australian["Climate Change"]["Influenced By"] = ["Global GHG"]
salt_marshes_australian["Climate Change"]["Influences"] = [
"Salt Marshes (Australian) - Sea Level Rise",
"Salt Marshes (Australian) - Coastal Erosion",
"Salt Marshes (Australian) - Altered Hydrology"
]
salt_marshes_australian["Climate Change"]["Logic Description"] = "Climate change, particularly sea level rise, is a major threat to Australian salt marshes. Changes in temperature, rainfall, and storm frequency/intensity also have impacts."
salt_marshes_australian["Climate Change"]["Impact Function"] = "impact_climate_change_salt_marshes_australian"

salt_marshes_australian["Coastal Development"]["Metric"] = "Area of salt marsh converted to urban development, infrastructure, or other land uses (ha/year); length of coastline with modified salt marshes."
salt_marshes_australian["Coastal Development"]["Data Sources"] = [
"Remote sensing data.",
"Land-use planning records (state and local governments).",
"Research publications."
]
salt_marshes_australian["Coastal Development"]["Impact on Area"] = "Direct loss of salt marsh habitat; fragmentation; altered hydrology."
salt_marshes_australian["Coastal Development"]["Impact on Biodiversity"] = "Loss of habitat for salt marsh plants and animals; reduced nursery grounds for fish and invertebrates; loss of coastal protection; reduced carbon sequestration."
salt_marshes_australian["Coastal Development"]["Influenced By"] = [
"Population Growth",
"Urbanization",
"Tourism Development",
"Infrastructure Development"
]
salt_marshes_australian["Coastal Development"]["Influences"] = [
"Salt Marshes (Australian) - Habitat Loss",
"Salt Marshes (Australian) - Altered Hydrology",
"Salt Marshes (Australian) - Water Quality"
]
salt_marshes_australian["Coastal Development"]["Logic Description"] = "Coastal development, including urbanization, infrastructure projects, and tourism development, directly destroys and degrades salt marsh habitats."
salt_marshes_australian["Coastal Development"]["Impact Function"] = "impact_coastal_development_salt_marshes_australian"

salt_marshes_australian["Altered Hydrology"]["Metric"] = "Changes in tidal flow; changes in freshwater inflow; construction of drainage channels, levees, and other structures."
salt_marshes_australian["Altered Hydrology"]["Data Sources"] = [
"Hydrological data (tidal records, river flow data).",
"Remote sensing data.",
"Research studies."
]
salt_marshes_australian["Altered Hydrology"]["Impact on Area"] = "Changes in salinity gradients; altered inundation patterns; changes in sediment deposition; altered drainage."
salt_marshes_australian["Altered Hydrology"]["Impact on Biodiversity"] = "Impacts on salt marsh vegetation (e.g., changes in species composition); impacts on fish, invertebrates, and birds that depend on salt marshes."
salt_marshes_australian["Altered Hydrology"]["Influenced By"] = [
"Salt Marshes (Australian) - Coastal Development",
"Upstream Water Diversions",
"Drainage for Agriculture or Mosquito Control",
"Climate Change"
]
salt_marshes_australian["Altered Hydrology"]["Influences"] = [
"Salt Marshes (Australian) - Salinity",
"Salt Marshes (Australian) - Sedimentation",
"Salt Marshes (Australian) - Habitat Suitability"
]
salt_marshes_australian["Altered Hydrology"]["Logic Description"] = "Changes in the natural water regime of salt marshes, due to coastal development, upstream water diversions, drainage, and climate change, can significantly alter their ecological character."
salt_marshes_australian["Altered Hydrology"]["Impact Function"] = "impact_altered_hydrology_salt_marshes_australian"

salt_marshes_australian["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., nutrients, heavy metals, pesticides, plastics) in water, sediment, and marsh organisms."
salt_marshes_australian["Pollution"]["Data Sources"] = [
"Water quality monitoring data (state government agencies).",
"Research studies."
]
salt_marshes_australian["Pollution"]["Impact on Area"] = "Degradation of water and sediment quality; potential impacts on salt marsh health."
salt_marshes_australian["Pollution"]["Impact on Biodiversity"] = "Toxic effects on salt marsh plants and animals; eutrophication (nutrient enrichment); impacts on food webs."
salt_marshes_australian["Pollution"]["Influenced By"] = [
"Urban Runoff",
"Agricultural Runoff",
"Industrial Discharge",
"Wastewater Treatment Plants"
]
salt_marshes_australian["Pollution"]["Influences"] = [
"Salt Marshes (Australian) - Water Quality",
"Salt Marshes (Australian) - Marsh Health"
]
salt_marshes_australian["Pollution"]["Logic Description"] = "Pollution from urban, agricultural, and industrial sources can degrade water quality and impact salt marsh ecosystems."
salt_marshes_australian["Pollution"]["Impact Function"] = "impact_pollution_salt_marshes_australian"

salt_marshes_australian["Invasive Species"]["Metric"] = "Distribution and abundance of key invasive species (e.g., *Spartina* species (cordgrasses) in some areas, other invasive plants, marine pests)."
salt_marshes_australian["Invasive Species"]["Data Sources"] = [
"Field surveys.",
"Research studies.",
"Government reports (biosecurity agencies)."
]
salt_marshes_australian["Invasive Species"]["Impact on Area"] = "Changes in vegetation composition; altered habitat structure; potential impacts on sediment dynamics."
salt_marshes_australian["Invasive Species"]["Impact on Biodiversity"] = "Competition with native salt marsh plants; impacts on invertebrate and bird communities; can alter ecosystem processes."
salt_marshes_australian["Invasive Species"]["Influenced By"] = [
"Introduction through human activities (e.g., ballast water, aquaculture).",
"Disturbance",
"Salt Marshes (Australian) - Altered Hydrology"
]
salt_marshes_australian["Invasive Species"]["Influences"] = [
"Salt Marshes (Australian) - Native Plant Communities",
"Salt Marshes (Australian) - Habitat Structure"
]
salt_marshes_australian["Invasive Species"]["Logic Description"] = "Invasive species, such as certain cordgrasses (*Spartina*), can outcompete native salt marsh plants and alter ecosystem structure."
salt_marshes_australian["Invasive Species"]["Impact Function"] = "impact_invasive_species_salt_marshes_australian"

salt_marshes_australian["Overgrazing"]["Metric"] = "Livestock density in salt marsh areas (where grazing occurs); vegetation cover and composition."
salt_marshes_australian["Overgrazing"]["Data Sources"] = [
"Agricultural statistics.",
"Vegetation surveys.",
"Research studies."
]
salt_marshes_australian["Overgrazing"]["Impact on Area"] = "Damage to salt marsh vegetation; soil compaction; increased erosion."
salt_marshes_australian["Overgrazing"]["Impact on Biodiversity"] = "Loss of palatable plant species; changes in plant community composition; impacts on invertebrates and birds that depend on salt marsh vegetation."
salt_marshes_australian["Overgrazing"]["Influenced By"] = [
"Livestock Management Practices",
"Feral Animals (in some areas)"
]
salt_marshes_australian["Overgrazing"]["Influences"] = [
"Salt Marshes (Australian) - Vegetation Changes",
"Salt Marshes (Australian) - Soil Erosion"
]
salt_marshes_australian["Overgrazing"]["Logic Description"] = "Overgrazing by livestock (and, in some areas, feral animals) can damage salt marsh vegetation and lead to soil erosion."
salt_marshes_australian["Overgrazing"]["Impact Function"] = "impact_overgrazing_salt_marshes_australian"

# --- Salt Marshes (European) ---
salt_marshes_european = all_stressors_data["European Salt Marshes"]

salt_marshes_european["Sea Level Rise"]["Metric"] = "Rate of sea level rise (mm/year); marsh elevation relative to sea level; accretion rates; frequency/duration of inundation."
salt_marshes_european["Sea Level Rise"]["Data Sources"] = [
"Tide gauge records.",
"Satellite altimetry.",
"Research publications.",
"European Environment Agency (EEA) data."
]
salt_marshes_european["Sea Level Rise"]["Impact on Area"] = "Inundation and submergence of low-lying marshes.; Coastal erosion.; Landward migration (often blocked by coastal defenses).; 'Coastal squeeze'."
salt_marshes_european["Sea Level Rise"]["Impact on Biodiversity"] = "Loss of habitat for marsh plants and animals.; Shifts in species composition.; Reduced nesting habitat for birds."
salt_marshes_european["Sea Level Rise"]["Influenced By"] = [
"Global Greenhouse Gas Emissions",
"Land Subsidence (in some areas)"
]
salt_marshes_european["Sea Level Rise"]["Influences"] = [
"Salt Marshes (European) - Coastal Erosion",
"Salt Marshes (European) - Habitat Loss"
]
salt_marshes_european["Sea Level Rise"]["Logic Description"] = "Sea level rise is a major threat to European salt marshes, and 'coastal squeeze' is a significant problem due to extensive coastal development."
salt_marshes_european["Sea Level Rise"]["Impact Function"] = "impact_sea_level_rise_european_salt_marshes"

salt_marshes_european["Coastal Development"]["Metric"] = "Area of salt marsh converted to development (ha/year); length of coastline with hard defenses (km)."
salt_marshes_european["Coastal Development"]["Data Sources"] = [
"Land-use planning records.",
"Remote sensing data.",
"EEA data."
]
salt_marshes_european["Coastal Development"]["Impact on Area"] = "Direct loss of habitat; fragmentation; *prevention of landward migration* of marshes in response to sea level rise (coastal squeeze)."
salt_marshes_european["Coastal Development"]["Impact on Biodiversity"] = "Loss of habitat; reduced nursery grounds for fish; loss of coastal protection."
salt_marshes_european["Coastal Development"]["Influenced By"] = [
"Urbanization",
"Infrastructure Development",
"Coastal Defenses (dikes, seawalls)",
"Tourism"
]
salt_marshes_european["Coastal Development"]["Influences"] = [
"Salt Marshes (European) - Habitat Loss",
"Salt Marshes (European) - Coastal Squeeze"
]
salt_marshes_european["Coastal Development"]["Logic Description"] = "Coastal development and hard coastal defenses are major threats, preventing landward migration of marshes and leading to habitat loss."
salt_marshes_european["Coastal Development"]["Impact Function"] = "impact_coastal_development_european_salt_marshes"

salt_marshes_european["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., nutrients, heavy metals, pesticides) in water, sediment, and marsh organisms."
salt_marshes_european["Pollution"]["Data Sources"] = [
"Water quality monitoring programs (national and EU-level).",
"Research studies."
]
salt_marshes_european["Pollution"]["Impact on Area"] = "Degradation of water and sediment quality; eutrophication."
salt_marshes_european["Pollution"]["Impact on Biodiversity"] = "Impacts on marsh plants and animals; potential for algal blooms; bioaccumulation of toxins."
salt_marshes_european["Pollution"]["Influenced By"] = [
"Agricultural Runoff",
"Urban Runoff",
"Industrial Discharge",
"Atmospheric Deposition"
]
salt_marshes_european["Pollution"]["Influences"] = [
"Salt Marshes (European) - Water Quality",
"Salt Marshes (European) - Marsh Health"
]
salt_marshes_european["Pollution"]["Logic Description"] = "Pollution from agriculture, urban areas, and industry degrades water quality and can impact marsh ecosystems."
salt_marshes_european["Pollution"]["Impact Function"] = "impact_pollution_european_salt_marshes"

salt_marshes_european["Invasive Species"]["Metric"] = "Distribution and abundance of key invasive species (e.g., *Spartina anglica* (common cordgrass))."
salt_marshes_european["Invasive Species"]["Data Sources"] = [
"Field surveys.",
"Research studies.",
"National monitoring programs."
]
salt_marshes_european["Invasive Species"]["Impact on Area"] = "Changes in vegetation composition and structure; altered sediment dynamics."
salt_marshes_european["Invasive Species"]["Impact on Biodiversity"] = "Competition with native marsh plants; impacts on invertebrate and bird communities; can alter ecosystem processes."
salt_marshes_european["Invasive Species"]["Influenced By"] = [
"Introduction through human activities (e.g., ballast water, intentional planting).",
"Disturbance",
"Salt Marshes (European) - Climate Change"
]
salt_marshes_european["Invasive Species"]["Influences"] = [
"Salt Marshes (European) - Native Plant Communities",
"Salt Marshes (European) - Ecosystem Functioning"
]
salt_marshes_european["Invasive Species"]["Logic Description"] = "Invasive species, such as *Spartina anglica*, can outcompete native salt marsh plants and alter ecosystem structure."
salt_marshes_european["Invasive Species"]["Impact Function"] = "impact_invasive_species_european_salt_marshes"

salt_marshes_european["Land Reclamation"]["Metric"] = "Area of salt marsh diked, drained, or filled for agriculture, development, or other uses (ha/year)."
salt_marshes_european["Land Reclamation"]["Data Sources"] = [
"Historical maps and records.",
"Land-use planning data.",
"Remote sensing data."
]
salt_marshes_european["Land Reclamation"]["Impact on Area"] = "*Significant* historical loss of salt marsh habitat; ongoing losses in some areas."
salt_marshes_european["Land Reclamation"]["Impact on Biodiversity"] = "Loss of habitat for marsh-dependent species; reduced nursery grounds for fish; loss of coastal protection."
salt_marshes_european["Land Reclamation"]["Influenced By"] = [
"Agricultural Expansion (historically a major driver)",
"Coastal Development",
"Flood Control"
]
salt_marshes_european["Land Reclamation"]["Influences"] = [
"Salt Marshes (European) - Habitat Loss",
"Salt Marshes (European) - Coastal Squeeze"
]
salt_marshes_european["Land Reclamation"]["Logic Description"] = "Land reclamation, particularly for agriculture, has historically been a major cause of salt marsh loss in Europe.  This continues to be a threat in some areas, and it exacerbates the impacts of sea level rise."
salt_marshes_european["Land Reclamation"]["Impact Function"] = "impact_land_reclamation_european_salt_marshes"

salt_marshes_european["Changes in Sediment Supply"]["Metric"] = "Sediment delivery rates to salt marshes; changes in erosion and accretion patterns."
salt_marshes_european["Changes in Sediment Supply"]["Data Sources"] = [
"Sediment core analysis.",
"Research studies.",
"Hydrological data (river discharge, sediment load)."
]
salt_marshes_european["Changes in Sediment Supply"]["Impact on Area"] = "Impacts the ability of marshes to keep pace with sea level rise; can lead to either marsh accretion or erosion."
salt_marshes_european["Changes in Sediment Supply"]["Impact on Biodiversity"] = "Changes in habitat suitability for marsh plants and animals."
salt_marshes_european["Changes in Sediment Supply"]["Influenced By"] = [
"Upstream Dams (reduce sediment delivery)",
"Coastal Engineering (can alter sediment transport)",
"Salt Marshes (European) - Climate Change (sea level rise)",
"Land Use Change (in the catchment)"
]
salt_marshes_european["Changes in Sediment Supply"]["Influences"] = [
"Salt Marshes (European) - Marsh Elevation",
"Salt Marshes (European) - Resilience to Sea Level Rise"
]
salt_marshes_european["Changes in Sediment Supply"]["Logic Description"] = "Changes in sediment supply, due to factors like upstream dams, coastal engineering, and climate change, can affect the ability of salt marshes to maintain their elevation relative to sea level."
salt_marshes_european["Changes in Sediment Supply"]["Impact Function"] = "impact_sediment_supply_changes_european_salt_marshes"

# --- Salt Marshes (Gulf of Mexico) ---
salt_marshes_gulf_of_mexico = all_stressors_data["Gulf of Mexico Salt Marshes"]

salt_marshes_gulf_of_mexico["Sea Level Rise"]["Metric"] = "Rate of relative sea level rise (mm/year); marsh elevation relative to sea level; accretion rates."
salt_marshes_gulf_of_mexico["Sea Level Rise"]["Data Sources"] = [
"NOAA tide gauge data.",
"USGS data.",
"Research publications."
]
salt_marshes_gulf_of_mexico["Sea Level Rise"]["Impact on Area"] = "Inundation and submergence of salt marshes.; Coastal erosion.; Landward migration (where possible).; *Significant* land loss in Louisiana."
salt_marshes_gulf_of_mexico["Sea Level Rise"]["Impact on Biodiversity"] = "Loss of habitat for marsh plants and animals (including commercially important species like shrimp, crabs, and fish).; Shifts in species composition.; Reduced nesting habitat for birds."
salt_marshes_gulf_of_mexico["Sea Level Rise"]["Influenced By"] = [
"Global Greenhouse Gas Emissions",
"Land Subsidence (especially in Louisiana)"
]
salt_marshes_gulf_of_mexico["Sea Level Rise"]["Influences"] = [
"Salt Marshes (Gulf of Mexico) - Coastal Erosion",
"Salt Marshes (Gulf of Mexico) - Habitat Loss"
]
salt_marshes_gulf_of_mexico["Sea Level Rise"]["Logic Description"] = "Sea level rise, combined with land subsidence in some areas (particularly Louisiana), is a major threat to Gulf of Mexico salt marshes, causing widespread land loss and habitat degradation."
salt_marshes_gulf_of_mexico["Sea Level Rise"]["Impact Function"] = "impact_sea_level_rise_gulf_of_mexico_salt_marshes"

salt_marshes_gulf_of_mexico["Coastal Development"]["Metric"] = "Area of salt marsh converted to development (ha/year); length of coastline with hardened structures."
salt_marshes_gulf_of_mexico["Coastal Development"]["Data Sources"] = [
"Land-use planning records (state and local governments).",
"Remote sensing data.",
"Research publications."
]
salt_marshes_gulf_of_mexico["Coastal Development"]["Impact on Area"] = "Direct loss of habitat.; Fragmentation.; Prevention of landward migration of marshes (coastal squeeze).; Altered hydrology."
salt_marshes_gulf_of_mexico["Coastal Development"]["Impact on Biodiversity"] = "Loss of habitat; reduced nursery grounds for fish and shellfish; loss of coastal protection."
salt_marshes_gulf_of_mexico["Coastal Development"]["Influenced By"] = [
"Urbanization",
"Infrastructure Development",
"Energy Development (oil and gas)",
"Tourism"
]
salt_marshes_gulf_of_mexico["Coastal Development"]["Influences"] = [
"Salt Marshes (Gulf of Mexico) - Habitat Loss",
"Salt Marshes (Gulf of Mexico) - Coastal Squeeze",
"Salt Marshes (Gulf of Mexico) - Altered Hydrology"
]
salt_marshes_gulf_of_mexico["Coastal Development"]["Logic Description"] = "Coastal development destroys and degrades salt marsh habitats, preventing natural adaptation to sea level rise."
salt_marshes_gulf_of_mexico["Coastal Development"]["Impact Function"] = "impact_coastal_development_gulf_of_mexico_salt_marshes"

salt_marshes_gulf_of_mexico["Oil Spills and Pollution"]["Metric"] = "Frequency and size of oil spills; concentrations of pollutants (oil, heavy metals, other chemicals) in water, sediment, and marsh organisms."
salt_marshes_gulf_of_mexico["Oil Spills and Pollution"]["Data Sources"] = [
"NOAA data (oil spill response).",
"EPA data.",
"State environmental agencies.",
"Research studies (e.g., after the Deepwater Horizon oil spill)."
]
salt_marshes_gulf_of_mexico["Oil Spills and Pollution"]["Impact on Area"] = "Acute and chronic impacts on salt marsh ecosystems.; Oiling of marshes; contamination of sediments."
salt_marshes_gulf_of_mexico["Oil Spills and Pollution"]["Impact on Biodiversity"] = "Mortality of marsh plants and animals.; Sub-lethal effects (e.g., reduced growth, reproductive impairment).; Long-term contamination of the food web."
salt_marshes_gulf_of_mexico["Oil Spills and Pollution"]["Influenced By"] = [
"Oil and Gas Extraction and Transportation (a major industry in the Gulf of Mexico)",
"Industrial Discharge",
"Urban Runoff",
"Shipping"
]
salt_marshes_gulf_of_mexico["Oil Spills and Pollution"]["Influences"] = [
"Salt Marshes (Gulf of Mexico) - Water Quality",
"Salt Marshes (Gulf of Mexico) - Marsh Health",
"Salt Marshes (Gulf of Mexico) - Wildlife Health"
]
salt_marshes_gulf_of_mexico["Oil Spills and Pollution"]["Logic Description"] = "The Gulf of Mexico is a major oil-producing region, and oil spills (both large and small) pose a significant threat to salt marshes. Other pollutants from industrial, urban, and agricultural sources also impact water quality."
salt_marshes_gulf_of_mexico["Oil Spills and Pollution"]["Impact Function"] = "impact_oil_spills_pollution_gulf_of_mexico_salt_marshes"

salt_marshes_gulf_of_mexico["Altered Hydrology and Sedimentation"]["Metric"] = "Changes in freshwater inflow; changes in sediment delivery; construction of canals, levees, and other structures."
salt_marshes_gulf_of_mexico["Altered Hydrology and Sedimentation"]["Data Sources"] = [
"USGS hydrological data.",
"US Army Corps of Engineers data.",
"Research publications."
]
salt_marshes_gulf_of_mexico["Altered Hydrology and Sedimentation"]["Impact on Area"] = "Changes in salinity gradients; altered inundation patterns; reduced sediment supply (in some areas, leading to marsh loss); increased sediment supply (in other areas, potentially burying marshes).; *Major* impacts in Louisiana due to alterations to the Mississippi River."
salt_marshes_gulf_of_mexico["Altered Hydrology and Sedimentation"]["Impact on Biodiversity"] = "Impacts on salt marsh vegetation; changes in habitat suitability for fish, invertebrates, and birds."
salt_marshes_gulf_of_mexico["Altered Hydrology and Sedimentation"]["Influenced By"] = [
"River Management (dams, levees, diversions on the Mississippi and other rivers)",
"Canal Construction (for navigation, oil and gas access)",
"Salt Marshes (Gulf of Mexico) - Coastal Development",
"Groundwater Extraction (contributing to subsidence)"
]
salt_marshes_gulf_of_mexico["Altered Hydrology and Sedimentation"]["Influences"] = [
"Salt Marshes (Gulf of Mexico) - Salinity",
"Salt Marshes (Gulf of Mexico) - Sedimentation",
"Salt Marshes (Gulf of Mexico) - Habitat Suitability",
"Louisiana Coastal Land Loss"
]
salt_marshes_gulf_of_mexico["Altered Hydrology and Sedimentation"]["Logic Description"] = "Alterations to river flow and sediment delivery, primarily due to river management and canal construction, have had profound impacts on Gulf of Mexico salt marshes, particularly in Louisiana."
salt_marshes_gulf_of_mexico["Altered Hydrology and Sedimentation"]["Impact Function"] = "impact_altered_hydrology_sedimentation_gulf_of_mexico_salt_marshes"

salt_marshes_gulf_of_mexico["Invasive Species"]["Metric"] = "Distribution and abundance of key invasive species (e.g., *Spartina alterniflora* (smooth cordgrass) in some areas (ironically, a *native* species on the Atlantic coast), nutria)."
salt_marshes_gulf_of_mexico["Invasive Species"]["Data Sources"] = [
"Field surveys.",
"Research studies.",
"Government reports."
]
salt_marshes_gulf_of_mexico["Invasive Species"]["Impact on Area"] = "Changes in vegetation composition; altered habitat structure."
salt_marshes_gulf_of_mexico["Invasive Species"]["Impact on Biodiversity"] = "Competition with native marsh plants; impacts on invertebrate and bird communities (e.g., nutria grazing).; Can alter physical processes."
salt_marshes_gulf_of_mexico["Invasive Species"]["Influenced By"] = [
"Intentional or Accidental Introductions",
"Disturbance"
]
salt_marshes_gulf_of_mexico["Invasive Species"]["Influences"] = [
"Salt Marshes (Gulf of Mexico) - Native Plant Communities",
"Salt Marshes (Gulf of Mexico) - Habitat Structure",
"Salt Marshes (Gulf of Mexico) - Erosion (nutria)"
]
salt_marshes_gulf_of_mexico["Invasive Species"]["Logic Description"] = "Invasive species can alter salt marsh structure and function."
salt_marshes_gulf_of_mexico["Invasive Species"]["Impact Function"] = "impact_invasive_species_gulf_of_mexico_salt_marshes"

salt_marshes_gulf_of_mexico["Nutrient Loading"]["Metric"] = "Concentrations of nitrogen and phosphorus in coastal waters."
salt_marshes_gulf_of_mexico["Nutrient Loading"]["Data Sources"] = [
"EPA data.",
"USGS data.",
"State environmental agencies.",
"Research publications."
]
salt_marshes_gulf_of_mexico["Nutrient Loading"]["Impact on Area"] = "Eutrophication of coastal waters."
salt_marshes_gulf_of_mexico["Nutrient Loading"]["Impact on Biodiversity"] = "Algal blooms; hypoxia (low oxygen); impacts on aquatic life. While salt marshes can *remove* some nutrients, excessive loading can still have negative impacts."
salt_marshes_gulf_of_mexico["Nutrient Loading"]["Influenced By"] = [
"Agricultural Runoff (from the Mississippi River Basin and other sources)",
"Urban Runoff",
"Wastewater Treatment Plants"
]
salt_marshes_gulf_of_mexico["Nutrient Loading"]["Influences"] = [
"Salt Marshes (Gulf of Mexico) - Water Quality",
"Gulf of Mexico Hypoxia"
]
salt_marshes_gulf_of_mexico["Nutrient Loading"]["Logic Description"] = "Excessive nutrient loading, primarily from agricultural runoff in the Mississippi River Basin, contributes to eutrophication and hypoxia in the Gulf of Mexico, impacting coastal ecosystems."
salt_marshes_gulf_of_mexico["Nutrient Loading"]["Impact Function"] = "impact_nutrient_loading_gulf_of_mexico_salt_marshes"

# --- Salt Marshes (North American Atlantic Coast) ---
salt_marshes_north_american_atlantic = all_stressors_data["North American Atlantic Coast Salt Marshes"]

salt_marshes_north_american_atlantic["Sea Level Rise"]["Metric"] = "Rate of sea level rise (mm/year); marsh elevation relative to sea level; rate of vertical accretion."
salt_marshes_north_american_atlantic["Sea Level Rise"]["Data Sources"] = [
"Tide gauge records (NOAA).",
"Satellite altimetry (NASA, ESA).",
"Sediment Elevation Tables (SETs).",
"USGS data.",
"Research publications."
]
salt_marshes_north_american_atlantic["Sea Level Rise"]["Impact on Area"] = "Inundation and submergence of low-lying marshes.; Landward migration (where possible).; Increased erosion.; \"Coastal squeeze\" where migration is blocked."
salt_marshes_north_american_atlantic["Sea Level Rise"]["Impact on Biodiversity"] = "Loss of habitat for marsh-dependent species.; Shifts in plant communities (towards more salt-tolerant species).; Reduced nesting habitat for birds (e.g., saltmarsh sparrow)."
salt_marshes_north_american_atlantic["Sea Level Rise"]["Influenced By"] = [
"Global Greenhouse Gas Emissions",
"Local Subsidence (in some areas)"
]
salt_marshes_north_american_atlantic["Sea Level Rise"]["Influences"] = [
"Salt Marshes (North American Atlantic Coast) - Coastal Erosion",
"Salt Marshes (North American Atlantic Coast) - Habitat Loss"
]
salt_marshes_north_american_atlantic["Sea Level Rise"]["Logic Description"] = "Sea level rise is a *critical* threat to North American Atlantic Coast salt marshes, with many areas experiencing high rates of relative sea level rise (global rise + local subsidence). \"Coastal squeeze\" is a major concern, as development prevents landward migration."
salt_marshes_north_american_atlantic["Sea Level Rise"]["Impact Function"] = "impact_sea_level_rise_north_american_atlantic_coast_salt_marshes"

salt_marshes_north_american_atlantic["Coastal Development"]["Metric"] = "Area of salt marsh converted to development (ha/year); length of hardened shoreline."
salt_marshes_north_american_atlantic["Coastal Development"]["Data Sources"] = [
"Remote sensing.",
"Land-use planning records."
]
salt_marshes_north_american_atlantic["Coastal Development"]["Impact on Area"] = "Direct loss of habitat; fragmentation; prevents landward migration."
salt_marshes_north_american_atlantic["Coastal Development"]["Impact on Biodiversity"] = "Loss of habitat.; Reduced nursery grounds for fish."
salt_marshes_north_american_atlantic["Coastal Development"]["Influenced By"] = [
"Urbanization",
"Infrastructure Development",
"\"Coastal Squeeze\""
]
salt_marshes_north_american_atlantic["Coastal Development"]["Influences"] = [
"Salt Marshes (North American Atlantic Coast) - Coastal Erosion",
"Salt Marshes (North American Atlantic Coast) - Habitat Loss"
]
salt_marshes_north_american_atlantic["Coastal Development"]["Logic Description"] = "Development directly removes marsh habitat and prevents landward migration in response to sea level rise."
salt_marshes_north_american_atlantic["Coastal Development"]["Impact Function"] = "impact_coastal_development_north_american_atlantic_coast_salt_marshes"

salt_marshes_north_american_atlantic["Altered Hydrology"]["Metric"] = "Changes in freshwater inflow; presence of ditches and drainage structures."
salt_marshes_north_american_atlantic["Altered Hydrology"]["Data Sources"] = [
"River gauge data.",
"Water management records."
]
salt_marshes_north_american_atlantic["Altered Hydrology"]["Impact on Area"] = "Changes in salinity.; Altered sedimentation."
salt_marshes_north_american_atlantic["Altered Hydrology"]["Impact on Biodiversity"] = "Shifts in plant communities.; Impacts on fish and invertebrates."
salt_marshes_north_american_atlantic["Altered Hydrology"]["Influenced By"] = [
"Ditching and Drainage (historical and ongoing).",
"Roads and Dikes.",
"Upstream Dams and Diversions."
]
salt_marshes_north_american_atlantic["Altered Hydrology"]["Influences"] = [
"Salt Marshes (North American Atlantic Coast) - Salinity",
"Salt Marshes (North American Atlantic Coast) - Sedimentation"
]
salt_marshes_north_american_atlantic["Altered Hydrology"]["Logic Description"] = "Altered hydrology impacts salinity, sedimentation, and habitat."
salt_marshes_north_american_atlantic["Altered Hydrology"]["Impact Function"] = "impact_altered_hydrology_north_american_atlantic_coast_salt_marshes"

salt_marshes_north_american_atlantic["Pollution"]["Metric"] = "Concentrations of nitrogen and phosphorus in water and sediments."
salt_marshes_north_american_atlantic["Pollution"]["Data Sources"] = [
"EPA data",
"State environmental agencies",
"Research publications"
]
salt_marshes_north_american_atlantic["Pollution"]["Impact on Area"] = "Eutrophication."
salt_marshes_north_american_atlantic["Pollution"]["Impact on Biodiversity"] = "Changes in plant communities (can favor invasive *Phragmites*). Reduced oxygen levels."
salt_marshes_north_american_atlantic["Pollution"]["Influenced By"] = [
"Agricultural Runoff",
"Urban Runoff",
"Wastewater Treatment Plants"
]
salt_marshes_north_american_atlantic["Pollution"]["Influences"] = [
"Salt Marshes (North American Atlantic Coast) - Water Quality",
"Salt Marshes (North American Atlantic Coast) - Plant Communities"
]
salt_marshes_north_american_atlantic["Pollution"]["Logic Description"] = "Nutrient pollution (primarily nitrogen) from agriculture and urban areas is a widespread problem, leading to eutrophication and changes in marsh vegetation."
salt_marshes_north_american_atlantic["Pollution"]["Impact Function"] = "impact_pollution_north_american_atlantic_coast_salt_marshes"

salt_marshes_north_american_atlantic["Invasive Species"]["Metric"] = "Extent and density of *Phragmites australis* stands."
salt_marshes_north_american_atlantic["Invasive Species"]["Data Sources"] = [
"Remote sensing.",
"Field surveys.",
"Research publications."
]
salt_marshes_north_american_atlantic["Invasive Species"]["Impact on Area"] = "*Phragmites* can outcompete native marsh vegetation, forming dense monocultures."
salt_marshes_north_american_atlantic["Invasive Species"]["Impact on Biodiversity"] = "Reduced plant diversity.; Loss of habitat for some native marsh animals.; Altered ecosystem processes."
salt_marshes_north_american_atlantic["Invasive Species"]["Influenced By"] = [
"Disturbance",
"Salt Marshes (North American Atlantic Coast) - Altered Hydrology",
"Salt Marshes (North American Atlantic Coast) - Pollution"
]
salt_marshes_north_american_atlantic["Invasive Species"]["Influences"] = [
"Salt Marshes (North American Atlantic Coast) - Native Plant Communities",
"Salt Marshes (North American Atlantic Coast) - Habitat Structure"
]
salt_marshes_north_american_atlantic["Invasive Species"]["Logic Description"] = "The invasive common reed, *Phragmites australis*, is a widespread problem, outcompeting native plants and altering habitat."
salt_marshes_north_american_atlantic["Invasive Species"]["Impact Function"] = "impact_invasive_species_north_american_atlantic_coast_salt_marshes"

# --- Salt Marshes (San Francisco Bay) ---
salt_marshes_san_francisco_bay = all_stressors_data["San Francisco Bay Salt Marshes"]

salt_marshes_san_francisco_bay["Historical Habitat Loss"]["Metric"] = "Area of salt marsh lost since pre-development times (a *very* large percentage)."
salt_marshes_san_francisco_bay["Historical Habitat Loss"]["Data Sources"] = [
"Historical maps and records.",
"Research publications.",
"San Francisco Estuary Institute (SFEI) data."
]
salt_marshes_san_francisco_bay["Historical Habitat Loss"]["Impact on Area"] = "*Massive* reduction in salt marsh area (over 90% in many parts of the Bay)."
salt_marshes_san_francisco_bay["Historical Habitat Loss"]["Impact on Biodiversity"] = "Loss of habitat for endangered species (e.g., salt marsh harvest mouse, Ridgway's rail).; Reduced nursery grounds for fish and shellfish.; Loss of coastal protection."
salt_marshes_san_francisco_bay["Historical Habitat Loss"]["Influenced By"] = [
"Historical Diking and Filling (for agriculture, salt production, and urban development)"
]
salt_marshes_san_francisco_bay["Historical Habitat Loss"]["Influences"] = [
"Salt Marshes (San Francisco Bay) - Current Habitat Availability",
"Exacerbates other stressors"
]
salt_marshes_san_francisco_bay["Historical Habitat Loss"]["Logic Description"] = "The San Francisco Bay has lost a *vast* majority of its historical salt marshes due to diking and filling for agriculture, salt ponds, and urban development. This historical loss is the *defining* characteristic of the ecosystem's current state and its vulnerability."
salt_marshes_san_francisco_bay["Historical Habitat Loss"]["Impact Function"] = "impact_historical_habitat_loss_sf_bay"

salt_marshes_san_francisco_bay["Sea Level Rise"]["Metric"] = "Rate of sea level rise (mm/year); marsh elevation; accretion rates."
salt_marshes_san_francisco_bay["Sea Level Rise"]["Data Sources"] = [
"Tide gauge records.",
"Satellite altimetry.",
"Sediment core analysis.",
"SFEI data."
]
salt_marshes_san_francisco_bay["Sea Level Rise"]["Impact on Area"] = "Inundation and erosion of remaining marshes; \"coastal squeeze\"."
salt_marshes_san_francisco_bay["Sea Level Rise"]["Impact on Biodiversity"] = "Further habitat loss.; Shifts in species composition."
salt_marshes_san_francisco_bay["Sea Level Rise"]["Influenced By"] = [
"Global Greenhouse Gas Emissions",
"Local Subsidence (in some areas)"
]
salt_marshes_san_francisco_bay["Sea Level Rise"]["Influences"] = [
"Salt Marshes (San Francisco Bay) - Coastal Erosion",
"Salt Marshes (San Francisco Bay) - Habitat Loss"
]
salt_marshes_san_francisco_bay["Sea Level Rise"]["Logic Description"] = "Sea level rise is a growing threat, exacerbating the impacts of historical habitat loss and making restoration efforts more challenging."
salt_marshes_san_francisco_bay["Sea Level Rise"]["Impact Function"] = "impact_sea_level_rise_sf_bay"

salt_marshes_san_francisco_bay["Invasive Species"]["Metric"] = "Extent and density of invasive *Spartina* (cordgrass) stands."
salt_marshes_san_francisco_bay["Invasive Species"]["Data Sources"] = [
"Remote sensing data (hyperspectral imagery).",
"Field surveys.",
"San Francisco Estuary Invasive Spartina Project data."
]
salt_marshes_san_francisco_bay["Invasive Species"]["Impact on Area"] = "*Spartina alterniflora* and its hybrids can outcompete native marsh vegetation and alter sediment dynamics. It can *increase* overall vegetated area in some cases, but in a way that is detrimental to the native ecosystem."
salt_marshes_san_francisco_bay["Invasive Species"]["Impact on Biodiversity"] = "Loss of native plant diversity (especially *Spartina foliosa*, the native Pacific cordgrass). Changes in habitat structure. Impacts on invertebrate and bird communities."
salt_marshes_san_francisco_bay["Invasive Species"]["Influenced By"] = [
"Intentional Introduction: *Spartina alterniflora* was intentionally introduced for erosion control.",
"Hybridization: Hybridization with native *Spartina foliosa* has created more aggressive forms.",
"Disturbance"
]
salt_marshes_san_francisco_bay["Invasive Species"]["Influences"] = [
"Salt Marshes (San Francisco Bay) - Native Plant Communities",
"Salt Marshes (San Francisco Bay) - Sediment Dynamics",
"Salt Marshes (San Francisco Bay) - Habitat Structure"
]
salt_marshes_san_francisco_bay["Invasive Species"]["Logic Description"] = "Invasive *Spartina* species, particularly hybrids between the introduced *Spartina alterniflora* and the native *Spartina foliosa*, are a major problem in San Francisco Bay, outcompeting native plants and altering mudflat and marsh habitats."
salt_marshes_san_francisco_bay["Invasive Species"]["Impact Function"] = "impact_invasive_species_sf_bay"

salt_marshes_san_francisco_bay["Pollution"]["Metric"] = "Concentrations of pollutants (e.g., heavy metals, legacy contaminants, nutrients) in water, sediments, and biota."
salt_marshes_san_francisco_bay["Pollution"]["Data Sources"] = [
"San Francisco Estuary Institute (SFEI) Regional Monitoring Program (RMP).",
"State Water Resources Control Board data.",
"Research studies."
]
salt_marshes_san_francisco_bay["Pollution"]["Impact on Area"] = "Degradation of water and sediment quality; contamination of the food web."
salt_marshes_san_francisco_bay["Pollution"]["Impact on Biodiversity"] = "Toxic effects on wildlife; bioaccumulation of pollutants; impacts on sensitive species."
salt_marshes_san_francisco_bay["Pollution"]["Influenced By"] = [
"Urban Runoff",
"Industrial Discharge (historical and ongoing)",
"Legacy Pollutants",
"Agricultural Runoff"
]
salt_marshes_san_francisco_bay["Pollution"]["Influences"] = [
"Salt Marshes (San Francisco Bay) - Water Quality",
"Salt Marshes (San Francisco Bay) - Wildlife Health"
]
salt_marshes_san_francisco_bay["Pollution"]["Logic Description"] = "The San Francisco Bay is surrounded by a large urban and industrial area, and pollution from runoff, industrial discharge, and legacy contaminants is a concern."
salt_marshes_san_francisco_bay["Pollution"]["Impact Function"] = "impact_pollution_sf_bay"

salt_marshes_san_francisco_bay["Altered Hydrology"]["Metric"] = "Changes to tidal and freshwater flows"
salt_marshes_san_francisco_bay["Altered Hydrology"]["Data Sources"] = [
"Water management records.",
"Research"
]
salt_marshes_san_francisco_bay["Altered Hydrology"]["Impact on Area"] = "Changes in salinity and sedimentation"
salt_marshes_san_francisco_bay["Altered Hydrology"]["Impact on Biodiversity"] = "Species shifts"
salt_marshes_san_francisco_bay["Altered Hydrology"]["Influenced By"] = [
"Water diversions",
"Levees"
]
salt_marshes_san_francisco_bay["Altered Hydrology"]["Influences"] = [
"Salt Marshes (San Francisco Bay) - Salinity",
"Salt Marshes (San Francisco Bay) - Sedimentation"
]
salt_marshes_san_francisco_bay["Altered Hydrology"]["Logic Description"] = "Alterations to water flow impacts the system."
salt_marshes_san_francisco_bay["Altered Hydrology"]["Impact Function"] = "impact_altered_hydrology_sf_bay"

# --- Seagrass (Australian) ---
seagrass_australian = all_stressors_data["Australian Seagrass"]


seagrass_australian["Climate Change"]["Metric"] = "Sea surface temperature (SST); frequency and severity of marine heatwaves; ocean acidification (pH); sea level rise; changes in storm intensity."
seagrass_australian["Climate Change"]["Data Sources"] = [
"Australian Bureau of Meteorology (BOM) data.",
"CSIRO research.",
"Climate models.",
"Research publications."
]
seagrass_australian["Climate Change"]["Impact on Area"] = "Seagrass die-offs (have occurred during marine heatwaves); changes in seagrass distribution and abundance; increased vulnerability to other stressors."
seagrass_australian["Climate Change"]["Impact on Biodiversity"] = "Loss of seagrass habitat; impacts on associated species (fish, invertebrates, dugongs, turtles); shifts in species composition."
seagrass_australian["Climate Change"]["Influenced By"] = [
"Global Greenhouse Gas Emissions"
]
seagrass_australian["Climate Change"]["Influences"] = [
"Seagrass (Australian) - Marine Heatwaves",
"Seagrass (Australian) - Ocean Acidification",
"Seagrass (Australian) - Sea Level Rise",
"Seagrass (Australian) - Storm Damage"
]
seagrass_australian["Climate Change"]["Logic Description"] = "Climate change, particularly marine heatwaves, ocean acidification, and sea level rise, poses a significant threat to Australian seagrass meadows."
seagrass_australian["Climate Change"]["Impact Function"] = "impact_climate_change_seagrass_australian"

seagrass_australian["Water Quality Degradation"]["Metric"] = "Water clarity (turbidity); nutrient concentrations (nitrogen, phosphorus); concentrations of other pollutants (e.g., herbicides, heavy metals)."
seagrass_australian["Water Quality Degradation"]["Data Sources"] = [
"State government water quality monitoring programs (e.g., Queensland, Western Australia).",
"Research studies.",
"Reports from regional councils and natural resource management groups."
]
seagrass_australian["Water Quality Degradation"]["Impact on Area"] = "Reduced light penetration, hindering seagrass growth and survival; increased algal growth (competing with seagrass).; Loss of seagrass meadows."
seagrass_australian["Water Quality Degradation"]["Impact on Biodiversity"] = "Loss of seagrass habitat; impacts on associated species; reduced water quality for marine life."
seagrass_australian["Water Quality Degradation"]["Influenced By"] = [
"Agricultural Runoff (nutrients, sediments, pesticides)",
"Urban Runoff (nutrients, sediments, pollutants)",
"Industrial Discharge",
"Dredging",
"Coastal Development"
]
seagrass_australian["Water Quality Degradation"]["Influences"] = [
"Seagrass (Australian) - Light Availability",
"Seagrass (Australian) - Seagrass Health"
]
seagrass_australian["Water Quality Degradation"]["Logic Description"] = "Reduced water quality, primarily due to increased sediment and nutrient runoff from land-based sources, is a major threat to Australian seagrass meadows."
seagrass_australian["Water Quality Degradation"]["Impact Function"] = "impact_water_quality_degradation_seagrass_australian"

seagrass_australian["Physical Damage"]["Metric"] = "Area of seagrass damaged by boat propellers, anchors, dredging, or other physical disturbances."
seagrass_australian["Physical Damage"]["Data Sources"] = [
"Aerial photography.",
"Underwater surveys.",
"Research studies."
]
seagrass_australian["Physical Damage"]["Impact on Area"] = "Direct loss of seagrass; fragmentation of seagrass meadows."
seagrass_australian["Physical Damage"]["Impact on Biodiversity"] = "Habitat loss; reduced connectivity between seagrass patches; increased vulnerability to other stressors."
seagrass_australian["Physical Damage"]["Influenced By"] = [
"Boating Activity",
"Dredging",
"Coastal Construction",
"Fishing Gear"
]
seagrass_australian["Physical Damage"]["Influences"] = [
"Seagrass (Australian) - Habitat Fragmentation",
"Seagrass (Australian) - Seagrass Loss"
]
seagrass_australian["Physical Damage"]["Logic Description"] = "Physical damage from boating activities, dredging, and coastal construction directly impacts seagrass meadows."
seagrass_australian["Physical Damage"]["Impact Function"] = "impact_physical_damage_seagrass_australian"

seagrass_australian["Coastal Development"]["Metric"] = "Area of coastline developed; proximity of development to seagrass meadows; infrastructure development (ports, marinas)."
seagrass_australian["Coastal Development"]["Data Sources"] = [
"Government planning data.",
"Remote sensing data.",
"Research publications."
]
seagrass_australian["Coastal Development"]["Impact on Area"] = "Habitat loss; increased runoff and pollution; altered hydrology."
seagrass_australian["Coastal Development"]["Impact on Biodiversity"] = "Impacts on seagrass meadows and associated species due to habitat loss, reduced water quality, and increased disturbance."
seagrass_australian["Coastal Development"]["Influenced By"] = [
"Population Growth",
"Urbanization",
"Tourism Development",
"Industrial Development"
]
seagrass_australian["Coastal Development"]["Influences"] = [
"Seagrass (Australian) - Water Quality",
"Seagrass (Australian) - Habitat Loss"
]
seagrass_australian["Coastal Development"]["Logic Description"] = "Coastal development can lead to habitat loss and increased pollution, impacting nearby seagrass meadows."
seagrass_australian["Coastal Development"]["Impact Function"] = "impact_coastal_development_seagrass_australian"

seagrass_australian["Overfishing"]["Metric"] = "Fishing effort and catch of key species that interact with seagrass ecosystems (e.g., some fish and invertebrates)."
seagrass_australian["Overfishing"]["Data Sources"] = [
"Fisheries data (state and federal agencies).",
"Research studies."
]
seagrass_australian["Overfishing"]["Impact on Area"] = "Indirect effects on seagrass through trophic cascades (e.g., removal of species that control grazers)."
seagrass_australian["Overfishing"]["Impact on Biodiversity"] = "Changes in food web structure; potential impacts on seagrass health (if key grazers or predators are removed)."
seagrass_australian["Overfishing"]["Influenced By"] = ["Fishing Pressure"]
seagrass_australian["Overfishing"]["Influences"] = [
"Seagrass (Australian) - Food Web Dynamics"
]
seagrass_australian["Overfishing"]["Logic Description"] = "Overfishing can disrupt food web interactions within seagrass ecosystems, potentially impacting seagrass health."
seagrass_australian["Overfishing"]["Impact Function"] = "impact_overfishing_seagrass_australian"

# --- Seagrass (Florida Bay) ---
seagrass_florida_bay = all_stressors_data["Florida Bay Seagrass"]

seagrass_florida_bay["Water Quality Degradation"]["Metric"] = "Water clarity (turbidity); nutrient concentrations (nitrogen, phosphorus); salinity; chlorophyll *a* concentrations."
seagrass_florida_bay["Water Quality Degradation"]["Data Sources"] = [
"South Florida Water Management District (SFWMD) data.",
"Florida Department of Environmental Protection (FDEP) data.",
"National Park Service (Everglades National Park).",
"Research publications.",
"Florida Bay and Adjacent Marine Systems Science Program."
]
seagrass_florida_bay["Water Quality Degradation"]["Impact on Area"] = "*Widespread* seagrass loss due to reduced light penetration and algal blooms; hypersalinity events."
seagrass_florida_bay["Water Quality Degradation"]["Impact on Biodiversity"] = "Massive seagrass die-offs (have occurred repeatedly in Florida Bay).; Loss of habitat for fish, invertebrates, and endangered species like manatees.; Altered food webs.; Increased disease susceptibility."
seagrass_florida_bay["Water Quality Degradation"]["Influenced By"] = [
"Seagrass (Florida Bay) - Altered Hydrology",
"Seagrass (Florida Bay) - Agricultural Runoff (from the Everglades and other areas)",
"Seagrass (Florida Bay) - Urban Runoff",
"Seagrass (Florida Bay) - Climate Change (can exacerbate nutrient impacts)"
]
seagrass_florida_bay["Water Quality Degradation"]["Influences"] = [
"Seagrass (Florida Bay) - Light Availability",
"Seagrass (Florida Bay) - Algal Blooms",
"Seagrass (Florida Bay) - Seagrass Die-offs",
"Seagrass (Florida Bay) - Salinity Stress"
]
seagrass_florida_bay["Water Quality Degradation"]["Logic Description"] = "Water quality degradation, primarily due to altered freshwater inflow from the Everglades, nutrient pollution, and increased salinity, is the *major* driver of seagrass loss in Florida Bay.  This has led to large-scale die-offs and ecosystem shifts."
seagrass_florida_bay["Water Quality Degradation"]["Impact Function"] = "impact_water_quality_degradation_florida_bay"

seagrass_florida_bay["Physical Damage"]["Metric"] = "Area of seagrass scarred by boat propellers; number of boating accidents in seagrass areas."
seagrass_florida_bay["Physical Damage"]["Data Sources"] = [
"Aerial surveys.",
"Florida Fish and Wildlife Conservation Commission (FWC) data.",
"Research studies."
]
seagrass_florida_bay["Physical Damage"]["Impact on Area"] = "Direct damage and loss of seagrass; fragmentation of seagrass beds."
seagrass_florida_bay["Physical Damage"]["Impact on Biodiversity"] = "Habitat loss; reduced connectivity; increased vulnerability to other stressors."
seagrass_florida_bay["Physical Damage"]["Influenced By"] = [
"Boating Activity",
"Shallow Water Depths",
"Lack of Boater Education and Awareness"
]
seagrass_florida_bay["Physical Damage"]["Influences"] = [
"Seagrass (Florida Bay) - Habitat Fragmentation",
"Seagrass (Florida Bay) - Seagrass Loss"
]
seagrass_florida_bay["Physical Damage"]["Logic Description"] = "Boat propeller scarring is a significant problem in Florida Bay due to the shallow waters and extensive seagrass beds.  This damage can be long-lasting."
seagrass_florida_bay["Physical Damage"]["Impact Function"] = "impact_physical_damage_florida_bay"

seagrass_florida_bay["Climate Change"]["Metric"] = "Sea surface temperature (SST); ocean acidification (pH); sea level rise; changes in storm intensity."
seagrass_florida_bay["Climate Change"]["Data Sources"] = [
"Climate models.",
"Oceanographic data.",
"Historical records."
]
seagrass_florida_bay["Climate Change"]["Impact on Area"] = "Increased stress on seagrasses; potential for die-offs; changes in distribution."
seagrass_florida_bay["Climate Change"]["Impact on Biodiversity"] = "Impacts on seagrass and associated species; exacerbation of other stressors."
seagrass_florida_bay["Climate Change"]["Influenced By"] = ["Global GHG"]
seagrass_florida_bay["Climate Change"]["Influences"] = [
"Seagrass (Florida Bay) - Sea Level Rise",
"Seagrass (Florida Bay) - Ocean Acidification",
"Seagrass (Florida Bay) - Water Temperature"
]
seagrass_florida_bay["Climate Change"]["Logic Description"] = "Climate change impacts, including warming waters, acidification, and sea level rise, add to the existing stressors on Florida Bay's seagrass ecosystems."
seagrass_florida_bay["Climate Change"]["Impact Function"] = "impact_climate_change_florida_bay"

seagrass_florida_bay["Altered Hydrology"]["Metric"] = "Changes in freshwater inflow from the Everglades; salinity levels in Florida Bay."
seagrass_florida_bay["Altered Hydrology"]["Data Sources"] = [
"South Florida Water Management District (SFWMD) data.",
"USGS data.",
"Research publications."
]
seagrass_florida_bay["Altered Hydrology"]["Impact on Area"] = "Changes in salinity gradients; hypersalinity events (periods of extremely high salinity)."
seagrass_florida_bay["Altered Hydrology"]["Impact on Biodiversity"] = "Stress on seagrasses and associated species due to altered salinity; can lead to seagrass die-offs."
seagrass_florida_bay["Altered Hydrology"]["Influenced By"] = [
"Water Management Practices in South Florida",
"Everglades Restoration Projects",
"Seagrass (Florida Bay) - Climate Change (changes in rainfall and sea level)"
]
seagrass_florida_bay["Altered Hydrology"]["Influences"] = [
"Seagrass (Florida Bay) - Salinity Stress",
"Seagrass (Florida Bay) - Water Quality Degradation"
]
seagrass_florida_bay["Altered Hydrology"]["Logic Description"] = "Changes in freshwater inflow from the Everglades, due to water management practices and climate change, have significantly altered the salinity regime in Florida Bay, impacting seagrass ecosystems."
seagrass_florida_bay["Altered Hydrology"]["Impact Function"] = "impact_altered_hydrology_florida_bay"

seagrass_florida_bay["Overfishing"]["Metric"] = "Fishing effort; catch of key species that interact with seagrass ecosystems."
seagrass_florida_bay["Overfishing"]["Data Sources"] = [
"Fisheries data (Florida Fish and Wildlife Conservation Commission).",
"Research studies."
]
seagrass_florida_bay["Overfishing"]["Impact on Area"] = "Indirect effects on seagrass through trophic cascades."
seagrass_florida_bay["Overfishing"]["Impact on Biodiversity"] = "Changes in food web structure; potential impacts on seagrass health (if key grazers or predators are removed)."
seagrass_florida_bay["Overfishing"]["Influenced By"] = ["Fishing Pressure"]
seagrass_florida_bay["Overfishing"]["Influences"] = [
"Seagrass (Florida Bay) - Food Web Dynamics"
]
seagrass_florida_bay["Overfishing"]["Logic Description"] = "Overfishing can disrupt the food web within seagrass meadows."
seagrass_florida_bay["Overfishing"]["Impact Function"] = "impact_overfishing_florida_bay"

# --- Seagrass (Mediterranean) ---
seagrass_mediterranean = all_stressors_data["Mediterranean Seagrass"]

seagrass_mediterranean["Coastal Development"]["Metric"] = "Length of coastline developed (km); area of seagrass meadows lost or degraded due to development (ha/year)."
seagrass_mediterranean["Coastal Development"]["Data Sources"] = [
"National and regional government data (coastal zone management plans).",
"Remote sensing data (satellite imagery, aerial photography).",
"Research publications.",
"European Environment Agency (EEA) data."
]
seagrass_mediterranean["Coastal Development"]["Impact on Area"] = "Direct loss of seagrass habitat (due to construction, dredging, etc.).; Fragmentation of meadows.; Increased turbidity and pollution from runoff.; Altered hydrology."
seagrass_mediterranean["Coastal Development"]["Impact on Biodiversity"] = "Loss of habitat for numerous species (fish, invertebrates, etc.).; Reduced nursery grounds for commercially important fish.; Impacts on endangered species (e.g., *Pinna nobilis* fan mussel). Reduced carbon sequestration."
seagrass_mediterranean["Coastal Development"]["Influenced By"] = [
"Tourism (a *major* driver in the Mediterranean)",
"Urbanization",
"Port Expansion",
"Marina Construction"
]
seagrass_mediterranean["Coastal Development"]["Influences"] = [
"Seagrass (Mediterranean) - Habitat Loss",
"Seagrass (Mediterranean) - Water Quality",
"Seagrass (Mediterranean) - Habitat Fragmentation"
]
seagrass_mediterranean["Coastal Development"]["Logic Description"] = "Intense coastal development, driven largely by tourism, is a *major* threat to Mediterranean seagrass meadows, causing habitat loss, fragmentation, and increased pollution."
seagrass_mediterranean["Coastal Development"]["Impact Function"] = "impact_coastal_development_mediterranean"

seagrass_mediterranean["Pollution"]["Metric"] = "Concentrations of pollutants (nutrients, heavy metals, organic pollutants, plastics) in water, sediments, and seagrass tissues."
seagrass_mediterranean["Pollution"]["Data Sources"] = [
"National and regional monitoring programs.",
"Research studies.",
"European Union (EU) data (e.g., Water Framework Directive monitoring)."
]
seagrass_mediterranean["Pollution"]["Impact on Area"] = "Reduced water quality; eutrophication (nutrient enrichment); toxic effects on seagrass and associated organisms.; Plastic accumulation."
seagrass_mediterranean["Pollution"]["Impact on Biodiversity"] = "Impacts on seagrass growth and survival.; Shifts in species composition.; Bioaccumulation of pollutants in the food chain.; Harmful algal blooms."
seagrass_mediterranean["Pollution"]["Influenced By"] = [
"Agricultural Runoff (fertilizers, pesticides)",
"Urban Runoff",
"Industrial Discharge",
"Wastewater Treatment Plants (often inadequate in some areas)",
"Shipping (including oil spills and antifouling paints)"
]
seagrass_mediterranean["Pollution"]["Influences"] = [
"Seagrass (Mediterranean) - Water Quality",
"Seagrass (Mediterranean) - Seagrass Health",
"Seagrass (Mediterranean) - Eutrophication"
]
seagrass_mediterranean["Pollution"]["Logic Description"] = "Pollution from various sources degrades water quality and impacts seagrass meadows and associated organisms in the Mediterranean."
seagrass_mediterranean["Pollution"]["Impact Function"] = "impact_pollution_mediterranean"

seagrass_mediterranean["Climate Change"]["Metric"] = "Sea surface temperature (SST); frequency and intensity of marine heatwaves; ocean acidification; sea level rise."
seagrass_mediterranean["Climate Change"]["Data Sources"] = [
"Climate models.",
"Oceanographic data (buoys, satellites).",
"Research publications.",
"MedECC (Mediterranean Experts on Climate and Environmental Change) reports."
]
seagrass_mediterranean["Climate Change"]["Impact on Area"] = "Increased seagrass mortality (particularly during heatwaves).; Changes in seagrass distribution (some species may shift northwards).; Ocean acidification reduces the ability of seagrasses to build calcium carbonate structures (important for some species, like *Posidonia oceanica*).; Increased storm damage."
seagrass_mediterranean["Climate Change"]["Impact on Biodiversity"] = "Loss of seagrass habitat; impacts on associated species; shifts in species composition; increased vulnerability to other stressors."
seagrass_mediterranean["Climate Change"]["Influenced By"] = [
"Global Greenhouse Gas Emissions"
]
seagrass_mediterranean["Climate Change"]["Influences"] = [
"Seagrass (Mediterranean) - Marine Heatwaves",
"Seagrass (Mediterranean) - Ocean Acidification",
"Seagrass (Mediterranean) - Sea Level Rise",
"Seagrass (Mediterranean) - Storm Damage"
]
seagrass_mediterranean["Climate Change"]["Logic Description"] = "The Mediterranean Sea is warming rapidly, and climate change (including warming, acidification, and sea level rise) is a major threat to seagrass meadows."
seagrass_mediterranean["Climate Change"]["Impact Function"] = "impact_climate_change_mediterranean"

seagrass_mediterranean["Invasive Species"]["Metric"] = "Distribution and abundance of key invasive species (e.g., *Caulerpa taxifolia*, *Caulerpa cylindracea*, *Lophocladia lallemandii*)."
seagrass_mediterranean["Invasive Species"]["Data Sources"] = [
"Field surveys.",
"Research studies.",
"Marine protected area monitoring programs."
]
seagrass_mediterranean["Invasive Species"]["Impact on Area"] = "Some invasive algae (e.g., *Caulerpa* species) can overgrow and displace native seagrasses.; Altered habitat structure."
seagrass_mediterranean["Invasive Species"]["Impact on Biodiversity"] = "Loss of native seagrass; reduced biodiversity; changes in ecosystem functioning."
seagrass_mediterranean["Invasive Species"]["Influenced By"] = [
"Aquarium Trade (a major source of *Caulerpa* introductions)",
"Shipping (ballast water)",
"Climate Change (may favor some invasive species)",
"Seagrass (Mediterranean) - Pollution (can make native species more vulnerable)"
]
seagrass_mediterranean["Invasive Species"]["Influences"] = [
"Seagrass (Mediterranean) - Competition with Native Seagrass",
"Seagrass (Mediterranean) - Habitat Alteration"
]
seagrass_mediterranean["Invasive Species"]["Logic Description"] = "Invasive algae, particularly *Caulerpa* species, pose a significant threat to Mediterranean seagrass meadows, outcompeting native species and altering habitats."
seagrass_mediterranean["Invasive Species"]["Impact Function"] = "impact_invasive_species_mediterranean"

seagrass_mediterranean["Fishing Activities"]["Metric"] = "Trawling intensity (hours/year or area trawled); fishing effort (number of vessels); bycatch of seagrass and associated species."
seagrass_mediterranean["Fishing Activities"]["Data Sources"] = [
"Fisheries statistics (national and EU-level).",
"Vessel Monitoring System (VMS) data.",
"Research studies."
]
seagrass_mediterranean["Fishing Activities"]["Impact on Area"] = "*Trawling* is particularly destructive, physically uprooting seagrass and damaging the seabed.; Other fishing gear (e.g., gillnets) can also have impacts."
seagrass_mediterranean["Fishing Activities"]["Impact on Biodiversity"] = "Direct loss of seagrass; damage to associated species; destruction of benthic habitats."
seagrass_mediterranean["Fishing Activities"]["Influenced By"] = [
"Fishing Practices",
"Enforcement of Regulations (trawling is banned in some areas, but illegal trawling occurs)"
]
seagrass_mediterranean["Fishing Activities"]["Influences"] = [
"Seagrass (Mediterranean) - Physical Damage",
"Seagrass (Mediterranean) - Habitat Loss"
]
seagrass_mediterranean["Fishing Activities"]["Logic Description"] = "Bottom trawling is a *highly* destructive practice that has severely impacted seagrass meadows in the Mediterranean. Other fishing gear can also cause damage."
seagrass_mediterranean["Fishing Activities"]["Impact Function"] = "impact_fishing_activities_mediterranean"

seagrass_mediterranean["Anchoring"]["Metric"] = "Number of boats anchoring in seagrass meadows; area of seagrass damaged by anchors."
seagrass_mediterranean["Anchoring"]["Data Sources"] = [
"Observations (diver surveys).",
"Aerial photography (in some areas).",
"Research studies"
]
seagrass_mediterranean["Anchoring"]["Impact on Area"] = "Physical damage to seagrass from anchors and chains; uprooting of plants; creation of scars in the meadow."
seagrass_mediterranean["Anchoring"]["Impact on Biodiversity"] = "Localized loss of seagrass habitat; fragmentation of meadows; increased vulnerability to other stressors."
seagrass_mediterranean["Anchoring"]["Influenced By"] = [
"Boating Activity (recreational and commercial)",
"Tourism",
"Lack of Mooring Buoys"
]
seagrass_mediterranean["Anchoring"]["Influences"] = [
"Seagrass (Mediterranean) - Physical Damage",
"Seagrass (Mediterranean) - Habitat Fragmentation"
]
seagrass_mediterranean["Anchoring"]["Logic Description"] = "Anchoring, particularly in popular tourist areas, can cause significant localized damage to seagrass meadows."
seagrass_mediterranean["Anchoring"]["Impact Function"] = "impact_anchoring_mediterranean"

# --- Seagrass (Southeast Asian) ---
seagrass_southeast_asian = all_stressors_data["Southeast Asian Seagrass"]

seagrass_southeast_asian["Coastal Development"]["Metric"] = "Area of seagrass habitat converted to other land uses (aquaculture, ports, urban development) (ha/year); length of coastline with modified seagrass beds."
seagrass_southeast_asian["Coastal Development"]["Data Sources"] = [
"Remote sensing data.",
"Government planning documents (Indonesia, Philippines, Thailand, Malaysia, Vietnam, etc.).",
"Research publications.",
"NGO reports."
]
seagrass_southeast_asian["Coastal Development"]["Impact on Area"] = "Direct loss of seagrass habitat; fragmentation; altered hydrology."
seagrass_southeast_asian["Coastal Development"]["Impact on Biodiversity"] = "Loss of habitat for a wide range of species; reduced nursery grounds for fish and shellfish; impacts on endangered species (e.g., dugongs).; Loss of ecosystem services."
seagrass_southeast_asian["Coastal Development"]["Influenced By"] = [
"Aquaculture Expansion",
"Urbanization and Population Growth",
"Tourism Development",
"Industrial Development (ports, etc.)",
"Infrastructure Projects"
]
seagrass_southeast_asian["Coastal Development"]["Influences"] = [
"Seagrass (Southeast Asian) - Habitat Loss",
"Seagrass (Southeast Asian) - Water Quality",
"Seagrass (Southeast Asian) - Sedimentation"
]
seagrass_southeast_asian["Coastal Development"]["Logic Description"] = "Coastal development, driven by aquaculture, urbanization, tourism, and industrial expansion, is a *major* threat to seagrass meadows in Southeast Asia, leading to significant habitat loss and degradation."
seagrass_southeast_asian["Coastal Development"]["Impact Function"] = "impact_coastal_development_seagrass_southeast_asian"

seagrass_southeast_asian["Pollution"]["Metric"] = "Concentrations of pollutants (nutrients, sediments, heavy metals, pesticides, plastics) in water, sediment, and seagrass tissues."
seagrass_southeast_asian["Pollution"]["Data Sources"] = [
"Water quality monitoring data (often limited).",
"Research studies."
]
seagrass_southeast_asian["Pollution"]["Impact on Area"] = "Reduced water quality; increased turbidity (cloudiness); potential for toxic effects."
seagrass_southeast_asian["Pollution"]["Impact on Biodiversity"] = "Nutrient enrichment can lead to algal blooms that shade out seagrasses.; Sedimentation reduces light penetration.; Toxic pollutants can harm seagrass and associated fauna.; Plastic pollution can entangle and be ingested by marine animals."
seagrass_southeast_asian["Pollution"]["Influenced By"] = [
"Agricultural Runoff (fertilizers, pesticides, sediments)",
"Urban Runoff (sewage, stormwater, industrial effluent)",
"Aquaculture Effluent",
"Deforestation (increased sediment runoff)",
"Mining Activities"
]
seagrass_southeast_asian["Pollution"]["Influences"] = [
"Seagrass (Southeast Asian) - Water Quality",
"Seagrass (Southeast Asian) - Light Availability",
"Seagrass (Southeast Asian) - Seagrass Health"
]
seagrass_southeast_asian["Pollution"]["Logic Description"] = "Pollution from various sources, including agriculture, urban areas, aquaculture, deforestation, and mining, degrades water quality and impacts seagrass meadows and associated biodiversity."
seagrass_southeast_asian["Pollution"]["Impact Function"] = "impact_pollution_seagrass_southeast_asian"

seagrass_southeast_asian["Climate Change"]["Metric"] = "Sea surface temperature (SST); ocean acidification (pH); sea level rise; changes in storm intensity."
seagrass_southeast_asian["Climate Change"]["Data Sources"] = [
"Climate models.",
"Oceanographic data.",
"Research publications."
]
seagrass_southeast_asian["Climate Change"]["Impact on Area"] = "Potential for seagrass die-offs due to extreme temperatures.; Changes in seagrass distribution due to sea level rise.; Increased damage from storms."
seagrass_southeast_asian["Climate Change"]["Impact on Biodiversity"] = "Shifts in species distributions.; Increased stress on seagrasses and associated fauna.; Impacts on calcifying organisms due to ocean acidification."
seagrass_southeast_asian["Climate Change"]["Influenced By"] = ["Global GHG"]
seagrass_southeast_asian["Climate Change"]["Influences"] = [
"Seagrass (Southeast Asian) - Sea Level Rise",
"Seagrass (Southeast Asian) - Ocean Acidification",
"Seagrass (Southeast Asian) - Water Temperature"
]
seagrass_southeast_asian["Climate Change"]["Logic Description"] = "Climate change, including warming waters, acidification, sea level rise, and increased storm intensity, poses multiple threats to Southeast Asian seagrass meadows."
seagrass_southeast_asian["Climate Change"]["Impact Function"] = "impact_climate_change_seagrass_southeast_asian"

seagrass_southeast_asian["Destructive Fishing Practices"]["Metric"] = "Use of dynamite fishing, bottom trawling, and other destructive methods; damage to seagrass beds."
seagrass_southeast_asian["Destructive Fishing Practices"]["Data Sources"] = [
"Reports from local communities and fishers.",
"Underwater surveys.",
"Law enforcement data (often limited).",
"Research studies."
]
seagrass_southeast_asian["Destructive Fishing Practices"]["Impact on Area"] = "Direct physical damage to seagrass meadows; uprooting of plants."
seagrass_southeast_asian["Destructive Fishing Practices"]["Impact on Biodiversity"] = "Loss of seagrass habitat; impacts on associated fish and invertebrate communities."
seagrass_southeast_asian["Destructive Fishing Practices"]["Influenced By"] = [
"Poverty and Lack of Alternative Livelihoods",
"Weak Enforcement of Fisheries Regulations",
"Lack of Awareness"
]
seagrass_southeast_asian["Destructive Fishing Practices"]["Influences"] = [
"Seagrass (Southeast Asian) - Habitat Loss",
"Seagrass (Southeast Asian) - Physical Damage"
]
seagrass_southeast_asian["Destructive Fishing Practices"]["Logic Description"] = "Destructive fishing practices, such as dynamite fishing and bottom trawling, directly damage seagrass meadows and their associated biodiversity."
seagrass_southeast_asian["Destructive Fishing Practices"]["Impact Function"] = "impact_destructive_fishing_seagrass_southeast_asian"

seagrass_southeast_asian["Sedimentation"]["Metric"] = "Increased sediment loads in coastal waters; turbidity; sediment deposition rates on seagrass beds."
seagrass_southeast_asian["Sedimentation"]["Data Sources"] = [
"Water quality monitoring data.",
"Remote sensing data (measuring turbidity).",
"Research studies."
]
seagrass_southeast_asian["Sedimentation"]["Impact on Area"] = "Reduced light penetration, hindering seagrass growth; smothering of seagrass."
seagrass_southeast_asian["Sedimentation"]["Impact on Biodiversity"] = "Loss of seagrass habitat; impacts on associated species."
seagrass_southeast_asian["Sedimentation"]["Influenced By"] = [
"Deforestation (in coastal watersheds)",
"Coastal Development",
"Dredging",
"Poor Land Management Practices"
]
seagrass_southeast_asian["Sedimentation"]["Influences"] = [
"Seagrass (Southeast Asian) - Water Quality",
"Seagrass (Southeast Asian) - Light Availability",
"Seagrass (Southeast Asian) - Seagrass Growth"
]
seagrass_southeast_asian["Sedimentation"]["Logic Description"] = "Increased sedimentation, often due to deforestation, coastal development, and poor land management, reduces light penetration and can smother seagrass meadows."
seagrass_southeast_asian["Sedimentation"]["Impact Function"] = "impact_sedimentation_seagrass_southeast_asian"

seagrass_southeast_asian["Overfishing"]["Metric"] = "Fishing effort; catch of key species that interact with seagrass ecosystems (e.g., some herbivores and predators)."
seagrass_southeast_asian["Overfishing"]["Data Sources"] = [
"Fisheries data (often limited).",
"Research studies."
]
seagrass_southeast_asian["Overfishing"]["Impact on Area"] = "Indirect effects on seagrass through trophic cascades."
seagrass_southeast_asian["Overfishing"]["Impact on Biodiversity"] = "Changes in food web structure; potential impacts on seagrass health (if key grazers or predators are removed)."
seagrass_southeast_asian["Overfishing"]["Influenced By"] = [
"Fishing Pressure",
"Lack of Effective Management"
]
seagrass_southeast_asian["Overfishing"]["Influences"] = [
"Seagrass (Southeast Asian) - Food Web Dynamics"
]
seagrass_southeast_asian["Overfishing"]["Logic Description"] = "Overfishing can disrupt food web interactions within seagrass ecosystems."
seagrass_southeast_asian["Overfishing"]["Impact Function"] = "impact_overfishing_seagrass_southeast_asian"

# --- Aquatic (Seamounts) ---
seamounts = all_stressors_data["Seamounts"]

seamounts["Bottom Trawling"]["Metric"] = "Area of seamounts trawled (km²/year); frequency of trawling; damage to benthic communities (e.g., corals, sponges)."
seamounts["Bottom Trawling"]["Data Sources"] = [
"Fisheries data (often incomplete for seamounts).",
"Vessel Monitoring System (VMS) data (if available).",
"Underwater surveys (using ROVs or submersibles).",
"Research publications."
]
seamounts["Bottom Trawling"]["Impact on Area"] = "*Severe* physical destruction of benthic habitats; removal of habitat-forming species (e.g., corals, sponges)."
seamounts["Bottom Trawling"]["Impact on Biodiversity"] = "High mortality of benthic organisms, including long-lived and slow-growing species.; Loss of biodiversity hotspots.; Disruption of seamount food webs.; *Extremely* slow recovery rates (centuries or millennia)."
seamounts["Bottom Trawling"]["Influenced By"] = [
"Demand for Deep-Sea Fish (e.g., orange roughy, which often aggregate around seamounts).",
"Fishing Technology",
"Lack of Effective Management and Protection"
]
seamounts["Bottom Trawling"]["Influences"] = [
"Seamounts - Habitat Destruction (the primary impact)",
"Seamounts - Benthic Community Structure"
]
seamounts["Bottom Trawling"]["Logic Description"] = "Bottom trawling is *highly destructive* to seamount ecosystems, physically destroying fragile habitats and the diverse communities they support. Recovery from trawling impacts on seamounts can take centuries or even millennia."
seamounts["Bottom Trawling"]["Impact Function"] = "impact_bottom_trawling_seamounts"

seamounts["Deep-Sea Mining"]["Metric"] = "Area of seamounts licensed for exploration or exploitation (km²); concentrations of target minerals (e.g., cobalt crusts)."
seamounts["Deep-Sea Mining"]["Data Sources"] = [
"International Seabed Authority (ISA) data.",
"National government data.",
"Research publications.",
"Environmental Impact Assessments (EIAs)."
]
seamounts["Deep-Sea Mining"]["Impact on Area"] = "Potential for direct physical removal of seabed substrate (e.g., cobalt crusts); creation of sediment plumes."
seamounts["Deep-Sea Mining"]["Impact on Biodiversity"] = "Loss of unique and often endemic seamount species.; Destruction of habitat and associated communities.; Potential for long-term or irreversible damage."
seamounts["Deep-Sea Mining"]["Influenced By"] = [
"Global Demand for Minerals",
"Technological Advancements",
"International Regulations (ISA)"
]
seamounts["Deep-Sea Mining"]["Influences"] = [
"Seamounts - Habitat Destruction",
"Seamounts - Water Quality (sediment plumes)"
]
seamounts["Deep-Sea Mining"]["Logic Description"] = "Deep-sea mining, particularly for cobalt crusts, poses a significant threat to seamount ecosystems, involving the direct removal of the substrate and the destruction of unique and vulnerable communities."
seamounts["Deep-Sea Mining"]["Impact Function"] = "impact_deep_sea_mining_seamounts"

seamounts["Climate Change"]["Metric"] = "Changes in deep-sea temperature (°C); changes in ocean currents; changes in oxygen levels; ocean acidification (pH)."
seamounts["Climate Change"]["Data Sources"] = [
"Climate models.",
"Oceanographic data (sparse for seamounts).",
"Research publications."
]
seamounts["Climate Change"]["Impact on Area"] = "Changes in the physical and chemical environment of seamounts."
seamounts["Climate Change"]["Impact on Biodiversity"] = "Potential shifts in species distributions; impacts on physiology and reproduction; changes in food availability (due to changes in surface productivity and ocean currents).  Specific impacts are less well understood than for shallower ecosystems."
seamounts["Climate Change"]["Influenced By"] = [
"Global Greenhouse Gas Emissions"
]
seamounts["Climate Change"]["Influences"] = [
"Seamounts - Ocean Acidification",
"Seamounts - Ocean Currents",
"Seamounts - Oxygen Levels"
]
seamounts["Climate Change"]["Logic Description"] = "Climate change is expected to impact seamount ecosystems through changes in temperature, ocean currents, oxygen levels, and acidification, although the specific effects are less well understood than for shallow-water habitats."
seamounts["Climate Change"]["Impact Function"] = "impact_climate_change_seamounts"

seamounts["Plastic Pollution"]["Metric"] = "Concentrations of plastic debris (macroplastics, microplastics) on seamounts and in surrounding waters."
seamounts["Plastic Pollution"]["Data Sources"] = [
"Research surveys (using ROVs and submersibles).",
"Analysis of samples collected from seamounts.",
"Research publications."
]
seamounts["Plastic Pollution"]["Impact on Area"] = "Accumulation of plastic debris on seamounts."
seamounts["Plastic Pollution"]["Impact on Biodiversity"] = "Entanglement of marine animals; ingestion of plastic by seamount fauna; potential for toxic effects; potential for microplastics to enter the food web."
seamounts["Plastic Pollution"]["Influenced By"] = [
"Land-Based Sources of Plastic Pollution",
"Shipping Activities",
"Fishing Gear (lost or discarded)"
]
seamounts["Plastic Pollution"]["Influences"] = [
"Seamounts - Wildlife Mortality"
]
seamounts["Plastic Pollution"]["Logic Description"] = "Plastic pollution, even in remote seamount ecosystems, is a growing concern, with potential impacts on deep-sea life."
seamounts["Plastic Pollution"]["Impact Function"] = "impact_plastic_pollution_seamounts"

seamounts["Ocean Acidification"]["Metric"] = "Ocean pH; aragonite and calcite saturation states in deep water."
seamounts["Ocean Acidification"]["Data Sources"] = [
"Oceanographic data (sparse for seamounts).",
"Research publications."
]
seamounts["Ocean Acidification"]["Impact on Area"] = "Potential impacts on calcifying organisms (e.g., cold-water corals) found on seamounts."
seamounts["Ocean Acidification"]["Impact on Biodiversity"] = "May reduce the ability of some cold-water corals to build and maintain their skeletons; impacts on other calcifying organisms."
seamounts["Ocean Acidification"]["Influenced By"] = ["Global CO2"]
seamounts["Ocean Acidification"]["Influences"] = [
"Seamounts - Cold-Water Corals"
]
seamounts["Ocean Acidification"]["Logic Description"] = "Ocean acidification, driven by increased atmospheric CO2, poses a threat to calcifying organisms on seamounts, such as cold-water corals."
seamounts["Ocean Acidification"]["Impact Function"] = "impact_ocean_acidification_seamounts"

# --- Smaller Lakes and Ponds ---
smaller_lakes_and_ponds = all_stressors_data["Smaller Lakes and Ponds"]

smaller_lakes_and_ponds["Nutrient Pollution (Eutrophication)"]["Metric"] = "Concentrations of nitrogen and phosphorus (total nitrogen, total phosphorus) in water (µg/L or ppm); chlorophyll *a* concentration (µg/L - a measure of algal biomass); Secchi depth (meters - a measure of water clarity); dissolved oxygen levels (mg/L)."
smaller_lakes_and_ponds["Nutrient Pollution (Eutrophication)"]["Data Sources"] = [
    "Water quality monitoring programs (often conducted by government agencies, universities, and lake associations).",
   "Remote sensing data (can be used to estimate chlorophyll *a* and turbidity).",
    "Research studies."
]
smaller_lakes_and_ponds["Nutrient Pollution (Eutrophication)"]["Impact on Area"] = "Increased algal growth; reduced water clarity; oxygen depletion in bottom waters."
smaller_lakes_and_ponds["Nutrient Pollution (Eutrophication)"]["Impact on Biodiversity"] = "Harmful algal blooms (HABs), some of which produce toxins.; Loss of submerged aquatic vegetation (SAV) due to reduced light penetration.; Fish kills due to oxygen depletion.; Changes in fish and invertebrate communities (favoring species tolerant of low oxygen)."
smaller_lakes_and_ponds["Nutrient Pollution (Eutrophication)"]["Influenced By"] = [
    "Agricultural Runoff: Fertilizers and animal waste are major sources of nutrients.",
    "Urban Runoff: Sewage, stormwater, and industrial effluent.",
   "Atmospheric Deposition: Nitrogen compounds can enter lakes through rainfall.",
    "Internal Loading: Nutrients can be released from lake sediments under certain conditions.",
 "Climate Change: Warmer water temperatures can exacerbate eutrophication."
]
smaller_lakes_and_ponds["Nutrient Pollution (Eutrophication)"]["Influences"] = [
   "Smaller Lakes and Ponds - Harmful Algal Blooms",
    "Smaller Lakes and Ponds - Oxygen Depletion",
  "Smaller Lakes and Ponds - Water Clarity",
    "Smaller Lakes and Ponds - Fish Kills"
]
smaller_lakes_and_ponds["Nutrient Pollution (Eutrophication)"]["Logic Description"] = "Eutrophication, or nutrient enrichment, is a major problem in many freshwater lakes. Excess nutrients (primarily phosphorus and nitrogen) from agriculture, urban areas, and other sources fuel excessive algal growth, leading to reduced water clarity, oxygen depletion, harmful algal blooms, and impacts on aquatic life."
smaller_lakes_and_ponds["Nutrient Pollution (Eutrophication)"]["Impact Function"] = "impact_nutrient_pollution_smaller_lakes_and_ponds"

smaller_lakes_and_ponds["Climate Change"]["Metric"] = "Water temperature (°C); changes in lake ice cover (duration, thickness); changes in stratification (layering of water due to temperature differences); changes in precipitation and evaporation patterns."
smaller_lakes_and_ponds["Climate Change"]["Data Sources"] = [
  "Climate models.",
    "Long-term lake monitoring data (temperature, ice cover).",
    "Remote sensing data.",
  "Historical records."
]
smaller_lakes_and_ponds["Climate Change"]["Impact on Area"] = "Changes in lake thermal structure; altered water levels; changes in mixing patterns."
smaller_lakes_and_ponds["Climate Change"]["Impact on Biodiversity"] = "Shifts in species distributions (warm-water species may expand their range, while cold-water species may decline).; Increased stress on fish and other aquatic organisms.; Changes in phenology (timing of biological events).; Increased risk of algal blooms.; Impacts on lake ice ecosystems."
smaller_lakes_and_ponds["Climate Change"]["Influenced By"] = [
 "Global Greenhouse Gas Emissions."
]
smaller_lakes_and_ponds["Climate Change"]["Influences"] = [
"Smaller Lakes and Ponds - Eutrophication",
   "Smaller Lakes and Ponds - Lake Stratification",
 "Smaller Lakes and Ponds - Ice Cover",
   "Smaller Lakes and Ponds - Water Levels"
]
smaller_lakes_and_ponds["Climate Change"]["Logic Description"] = "Climate change is warming lake waters, altering ice cover, changing stratification patterns, and affecting water levels, with significant impacts on lake ecosystems and biodiversity."
smaller_lakes_and_ponds["Climate Change"]["Impact Function"] = "impact_climate_change_smaller_lakes_and_ponds"

smaller_lakes_and_ponds["Acidification"]["Metric"] = "Lake water pH; concentrations of acid-neutralizing capacity (ANC)."
smaller_lakes_and_ponds["Acidification"]["Data Sources"] = [
     "Water quality monitoring programs.",
  "Research studies."
]
smaller_lakes_and_ponds["Acidification"]["Impact on Area"] = "Lowered pH levels; reduced buffering capacity."
smaller_lakes_and_ponds["Acidification"]["Impact on Biodiversity"] = "Impacts on fish, invertebrates, and amphibians (many species are sensitive to low pH).; Changes in phytoplankton and zooplankton communities.; Loss of sensitive species."
smaller_lakes_and_ponds["Acidification"]["Influenced By"] = [
  "Acid Rain (caused by atmospheric pollution - sulfur dioxide and nitrogen oxides)",
    "Acid Mine Drainage (in areas with mining activity)",
 "Natural Acidity (in some regions with certain types of geology and soils)"
]
smaller_lakes_and_ponds["Acidification"]["Influences"] = [
    "Smaller Lakes and Ponds - Water Chemistry",
    "Smaller Lakes and Ponds - Aquatic Life"
]
smaller_lakes_and_ponds["Acidification"]["Logic Description"] = "Acidification, primarily due to acid rain (and in some areas, acid mine drainage), can lower the pH of smaller lakes and ponds, impacting aquatic life."
smaller_lakes_and_ponds["Acidification"]["Impact Function"] = "impact_acidification_smaller_lakes_and_ponds"

smaller_lakes_and_ponds["Invasive Species"]["Metric"] = "Distribution and abundance of key invasive species (e.g., Eurasian watermilfoil, zebra mussels, spiny water flea, certain fish species)."
smaller_lakes_and_ponds["Invasive Species"]["Data Sources"] = [
     "Lake monitoring programs (often conducted by government agencies, universities, and lake associations).",
   "Research studies."
]
smaller_lakes_and_ponds["Invasive Species"]["Impact on Area"] = "Changes in lake ecosystems."
smaller_lakes_and_ponds["Invasive Species"]["Impact on Biodiversity"] = "Competition with native species.; Predation on native species.; Alteration of habitat.; Changes in food web structure.; Economic impacts (e.g., clogging water intakes)."
smaller_lakes_and_ponds["Invasive Species"]["Influenced By"] = [
    "Ballast Water Discharge: From ships.",
     "Recreational Boating: Transport of species between water bodies.",
   "Aquarium Releases.",
     "Intentional Introductions (for some species, historically).",
 "Climate Change"
]
smaller_lakes_and_ponds["Invasive Species"]["Influences"] = [
    "Smaller Lakes and Ponds - Native Species Populations.",
   "Smaller Lakes and Ponds - Water Quality (in some cases).",
    "Smaller Lakes and Ponds - Ecosystem Functioning."
]
smaller_lakes_and_ponds["Invasive Species"]["Logic Description"] = "Invasive species can have significant impacts on freshwater lakes, outcompeting native species, altering food webs, and causing economic damage."
smaller_lakes_and_ponds["Invasive Species"]["Impact Function"] = "impact_invasive_species_smaller_lakes_and_ponds"

smaller_lakes_and_ponds["Habitat Alteration"]["Metric"] = "Loss of shoreline vegetation; development along lake shores; removal of submerged aquatic vegetation (SAV); construction of docks and other structures."
smaller_lakes_and_ponds["Habitat Alteration"]["Data Sources"] = [
 "Remote sensing data.",
  "Shoreline surveys.",
   "Land-use planning records.",
   "Research studies."
]
smaller_lakes_and_ponds["Habitat Alteration"]["Impact on Area"] = "Loss of critical habitat for fish, amphibians, invertebrates, and birds.; Increased erosion; altered water quality."
smaller_lakes_and_ponds["Habitat Alteration"]["Impact on Biodiversity"] = "Reduced spawning habitat for fish.; Loss of shelter and food sources for aquatic organisms.; Impacts on shoreline-dependent species (e.g., birds, amphibians).; Reduced water quality"
smaller_lakes_and_ponds["Habitat Alteration"]["Influenced By"] = [
  "Residential Development",
 "Recreational Development",
  "Shoreline Modification (e.g., seawalls, riprap)",
   "Vegetation Removal"
]
smaller_lakes_and_ponds["Habitat Alteration"]["Influences"] = [
 "Smaller Lakes and Ponds - Habitat Loss",
  "Smaller Lakes and Ponds - Water Quality"
]
smaller_lakes_and_ponds["Habitat Alteration"]["Logic Description"] = "Alteration of shoreline and nearshore habitats, due to development and other human activities, degrades critical habitat for aquatic and terrestrial species."
smaller_lakes_and_ponds["Habitat Alteration"]["Impact Function"] = "impact_habitat_alteration_smaller_lakes_and_ponds"

smaller_lakes_and_ponds["Water Withdrawals"]["Metric"] = "Volume of water withdrawn; lake levels."
smaller_lakes_and_ponds["Water Withdrawals"]["Data Sources"] = [
    "Water permits",
     "Government agencies"
]
smaller_lakes_and_ponds["Water Withdrawals"]["Impact on Area"] = "Reduced lake levels"
smaller_lakes_and_ponds["Water Withdrawals"]["Impact on Biodiversity"] = "Habitat loss; changes in species."
smaller_lakes_and_ponds["Water Withdrawals"]["Influenced By"] = [
     "Agriculture",
    "Urban use",
   "Industry"
]
smaller_lakes_and_ponds["Water Withdrawals"]["Influences"] = [
        "Smaller Lakes and Ponds - Water availability"
]
smaller_lakes_and_ponds["Water Withdrawals"]["Logic Description"] = "Water being pulled out impacts."
smaller_lakes_and_ponds["Water Withdrawals"]["Impact Function"] = "impact_water_withdrawals_smaller_lakes_and_ponds"

smaller_lakes_and_ponds["Pollution"]["Metric"] = "Concentration of pollutants"
smaller_lakes_and_ponds["Pollution"]["Data Sources"] = ["Water quality monitoring."]
smaller_lakes_and_ponds["Pollution"]["Impact on Area"] = "Contamination"
smaller_lakes_and_ponds["Pollution"]["Impact on Biodiversity"] = "Toxic effects"
smaller_lakes_and_ponds["Pollution"]["Influenced By"] = [
   "Industrial discharge",
    "Agricultural Runoff",
    "Urban Runoff"
]
smaller_lakes_and_ponds["Pollution"]["Influences"] = [
       "Smaller Lakes and Ponds - Water Quality",
        "Wildlife health"
]
smaller_lakes_and_ponds["Pollution"]["Logic Description"] = "Many different pollutants impact."
smaller_lakes_and_ponds["Pollution"]["Impact Function"] = "impact_pollution_smaller_lakes_and_ponds"