from stressor_templates import *
import copy

wetlands_pantanal_stressors = {
    "Land-Use Change": {},
    "Altered Hydrology": copy.deepcopy(altered_hydrology_template),
    "Pollution": copy.deepcopy(pollution_template),
    "Climate Change": copy.deepcopy(climate_change_template),
    "Wildfires": copy.deepcopy(fire_regime_template),
    "Agricultural Expansion": {},
    "Economic Growth": {},
    "Government Policies": {},
    "Infrastructure Development": copy.deepcopy(infrastructure_development_template),
    "Upstream Dam Construction": {},
    "Deforestation": copy.deepcopy(deforestation_template),
    "Water Diversion": {},
    "Mining Activities": {},
    "Agricultural Runoff": {},
    "Wildlife Health": {},
    "Temperature": {},
    "Changes in Precipitation": copy.deepcopy(climate_change_template),
    "Human Activities": {},
    "Air Quality": {},
    "Habitat Availability": {},
    "Water Quality": {},
    "Habitat Fragmentation": {},
    "Global Demand": {},
    "Water Demand": {},
    "Politics": {},
    "Energy Demand": {},
}

# --- Land-Use Change ---
wetlands_pantanal_stressors["Land-Use Change"]["Metric"] = 'Area converted to agriculture (primarily cattle ranching) and other land uses (ha/year).'
wetlands_pantanal_stressors["Land-Use Change"]["Data Sources"] = ['Remote sensing data.', 'Brazilian, Bolivian, and Paraguayan government data.', 'Research publications.', '**Impact on Area:** Loss of wetland and savanna habitat; fragmentation.', '**Impact on Biodiversity:**', 'Habitat loss and fragmentation.', 'Impacts on wildlife populations (e.g., jaguars, giant anteaters, hyacinth macaws).', 'Increased human-wildlife conflict.', '**Influenced By (Stressors):**', 'Pantanal - Agricultural Expansion', 'Pantanal - Economic Growth', 'Pantanal - Government Policies', '*  Pantanal - Infrastructure Development', '**Influences (Stressors):**', '*  Pantanal - Habitat Fragmentation', '**Logic Description:** Conversion of Pantanal habitat to cattle pasture is a growing threat, leading to habitat loss and fragmentation.']
wetlands_pantanal_stressors["Land-Use Change"]["Impact on Area"] = 'Loss of wetland and savanna habitat; fragmentation.'
wetlands_pantanal_stressors["Land-Use Change"]["Impact on Biodiversity"] = 'Habitat loss and fragmentation.\nImpacts on wildlife populations (e.g., jaguars, giant anteaters, hyacinth macaws).\nIncreased human-wildlife conflict.\n**Influenced By (Stressors):**\nPantanal - Agricultural Expansion\nPantanal - Economic Growth\nPantanal - Government Policies\n*  Pantanal - Infrastructure Development\n**Influences (Stressors):**\n*  Pantanal - Habitat Fragmentation\n**Logic Description:** Conversion of Pantanal habitat to cattle pasture is a growing threat, leading to habitat loss and fragmentation.'
wetlands_pantanal_stressors["Land-Use Change"]["Influenced By"] = ['Pantanal - Agricultural Expansion', 'Pantanal - Economic Growth', 'Pantanal - Government Policies', '*  Pantanal - Infrastructure Development', '**Influences (Stressors):**', '*  Pantanal - Habitat Fragmentation', '**Logic Description:** Conversion of Pantanal habitat to cattle pasture is a growing threat, leading to habitat loss and fragmentation.']
wetlands_pantanal_stressors["Land-Use Change"]["Influences"] = ['*  Pantanal - Habitat Fragmentation', '**Logic Description:** Conversion of Pantanal habitat to cattle pasture is a growing threat, leading to habitat loss and fragmentation.']
wetlands_pantanal_stressors["Land-Use Change"]["Logic Description"] = '---'

