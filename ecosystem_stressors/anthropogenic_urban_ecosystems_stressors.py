from stressor_templates import *
import copy

anthropogenic_urban_ecosystems_stressors = {
    "Habitat Loss and Fragmentation": {},
    "Urban Heat Island Effect": {},
    "Pollution": copy.deepcopy(pollution_template),
    "Altered Hydrology": copy.deepcopy(altered_hydrology_template),
    "Invasive Species": copy.deepcopy(invasive_species_template),
    "Urban Sprawl": {},
    "Population Growth": {},
    "Economic Development": {},
    "Infrastructure Development": copy.deepcopy(infrastructure_development_template),
    "Loss of Vegetation": {},
}

# --- Habitat Loss and Fragmentation ---
anthropogenic_urban_ecosystems_stressors["Habitat Loss and Fragmentation"]["Metric"] = 'Area of natural habitat converted to urban land use (ha/year); patch size and connectivity of remaining natural areas.'
anthropogenic_urban_ecosystems_stressors["Habitat Loss and Fragmentation"]["Data Sources"] = ['Remote sensing data (satellite imagery).', 'Land use/land cover maps.', 'City planning data.', '**Impact on Area:** Reduction in the amount and connectivity of natural habitat within urban areas.', '**Impact on Biodiversity:**', 'Loss of species diversity.', 'Disruption of ecological processes.', 'Increased dominance of urban-adapted species.', 'Reduced genetic diversity within remaining populations.', '**Influenced By (Stressors):**', 'Urban Ecosystems - Urban Sprawl', 'Urban Ecosystems - Population Growth', 'Urban Ecosystems - Economic Development', '* Urban Ecosystems - Infrastructure Development', '**Influences (Stressors):**', '*  Many, varies.', '**Logic Description:** Urban development directly replaces natural habitats with buildings, roads, and other infrastructure, leading to habitat loss and fragmentation.']
anthropogenic_urban_ecosystems_stressors["Habitat Loss and Fragmentation"]["Impact on Area"] = 'Reduction in the amount and connectivity of natural habitat within urban areas.'
anthropogenic_urban_ecosystems_stressors["Habitat Loss and Fragmentation"]["Impact on Biodiversity"] = 'Loss of species diversity.\nDisruption of ecological processes.\nIncreased dominance of urban-adapted species.\nReduced genetic diversity within remaining populations.\n**Influenced By (Stressors):**\nUrban Ecosystems - Urban Sprawl\nUrban Ecosystems - Population Growth\nUrban Ecosystems - Economic Development\n* Urban Ecosystems - Infrastructure Development\n**Influences (Stressors):**\n*  Many, varies.\n**Logic Description:** Urban development directly replaces natural habitats with buildings, roads, and other infrastructure, leading to habitat loss and fragmentation.'
anthropogenic_urban_ecosystems_stressors["Habitat Loss and Fragmentation"]["Influenced By"] = ['Urban Ecosystems - Urban Sprawl', 'Urban Ecosystems - Population Growth', 'Urban Ecosystems - Economic Development', '* Urban Ecosystems - Infrastructure Development', '**Influences (Stressors):**', '*  Many, varies.', '**Logic Description:** Urban development directly replaces natural habitats with buildings, roads, and other infrastructure, leading to habitat loss and fragmentation.']
anthropogenic_urban_ecosystems_stressors["Habitat Loss and Fragmentation"]["Influences"] = ['*  Many, varies.', '**Logic Description:** Urban development directly replaces natural habitats with buildings, roads, and other infrastructure, leading to habitat loss and fragmentation.']
anthropogenic_urban_ecosystems_stressors["Habitat Loss and Fragmentation"]["Logic Description"] = '---'
anthropogenic_urban_ecosystems_stressors["Habitat Loss and Fragmentation"]["Impact Function"] = "impact_habitat_loss_and_fragmentation_anthropogenic_urban_ecosystems"

