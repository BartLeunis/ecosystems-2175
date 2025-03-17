from stressor_templates import *
import copy

anthropogenic_pastoral_lands_stressors = {
    "Overgrazing": {},
    "Climate Change": copy.deepcopy(climate_change_template),
    "Land Use Change": {},
    "Soil Degradation": {},
    "Water Availability": {},
    "Invasive Species": copy.deepcopy(invasive_species_template),
    "Socioeconomic Factors": {},
    "Stocking Rates": {},
    "Grazing Management Practices": {},
    "Climate Variability": {},
    "Land Tenure and Access Rights": {},
    "Desertification": {},
    "Water Quality": {},
    "Wildfires": copy.deepcopy(fire_regime_template),
    "Forage Production": {},
    "Vegetation Changes": {},
}

# --- Overgrazing ---
anthropogenic_pastoral_lands_stressors["Overgrazing"]["Metric"] = 'Livestock density (animals per unit area); vegetation cover and composition; soil erosion rates.'
anthropogenic_pastoral_lands_stressors["Overgrazing"]["Data Sources"] = ['Livestock censuses.', 'Vegetation surveys (remote sensing and field-based).', 'Soil erosion assessments.', 'Research publications.', '**Impact on Area:** Reduced vegetation cover; soil degradation; desertification (in extreme cases).', '**Impact on Biodiversity:**', 'Loss of palatable plant species.', 'Increase in unpalatable or invasive species.', 'Soil compaction, reducing water infiltration and harming soil organisms.', 'Habitat loss and fragmentation for wildlife.', 'Increased competition between livestock and native herbivores.', '**Influenced By (Stressors):**', 'Pastoral Lands - Stocking Rates: The number of animals grazing an area.', 'Pastoral Lands - Grazing Management Practices: (e.g., rotational grazing, continuous grazing).', 'Pastoral Lands - Climate Variability: Drought can exacerbate overgrazing.', 'Pastoral Lands - Land Tenure and Access Rights:  Influence control over grazing.', 'Pastoral Lands - Socioeconomic Factors: Poverty, market pressures, and population growth can contribute to overgrazing.', '**Influences (Stressors):**', 'Pastoral Lands - Soil Degradation', 'Pastoral Lands - Desertification', 'Pastoral Lands - Water Quality (through erosion and runoff).', 'Pastoral Lands - Vegetation Changes', '**Logic Description:** Overgrazing occurs when livestock density exceeds the carrying capacity of the land, leading to vegetation loss, soil degradation, and negative impacts on biodiversity.']
anthropogenic_pastoral_lands_stressors["Overgrazing"]["Impact on Area"] = 'Reduced vegetation cover; soil degradation; desertification (in extreme cases).'
anthropogenic_pastoral_lands_stressors["Overgrazing"]["Impact on Biodiversity"] = 'Loss of palatable plant species.\nIncrease in unpalatable or invasive species.\nSoil compaction, reducing water infiltration and harming soil organisms.\nHabitat loss and fragmentation for wildlife.\nIncreased competition between livestock and native herbivores.\n**Influenced By (Stressors):**\nPastoral Lands - Stocking Rates: The number of animals grazing an area.\nPastoral Lands - Grazing Management Practices: (e.g., rotational grazing, continuous grazing).\nPastoral Lands - Climate Variability: Drought can exacerbate overgrazing.\nPastoral Lands - Land Tenure and Access Rights:  Influence control over grazing.\nPastoral Lands - Socioeconomic Factors: Poverty, market pressures, and population growth can contribute to overgrazing.\n**Influences (Stressors):**\nPastoral Lands - Soil Degradation\nPastoral Lands - Desertification\nPastoral Lands - Water Quality (through erosion and runoff).\nPastoral Lands - Vegetation Changes\n**Logic Description:** Overgrazing occurs when livestock density exceeds the carrying capacity of the land, leading to vegetation loss, soil degradation, and negative impacts on biodiversity.'
anthropogenic_pastoral_lands_stressors["Overgrazing"]["Influenced By"] = ['Pastoral Lands - Stocking Rates: The number of animals grazing an area.', 'Pastoral Lands - Grazing Management Practices: (e.g., rotational grazing, continuous grazing).', 'Pastoral Lands - Climate Variability: Drought can exacerbate overgrazing.', 'Pastoral Lands - Land Tenure and Access Rights:  Influence control over grazing.', 'Pastoral Lands - Socioeconomic Factors: Poverty, market pressures, and population growth can contribute to overgrazing.', '**Influences (Stressors):**', 'Pastoral Lands - Soil Degradation', 'Pastoral Lands - Desertification', 'Pastoral Lands - Water Quality (through erosion and runoff).', 'Pastoral Lands - Vegetation Changes', '**Logic Description:** Overgrazing occurs when livestock density exceeds the carrying capacity of the land, leading to vegetation loss, soil degradation, and negative impacts on biodiversity.']
anthropogenic_pastoral_lands_stressors["Overgrazing"]["Influences"] = ['Pastoral Lands - Soil Degradation', 'Pastoral Lands - Desertification', 'Pastoral Lands - Water Quality (through erosion and runoff).', 'Pastoral Lands - Vegetation Changes', '**Logic Description:** Overgrazing occurs when livestock density exceeds the carrying capacity of the land, leading to vegetation loss, soil degradation, and negative impacts on biodiversity.']
anthropogenic_pastoral_lands_stressors["Overgrazing"]["Logic Description"] = '---'
anthropogenic_pastoral_lands_stressors["Overgrazing"]["Impact Function"] = "impact_overgrazing_anthropogenic_pastoral_lands"

