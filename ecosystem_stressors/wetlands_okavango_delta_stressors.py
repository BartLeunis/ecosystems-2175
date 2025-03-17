from stressor_templates import *
import copy

wetlands_okavango_delta_stressors = {
    "Water Diversion": {},
    "Climate Change": copy.deepcopy(climate_change_template),
    "Pollution": copy.deepcopy(pollution_template),
    "Overfishing": copy.deepcopy(overfishing_template),
    "Invasive Species": copy.deepcopy(invasive_species_template),
    "Upstream Water Demand": {},
    "Government Policies": {},
    "Tourism": {},
    "Agricultural Runoff": {},
    "Upstream Development": {},
    "Human Activities": {},
    "Fishing Practices": {},
    "Population Growth": {},
    "Fish Populations": {},
    "Food Web": {},
    "Native Species": {},
    "Hydrology": copy.deepcopy(altered_hydrology_template),
    "Water Quality": {},
    "Wildlife Health": {},
}

# --- Water Diversion ---
wetlands_okavango_delta_stressors["Water Diversion"]["Metric"] = 'Amount of water extracted from the Okavango River system upstream of the delta (cubic meters/year).'
wetlands_okavango_delta_stressors["Water Diversion"]["Data Sources"] = ['Government data (Botswana, Namibia, Angola).', 'International agreements (e.g., OKACOM - Permanent Okavango River Basin Water Commission).', 'Research studies.', '**Impact on Area:** Reduced inflow to the delta, potentially shrinking the flooded area.', '**Impact on Biodiversity:**', 'Impacts on fish populations.', 'Impacts on wading bird populations.', 'Changes in vegetation communities.', 'Reduced habitat availability for wildlife.', '**Influenced By (Stressors):**', 'Okavango Delta - Upstream Water Demand', 'Okavango Delta - Government Policies', '**Influences (Stressors):**', '*  Okavango Delta - Habitat Availability', '**Logic Description:** The Okavango Delta is dependent on inflows from the Okavango River. Increased water extraction upstream could significantly reduce the amount of water, impacting its size and function.']
wetlands_okavango_delta_stressors["Water Diversion"]["Impact on Area"] = 'Reduced inflow to the delta, potentially shrinking the flooded area.'
wetlands_okavango_delta_stressors["Water Diversion"]["Impact on Biodiversity"] = 'Impacts on fish populations.\nImpacts on wading bird populations.\nChanges in vegetation communities.\nReduced habitat availability for wildlife.\n**Influenced By (Stressors):**\nOkavango Delta - Upstream Water Demand\nOkavango Delta - Government Policies\n**Influences (Stressors):**\n*  Okavango Delta - Habitat Availability\n**Logic Description:** The Okavango Delta is dependent on inflows from the Okavango River. Increased water extraction upstream could significantly reduce the amount of water, impacting its size and function.'
wetlands_okavango_delta_stressors["Water Diversion"]["Influenced By"] = ['Okavango Delta - Upstream Water Demand', 'Okavango Delta - Government Policies', '**Influences (Stressors):**', '*  Okavango Delta - Habitat Availability', '**Logic Description:** The Okavango Delta is dependent on inflows from the Okavango River. Increased water extraction upstream could significantly reduce the amount of water, impacting its size and function.']
wetlands_okavango_delta_stressors["Water Diversion"]["Influences"] = ['*  Okavango Delta - Habitat Availability', '**Logic Description:** The Okavango Delta is dependent on inflows from the Okavango River. Increased water extraction upstream could significantly reduce the amount of water, impacting its size and function.']
wetlands_okavango_delta_stressors["Water Diversion"]["Logic Description"] = '---'

