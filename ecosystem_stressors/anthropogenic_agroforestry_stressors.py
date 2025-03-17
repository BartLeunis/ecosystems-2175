from stressor_templates import *
import copy

anthropogenic_agroforestry_stressors = {
    "Land Use Change": {},
    "Management Practices": {},
    "Climate Change": copy.deepcopy(climate_change_template),
    "Pest and Disease Outbreaks": {},
    "Soil Degradation": {},
    "Water Availability": {},
    "Market Access": {},
    "Farmer Knowledge and Skills": {},
    "Economic Incentives": {},
    "Government Policies": {},
    "Population Pressure": {},
    "Access to Resources": {},
    "Carbon Sequestration": {},
    "Tree and Crop Productivity": {},
    "Introduction of Exotic Species": {},
    "Erosion": {},
    "Water Use": {},
}

# --- Land Use Change ---
anthropogenic_agroforestry_stressors["Land Use Change"]["Metric"] = 'Conversion of natural forest or other land cover types to agroforestry systems; conversion of agroforestry to other land uses (e.g., monoculture agriculture, urban development).'
anthropogenic_agroforestry_stressors["Land Use Change"]["Data Sources"] = ['Remote sensing data (satellite imagery, aerial photography).', 'Land use/land cover maps.', 'Agricultural statistics.', 'Research publications.', '**Impact on Area:** Changes in land cover and landscape structure.  Can be *positive* (e.g., converting degraded land to agroforestry) or *negative* (e.g., converting forest to a simplified agroforestry system).', '**Impact on Biodiversity:**', 'Depends on the type of agroforestry system and the previous land use. Agroforestry can *increase* biodiversity compared to monoculture agriculture, but may *decrease* it compared to natural forest.', 'Can provide habitat for some species, but may not support specialized forest species.', '**Influenced By (Stressors):**', 'Agroforestry - Economic Incentives: Market demand for agroforestry products (e.g., timber, fruits, nuts, coffee, cocoa).', 'Agroforestry - Government Policies: Subsidies, regulations, land tenure.', 'Agroforestry - Population Pressure: Demand for land and resources.', 'Agroforestry - Climate Change: May influence the suitability of certain agroforestry systems.', '**Influences (Stressors):**', 'Habitat availability (for some species).', '**Logic Description:** Conversion of land *to* or *from* agroforestry can have significant impacts on biodiversity and ecosystem services, depending on the context.  Agroforestry can be more sustainable than intensive agriculture, but less biodiverse than natural forest.']
anthropogenic_agroforestry_stressors["Land Use Change"]["Impact on Area"] = 'Changes in land cover and landscape structure.  Can be *positive* (e.g., converting degraded land to agroforestry) or *negative* (e.g., converting forest to a simplified agroforestry system).'
anthropogenic_agroforestry_stressors["Land Use Change"]["Impact on Biodiversity"] = 'Depends on the type of agroforestry system and the previous land use. Agroforestry can *increase* biodiversity compared to monoculture agriculture, but may *decrease* it compared to natural forest.\nCan provide habitat for some species, but may not support specialized forest species.\n**Influenced By (Stressors):**\nAgroforestry - Economic Incentives: Market demand for agroforestry products (e.g., timber, fruits, nuts, coffee, cocoa).\nAgroforestry - Government Policies: Subsidies, regulations, land tenure.\nAgroforestry - Population Pressure: Demand for land and resources.\nAgroforestry - Climate Change: May influence the suitability of certain agroforestry systems.\n**Influences (Stressors):**\nHabitat availability (for some species).\n**Logic Description:** Conversion of land *to* or *from* agroforestry can have significant impacts on biodiversity and ecosystem services, depending on the context.  Agroforestry can be more sustainable than intensive agriculture, but less biodiverse than natural forest.'
anthropogenic_agroforestry_stressors["Land Use Change"]["Influenced By"] = ['Agroforestry - Economic Incentives: Market demand for agroforestry products (e.g., timber, fruits, nuts, coffee, cocoa).', 'Agroforestry - Government Policies: Subsidies, regulations, land tenure.', 'Agroforestry - Population Pressure: Demand for land and resources.', 'Agroforestry - Climate Change: May influence the suitability of certain agroforestry systems.', '**Influences (Stressors):**', 'Habitat availability (for some species).', '**Logic Description:** Conversion of land *to* or *from* agroforestry can have significant impacts on biodiversity and ecosystem services, depending on the context.  Agroforestry can be more sustainable than intensive agriculture, but less biodiverse than natural forest.']
anthropogenic_agroforestry_stressors["Land Use Change"]["Influences"] = ['Habitat availability (for some species).', '**Logic Description:** Conversion of land *to* or *from* agroforestry can have significant impacts on biodiversity and ecosystem services, depending on the context.  Agroforestry can be more sustainable than intensive agriculture, but less biodiverse than natural forest.']
anthropogenic_agroforestry_stressors["Land Use Change"]["Logic Description"] = '---'
anthropogenic_agroforestry_stressors["Land Use Change"]["Impact Function"] = "impact_land_use_change_anthropogenic_agroforestry"

