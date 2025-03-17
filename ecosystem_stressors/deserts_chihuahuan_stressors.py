from stressor_templates import *
import copy

deserts_chihuahuan_stressors = {
    "Overgrazing": {},
    "Water Extraction": copy.deepcopy(water_extraction_template),
    "Land-Use Change": {},
    "Invasive Species": copy.deepcopy(invasive_species_template),
    "Climate Change": copy.deepcopy(climate_change_template),
}

# --- Overgrazing ---
deserts_chihuahuan_stressors["Overgrazing"]["Metric"] = 'Livestock density; vegetation cover and composition; soil erosion.'
deserts_chihuahuan_stressors["Overgrazing"]["Data Sources"] = ['US Bureau of Land Management (BLM) data (for public lands).', 'Mexican government data.', 'Research publications.', '**Impact on Area:** Degradation of vegetation; soil erosion; shrub encroachment.', '**Impact on Biodiversity:**', 'Loss of palatable grasses and forbs.', 'Changes in plant community composition.', 'Impacts on wildlife that depend on grasslands.', '**Influenced By (Stressors):**', 'Livestock Management Practices: Overstocking.', 'Land Tenure Systems.', '**Influences (Stressors):**', 'Desertification.', 'Shrub Encroachment.', '**Logic Description:** Overgrazing by livestock is a *widespread* problem in the Chihuahuan Desert, leading to vegetation degradation, soil erosion, and shifts in plant communities.']
deserts_chihuahuan_stressors["Overgrazing"]["Impact on Area"] = 'Degradation of vegetation; soil erosion; shrub encroachment.'
deserts_chihuahuan_stressors["Overgrazing"]["Impact on Biodiversity"] = 'Loss of palatable grasses and forbs.\nChanges in plant community composition.\nImpacts on wildlife that depend on grasslands.\n**Influenced By (Stressors):**\nLivestock Management Practices: Overstocking.\nLand Tenure Systems.\n**Influences (Stressors):**\nDesertification.\nShrub Encroachment.\n**Logic Description:** Overgrazing by livestock is a *widespread* problem in the Chihuahuan Desert, leading to vegetation degradation, soil erosion, and shifts in plant communities.'
deserts_chihuahuan_stressors["Overgrazing"]["Influenced By"] = ['Livestock Management Practices: Overstocking.', 'Land Tenure Systems.', '**Influences (Stressors):**', 'Desertification.', 'Shrub Encroachment.', '**Logic Description:** Overgrazing by livestock is a *widespread* problem in the Chihuahuan Desert, leading to vegetation degradation, soil erosion, and shifts in plant communities.']
deserts_chihuahuan_stressors["Overgrazing"]["Influences"] = ['Desertification.', 'Shrub Encroachment.', '**Logic Description:** Overgrazing by livestock is a *widespread* problem in the Chihuahuan Desert, leading to vegetation degradation, soil erosion, and shifts in plant communities.']
deserts_chihuahuan_stressors["Overgrazing"]["Logic Description"] = '---'

# --- Water Extraction ---
deserts_chihuahuan_stressors["Water Extraction"]["Metric"] = 'Volume of groundwater extracted (m³/year); changes in groundwater levels; impacts on springs.'
deserts_chihuahuan_stressors["Water Extraction"]["Data Sources"] = ['USGS water resource data.', 'Mexican government data.', 'Research publications.', '**Impact on Area:** Depletion of groundwater; loss of water sources.', '**Impact on Biodiversity:**', 'Impacts on riparian habitats and springs, which are crucial for many desert species.', 'Increased stress on vegetation.', '**Influenced By (Stressors):**', 'Agricultural Water Use.', 'Urban Water Demand.', 'Mining Activities.', '**Influences (Stressors):**', 'Water Availability.', '**Logic Description:** Groundwater extraction for agriculture, urban use, and mining is a significant concern, impacting water availability for desert ecosystems.']
deserts_chihuahuan_stressors["Water Extraction"]["Impact on Area"] = 'Depletion of groundwater; loss of water sources.'
deserts_chihuahuan_stressors["Water Extraction"]["Impact on Biodiversity"] = 'Impacts on riparian habitats and springs, which are crucial for many desert species.\nIncreased stress on vegetation.\n**Influenced By (Stressors):**\nAgricultural Water Use.\nUrban Water Demand.\nMining Activities.\n**Influences (Stressors):**\nWater Availability.\n**Logic Description:** Groundwater extraction for agriculture, urban use, and mining is a significant concern, impacting water availability for desert ecosystems.'
deserts_chihuahuan_stressors["Water Extraction"]["Influenced By"] = ['Agricultural Water Use.', 'Urban Water Demand.', 'Mining Activities.', '**Influences (Stressors):**', 'Water Availability.', '**Logic Description:** Groundwater extraction for agriculture, urban use, and mining is a significant concern, impacting water availability for desert ecosystems.']
deserts_chihuahuan_stressors["Water Extraction"]["Influences"] = ['Water Availability.', '**Logic Description:** Groundwater extraction for agriculture, urban use, and mining is a significant concern, impacting water availability for desert ecosystems.']
deserts_chihuahuan_stressors["Water Extraction"]["Logic Description"] = '---'

