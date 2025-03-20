# stressor_templates.py

# --- Templates for Stressor Definitions ---

# These are dictionaries that serve as templates for defining stressors.
# We use copy.deepcopy() to create instances of these templates in all_stressors.py,
# avoiding unintended modifications to the templates themselves.

# --- General Templates ---

climate_change_template = {
    "Metric": "Define the metric used to measure the stressor (e.g., temperature change in degrees Celsius).",
    "Data Sources": ["List data sources (e.g., IPCC reports, specific climate models, observational datasets)."],
    "Impact on Area": "Describe the impact of the stressor on the geographic area of the ecosystem.",
    "Impact on Biodiversity": "Describe the impact on biodiversity (species, genetic diversity, ecosystem function).",
    "Influenced By": ["List other stressors that influence this one (e.g., deforestation, greenhouse gas emissions)."],
    "Influences": ["List other stressors that this one influences (e.g., wildfires, sea level rise)."],
    "Logic Description": "Provide a concise explanation of the causal chain: how the stressor works and its impacts.",
    "Impact Function": "Name of the Python function that will calculate the stressor's impact (to be defined later)."
}

deforestation_template = {
    "Metric": "Area of forest cleared per year (e.g., hectares/year).",
    "Data Sources": ["List data sources (e.g., Global Forest Watch, national forest inventories)."],
    "Impact on Area": "Direct reduction of forest area.",
    "Impact on Biodiversity": "Habitat loss and fragmentation, leading to species decline and loss of ecosystem services.",
    "Influenced By": ["List factors driving deforestation (e.g., agricultural expansion, logging, mining)."],
    "Influences": ["List other stressors affected by deforestation (e.g., wildfires, climate change)."],
    "Logic Description": "Explain the process and consequences of deforestation.",
    "Impact Function": "Name of the impact function."
}

land_use_change_template = {
    "Metric": "Area of land converted (e.g., hectares/year), type of conversion.",
    "Data Sources":["List Data Sources"],
    "Impact on Area": "Describe impact on area.",
    "Impact on Biodiversity": "Describe impact on biodiversity.",
    "Influenced By": ["List influences"],
    "Influences": ["List what is influenced"],
    "Logic Description": "Describe the logic of how this stressor works",
    "Impact Function": "Name of impact function"
}

fire_regime_template = {
    "Metric": "Fire frequency, intensity, seasonality, and area burned.",
    "Data Sources": ["List data sources (e.g., satellite data, fire records)."],
    "Impact on Area": "Direct loss of vegetation and changes in ecosystem structure.",
    "Impact on Biodiversity": "Mortality of plants and animals, habitat loss, changes in species composition.",
    "Influenced By": ["List factors influencing fire regimes (e.g., climate change, deforestation, human ignitions)."],
    "Influences": ["List other stressors affected by fire (e.g., air quality, carbon emissions)."],
    "Logic Description": "Explain the role of fire in the ecosystem and the impacts of altered fire regimes.",
    "Impact Function": "Name of the impact function."
}

overfishing_template = {
    "Metric": "Catch per unit effort (CPUE), fish biomass, size/age structure of fish populations.",
    "Data Sources": ["List data sources (e.g., fisheries data, stock assessments)."],
    "Impact on Area": "Not directly applicable, but affects ecosystem structure.",
    "Impact on Biodiversity": "Decline of fish populations, disruption of food webs, impacts on other marine life.",
    "Influenced By": ["List factors influencing overfishing (e.g., fishing pressure, lack of regulation)."],
    "Influences": ["List other stressors affected by overfishing (e.g., coral reef health, algal blooms)."],
    "Logic Description": "Explain the consequences of overfishing on fish populations and the ecosystem.",
    "Impact Function": "Name of the impact function."
}
# Added a unique identifier for the fishing stressor
overfishing_template["Stressor ID"] = "fishing"

pollution_template = {
    "Metric": "Concentrations of various pollutants (e.g., nutrients, heavy metals, pesticides) in water, soil, and biota.",
    "Data Sources": ["List data sources (e.g., water quality monitoring data, pollution reports)."],
    "Impact on Area": "Degradation of water and soil quality, contamination of ecosystems.",
    "Impact on Biodiversity": "Toxic effects on organisms, reduced reproductive success, bioaccumulation of pollutants.",
    "Influenced By": ["List sources of pollution (e.g., agriculture, industry, sewage)."],
    "Influences": ["List other stressors affected by pollution (e.g., water quality, human health)."],
    "Logic Description": "Explain the sources, pathways, and effects of pollution.",
    "Impact Function": "Name of the impact function."
}

infrastructure_development_template = {
    "Metric": "Area of land developed, length of roads built, number of dams, etc.",
    "Data Sources": ["List data sources"],
    "Impact on Area": "Describe impact on area.",
    "Impact on Biodiversity": "Describe impact on biodiversity.",
    "Influenced By": ["List influences"],
    "Influences": ["List what is influenced"],
    "Logic Description": "Describe the logic of how this stressor works",
    "Impact Function": "Name of impact function"
}