# --- Climate Change ---
wetlands_okavango_delta_stressors["Climate Change"]["Metric"] = 'Changes in temperature and precipitation.'
wetlands_okavango_delta_stressors["Climate Change"]["Data Sources"] = ['* Climate models', '* Historical data', '**Impact on Area**: Changes in water availability and flooding patterns.', '**Impact on Biodiversity:**', '* Increased stress on species.', '* Shifts in species distributions.', '**Influenced By (Stressors):**', '* Global greenhouse gas emissions.', '**Influences (Stressors):**', '* Okavango Delta - Hydrology (This was already present, ensuring no duplication)', '**Logic Description**:  Climate change is a significant long-term threat.']
wetlands_okavango_delta_stressors["Climate Change"]["Impact on Biodiversity"] = '* Increased stress on species.\n* Shifts in species distributions.\n**Influenced By (Stressors):**\n* Global greenhouse gas emissions.\n**Influences (Stressors):**\n* Okavango Delta - Hydrology (This was already present, ensuring no duplication)\n**Logic Description**:  Climate change is a significant long-term threat.'
wetlands_okavango_delta_stressors["Climate Change"]["Influenced By"] = ['* Global greenhouse gas emissions.', '**Influences (Stressors):**', '* Okavango Delta - Hydrology (This was already present, ensuring no duplication)', '**Logic Description**:  Climate change is a significant long-term threat.']
wetlands_okavango_delta_stressors["Climate Change"]["Influences"] = ['* Okavango Delta - Hydrology (This was already present, ensuring no duplication)', '**Logic Description**:  Climate change is a significant long-term threat.']

# --- Pollution ---
wetlands_okavango_delta_stressors["Pollution"]["Metric"] = 'Concentration of pollutants in water and sediment.'
wetlands_okavango_delta_stressors["Pollution"]["Data Sources"] = ['Water quality monitoring.', 'Research studies.', '**Impact on Area:** Water quality degradation.', '**Impact on Biodiversity:**', '* Toxic effects.', '* Impacts on food webs.', '**Influenced By (Stressors):**', 'Okavango Delta - Tourism', 'Okavango Delta - Agricultural Runoff', 'Okavango Delta - Upstream Development', '**Influences (Stressors):**', '*  Okavango Delta - Water Quality', '*  Okavango Delta - Wildlife Health', '**Logic Description:** While currently relatively pristine, the Okavango Delta is vulnerable to pollution.']
wetlands_okavango_delta_stressors["Pollution"]["Impact on Area"] = 'Water quality degradation.'
wetlands_okavango_delta_stressors["Pollution"]["Impact on Biodiversity"] = '* Toxic effects.\n* Impacts on food webs.\n**Influenced By (Stressors):**\nOkavango Delta - Tourism\nOkavango Delta - Agricultural Runoff\nOkavango Delta - Upstream Development\n**Influences (Stressors):**\n*  Okavango Delta - Water Quality\n*  Okavango Delta - Wildlife Health\n**Logic Description:** While currently relatively pristine, the Okavango Delta is vulnerable to pollution.'
wetlands_okavango_delta_stressors["Pollution"]["Influenced By"] = ['Okavango Delta - Tourism', 'Okavango Delta - Agricultural Runoff', 'Okavango Delta - Upstream Development', '**Influences (Stressors):**', '*  Okavango Delta - Water Quality', '*  Okavango Delta - Wildlife Health', '**Logic Description:** While currently relatively pristine, the Okavango Delta is vulnerable to pollution.']
wetlands_okavango_delta_stressors["Pollution"]["Influences"] = ['*  Okavango Delta - Water Quality', '*  Okavango Delta - Wildlife Health', '**Logic Description:** While currently relatively pristine, the Okavango Delta is vulnerable to pollution.']
wetlands_okavango_delta_stressors["Pollution"]["Logic Description"] = '---'

