from stressor_templates import *
import copy

anthropogenic_intensive_croplands_stressors = {
    "Soil Degradation": {},
    "Water Pollution": copy.deepcopy(pollution_template),
    "Pesticide Use": {},
    "Habitat Loss": {},
    "Genetic Homogeneity": {},
    "Climate Change": copy.deepcopy(climate_change_template),
    "Water Use": {},
    "Energy Use": {},
    "Soil Erosion": {},
    "Agricultural Expansion": {},
    "Intensive Tillage": {},
    "Monoculture Cropping": {},
    "Overuse of Fertilizers and Pesticides": {},
    "Removal of Crop Residues": {},
    "Lack of Cover Crops": {},
    "Irrigation Practices": {},
    "Pest and Disease Outbreaks": {},
    "Soil Contamination": {},
    "Loss of Soil Fertility": {},
    "Farming Practices": {},
}

# --- Soil Degradation ---
anthropogenic_intensive_croplands_stressors["Soil Degradation"]["Metric"] = 'Soil organic matter content (%); soil erosion rate (tonnes/ha/year); nutrient depletion; soil compaction.'
anthropogenic_intensive_croplands_stressors["Soil Degradation"]["Data Sources"] = ['Soil surveys (e.g., USDA Natural Resources Conservation Service (NRCS) in the US, national soil surveys in other countries).', 'Research publications.', 'Remote sensing data (can be used to assess erosion and vegetation cover).', '**Impact on Area:** Reduced soil fertility and productivity; potential for land abandonment.', '**Impact on Biodiversity:**', 'Loss of soil biodiversity (microorganisms, invertebrates).', 'Reduced habitat quality for species that utilize cropland edges or adjacent habitats.', 'Indirect impacts on biodiversity in nearby ecosystems (e.g., through runoff).', '**Influenced By (Stressors):**', 'Intensive Croplands - Intensive Tillage: Frequent and deep tillage disrupts soil structure and increases erosion.', 'Intensive Croplands - Monoculture Cropping: Growing the same crop repeatedly depletes specific nutrients and reduces soil biodiversity.', 'Intensive Croplands - Overuse of Fertilizers and Pesticides: Can harm soil organisms and lead to nutrient imbalances.', 'Intensive Croplands - Removal of Crop Residues: Reduces organic matter input.', 'Intensive Croplands - Lack of Cover Crops: Leaves soil exposed to erosion.', '**Influences (Stressors):**', 'Intensive Croplands - Water Pollution (through runoff).', 'Intensive Croplands - Soil Erosion.', 'Intensive Croplands - Loss of Soil Fertility', '**Logic Description:** Intensive agricultural practices, such as frequent tillage, monoculture cropping, and overuse of fertilizers and pesticides, can lead to soil degradation, reducing soil fertility, increasing erosion, and harming soil biodiversity.']
anthropogenic_intensive_croplands_stressors["Soil Degradation"]["Impact on Area"] = 'Reduced soil fertility and productivity; potential for land abandonment.'
anthropogenic_intensive_croplands_stressors["Soil Degradation"]["Impact on Biodiversity"] = 'Loss of soil biodiversity (microorganisms, invertebrates).\nReduced habitat quality for species that utilize cropland edges or adjacent habitats.\nIndirect impacts on biodiversity in nearby ecosystems (e.g., through runoff).\n**Influenced By (Stressors):**\nIntensive Croplands - Intensive Tillage: Frequent and deep tillage disrupts soil structure and increases erosion.\nIntensive Croplands - Monoculture Cropping: Growing the same crop repeatedly depletes specific nutrients and reduces soil biodiversity.\nIntensive Croplands - Overuse of Fertilizers and Pesticides: Can harm soil organisms and lead to nutrient imbalances.\nIntensive Croplands - Removal of Crop Residues: Reduces organic matter input.\nIntensive Croplands - Lack of Cover Crops: Leaves soil exposed to erosion.\n**Influences (Stressors):**\nIntensive Croplands - Water Pollution (through runoff).\nIntensive Croplands - Soil Erosion.\nIntensive Croplands - Loss of Soil Fertility\n**Logic Description:** Intensive agricultural practices, such as frequent tillage, monoculture cropping, and overuse of fertilizers and pesticides, can lead to soil degradation, reducing soil fertility, increasing erosion, and harming soil biodiversity.'
anthropogenic_intensive_croplands_stressors["Soil Degradation"]["Influenced By"] = ['Intensive Croplands - Intensive Tillage: Frequent and deep tillage disrupts soil structure and increases erosion.', 'Intensive Croplands - Monoculture Cropping: Growing the same crop repeatedly depletes specific nutrients and reduces soil biodiversity.', 'Intensive Croplands - Overuse of Fertilizers and Pesticides: Can harm soil organisms and lead to nutrient imbalances.', 'Intensive Croplands - Removal of Crop Residues: Reduces organic matter input.', 'Intensive Croplands - Lack of Cover Crops: Leaves soil exposed to erosion.', '**Influences (Stressors):**', 'Intensive Croplands - Water Pollution (through runoff).', 'Intensive Croplands - Soil Erosion.', 'Intensive Croplands - Loss of Soil Fertility', '**Logic Description:** Intensive agricultural practices, such as frequent tillage, monoculture cropping, and overuse of fertilizers and pesticides, can lead to soil degradation, reducing soil fertility, increasing erosion, and harming soil biodiversity.']
anthropogenic_intensive_croplands_stressors["Soil Degradation"]["Influences"] = ['Intensive Croplands - Water Pollution (through runoff).', 'Intensive Croplands - Soil Erosion.', 'Intensive Croplands - Loss of Soil Fertility', '**Logic Description:** Intensive agricultural practices, such as frequent tillage, monoculture cropping, and overuse of fertilizers and pesticides, can lead to soil degradation, reducing soil fertility, increasing erosion, and harming soil biodiversity.']
anthropogenic_intensive_croplands_stressors["Soil Degradation"]["Logic Description"] = '---'
anthropogenic_intensive_croplands_stressors["Soil Degradation"]["Impact Function"] = "impact_soil_degradation_anthropogenic_intensive_croplands"