invasive_species_template = {
    "Metric": "Abundance and distribution of invasive species, impacts on native species.",
    "Data Sources": ["List data sources"],
    "Impact on Area": "Describe impact on area.",
    "Impact on Biodiversity": "Describe impact on biodiversity.",
    "Influenced By": ["List influences"],
    "Influences": ["List what is influenced"],
    "Logic Description": "Describe the logic of how this stressor works",
    "Impact Function": "Name of impact function"
}
water_extraction_template = {
    "Metric": "Volume of water extracted.",
    "Data Sources":["List data sources"],
    "Impact on Area": "Reduced water availability.",
    "Impact on Biodiversity": "Describe impact on biodiversity.",
    "Influenced By": ["List influences"],
    "Influences": ["List what is influenced"],
    "Logic Description": "Describe the logic of how this stressor works",
    "Impact Function": "Name of impact function"
}

altered_hydrology_template = {
   "Metric":"Changes in flow regime",
    "Data Sources":["List data sources"],
    "Impact on Area":"Describe impact on area",
    "Impact on Biodiversity":"Describe impact on biodiversity",
    "Influenced By":["List Influences"],
    "Influences":["List what is influenced"],
    "Logic Description": "Describe the logic of how this stressor works",
    "Impact Function": "Name of impact function"

}

overgrazing_template = {
    "Metric": "Livestock Density",
    "Data Sources": ["List data sources"],
    "Impact on Area": "Describe impact on area",
    "Impact on Biodiversity":"Describe impact on biodiversity",
    "Influenced By": ["List Influences"],
    "Influences": ["List what is influenced"],
    "Logic Description": "Describe the logic",
    "Impact Function": "Name of impact function"
}

permafrost_thaw_template = {
     "Metric": "Active layer thickness",
    "Data Sources": ["List data sources"],
    "Impact on Area": "Describe impact on area",
    "Impact on Biodiversity":"Describe impact on biodiversity",
    "Influenced By": ["List Influences"],
    "Influences": ["List what is influenced"],
    "Logic Description": "Explain",
    "Impact Function": "Name of impact function"
}

sea_ice_loss_template = {
 "Metric": "Sea ice extent, thickness, duration.",
    "Data Sources": ["List data sources"],
    "Impact on Area": "Describe impact on area",
    "Impact on Biodiversity": "Describe impact on biodiversity",
    "Influenced By":["List Influences"],
    "Influences": ["List what is influenced"],
    "Logic Description": "Explain",
    "Impact Function": "Name of impact function"
}

poaching_template = {
     "Metric": "Number of illegally killed animals.",
    "Data Sources":["List data sources"],
    "Impact on Area": "Indirect",
    "Impact on Biodiversity": "Describe impact on biodiversity",
    "Influenced By": ["List Influences"],
    "Influences": ["List what is influenced"],
    "Logic Description": "Describe the logic",
    "Impact Function": "Name of impact function"
}

ocean_acidification_template = {
   "Metric": "Changes to PH levels",
    "Data Sources": ["List data sources"],
    "Impact on Area": "Describe impact on area.",
    "Impact on Biodiversity": "Describe impact on biodiversity.",
    "Influenced By": ["List influences"],
    "Influences": ["List what is influenced"],
    "Logic Description": "Describe the logic of how this stressor works",
    "Impact Function": "Name of impact function"
}

mining_template = {
   "Metric": "Area affected by mining; pollutant levels",
    "Data Sources": ["List data sources"],
    "Impact on Area": "Describe impact on area.",
    "Impact on Biodiversity": "Describe impact on biodiversity.",
    "Influenced By": ["List influences"],
    "Influences": ["List what is influenced"],
    "Logic Description": "Describe the logic of how this stressor works",
    "Impact Function": "Name of impact function"
}

eutrophication_template = {
   "Metric": "Nutrient Levels",
    "Data Sources": ["List data sources"],
    "Impact on Area": "Describe impact on area.",
    "Impact on Biodiversity": "Describe impact on biodiversity.",
    "Influenced By": ["List influences"],
    "Influences": ["List what is influenced"],
    "Logic Description": "Describe the logic of how this stressor works",
    "Impact Function": "Name of impact function"
}

fragmentation_template = {
"Metric": "Patch size, edge density, connectivity",
 "Data Sources": ["List data sources"],
 "Impact on Area": "Describe impact.",
 "Impact on Biodiversity": "Describe impact.",
 "Influenced By": ["List influences"],
 "Influences": ["List what is influenced"],
 "Logic Description": "Describe the logic.",
 "Impact Function": "Name of impact function"
}

sedimentation_template = {
 "Metric":"Sediment load/deposition rates",
"Data Sources":["List data sources"],
"Impact on Area": "Describe impact.",
"Impact on Biodiversity": "Describe impact.",
"Influenced By": ["List influences"],
"Influences": ["List what is influenced"],
"Logic Description": "Describe the logic.",
"Impact Function": "Name of impact function"
}