# --- Management Practices ---
anthropogenic_agroforestry_stressors["Management Practices"]["Metric"] = 'Tree density; species composition; use of fertilizers and pesticides; pruning and thinning practices; soil management practices.'
anthropogenic_agroforestry_stressors["Management Practices"]["Data Sources"] = ['Field surveys.', 'Agricultural statistics.', 'Research publications.', '**Impact on Area:** Influences the structure and function of the agroforestry system.', '**Impact on Biodiversity:**', 'Species diversity of trees and understory plants.', 'Habitat quality for wildlife.', 'Soil health and nutrient cycling.', '**Influenced By (Stressors):**', 'Agroforestry - Farmer Knowledge and Skills', 'Agroforestry - Economic Factors: Costs and benefits of different practices.', 'Agroforestry - Access to Resources: (e.g., planting material, fertilizers).', 'Agroforestry - Government Policies and Extension Services.', '**Influences (Stressors):**', 'Agroforestry - Soil Degradation.', 'Agroforestry - Water Quality.', 'Agroforestry - Pest and Disease Outbreaks.', 'Agroforestry - Carbon Sequestration.', '**Logic Description:** The specific management practices used in an agroforestry system (e.g., tree species selection, planting density, pruning, fertilization) have a major influence on its biodiversity, productivity, and ecosystem services.']
anthropogenic_agroforestry_stressors["Management Practices"]["Impact on Area"] = 'Influences the structure and function of the agroforestry system.'
anthropogenic_agroforestry_stressors["Management Practices"]["Impact on Biodiversity"] = 'Species diversity of trees and understory plants.\nHabitat quality for wildlife.\nSoil health and nutrient cycling.\n**Influenced By (Stressors):**\nAgroforestry - Farmer Knowledge and Skills\nAgroforestry - Economic Factors: Costs and benefits of different practices.\nAgroforestry - Access to Resources: (e.g., planting material, fertilizers).\nAgroforestry - Government Policies and Extension Services.\n**Influences (Stressors):**\nAgroforestry - Soil Degradation.\nAgroforestry - Water Quality.\nAgroforestry - Pest and Disease Outbreaks.\nAgroforestry - Carbon Sequestration.\n**Logic Description:** The specific management practices used in an agroforestry system (e.g., tree species selection, planting density, pruning, fertilization) have a major influence on its biodiversity, productivity, and ecosystem services.'
anthropogenic_agroforestry_stressors["Management Practices"]["Influenced By"] = ['Agroforestry - Farmer Knowledge and Skills', 'Agroforestry - Economic Factors: Costs and benefits of different practices.', 'Agroforestry - Access to Resources: (e.g., planting material, fertilizers).', 'Agroforestry - Government Policies and Extension Services.', '**Influences (Stressors):**', 'Agroforestry - Soil Degradation.', 'Agroforestry - Water Quality.', 'Agroforestry - Pest and Disease Outbreaks.', 'Agroforestry - Carbon Sequestration.', '**Logic Description:** The specific management practices used in an agroforestry system (e.g., tree species selection, planting density, pruning, fertilization) have a major influence on its biodiversity, productivity, and ecosystem services.']
anthropogenic_agroforestry_stressors["Management Practices"]["Influences"] = ['Agroforestry - Soil Degradation.', 'Agroforestry - Water Quality.', 'Agroforestry - Pest and Disease Outbreaks.', 'Agroforestry - Carbon Sequestration.', '**Logic Description:** The specific management practices used in an agroforestry system (e.g., tree species selection, planting density, pruning, fertilization) have a major influence on its biodiversity, productivity, and ecosystem services.']
anthropogenic_agroforestry_stressors["Management Practices"]["Logic Description"] = '---'
anthropogenic_agroforestry_stressors["Management Practices"]["Impact Function"] = "impact_management_practices_anthropogenic_agroforestry"