# --- Climate Change ---
anthropogenic_pastoral_lands_stressors["Climate Change"]["Metric"] = 'Changes in temperature, precipitation, and the frequency/intensity of extreme weather events (e.g., droughts, floods).'
anthropogenic_pastoral_lands_stressors["Climate Change"]["Data Sources"] = ['Climate models.', 'Historical weather records.', 'Remote sensing data.', '**Impact on Area:** Changes in forage availability and quality; increased water stress; increased risk of desertification.', '**Impact on Biodiversity:**', 'Shifts in plant species distributions.', 'Increased stress on livestock and wildlife.', 'Increased risk of wildfires.', 'Changes in disease dynamics.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions', '**Influences (Stressors):**', 'Pastoral Lands - Water Availability', 'Pastoral Lands - Forage Production', 'Pastoral Lands - Desertification', 'Pastoral Lands - Wildfires', '**Logic Description:** Climate change is altering temperature and precipitation patterns, impacting forage production, water availability, and the overall sustainability of pastoral systems.']
anthropogenic_pastoral_lands_stressors["Climate Change"]["Impact on Area"] = 'Changes in forage availability and quality; increased water stress; increased risk of desertification.'
anthropogenic_pastoral_lands_stressors["Climate Change"]["Impact on Biodiversity"] = 'Shifts in plant species distributions.\nIncreased stress on livestock and wildlife.\nIncreased risk of wildfires.\nChanges in disease dynamics.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions\n**Influences (Stressors):**\nPastoral Lands - Water Availability\nPastoral Lands - Forage Production\nPastoral Lands - Desertification\nPastoral Lands - Wildfires\n**Logic Description:** Climate change is altering temperature and precipitation patterns, impacting forage production, water availability, and the overall sustainability of pastoral systems.'
anthropogenic_pastoral_lands_stressors["Climate Change"]["Influenced By"] = ['Global Greenhouse Gas Emissions', '**Influences (Stressors):**', 'Pastoral Lands - Water Availability', 'Pastoral Lands - Forage Production', 'Pastoral Lands - Desertification', 'Pastoral Lands - Wildfires', '**Logic Description:** Climate change is altering temperature and precipitation patterns, impacting forage production, water availability, and the overall sustainability of pastoral systems.']
anthropogenic_pastoral_lands_stressors["Climate Change"]["Influences"] = ['Pastoral Lands - Water Availability', 'Pastoral Lands - Forage Production', 'Pastoral Lands - Desertification', 'Pastoral Lands - Wildfires', '**Logic Description:** Climate change is altering temperature and precipitation patterns, impacting forage production, water availability, and the overall sustainability of pastoral systems.']
anthropogenic_pastoral_lands_stressors["Climate Change"]["Logic Description"] = '---'
anthropogenic_pastoral_lands_stressors["Climate Change"]["Impact Function"] = "impact_climate_change_anthropogenic_pastoral_lands"