# --- Altered Hydrology ---
wetlands_pantanal_stressors["Altered Hydrology"]["Metric"] = 'Changes in water levels, flooding patterns, and river flow.'
wetlands_pantanal_stressors["Altered Hydrology"]["Data Sources"] = ['Hydrological monitoring data (river gauges).', 'Remote sensing data.', 'Research studies.', '**Impact on Area:** Changes in the extent and duration of flooding, affecting wetland habitats.', '**Impact on Biodiversity:**', 'Impacts on fish populations (spawning and migration).', 'Impacts on aquatic invertebrates.', 'Impacts on wading bird populations.', 'Changes in vegetation communities.', '**Influenced By (Stressors):**', 'Pantanal - Upstream Dam Construction', 'Pantanal - Climate Change', 'Pantanal - Deforestation', '*  Pantanal - Water Diversion', '**Influences (Stressors):**', '*  Pantanal - Habitat Availability', "**Logic Description:** The Pantanal's ecology is driven by its annual flood pulse. Dams, climate change, and deforestation are altering this."]
wetlands_pantanal_stressors["Altered Hydrology"]["Impact on Area"] = 'Changes in the extent and duration of flooding, affecting wetland habitats.'
wetlands_pantanal_stressors["Altered Hydrology"]["Impact on Biodiversity"] = "Impacts on fish populations (spawning and migration).\nImpacts on aquatic invertebrates.\nImpacts on wading bird populations.\nChanges in vegetation communities.\n**Influenced By (Stressors):**\nPantanal - Upstream Dam Construction\nPantanal - Climate Change\nPantanal - Deforestation\n*  Pantanal - Water Diversion\n**Influences (Stressors):**\n*  Pantanal - Habitat Availability\n**Logic Description:** The Pantanal's ecology is driven by its annual flood pulse. Dams, climate change, and deforestation are altering this."
wetlands_pantanal_stressors["Altered Hydrology"]["Influenced By"] = ['Pantanal - Upstream Dam Construction', 'Pantanal - Climate Change', 'Pantanal - Deforestation', '*  Pantanal - Water Diversion', '**Influences (Stressors):**', '*  Pantanal - Habitat Availability', "**Logic Description:** The Pantanal's ecology is driven by its annual flood pulse. Dams, climate change, and deforestation are altering this."]
wetlands_pantanal_stressors["Altered Hydrology"]["Influences"] = ['*  Pantanal - Habitat Availability', "**Logic Description:** The Pantanal's ecology is driven by its annual flood pulse. Dams, climate change, and deforestation are altering this."]
wetlands_pantanal_stressors["Altered Hydrology"]["Logic Description"] = '---'

# --- Pollution ---
wetlands_pantanal_stressors["Pollution"]["Metric"] = 'Concentrations of pollutants (e.g., mercury, pesticides, sediment) in water and sediments.'
wetlands_pantanal_stressors["Pollution"]["Data Sources"] = ['Water quality monitoring data.', 'Research studies.', '**Impact on Area:** Water quality degradation.', '**Impact on Biodiversity:**', 'Toxic effects on wildlife (e.g., mercury contamination in fish).', 'Impacts on aquatic food webs.', '**Influenced By (Stressors):**', 'Pantanal - Mining Activities', 'Pantanal - Agricultural Runoff', 'Pantanal - Deforestation', '**Influences (Stressors):**', '*  Pantanal - Water Quality', '*  Pantanal - Wildlife Health', '**Logic Description:** Pollution from mining, agriculture, and deforestation degrades water quality and impacts wildlife.']
wetlands_pantanal_stressors["Pollution"]["Impact on Area"] = 'Water quality degradation.'
wetlands_pantanal_stressors["Pollution"]["Impact on Biodiversity"] = 'Toxic effects on wildlife (e.g., mercury contamination in fish).\nImpacts on aquatic food webs.\n**Influenced By (Stressors):**\nPantanal - Mining Activities\nPantanal - Agricultural Runoff\nPantanal - Deforestation\n**Influences (Stressors):**\n*  Pantanal - Water Quality\n*  Pantanal - Wildlife Health\n**Logic Description:** Pollution from mining, agriculture, and deforestation degrades water quality and impacts wildlife.'
wetlands_pantanal_stressors["Pollution"]["Influenced By"] = ['Pantanal - Mining Activities', 'Pantanal - Agricultural Runoff', 'Pantanal - Deforestation', '**Influences (Stressors):**', '*  Pantanal - Water Quality', '*  Pantanal - Wildlife Health', '**Logic Description:** Pollution from mining, agriculture, and deforestation degrades water quality and impacts wildlife.']
wetlands_pantanal_stressors["Pollution"]["Influences"] = ['*  Pantanal - Water Quality', '*  Pantanal - Wildlife Health', '**Logic Description:** Pollution from mining, agriculture, and deforestation degrades water quality and impacts wildlife.']
wetlands_pantanal_stressors["Pollution"]["Logic Description"] = '---'

# --- Climate Change ---
wetlands_pantanal_stressors["Climate Change"]["Metric"] = 'Temperature, Precipitation, increased frequency of extreme weather events.'
wetlands_pantanal_stressors["Climate Change"]["Data Sources"] = ['* Climate models', '* Historical data', '**Impact on Area:** Indirect', '**Impact on Biodiversity:**', '* Shifts in Species', '* Increased stress.', '* Changes in phenology.', '**Influenced By (Stressors):**', '* Global GHG', '**Influences (Stressors):**', '*  Pantanal - Hydrology', '*  Pantanal - Wildfires', '**Logic Description:** Climate change impacts']
wetlands_pantanal_stressors["Climate Change"]["Impact on Area"] = 'Indirect'
wetlands_pantanal_stressors["Climate Change"]["Impact on Biodiversity"] = '* Shifts in Species\n* Increased stress.\n* Changes in phenology.\n**Influenced By (Stressors):**\n* Global GHG\n**Influences (Stressors):**\n*  Pantanal - Hydrology\n*  Pantanal - Wildfires\n**Logic Description:** Climate change impacts'
wetlands_pantanal_stressors["Climate Change"]["Influenced By"] = ['* Global GHG', '**Influences (Stressors):**', '*  Pantanal - Hydrology', '*  Pantanal - Wildfires', '**Logic Description:** Climate change impacts']
wetlands_pantanal_stressors["Climate Change"]["Influences"] = ['*  Pantanal - Hydrology', '*  Pantanal - Wildfires', '**Logic Description:** Climate change impacts']
wetlands_pantanal_stressors["Climate Change"]["Logic Description"] = '---'

