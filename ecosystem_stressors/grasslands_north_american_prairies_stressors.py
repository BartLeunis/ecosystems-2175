from stressor_templates import *
import copy

grasslands_north_american_prairies_stressors = {
    "Land-Use Change": {},
    "Habitat Fragmentation": {},
    "Invasive Species": copy.deepcopy(invasive_species_template),
    "Climate Change": copy.deepcopy(climate_change_template),
    "Fire Suppression": copy.deepcopy(fire_regime_template),
    "Overgrazing": {},
    "Agricultural Expansion": {},
    "Urban Sprawl": {},
    "Government Policies": {},
    "Infrastructure Development": copy.deepcopy(infrastructure_development_template),
    "Disturbance": {},
    "Introduction": {},
    "Land Management Practices": {},
    "Fire Regimes": copy.deepcopy(fire_regime_template),
    "Woody encroachment": {},
    "Fire Intensity": copy.deepcopy(fire_regime_template),
    "Water Availability": {},
    "Vegetation Changes": {},
}

# --- Land-Use Change ---
grasslands_north_american_prairies_stressors["Land-Use Change"]["Metric"] = 'Area converted to agriculture, urban development, or other land uses (ha/year).'
grasslands_north_american_prairies_stressors["Land-Use Change"]["Data Sources"] = ['USDA National Agricultural Statistics Service (NASS).', 'USGS National Land Cover Database (NLCD).', 'Canadian government data (e.g., Agriculture and Agri-Food Canada).', 'Remote sensing data.', '**Impact on Area:** Drastic reduction in prairie area (historically, the most significant stressor).', '**Impact on Biodiversity:**', 'Massive habitat loss and fragmentation.', 'Decline of prairie-dependent species (plants, animals, insects).', 'Increased risk of extinction for many species.', '**Influenced By (Stressors):**', 'North American Prairies - Agricultural Expansion', 'North American Prairies - Urban Sprawl', 'North American Prairies - Government Policies', '**Influences (Stressors):**', 'North American Prairies - Habitat Fragmentation', '**Logic Description:** Conversion of prairie to agriculture and urban areas has been the dominant stressor, leading to massive habitat loss and fragmentation. This is the primary reason why prairies are one of the most endangered ecosystems on Earth.']
grasslands_north_american_prairies_stressors["Land-Use Change"]["Impact on Area"] = 'Drastic reduction in prairie area (historically, the most significant stressor).'
grasslands_north_american_prairies_stressors["Land-Use Change"]["Impact on Biodiversity"] = 'Massive habitat loss and fragmentation.\nDecline of prairie-dependent species (plants, animals, insects).\nIncreased risk of extinction for many species.\n**Influenced By (Stressors):**\nNorth American Prairies - Agricultural Expansion\nNorth American Prairies - Urban Sprawl\nNorth American Prairies - Government Policies\n**Influences (Stressors):**\nNorth American Prairies - Habitat Fragmentation\n**Logic Description:** Conversion of prairie to agriculture and urban areas has been the dominant stressor, leading to massive habitat loss and fragmentation. This is the primary reason why prairies are one of the most endangered ecosystems on Earth.'
grasslands_north_american_prairies_stressors["Land-Use Change"]["Influenced By"] = ['North American Prairies - Agricultural Expansion', 'North American Prairies - Urban Sprawl', 'North American Prairies - Government Policies', '**Influences (Stressors):**', 'North American Prairies - Habitat Fragmentation', '**Logic Description:** Conversion of prairie to agriculture and urban areas has been the dominant stressor, leading to massive habitat loss and fragmentation. This is the primary reason why prairies are one of the most endangered ecosystems on Earth.']
grasslands_north_american_prairies_stressors["Land-Use Change"]["Influences"] = ['North American Prairies - Habitat Fragmentation', '**Logic Description:** Conversion of prairie to agriculture and urban areas has been the dominant stressor, leading to massive habitat loss and fragmentation. This is the primary reason why prairies are one of the most endangered ecosystems on Earth.']
grasslands_north_american_prairies_stressors["Land-Use Change"]["Logic Description"] = '---'