# --- Land Use Change ---
anthropogenic_pastoral_lands_stressors["Land Use Change"]["Metric"] = 'Conversion of pastoral lands to other land uses (e.g., agriculture, urbanization, mining).'
anthropogenic_pastoral_lands_stressors["Land Use Change"]["Data Sources"] = ['* Remote sensing', '* Land use records.', '**Impact on Area:** Loss of grazing land.', '**Impact on Biodiversity:**', '* Habitat loss and fragmentation', '**Influenced By (Stressors):**', '* Population growth', '* Economic development', '* Agricultural expansion.', '**Influences (Stressors):**', 'Habitat availability', '**Logic Description:** Conversion of pastoral lands reduces the area available for grazing.']
anthropogenic_pastoral_lands_stressors["Land Use Change"]["Impact on Area"] = 'Loss of grazing land.'
anthropogenic_pastoral_lands_stressors["Land Use Change"]["Impact on Biodiversity"] = '* Habitat loss and fragmentation\n**Influenced By (Stressors):**\n* Population growth\n* Economic development\n* Agricultural expansion.\n**Influences (Stressors):**\nHabitat availability\n**Logic Description:** Conversion of pastoral lands reduces the area available for grazing.'
anthropogenic_pastoral_lands_stressors["Land Use Change"]["Influenced By"] = ['* Population growth', '* Economic development', '* Agricultural expansion.', '**Influences (Stressors):**', 'Habitat availability', '**Logic Description:** Conversion of pastoral lands reduces the area available for grazing.']
anthropogenic_pastoral_lands_stressors["Land Use Change"]["Influences"] = ['Habitat availability', '**Logic Description:** Conversion of pastoral lands reduces the area available for grazing.']
anthropogenic_pastoral_lands_stressors["Land Use Change"]["Logic Description"] = '---'
anthropogenic_pastoral_lands_stressors["Land Use Change"]["Impact Function"] = "impact_land_use_change_anthropogenic_pastoral_lands"

# --- Soil Degradation ---
anthropogenic_pastoral_lands_stressors["Soil Degradation"]["Metric"] = 'Soil organic matter content; soil erosion rate; nutrient depletion; soil compaction.'
anthropogenic_pastoral_lands_stressors["Soil Degradation"]["Data Sources"] = ['* Soil surveys', '* Research', '**Impact on Area:** Reduced soil fertility and productivity.', '**Impact on Biodiversity:**', '* Loss of soil biodiversity.', 'Reduced habitat quality.', '**Influenced By (Stressors):**', '* Pastoral Lands - Overgrazing', '* Pastoral Lands - Erosion', '**Influences (Stressors):**', '* Pastoral Lands - Forage Production', '**Logic Description:** Soil degradation reduces the ability of the land to support vegetation.']
anthropogenic_pastoral_lands_stressors["Soil Degradation"]["Impact on Area"] = 'Reduced soil fertility and productivity.'
anthropogenic_pastoral_lands_stressors["Soil Degradation"]["Impact on Biodiversity"] = '* Loss of soil biodiversity.\nReduced habitat quality.\n**Influenced By (Stressors):**\n* Pastoral Lands - Overgrazing\n* Pastoral Lands - Erosion\n**Influences (Stressors):**\n* Pastoral Lands - Forage Production\n**Logic Description:** Soil degradation reduces the ability of the land to support vegetation.'
anthropogenic_pastoral_lands_stressors["Soil Degradation"]["Influenced By"] = ['* Pastoral Lands - Overgrazing', '* Pastoral Lands - Erosion', '**Influences (Stressors):**', '* Pastoral Lands - Forage Production', '**Logic Description:** Soil degradation reduces the ability of the land to support vegetation.']
anthropogenic_pastoral_lands_stressors["Soil Degradation"]["Influences"] = ['* Pastoral Lands - Forage Production', '**Logic Description:** Soil degradation reduces the ability of the land to support vegetation.']
anthropogenic_pastoral_lands_stressors["Soil Degradation"]["Logic Description"] = '---'
anthropogenic_pastoral_lands_stressors["Soil Degradation"]["Impact Function"] = "impact_soil_degradation_anthropogenic_pastoral_lands"