# --- Overfishing ---
wetlands_okavango_delta_stressors["Overfishing"]["Metric"] = 'Fish catches (tonnes/year); fish population sizes.'
wetlands_okavango_delta_stressors["Overfishing"]["Data Sources"] = ['* Fisheries data (where available).', 'Research studies.', '**Impact on Area:** N/A', '**Impact on Biodiversity:**', 'Decline of fish populations.', 'Impacts on the food web (e.g., on fish-eating birds and mammals).', '**Influenced By (Stressors):**', 'Okavango Delta - Population Growth', 'Okavango Delta - Fishing Practices', '**Influences (Stressors):**', '*  Okavango Delta - Fish Populations', '*  Okavango Delta - Food Web', '**Logic Description:** Overfishing can deplete fish stocks, impacting the food web.']
wetlands_okavango_delta_stressors["Overfishing"]["Impact on Area"] = 'N/A'
wetlands_okavango_delta_stressors["Overfishing"]["Impact on Biodiversity"] = 'Decline of fish populations.\nImpacts on the food web (e.g., on fish-eating birds and mammals).\n**Influenced By (Stressors):**\nOkavango Delta - Population Growth\nOkavango Delta - Fishing Practices\n**Influences (Stressors):**\n*  Okavango Delta - Fish Populations\n*  Okavango Delta - Food Web\n**Logic Description:** Overfishing can deplete fish stocks, impacting the food web.'
wetlands_okavango_delta_stressors["Overfishing"]["Influenced By"] = ['Okavango Delta - Population Growth', 'Okavango Delta - Fishing Practices', '**Influences (Stressors):**', '*  Okavango Delta - Fish Populations', '*  Okavango Delta - Food Web', '**Logic Description:** Overfishing can deplete fish stocks, impacting the food web.']
wetlands_okavango_delta_stressors["Overfishing"]["Influences"] = ['*  Okavango Delta - Fish Populations', '*  Okavango Delta - Food Web', '**Logic Description:** Overfishing can deplete fish stocks, impacting the food web.']
wetlands_okavango_delta_stressors["Overfishing"]["Logic Description"] = '---'

# --- Invasive Species ---
wetlands_okavango_delta_stressors["Invasive Species"]["Metric"] = 'Abundance/distribution of key invasive species.'
wetlands_okavango_delta_stressors["Invasive Species"]["Data Sources"] = ['* Research', '* Monitoring', '**Impact on Area:** Changes in vegetation (e.g., aquatic weeds).', '**Impact on Biodiversity:**', 'Competition with native species.', 'Alteration of habitat.', '**Influenced By (Stressors):**', '*  Okavango Delta - Human Activities', 'Okavango Delta - Climate Change', '**Influences (Stressors):**', '*  Okavango Delta - Native Species', '**Logic Description:** Invasive aquatic plants (e.g., Salvinia molesta) can clog waterways and reduce habitat quality.']
wetlands_okavango_delta_stressors["Invasive Species"]["Impact on Area"] = 'Changes in vegetation (e.g., aquatic weeds).'
wetlands_okavango_delta_stressors["Invasive Species"]["Impact on Biodiversity"] = 'Competition with native species.\nAlteration of habitat.\n**Influenced By (Stressors):**\n*  Okavango Delta - Human Activities\nOkavango Delta - Climate Change\n**Influences (Stressors):**\n*  Okavango Delta - Native Species\n**Logic Description:** Invasive aquatic plants (e.g., Salvinia molesta) can clog waterways and reduce habitat quality.'
wetlands_okavango_delta_stressors["Invasive Species"]["Influenced By"] = ['*  Okavango Delta - Human Activities', 'Okavango Delta - Climate Change', '**Influences (Stressors):**', '*  Okavango Delta - Native Species', '**Logic Description:** Invasive aquatic plants (e.g., Salvinia molesta) can clog waterways and reduce habitat quality.']
wetlands_okavango_delta_stressors["Invasive Species"]["Influences"] = ['*  Okavango Delta - Native Species', '**Logic Description:** Invasive aquatic plants (e.g., Salvinia molesta) can clog waterways and reduce habitat quality.']
wetlands_okavango_delta_stressors["Invasive Species"]["Logic Description"] = '---'