# --- Wildfires ---
wetlands_pantanal_stressors["Wildfires"]["Data Sources"] = ['* Remote Sensing', '* Local Reports', '**Impact on Area:** Direct loss', '**Impact on Biodiversity:**', '* Mortality', '* Habitat loss', '**Influenced By (Stressors):**', '*  Pantanal - Deforestation', '*  Pantanal - Temperature', '*  Pantanal - Changes in Precipitation', '*  Pantanal - Human Activities', '**Influences (Stressors):**', '*  Pantanal - Air Quality', '**Logic Description:** Wildfires exacerbated by human activities and climate.']
wetlands_pantanal_stressors["Wildfires"]["Impact on Area"] = 'Direct loss'
wetlands_pantanal_stressors["Wildfires"]["Impact on Biodiversity"] = '* Mortality\n* Habitat loss\n**Influenced By (Stressors):**\n*  Pantanal - Deforestation\n*  Pantanal - Temperature\n*  Pantanal - Changes in Precipitation\n*  Pantanal - Human Activities\n**Influences (Stressors):**\n*  Pantanal - Air Quality\n**Logic Description:** Wildfires exacerbated by human activities and climate.'
wetlands_pantanal_stressors["Wildfires"]["Influenced By"] = ['*  Pantanal - Deforestation', '*  Pantanal - Temperature', '*  Pantanal - Changes in Precipitation', '*  Pantanal - Human Activities', '**Influences (Stressors):**', '*  Pantanal - Air Quality', '**Logic Description:** Wildfires exacerbated by human activities and climate.']
wetlands_pantanal_stressors["Wildfires"]["Influences"] = ['*  Pantanal - Air Quality', '**Logic Description:** Wildfires exacerbated by human activities and climate.']
wetlands_pantanal_stressors["Wildfires"]["Logic Description"] = '---'

# --- Agricultural Expansion ---
wetlands_pantanal_stressors["Agricultural Expansion"]["Metric"] = 'Area converted to agriculture'
wetlands_pantanal_stressors["Agricultural Expansion"]["Data Sources"] = ['* Remote Sensing', '* Government Data', '**Impact on Area:** Habitat Loss', '**Impact on Biodiversity**:', '* Species loss', '**Influenced By (Stressors):**', '* Global Demand', '**Influences (Stressors):**', '* Pantanal - Land-Use Change', '**Logic Description:** Demand for agricultural land.']
wetlands_pantanal_stressors["Agricultural Expansion"]["Impact on Area"] = 'Habitat Loss'
wetlands_pantanal_stressors["Agricultural Expansion"]["Influenced By"] = ['* Global Demand', '**Influences (Stressors):**', '* Pantanal - Land-Use Change', '**Logic Description:** Demand for agricultural land.']
wetlands_pantanal_stressors["Agricultural Expansion"]["Influences"] = ['* Pantanal - Land-Use Change', '**Logic Description:** Demand for agricultural land.']
wetlands_pantanal_stressors["Agricultural Expansion"]["Logic Description"] = '---'

# --- Economic Growth ---
wetlands_pantanal_stressors["Economic Growth"]["Metric"] = 'GDP, etc.'
wetlands_pantanal_stressors["Economic Growth"]["Data Sources"] = ['* Economic indicators', '**Impact on Area:** Indirect, via increased resource demand', '**Impact on Biodiversity:**', '* Habitat Loss', '**Influenced By (Stressors):**', '* Global Markets', '**Influences (Stressors):**', '* Pantanal - Land-Use Change', '* Pantanal - Agricultural Expansion', '* Pantanal - Infrastructure Development', '**Logic Description:** Economic development pressures.']
wetlands_pantanal_stressors["Economic Growth"]["Impact on Area"] = 'Indirect, via increased resource demand'
wetlands_pantanal_stressors["Economic Growth"]["Impact on Biodiversity"] = '* Habitat Loss\n**Influenced By (Stressors):**\n* Global Markets\n**Influences (Stressors):**\n* Pantanal - Land-Use Change\n* Pantanal - Agricultural Expansion\n* Pantanal - Infrastructure Development\n**Logic Description:** Economic development pressures.'
wetlands_pantanal_stressors["Economic Growth"]["Influenced By"] = ['* Global Markets', '**Influences (Stressors):**', '* Pantanal - Land-Use Change', '* Pantanal - Agricultural Expansion', '* Pantanal - Infrastructure Development', '**Logic Description:** Economic development pressures.']
wetlands_pantanal_stressors["Economic Growth"]["Influences"] = ['* Pantanal - Land-Use Change', '* Pantanal - Agricultural Expansion', '* Pantanal - Infrastructure Development', '**Logic Description:** Economic development pressures.']
wetlands_pantanal_stressors["Economic Growth"]["Logic Description"] = '---'