# --- Water Pollution ---
anthropogenic_intensive_croplands_stressors["Water Pollution"]["Metric"] = 'Concentrations of nutrients (nitrogen, phosphorus), pesticides, and sediments in water bodies adjacent to or downstream from croplands.'
anthropogenic_intensive_croplands_stressors["Water Pollution"]["Data Sources"] = ['Water quality monitoring programs (government agencies, research institutions).', 'Research publications.', '**Impact on Area:** Contamination of surface water and groundwater.', '**Impact on Biodiversity:**', 'Eutrophication of aquatic ecosystems (leading to algal blooms and oxygen depletion).', 'Toxic effects of pesticides on aquatic organisms.', 'Impacts on human health (through drinking water contamination).', '**Influenced By (Stressors):**', 'Intensive Croplands - Agricultural Runoff: The primary source of pollution from croplands.', 'Intensive Croplands - Overuse of Fertilizers and Pesticides.', 'Intensive Croplands - Soil Erosion: Carries sediment and attached pollutants into waterways.', 'Intensive Croplands - Irrigation Practices (can increase runoff).', '**Influences (Stressors):**', 'Aquatic Ecosystems - Eutrophication.', 'Aquatic Ecosystems - Pollution.', 'Human Health (through water contamination).', '**Logic Description:** Agricultural runoff from croplands carries excess nutrients (from fertilizers), pesticides, and sediment into waterways, causing water pollution and harming aquatic ecosystems.']
anthropogenic_intensive_croplands_stressors["Water Pollution"]["Impact on Area"] = 'Contamination of surface water and groundwater.'
anthropogenic_intensive_croplands_stressors["Water Pollution"]["Impact on Biodiversity"] = 'Eutrophication of aquatic ecosystems (leading to algal blooms and oxygen depletion).\nToxic effects of pesticides on aquatic organisms.\nImpacts on human health (through drinking water contamination).\n**Influenced By (Stressors):**\nIntensive Croplands - Agricultural Runoff: The primary source of pollution from croplands.\nIntensive Croplands - Overuse of Fertilizers and Pesticides.\nIntensive Croplands - Soil Erosion: Carries sediment and attached pollutants into waterways.\nIntensive Croplands - Irrigation Practices (can increase runoff).\n**Influences (Stressors):**\nAquatic Ecosystems - Eutrophication.\nAquatic Ecosystems - Pollution.\nHuman Health (through water contamination).\n**Logic Description:** Agricultural runoff from croplands carries excess nutrients (from fertilizers), pesticides, and sediment into waterways, causing water pollution and harming aquatic ecosystems.'
anthropogenic_intensive_croplands_stressors["Water Pollution"]["Influenced By"] = ['Intensive Croplands - Agricultural Runoff: The primary source of pollution from croplands.', 'Intensive Croplands - Overuse of Fertilizers and Pesticides.', 'Intensive Croplands - Soil Erosion: Carries sediment and attached pollutants into waterways.', 'Intensive Croplands - Irrigation Practices (can increase runoff).', '**Influences (Stressors):**', 'Aquatic Ecosystems - Eutrophication.', 'Aquatic Ecosystems - Pollution.', 'Human Health (through water contamination).', '**Logic Description:** Agricultural runoff from croplands carries excess nutrients (from fertilizers), pesticides, and sediment into waterways, causing water pollution and harming aquatic ecosystems.']
anthropogenic_intensive_croplands_stressors["Water Pollution"]["Influences"] = ['Aquatic Ecosystems - Eutrophication.', 'Aquatic Ecosystems - Pollution.', 'Human Health (through water contamination).', '**Logic Description:** Agricultural runoff from croplands carries excess nutrients (from fertilizers), pesticides, and sediment into waterways, causing water pollution and harming aquatic ecosystems.']
anthropogenic_intensive_croplands_stressors["Water Pollution"]["Logic Description"] = '---'
anthropogenic_intensive_croplands_stressors["Water Pollution"]["Impact Function"] = "impact_water_pollution_anthropogenic_intensive_croplands"