# --- Upstream Water Demand ---
wetlands_okavango_delta_stressors["Upstream Water Demand"]["Metric"] = 'Water use by sector (agriculture, urban, etc.) upstream of the delta.'
wetlands_okavango_delta_stressors["Upstream Water Demand"]["Data Sources"] = ['* Government data (Angola, Namibia).', '**Impact on Area:** Reduced inflow to the delta', '**Impact on Biodiversity:**', '* Habitat loss', '**Influenced By (Stressors):**', '* Population growth', '* Economic Development', '**Influences (Stressors):**', '* Okavango Delta - Water Diversion', '**Logic Description**: Upstream water use reduces inflow.']
wetlands_okavango_delta_stressors["Upstream Water Demand"]["Impact on Area"] = 'Reduced inflow to the delta'
wetlands_okavango_delta_stressors["Upstream Water Demand"]["Impact on Biodiversity"] = '* Habitat loss\n**Influenced By (Stressors):**\n* Population growth\n* Economic Development\n**Influences (Stressors):**\n* Okavango Delta - Water Diversion\n**Logic Description**: Upstream water use reduces inflow.'
wetlands_okavango_delta_stressors["Upstream Water Demand"]["Influenced By"] = ['* Population growth', '* Economic Development', '**Influences (Stressors):**', '* Okavango Delta - Water Diversion', '**Logic Description**: Upstream water use reduces inflow.']
wetlands_okavango_delta_stressors["Upstream Water Demand"]["Influences"] = ['* Okavango Delta - Water Diversion', '**Logic Description**: Upstream water use reduces inflow.']

# --- Government Policies ---
wetlands_okavango_delta_stressors["Government Policies"]["Data Sources"] = ['* Policy documents, legal frameworks.', '**Impact on Area**: Variable, can be positive or negative.', '**Impact on Biodiversity:**', '* Variable', '**Influenced By (Stressors):**', '* Politics', '* Economics', '* International agreements', '**Influences (Stressors):**', '* Okavango Delta - Water Diversion', '**Logic Description**: Government policy shapes resource management.']
wetlands_okavango_delta_stressors["Government Policies"]["Impact on Biodiversity"] = '* Variable\n**Influenced By (Stressors):**\n* Politics\n* Economics\n* International agreements\n**Influences (Stressors):**\n* Okavango Delta - Water Diversion\n**Logic Description**: Government policy shapes resource management.'
wetlands_okavango_delta_stressors["Government Policies"]["Influenced By"] = ['* Politics', '* Economics', '* International agreements', '**Influences (Stressors):**', '* Okavango Delta - Water Diversion', '**Logic Description**: Government policy shapes resource management.']
wetlands_okavango_delta_stressors["Government Policies"]["Influences"] = ['* Okavango Delta - Water Diversion', '**Logic Description**: Government policy shapes resource management.']

# --- Tourism ---
wetlands_okavango_delta_stressors["Tourism"]["Data Sources"] = ['* Tourism statistics', '**Impact on Area:** Localized impacts, potential for pollution and disturbance.', '**Impact on Biodiversity:**', '* Disturbance to wildlife.', '**Influenced By (Stressors):**', '* Global travel trends', '**Influences (Stressors):**', '* Okavango Delta - Pollution', '**Logic Description**: Tourism impacts.']
wetlands_okavango_delta_stressors["Tourism"]["Impact on Area"] = 'Localized impacts, potential for pollution and disturbance.'
wetlands_okavango_delta_stressors["Tourism"]["Impact on Biodiversity"] = '* Disturbance to wildlife.\n**Influenced By (Stressors):**\n* Global travel trends\n**Influences (Stressors):**\n* Okavango Delta - Pollution\n**Logic Description**: Tourism impacts.'
wetlands_okavango_delta_stressors["Tourism"]["Influenced By"] = ['* Global travel trends', '**Influences (Stressors):**', '* Okavango Delta - Pollution', '**Logic Description**: Tourism impacts.']
wetlands_okavango_delta_stressors["Tourism"]["Influences"] = ['* Okavango Delta - Pollution', '**Logic Description**: Tourism impacts.']

# --- Agricultural Runoff ---
wetlands_okavango_delta_stressors["Agricultural Runoff"]["Metric"] = 'Nutrient and pesticide concentrations in water.'
wetlands_okavango_delta_stressors["Agricultural Runoff"]["Data Sources"] = ['* Water quality monitoring data.', '**Impact on Area:** Water quality degradation.', '**Impact on Biodiversity:**', '* Potential for eutrophication and toxic effects', '**Influenced By (Stressors)**', '* Agricultural practices upstream.', '**Influences (Stressors)**', '* Okavango Delta - Pollution', '**Logic Description**: Runoff from agricultural areas.']
wetlands_okavango_delta_stressors["Agricultural Runoff"]["Impact on Area"] = 'Water quality degradation.'
wetlands_okavango_delta_stressors["Agricultural Runoff"]["Impact on Biodiversity"] = '* Potential for eutrophication and toxic effects\n**Influenced By (Stressors)**\n* Agricultural practices upstream.\n**Influences (Stressors)**\n* Okavango Delta - Pollution\n**Logic Description**: Runoff from agricultural areas.'