# --- Urban Heat Island Effect ---
anthropogenic_urban_ecosystems_stressors["Urban Heat Island Effect"]["Metric"] = 'Temperature difference between urban areas and surrounding rural areas (°C).'
anthropogenic_urban_ecosystems_stressors["Urban Heat Island Effect"]["Data Sources"] = ['Temperature measurements (weather stations, remote sensing).', 'Climate models.', '**Impact on Area:** Increased temperatures in urban areas.', '**Impact on Biodiversity:**', 'Stress on heat-sensitive species.', 'Changes in species distributions.', 'Increased energy consumption (for cooling).', 'Impacts on human health.', '**Influenced By (Stressors):**', 'Urban Ecosystems - Loss of Vegetation', 'Urban Ecosystems - Impervious Surfaces (roads, buildings)', 'Urban Ecosystems - Anthropogenic Heat Release (from vehicles, industry, air conditioning).', '**Influences (Stressors):**', '*  Local climate', '**Logic Description:** Urban areas tend to be warmer than surrounding rural areas due to the replacement of vegetation with heat-absorbing surfaces and human activities.']
anthropogenic_urban_ecosystems_stressors["Urban Heat Island Effect"]["Impact on Area"] = 'Increased temperatures in urban areas.'
anthropogenic_urban_ecosystems_stressors["Urban Heat Island Effect"]["Impact on Biodiversity"] = 'Stress on heat-sensitive species.\nChanges in species distributions.\nIncreased energy consumption (for cooling).\nImpacts on human health.\n**Influenced By (Stressors):**\nUrban Ecosystems - Loss of Vegetation\nUrban Ecosystems - Impervious Surfaces (roads, buildings)\nUrban Ecosystems - Anthropogenic Heat Release (from vehicles, industry, air conditioning).\n**Influences (Stressors):**\n*  Local climate\n**Logic Description:** Urban areas tend to be warmer than surrounding rural areas due to the replacement of vegetation with heat-absorbing surfaces and human activities.'
anthropogenic_urban_ecosystems_stressors["Urban Heat Island Effect"]["Influenced By"] = ['Urban Ecosystems - Loss of Vegetation', 'Urban Ecosystems - Impervious Surfaces (roads, buildings)', 'Urban Ecosystems - Anthropogenic Heat Release (from vehicles, industry, air conditioning).', '**Influences (Stressors):**', '*  Local climate', '**Logic Description:** Urban areas tend to be warmer than surrounding rural areas due to the replacement of vegetation with heat-absorbing surfaces and human activities.']
anthropogenic_urban_ecosystems_stressors["Urban Heat Island Effect"]["Influences"] = ['*  Local climate', '**Logic Description:** Urban areas tend to be warmer than surrounding rural areas due to the replacement of vegetation with heat-absorbing surfaces and human activities.']
anthropogenic_urban_ecosystems_stressors["Urban Heat Island Effect"]["Logic Description"] = '---'
anthropogenic_urban_ecosystems_stressors["Urban Heat Island Effect"]["Impact Function"] = "impact_urban_heat_island_effect_anthropogenic_urban_ecosystems"

# --- Pollution ---
anthropogenic_urban_ecosystems_stressors["Pollution"]["Metric"] = 'Concentrations of pollutants (e.g., air pollutants, water pollutants, noise, light) in air, water, and soil.'
anthropogenic_urban_ecosystems_stressors["Pollution"]["Data Sources"] = ['Air and water quality monitoring data.', 'Noise level measurements.', 'Light pollution maps.', '**Impact on Area:** Degradation of air, water, and soil quality.', '**Impact on Biodiversity:**', 'Toxic effects on wildlife and plants.', 'Disruption of behavior (e.g., due to noise and light).', 'Impacts on human health.', '**Influenced By (Stressors):**', 'Urban Ecosystems - Industrial Activity', 'Urban Ecosystems - Transportation', 'Urban Ecosystems - Waste Disposal', 'Urban Ecosystems - Construction', '**Influences (Stressors):**', '*  Urban Ecosystems - Water Quality', 'Urban Ecosystems - Air Quality', '*  Urban Ecosystems - Wildlife Health', '**Logic Description:** Urban areas are sources of various pollutants that can degrade environmental quality and impact both wildlife and human health.']
anthropogenic_urban_ecosystems_stressors["Pollution"]["Impact on Area"] = 'Degradation of air, water, and soil quality.'
anthropogenic_urban_ecosystems_stressors["Pollution"]["Impact on Biodiversity"] = 'Toxic effects on wildlife and plants.\nDisruption of behavior (e.g., due to noise and light).\nImpacts on human health.\n**Influenced By (Stressors):**\nUrban Ecosystems - Industrial Activity\nUrban Ecosystems - Transportation\nUrban Ecosystems - Waste Disposal\nUrban Ecosystems - Construction\n**Influences (Stressors):**\n*  Urban Ecosystems - Water Quality\nUrban Ecosystems - Air Quality\n*  Urban Ecosystems - Wildlife Health\n**Logic Description:** Urban areas are sources of various pollutants that can degrade environmental quality and impact both wildlife and human health.'
anthropogenic_urban_ecosystems_stressors["Pollution"]["Influenced By"] = ['Urban Ecosystems - Industrial Activity', 'Urban Ecosystems - Transportation', 'Urban Ecosystems - Waste Disposal', 'Urban Ecosystems - Construction', '**Influences (Stressors):**', '*  Urban Ecosystems - Water Quality', 'Urban Ecosystems - Air Quality', '*  Urban Ecosystems - Wildlife Health', '**Logic Description:** Urban areas are sources of various pollutants that can degrade environmental quality and impact both wildlife and human health.']
anthropogenic_urban_ecosystems_stressors["Pollution"]["Influences"] = ['*  Urban Ecosystems - Water Quality', 'Urban Ecosystems - Air Quality', '*  Urban Ecosystems - Wildlife Health', '**Logic Description:** Urban areas are sources of various pollutants that can degrade environmental quality and impact both wildlife and human health.']
anthropogenic_urban_ecosystems_stressors["Pollution"]["Logic Description"] = '---'
anthropogenic_urban_ecosystems_stressors["Pollution"]["Impact Function"] = "impact_pollution_anthropogenic_urban_ecosystems"