# --- Water Availability ---
anthropogenic_pastoral_lands_stressors["Water Availability"]["Metric"] = 'Rainfall, access to water sources (wells, rivers, etc.)'
anthropogenic_pastoral_lands_stressors["Water Availability"]["Data Sources"] = ['* Weather data', '* Hydrological data', '**Impact on Area:** Affects forage production and livestock survival.', '**Impact on Biodiversity:**', '* Impacts on both plants and animals.', '**Influenced By (Stressors):**', '* Pastoral Lands - Climate Change', '* Water withdrawals (for other uses).', '**Influences (Stressors):**', '*  Pastoral Lands - Forage Production', '* Livestock and wildlife survival.', '**Logic Description**: Water is essential for pastoral systems']
anthropogenic_pastoral_lands_stressors["Water Availability"]["Impact on Area"] = 'Affects forage production and livestock survival.'
anthropogenic_pastoral_lands_stressors["Water Availability"]["Impact on Biodiversity"] = '* Impacts on both plants and animals.\n**Influenced By (Stressors):**\n* Pastoral Lands - Climate Change\n* Water withdrawals (for other uses).\n**Influences (Stressors):**\n*  Pastoral Lands - Forage Production\n* Livestock and wildlife survival.\n**Logic Description**: Water is essential for pastoral systems'
anthropogenic_pastoral_lands_stressors["Water Availability"]["Influenced By"] = ['* Pastoral Lands - Climate Change', '* Water withdrawals (for other uses).', '**Influences (Stressors):**', '*  Pastoral Lands - Forage Production', '* Livestock and wildlife survival.', '**Logic Description**: Water is essential for pastoral systems']
anthropogenic_pastoral_lands_stressors["Water Availability"]["Influences"] = ['*  Pastoral Lands - Forage Production', '* Livestock and wildlife survival.', '**Logic Description**: Water is essential for pastoral systems']
anthropogenic_pastoral_lands_stressors["Water Availability"]["Impact Function"] = "impact_water_availability_anthropogenic_pastoral_lands"

# --- Invasive Species ---
anthropogenic_pastoral_lands_stressors["Invasive Species"]["Metric"] = 'Abundance and distribution of invasive plant species.'
anthropogenic_pastoral_lands_stressors["Invasive Species"]["Data Sources"] = ['* Field Surveys', '* Remote Sensing', '**Impact on Area**: Can reduce forage quality and availability.', '**Impact on Biodiversity:**', '* Competition with native plants', '**Influenced By (Stressors):**', '*  Pastoral Lands - Overgrazing (can create opportunities for invasives)', '* Climate Change', '**Influences (Stressors):**', '*  Pastoral Lands - Forage Production', '* Native plant communities', '**Logic Description**: Invasive plants can outcompete native forage species.']
anthropogenic_pastoral_lands_stressors["Invasive Species"]["Impact on Biodiversity"] = '* Competition with native plants\n**Influenced By (Stressors):**\n*  Pastoral Lands - Overgrazing (can create opportunities for invasives)\n* Climate Change\n**Influences (Stressors):**\n*  Pastoral Lands - Forage Production\n* Native plant communities\n**Logic Description**: Invasive plants can outcompete native forage species.'
anthropogenic_pastoral_lands_stressors["Invasive Species"]["Influenced By"] = ['*  Pastoral Lands - Overgrazing (can create opportunities for invasives)', '* Climate Change', '**Influences (Stressors):**', '*  Pastoral Lands - Forage Production', '* Native plant communities', '**Logic Description**: Invasive plants can outcompete native forage species.']
anthropogenic_pastoral_lands_stressors["Invasive Species"]["Influences"] = ['*  Pastoral Lands - Forage Production', '* Native plant communities', '**Logic Description**: Invasive plants can outcompete native forage species.']
anthropogenic_pastoral_lands_stressors["Invasive Species"]["Impact Function"] = "impact_invasive_species_anthropogenic_pastoral_lands"

