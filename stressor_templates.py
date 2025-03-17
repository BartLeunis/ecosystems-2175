# stressor_templates.py

climate_change_template = {
    "Metric": "Temperature increase (°C); changes in precipitation patterns",
    "Data Sources": ["Climate models", "Historical weather records"],
    "Impact on Area": "Indirect; changes in habitat",
    "Impact on Biodiversity": "Shifts in species distributions, increased stress",
    "Influenced By": ["Global Greenhouse Gas Emissions"],
    "Influences": ["Various, depending on ecosystem"],
    "Logic Description": "Climate change impacts...",
    "Impact Function": "placeholder_climate_change_impact"
}

deforestation_template = {
    "Metric": "Area deforested annually (ha/year)",
    "Data Sources": ["Remote sensing data", "Governmental reports", "NGO reports"],
    "Impact on Area": "Direct reduction in forest area",
    "Impact on Biodiversity": "Habitat loss, fragmentation, reduced connectivity",
    "Influenced By": ["Infrastructure Development", "Economic Growth", "Global Commodity Prices", "Population Growth", "Government Policies"],
    "Influences": ["Habitat Fragmentation", "Edge Effects", "Soil Erosion","Hydrological Changes","Regional Climate Change", "Carbon Emissions" ],
    "Logic Description": "Deforestation directly reduces forest area, causing habitat loss.",
    "Impact Function": "placeholder_deforestation_impact"
}

infrastructure_development_template = {
    "Metric": "Road density (km/km²); area affected by development (ha/year)",
    "Data Sources": ["Government statistics", "Remote sensing", "Industry reports"],
    "Impact on Area": "Habitat fragmentation; direct loss",
    "Impact on Biodiversity": "Habitat loss, fragmentation, disruption of corridors",
    "Influenced By": ["Economic Growth", "Population Growth", "Government Policies"],
    "Influences": ["Deforestation", "Pollution", "Access for hunting/poaching"],
    "Logic Description": "Infrastructure development fragments habitat and facilitates other stressors.",
    "Impact Function": "placeholder_infrastructure_impact"
}

# Add more templates as needed (e.g., for Overfishing, Pollution, Invasive Species, etc.)
#  Make them as GENERAL as possible.

overfishing_template = {
    "Metric": "Fish catch (tonnes/year), stock assessments, bycatch",
    "Data Sources": ["Fisheries data", "Stock assessments", "Research"],
    "Impact on Area": "N/A - affects population sizes, not area directly",
    "Impact on Biodiversity": "Depletion of fish stocks, food web changes, bycatch impacts",
    "Influenced By": ["Demand for seafood", "Fishing technology", "Subsidies", "Illegal fishing", "Weak governance"],
    "Influences": ["Marine Food Webs", "Ecosystem Function"],
    "Logic Description": "Overfishing depletes stocks and disrupts food webs.",
    "Impact Function": "placeholder_overfishing_impact",
}
pollution_template = {
    "Metric": "Concentrations of pollutants",
    "Data Sources":["Monitoring programs","Research studies"],
    "Impact on Area": "Contamination of soil, water, and/or air.",
    "Impact on Biodiversity":"Toxic effects on organisms; bioaccumulation.",
    "Influenced By": ["Various, depending on the specific pollutant and ecosystem."],
    "Influences": ["Water Quality", "Wildlife health","Ecosystem health"],
    "Logic Description": "Pollution negatively impacts through toxic effects",
    "Impact Function": "placeholder_pollution_impact"
}
invasive_species_template = {
    "Metric":"Distribution and abundance of key invasive species.",
    "Data Sources": ["Field surveys", "Research studies", "Monitoring programs"],
    "Impact on Area": "Changes in ecosystem structure/composition.",
    "Impact on Biodiversity": "Competition, Predation, Disease transmission, Altered ecosystem processes.",
    "Influenced By":["Human activities, climate change, disturbance"],
    "Influences": ["Native species populations", "Ecosystem functioning"],
    "Logic Description": "Invasive species negatively impact biodiversity.",
    "Impact Function": "placeholder_invasive_species_impact"
}
water_extraction_template = {
    "Metric": "Volume of water extracted.",
    "Data Sources":["Government water resource agencies","Research Studies"],
    "Impact on Area": "Reduced water levels/flow",
    "Impact on Biodiversity": "Habitat loss/degradation.",
    "Influenced By":["Agricultural expansion", "Population growth", "Industrial activities"],
    "Influences":["Water availability", "Habitat quality"],
    "Logic Description": "Water extraction impacts biodiversity",
    "Impact Function": "placeholder_water_extraction_impact"
}

altered_hydrology_template = {
   "Metric":"Changes in flow regime",
    "Data Sources":["River gauge data","Hydrological models","Remote sensing"],
    "Impact on Area":"Changes in physical characteristics of the river channel",
    "Impact on Biodiversity":"Impacts on fish migration",
    "Influenced By":["Dams and reservoirs","Water diversions","Channelization","Land-use change","Climate change"],
    "Influences":["Water availability","Sediment transport","Habitat connectivity", "Water temperature"],
    "Logic Description":"Altered hydrology significantly impacts rivers and streams.",
    "Impact Function": "placeholder_altered_hydrology_impact"

}

fire_regime_template = {
   "Metric": "Fire Frequency, Area burned, fire intensity",
    "Data Sources": ["Remote Sensing", "Government agency data", "Local community Knowledge", "Research Studies"],
    "Impact on Area": "Changes in vegetation structure and composition",
    "Impact on Biodiversity": "Varies based on ecosystem, but generally alters habitat",
    "Influenced By": ["Climate change, Human activities, Land-use change", "Land Management Practices"],
    "Influences":["Vegetation structure, air quality, carbon cycle, future fire risk"],
    "Logic Description": "Changes to fire regime can shift vegetation",
    "Impact Function": "placeholder_fire_regime_impact"
}