# --- Habitat Fragmentation ---
grasslands_north_american_prairies_stressors["Habitat Fragmentation"]["Metric"] = 'Patch size distribution; edge density; connectivity indices.'
grasslands_north_american_prairies_stressors["Habitat Fragmentation"]["Data Sources"] = ['Land cover data (from remote sensing and other sources).', 'GIS analysis.', '**Impact on Area:** Remaining prairie exists in small, isolated patches.', '**Impact on Biodiversity:**', 'Reduced gene flow.', 'Increased edge effects (exposure to predators, invasive species, altered microclimate).', 'Limited dispersal ability for many species.', 'Increased vulnerability to stochastic events (e.g., disease outbreaks, extreme weather).', '**Influenced By (Stressors):**', 'North American Prairies - Land-Use Change', 'North American Prairies - Infrastructure Development', '**Influences (Stressors):**', '* Exacerbates impacts of other stressors.', '**Logic Description:** Fragmentation, a consequence of land-use change, isolates remaining prairie patches, reducing their ecological viability and increasing the vulnerability of prairie species.']
grasslands_north_american_prairies_stressors["Habitat Fragmentation"]["Impact on Area"] = 'Remaining prairie exists in small, isolated patches.'
grasslands_north_american_prairies_stressors["Habitat Fragmentation"]["Impact on Biodiversity"] = 'Reduced gene flow.\nIncreased edge effects (exposure to predators, invasive species, altered microclimate).\nLimited dispersal ability for many species.\nIncreased vulnerability to stochastic events (e.g., disease outbreaks, extreme weather).\n**Influenced By (Stressors):**\nNorth American Prairies - Land-Use Change\nNorth American Prairies - Infrastructure Development\n**Influences (Stressors):**\n* Exacerbates impacts of other stressors.\n**Logic Description:** Fragmentation, a consequence of land-use change, isolates remaining prairie patches, reducing their ecological viability and increasing the vulnerability of prairie species.'
grasslands_north_american_prairies_stressors["Habitat Fragmentation"]["Influenced By"] = ['North American Prairies - Land-Use Change', 'North American Prairies - Infrastructure Development', '**Influences (Stressors):**', '* Exacerbates impacts of other stressors.', '**Logic Description:** Fragmentation, a consequence of land-use change, isolates remaining prairie patches, reducing their ecological viability and increasing the vulnerability of prairie species.']
grasslands_north_american_prairies_stressors["Habitat Fragmentation"]["Influences"] = ['* Exacerbates impacts of other stressors.', '**Logic Description:** Fragmentation, a consequence of land-use change, isolates remaining prairie patches, reducing their ecological viability and increasing the vulnerability of prairie species.']
grasslands_north_american_prairies_stressors["Habitat Fragmentation"]["Logic Description"] = '---'

# --- Invasive Species ---
grasslands_north_american_prairies_stressors["Invasive Species"]["Metric"] = 'Abundance and distribution of key invasive species (e.g., smooth brome, leafy spurge, cheatgrass).'
grasslands_north_american_prairies_stressors["Invasive Species"]["Data Sources"] = ['Vegetation surveys.', 'Research studies.', 'Land management agency data.', '**Impact on Area:** Changes in vegetation composition and structure.', '**Impact on Biodiversity:**', 'Competition with native prairie plants.', 'Altered fire regimes (some invasives increase fire frequency or intensity).', 'Reduced forage quality for native grazers.', 'Changes in soil properties.', '**Influenced By (Stressors):**', 'North American Prairies - Disturbance', 'North American Prairies - Climate Change', 'North American Prairies - Introduction', '**Influences (Stressors):**', '*  North American Prairies - Fire Regimes', '**Logic Description:** Invasive species outcompete native prairie plants, altering ecosystem structure and function.']
grasslands_north_american_prairies_stressors["Invasive Species"]["Impact on Area"] = 'Changes in vegetation composition and structure.'
grasslands_north_american_prairies_stressors["Invasive Species"]["Impact on Biodiversity"] = 'Competition with native prairie plants.\nAltered fire regimes (some invasives increase fire frequency or intensity).\nReduced forage quality for native grazers.\nChanges in soil properties.\n**Influenced By (Stressors):**\nNorth American Prairies - Disturbance\nNorth American Prairies - Climate Change\nNorth American Prairies - Introduction\n**Influences (Stressors):**\n*  North American Prairies - Fire Regimes\n**Logic Description:** Invasive species outcompete native prairie plants, altering ecosystem structure and function.'
grasslands_north_american_prairies_stressors["Invasive Species"]["Influenced By"] = ['North American Prairies - Disturbance', 'North American Prairies - Climate Change', 'North American Prairies - Introduction', '**Influences (Stressors):**', '*  North American Prairies - Fire Regimes', '**Logic Description:** Invasive species outcompete native prairie plants, altering ecosystem structure and function.']
grasslands_north_american_prairies_stressors["Invasive Species"]["Influences"] = ['*  North American Prairies - Fire Regimes', '**Logic Description:** Invasive species outcompete native prairie plants, altering ecosystem structure and function.']
grasslands_north_american_prairies_stressors["Invasive Species"]["Logic Description"] = '---'

