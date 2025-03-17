from stressor_templates import *
import copy

aquatic_kelp_forests_north_atlantic_stressors = {
    "Ocean Warming": {},
    "Invasive Species": copy.deepcopy(invasive_species_template),
    "Storms and Wave Action": {},
    "Pollution": copy.deepcopy(pollution_template),
}

# --- Ocean Warming ---
aquatic_kelp_forests_north_atlantic_stressors["Ocean Warming"]["Metric"] = 'Sea surface temperature (SST) (°C); frequency and severity of marine heatwaves; Degree Heating Weeks (DHW).'
aquatic_kelp_forests_north_atlantic_stressors["Ocean Warming"]["Data Sources"] = ['Satellite data', 'In-situ temperature loggers.', 'Climate models.', '**Impact on Area:** Reduced kelp growth and survival; kelp forest die-offs during extreme events.', '**Impact on Biodiversity:**', 'Loss of habitat for many fish, invertebrates, and marine mammals.', 'Changes in community structure (shift towards more warm-tolerant species).', 'Increased vulnerability to other stressors.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions: Primary driver.', '**Influences (Stressors):**', 'Sea Urchin Barrens Formation (see below).', '**Logic Description:** Rising ocean temperatures, particularly during marine heatwaves, can stress kelp, leading to reduced growth, increased mortality, and even large-scale die-offs.']
aquatic_kelp_forests_north_atlantic_stressors["Ocean Warming"]["Impact on Area"] = 'Reduced kelp growth and survival; kelp forest die-offs during extreme events.'
aquatic_kelp_forests_north_atlantic_stressors["Ocean Warming"]["Impact on Biodiversity"] = 'Loss of habitat for many fish, invertebrates, and marine mammals.\nChanges in community structure (shift towards more warm-tolerant species).\nIncreased vulnerability to other stressors.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions: Primary driver.\n**Influences (Stressors):**\nSea Urchin Barrens Formation (see below).\n**Logic Description:** Rising ocean temperatures, particularly during marine heatwaves, can stress kelp, leading to reduced growth, increased mortality, and even large-scale die-offs.'
aquatic_kelp_forests_north_atlantic_stressors["Ocean Warming"]["Influenced By"] = ['Global Greenhouse Gas Emissions: Primary driver.', '**Influences (Stressors):**', 'Sea Urchin Barrens Formation (see below).', '**Logic Description:** Rising ocean temperatures, particularly during marine heatwaves, can stress kelp, leading to reduced growth, increased mortality, and even large-scale die-offs.']
aquatic_kelp_forests_north_atlantic_stressors["Ocean Warming"]["Influences"] = ['Sea Urchin Barrens Formation (see below).', '**Logic Description:** Rising ocean temperatures, particularly during marine heatwaves, can stress kelp, leading to reduced growth, increased mortality, and even large-scale die-offs.']
aquatic_kelp_forests_north_atlantic_stressors["Ocean Warming"]["Logic Description"] = '---'
aquatic_kelp_forests_north_atlantic_stressors["Ocean Warming"]["Impact Function"] = "impact_ocean_warming_aquatic_kelp_forests_north_atlantic"

# --- Invasive Species ---
aquatic_kelp_forests_north_atlantic_stressors["Invasive Species"]["Metric"] = 'Distribution and abundance of key invasive species (e.g.,  *Membranipora membranacea*, a bryozoan).'
aquatic_kelp_forests_north_atlantic_stressors["Invasive Species"]["Data Sources"] = ['Underwater surveys.', 'Research publications', '**Impact on Area**: Impacts on kelp health and survival.', '**Impact on Biodiversity:**', '* *Membranipora* encrusts kelp blades, reducing their ability to photosynthesize and making them more susceptible to breakage.', '**Influenced By (Stressors):**', '* Shipping (ballast water, hull fouling).', '**Influences (Stressors):**', '* Kelp health and survival', '**Logic Description:** The invasive bryozoan *Membranipora membranacea* is a significant threat to kelp forests in some parts of the North Atlantic, encrusting kelp blades and reducing their photosynthetic capacity.']
aquatic_kelp_forests_north_atlantic_stressors["Invasive Species"]["Impact on Biodiversity"] = '* *Membranipora* encrusts kelp blades, reducing their ability to photosynthesize and making them more susceptible to breakage.\n**Influenced By (Stressors):**\n* Shipping (ballast water, hull fouling).\n**Influences (Stressors):**\n* Kelp health and survival\n**Logic Description:** The invasive bryozoan *Membranipora membranacea* is a significant threat to kelp forests in some parts of the North Atlantic, encrusting kelp blades and reducing their photosynthetic capacity.'
aquatic_kelp_forests_north_atlantic_stressors["Invasive Species"]["Influenced By"] = ['* Shipping (ballast water, hull fouling).', '**Influences (Stressors):**', '* Kelp health and survival', '**Logic Description:** The invasive bryozoan *Membranipora membranacea* is a significant threat to kelp forests in some parts of the North Atlantic, encrusting kelp blades and reducing their photosynthetic capacity.']
aquatic_kelp_forests_north_atlantic_stressors["Invasive Species"]["Influences"] = ['* Kelp health and survival', '**Logic Description:** The invasive bryozoan *Membranipora membranacea* is a significant threat to kelp forests in some parts of the North Atlantic, encrusting kelp blades and reducing their photosynthetic capacity.']
aquatic_kelp_forests_north_atlantic_stressors["Invasive Species"]["Logic Description"] = '---'
aquatic_kelp_forests_north_atlantic_stressors["Invasive Species"]["Impact Function"] = "impact_invasive_species_aquatic_kelp_forests_north_atlantic"