# --- Climate Change ---
anthropogenic_agroforestry_stressors["Climate Change"]["Metric"] = 'Changes in temperature, precipitation, and extreme weather events.'
anthropogenic_agroforestry_stressors["Climate Change"]["Data Sources"] = ['* Climate models.', '* Historical weather data.', '**Impact on Area:** Changes in growing conditions.', '**Impact on Biodiversity:**', '* May affect the suitability of certain tree and crop species.', 'Increased stress on plants and animals.', 'Changes in pest and disease dynamics.', '**Influenced By (Stressors):**', '* Global Greenhouse Gas Emissions', '**Influences (Stressors):**', '* Agroforestry - Water Availability.', '* Agroforestry - Pest and Disease Outbreaks', '* Agroforestry - Tree and Crop Productivity', '**Logic Description:** Climate change can alter growing conditions, making some agroforestry systems less viable or requiring adaptation.']
anthropogenic_agroforestry_stressors["Climate Change"]["Impact on Area"] = 'Changes in growing conditions.'
anthropogenic_agroforestry_stressors["Climate Change"]["Impact on Biodiversity"] = '* May affect the suitability of certain tree and crop species.\nIncreased stress on plants and animals.\nChanges in pest and disease dynamics.\n**Influenced By (Stressors):**\n* Global Greenhouse Gas Emissions\n**Influences (Stressors):**\n* Agroforestry - Water Availability.\n* Agroforestry - Pest and Disease Outbreaks\n* Agroforestry - Tree and Crop Productivity\n**Logic Description:** Climate change can alter growing conditions, making some agroforestry systems less viable or requiring adaptation.'
anthropogenic_agroforestry_stressors["Climate Change"]["Influenced By"] = ['* Global Greenhouse Gas Emissions', '**Influences (Stressors):**', '* Agroforestry - Water Availability.', '* Agroforestry - Pest and Disease Outbreaks', '* Agroforestry - Tree and Crop Productivity', '**Logic Description:** Climate change can alter growing conditions, making some agroforestry systems less viable or requiring adaptation.']
anthropogenic_agroforestry_stressors["Climate Change"]["Influences"] = ['* Agroforestry - Water Availability.', '* Agroforestry - Pest and Disease Outbreaks', '* Agroforestry - Tree and Crop Productivity', '**Logic Description:** Climate change can alter growing conditions, making some agroforestry systems less viable or requiring adaptation.']
anthropogenic_agroforestry_stressors["Climate Change"]["Logic Description"] = '---'
anthropogenic_agroforestry_stressors["Climate Change"]["Impact Function"] = "impact_climate_change_anthropogenic_agroforestry"