# --- Upstream Development ---
wetlands_okavango_delta_stressors["Upstream Development"]["Metric"] = 'Infrastructure development, economic activity in the catchment area.'
wetlands_okavango_delta_stressors["Upstream Development"]["Data Sources"] = ['* Government reports, project plans.', '**Impact on Area:** Potential for increased water use and pollution.', '**Impact on Biodiversity:**', '* Habitat loss and degradation.', '**Influenced By (Stressors):**', '* Economic growth', '* Population growth', '**Influences (Stressors):**', '* Okavango Delta - Pollution', '* Okavango Delta - Water Diversion', '**Logic Description**: Development activities upstream can affect the delta.']
wetlands_okavango_delta_stressors["Upstream Development"]["Impact on Area"] = 'Potential for increased water use and pollution.'
wetlands_okavango_delta_stressors["Upstream Development"]["Impact on Biodiversity"] = '* Habitat loss and degradation.\n**Influenced By (Stressors):**\n* Economic growth\n* Population growth\n**Influences (Stressors):**\n* Okavango Delta - Pollution\n* Okavango Delta - Water Diversion\n**Logic Description**: Development activities upstream can affect the delta.'
wetlands_okavango_delta_stressors["Upstream Development"]["Influenced By"] = ['* Economic growth', '* Population growth', '**Influences (Stressors):**', '* Okavango Delta - Pollution', '* Okavango Delta - Water Diversion', '**Logic Description**: Development activities upstream can affect the delta.']
wetlands_okavango_delta_stressors["Upstream Development"]["Influences"] = ['* Okavango Delta - Pollution', '* Okavango Delta - Water Diversion', '**Logic Description**: Development activities upstream can affect the delta.']

# --- Human Activities ---
wetlands_okavango_delta_stressors["Human Activities"]["Data Sources"] = ['* Varies', '**Impact on Area:** Varies', '**Impact on Biodiversity**:', '* Varies', '**Influenced By (Stressors):**', '* Many', '**Influences (Stressors):**', '*  Okavango Delta - Invasive Species', '**Logic Description**: General Category.']
wetlands_okavango_delta_stressors["Human Activities"]["Impact on Area"] = 'Varies'
wetlands_okavango_delta_stressors["Human Activities"]["Influenced By"] = ['* Many', '**Influences (Stressors):**', '*  Okavango Delta - Invasive Species', '**Logic Description**: General Category.']
wetlands_okavango_delta_stressors["Human Activities"]["Influences"] = ['*  Okavango Delta - Invasive Species', '**Logic Description**: General Category.']

# --- Fishing Practices ---
wetlands_okavango_delta_stressors["Fishing Practices"]["Metric"] = 'Types of fishing gear used, fishing effort.'
wetlands_okavango_delta_stressors["Fishing Practices"]["Data Sources"] = ['* Fisheries surveys, local knowledge.', '**Impact on Area:** N/A', '**Impact on Biodiversity**:', '* Impacts on fish populations and size structure.', '**Influenced By (Stressors):**', '* Local regulations, enforcement.', '**Influences (Stressors):**', '* Okavango Delta - Overfishing', '**Logic Description**: Unsustainable fishing practices can damage fish stocks.']
wetlands_okavango_delta_stressors["Fishing Practices"]["Impact on Area"] = 'N/A'
wetlands_okavango_delta_stressors["Fishing Practices"]["Influenced By"] = ['* Local regulations, enforcement.', '**Influences (Stressors):**', '* Okavango Delta - Overfishing', '**Logic Description**: Unsustainable fishing practices can damage fish stocks.']
wetlands_okavango_delta_stressors["Fishing Practices"]["Influences"] = ['* Okavango Delta - Overfishing', '**Logic Description**: Unsustainable fishing practices can damage fish stocks.']