# --- Socioeconomic Factors ---
anthropogenic_pastoral_lands_stressors["Socioeconomic Factors"]["Metric"] = 'Poverty, market access, land tenure, conflict.'
anthropogenic_pastoral_lands_stressors["Socioeconomic Factors"]["Data Sources"] = ['* Socioeconomic data', '* Surveys.', '**Impact on Area:** Influence management practices and sustainability', '**Impact on Biodiversity:**', '* Indirect', '**Influenced By (Stressors):**', '* Many factors', '**Influences (Stressors)**', '*  Pastoral Lands - Overgrazing', '**Logic Description**: Socioeconomic factors influence land use decisions.']
anthropogenic_pastoral_lands_stressors["Socioeconomic Factors"]["Impact on Area"] = 'Influence management practices and sustainability'
anthropogenic_pastoral_lands_stressors["Socioeconomic Factors"]["Impact on Biodiversity"] = '* Indirect\n**Influenced By (Stressors):**\n* Many factors\n**Influences (Stressors)**\n*  Pastoral Lands - Overgrazing\n**Logic Description**: Socioeconomic factors influence land use decisions.'
anthropogenic_pastoral_lands_stressors["Socioeconomic Factors"]["Influenced By"] = ['* Many factors', '**Influences (Stressors)**', '*  Pastoral Lands - Overgrazing', '**Logic Description**: Socioeconomic factors influence land use decisions.']
anthropogenic_pastoral_lands_stressors["Socioeconomic Factors"]["Impact Function"] = "impact_socioeconomic_factors_anthropogenic_pastoral_lands"

# --- Stocking Rates ---
anthropogenic_pastoral_lands_stressors["Stocking Rates"]["Data Sources"] = ['* Livestock censuses', '**Impact on Area**: Grazing pressure', '**Impact on Biodiversity:**', '* Overgrazing impacts', '**Influenced By (Stressors):**', '* Pastoral Lands - Socioeconomic Factors', '**Influences (Stressors):**', '* Pastoral Lands - Overgrazing', '**Logic Description**: Stocking rates are a key management factor.']
anthropogenic_pastoral_lands_stressors["Stocking Rates"]["Impact on Biodiversity"] = '* Overgrazing impacts\n**Influenced By (Stressors):**\n* Pastoral Lands - Socioeconomic Factors\n**Influences (Stressors):**\n* Pastoral Lands - Overgrazing\n**Logic Description**: Stocking rates are a key management factor.'
anthropogenic_pastoral_lands_stressors["Stocking Rates"]["Influenced By"] = ['* Pastoral Lands - Socioeconomic Factors', '**Influences (Stressors):**', '* Pastoral Lands - Overgrazing', '**Logic Description**: Stocking rates are a key management factor.']
anthropogenic_pastoral_lands_stressors["Stocking Rates"]["Influences"] = ['* Pastoral Lands - Overgrazing', '**Logic Description**: Stocking rates are a key management factor.']
anthropogenic_pastoral_lands_stressors["Stocking Rates"]["Impact Function"] = "impact_stocking_rates_anthropogenic_pastoral_lands"

# --- Grazing Management Practices ---
anthropogenic_pastoral_lands_stressors["Grazing Management Practices"]["Data Sources"] = ['* Surveys', '* Research', '**Impact on Area**: Variable, can have positive or negative impacts.', '**Impact on Biodiversity**:', '* Variable', '**Influenced By (Stressors):**', '* Pastoral Lands - Socioeconomic Factors', '**Influences (Stressors)**', '* Pastoral Lands - Overgrazing', '* Many', '**Logic Description:** Management practices influence grazing impacts.']
anthropogenic_pastoral_lands_stressors["Grazing Management Practices"]["Influenced By"] = ['* Pastoral Lands - Socioeconomic Factors', '**Influences (Stressors)**', '* Pastoral Lands - Overgrazing', '* Many', '**Logic Description:** Management practices influence grazing impacts.']
anthropogenic_pastoral_lands_stressors["Grazing Management Practices"]["Logic Description"] = '---'
anthropogenic_pastoral_lands_stressors["Grazing Management Practices"]["Impact Function"] = "impact_grazing_management_practices_anthropogenic_pastoral_lands"