# --- Government Policies ---
wetlands_pantanal_stressors["Government Policies"]["Metric"] = 'Land use regulations, environmental protections'
wetlands_pantanal_stressors["Government Policies"]["Data Sources"] = ['* Policy Documents', '**Impact on Area:** Variable', '**Impact on Biodiversity:**', '* Variable', '**Influenced By (Stressors):**', '* Politics', '* Economics', '**Influences (Stressors):**', '*  Pantanal - Land-Use Change', '**Logic Description:** Policy can have positive or negative impacts.']
wetlands_pantanal_stressors["Government Policies"]["Impact on Area"] = 'Variable'
wetlands_pantanal_stressors["Government Policies"]["Impact on Biodiversity"] = '* Variable\n**Influenced By (Stressors):**\n* Politics\n* Economics\n**Influences (Stressors):**\n*  Pantanal - Land-Use Change\n**Logic Description:** Policy can have positive or negative impacts.'
wetlands_pantanal_stressors["Government Policies"]["Influenced By"] = ['* Politics', '* Economics', '**Influences (Stressors):**', '*  Pantanal - Land-Use Change', '**Logic Description:** Policy can have positive or negative impacts.']
wetlands_pantanal_stressors["Government Policies"]["Influences"] = ['*  Pantanal - Land-Use Change', '**Logic Description:** Policy can have positive or negative impacts.']
wetlands_pantanal_stressors["Government Policies"]["Logic Description"] = '---'

# --- Infrastructure Development ---
wetlands_pantanal_stressors["Infrastructure Development"]["Impact on Area"] = 'Fragmentation'
wetlands_pantanal_stressors["Infrastructure Development"]["Impact on Biodiversity"] = '* Habitat Loss\n**Influenced By (Stressors):**\n*  Pantanal - Economic Growth\n**Influences (Stressors):**\n* Pantanal - Habitat Fragmentation\n* Pantanal - Land Use Change\n**Logic Description**: Infrastructure projects can damage habitat.'
wetlands_pantanal_stressors["Infrastructure Development"]["Influenced By"] = ['*  Pantanal - Economic Growth', '**Influences (Stressors):**', '* Pantanal - Habitat Fragmentation', '* Pantanal - Land Use Change', '**Logic Description**: Infrastructure projects can damage habitat.']
wetlands_pantanal_stressors["Infrastructure Development"]["Influences"] = ['* Pantanal - Habitat Fragmentation', '* Pantanal - Land Use Change', '**Logic Description**: Infrastructure projects can damage habitat.']

# --- Upstream Dam Construction ---
wetlands_pantanal_stressors["Upstream Dam Construction"]["Metric"] = 'Number and capacity of upstream dams'
wetlands_pantanal_stressors["Upstream Dam Construction"]["Data Sources"] = ['Government records (Brazil, Bolivia, Paraguay).', 'Research publications.', '**Impact on Area:** Altered hydrology of the Pantanal.', '**Impact on Biodiversity:**', 'Changes in fish migration and spawning.', 'Impacts on other aquatic species.', 'Changes in vegetation communities.', '**Influenced By (Stressors):**', '*  Pantanal - Energy Demand', 'Government Policies (of upstream countries).', '**Influences (Stressors):**', 'Pantanal - Altered Hydrology', "**Logic Description:** Dams built on rivers that feed the Pantanal alter the natural flow regime, impacting the wetland's ecology."]
wetlands_pantanal_stressors["Upstream Dam Construction"]["Impact on Area"] = 'Altered hydrology of the Pantanal.'
wetlands_pantanal_stressors["Upstream Dam Construction"]["Impact on Biodiversity"] = "Changes in fish migration and spawning.\nImpacts on other aquatic species.\nChanges in vegetation communities.\n**Influenced By (Stressors):**\n*  Pantanal - Energy Demand\nGovernment Policies (of upstream countries).\n**Influences (Stressors):**\nPantanal - Altered Hydrology\n**Logic Description:** Dams built on rivers that feed the Pantanal alter the natural flow regime, impacting the wetland's ecology."
wetlands_pantanal_stressors["Upstream Dam Construction"]["Influenced By"] = ['*  Pantanal - Energy Demand', 'Government Policies (of upstream countries).', '**Influences (Stressors):**', 'Pantanal - Altered Hydrology', "**Logic Description:** Dams built on rivers that feed the Pantanal alter the natural flow regime, impacting the wetland's ecology."]
wetlands_pantanal_stressors["Upstream Dam Construction"]["Influences"] = ['Pantanal - Altered Hydrology', "**Logic Description:** Dams built on rivers that feed the Pantanal alter the natural flow regime, impacting the wetland's ecology."]
wetlands_pantanal_stressors["Upstream Dam Construction"]["Logic Description"] = '---'