# --- Pest and Disease Outbreaks ---
anthropogenic_agroforestry_stressors["Pest and Disease Outbreaks"]["Metric"] = 'Incidence and severity of pest and disease outbreaks.'
anthropogenic_agroforestry_stressors["Pest and Disease Outbreaks"]["Data Sources"] = ['Field surveys.', 'Agricultural statistics.', 'Research publications.', '**Impact on Area:** Reduced tree and crop productivity; economic losses.', '**Impact on Biodiversity:**', '* Can impact both crop and non-crop species.', '**Influenced By (Stressors):**', 'Agroforestry - Management Practices (e.g., species diversity, use of pesticides).', 'Agroforestry - Climate Change (can alter pest and disease dynamics).', 'Agroforestry - Introduction of Exotic Species', '**Influences (Stressors):**', '*  Agroforestry - Tree and Crop Productivity', '**Logic Description:** Pest and disease outbreaks can damage or kill trees and crops in agroforestry systems.']
anthropogenic_agroforestry_stressors["Pest and Disease Outbreaks"]["Impact on Area"] = 'Reduced tree and crop productivity; economic losses.'
anthropogenic_agroforestry_stressors["Pest and Disease Outbreaks"]["Impact on Biodiversity"] = '* Can impact both crop and non-crop species.\n**Influenced By (Stressors):**\nAgroforestry - Management Practices (e.g., species diversity, use of pesticides).\nAgroforestry - Climate Change (can alter pest and disease dynamics).\nAgroforestry - Introduction of Exotic Species\n**Influences (Stressors):**\n*  Agroforestry - Tree and Crop Productivity\n**Logic Description:** Pest and disease outbreaks can damage or kill trees and crops in agroforestry systems.'
anthropogenic_agroforestry_stressors["Pest and Disease Outbreaks"]["Influenced By"] = ['Agroforestry - Management Practices (e.g., species diversity, use of pesticides).', 'Agroforestry - Climate Change (can alter pest and disease dynamics).', 'Agroforestry - Introduction of Exotic Species', '**Influences (Stressors):**', '*  Agroforestry - Tree and Crop Productivity', '**Logic Description:** Pest and disease outbreaks can damage or kill trees and crops in agroforestry systems.']
anthropogenic_agroforestry_stressors["Pest and Disease Outbreaks"]["Influences"] = ['*  Agroforestry - Tree and Crop Productivity', '**Logic Description:** Pest and disease outbreaks can damage or kill trees and crops in agroforestry systems.']
anthropogenic_agroforestry_stressors["Pest and Disease Outbreaks"]["Logic Description"] = '---'
anthropogenic_agroforestry_stressors["Pest and Disease Outbreaks"]["Impact Function"] = "impact_pest_and_disease_outbreaks_anthropogenic_agroforestry"

# --- Soil Degradation ---
anthropogenic_agroforestry_stressors["Soil Degradation"]["Metric"] = 'Soil organic matter content; soil erosion rate; nutrient depletion; soil compaction.'
anthropogenic_agroforestry_stressors["Soil Degradation"]["Data Sources"] = ['Soil surveys.', 'Research publications.', '**Impact on Area:** Reduced soil fertility and productivity.', '**Impact on Biodiversity:**', '* Impacts on soil organisms.', '**Influenced By (Stressors):**', '*  Agroforestry - Management Practices (e.g., tillage, fertilization, cover cropping).', 'Agroforestry - Overgrazing (in silvopastoral systems).', '*  Agroforestry - Erosion', '**Influences (Stressors):**', 'Agroforestry - Tree and Crop Productivity', '*  Agroforestry - Water Quality', '**Logic Description:** Soil degradation can reduce the productivity and sustainability of agroforestry systems.']
anthropogenic_agroforestry_stressors["Soil Degradation"]["Impact on Area"] = 'Reduced soil fertility and productivity.'
anthropogenic_agroforestry_stressors["Soil Degradation"]["Impact on Biodiversity"] = '* Impacts on soil organisms.\n**Influenced By (Stressors):**\n*  Agroforestry - Management Practices (e.g., tillage, fertilization, cover cropping).\nAgroforestry - Overgrazing (in silvopastoral systems).\n*  Agroforestry - Erosion\n**Influences (Stressors):**\nAgroforestry - Tree and Crop Productivity\n*  Agroforestry - Water Quality\n**Logic Description:** Soil degradation can reduce the productivity and sustainability of agroforestry systems.'
anthropogenic_agroforestry_stressors["Soil Degradation"]["Influenced By"] = ['*  Agroforestry - Management Practices (e.g., tillage, fertilization, cover cropping).', 'Agroforestry - Overgrazing (in silvopastoral systems).', '*  Agroforestry - Erosion', '**Influences (Stressors):**', 'Agroforestry - Tree and Crop Productivity', '*  Agroforestry - Water Quality', '**Logic Description:** Soil degradation can reduce the productivity and sustainability of agroforestry systems.']
anthropogenic_agroforestry_stressors["Soil Degradation"]["Influences"] = ['Agroforestry - Tree and Crop Productivity', '*  Agroforestry - Water Quality', '**Logic Description:** Soil degradation can reduce the productivity and sustainability of agroforestry systems.']
anthropogenic_agroforestry_stressors["Soil Degradation"]["Logic Description"] = '---'
anthropogenic_agroforestry_stressors["Soil Degradation"]["Impact Function"] = "impact_soil_degradation_anthropogenic_agroforestry"

