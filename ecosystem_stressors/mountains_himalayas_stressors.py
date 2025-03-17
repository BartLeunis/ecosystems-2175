from stressor_templates import *
import copy

mountains_himalayas_stressors = {
    "Glacier Retreat": {},
    "Black Carbon Deposition": {},
    "Overgrazing and Collection of Medicinal Plants": {},
    "Tourism": {},
    "Climate Change": copy.deepcopy(climate_change_template),
}

# --- Glacier Retreat ---
mountains_himalayas_stressors["Glacier Retreat"]["Metric"] = 'Change in glacier area and volume; glacier mass balance; changes in meltwater runoff.'
mountains_himalayas_stressors["Glacier Retreat"]["Data Sources"] = ['Remote sensing data.', 'Field measurements (limited, but increasing).', 'Research publications (e.g., from ICIMOD - International Centre for Integrated Mountain Development).', '**Impact on Area:** *Rapid* glacier loss; changes in river flow.', '**Impact on Biodiversity:**', 'Changes in downstream water availability, impacting aquatic ecosystems *and a vast human population*.', 'Loss of habitat for glacier-dependent species.', 'Increased risk of glacial lake outburst floods (GLOFs).', '**Influenced By (Stressors):**', 'Temperature Increase.', 'Black Carbon Deposition: *Significant* in the Himalayas, accelerating melting.', 'Changes in Precipitation (in some areas).', '**Influences (Stressors):**', 'Water Resources: *Critically* important for downstream populations.', 'Hazard Risks (GLOFs): A *major* concern.', '**Logic Description:** Glacier retreat in the Himalayas is a *major* issue, driven by climate change and black carbon deposition.  This impacts water resources for a *huge* downstream population and increases the risk of glacial lake outburst floods.']
mountains_himalayas_stressors["Glacier Retreat"]["Impact on Area"] = '*Rapid* glacier loss; changes in river flow.'
mountains_himalayas_stressors["Glacier Retreat"]["Impact on Biodiversity"] = 'Changes in downstream water availability, impacting aquatic ecosystems *and a vast human population*.\nLoss of habitat for glacier-dependent species.\nIncreased risk of glacial lake outburst floods (GLOFs).\n**Influenced By (Stressors):**\nTemperature Increase.\nBlack Carbon Deposition: *Significant* in the Himalayas, accelerating melting.\nChanges in Precipitation (in some areas).\n**Influences (Stressors):**\nWater Resources: *Critically* important for downstream populations.\nHazard Risks (GLOFs): A *major* concern.\n**Logic Description:** Glacier retreat in the Himalayas is a *major* issue, driven by climate change and black carbon deposition.  This impacts water resources for a *huge* downstream population and increases the risk of glacial lake outburst floods.'
mountains_himalayas_stressors["Glacier Retreat"]["Influenced By"] = ['Temperature Increase.', 'Black Carbon Deposition: *Significant* in the Himalayas, accelerating melting.', 'Changes in Precipitation (in some areas).', '**Influences (Stressors):**', 'Water Resources: *Critically* important for downstream populations.', 'Hazard Risks (GLOFs): A *major* concern.', '**Logic Description:** Glacier retreat in the Himalayas is a *major* issue, driven by climate change and black carbon deposition.  This impacts water resources for a *huge* downstream population and increases the risk of glacial lake outburst floods.']
mountains_himalayas_stressors["Glacier Retreat"]["Influences"] = ['Water Resources: *Critically* important for downstream populations.', 'Hazard Risks (GLOFs): A *major* concern.', '**Logic Description:** Glacier retreat in the Himalayas is a *major* issue, driven by climate change and black carbon deposition.  This impacts water resources for a *huge* downstream population and increases the risk of glacial lake outburst floods.']
mountains_himalayas_stressors["Glacier Retreat"]["Logic Description"] = '---'

# --- Black Carbon Deposition ---
mountains_himalayas_stressors["Black Carbon Deposition"]["Metric"] = 'Concentration of black carbon in snow and ice; changes in albedo (reflectivity) of snow and ice.'
mountains_himalayas_stressors["Black Carbon Deposition"]["Data Sources"] = ['Field measurements (on glaciers).', 'Atmospheric monitoring.', 'Research publications.', '**Impact on Area:** Accelerates glacier melting.', '**Impact on Biodiversity:**', 'Indirect, through impacts on glacier retreat and water resources.', '**Influenced By (Stressors):**', 'Burning of Fossil Fuels: In South Asia and other regions.', 'Biomass Burning: (e.g., cooking fires, agricultural burning).', '**Influences (Stressors):**', 'Glacier Retreat: A *major* contributing factor.', '**Logic Description:** Black carbon (soot) deposition on Himalayan glaciers darkens the surface, reducing its reflectivity and accelerating melting.  This is a significant contributor to glacier retreat.']
mountains_himalayas_stressors["Black Carbon Deposition"]["Impact on Area"] = 'Accelerates glacier melting.'
mountains_himalayas_stressors["Black Carbon Deposition"]["Impact on Biodiversity"] = 'Indirect, through impacts on glacier retreat and water resources.\n**Influenced By (Stressors):**\nBurning of Fossil Fuels: In South Asia and other regions.\nBiomass Burning: (e.g., cooking fires, agricultural burning).\n**Influences (Stressors):**\nGlacier Retreat: A *major* contributing factor.\n**Logic Description:** Black carbon (soot) deposition on Himalayan glaciers darkens the surface, reducing its reflectivity and accelerating melting.  This is a significant contributor to glacier retreat.'
mountains_himalayas_stressors["Black Carbon Deposition"]["Influenced By"] = ['Burning of Fossil Fuels: In South Asia and other regions.', 'Biomass Burning: (e.g., cooking fires, agricultural burning).', '**Influences (Stressors):**', 'Glacier Retreat: A *major* contributing factor.', '**Logic Description:** Black carbon (soot) deposition on Himalayan glaciers darkens the surface, reducing its reflectivity and accelerating melting.  This is a significant contributor to glacier retreat.']
mountains_himalayas_stressors["Black Carbon Deposition"]["Influences"] = ['Glacier Retreat: A *major* contributing factor.', '**Logic Description:** Black carbon (soot) deposition on Himalayan glaciers darkens the surface, reducing its reflectivity and accelerating melting.  This is a significant contributor to glacier retreat.']
mountains_himalayas_stressors["Black Carbon Deposition"]["Logic Description"] = '---'

