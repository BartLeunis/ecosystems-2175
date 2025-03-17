from stressor_templates import *
import copy

deserts_sonoran_stressors = {
    "Urban Sprawl": {},
    "Water Extraction": copy.deepcopy(water_extraction_template),
    "Border Infrastructure": {},
    "Invasive Species": copy.deepcopy(invasive_species_template),
    "Climate Change": copy.deepcopy(climate_change_template),
}

# --- Urban Sprawl ---
deserts_sonoran_stressors["Urban Sprawl"]["Metric"] = 'Area converted to urban development (ha/year) (Phoenix, Tucson, etc.).'
deserts_sonoran_stressors["Urban Sprawl"]["Data Sources"] = ['Remote sensing data.', 'City and county planning documents.', '**Impact on Area:** *Significant* habitat loss and fragmentation.', '**Impact on Biodiversity:**', 'Loss of habitat for iconic desert species (e.g., saguaro cactus, desert tortoise).', 'Increased human-wildlife conflict.', '**Influenced By (Stressors):**', 'Population Growth: Rapid population growth in cities like Phoenix and Tucson.', 'Urban Expansion.', '**Influences (Stressors):**', 'Habitat Fragmentation.', '**Logic Description:** Urban sprawl, driven by rapid population growth in cities within and adjacent to the Sonoran Desert, is a *major* threat to habitat and biodiversity.']
deserts_sonoran_stressors["Urban Sprawl"]["Impact on Area"] = '*Significant* habitat loss and fragmentation.'
deserts_sonoran_stressors["Urban Sprawl"]["Impact on Biodiversity"] = 'Loss of habitat for iconic desert species (e.g., saguaro cactus, desert tortoise).\nIncreased human-wildlife conflict.\n**Influenced By (Stressors):**\nPopulation Growth: Rapid population growth in cities like Phoenix and Tucson.\nUrban Expansion.\n**Influences (Stressors):**\nHabitat Fragmentation.\n**Logic Description:** Urban sprawl, driven by rapid population growth in cities within and adjacent to the Sonoran Desert, is a *major* threat to habitat and biodiversity.'
deserts_sonoran_stressors["Urban Sprawl"]["Influenced By"] = ['Population Growth: Rapid population growth in cities like Phoenix and Tucson.', 'Urban Expansion.', '**Influences (Stressors):**', 'Habitat Fragmentation.', '**Logic Description:** Urban sprawl, driven by rapid population growth in cities within and adjacent to the Sonoran Desert, is a *major* threat to habitat and biodiversity.']
deserts_sonoran_stressors["Urban Sprawl"]["Influences"] = ['Habitat Fragmentation.', '**Logic Description:** Urban sprawl, driven by rapid population growth in cities within and adjacent to the Sonoran Desert, is a *major* threat to habitat and biodiversity.']
deserts_sonoran_stressors["Urban Sprawl"]["Logic Description"] = '---'
deserts_sonoran_stressors["Urban Sprawl"]["Impact Function"] = "impact_urban_sprawl_deserts_sonoran"

# --- Water Extraction ---
deserts_sonoran_stressors["Water Extraction"]["Metric"] = 'Volume of groundwater extracted (m³/year); changes in groundwater levels; impacts on springs.'
deserts_sonoran_stressors["Water Extraction"]["Data Sources"] = ['USGS water resource data.', 'Arizona Department of Water Resources data.', 'Research publications.', '**Impact on Area:** Depletion of groundwater; loss of water sources.', '**Impact on Biodiversity:**', 'Impacts on riparian habitats and springs, which are crucial for many desert species.', 'Increased stress on vegetation.', '**Influenced By (Stressors):**', 'Urban Water Demand.', 'Agricultural Water Use.', '**Influences (Stressors):**', 'Water Availability.', '**Logic Description:** Groundwater extraction for urban and agricultural use is a major concern, impacting water availability for desert ecosystems.']
deserts_sonoran_stressors["Water Extraction"]["Impact on Area"] = 'Depletion of groundwater; loss of water sources.'
deserts_sonoran_stressors["Water Extraction"]["Impact on Biodiversity"] = 'Impacts on riparian habitats and springs, which are crucial for many desert species.\nIncreased stress on vegetation.\n**Influenced By (Stressors):**\nUrban Water Demand.\nAgricultural Water Use.\n**Influences (Stressors):**\nWater Availability.\n**Logic Description:** Groundwater extraction for urban and agricultural use is a major concern, impacting water availability for desert ecosystems.'
deserts_sonoran_stressors["Water Extraction"]["Influenced By"] = ['Urban Water Demand.', 'Agricultural Water Use.', '**Influences (Stressors):**', 'Water Availability.', '**Logic Description:** Groundwater extraction for urban and agricultural use is a major concern, impacting water availability for desert ecosystems.']
deserts_sonoran_stressors["Water Extraction"]["Influences"] = ['Water Availability.', '**Logic Description:** Groundwater extraction for urban and agricultural use is a major concern, impacting water availability for desert ecosystems.']
deserts_sonoran_stressors["Water Extraction"]["Logic Description"] = '---'
deserts_sonoran_stressors["Water Extraction"]["Impact Function"] = "impact_water_extraction_deserts_sonoran"