# --- Pesticide Use ---
anthropogenic_intensive_croplands_stressors["Pesticide Use"]["Metric"] = 'Amount and type of pesticides applied (kg/ha/year); concentrations of pesticides in soil, water, and biota.'
anthropogenic_intensive_croplands_stressors["Pesticide Use"]["Data Sources"] = ['Agricultural statistics (pesticide sales and use data).', 'Environmental monitoring programs.', 'Research publications.', '**Impact on Area:** Contamination of soil and water.', '**Impact on Biodiversity:**', 'Non-target effects: Pesticides can harm beneficial insects (pollinators, natural enemies of pests), birds, mammals, and aquatic organisms.', 'Development of pesticide resistance in pest populations.', 'Disruption of food webs.', '**Influenced By (Stressors):**', 'Intensive Croplands - Pest Management Practices: Reliance on chemical pesticides.', 'Intensive Croplands - Monoculture Cropping: Can increase pest pressure.', 'Intensive Croplands - Government Regulations: (or lack thereof).', '**Influences (Stressors):**', 'Intensive Croplands - Water Pollution.', 'Intensive Croplands - Soil Contamination.', 'Non-Target Species Mortality.', 'Pollinator Decline.', '**Logic Description:** Intensive pesticide use in croplands can have significant negative impacts on biodiversity, including non-target species like pollinators and beneficial insects.']
anthropogenic_intensive_croplands_stressors["Pesticide Use"]["Impact on Area"] = 'Contamination of soil and water.'
anthropogenic_intensive_croplands_stressors["Pesticide Use"]["Impact on Biodiversity"] = 'Non-target effects: Pesticides can harm beneficial insects (pollinators, natural enemies of pests), birds, mammals, and aquatic organisms.\nDevelopment of pesticide resistance in pest populations.\nDisruption of food webs.\n**Influenced By (Stressors):**\nIntensive Croplands - Pest Management Practices: Reliance on chemical pesticides.\nIntensive Croplands - Monoculture Cropping: Can increase pest pressure.\nIntensive Croplands - Government Regulations: (or lack thereof).\n**Influences (Stressors):**\nIntensive Croplands - Water Pollution.\nIntensive Croplands - Soil Contamination.\nNon-Target Species Mortality.\nPollinator Decline.\n**Logic Description:** Intensive pesticide use in croplands can have significant negative impacts on biodiversity, including non-target species like pollinators and beneficial insects.'
anthropogenic_intensive_croplands_stressors["Pesticide Use"]["Influenced By"] = ['Intensive Croplands - Pest Management Practices: Reliance on chemical pesticides.', 'Intensive Croplands - Monoculture Cropping: Can increase pest pressure.', 'Intensive Croplands - Government Regulations: (or lack thereof).', '**Influences (Stressors):**', 'Intensive Croplands - Water Pollution.', 'Intensive Croplands - Soil Contamination.', 'Non-Target Species Mortality.', 'Pollinator Decline.', '**Logic Description:** Intensive pesticide use in croplands can have significant negative impacts on biodiversity, including non-target species like pollinators and beneficial insects.']
anthropogenic_intensive_croplands_stressors["Pesticide Use"]["Influences"] = ['Intensive Croplands - Water Pollution.', 'Intensive Croplands - Soil Contamination.', 'Non-Target Species Mortality.', 'Pollinator Decline.', '**Logic Description:** Intensive pesticide use in croplands can have significant negative impacts on biodiversity, including non-target species like pollinators and beneficial insects.']
anthropogenic_intensive_croplands_stressors["Pesticide Use"]["Logic Description"] = '---'
anthropogenic_intensive_croplands_stressors["Pesticide Use"]["Impact Function"] = "impact_pesticide_use_anthropogenic_intensive_croplands"