# --- Water Availability ---
anthropogenic_agroforestry_stressors["Water Availability"]["Metric"] = 'Rainfall amount and distribution, soil moisture content, access to irrigation.'
anthropogenic_agroforestry_stressors["Water Availability"]["Data Sources"] = ['* Weather data', '* Hydrological models.', '**Impact on Area:** Affects tree and crop growth.', '**Impact on Biodiversity:**', '* Water stress can impact both plants and animals.', '**Influenced By (Stressors):**', '* Agroforestry - Climate Change', '* Agroforestry - Water Use', '**Influences (Stressors):**', '*  Agroforestry - Tree and Crop Productivity', '* Many', '**Logic Description:** Water availability is essential for plant growth and overall system productivity.']
anthropogenic_agroforestry_stressors["Water Availability"]["Impact on Area"] = 'Affects tree and crop growth.'
anthropogenic_agroforestry_stressors["Water Availability"]["Impact on Biodiversity"] = '* Water stress can impact both plants and animals.\n**Influenced By (Stressors):**\n* Agroforestry - Climate Change\n* Agroforestry - Water Use\n**Influences (Stressors):**\n*  Agroforestry - Tree and Crop Productivity\n* Many\n**Logic Description:** Water availability is essential for plant growth and overall system productivity.'
anthropogenic_agroforestry_stressors["Water Availability"]["Influenced By"] = ['* Agroforestry - Climate Change', '* Agroforestry - Water Use', '**Influences (Stressors):**', '*  Agroforestry - Tree and Crop Productivity', '* Many', '**Logic Description:** Water availability is essential for plant growth and overall system productivity.']
anthropogenic_agroforestry_stressors["Water Availability"]["Influences"] = ['*  Agroforestry - Tree and Crop Productivity', '* Many', '**Logic Description:** Water availability is essential for plant growth and overall system productivity.']
anthropogenic_agroforestry_stressors["Water Availability"]["Logic Description"] = '---'
anthropogenic_agroforestry_stressors["Water Availability"]["Impact Function"] = "impact_water_availability_anthropogenic_agroforestry"

# --- Market Access ---
anthropogenic_agroforestry_stressors["Market Access"]["Metric"] = 'Access to markets for agroforestry products.'
anthropogenic_agroforestry_stressors["Market Access"]["Data Sources"] = ['* Economic data', '* Surveys.', '**Impact on Area:** Influences the economic viability', '**Impact on Biodiversity:**', '* Indirect - may influence farmer decisions about crop/tree selection.', '**Influenced By (Stressors):**', '* Economic factors, infrastructure.', '**Influences (Stressors):**', '* Agroforestry - Economic Incentives', '**Logic Description**: Market access is crucial for the economic success.']
anthropogenic_agroforestry_stressors["Market Access"]["Impact on Area"] = 'Influences the economic viability'
anthropogenic_agroforestry_stressors["Market Access"]["Impact on Biodiversity"] = '* Indirect - may influence farmer decisions about crop/tree selection.\n**Influenced By (Stressors):**\n* Economic factors, infrastructure.\n**Influences (Stressors):**\n* Agroforestry - Economic Incentives\n**Logic Description**: Market access is crucial for the economic success.'
anthropogenic_agroforestry_stressors["Market Access"]["Influenced By"] = ['* Economic factors, infrastructure.', '**Influences (Stressors):**', '* Agroforestry - Economic Incentives', '**Logic Description**: Market access is crucial for the economic success.']
anthropogenic_agroforestry_stressors["Market Access"]["Influences"] = ['* Agroforestry - Economic Incentives', '**Logic Description**: Market access is crucial for the economic success.']
anthropogenic_agroforestry_stressors["Market Access"]["Impact Function"] = "impact_market_access_anthropogenic_agroforestry"