# --- Land-Use Change ---
deserts_chihuahuan_stressors["Land-Use Change"]["Metric"] = 'Area converted to agriculture, urban development, or other uses (ha/year).'
deserts_chihuahuan_stressors["Land-Use Change"]["Data Sources"] = ['* Remote Sensing', '* Government', '**Impact on Area:** Habitat loss and fragmentation.', '**Impact on Biodiversity:**', 'Loss of habitat.', 'Disruption of ecological processes.', '**Influenced By (Stressors):**', '* Agricultural expansion', '* Urban sprawl', '**Influences (Stressors):**', '* Fragmentation.', '**Logic Description:** Conversion of desert habitat to other land uses.']
deserts_chihuahuan_stressors["Land-Use Change"]["Impact on Area"] = 'Habitat loss and fragmentation.'
deserts_chihuahuan_stressors["Land-Use Change"]["Impact on Biodiversity"] = 'Loss of habitat.\nDisruption of ecological processes.\n**Influenced By (Stressors):**\n* Agricultural expansion\n* Urban sprawl\n**Influences (Stressors):**\n* Fragmentation.\n**Logic Description:** Conversion of desert habitat to other land uses.'
deserts_chihuahuan_stressors["Land-Use Change"]["Influenced By"] = ['* Agricultural expansion', '* Urban sprawl', '**Influences (Stressors):**', '* Fragmentation.', '**Logic Description:** Conversion of desert habitat to other land uses.']
deserts_chihuahuan_stressors["Land-Use Change"]["Influences"] = ['* Fragmentation.', '**Logic Description:** Conversion of desert habitat to other land uses.']
deserts_chihuahuan_stressors["Land-Use Change"]["Logic Description"] = '---'

# --- Invasive Species ---
deserts_chihuahuan_stressors["Invasive Species"]["Metric"] = 'Distribution and abundance of key invasive species (e.g., Lehmann lovegrass).'
deserts_chihuahuan_stressors["Invasive Species"]["Data Sources"] = ['* Vegetation surveys', '* Research.', '**Impact on Area:** Changes in vegetation composition and structure; altered fire regimes (in some cases).', '**Impact on Biodiversity:**', '* Competition', '* Altered fire.', '**Influenced By (Stressors):**', 'Disturbance (e.g., overgrazing).', '**Influences (Stressors):**', '* Native Plants', '* Fire', '**Logic Description:** Invasive plants can outcompete natives and alter fire regimes.']
deserts_chihuahuan_stressors["Invasive Species"]["Impact on Area"] = 'Changes in vegetation composition and structure; altered fire regimes (in some cases).'
deserts_chihuahuan_stressors["Invasive Species"]["Impact on Biodiversity"] = '* Competition\n* Altered fire.\n**Influenced By (Stressors):**\nDisturbance (e.g., overgrazing).\n**Influences (Stressors):**\n* Native Plants\n* Fire\n**Logic Description:** Invasive plants can outcompete natives and alter fire regimes.'
deserts_chihuahuan_stressors["Invasive Species"]["Influenced By"] = ['Disturbance (e.g., overgrazing).', '**Influences (Stressors):**', '* Native Plants', '* Fire', '**Logic Description:** Invasive plants can outcompete natives and alter fire regimes.']
deserts_chihuahuan_stressors["Invasive Species"]["Influences"] = ['* Native Plants', '* Fire', '**Logic Description:** Invasive plants can outcompete natives and alter fire regimes.']
deserts_chihuahuan_stressors["Invasive Species"]["Logic Description"] = '---'

# --- Climate Change ---
deserts_chihuahuan_stressors["Climate Change"]["Metric"] = 'Temperature increase; changes in precipitation; increased drought.'
deserts_chihuahuan_stressors["Climate Change"]["Data Sources"] = ['* Climate models.', '* Historical Data.', '**Impact on Area:** Increased aridity', '**Impact on Biodiversity:**', '* Stress on species.', '* Distribution changes.', '**Influenced By (Stressors):**', '* Global GHG', '**Influences (Stressors):**', '* Water Availability.', '**Logic Description:** Climate change will exacerbate aridity and water stress.']
deserts_chihuahuan_stressors["Climate Change"]["Impact on Area"] = 'Increased aridity'
deserts_chihuahuan_stressors["Climate Change"]["Impact on Biodiversity"] = '* Stress on species.\n* Distribution changes.\n**Influenced By (Stressors):**\n* Global GHG\n**Influences (Stressors):**\n* Water Availability.\n**Logic Description:** Climate change will exacerbate aridity and water stress.'
deserts_chihuahuan_stressors["Climate Change"]["Influenced By"] = ['* Global GHG', '**Influences (Stressors):**', '* Water Availability.', '**Logic Description:** Climate change will exacerbate aridity and water stress.']
deserts_chihuahuan_stressors["Climate Change"]["Influences"] = ['* Water Availability.', '**Logic Description:** Climate change will exacerbate aridity and water stress.']
deserts_chihuahuan_stressors["Climate Change"]["Logic Description"] = '---'