# --- Altered Hydrology ---
anthropogenic_urban_ecosystems_stressors["Altered Hydrology"]["Metric"] = 'Impervious surface area (%); stormwater runoff volume; streamflow patterns.'
anthropogenic_urban_ecosystems_stressors["Altered Hydrology"]["Data Sources"] = ['Hydrological models.', 'Streamflow measurements.', 'Impervious surface maps.', '**Impact on Area:** Increased stormwater runoff; reduced groundwater recharge; altered streamflow.', '**Impact on Biodiversity:**', 'Erosion and sedimentation in streams.', 'Flooding.', 'Impacts on aquatic ecosystems.', '**Influenced By (Stressors):**', 'Urban Ecosystems - Impervious Surfaces', 'Urban Ecosystems - Urban Sprawl', '*  Urban Ecosystems - Stormwater Management Practices', '**Influences (Stressors):**', '* Urban Ecosystems - Water Quality', '*  Urban Ecosystems - Flooding', '**Logic Description:** Urban development increases impervious surfaces, leading to altered hydrology, increased runoff, and impacts on aquatic ecosystems.']
anthropogenic_urban_ecosystems_stressors["Altered Hydrology"]["Impact on Area"] = 'Increased stormwater runoff; reduced groundwater recharge; altered streamflow.'
anthropogenic_urban_ecosystems_stressors["Altered Hydrology"]["Impact on Biodiversity"] = 'Erosion and sedimentation in streams.\nFlooding.\nImpacts on aquatic ecosystems.\n**Influenced By (Stressors):**\nUrban Ecosystems - Impervious Surfaces\nUrban Ecosystems - Urban Sprawl\n*  Urban Ecosystems - Stormwater Management Practices\n**Influences (Stressors):**\n* Urban Ecosystems - Water Quality\n*  Urban Ecosystems - Flooding\n**Logic Description:** Urban development increases impervious surfaces, leading to altered hydrology, increased runoff, and impacts on aquatic ecosystems.'
anthropogenic_urban_ecosystems_stressors["Altered Hydrology"]["Influenced By"] = ['Urban Ecosystems - Impervious Surfaces', 'Urban Ecosystems - Urban Sprawl', '*  Urban Ecosystems - Stormwater Management Practices', '**Influences (Stressors):**', '* Urban Ecosystems - Water Quality', '*  Urban Ecosystems - Flooding', '**Logic Description:** Urban development increases impervious surfaces, leading to altered hydrology, increased runoff, and impacts on aquatic ecosystems.']
anthropogenic_urban_ecosystems_stressors["Altered Hydrology"]["Influences"] = ['* Urban Ecosystems - Water Quality', '*  Urban Ecosystems - Flooding', '**Logic Description:** Urban development increases impervious surfaces, leading to altered hydrology, increased runoff, and impacts on aquatic ecosystems.']
anthropogenic_urban_ecosystems_stressors["Altered Hydrology"]["Logic Description"] = '---'
anthropogenic_urban_ecosystems_stressors["Altered Hydrology"]["Impact Function"] = "impact_altered_hydrology_anthropogenic_urban_ecosystems"