# --- Population Growth ---
wetlands_okavango_delta_stressors["Population Growth"]["Metric"] = 'Human population size and density in and around the delta.'
wetlands_okavango_delta_stressors["Population Growth"]["Data Sources"] = ['* Census data', '**Impact on Area:** Increased pressure on resources.', '**Impact on Biodiversity**:', '* Increased demand for food and water, leading to overfishing, etc.', '**Influenced By (Stressors)**', '* Socioeconomic factors', '**Influences (Stressors):**', '* Okavango Delta - Overfishing', '**Logic Description:** Population growth increases resource use.']
wetlands_okavango_delta_stressors["Population Growth"]["Impact on Area"] = 'Increased pressure on resources.'
wetlands_okavango_delta_stressors["Population Growth"]["Influences"] = ['* Okavango Delta - Overfishing', '**Logic Description:** Population growth increases resource use.']
wetlands_okavango_delta_stressors["Population Growth"]["Logic Description"] = '---'

# --- Fish Populations ---
wetlands_okavango_delta_stressors["Fish Populations"]["Metric"] = 'Population sizes and structure of key fish species.'
wetlands_okavango_delta_stressors["Fish Populations"]["Data Sources"] = ['* Fish surveys', '**Impact on Area:** N/A', '**Impact on Biodiversity:**', '* Food web dynamics', '**Influenced By (Stressors):**', '* Okavango Delta - Overfishing', '* Okavango Delta - Fishing Practices', '**Influences (Stressors)**', '* Okavango Delta - Food Web', '**Logic Description**: Fish are a key part of the ecosystem.']
wetlands_okavango_delta_stressors["Fish Populations"]["Impact on Area"] = 'N/A'
wetlands_okavango_delta_stressors["Fish Populations"]["Impact on Biodiversity"] = '* Food web dynamics\n**Influenced By (Stressors):**\n* Okavango Delta - Overfishing\n* Okavango Delta - Fishing Practices\n**Influences (Stressors)**\n* Okavango Delta - Food Web\n**Logic Description**: Fish are a key part of the ecosystem.'
wetlands_okavango_delta_stressors["Fish Populations"]["Influenced By"] = ['* Okavango Delta - Overfishing', '* Okavango Delta - Fishing Practices', '**Influences (Stressors)**', '* Okavango Delta - Food Web', '**Logic Description**: Fish are a key part of the ecosystem.']

# --- Food Web ---
wetlands_okavango_delta_stressors["Food Web"]["Data Sources"] = ['* Research Studies.', '**Impact on Area:** N/A', '**Impact on Biodiversity:**', '* Overall ecosystem stability.', '**Influenced By (Stressors):**', '* Okavango Delta - Fish Populations', '* Many others', '**Influences (Stressors):**', '* Many, varies', '**Logic Description:** Complex interactions within the food web.']
wetlands_okavango_delta_stressors["Food Web"]["Impact on Area"] = 'N/A'
wetlands_okavango_delta_stressors["Food Web"]["Impact on Biodiversity"] = '* Overall ecosystem stability.\n**Influenced By (Stressors):**\n* Okavango Delta - Fish Populations\n* Many others\n**Influences (Stressors):**\n* Many, varies\n**Logic Description:** Complex interactions within the food web.'
wetlands_okavango_delta_stressors["Food Web"]["Influenced By"] = ['* Okavango Delta - Fish Populations', '* Many others', '**Influences (Stressors):**', '* Many, varies', '**Logic Description:** Complex interactions within the food web.']
wetlands_okavango_delta_stressors["Food Web"]["Influences"] = ['* Many, varies', '**Logic Description:** Complex interactions within the food web.']
wetlands_okavango_delta_stressors["Food Web"]["Logic Description"] = '---'