# --- Deforestation ---
wetlands_pantanal_stressors["Deforestation"]["Metric"] = 'Area of forest cleared (ha/year).'
wetlands_pantanal_stressors["Deforestation"]["Data Sources"] = ['* Remote sensing', '* Government Data', '**Impact on Area**: Reduced forest cover.', '**Impact on Biodiversity**:', '* Habitat Loss', '* Increased soil erosion.', '**Influenced By (Stressors):**', '* Pantanal - Agricultural Expansion', '* Pantanal - Land-Use Change', '**Influences (Stressors):**', '* Pantanal - Altered Hydrology', '* Pantanal - Pollution', '* Pantanal - Wildfires', '**Logic Description:** Deforestation contributes to multiple other stressors.']
wetlands_pantanal_stressors["Deforestation"]["Influenced By"] = ['* Pantanal - Agricultural Expansion', '* Pantanal - Land-Use Change', '**Influences (Stressors):**', '* Pantanal - Altered Hydrology', '* Pantanal - Pollution', '* Pantanal - Wildfires', '**Logic Description:** Deforestation contributes to multiple other stressors.']
wetlands_pantanal_stressors["Deforestation"]["Influences"] = ['* Pantanal - Altered Hydrology', '* Pantanal - Pollution', '* Pantanal - Wildfires', '**Logic Description:** Deforestation contributes to multiple other stressors.']
wetlands_pantanal_stressors["Deforestation"]["Logic Description"] = '---'

# --- Water Diversion ---
wetlands_pantanal_stressors["Water Diversion"]["Metric"] = 'Volume of water diverted for irrigation, etc.'
wetlands_pantanal_stressors["Water Diversion"]["Data Sources"] = ['* Government Records', '* Research studies.', '**Impact on Area:** Reduced water availability in the wetland.', '**Impact on Biodiversity:**', '* Impacts on aquatic species.', '**Influenced By (Stressors):**', '* Pantanal - Agricultural Expansion', '* Pantanal - Water Demand', '**Influences (Stressors):**', '* Pantanal - Altered Hydrology', "**Logic Description:** Water extraction reduces the Pantanal's flood pulse."]
wetlands_pantanal_stressors["Water Diversion"]["Impact on Area"] = 'Reduced water availability in the wetland.'
wetlands_pantanal_stressors["Water Diversion"]["Impact on Biodiversity"] = "* Impacts on aquatic species.\n**Influenced By (Stressors):**\n* Pantanal - Agricultural Expansion\n* Pantanal - Water Demand\n**Influences (Stressors):**\n* Pantanal - Altered Hydrology\n**Logic Description:** Water extraction reduces the Pantanal's flood pulse."
wetlands_pantanal_stressors["Water Diversion"]["Influenced By"] = ['* Pantanal - Agricultural Expansion', '* Pantanal - Water Demand', '**Influences (Stressors):**', '* Pantanal - Altered Hydrology', "**Logic Description:** Water extraction reduces the Pantanal's flood pulse."]
wetlands_pantanal_stressors["Water Diversion"]["Influences"] = ['* Pantanal - Altered Hydrology', "**Logic Description:** Water extraction reduces the Pantanal's flood pulse."]
wetlands_pantanal_stressors["Water Diversion"]["Logic Description"] = '---'

# --- Mining Activities ---
wetlands_pantanal_stressors["Mining Activities"]["Metric"] = 'Number of mines, area affected, pollutant levels'
wetlands_pantanal_stressors["Mining Activities"]["Data Sources"] = ['* Government records.', '* Environmental monitoring data.', '**Impact on Area**: Water and soil contamination.', '**Impact on Biodiversity**:', '* Toxic effects on wildlife.', '**Influenced By (Stressors):**', '* Economic Growth', '**Influences (Stressors):**', '* Pantanal - Pollution', '**Logic Description:** Mining releases pollutants into the environment.']
wetlands_pantanal_stressors["Mining Activities"]["Influenced By"] = ['* Economic Growth', '**Influences (Stressors):**', '* Pantanal - Pollution', '**Logic Description:** Mining releases pollutants into the environment.']
wetlands_pantanal_stressors["Mining Activities"]["Influences"] = ['* Pantanal - Pollution', '**Logic Description:** Mining releases pollutants into the environment.']
wetlands_pantanal_stressors["Mining Activities"]["Logic Description"] = '---'

# --- Agricultural Runoff ---
wetlands_pantanal_stressors["Agricultural Runoff"]["Metric"] = 'Nutrient and pesticide concentrations in water.'
wetlands_pantanal_stressors["Agricultural Runoff"]["Data Sources"] = ['* Water quality monitoring data.', '**Impact on Area**: Water quality degradation.', '**Impact on Biodiversity:**', '* Eutrophication', '* Toxic effects', '**Influenced By (Stressors)**', '* Pantanal - Agricultural Expansion', '**Influences (Stressors)**', '* Pantanal - Pollution', '**Logic Description**: Runoff carries pollutants from agricultural areas']
wetlands_pantanal_stressors["Agricultural Runoff"]["Impact on Biodiversity"] = '* Eutrophication\n* Toxic effects\n**Influenced By (Stressors)**\n* Pantanal - Agricultural Expansion\n**Influences (Stressors)**\n* Pantanal - Pollution\n**Logic Description**: Runoff carries pollutants from agricultural areas'