# --- Climate Variability ---
anthropogenic_pastoral_lands_stressors["Climate Variability"]["Impact on Biodiversity"] = '* Increased stress on plants and animals.\n**Influenced By (Stressors)**\n* Climate Change\n**Influences (Stressors)**\n* Pastoral Lands - Overgrazing\n**Logic Description**: Climate variability adds to the challenges of pastoralism.'
anthropogenic_pastoral_lands_stressors["Climate Variability"]["Impact Function"] = "impact_climate_variability_anthropogenic_pastoral_lands"

# --- Land Tenure and Access Rights ---
anthropogenic_pastoral_lands_stressors["Land Tenure and Access Rights"]["Data Sources"] = ['* Legal documents', '* Surveys', '**Impact on Area**: Influences management practices and investment in land.', '**Impact on Biodiversity**:', '* Indirect, through impacts on management.', '**Influenced By (Stressors)**', '* Government policies', '* Social factors', '**Influences (Stressors):**', '* Pastoral Lands - Overgrazing', '**Logic Description**: Secure land tenure is often linked to better management.']
anthropogenic_pastoral_lands_stressors["Land Tenure and Access Rights"]["Influences"] = ['* Pastoral Lands - Overgrazing', '**Logic Description**: Secure land tenure is often linked to better management.']
anthropogenic_pastoral_lands_stressors["Land Tenure and Access Rights"]["Impact Function"] = "impact_land_tenure_and_access_rights_anthropogenic_pastoral_lands"

# --- Desertification ---
anthropogenic_pastoral_lands_stressors["Desertification"]["Data Sources"] = ['* Remote sensing', '* Field surveys', '**Impact on Area**: Loss of productivity, land abandonment', '**Impact on Biodiversity**:', '* Major loss of biodiversity.', '**Influenced By (Stressors):**', '*  Pastoral Lands - Overgrazing', '* Climate Change', '**Influences (Stressors)**', '* Many', '**Logic Description**: Extreme land degradation.']
anthropogenic_pastoral_lands_stressors["Desertification"]["Influenced By"] = ['*  Pastoral Lands - Overgrazing', '* Climate Change', '**Influences (Stressors)**', '* Many', '**Logic Description**: Extreme land degradation.']
anthropogenic_pastoral_lands_stressors["Desertification"]["Impact Function"] = "impact_desertification_anthropogenic_pastoral_lands"

# --- Water Quality ---
anthropogenic_pastoral_lands_stressors["Water Quality"]["Data Sources"] = ['* Water quality monitoring.', '**Impact on Area**: Affects drinking water for livestock and humans', '**Impact on Biodiversity:**', '* Impacts on aquatic ecosystems.', '**Influenced By (Stressors):**', '*  Pastoral Lands - Overgrazing (leading to erosion)', '**Influences (Stressors)**', '* Livestock and human health', '**Logic Description:** Water quality in pastoral systems.']
anthropogenic_pastoral_lands_stressors["Water Quality"]["Impact on Biodiversity"] = '* Impacts on aquatic ecosystems.\n**Influenced By (Stressors):**\n*  Pastoral Lands - Overgrazing (leading to erosion)\n**Influences (Stressors)**\n* Livestock and human health\n**Logic Description:** Water quality in pastoral systems.'
anthropogenic_pastoral_lands_stressors["Water Quality"]["Influenced By"] = ['*  Pastoral Lands - Overgrazing (leading to erosion)', '**Influences (Stressors)**', '* Livestock and human health', '**Logic Description:** Water quality in pastoral systems.']
anthropogenic_pastoral_lands_stressors["Water Quality"]["Logic Description"] = '---'
anthropogenic_pastoral_lands_stressors["Water Quality"]["Impact Function"] = "impact_water_quality_anthropogenic_pastoral_lands"