# --- Storms and Wave Action ---
aquatic_kelp_forests_north_atlantic_stressors["Storms and Wave Action"]["Metric"] = 'Wave Height, storm frequency'
aquatic_kelp_forests_north_atlantic_stressors["Storms and Wave Action"]["Data Sources"] = ['* Buoy Data', '* Weather records.', '* Climate Models', '**Impact on Area:** Physical damage/removal of kelp.', '**Impact on Biodiversity:**', '* Loss of habitat', '* Disturbance', '**Influenced By (Stressors):**', '* Climate Change', '* Weather Patterns', '**Influences (Stressors):**', '* Kelp forest structure', '**Logic Description:** Increased storm intensity or frequency, potentially linked to climate change, can cause physical damage to kelp forests.']
aquatic_kelp_forests_north_atlantic_stressors["Storms and Wave Action"]["Impact on Area"] = 'Physical damage/removal of kelp.'
aquatic_kelp_forests_north_atlantic_stressors["Storms and Wave Action"]["Impact on Biodiversity"] = '* Loss of habitat\n* Disturbance\n**Influenced By (Stressors):**\n* Climate Change\n* Weather Patterns\n**Influences (Stressors):**\n* Kelp forest structure\n**Logic Description:** Increased storm intensity or frequency, potentially linked to climate change, can cause physical damage to kelp forests.'
aquatic_kelp_forests_north_atlantic_stressors["Storms and Wave Action"]["Influenced By"] = ['* Climate Change', '* Weather Patterns', '**Influences (Stressors):**', '* Kelp forest structure', '**Logic Description:** Increased storm intensity or frequency, potentially linked to climate change, can cause physical damage to kelp forests.']
aquatic_kelp_forests_north_atlantic_stressors["Storms and Wave Action"]["Influences"] = ['* Kelp forest structure', '**Logic Description:** Increased storm intensity or frequency, potentially linked to climate change, can cause physical damage to kelp forests.']
aquatic_kelp_forests_north_atlantic_stressors["Storms and Wave Action"]["Logic Description"] = '---'
aquatic_kelp_forests_north_atlantic_stressors["Storms and Wave Action"]["Impact Function"] = "impact_storms_and_wave_action_aquatic_kelp_forests_north_atlantic"

# --- Pollution ---
aquatic_kelp_forests_north_atlantic_stressors["Pollution"]["Metric"] = 'Water quality'
aquatic_kelp_forests_north_atlantic_stressors["Pollution"]["Data Sources"] = ['* Monitoring', '* Research', '**Impact on Area:** Impact on Kelp growth', '**Impact on Biodiversity:**', '* Impacts to kelp and associated organisms', '**Influenced By (Stressors):**', '* Runoff, industrial discharge', '**Influences (Stressors):**', '* Kelp growth', '**Logic Description:** Water pollution can impact']
aquatic_kelp_forests_north_atlantic_stressors["Pollution"]["Impact on Area"] = 'Impact on Kelp growth'
aquatic_kelp_forests_north_atlantic_stressors["Pollution"]["Impact on Biodiversity"] = '* Impacts to kelp and associated organisms\n**Influenced By (Stressors):**\n* Runoff, industrial discharge\n**Influences (Stressors):**\n* Kelp growth\n**Logic Description:** Water pollution can impact'
aquatic_kelp_forests_north_atlantic_stressors["Pollution"]["Influenced By"] = ['* Runoff, industrial discharge', '**Influences (Stressors):**', '* Kelp growth', '**Logic Description:** Water pollution can impact']
aquatic_kelp_forests_north_atlantic_stressors["Pollution"]["Influences"] = ['* Kelp growth', '**Logic Description:** Water pollution can impact']
aquatic_kelp_forests_north_atlantic_stressors["Pollution"]["Logic Description"] = '---'
aquatic_kelp_forests_north_atlantic_stressors["Pollution"]["Impact Function"] = "impact_pollution_aquatic_kelp_forests_north_atlantic"