# --- Wildlife Health ---
wetlands_pantanal_stressors["Wildlife Health"]["Metric"] = 'Disease prevalence, mortality rates, contaminant levels in wildlife.'
wetlands_pantanal_stressors["Wildlife Health"]["Data Sources"] = ['Wildlife monitoring data.', 'Research studies.', '**Impact on Area:** Indirect, through impacts on populations.', '**Impact on Biodiversity:**', 'Population declines.', '**Influenced By (Stressors):**', 'Pantanal - Pollution', '**Influences (Stressors):**', 'Population dynamics', '**Logic Description**: Wildlife health is an indicator of ecosystem health.']
wetlands_pantanal_stressors["Wildlife Health"]["Impact on Area"] = 'Indirect, through impacts on populations.'
wetlands_pantanal_stressors["Wildlife Health"]["Impact on Biodiversity"] = 'Population declines.\n**Influenced By (Stressors):**\nPantanal - Pollution\n**Influences (Stressors):**\nPopulation dynamics\n**Logic Description**: Wildlife health is an indicator of ecosystem health.'
wetlands_pantanal_stressors["Wildlife Health"]["Influenced By"] = ['Pantanal - Pollution', '**Influences (Stressors):**', 'Population dynamics', '**Logic Description**: Wildlife health is an indicator of ecosystem health.']
wetlands_pantanal_stressors["Wildlife Health"]["Influences"] = ['Population dynamics', '**Logic Description**: Wildlife health is an indicator of ecosystem health.']

# --- Temperature ---
wetlands_pantanal_stressors["Temperature"]["Metric"] = 'Average and extreme temperatures.'
wetlands_pantanal_stressors["Temperature"]["Data Sources"] = ['* Climate Data.', '**Impact on Area:** Indirect', '**Impact on Biodiversity:**', '* Species stress', '**Influenced By (Stressors):**', '* Pantanal - Climate Change', '**Influences (Stressors):**', '* Pantanal - Wildfires', '**Logic Description**: Temperature is a key environmental variable.']
wetlands_pantanal_stressors["Temperature"]["Impact on Area"] = 'Indirect'
wetlands_pantanal_stressors["Temperature"]["Impact on Biodiversity"] = '* Species stress\n**Influenced By (Stressors):**\n* Pantanal - Climate Change\n**Influences (Stressors):**\n* Pantanal - Wildfires\n**Logic Description**: Temperature is a key environmental variable.'
wetlands_pantanal_stressors["Temperature"]["Influenced By"] = ['* Pantanal - Climate Change', '**Influences (Stressors):**', '* Pantanal - Wildfires', '**Logic Description**: Temperature is a key environmental variable.']
wetlands_pantanal_stressors["Temperature"]["Influences"] = ['* Pantanal - Wildfires', '**Logic Description**: Temperature is a key environmental variable.']

# --- Changes in Precipitation ---
wetlands_pantanal_stressors["Changes in Precipitation"]["Metric"] = 'Rainfall amount, seasonality.'
wetlands_pantanal_stressors["Changes in Precipitation"]["Influenced By"] = ['* Pantanal - Climate Change', '**Influences (Stressors):**', '* Pantanal - Wildfires', '**Logic Description**: Rainfall patterns are critical for wetlands.']
wetlands_pantanal_stressors["Changes in Precipitation"]["Influences"] = ['* Pantanal - Wildfires', '**Logic Description**: Rainfall patterns are critical for wetlands.']

# --- Human Activities ---
wetlands_pantanal_stressors["Human Activities"]["Metric"] = 'Varies depending on the specific activity.'
wetlands_pantanal_stressors["Human Activities"]["Data Sources"] = ['Various.', '**Impact on Area:** Variable, can be direct or indirect.', '**Impact on Biodiversity:**', 'Variable.', '**Influenced By (Stressors):**', '* Many', '**Influences (Stressors):**', '* Pantanal - Wildfires', '**Logic Description:** A broad category encompassing many human impacts.']
wetlands_pantanal_stressors["Human Activities"]["Impact on Area"] = 'Variable, can be direct or indirect.'
wetlands_pantanal_stressors["Human Activities"]["Impact on Biodiversity"] = 'Variable.\n**Influenced By (Stressors):**\n* Many\n**Influences (Stressors):**\n* Pantanal - Wildfires\n**Logic Description:** A broad category encompassing many human impacts.'
wetlands_pantanal_stressors["Human Activities"]["Influenced By"] = ['* Many', '**Influences (Stressors):**', '* Pantanal - Wildfires', '**Logic Description:** A broad category encompassing many human impacts.']
wetlands_pantanal_stressors["Human Activities"]["Influences"] = ['* Pantanal - Wildfires', '**Logic Description:** A broad category encompassing many human impacts.']
wetlands_pantanal_stressors["Human Activities"]["Logic Description"] = '---'