# --- Border Infrastructure ---
deserts_sonoran_stressors["Border Infrastructure"]["Metric"] = 'Length and placement of border wall/fencing.'
deserts_sonoran_stressors["Border Infrastructure"]["Data Sources"] = ['* Government records', '**Impact on Area:** Fragmentation of habitat', '**Impact on Biodiversity:**', '* Blocks movement and gene flow for wildlife.', '**Influenced By (Stressors):**', '* Political decisions', '**Influences (Stressors):**', '* Wildlife movement', '**Logic Description:** Construction along the US-Mexico border impacts.']
deserts_sonoran_stressors["Border Infrastructure"]["Impact on Area"] = 'Fragmentation of habitat'
deserts_sonoran_stressors["Border Infrastructure"]["Impact on Biodiversity"] = '* Blocks movement and gene flow for wildlife.\n**Influenced By (Stressors):**\n* Political decisions\n**Influences (Stressors):**\n* Wildlife movement\n**Logic Description:** Construction along the US-Mexico border impacts.'
deserts_sonoran_stressors["Border Infrastructure"]["Influenced By"] = ['* Political decisions', '**Influences (Stressors):**', '* Wildlife movement', '**Logic Description:** Construction along the US-Mexico border impacts.']
deserts_sonoran_stressors["Border Infrastructure"]["Influences"] = ['* Wildlife movement', '**Logic Description:** Construction along the US-Mexico border impacts.']
deserts_sonoran_stressors["Border Infrastructure"]["Logic Description"] = '---'
deserts_sonoran_stressors["Border Infrastructure"]["Impact Function"] = "impact_border_infrastructure_deserts_sonoran"

# --- Invasive Species ---
deserts_sonoran_stressors["Invasive Species"]["Metric"] = 'Distribution and abundance (e.g., buffelgrass).'
deserts_sonoran_stressors["Invasive Species"]["Data Sources"] = ['Vegetation surveys.', 'Research studies.', '**Impact on Area:** Changes in vegetation; increased fire risk.', '**Impact on Biodiversity:**', '* Competition with native plants', '* Altered fire', '**Influenced By (Stressors):**', '* Disturbance', '* Climate Change', '**Influences (Stressors):**', '* Fire regimes.', '* Native plants', '**Logic Description:** Invasive plants like buffelgrass are outcompeting natives and increasing fire risk.']
deserts_sonoran_stressors["Invasive Species"]["Impact on Area"] = 'Changes in vegetation; increased fire risk.'
deserts_sonoran_stressors["Invasive Species"]["Impact on Biodiversity"] = '* Competition with native plants\n* Altered fire\n**Influenced By (Stressors):**\n* Disturbance\n* Climate Change\n**Influences (Stressors):**\n* Fire regimes.\n* Native plants\n**Logic Description:** Invasive plants like buffelgrass are outcompeting natives and increasing fire risk.'
deserts_sonoran_stressors["Invasive Species"]["Influenced By"] = ['* Disturbance', '* Climate Change', '**Influences (Stressors):**', '* Fire regimes.', '* Native plants', '**Logic Description:** Invasive plants like buffelgrass are outcompeting natives and increasing fire risk.']
deserts_sonoran_stressors["Invasive Species"]["Influences"] = ['* Fire regimes.', '* Native plants', '**Logic Description:** Invasive plants like buffelgrass are outcompeting natives and increasing fire risk.']
deserts_sonoran_stressors["Invasive Species"]["Logic Description"] = '---'
deserts_sonoran_stressors["Invasive Species"]["Impact Function"] = "impact_invasive_species_deserts_sonoran"

# --- Climate Change ---
deserts_sonoran_stressors["Climate Change"]["Metric"] = 'Increased temperature; changes in precipitation.'
deserts_sonoran_stressors["Climate Change"]["Data Sources"] = ['* Climate models.', '* Historical data.', '**Impact on Area:** Increased aridity', '**Impact on Biodiversity:**', '* Stress on species.', '* Shifts in distributions.', '**Influenced By (Stressors):**', '* Global GHG', '**Influences (Stressors):**', '* Water availability', '* Fire regimes', '**Logic Description:** Climate change impacts.']
deserts_sonoran_stressors["Climate Change"]["Impact on Area"] = 'Increased aridity'
deserts_sonoran_stressors["Climate Change"]["Impact on Biodiversity"] = '* Stress on species.\n* Shifts in distributions.\n**Influenced By (Stressors):**\n* Global GHG\n**Influences (Stressors):**\n* Water availability\n* Fire regimes\n**Logic Description:** Climate change impacts.'
deserts_sonoran_stressors["Climate Change"]["Influenced By"] = ['* Global GHG', '**Influences (Stressors):**', '* Water availability', '* Fire regimes', '**Logic Description:** Climate change impacts.']
deserts_sonoran_stressors["Climate Change"]["Influences"] = ['* Water availability', '* Fire regimes', '**Logic Description:** Climate change impacts.']
deserts_sonoran_stressors["Climate Change"]["Logic Description"] = '---'
deserts_sonoran_stressors["Climate Change"]["Impact Function"] = "impact_climate_change_deserts_sonoran"