# --- Climate Change ---
grasslands_north_american_prairies_stressors["Climate Change"]["Metric"] = 'Temperature increase (°C); changes in precipitation (mm/year, seasonality); increased frequency and severity of drought.'
grasslands_north_american_prairies_stressors["Climate Change"]["Data Sources"] = ['* Climate Models', '* Historical Records', '**Impact on Area:** Indirect; changes in growing conditions.', '**Impact on Biodiversity:**', 'Shifts in species distributions.', 'Increased stress on native species.', 'Changes in phenology.', 'Increased fire risk (in some areas).', 'May favor some invasive species.', '**Influenced By (Stressors):**', '* Global GHG', '**Influences (Stressors):**', '*  North American Prairies - Fire Regimes', '*  North American Prairies - Water Availability', '**Logic Description:** Climate change is altering temperature and precipitation patterns, increasing stress on prairie ecosystems and potentially favoring invasive species.']
grasslands_north_american_prairies_stressors["Climate Change"]["Impact on Area"] = 'Indirect; changes in growing conditions.'
grasslands_north_american_prairies_stressors["Climate Change"]["Impact on Biodiversity"] = 'Shifts in species distributions.\nIncreased stress on native species.\nChanges in phenology.\nIncreased fire risk (in some areas).\nMay favor some invasive species.\n**Influenced By (Stressors):**\n* Global GHG\n**Influences (Stressors):**\n*  North American Prairies - Fire Regimes\n*  North American Prairies - Water Availability\n**Logic Description:** Climate change is altering temperature and precipitation patterns, increasing stress on prairie ecosystems and potentially favoring invasive species.'
grasslands_north_american_prairies_stressors["Climate Change"]["Influenced By"] = ['* Global GHG', '**Influences (Stressors):**', '*  North American Prairies - Fire Regimes', '*  North American Prairies - Water Availability', '**Logic Description:** Climate change is altering temperature and precipitation patterns, increasing stress on prairie ecosystems and potentially favoring invasive species.']
grasslands_north_american_prairies_stressors["Climate Change"]["Influences"] = ['*  North American Prairies - Fire Regimes', '*  North American Prairies - Water Availability', '**Logic Description:** Climate change is altering temperature and precipitation patterns, increasing stress on prairie ecosystems and potentially favoring invasive species.']
grasslands_north_american_prairies_stressors["Climate Change"]["Logic Description"] = '---'