# --- Ecosystem-Specific Templates (if needed) ---
# Add more specific templates here if certain ecosystems require unique
# stressor definitions. For example:

# peatland_degradation_template = { ... }

# --- Additional Templates ---
air_pollution_template = {
    "Metric": "Concentrations of pollutants (e.g., ozone, nitrogen oxides, sulfur dioxide, particulate matter).",
    "Data Sources": ["List data sources (e.g., air quality monitoring networks)."],
    "Impact on Area": "Describe impact on area (e.g., reduced forest health, damage to vegetation).",
    "Impact on Biodiversity": "Describe impact on biodiversity (e.g., damage to sensitive species, changes in species composition).",
    "Influenced By": ["List sources of air pollution (e.g., industrial emissions, vehicle emissions)."],
    "Influences": ["List other stressors affected by air pollution (e.g., water quality, soil acidification)."],
    "Logic Description": "Explain the sources, pathways, and effects of air pollution.",
    "Impact Function": "Name of the impact function."
}

# A more general template for overexploitation, applicable to hunting, etc.
overexploitation_template = {
    "Metric": "Population declines of targeted species; harvest rates.",
    "Data Sources": ["List data sources (e.g., wildlife surveys, hunting records)."],
    "Impact on Area": "Indirect, through changes in species populations and ecological interactions.",
    "Impact on Biodiversity": "Decline of targeted species; disruption of ecological processes.",
    "Influenced By": ["List factors driving overexploitation (e.g., hunting, poaching, illegal trade)."],
    "Influences": ["List other stressors affected (e.g., seed dispersal, forest regeneration)."],
    "Logic Description": "Explain the consequences of overexploitation on targeted species and the ecosystem.",
    "Impact Function": "Name of the impact function."
}

# Template to cover water stress
water_stress_template = {
 "Metric": "Indicators of water stress",
 "Data Sources": ["List data sources"],
 "Impact on Area": "Describe.",
 "Impact on Biodiversity": "Describe impact.",
 "Influenced By": ["List influences"],
 "Influences": ["List what is influenced"],
 "Logic Description": "Describe the logic.",
 "Impact Function": "Name of impact function"
}

desertification_template = {
    "Metric": "Indicators of desertification (e.g., vegetation cover, soil erosion, dust storm frequency).",
    "Data Sources": ["List data sources"],
    "Impact on Area": "Describe impact on area (e.g., land degradation, loss of productivity).",
    "Impact on Biodiversity": "Describe impact on biodiversity (e.g., loss of habitat, species decline).",
    "Influenced By": ["List factors driving desertification (e.g., climate change, overgrazing, deforestation)."],
    "Influences": ["List other stressors affected by desertification (e.g., water scarcity, dust storms)."],
    "Logic Description": "Explain the process of desertification and its consequences.",
    "Impact Function": "Name of the impact function."
}
governance_template = {
    "Metric": "Indicators of political stability/governance.",
    "Data Sources":["List Data Sources"],
    "Impact on Area": "Variable",
    "Impact on Biodiversity": "Variable.",
    "Influenced By":["List influences"],
    "Influences": ["List what is influenced"],
    "Logic Description": "Describe the logic",
    "Impact Function": "Name of impact function"
}

fishing_template = {
    "Metric": "Fishing effort, catch of key species",
    "Data Sources": ["List data sources"],
    "Impact on Area": "Describe impact.",
    "Impact on Biodiversity": "Describe impact.",
    "Influenced By": ["List influences"],
    "Influences": ["List what is influenced"],
    "Logic Description": "Describe the logic.",
    "Impact Function": "Name of impact function"
}

urbanization_template = {
 "Metric": "Rate of urban expansion; population density; impervious surface area.",
 "Data Sources": ["List data sources"],
 "Impact on Area": "Habitat loss and fragmentation.",
 "Impact on Biodiversity": "Reduced biodiversity; increased human-wildlife conflict.",
 "Influenced By": ["List influences"],
 "Influences":["List what is influenced"],
 "Logic Description": "Explain how urbanization leads to environmental changes",
 "Impact Function": "Name of impact function"
}

destructive_fishing_template = {
    "Metric": "Frequency of destructive fishing events; area affected.",
    "Data Sources": ["List data sources (e.g., reports from local communities, underwater surveys)."],
    "Impact on Area": "Direct physical damage to habitats (e.g., coral reefs, seagrass beds).",
    "Impact on Biodiversity": "High mortality of marine organisms; destruction of habitats.",
    "Influenced By": ["List factors driving destructive practices (e.g., poverty, lack of enforcement)."],
    "Influences": ["List other stressors affected (e.g., habitat loss, fish populations)."],
    "Logic Description": "Explain the specific methods used (e.g., blast fishing, cyanide fishing) and their immediate and long-term consequences.",
    "Impact Function": "Name of the impact function."
}