# --- Habitat Loss ---
anthropogenic_intensive_croplands_stressors["Habitat Loss"]["Impact on Area"] = 'Reduction in natural habitat.'
anthropogenic_intensive_croplands_stressors["Habitat Loss"]["Impact on Biodiversity"] = '* Loss of species that depend on natural habitats\n**Influenced By (Stressors):**\n*  Intensive Croplands - Agricultural Expansion\n**Influences (Stressors):**\n* Biodiversity loss.\n**Logic Description:** The conversion of natural habitats to croplands.'
anthropogenic_intensive_croplands_stressors["Habitat Loss"]["Influenced By"] = ['*  Intensive Croplands - Agricultural Expansion', '**Influences (Stressors):**', '* Biodiversity loss.', '**Logic Description:** The conversion of natural habitats to croplands.']
anthropogenic_intensive_croplands_stressors["Habitat Loss"]["Influences"] = ['* Biodiversity loss.', '**Logic Description:** The conversion of natural habitats to croplands.']
anthropogenic_intensive_croplands_stressors["Habitat Loss"]["Logic Description"] = '---'
anthropogenic_intensive_croplands_stressors["Habitat Loss"]["Impact Function"] = "impact_habitat_loss_anthropogenic_intensive_croplands"

# --- Genetic Homogeneity ---
anthropogenic_intensive_croplands_stressors["Genetic Homogeneity"]["Data Sources"] = ['* Agricultural statistics', '* Research', '**Impact on Area:** Increased vulnerability to pests and diseases.', '**Impact on Biodiversity:**', 'Loss of crop diversity, making agriculture more vulnerable.', '**Influenced By (Stressors):**', '* Agricultural practices.', '**Influences (Stressors):**', '*  Intensive Croplands - Pest and Disease Outbreaks', '**Logic Description:**  The widespread planting of genetically uniform crops reduces resilience.']
anthropogenic_intensive_croplands_stressors["Genetic Homogeneity"]["Impact on Area"] = 'Increased vulnerability to pests and diseases.'
anthropogenic_intensive_croplands_stressors["Genetic Homogeneity"]["Impact on Biodiversity"] = 'Loss of crop diversity, making agriculture more vulnerable.\n**Influenced By (Stressors):**\n* Agricultural practices.\n**Influences (Stressors):**\n*  Intensive Croplands - Pest and Disease Outbreaks\n**Logic Description:**  The widespread planting of genetically uniform crops reduces resilience.'
anthropogenic_intensive_croplands_stressors["Genetic Homogeneity"]["Influenced By"] = ['* Agricultural practices.', '**Influences (Stressors):**', '*  Intensive Croplands - Pest and Disease Outbreaks', '**Logic Description:**  The widespread planting of genetically uniform crops reduces resilience.']
anthropogenic_intensive_croplands_stressors["Genetic Homogeneity"]["Influences"] = ['*  Intensive Croplands - Pest and Disease Outbreaks', '**Logic Description:**  The widespread planting of genetically uniform crops reduces resilience.']
anthropogenic_intensive_croplands_stressors["Genetic Homogeneity"]["Logic Description"] = '---'
anthropogenic_intensive_croplands_stressors["Genetic Homogeneity"]["Impact Function"] = "impact_genetic_homogeneity_anthropogenic_intensive_croplands"