# --- Fire Suppression ---
grasslands_north_american_prairies_stressors["Fire Suppression"]["Metric"] = 'Fire frequency (return interval - years); area burned (ha/year).'
grasslands_north_american_prairies_stressors["Fire Suppression"]["Data Sources"] = ['* Historical fire records.', '* Land management agency data.', '**Impact on Area:** Changes in vegetation structure (woody encroachment).', '**Impact on Biodiversity:**', 'Loss of open prairie habitat.', 'Decline of fire-dependent species.', 'Increased fuel loads, leading to more intense fires when they do occur.', '**Influenced By (Stressors):**', 'North American Prairies - Land Management Practices', '**Influences (Stressors):**', '*  North American Prairies - Woody Encroachment', '*  North American Prairies - Fire Intensity', '**Logic Description:** Fire suppression, a common management practice, has altered the natural fire regime of prairies, leading to woody encroachment (trees and shrubs invading grasslands) and the decline of fire-dependent species.']
grasslands_north_american_prairies_stressors["Fire Suppression"]["Impact on Area"] = 'Changes in vegetation structure (woody encroachment).'
grasslands_north_american_prairies_stressors["Fire Suppression"]["Impact on Biodiversity"] = 'Loss of open prairie habitat.\nDecline of fire-dependent species.\nIncreased fuel loads, leading to more intense fires when they do occur.\n**Influenced By (Stressors):**\nNorth American Prairies - Land Management Practices\n**Influences (Stressors):**\n*  North American Prairies - Woody Encroachment\n*  North American Prairies - Fire Intensity\n**Logic Description:** Fire suppression, a common management practice, has altered the natural fire regime of prairies, leading to woody encroachment (trees and shrubs invading grasslands) and the decline of fire-dependent species.'
grasslands_north_american_prairies_stressors["Fire Suppression"]["Influenced By"] = ['North American Prairies - Land Management Practices', '**Influences (Stressors):**', '*  North American Prairies - Woody Encroachment', '*  North American Prairies - Fire Intensity', '**Logic Description:** Fire suppression, a common management practice, has altered the natural fire regime of prairies, leading to woody encroachment (trees and shrubs invading grasslands) and the decline of fire-dependent species.']
grasslands_north_american_prairies_stressors["Fire Suppression"]["Influences"] = ['*  North American Prairies - Woody Encroachment', '*  North American Prairies - Fire Intensity', '**Logic Description:** Fire suppression, a common management practice, has altered the natural fire regime of prairies, leading to woody encroachment (trees and shrubs invading grasslands) and the decline of fire-dependent species.']
grasslands_north_american_prairies_stressors["Fire Suppression"]["Logic Description"] = '---'

# --- Overgrazing ---
grasslands_north_american_prairies_stressors["Overgrazing"]["Metric"] = 'Livestock Density, vegetation cover'
grasslands_north_american_prairies_stressors["Overgrazing"]["Data Sources"] = ['* Agricultural Statistics', '* Vegetation surveys', '**Impact on Area:** Changes in vegetation, soil erosion.', '**Impact on Biodiversity:**', '* Loss of palatable species.', '* Spread of invasives.', '* Soil compaction.', '**Influenced By (Stressors):**', '*  North American Prairies - Livestock Management', '**Influences (Stressors):**', '*  North American Prairies - Vegetation Changes', '**Logic Description:** Overgrazing can degrade prairie vegetation, leading to soil erosion and the spread of invasive species.']
grasslands_north_american_prairies_stressors["Overgrazing"]["Impact on Area"] = 'Changes in vegetation, soil erosion.'
grasslands_north_american_prairies_stressors["Overgrazing"]["Impact on Biodiversity"] = '* Loss of palatable species.\n* Spread of invasives.\n* Soil compaction.\n**Influenced By (Stressors):**\n*  North American Prairies - Livestock Management\n**Influences (Stressors):**\n*  North American Prairies - Vegetation Changes\n**Logic Description:** Overgrazing can degrade prairie vegetation, leading to soil erosion and the spread of invasive species.'
grasslands_north_american_prairies_stressors["Overgrazing"]["Influenced By"] = ['*  North American Prairies - Livestock Management', '**Influences (Stressors):**', '*  North American Prairies - Vegetation Changes', '**Logic Description:** Overgrazing can degrade prairie vegetation, leading to soil erosion and the spread of invasive species.']
grasslands_north_american_prairies_stressors["Overgrazing"]["Influences"] = ['*  North American Prairies - Vegetation Changes', '**Logic Description:** Overgrazing can degrade prairie vegetation, leading to soil erosion and the spread of invasive species.']
grasslands_north_american_prairies_stressors["Overgrazing"]["Logic Description"] = '---'