# --- Invasive Species ---
anthropogenic_urban_ecosystems_stressors["Invasive Species"]["Metric"] = 'Abundance of key invasive species'
anthropogenic_urban_ecosystems_stressors["Invasive Species"]["Data Sources"] = ['* Field Surveys', '**Impact on Area:** Changes in species composition.', '**Impact on Biodiversity:**', '* Competition with native species', '**Influenced By (Stressors):**', '* Urban Ecosystems - Disturbance', '* Urban Ecosystems - Introduction', '**Influences (Stressors):**', '*  Native species', '**Logic Description:** Invasive species can outcompete natives.']
anthropogenic_urban_ecosystems_stressors["Invasive Species"]["Impact on Area"] = 'Changes in species composition.'
anthropogenic_urban_ecosystems_stressors["Invasive Species"]["Impact on Biodiversity"] = '* Competition with native species\n**Influenced By (Stressors):**\n* Urban Ecosystems - Disturbance\n* Urban Ecosystems - Introduction\n**Influences (Stressors):**\n*  Native species\n**Logic Description:** Invasive species can outcompete natives.'
anthropogenic_urban_ecosystems_stressors["Invasive Species"]["Influenced By"] = ['* Urban Ecosystems - Disturbance', '* Urban Ecosystems - Introduction', '**Influences (Stressors):**', '*  Native species', '**Logic Description:** Invasive species can outcompete natives.']
anthropogenic_urban_ecosystems_stressors["Invasive Species"]["Influences"] = ['*  Native species', '**Logic Description:** Invasive species can outcompete natives.']
anthropogenic_urban_ecosystems_stressors["Invasive Species"]["Logic Description"] = '---'
anthropogenic_urban_ecosystems_stressors["Invasive Species"]["Impact Function"] = "impact_invasive_species_anthropogenic_urban_ecosystems"

# --- Urban Sprawl ---
anthropogenic_urban_ecosystems_stressors["Urban Sprawl"]["Metric"] = 'Rate of urban expansion (ha/year).'
anthropogenic_urban_ecosystems_stressors["Urban Sprawl"]["Data Sources"] = ['* Remote sensing', '* City planning data', '**Impact on Area:** Loss of natural habitat at the urban fringe', '**Impact on Biodiversity:**', '* Habitat loss and fragmentation', '**Influenced By (Stressors):**', '* Population Growth', '* Economic Development.', '**Influences (Stressors):**', 'Urban Ecosystems - Habitat Loss and Fragmentation', '**Logic Description:** Urban expansion consumes natural land.']
anthropogenic_urban_ecosystems_stressors["Urban Sprawl"]["Impact on Area"] = 'Loss of natural habitat at the urban fringe'
anthropogenic_urban_ecosystems_stressors["Urban Sprawl"]["Impact on Biodiversity"] = '* Habitat loss and fragmentation\n**Influenced By (Stressors):**\n* Population Growth\n* Economic Development.\n**Influences (Stressors):**\nUrban Ecosystems - Habitat Loss and Fragmentation\n**Logic Description:** Urban expansion consumes natural land.'
anthropogenic_urban_ecosystems_stressors["Urban Sprawl"]["Influenced By"] = ['* Population Growth', '* Economic Development.', '**Influences (Stressors):**', 'Urban Ecosystems - Habitat Loss and Fragmentation', '**Logic Description:** Urban expansion consumes natural land.']
anthropogenic_urban_ecosystems_stressors["Urban Sprawl"]["Influences"] = ['Urban Ecosystems - Habitat Loss and Fragmentation', '**Logic Description:** Urban expansion consumes natural land.']
anthropogenic_urban_ecosystems_stressors["Urban Sprawl"]["Logic Description"] = '---'
anthropogenic_urban_ecosystems_stressors["Urban Sprawl"]["Impact Function"] = "impact_urban_sprawl_anthropogenic_urban_ecosystems"