# --- Farmer Knowledge and Skills ---
anthropogenic_agroforestry_stressors["Farmer Knowledge and Skills"]["Metric"] = 'Level of farmer knowledge about agroforestry practices.'
anthropogenic_agroforestry_stressors["Farmer Knowledge and Skills"]["Data Sources"] = ['* Surveys', '* Research.', '**Impact on Area:** Influences management decisions.', '**Impact on Biodiversity:**', '* Can influence the success of the system in supporting biodiversity', '**Influenced By (Stressors)**', '* Education, extension services.', '**Influences (Stressors)**:', '* Agroforestry - Management Practices.', '**Logic Description**: Farmer knowledge is crucial for effective agroforestry.']
anthropogenic_agroforestry_stressors["Farmer Knowledge and Skills"]["Impact on Area"] = 'Influences management decisions.'
anthropogenic_agroforestry_stressors["Farmer Knowledge and Skills"]["Impact on Biodiversity"] = '* Can influence the success of the system in supporting biodiversity\n**Influenced By (Stressors)**\n* Education, extension services.\n**Influences (Stressors)**:\n* Agroforestry - Management Practices.\n**Logic Description**: Farmer knowledge is crucial for effective agroforestry.'
anthropogenic_agroforestry_stressors["Farmer Knowledge and Skills"]["Impact Function"] = "impact_farmer_knowledge_and_skills_anthropogenic_agroforestry"

# --- Economic Incentives ---
anthropogenic_agroforestry_stressors["Economic Incentives"]["Metric"] = 'Prices for agroforestry products, subsidies, etc.'
anthropogenic_agroforestry_stressors["Economic Incentives"]["Data Sources"] = ['* Economic data', '**Impact on Area**: Influences farmer decisions', '**Impact on Biodiversity:**', '* Indirect - influences management practices.', '**Influenced By (Stressors):**', '* Market Access', '**Influences (Stressors):**', '* Agroforestry - Management Practices.', '* Agroforestry - Land Use Change', '**Logic Description:** Economic incentives influence farmer decisions.']
anthropogenic_agroforestry_stressors["Economic Incentives"]["Impact on Biodiversity"] = '* Indirect - influences management practices.\n**Influenced By (Stressors):**\n* Market Access\n**Influences (Stressors):**\n* Agroforestry - Management Practices.\n* Agroforestry - Land Use Change\n**Logic Description:** Economic incentives influence farmer decisions.'
anthropogenic_agroforestry_stressors["Economic Incentives"]["Influenced By"] = ['* Market Access', '**Influences (Stressors):**', '* Agroforestry - Management Practices.', '* Agroforestry - Land Use Change', '**Logic Description:** Economic incentives influence farmer decisions.']
anthropogenic_agroforestry_stressors["Economic Incentives"]["Influences"] = ['* Agroforestry - Management Practices.', '* Agroforestry - Land Use Change', '**Logic Description:** Economic incentives influence farmer decisions.']
anthropogenic_agroforestry_stressors["Economic Incentives"]["Logic Description"] = '---'
anthropogenic_agroforestry_stressors["Economic Incentives"]["Impact Function"] = "impact_economic_incentives_anthropogenic_agroforestry"

# --- Government Policies ---
anthropogenic_agroforestry_stressors["Government Policies"]["Data Sources"] = ['* Policy documents', '**Impact on Area**: Variable', '**Impact on Biodiversity**:', '* Variable', '**Influenced By (Stressors)**', '* Politics, economics', '**Influences (Stressors):**', '* Agroforestry - Land Use Change', '*  Agroforestry - Management Practices', '**Logic Description:** Policies can promote or hinder agroforestry.']
anthropogenic_agroforestry_stressors["Government Policies"]["Influences"] = ['* Agroforestry - Land Use Change', '*  Agroforestry - Management Practices', '**Logic Description:** Policies can promote or hinder agroforestry.']
anthropogenic_agroforestry_stressors["Government Policies"]["Logic Description"] = '---'
anthropogenic_agroforestry_stressors["Government Policies"]["Impact Function"] = "impact_government_policies_anthropogenic_agroforestry"