# --- Agricultural Expansion ---
grasslands_north_american_prairies_stressors["Agricultural Expansion"]["Metric"] = 'Area converted to agriculture.'
grasslands_north_american_prairies_stressors["Agricultural Expansion"]["Data Sources"] = ['* Government Data', '**Impact on Area:** Habitat loss.', '**Impact on Biodiversity:**', '* Species Loss', '**Influenced By (Stressors):**', '* Global Demand', '**Influences (Stressors):**', '*  North American Prairies - Land-Use Change', '**Logic Description**: Demand for agricultural land.']
grasslands_north_american_prairies_stressors["Agricultural Expansion"]["Impact on Area"] = 'Habitat loss.'
grasslands_north_american_prairies_stressors["Agricultural Expansion"]["Impact on Biodiversity"] = '* Species Loss\n**Influenced By (Stressors):**\n* Global Demand\n**Influences (Stressors):**\n*  North American Prairies - Land-Use Change\n**Logic Description**: Demand for agricultural land.'
grasslands_north_american_prairies_stressors["Agricultural Expansion"]["Influenced By"] = ['* Global Demand', '**Influences (Stressors):**', '*  North American Prairies - Land-Use Change', '**Logic Description**: Demand for agricultural land.']
grasslands_north_american_prairies_stressors["Agricultural Expansion"]["Influences"] = ['*  North American Prairies - Land-Use Change', '**Logic Description**: Demand for agricultural land.']

# --- Urban Sprawl ---
grasslands_north_american_prairies_stressors["Urban Sprawl"]["Impact on Area"] = 'Habitat loss.'
grasslands_north_american_prairies_stressors["Urban Sprawl"]["Impact on Biodiversity"] = '* Species Loss\n**Influenced By (Stressors):**\n* Population Growth\n**Influences (Stressors):**\n* North American Prairies - Land-Use Change\n**Logic Description**: Urban expansion consumes habitat.'
grasslands_north_american_prairies_stressors["Urban Sprawl"]["Influenced By"] = ['* Population Growth', '**Influences (Stressors):**', '* North American Prairies - Land-Use Change', '**Logic Description**: Urban expansion consumes habitat.']
grasslands_north_american_prairies_stressors["Urban Sprawl"]["Influences"] = ['* North American Prairies - Land-Use Change', '**Logic Description**: Urban expansion consumes habitat.']

# --- Government Policies ---
grasslands_north_american_prairies_stressors["Government Policies"]["Metric"] = 'Subsidies; regulations.'
grasslands_north_american_prairies_stressors["Government Policies"]["Impact on Area"] = 'Variable, can influence land use.'
grasslands_north_american_prairies_stressors["Government Policies"]["Impact on Biodiversity"] = '* Variable.\n**Influenced By (Stressors):**\n* Economics\n**Influences (Stressors):**\n*  North American Prairies - Land-Use Change\n*  North American Prairies - Agricultural Expansion\n**Logic Description**: Policies influence land use decisions.'
grasslands_north_american_prairies_stressors["Government Policies"]["Influenced By"] = ['* Economics', '**Influences (Stressors):**', '*  North American Prairies - Land-Use Change', '*  North American Prairies - Agricultural Expansion', '**Logic Description**: Policies influence land use decisions.']
grasslands_north_american_prairies_stressors["Government Policies"]["Influences"] = ['*  North American Prairies - Land-Use Change', '*  North American Prairies - Agricultural Expansion', '**Logic Description**: Policies influence land use decisions.']

# --- Infrastructure Development ---
grasslands_north_american_prairies_stressors["Infrastructure Development"]["Metric"] = 'Road density, etc.'
grasslands_north_american_prairies_stressors["Infrastructure Development"]["Data Sources"] = ['* Government Records', '**Impact on Area:** Fragmentation', '**Impact on Biodiversity:**', '* Habitat Loss.', '**Influenced By (Stressors):**', '* Economic Growth', '**Influences (Stressors):**', '* North American Prairies - Habitat Fragmentation', '**Logic Description:** Roads and other infrastructure fragment the landscape.']
grasslands_north_american_prairies_stressors["Infrastructure Development"]["Impact on Area"] = 'Fragmentation'
grasslands_north_american_prairies_stressors["Infrastructure Development"]["Impact on Biodiversity"] = '* Habitat Loss.\n**Influenced By (Stressors):**\n* Economic Growth\n**Influences (Stressors):**\n* North American Prairies - Habitat Fragmentation\n**Logic Description:** Roads and other infrastructure fragment the landscape.'
grasslands_north_american_prairies_stressors["Infrastructure Development"]["Influenced By"] = ['* Economic Growth', '**Influences (Stressors):**', '* North American Prairies - Habitat Fragmentation', '**Logic Description:** Roads and other infrastructure fragment the landscape.']
grasslands_north_american_prairies_stressors["Infrastructure Development"]["Influences"] = ['* North American Prairies - Habitat Fragmentation', '**Logic Description:** Roads and other infrastructure fragment the landscape.']
grasslands_north_american_prairies_stressors["Infrastructure Development"]["Logic Description"] = '---'