# --- Native Species ---
wetlands_okavango_delta_stressors["Native Species"]["Metric"] = 'Population sizes and distributions of native plants and animals.'
wetlands_okavango_delta_stressors["Native Species"]["Data Sources"] = ['* Species Surveys', '**Impact on Area**: Varies', '**Impact on Biodiversity:**', '* Ecosystem Function', '**Influenced By (Stressors):**', '* Okavango Delta - Invasive Species', '**Influences (Stressors)**', '* Many', '**Logic Description**: Native species health.']
wetlands_okavango_delta_stressors["Native Species"]["Impact on Biodiversity"] = '* Ecosystem Function\n**Influenced By (Stressors):**\n* Okavango Delta - Invasive Species\n**Influences (Stressors)**\n* Many\n**Logic Description**: Native species health.'
wetlands_okavango_delta_stressors["Native Species"]["Influenced By"] = ['* Okavango Delta - Invasive Species', '**Influences (Stressors)**', '* Many', '**Logic Description**: Native species health.']

# --- Hydrology ---
wetlands_okavango_delta_stressors["Hydrology"]["Metric"] = 'Water levels, flow rates, flooding patterns.'
wetlands_okavango_delta_stressors["Hydrology"]["Data Sources"] = ['* Hydrological monitoring data', '**Impact on Area:** Extent and duration of flooding, habitat availability.', '**Impact on Biodiversity:**', '* Impacts on all aquatic and wetland species.', '**Influenced By (Stressors):**', '* Okavango Delta - Water Diversion', '* Okavango Delta- Climate Change', '**Influences (Stressors)**', '* Many, varies', '**Logic Description**: Water flow is the fundamental driver of the ecosystem.']
wetlands_okavango_delta_stressors["Hydrology"]["Impact on Area"] = 'Extent and duration of flooding, habitat availability.'
wetlands_okavango_delta_stressors["Hydrology"]["Impact on Biodiversity"] = '* Impacts on all aquatic and wetland species.\n**Influenced By (Stressors):**\n* Okavango Delta - Water Diversion\n* Okavango Delta- Climate Change\n**Influences (Stressors)**\n* Many, varies\n**Logic Description**: Water flow is the fundamental driver of the ecosystem.'
wetlands_okavango_delta_stressors["Hydrology"]["Influenced By"] = ['* Okavango Delta - Water Diversion', '* Okavango Delta- Climate Change', '**Influences (Stressors)**', '* Many, varies', '**Logic Description**: Water flow is the fundamental driver of the ecosystem.']

# --- Water Quality ---
wetlands_okavango_delta_stressors["Water Quality"]["Metric"] = 'Various water quality parameters.'
wetlands_okavango_delta_stressors["Water Quality"]["Impact on Area"] = 'Overall Health'
wetlands_okavango_delta_stressors["Water Quality"]["Impact on Biodiversity"] = '* Impacts on Aquatic life\n**Influenced By (Stressors):**\n* Okavango Delta - Pollution\n**Influences (Stressors):**\n* Many, varies\n**Logic Description:** Water Quality is a critical factor.'
wetlands_okavango_delta_stressors["Water Quality"]["Influenced By"] = ['* Okavango Delta - Pollution', '**Influences (Stressors):**', '* Many, varies', '**Logic Description:** Water Quality is a critical factor.']
wetlands_okavango_delta_stressors["Water Quality"]["Influences"] = ['* Many, varies', '**Logic Description:** Water Quality is a critical factor.']
wetlands_okavango_delta_stressors["Water Quality"]["Logic Description"] = '---'

# --- Wildlife Health ---
wetlands_okavango_delta_stressors["Wildlife Health"]["Metric"] = 'Disease prevalence, mortality rates'
wetlands_okavango_delta_stressors["Wildlife Health"]["Data Sources"] = ['* Wildlife Monitoring.', '**Impact on Area**: Indirect', '**Impact on Biodiversity**:', 'Population Declines', '**Influenced By (Stressors):**', '* Okavango Delta - Pollution', '**Influences (Stressors):**', '* Population Dynamics', '**Logic Description**: Overall Health.']
wetlands_okavango_delta_stressors["Wildlife Health"]["Influenced By"] = ['* Okavango Delta - Pollution', '**Influences (Stressors):**', '* Population Dynamics', '**Logic Description**: Overall Health.']
wetlands_okavango_delta_stressors["Wildlife Health"]["Influences"] = ['* Population Dynamics', '**Logic Description**: Overall Health.']