# --- Air Quality ---
wetlands_pantanal_stressors["Air Quality"]["Data Sources"] = ['* Air quality monitoring.', '**Impact on Area:** Air Quality', '**Impact on Biodiversity:**', '* Respiratory issues in wildlife', '**Influenced By (Stressors):**', '* Pantanal - Wildfires', '**Influences (Stressors):**', '* Wildlife Health', '**Logic Description:** Air quality impacts both human and wildlife health.']
wetlands_pantanal_stressors["Air Quality"]["Impact on Area"] = 'Air Quality'
wetlands_pantanal_stressors["Air Quality"]["Impact on Biodiversity"] = '* Respiratory issues in wildlife\n**Influenced By (Stressors):**\n* Pantanal - Wildfires\n**Influences (Stressors):**\n* Wildlife Health\n**Logic Description:** Air quality impacts both human and wildlife health.'
wetlands_pantanal_stressors["Air Quality"]["Influenced By"] = ['* Pantanal - Wildfires', '**Influences (Stressors):**', '* Wildlife Health', '**Logic Description:** Air quality impacts both human and wildlife health.']
wetlands_pantanal_stressors["Air Quality"]["Influences"] = ['* Wildlife Health', '**Logic Description:** Air quality impacts both human and wildlife health.']
wetlands_pantanal_stressors["Air Quality"]["Logic Description"] = '---'

# --- Habitat Availability ---
wetlands_pantanal_stressors["Habitat Availability"]["Data Sources"] = ['* Remote Sensing', '* Species distribution models', '**Impact on Area**: N/A', '**Impact on Biodiversity:**', '*  Population sizes.', '**Influenced By (Stressors)**', '* Pantanal - Altered Hydrology', '* Many others', '**Influences (Stressors):**', '* Population dynamics.', '**Logic Description**: The amount of suitable habitat affects populations.']
wetlands_pantanal_stressors["Habitat Availability"]["Impact on Biodiversity"] = '*  Population sizes.\n**Influenced By (Stressors)**\n* Pantanal - Altered Hydrology\n* Many others\n**Influences (Stressors):**\n* Population dynamics.\n**Logic Description**: The amount of suitable habitat affects populations.'
wetlands_pantanal_stressors["Habitat Availability"]["Influences"] = ['* Population dynamics.', '**Logic Description**: The amount of suitable habitat affects populations.']

# --- Water Quality ---
wetlands_pantanal_stressors["Water Quality"]["Data Sources"] = ['* Monitoring Networks', '**Impact on Area:** Overall aquatic environment', '**Impact on Biodiversity:**', '* Impacts on many species', '**Influenced By (Stressors):**', '* Pantanal - Pollution', '**Influences (Stressors):**', '* Many, varies.', '**Logic Description**: Water quality is fundamental to wetland ecosystems.']
wetlands_pantanal_stressors["Water Quality"]["Impact on Area"] = 'Overall aquatic environment'
wetlands_pantanal_stressors["Water Quality"]["Impact on Biodiversity"] = '* Impacts on many species\n**Influenced By (Stressors):**\n* Pantanal - Pollution\n**Influences (Stressors):**\n* Many, varies.\n**Logic Description**: Water quality is fundamental to wetland ecosystems.'
wetlands_pantanal_stressors["Water Quality"]["Influenced By"] = ['* Pantanal - Pollution', '**Influences (Stressors):**', '* Many, varies.', '**Logic Description**: Water quality is fundamental to wetland ecosystems.']
wetlands_pantanal_stressors["Water Quality"]["Influences"] = ['* Many, varies.', '**Logic Description**: Water quality is fundamental to wetland ecosystems.']

# --- Habitat Fragmentation ---
wetlands_pantanal_stressors["Habitat Fragmentation"]["Metric"] = 'Patch size, connectivity.'
wetlands_pantanal_stressors["Habitat Fragmentation"]["Data Sources"] = ['* Remote Sensing', '**Impact on Area:** Isolation of habitat patches.', '**Impact on Biodiversity:**', '* Reduced gene flow, increased vulnerability.', '**Influenced By (Stressors):**', '* Pantanal - Land-Use Change', '* Pantanal - Infrastructure Development', '**Influences (Stressors):**', '* Exacerbates other stressors.', '**Logic Description**: Fragmentation reduces the viability of habitats']
wetlands_pantanal_stressors["Habitat Fragmentation"]["Impact on Area"] = 'Isolation of habitat patches.'
wetlands_pantanal_stressors["Habitat Fragmentation"]["Impact on Biodiversity"] = '* Reduced gene flow, increased vulnerability.\n**Influenced By (Stressors):**\n* Pantanal - Land-Use Change\n* Pantanal - Infrastructure Development\n**Influences (Stressors):**\n* Exacerbates other stressors.\n**Logic Description**: Fragmentation reduces the viability of habitats'
wetlands_pantanal_stressors["Habitat Fragmentation"]["Influenced By"] = ['* Pantanal - Land-Use Change', '* Pantanal - Infrastructure Development', '**Influences (Stressors):**', '* Exacerbates other stressors.', '**Logic Description**: Fragmentation reduces the viability of habitats']
wetlands_pantanal_stressors["Habitat Fragmentation"]["Influences"] = ['* Exacerbates other stressors.', '**Logic Description**: Fragmentation reduces the viability of habitats']