# --- Disturbance ---
grasslands_north_american_prairies_stressors["Disturbance"]["Data Sources"] = ['* Field Surveys', '**Impact on Area**: Site-specific', '**Impact on Biodiversity:**', '* Variable', '**Influenced By (Stressors):**', '*  North American Prairies - Overgrazing', '*  North American Prairies - Fire Suppression', '**Influences (Stressors):**', '* North American Prairies - Invasive Species', '**Logic Description:** General category for physical disturbances.']
grasslands_north_american_prairies_stressors["Disturbance"]["Impact on Biodiversity"] = '* Variable\n**Influenced By (Stressors):**\n*  North American Prairies - Overgrazing\n*  North American Prairies - Fire Suppression\n**Influences (Stressors):**\n* North American Prairies - Invasive Species\n**Logic Description:** General category for physical disturbances.'
grasslands_north_american_prairies_stressors["Disturbance"]["Influenced By"] = ['*  North American Prairies - Overgrazing', '*  North American Prairies - Fire Suppression', '**Influences (Stressors):**', '* North American Prairies - Invasive Species', '**Logic Description:** General category for physical disturbances.']
grasslands_north_american_prairies_stressors["Disturbance"]["Influences"] = ['* North American Prairies - Invasive Species', '**Logic Description:** General category for physical disturbances.']
grasslands_north_american_prairies_stressors["Disturbance"]["Logic Description"] = '---'

# --- Introduction ---
grasslands_north_american_prairies_stressors["Introduction"]["Metric"] = 'Number of introduced species'
grasslands_north_american_prairies_stressors["Introduction"]["Data Sources"] = ['* Records', '**Impact on Area:** Variable', '**Impact on Biodiversity:**', '* Competition, etc.', '**Influenced By (Stressors):**', '* Global trade', '**Influences (Stressors):**', '* North American Prairies - Invasive Species', '**Logic Description**: Intentional/Unintentional introductions']
grasslands_north_american_prairies_stressors["Introduction"]["Impact on Area"] = 'Variable'
grasslands_north_american_prairies_stressors["Introduction"]["Impact on Biodiversity"] = '* Competition, etc.\n**Influenced By (Stressors):**\n* Global trade\n**Influences (Stressors):**\n* North American Prairies - Invasive Species\n**Logic Description**: Intentional/Unintentional introductions'
grasslands_north_american_prairies_stressors["Introduction"]["Influenced By"] = ['* Global trade', '**Influences (Stressors):**', '* North American Prairies - Invasive Species', '**Logic Description**: Intentional/Unintentional introductions']
grasslands_north_american_prairies_stressors["Introduction"]["Influences"] = ['* North American Prairies - Invasive Species', '**Logic Description**: Intentional/Unintentional introductions']

# --- Land Management Practices ---
grasslands_north_american_prairies_stressors["Land Management Practices"]["Metric"] = 'Area Under different practices.'
grasslands_north_american_prairies_stressors["Land Management Practices"]["Data Sources"] = ['* Records and surveys.', '**Impact on Area:** Variable', '**Impact on Biodiversity:**', '* Variable.', '**Influenced By (Stressors):**', '* Policy', '**Influences (Stressors):**', '* North American Prairies - Fire Suppression', '* North American Prairies - Overgrazing', '**Logic Description:** Practices influence outcomes.']
grasslands_north_american_prairies_stressors["Land Management Practices"]["Impact on Area"] = 'Variable'
grasslands_north_american_prairies_stressors["Land Management Practices"]["Impact on Biodiversity"] = '* Variable.\n**Influenced By (Stressors):**\n* Policy\n**Influences (Stressors):**\n* North American Prairies - Fire Suppression\n* North American Prairies - Overgrazing\n**Logic Description:** Practices influence outcomes.'
grasslands_north_american_prairies_stressors["Land Management Practices"]["Influenced By"] = ['* Policy', '**Influences (Stressors):**', '* North American Prairies - Fire Suppression', '* North American Prairies - Overgrazing', '**Logic Description:** Practices influence outcomes.']
grasslands_north_american_prairies_stressors["Land Management Practices"]["Influences"] = ['* North American Prairies - Fire Suppression', '* North American Prairies - Overgrazing', '**Logic Description:** Practices influence outcomes.']
grasslands_north_american_prairies_stressors["Land Management Practices"]["Logic Description"] = '---'