# --- Climate Change ---
anthropogenic_intensive_croplands_stressors["Climate Change"]["Data Sources"] = ['* Climate models and projections', '**Impact on Area:** Changes growing conditions.', '**Impact on Biodiversity:**', 'May exacerbate other stressors.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', '* Many, varies by location.', '**Logic Description:** Climate change will affect growing conditions and water availability.']
anthropogenic_intensive_croplands_stressors["Climate Change"]["Impact on Area"] = 'Changes growing conditions.'
anthropogenic_intensive_croplands_stressors["Climate Change"]["Impact on Biodiversity"] = 'May exacerbate other stressors.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\n**Influences (Stressors):**\n* Many, varies by location.\n**Logic Description:** Climate change will affect growing conditions and water availability.'
anthropogenic_intensive_croplands_stressors["Climate Change"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', '* Many, varies by location.', '**Logic Description:** Climate change will affect growing conditions and water availability.']
anthropogenic_intensive_croplands_stressors["Climate Change"]["Influences"] = ['* Many, varies by location.', '**Logic Description:** Climate change will affect growing conditions and water availability.']
anthropogenic_intensive_croplands_stressors["Climate Change"]["Logic Description"] = '---'
anthropogenic_intensive_croplands_stressors["Climate Change"]["Impact Function"] = "impact_climate_change_anthropogenic_intensive_croplands"

# --- Water Use ---
anthropogenic_intensive_croplands_stressors["Water Use"]["Data Sources"] = ['* Water usage records', '* Government agencies', '**Impact on Area:** Water resource depletion', '**Impact on Biodiversity:**', '* Impacts on aquatic ecosystems (reduced instream flows)', '**Influenced By (Stressors):**', '* Intensive Croplands - Irrigation Practices', '**Influences (Stressors):**', '*  Water availability', '**Logic Description:** Irrigation can deplete water resources.']
anthropogenic_intensive_croplands_stressors["Water Use"]["Impact on Area"] = 'Water resource depletion'
anthropogenic_intensive_croplands_stressors["Water Use"]["Impact on Biodiversity"] = '* Impacts on aquatic ecosystems (reduced instream flows)\n**Influenced By (Stressors):**\n* Intensive Croplands - Irrigation Practices\n**Influences (Stressors):**\n*  Water availability\n**Logic Description:** Irrigation can deplete water resources.'
anthropogenic_intensive_croplands_stressors["Water Use"]["Influenced By"] = ['* Intensive Croplands - Irrigation Practices', '**Influences (Stressors):**', '*  Water availability', '**Logic Description:** Irrigation can deplete water resources.']
anthropogenic_intensive_croplands_stressors["Water Use"]["Influences"] = ['*  Water availability', '**Logic Description:** Irrigation can deplete water resources.']
anthropogenic_intensive_croplands_stressors["Water Use"]["Logic Description"] = '---'
anthropogenic_intensive_croplands_stressors["Water Use"]["Impact Function"] = "impact_water_use_anthropogenic_intensive_croplands"

# --- Energy Use ---
anthropogenic_intensive_croplands_stressors["Energy Use"]["Influences"] = ['* Climate Change', '**Logic Description**: Energy use, particularly from fossil fuels, contributes to climate change.']
anthropogenic_intensive_croplands_stressors["Energy Use"]["Impact Function"] = "impact_energy_use_anthropogenic_intensive_croplands"

# --- Soil Erosion ---
anthropogenic_intensive_croplands_stressors["Soil Erosion"]["Metric"] = 'Soil loss rate (tonnes/ha/year).'
anthropogenic_intensive_croplands_stressors["Soil Erosion"]["Data Sources"] = ['* Field measurements.', '* Models (e.g., Universal Soil Loss Equation - USLE).', '**Impact on Area:** Loss of topsoil, reduced soil fertility.', '**Impact on Biodiversity:**', '* Impacts on soil organisms.', '**Influenced By (Stressors):**', '*  Intensive Croplands - Intensive Tillage', '* Lack of cover crops', '**Influences (Stressors):**', '* Intensive Croplands - Soil Degradation', '**Logic Description:** Soil erosion removes topsoil, reducing fertility.']
anthropogenic_intensive_croplands_stressors["Soil Erosion"]["Impact on Area"] = 'Loss of topsoil, reduced soil fertility.'
anthropogenic_intensive_croplands_stressors["Soil Erosion"]["Impact on Biodiversity"] = '* Impacts on soil organisms.\n**Influenced By (Stressors):**\n*  Intensive Croplands - Intensive Tillage\n* Lack of cover crops\n**Influences (Stressors):**\n* Intensive Croplands - Soil Degradation\n**Logic Description:** Soil erosion removes topsoil, reducing fertility.'
anthropogenic_intensive_croplands_stressors["Soil Erosion"]["Influenced By"] = ['*  Intensive Croplands - Intensive Tillage', '* Lack of cover crops', '**Influences (Stressors):**', '* Intensive Croplands - Soil Degradation', '**Logic Description:** Soil erosion removes topsoil, reducing fertility.']
anthropogenic_intensive_croplands_stressors["Soil Erosion"]["Influences"] = ['* Intensive Croplands - Soil Degradation', '**Logic Description:** Soil erosion removes topsoil, reducing fertility.']
anthropogenic_intensive_croplands_stressors["Soil Erosion"]["Logic Description"] = '---'
anthropogenic_intensive_croplands_stressors["Soil Erosion"]["Impact Function"] = "impact_soil_erosion_anthropogenic_intensive_croplands"

# --- Agricultural Expansion ---
anthropogenic_intensive_croplands_stressors["Agricultural Expansion"]["Data Sources"] = ['* Remote Sensing', '* Land Use data', '**Impact on Area:** Loss of natural habitats.', '**Impact on Biodiversity:**', '* Habitat Loss', '**Influenced By (Stressors)**', '* Global demand for food.', '* Economic factors.', '**Influences (Stressors):**', '* Many', '**Logic Description:** Expansion of agricultural land is a major driver of habitat loss.']
anthropogenic_intensive_croplands_stressors["Agricultural Expansion"]["Impact on Area"] = 'Loss of natural habitats.'
anthropogenic_intensive_croplands_stressors["Agricultural Expansion"]["Impact on Biodiversity"] = '* Habitat Loss\n**Influenced By (Stressors)**\n* Global demand for food.\n* Economic factors.\n**Influences (Stressors):**\n* Many\n**Logic Description:** Expansion of agricultural land is a major driver of habitat loss.'
anthropogenic_intensive_croplands_stressors["Agricultural Expansion"]["Influences"] = ['* Many', '**Logic Description:** Expansion of agricultural land is a major driver of habitat loss.']
anthropogenic_intensive_croplands_stressors["Agricultural Expansion"]["Logic Description"] = '---'
anthropogenic_intensive_croplands_stressors["Agricultural Expansion"]["Impact Function"] = "impact_agricultural_expansion_anthropogenic_intensive_croplands"

# --- Intensive Tillage ---
anthropogenic_intensive_croplands_stressors["Intensive Tillage"]["Metric"] = 'Frequency and depth of tillage operations.'
anthropogenic_intensive_croplands_stressors["Intensive Tillage"]["Data Sources"] = ['* Agricultural surveys', '* Research Studies', '**Impact on Area:** Soil Structure degradation', '**Impact on Biodiversity:**', '* Loss of soil biota', '**Influenced By (Stressors)**:', '*  Intensive Croplands - Farming Practices', '**Influences (Stressors)**', '* Intensive Croplands - Soil Degradation', '* Intensive Croplands - Soil Erosion', '**Logic Description**: Tillage practices impact soil health.']
anthropogenic_intensive_croplands_stressors["Intensive Tillage"]["Impact on Area"] = 'Soil Structure degradation'
anthropogenic_intensive_croplands_stressors["Intensive Tillage"]["Impact on Biodiversity"] = '* Loss of soil biota\n**Influenced By (Stressors)**:\n*  Intensive Croplands - Farming Practices\n**Influences (Stressors)**\n* Intensive Croplands - Soil Degradation\n* Intensive Croplands - Soil Erosion\n**Logic Description**: Tillage practices impact soil health.'
anthropogenic_intensive_croplands_stressors["Intensive Tillage"]["Impact Function"] = "impact_intensive_tillage_anthropogenic_intensive_croplands"

# --- Monoculture Cropping ---
anthropogenic_intensive_croplands_stressors["Monoculture Cropping"]["Influenced By"] = ['* Economic factors.', '**Influences (Stressors):**', '*  Intensive Croplands - Soil Degradation', '*  Intensive Croplands - Pest and Disease Outbreaks', '*  Intensive Croplands - Pesticide Use', '**Logic Description:** Lack of crop diversity increases vulnerability.']
anthropogenic_intensive_croplands_stressors["Monoculture Cropping"]["Influences"] = ['*  Intensive Croplands - Soil Degradation', '*  Intensive Croplands - Pest and Disease Outbreaks', '*  Intensive Croplands - Pesticide Use', '**Logic Description:** Lack of crop diversity increases vulnerability.']
anthropogenic_intensive_croplands_stressors["Monoculture Cropping"]["Logic Description"] = '---'
anthropogenic_intensive_croplands_stressors["Monoculture Cropping"]["Impact Function"] = "impact_monoculture_cropping_anthropogenic_intensive_croplands"

# --- Overuse of Fertilizers and Pesticides ---
anthropogenic_intensive_croplands_stressors["Overuse of Fertilizers and Pesticides"]["Metric"] = 'Application rates of fertilizers and pesticides.'
anthropogenic_intensive_croplands_stressors["Overuse of Fertilizers and Pesticides"]["Data Sources"] = ['* Agricultural statistics.', '**Impact on Area:** Soil and water contamination', '**Impact on Biodiversity**:', '* Negative impacts on non-target species.', '**Influenced By (Stressors):**', '* Intensive Croplands - Monoculture Cropping', '**Influences (Stressors):**', '* Intensive Croplands - Water Pollution', '*  Intensive Croplands - Soil Degradation', '**Logic Description:** Excessive use can harm the environment.']
anthropogenic_intensive_croplands_stressors["Overuse of Fertilizers and Pesticides"]["Impact on Area"] = 'Soil and water contamination'
anthropogenic_intensive_croplands_stressors["Overuse of Fertilizers and Pesticides"]["Influenced By"] = ['* Intensive Croplands - Monoculture Cropping', '**Influences (Stressors):**', '* Intensive Croplands - Water Pollution', '*  Intensive Croplands - Soil Degradation', '**Logic Description:** Excessive use can harm the environment.']
anthropogenic_intensive_croplands_stressors["Overuse of Fertilizers and Pesticides"]["Influences"] = ['* Intensive Croplands - Water Pollution', '*  Intensive Croplands - Soil Degradation', '**Logic Description:** Excessive use can harm the environment.']
anthropogenic_intensive_croplands_stressors["Overuse of Fertilizers and Pesticides"]["Logic Description"] = '---'
anthropogenic_intensive_croplands_stressors["Overuse of Fertilizers and Pesticides"]["Impact Function"] = "impact_overuse_of_fertilizers_and_pesticides_anthropogenic_intensive_croplands"

# --- Removal of Crop Residues ---
anthropogenic_intensive_croplands_stressors["Removal of Crop Residues"]["Data Sources"] = ['* Agricultural surveys', '* Research', '**Impact on Area**: Reduced soil organic matter', '**Impact on Biodiversity**:', '* Impacts soil organisms', '**Influenced By (Stressors):**', '* Intensive Croplands - Farming Practices', '**Influences (Stressors):**', '*  Intensive Croplands - Soil Degradation', '**Logic Description**: Crop residue management affects soil health.']
anthropogenic_intensive_croplands_stressors["Removal of Crop Residues"]["Influenced By"] = ['* Intensive Croplands - Farming Practices', '**Influences (Stressors):**', '*  Intensive Croplands - Soil Degradation', '**Logic Description**: Crop residue management affects soil health.']
anthropogenic_intensive_croplands_stressors["Removal of Crop Residues"]["Influences"] = ['*  Intensive Croplands - Soil Degradation', '**Logic Description**: Crop residue management affects soil health.']
anthropogenic_intensive_croplands_stressors["Removal of Crop Residues"]["Impact Function"] = "impact_removal_of_crop_residues_anthropogenic_intensive_croplands"

# --- Lack of Cover Crops ---
anthropogenic_intensive_croplands_stressors["Lack of Cover Crops"]["Data Sources"] = ['* Agricultural surveys', '* Remote sensing', '**Impact on Area**: Increased soil erosion, nutrient loss.', '**Impact on Biodiversity:**', '* Reduced soil biodiversity.', '**Influenced By (Stressors):**', '* Intensive Croplands - Farming Practices', '**Influences (Stressors):**', '*  Intensive Croplands - Soil Degradation', '* Intensive Croplands - Soil Erosion', '**Logic Description**: Cover crops help protect and improve soil.']
anthropogenic_intensive_croplands_stressors["Lack of Cover Crops"]["Impact on Biodiversity"] = '* Reduced soil biodiversity.\n**Influenced By (Stressors):**\n* Intensive Croplands - Farming Practices\n**Influences (Stressors):**\n*  Intensive Croplands - Soil Degradation\n* Intensive Croplands - Soil Erosion\n**Logic Description**: Cover crops help protect and improve soil.'
anthropogenic_intensive_croplands_stressors["Lack of Cover Crops"]["Influenced By"] = ['* Intensive Croplands - Farming Practices', '**Influences (Stressors):**', '*  Intensive Croplands - Soil Degradation', '* Intensive Croplands - Soil Erosion', '**Logic Description**: Cover crops help protect and improve soil.']
anthropogenic_intensive_croplands_stressors["Lack of Cover Crops"]["Influences"] = ['*  Intensive Croplands - Soil Degradation', '* Intensive Croplands - Soil Erosion', '**Logic Description**: Cover crops help protect and improve soil.']
anthropogenic_intensive_croplands_stressors["Lack of Cover Crops"]["Impact Function"] = "impact_lack_of_cover_crops_anthropogenic_intensive_croplands"

# --- Irrigation Practices ---
anthropogenic_intensive_croplands_stressors["Irrigation Practices"]["Influenced By"] = ['* Water availability', '* Climate', '**Influences (Stressors):**', '*  Intensive Croplands - Water Pollution', '**Logic Description**: Irrigation methods influence water use and pollution.']
anthropogenic_intensive_croplands_stressors["Irrigation Practices"]["Influences"] = ['*  Intensive Croplands - Water Pollution', '**Logic Description**: Irrigation methods influence water use and pollution.']
anthropogenic_intensive_croplands_stressors["Irrigation Practices"]["Impact Function"] = "impact_irrigation_practices_anthropogenic_intensive_croplands"

# --- Pest and Disease Outbreaks ---
anthropogenic_intensive_croplands_stressors["Pest and Disease Outbreaks"]["Data Sources"] = ['* Agricultural monitoring programs.', '**Impact on Area**: Crop losses', '**Impact on Biodiversity**:', '*  Can lead to increased pesticide use.', '**Influenced By (Stressors):**', '* Intensive Croplands - Genetic Homogeneity', '* Intensive Croplands - Monoculture Cropping', '* Climate Change', '**Influences (Stressors):**', '* Intensive Croplands - Pesticide Use', '**Logic Description:** Monocultures are vulnerable to outbreaks.']
anthropogenic_intensive_croplands_stressors["Pest and Disease Outbreaks"]["Influenced By"] = ['* Intensive Croplands - Genetic Homogeneity', '* Intensive Croplands - Monoculture Cropping', '* Climate Change', '**Influences (Stressors):**', '* Intensive Croplands - Pesticide Use', '**Logic Description:** Monocultures are vulnerable to outbreaks.']
anthropogenic_intensive_croplands_stressors["Pest and Disease Outbreaks"]["Influences"] = ['* Intensive Croplands - Pesticide Use', '**Logic Description:** Monocultures are vulnerable to outbreaks.']
anthropogenic_intensive_croplands_stressors["Pest and Disease Outbreaks"]["Logic Description"] = '---'
anthropogenic_intensive_croplands_stressors["Pest and Disease Outbreaks"]["Impact Function"] = "impact_pest_and_disease_outbreaks_anthropogenic_intensive_croplands"

# --- Soil Contamination ---
anthropogenic_intensive_croplands_stressors["Soil Contamination"]["Data Sources"] = ['* Soil Testing', '**Impact on Area**: Soil health degradation', '**Impact on Biodiversity:**', '* Toxic effects', '**Influenced By (Stressors)**', '* Intensive Croplands - Overuse of Fertilizers and Pesticides', '**Influences (Stressors):**', '* Intensive Croplands - Soil Degradation', '**Logic Description**: Soil contamination with pollutants.']
anthropogenic_intensive_croplands_stressors["Soil Contamination"]["Impact on Biodiversity"] = '* Toxic effects\n**Influenced By (Stressors)**\n* Intensive Croplands - Overuse of Fertilizers and Pesticides\n**Influences (Stressors):**\n* Intensive Croplands - Soil Degradation\n**Logic Description**: Soil contamination with pollutants.'
anthropogenic_intensive_croplands_stressors["Soil Contamination"]["Influences"] = ['* Intensive Croplands - Soil Degradation', '**Logic Description**: Soil contamination with pollutants.']
anthropogenic_intensive_croplands_stressors["Soil Contamination"]["Impact Function"] = "impact_soil_contamination_anthropogenic_intensive_croplands"

# --- Loss of Soil Fertility ---
anthropogenic_intensive_croplands_stressors["Loss of Soil Fertility"]["Data Sources"] = ['* Soil testing', '**Impact on Area**: Reduced crop yields', '**Impact on Biodiversity:**', '* Impacts on soil organisms', '**Influenced By (Stressors)**', '* Intensive Croplands - Soil Degradation', '**Influences (Stressors):**', '* Crop yields', '**Logic Description:** Soil degradation reduces fertility.']
anthropogenic_intensive_croplands_stressors["Loss of Soil Fertility"]["Impact on Biodiversity"] = '* Impacts on soil organisms\n**Influenced By (Stressors)**\n* Intensive Croplands - Soil Degradation\n**Influences (Stressors):**\n* Crop yields\n**Logic Description:** Soil degradation reduces fertility.'
anthropogenic_intensive_croplands_stressors["Loss of Soil Fertility"]["Influences"] = ['* Crop yields', '**Logic Description:** Soil degradation reduces fertility.']
anthropogenic_intensive_croplands_stressors["Loss of Soil Fertility"]["Logic Description"] = '---'
anthropogenic_intensive_croplands_stressors["Loss of Soil Fertility"]["Impact Function"] = "impact_loss_of_soil_fertility_anthropogenic_intensive_croplands"

# --- Farming Practices ---
anthropogenic_intensive_croplands_stressors["Farming Practices"]["Data Sources"] = ['* Agricultural surveys', '* Research', '**Impact on Area**: Variable, can have positive or negative impacts', '**Impact on Biodiversity**:', '* Variable', '**Influenced By (Stressors)**', '* Economics, knowledge', '**Influences (Stressors):**', '* Many', '* Variable', '**Logic Description:** A broad category encompassing management decisions.']
anthropogenic_intensive_croplands_stressors["Farming Practices"]["Influences"] = ['* Many', '* Variable', '**Logic Description:** A broad category encompassing management decisions.']
anthropogenic_intensive_croplands_stressors["Farming Practices"]["Logic Description"] = '---'
anthropogenic_intensive_croplands_stressors["Farming Practices"]["Impact Function"] = "impact_farming_practices_anthropogenic_intensive_croplands"