# --- Wildfires ---
anthropogenic_pastoral_lands_stressors["Wildfires"]["Data Sources"] = ['* Remote Sensing', '**Impact on Area**: Can be positive (in some ecosystems) or negative (if too frequent or intense)', '**Impact on Biodiversity**:', '* Variable.', '**Influenced By (Stressors):**', '* Climate Change', '* Pastoral Lands - Overgrazing (can increase fuel load in some cases).', '**Influences (Stressors):**', '* Many', '**Logic Description**: Fire is a natural process, but can be altered by human activities.']
anthropogenic_pastoral_lands_stressors["Wildfires"]["Influenced By"] = ['* Climate Change', '* Pastoral Lands - Overgrazing (can increase fuel load in some cases).', '**Influences (Stressors):**', '* Many', '**Logic Description**: Fire is a natural process, but can be altered by human activities.']
anthropogenic_pastoral_lands_stressors["Wildfires"]["Influences"] = ['* Many', '**Logic Description**: Fire is a natural process, but can be altered by human activities.']
anthropogenic_pastoral_lands_stressors["Wildfires"]["Impact Function"] = "impact_wildfires_anthropogenic_pastoral_lands"

# --- Forage Production ---
anthropogenic_pastoral_lands_stressors["Forage Production"]["Metric"] = 'Biomass of palatable plants.'
anthropogenic_pastoral_lands_stressors["Forage Production"]["Data Sources"] = ['* Field Measurements', '* Remote Sensing.', '**Impact on Area:** Determines carrying capacity for livestock.', '**Impact on Biodiversity:**', '* Indirect, affects available resources', '**Influenced By (Stressors):**', '* Many', '**Influences (Stressors):**', '*  Livestock production.', '**Logic Description:** Forage production is the basis of pastoral systems.']
anthropogenic_pastoral_lands_stressors["Forage Production"]["Impact on Area"] = 'Determines carrying capacity for livestock.'
anthropogenic_pastoral_lands_stressors["Forage Production"]["Impact on Biodiversity"] = '* Indirect, affects available resources\n**Influenced By (Stressors):**\n* Many\n**Influences (Stressors):**\n*  Livestock production.\n**Logic Description:** Forage production is the basis of pastoral systems.'
anthropogenic_pastoral_lands_stressors["Forage Production"]["Influenced By"] = ['* Many', '**Influences (Stressors):**', '*  Livestock production.', '**Logic Description:** Forage production is the basis of pastoral systems.']
anthropogenic_pastoral_lands_stressors["Forage Production"]["Influences"] = ['*  Livestock production.', '**Logic Description:** Forage production is the basis of pastoral systems.']
anthropogenic_pastoral_lands_stressors["Forage Production"]["Logic Description"] = '---'
anthropogenic_pastoral_lands_stressors["Forage Production"]["Impact Function"] = "impact_forage_production_anthropogenic_pastoral_lands"

# --- Vegetation Changes ---
anthropogenic_pastoral_lands_stressors["Vegetation Changes"]["Data Sources"] = ['* Field surveys', '* Remote sensing', '**Impact on Area:** Habitat structure and quality', '**Impact on Biodiversity:**', 'Changes in species composition.', '**Influenced By (Stressors):**', '* Pastoral Lands - Overgrazing', '* Many Other', '**Influences (Stressors):**', '* Many', '**Logic Description**: Changes in Vegetation reflect multiple stressors.']
anthropogenic_pastoral_lands_stressors["Vegetation Changes"]["Impact on Area"] = 'Habitat structure and quality'
anthropogenic_pastoral_lands_stressors["Vegetation Changes"]["Impact on Biodiversity"] = 'Changes in species composition.\n**Influenced By (Stressors):**\n* Pastoral Lands - Overgrazing\n* Many Other\n**Influences (Stressors):**\n* Many\n**Logic Description**: Changes in Vegetation reflect multiple stressors.'
anthropogenic_pastoral_lands_stressors["Vegetation Changes"]["Influenced By"] = ['* Pastoral Lands - Overgrazing', '* Many Other', '**Influences (Stressors):**', '* Many', '**Logic Description**: Changes in Vegetation reflect multiple stressors.']
anthropogenic_pastoral_lands_stressors["Vegetation Changes"]["Influences"] = ['* Many', '**Logic Description**: Changes in Vegetation reflect multiple stressors.']
anthropogenic_pastoral_lands_stressors["Vegetation Changes"]["Impact Function"] = "impact_vegetation_changes_anthropogenic_pastoral_lands"