# --- Fire Regimes ---
grasslands_north_american_prairies_stressors["Fire Regimes"]["Metric"] = 'Fire frequency, intensity, seasonality, size'
grasslands_north_american_prairies_stressors["Fire Regimes"]["Data Sources"] = ['* Remote Sensing', '* Historical Records', '**Impact on Area:** Vegetation Structure', '**Impact on Biodiversity:**', '* Species Composition.', '**Influenced By (Stressors):**', '*  North American Prairies - Fire Suppression', '*  North American Prairies - Climate Change', '*  North American Prairies - Invasive Species', '**Influences (Stressors):**', '* North American Prairies - Woody encroachment', '* North American Prairies - Invasive Species', '**Logic Description**: Fire is a natural process, but alterations can have negative impacts.']
grasslands_north_american_prairies_stressors["Fire Regimes"]["Impact on Area"] = 'Vegetation Structure'
grasslands_north_american_prairies_stressors["Fire Regimes"]["Impact on Biodiversity"] = '* Species Composition.\n**Influenced By (Stressors):**\n*  North American Prairies - Fire Suppression\n*  North American Prairies - Climate Change\n*  North American Prairies - Invasive Species\n**Influences (Stressors):**\n* North American Prairies - Woody encroachment\n* North American Prairies - Invasive Species\n**Logic Description**: Fire is a natural process, but alterations can have negative impacts.'
grasslands_north_american_prairies_stressors["Fire Regimes"]["Influenced By"] = ['*  North American Prairies - Fire Suppression', '*  North American Prairies - Climate Change', '*  North American Prairies - Invasive Species', '**Influences (Stressors):**', '* North American Prairies - Woody encroachment', '* North American Prairies - Invasive Species', '**Logic Description**: Fire is a natural process, but alterations can have negative impacts.']
grasslands_north_american_prairies_stressors["Fire Regimes"]["Influences"] = ['* North American Prairies - Woody encroachment', '* North American Prairies - Invasive Species', '**Logic Description**: Fire is a natural process, but alterations can have negative impacts.']

# --- Woody encroachment ---
grasslands_north_american_prairies_stressors["Woody encroachment"]["Data Sources"] = ['* Remote Sensing', '* Field Surveys', '**Impact on Area:** Habitat Change', '**Impact on Biodiversity:**', '* Loss of grassland species', '**Influenced By (Stressors):**', '* North American Prairies - Fire Suppression', '* North American Prairies - Fire Regimes', '**Influences (Stressors):**', '* Habitat Loss', '**Logic Description:** Trees and shrubs take over grasslands.']
grasslands_north_american_prairies_stressors["Woody encroachment"]["Impact on Area"] = 'Habitat Change'
grasslands_north_american_prairies_stressors["Woody encroachment"]["Impact on Biodiversity"] = '* Loss of grassland species\n**Influenced By (Stressors):**\n* North American Prairies - Fire Suppression\n* North American Prairies - Fire Regimes\n**Influences (Stressors):**\n* Habitat Loss\n**Logic Description:** Trees and shrubs take over grasslands.'
grasslands_north_american_prairies_stressors["Woody encroachment"]["Influenced By"] = ['* North American Prairies - Fire Suppression', '* North American Prairies - Fire Regimes', '**Influences (Stressors):**', '* Habitat Loss', '**Logic Description:** Trees and shrubs take over grasslands.']
grasslands_north_american_prairies_stressors["Woody encroachment"]["Influences"] = ['* Habitat Loss', '**Logic Description:** Trees and shrubs take over grasslands.']
grasslands_north_american_prairies_stressors["Woody encroachment"]["Logic Description"] = '---'