# --- Population Pressure ---
anthropogenic_agroforestry_stressors["Population Pressure"]["Data Sources"] = ['* Census data', '**Impact on Area:** Can lead to land conversion and intensification.', '**Impact on Biodiversity:**', '* Variable, depends on how land use changes.', '**Influenced By (Stressors)**', '* Socioeconomic factors.', '**Influences (Stressors)**', '* Agroforestry - Land Use Change', '**Logic Description:** Population pressure influences land use.']
anthropogenic_agroforestry_stressors["Population Pressure"]["Impact on Area"] = 'Can lead to land conversion and intensification.'
anthropogenic_agroforestry_stressors["Population Pressure"]["Impact on Biodiversity"] = '* Variable, depends on how land use changes.\n**Influenced By (Stressors)**\n* Socioeconomic factors.\n**Influences (Stressors)**\n* Agroforestry - Land Use Change\n**Logic Description:** Population pressure influences land use.'
anthropogenic_agroforestry_stressors["Population Pressure"]["Logic Description"] = '---'
anthropogenic_agroforestry_stressors["Population Pressure"]["Impact Function"] = "impact_population_pressure_anthropogenic_agroforestry"

# --- Access to Resources ---
anthropogenic_agroforestry_stressors["Access to Resources"]["Data Sources"] = ['* Surveys', '* Research studies.', '**Impact on Area:** Influences the ability of farmers to implement agroforestry.', '**Impact on Biodiversity:**', '* Indirect, through impacts on management practices.', '**Influenced By (Stressors)**', '* Economic factors', '* Government policies.', '**Influences (Stressors):**', '*  Agroforestry - Management Practices', '**Logic Description:** Resources are needed to implement agroforestry.']
anthropogenic_agroforestry_stressors["Access to Resources"]["Impact on Area"] = 'Influences the ability of farmers to implement agroforestry.'
anthropogenic_agroforestry_stressors["Access to Resources"]["Impact on Biodiversity"] = '* Indirect, through impacts on management practices.\n**Influenced By (Stressors)**\n* Economic factors\n* Government policies.\n**Influences (Stressors):**\n*  Agroforestry - Management Practices\n**Logic Description:** Resources are needed to implement agroforestry.'
anthropogenic_agroforestry_stressors["Access to Resources"]["Influences"] = ['*  Agroforestry - Management Practices', '**Logic Description:** Resources are needed to implement agroforestry.']
anthropogenic_agroforestry_stressors["Access to Resources"]["Logic Description"] = '---'
anthropogenic_agroforestry_stressors["Access to Resources"]["Impact Function"] = "impact_access_to_resources_anthropogenic_agroforestry"

# --- Carbon Sequestration ---
anthropogenic_agroforestry_stressors["Carbon Sequestration"]["Metric"] = 'Amount of carbon stored in trees and soil.'
anthropogenic_agroforestry_stressors["Carbon Sequestration"]["Data Sources"] = ['* Field measurements', '* Models.', '**Impact on Area:** Positive - contributes to climate change mitigation.', '**Impact on Biodiversity**:', '* Indirect - helps mitigate climate change, which benefits biodiversity in the long run.', '**Influenced By (Stressors)**', '* Agroforestry - Management Practices', '**Influences (Stressors)**:', '* Global climate change (mitigation).', '**Logic Description:** Agroforestry can sequester carbon, helping to mitigate climate change.']
anthropogenic_agroforestry_stressors["Carbon Sequestration"]["Impact on Area"] = 'Positive - contributes to climate change mitigation.'
anthropogenic_agroforestry_stressors["Carbon Sequestration"]["Logic Description"] = '---'
anthropogenic_agroforestry_stressors["Carbon Sequestration"]["Impact Function"] = "impact_carbon_sequestration_anthropogenic_agroforestry"