# --- Overgrazing and Collection of Medicinal Plants ---
mountains_himalayas_stressors["Overgrazing and Collection of Medicinal Plants"]["Metric"] = 'Livestock density; abundance of key medicinal plant species.'
mountains_himalayas_stressors["Overgrazing and Collection of Medicinal Plants"]["Data Sources"] = ['Agricultural statistics.', 'Research publications.', '**Impact on Area:** Degradation of alpine meadows; decline of medicinal plant populations.', '**Impact on Biodiversity:**', '* Loss of plant diversity.', '**Influenced By (Stressors):**', '* Population growth', '* Economic pressures', '**Influences (Stressors):**', '* Plant communities', '**Logic Description:** Overgrazing and collection pressures on plant resources.']
mountains_himalayas_stressors["Overgrazing and Collection of Medicinal Plants"]["Impact on Area"] = 'Degradation of alpine meadows; decline of medicinal plant populations.'
mountains_himalayas_stressors["Overgrazing and Collection of Medicinal Plants"]["Impact on Biodiversity"] = '* Loss of plant diversity.\n**Influenced By (Stressors):**\n* Population growth\n* Economic pressures\n**Influences (Stressors):**\n* Plant communities\n**Logic Description:** Overgrazing and collection pressures on plant resources.'
mountains_himalayas_stressors["Overgrazing and Collection of Medicinal Plants"]["Influenced By"] = ['* Population growth', '* Economic pressures', '**Influences (Stressors):**', '* Plant communities', '**Logic Description:** Overgrazing and collection pressures on plant resources.']
mountains_himalayas_stressors["Overgrazing and Collection of Medicinal Plants"]["Influences"] = ['* Plant communities', '**Logic Description:** Overgrazing and collection pressures on plant resources.']
mountains_himalayas_stressors["Overgrazing and Collection of Medicinal Plants"]["Logic Description"] = '---'

# --- Tourism ---
mountains_himalayas_stressors["Tourism"]["Metric"] = 'Number of tourists; development of tourism infrastructure.'
mountains_himalayas_stressors["Tourism"]["Data Sources"] = ['* Tourism statistics.', '**Impact on Area:** Localized impacts on vegetation and waste management.', '**Impact on Biodiversity:**', '* Disturbance to wildlife.', '**Influenced By (Stressors):**', '* Increasing popularity of trekking and mountaineering.', '**Influences (Stressors):**', '* Local environments.', '**Logic Description:** Tourism can have localized negative impacts.']
mountains_himalayas_stressors["Tourism"]["Impact on Area"] = 'Localized impacts on vegetation and waste management.'
mountains_himalayas_stressors["Tourism"]["Impact on Biodiversity"] = '* Disturbance to wildlife.\n**Influenced By (Stressors):**\n* Increasing popularity of trekking and mountaineering.\n**Influences (Stressors):**\n* Local environments.\n**Logic Description:** Tourism can have localized negative impacts.'
mountains_himalayas_stressors["Tourism"]["Influenced By"] = ['* Increasing popularity of trekking and mountaineering.', '**Influences (Stressors):**', '* Local environments.', '**Logic Description:** Tourism can have localized negative impacts.']
mountains_himalayas_stressors["Tourism"]["Influences"] = ['* Local environments.', '**Logic Description:** Tourism can have localized negative impacts.']
mountains_himalayas_stressors["Tourism"]["Logic Description"] = '---'

# --- Climate Change ---
mountains_himalayas_stressors["Climate Change"]["Metric"] = 'Changes in temp, precip, and extreme weather'
mountains_himalayas_stressors["Climate Change"]["Data Sources"] = ['* Climate models, historical records', '**Impact on Area:** Impacts on fragile ecosystems', '**Impact on Biodiversity:**', '* Shifts and stress', '**Influenced By (Stressors):**', '* Global GHG', '**Influences (Stressors):**', '* Water resources.', '**Logic Description:** Climate change.']
mountains_himalayas_stressors["Climate Change"]["Impact on Area"] = 'Impacts on fragile ecosystems'
mountains_himalayas_stressors["Climate Change"]["Impact on Biodiversity"] = '* Shifts and stress\n**Influenced By (Stressors):**\n* Global GHG\n**Influences (Stressors):**\n* Water resources.\n**Logic Description:** Climate change.'
mountains_himalayas_stressors["Climate Change"]["Influenced By"] = ['* Global GHG', '**Influences (Stressors):**', '* Water resources.', '**Logic Description:** Climate change.']
mountains_himalayas_stressors["Climate Change"]["Influences"] = ['* Water resources.', '**Logic Description:** Climate change.']
mountains_himalayas_stressors["Climate Change"]["Logic Description"] = '---'