# --- Fire Intensity ---
grasslands_north_american_prairies_stressors["Fire Intensity"]["Data Sources"] = ['* Fire records.', '* Remote sensing.', '**Impact on Area:** Variable, depending on intensity.', '**Impact on Biodiversity:**', '*  Variable, depending on intensity.', '**Influenced By (Stressors):**', '* North American Prairies - Fire Suppression', '**Influences (Stressors):**', '* North American Prairies - Fire Regimes', '**Logic Description:** The intensity of fires affects impact.']
grasslands_north_american_prairies_stressors["Fire Intensity"]["Impact on Area"] = 'Variable, depending on intensity.'
grasslands_north_american_prairies_stressors["Fire Intensity"]["Impact on Biodiversity"] = '*  Variable, depending on intensity.\n**Influenced By (Stressors):**\n* North American Prairies - Fire Suppression\n**Influences (Stressors):**\n* North American Prairies - Fire Regimes\n**Logic Description:** The intensity of fires affects impact.'
grasslands_north_american_prairies_stressors["Fire Intensity"]["Influenced By"] = ['* North American Prairies - Fire Suppression', '**Influences (Stressors):**', '* North American Prairies - Fire Regimes', '**Logic Description:** The intensity of fires affects impact.']
grasslands_north_american_prairies_stressors["Fire Intensity"]["Influences"] = ['* North American Prairies - Fire Regimes', '**Logic Description:** The intensity of fires affects impact.']
grasslands_north_american_prairies_stressors["Fire Intensity"]["Logic Description"] = '---'

# --- Water Availability ---
grasslands_north_american_prairies_stressors["Water Availability"]["Metric"] = 'Precipitation, drought indices.'
grasslands_north_american_prairies_stressors["Water Availability"]["Impact on Area"] = 'Vegetation Growth.'
grasslands_north_american_prairies_stressors["Water Availability"]["Impact on Biodiversity"] = '* Species composition\n**Influenced By (Stressors):**\n* North American Prairies - Climate Change\n**Influences (Stressors):**\n* Many, varies\n**Logic Description:** Water availability drives many processes.'
grasslands_north_american_prairies_stressors["Water Availability"]["Influenced By"] = ['* North American Prairies - Climate Change', '**Influences (Stressors):**', '* Many, varies', '**Logic Description:** Water availability drives many processes.']
grasslands_north_american_prairies_stressors["Water Availability"]["Influences"] = ['* Many, varies', '**Logic Description:** Water availability drives many processes.']
grasslands_north_american_prairies_stressors["Water Availability"]["Logic Description"] = '---'

# --- Vegetation Changes ---
grasslands_north_american_prairies_stressors["Vegetation Changes"]["Metric"] = 'Plant community composition.'
grasslands_north_american_prairies_stressors["Vegetation Changes"]["Data Sources"] = ['* Field surveys.', '* Remote sensing', '**Impact on Area:** Habitat changes.', '**Impact on Biodiversity:**', '*  Altered species interactions.', '**Influenced By (Stressors):**', '* North American Prairies - Overgrazing', '**Influences (Stressors):**', '*  Many, varies.', '**Logic Description:** Changes in plant communities.']
grasslands_north_american_prairies_stressors["Vegetation Changes"]["Impact on Area"] = 'Habitat changes.'
grasslands_north_american_prairies_stressors["Vegetation Changes"]["Impact on Biodiversity"] = '*  Altered species interactions.\n**Influenced By (Stressors):**\n* North American Prairies - Overgrazing\n**Influences (Stressors):**\n*  Many, varies.\n**Logic Description:** Changes in plant communities.'
grasslands_north_american_prairies_stressors["Vegetation Changes"]["Influenced By"] = ['* North American Prairies - Overgrazing', '**Influences (Stressors):**', '*  Many, varies.', '**Logic Description:** Changes in plant communities.']
grasslands_north_american_prairies_stressors["Vegetation Changes"]["Influences"] = ['*  Many, varies.', '**Logic Description:** Changes in plant communities.']
grasslands_north_american_prairies_stressors["Vegetation Changes"]["Logic Description"] = ''