# --- Tree and Crop Productivity ---
anthropogenic_agroforestry_stressors["Tree and Crop Productivity"]["Impact on Biodiversity"] = '* Indirect.\n**Influenced By (Stressors):**\n* Many, Varies.\n**Influences (Stressors):**\n* Livelihoods.\n**Logic Description:** Productivity is key for economic viability'
anthropogenic_agroforestry_stressors["Tree and Crop Productivity"]["Influenced By"] = ['* Many, Varies.', '**Influences (Stressors):**', '* Livelihoods.', '**Logic Description:** Productivity is key for economic viability']
anthropogenic_agroforestry_stressors["Tree and Crop Productivity"]["Influences"] = ['* Livelihoods.', '**Logic Description:** Productivity is key for economic viability']
anthropogenic_agroforestry_stressors["Tree and Crop Productivity"]["Logic Description"] = '---'
anthropogenic_agroforestry_stressors["Tree and Crop Productivity"]["Impact Function"] = "impact_tree_and_crop_productivity_anthropogenic_agroforestry"

# --- Introduction of Exotic Species ---
anthropogenic_agroforestry_stressors["Introduction of Exotic Species"]["Data Sources"] = ['* Field surveys', '**Impact on Area**: Can be positive (if well-managed) or negative (if invasive).', '**Impact on Biodiversity:**', '* Potential for negative impacts if species become invasive.', '**Influenced By (Stressors):**', '*  Agroforestry - Management Practices', '**Influences (Stressors)**:', '* Agroforestry - Pest and Disease Outbreaks', '**Logic Description**: Exotic species can be beneficial or detrimental.']
anthropogenic_agroforestry_stressors["Introduction of Exotic Species"]["Impact on Biodiversity"] = '* Potential for negative impacts if species become invasive.\n**Influenced By (Stressors):**\n*  Agroforestry - Management Practices\n**Influences (Stressors)**:\n* Agroforestry - Pest and Disease Outbreaks\n**Logic Description**: Exotic species can be beneficial or detrimental.'
anthropogenic_agroforestry_stressors["Introduction of Exotic Species"]["Influenced By"] = ['*  Agroforestry - Management Practices', '**Influences (Stressors)**:', '* Agroforestry - Pest and Disease Outbreaks', '**Logic Description**: Exotic species can be beneficial or detrimental.']
anthropogenic_agroforestry_stressors["Introduction of Exotic Species"]["Impact Function"] = "impact_introduction_of_exotic_species_anthropogenic_agroforestry"

# --- Erosion ---
anthropogenic_agroforestry_stressors["Erosion"]["Influenced By"] = ['* Agroforestry - Soil Degradation', '**Influences (Stressors)**', '* Agroforestry - Soil Degradation', '**Logic Description:** Loss of soil.']
anthropogenic_agroforestry_stressors["Erosion"]["Logic Description"] = '---'
anthropogenic_agroforestry_stressors["Erosion"]["Impact Function"] = "impact_erosion_anthropogenic_agroforestry"

# --- Water Use ---
anthropogenic_agroforestry_stressors["Water Use"]["Data Sources"] = ['* Field measurements', '* Models', '**Impact on Area**: Water balance', '**Impact on Biodiversity:**', '* Can impact downstream water availability.', '**Influenced By (Stressors):**', '*  Agroforestry - Climate Change', '* Species Choices', '**Influences (Stressors):**', '* Agroforestry - Water Availability', '**Logic Description**: Water Use']
anthropogenic_agroforestry_stressors["Water Use"]["Impact on Biodiversity"] = '* Can impact downstream water availability.\n**Influenced By (Stressors):**\n*  Agroforestry - Climate Change\n* Species Choices\n**Influences (Stressors):**\n* Agroforestry - Water Availability\n**Logic Description**: Water Use'
anthropogenic_agroforestry_stressors["Water Use"]["Influenced By"] = ['*  Agroforestry - Climate Change', '* Species Choices', '**Influences (Stressors):**', '* Agroforestry - Water Availability', '**Logic Description**: Water Use']
anthropogenic_agroforestry_stressors["Water Use"]["Influences"] = ['* Agroforestry - Water Availability', '**Logic Description**: Water Use']
anthropogenic_agroforestry_stressors["Water Use"]["Impact Function"] = "impact_water_use_anthropogenic_agroforestry"