# --- Population Growth ---
anthropogenic_urban_ecosystems_stressors["Population Growth"]["Data Sources"] = ['* Census', '**Impact on Area:** Increased resource demand', '**Impact on Biodiversity:**', '* Indirect effects', '**Influenced By (Stressors):**', '* Socioeconomic factors', '**Influences (Stressors):**', 'Urban Ecosystems - Habitat Loss and Fragmentation', '*  Urban Ecosystems - Urban Sprawl', '**Logic Description:** Population growth drives urban expansion']
anthropogenic_urban_ecosystems_stressors["Population Growth"]["Impact on Area"] = 'Increased resource demand'
anthropogenic_urban_ecosystems_stressors["Population Growth"]["Impact on Biodiversity"] = '* Indirect effects\n**Influenced By (Stressors):**\n* Socioeconomic factors\n**Influences (Stressors):**\nUrban Ecosystems - Habitat Loss and Fragmentation\n*  Urban Ecosystems - Urban Sprawl\n**Logic Description:** Population growth drives urban expansion'
anthropogenic_urban_ecosystems_stressors["Population Growth"]["Influenced By"] = ['* Socioeconomic factors', '**Influences (Stressors):**', 'Urban Ecosystems - Habitat Loss and Fragmentation', '*  Urban Ecosystems - Urban Sprawl', '**Logic Description:** Population growth drives urban expansion']
anthropogenic_urban_ecosystems_stressors["Population Growth"]["Influences"] = ['Urban Ecosystems - Habitat Loss and Fragmentation', '*  Urban Ecosystems - Urban Sprawl', '**Logic Description:** Population growth drives urban expansion']
anthropogenic_urban_ecosystems_stressors["Population Growth"]["Logic Description"] = '---'
anthropogenic_urban_ecosystems_stressors["Population Growth"]["Impact Function"] = "impact_population_growth_anthropogenic_urban_ecosystems"

# --- Economic Development ---
anthropogenic_urban_ecosystems_stressors["Economic Development"]["Metric"] = 'GDP, industrial output.'
anthropogenic_urban_ecosystems_stressors["Economic Development"]["Data Sources"] = ['* Economic data', '**Impact on Area:** Variable', '**Impact on Biodiversity:**', '* Variable, can be positive or negative', '**Influenced By (Stressors):**', '* Many factors', '**Influences (Stressors):**', '* Many, Varies', 'Urban Ecosystems - Habitat Loss and Fragmentation', '*  Urban Ecosystems - Urban Sprawl', '**Logic Description:** Economic activity shapes urban development.']
anthropogenic_urban_ecosystems_stressors["Economic Development"]["Impact on Area"] = 'Variable'
anthropogenic_urban_ecosystems_stressors["Economic Development"]["Impact on Biodiversity"] = '* Variable, can be positive or negative\n**Influenced By (Stressors):**\n* Many factors\n**Influences (Stressors):**\n* Many, Varies\nUrban Ecosystems - Habitat Loss and Fragmentation\n*  Urban Ecosystems - Urban Sprawl\n**Logic Description:** Economic activity shapes urban development.'
anthropogenic_urban_ecosystems_stressors["Economic Development"]["Influenced By"] = ['* Many factors', '**Influences (Stressors):**', '* Many, Varies', 'Urban Ecosystems - Habitat Loss and Fragmentation', '*  Urban Ecosystems - Urban Sprawl', '**Logic Description:** Economic activity shapes urban development.']
anthropogenic_urban_ecosystems_stressors["Economic Development"]["Influences"] = ['* Many, Varies', 'Urban Ecosystems - Habitat Loss and Fragmentation', '*  Urban Ecosystems - Urban Sprawl', '**Logic Description:** Economic activity shapes urban development.']
anthropogenic_urban_ecosystems_stressors["Economic Development"]["Logic Description"] = '---'
anthropogenic_urban_ecosystems_stressors["Economic Development"]["Impact Function"] = "impact_economic_development_anthropogenic_urban_ecosystems"

# --- Infrastructure Development ---
anthropogenic_urban_ecosystems_stressors["Infrastructure Development"]["Influenced By"] = ['*  Urban Ecosystems - Urban Sprawl', '**Influences (Stressors):**', 'Urban Ecosystems - Habitat Loss and Fragmentation', '**Logic Description:** Infrastructure is a key component of urban development.']
anthropogenic_urban_ecosystems_stressors["Infrastructure Development"]["Influences"] = ['Urban Ecosystems - Habitat Loss and Fragmentation', '**Logic Description:** Infrastructure is a key component of urban development.']
anthropogenic_urban_ecosystems_stressors["Infrastructure Development"]["Logic Description"] = '---'
anthropogenic_urban_ecosystems_stressors["Infrastructure Development"]["Impact Function"] = "impact_infrastructure_development_anthropogenic_urban_ecosystems"

# --- Loss of Vegetation ---
anthropogenic_urban_ecosystems_stressors["Loss of Vegetation"]["Impact Function"] = "impact_loss_of_vegetation_anthropogenic_urban_ecosystems"