# --- Global Demand ---
wetlands_pantanal_stressors["Global Demand"]["Metric"] = 'Prices for agricultural commodities.'
wetlands_pantanal_stressors["Global Demand"]["Data Sources"] = ['* Economic data', '**Impact on Area:** Influences land use decisions', '**Impact on Biodiversity:**', '* Indirect, through land-use change.', '**Influenced By (Stressors):**', '* Global markets', '**Influences (Stressors):**', '* Pantanal - Agricultural Expansion', '**Logic Description:** Global markets drive local land use']
wetlands_pantanal_stressors["Global Demand"]["Impact on Area"] = 'Influences land use decisions'
wetlands_pantanal_stressors["Global Demand"]["Impact on Biodiversity"] = '* Indirect, through land-use change.\n**Influenced By (Stressors):**\n* Global markets\n**Influences (Stressors):**\n* Pantanal - Agricultural Expansion\n**Logic Description:** Global markets drive local land use'
wetlands_pantanal_stressors["Global Demand"]["Influenced By"] = ['* Global markets', '**Influences (Stressors):**', '* Pantanal - Agricultural Expansion', '**Logic Description:** Global markets drive local land use']
wetlands_pantanal_stressors["Global Demand"]["Influences"] = ['* Pantanal - Agricultural Expansion', '**Logic Description:** Global markets drive local land use']
wetlands_pantanal_stressors["Global Demand"]["Logic Description"] = '---'

# --- Water Demand ---
wetlands_pantanal_stressors["Water Demand"]["Metric"] = 'Water usage by different sectors.'
wetlands_pantanal_stressors["Water Demand"]["Data Sources"] = ['* Government Records', '**Impact on Area:** Water availability in the Pantanal.', '**Impact on Biodiversity:**', '* Impacts on aquatic species.', '**Influenced By (Stressors):**', '* Population growth', '* Economic development', '**Influences (Stressors):**', '* Pantanal - Water Diversion', '**Logic Description**: Demand for water resources.']
wetlands_pantanal_stressors["Water Demand"]["Impact on Area"] = 'Water availability in the Pantanal.'
wetlands_pantanal_stressors["Water Demand"]["Impact on Biodiversity"] = '* Impacts on aquatic species.\n**Influenced By (Stressors):**\n* Population growth\n* Economic development\n**Influences (Stressors):**\n* Pantanal - Water Diversion\n**Logic Description**: Demand for water resources.'
wetlands_pantanal_stressors["Water Demand"]["Influenced By"] = ['* Population growth', '* Economic development', '**Influences (Stressors):**', '* Pantanal - Water Diversion', '**Logic Description**: Demand for water resources.']
wetlands_pantanal_stressors["Water Demand"]["Influences"] = ['* Pantanal - Water Diversion', '**Logic Description**: Demand for water resources.']

# --- Politics ---
wetlands_pantanal_stressors["Politics"]["Data Sources"] = ['* Government Records', '* News Reports', '**Impact on Area**: Variable', '**Impact on Biodiversity**:', '* Variable', '**Influenced By (Stressors):**', '* Many', '**Influences (Stressors):**', '* Pantanal - Government Policies', '**Logic Description:** Political factors influence policy decisions.']
wetlands_pantanal_stressors["Politics"]["Influenced By"] = ['* Many', '**Influences (Stressors):**', '* Pantanal - Government Policies', '**Logic Description:** Political factors influence policy decisions.']
wetlands_pantanal_stressors["Politics"]["Influences"] = ['* Pantanal - Government Policies', '**Logic Description:** Political factors influence policy decisions.']
wetlands_pantanal_stressors["Politics"]["Logic Description"] = '---'

# --- Energy Demand ---
wetlands_pantanal_stressors["Energy Demand"]["Metric"] = 'Energy consumption and production.'
wetlands_pantanal_stressors["Energy Demand"]["Data Sources"] = ['* Government Statistics', '**Impact on Area:** Drivers for dam construction.', '**Impact on Biodiversity**:', '* Impacts related to dam construction', '**Influenced By (Stressors):**', '* Economic Growth', '**Influences (Stressors):**', '* Pantanal - Upstream Dam Construction', '**Logic Description**: Energy needs can influence infrastructure development.']
wetlands_pantanal_stressors["Energy Demand"]["Impact on Area"] = 'Drivers for dam construction.'
wetlands_pantanal_stressors["Energy Demand"]["Influenced By"] = ['* Economic Growth', '**Influences (Stressors):**', '* Pantanal - Upstream Dam Construction', '**Logic Description**: Energy needs can influence infrastructure development.']
wetlands_pantanal_stressors["Energy Demand"]["Influences"] = ['* Pantanal - Upstream Dam Construction', '**Logic Description**: Energy needs can influence infrastructure development.']

