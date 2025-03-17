from stressor_templates import *
import copy

anthropogenic_aquaculture_stressors = {
    "Water Pollution": copy.deepcopy(pollution_template),
    "Habitat Conversion": {},
    "Disease Outbreaks": {},
    "Escaped Fish": {},
    "Introduction of Non-Native Species": {},
    "Feed Sourcing": {},
    "Genetic Impacts": {},
}

# --- Water Pollution ---
anthropogenic_aquaculture_stressors["Water Pollution"]["Metric"] = 'Concentrations of nutrients (nitrogen, phosphorus), organic matter, and other pollutants (e.g., antibiotics, pesticides, antifoulants) in effluent from aquaculture facilities.'
anthropogenic_aquaculture_stressors["Water Pollution"]["Data Sources"] = ['Water quality monitoring data from aquaculture farms (often required by regulations).', 'Government environmental agencies.', 'Research studies.', '**Impact on Area:** Degradation of water quality in surrounding water bodies.', '**Impact on Biodiversity:**', 'Eutrophication (nutrient enrichment) leading to algal blooms and oxygen depletion in receiving waters.', 'Toxic effects of pollutants on aquatic organisms.', 'Impacts on wild fish populations and other wildlife.', '**Influenced By (Stressors):**', 'Aquaculture - Feed Type and Management: The type and amount of feed used, and how uneaten feed is managed.', 'Aquaculture - Stocking Density: High stocking densities lead to more waste production.', 'Aquaculture - Waste Management Practices: (e.g., presence/absence of treatment systems).', 'Aquaculture - Water Exchange Rates: How often water is flushed from the system.', 'Aquaculture - Use of Antibiotics and Other Chemicals.', '**Influences (Stressors):**', 'Eutrophication (in receiving waters).', 'Water Quality (in surrounding ecosystems).', 'Disease Outbreaks (in wild populations - potentially).', '**Logic Description:** Aquaculture facilities can release significant amounts of pollutants into the surrounding environment, including excess nutrients (from uneaten feed and fish waste), organic matter, antibiotics, pesticides, and antifouling agents. This pollution can degrade water quality and harm aquatic life.']
anthropogenic_aquaculture_stressors["Water Pollution"]["Impact on Area"] = 'Degradation of water quality in surrounding water bodies.'
anthropogenic_aquaculture_stressors["Water Pollution"]["Impact on Biodiversity"] = 'Eutrophication (nutrient enrichment) leading to algal blooms and oxygen depletion in receiving waters.\nToxic effects of pollutants on aquatic organisms.\nImpacts on wild fish populations and other wildlife.\n**Influenced By (Stressors):**\nAquaculture - Feed Type and Management: The type and amount of feed used, and how uneaten feed is managed.\nAquaculture - Stocking Density: High stocking densities lead to more waste production.\nAquaculture - Waste Management Practices: (e.g., presence/absence of treatment systems).\nAquaculture - Water Exchange Rates: How often water is flushed from the system.\nAquaculture - Use of Antibiotics and Other Chemicals.\n**Influences (Stressors):**\nEutrophication (in receiving waters).\nWater Quality (in surrounding ecosystems).\nDisease Outbreaks (in wild populations - potentially).\n**Logic Description:** Aquaculture facilities can release significant amounts of pollutants into the surrounding environment, including excess nutrients (from uneaten feed and fish waste), organic matter, antibiotics, pesticides, and antifouling agents. This pollution can degrade water quality and harm aquatic life.'
anthropogenic_aquaculture_stressors["Water Pollution"]["Influenced By"] = ['Aquaculture - Feed Type and Management: The type and amount of feed used, and how uneaten feed is managed.', 'Aquaculture - Stocking Density: High stocking densities lead to more waste production.', 'Aquaculture - Waste Management Practices: (e.g., presence/absence of treatment systems).', 'Aquaculture - Water Exchange Rates: How often water is flushed from the system.', 'Aquaculture - Use of Antibiotics and Other Chemicals.', '**Influences (Stressors):**', 'Eutrophication (in receiving waters).', 'Water Quality (in surrounding ecosystems).', 'Disease Outbreaks (in wild populations - potentially).', '**Logic Description:** Aquaculture facilities can release significant amounts of pollutants into the surrounding environment, including excess nutrients (from uneaten feed and fish waste), organic matter, antibiotics, pesticides, and antifouling agents. This pollution can degrade water quality and harm aquatic life.']
anthropogenic_aquaculture_stressors["Water Pollution"]["Influences"] = ['Eutrophication (in receiving waters).', 'Water Quality (in surrounding ecosystems).', 'Disease Outbreaks (in wild populations - potentially).', '**Logic Description:** Aquaculture facilities can release significant amounts of pollutants into the surrounding environment, including excess nutrients (from uneaten feed and fish waste), organic matter, antibiotics, pesticides, and antifouling agents. This pollution can degrade water quality and harm aquatic life.']
anthropogenic_aquaculture_stressors["Water Pollution"]["Logic Description"] = '---'
anthropogenic_aquaculture_stressors["Water Pollution"]["Impact Function"] = "impact_water_pollution_anthropogenic_aquaculture"

# --- Habitat Conversion ---
anthropogenic_aquaculture_stressors["Habitat Conversion"]["Metric"] = 'Area of natural habitats (e.g., mangroves, seagrass beds, wetlands) converted to aquaculture ponds (ha/year).'
anthropogenic_aquaculture_stressors["Habitat Conversion"]["Data Sources"] = ['Remote sensing data.', 'Government statistics (aquaculture development).', 'Reports from environmental organizations.', '**Impact on Area:** Loss of important coastal and wetland habitats.', '**Impact on Biodiversity:**', '*Major* loss of habitat for many species (especially mangroves and other coastal wetlands).', 'Reduced nursery grounds for wild fish and shellfish.', 'Loss of coastal protection (if mangroves are removed).', 'Loss of carbon sequestration.', '**Influenced By (Stressors):**', 'Aquaculture - Demand for Aquaculture Products: (e.g., shrimp, fish).', 'Aquaculture - Economic Incentives: Profitability of aquaculture.', 'Aquaculture - Government Policies: (e.g., promotion of aquaculture development).', 'Aquaculture - Land Availability: Coastal land suitable for aquaculture.', '**Influences (Stressors):**', 'Habitat Loss (the primary impact).', 'Coastal Erosion (if mangroves are removed).', '**Logic Description:** The conversion of natural habitats, particularly mangroves, seagrass beds, and other coastal wetlands, to aquaculture ponds is a *major* environmental impact of aquaculture, leading to significant biodiversity loss and ecosystem degradation.']
anthropogenic_aquaculture_stressors["Habitat Conversion"]["Impact on Area"] = 'Loss of important coastal and wetland habitats.'
anthropogenic_aquaculture_stressors["Habitat Conversion"]["Impact on Biodiversity"] = '*Major* loss of habitat for many species (especially mangroves and other coastal wetlands).\nReduced nursery grounds for wild fish and shellfish.\nLoss of coastal protection (if mangroves are removed).\nLoss of carbon sequestration.\n**Influenced By (Stressors):**\nAquaculture - Demand for Aquaculture Products: (e.g., shrimp, fish).\nAquaculture - Economic Incentives: Profitability of aquaculture.\nAquaculture - Government Policies: (e.g., promotion of aquaculture development).\nAquaculture - Land Availability: Coastal land suitable for aquaculture.\n**Influences (Stressors):**\nHabitat Loss (the primary impact).\nCoastal Erosion (if mangroves are removed).\n**Logic Description:** The conversion of natural habitats, particularly mangroves, seagrass beds, and other coastal wetlands, to aquaculture ponds is a *major* environmental impact of aquaculture, leading to significant biodiversity loss and ecosystem degradation.'
anthropogenic_aquaculture_stressors["Habitat Conversion"]["Influenced By"] = ['Aquaculture - Demand for Aquaculture Products: (e.g., shrimp, fish).', 'Aquaculture - Economic Incentives: Profitability of aquaculture.', 'Aquaculture - Government Policies: (e.g., promotion of aquaculture development).', 'Aquaculture - Land Availability: Coastal land suitable for aquaculture.', '**Influences (Stressors):**', 'Habitat Loss (the primary impact).', 'Coastal Erosion (if mangroves are removed).', '**Logic Description:** The conversion of natural habitats, particularly mangroves, seagrass beds, and other coastal wetlands, to aquaculture ponds is a *major* environmental impact of aquaculture, leading to significant biodiversity loss and ecosystem degradation.']
anthropogenic_aquaculture_stressors["Habitat Conversion"]["Influences"] = ['Habitat Loss (the primary impact).', 'Coastal Erosion (if mangroves are removed).', '**Logic Description:** The conversion of natural habitats, particularly mangroves, seagrass beds, and other coastal wetlands, to aquaculture ponds is a *major* environmental impact of aquaculture, leading to significant biodiversity loss and ecosystem degradation.']
anthropogenic_aquaculture_stressors["Habitat Conversion"]["Logic Description"] = '---'
anthropogenic_aquaculture_stressors["Habitat Conversion"]["Impact Function"] = "impact_habitat_conversion_anthropogenic_aquaculture"

# --- Disease Outbreaks ---
anthropogenic_aquaculture_stressors["Disease Outbreaks"]["Metric"] = 'Frequency and severity of disease outbreaks in aquaculture facilities; use of antibiotics and other chemicals.'
anthropogenic_aquaculture_stressors["Disease Outbreaks"]["Data Sources"] = ['Aquaculture industry reports.', 'Veterinary records.', 'Research studies.', '**Impact on Area:** Can lead to the release of pathogens and chemicals into the environment.', '**Impact on Biodiversity:**', 'Disease outbreaks can spread from farmed fish to wild fish populations.', 'Use of antibiotics can lead to antibiotic resistance in bacteria.', 'Use of other chemicals can have toxic effects on non-target organisms.', '**Influenced By (Stressors):**', 'Aquaculture - Stocking Density: High stocking densities increase the risk of disease outbreaks.', 'Aquaculture - Water Quality: Poor water quality can stress fish and make them more susceptible to disease.', 'Aquaculture - Feed Quality: Poor quality feed can weaken fish immune systems.', 'Aquaculture - Introduction of Non-Native Species: Can introduce new diseases.', 'Aquaculture - Biosecurity Measures: (or lack thereof).', '**Influences (Stressors):**', 'Aquaculture - Water Pollution (release of antibiotics and other chemicals).', 'Wild Fish Populations: (potential for disease transmission).', '**Logic Description:** Disease outbreaks are common in aquaculture facilities due to high stocking densities and stress.  These outbreaks can lead to the use of antibiotics and other chemicals, which can have negative environmental impacts, and can potentially spread to wild fish populations.']
anthropogenic_aquaculture_stressors["Disease Outbreaks"]["Impact on Area"] = 'Can lead to the release of pathogens and chemicals into the environment.'
anthropogenic_aquaculture_stressors["Disease Outbreaks"]["Impact on Biodiversity"] = 'Disease outbreaks can spread from farmed fish to wild fish populations.\nUse of antibiotics can lead to antibiotic resistance in bacteria.\nUse of other chemicals can have toxic effects on non-target organisms.\n**Influenced By (Stressors):**\nAquaculture - Stocking Density: High stocking densities increase the risk of disease outbreaks.\nAquaculture - Water Quality: Poor water quality can stress fish and make them more susceptible to disease.\nAquaculture - Feed Quality: Poor quality feed can weaken fish immune systems.\nAquaculture - Introduction of Non-Native Species: Can introduce new diseases.\nAquaculture - Biosecurity Measures: (or lack thereof).\n**Influences (Stressors):**\nAquaculture - Water Pollution (release of antibiotics and other chemicals).\nWild Fish Populations: (potential for disease transmission).\n**Logic Description:** Disease outbreaks are common in aquaculture facilities due to high stocking densities and stress.  These outbreaks can lead to the use of antibiotics and other chemicals, which can have negative environmental impacts, and can potentially spread to wild fish populations.'
anthropogenic_aquaculture_stressors["Disease Outbreaks"]["Influenced By"] = ['Aquaculture - Stocking Density: High stocking densities increase the risk of disease outbreaks.', 'Aquaculture - Water Quality: Poor water quality can stress fish and make them more susceptible to disease.', 'Aquaculture - Feed Quality: Poor quality feed can weaken fish immune systems.', 'Aquaculture - Introduction of Non-Native Species: Can introduce new diseases.', 'Aquaculture - Biosecurity Measures: (or lack thereof).', '**Influences (Stressors):**', 'Aquaculture - Water Pollution (release of antibiotics and other chemicals).', 'Wild Fish Populations: (potential for disease transmission).', '**Logic Description:** Disease outbreaks are common in aquaculture facilities due to high stocking densities and stress.  These outbreaks can lead to the use of antibiotics and other chemicals, which can have negative environmental impacts, and can potentially spread to wild fish populations.']
anthropogenic_aquaculture_stressors["Disease Outbreaks"]["Influences"] = ['Aquaculture - Water Pollution (release of antibiotics and other chemicals).', 'Wild Fish Populations: (potential for disease transmission).', '**Logic Description:** Disease outbreaks are common in aquaculture facilities due to high stocking densities and stress.  These outbreaks can lead to the use of antibiotics and other chemicals, which can have negative environmental impacts, and can potentially spread to wild fish populations.']
anthropogenic_aquaculture_stressors["Disease Outbreaks"]["Logic Description"] = '---'
anthropogenic_aquaculture_stressors["Disease Outbreaks"]["Impact Function"] = "impact_disease_outbreaks_anthropogenic_aquaculture"

# --- Escaped Fish ---
anthropogenic_aquaculture_stressors["Escaped Fish"]["Influenced By"] = ['* Aquaculture - Management Practices', '* Storm events.', '* Infrastructure failures.', '**Influences (Stressors):**', '* Wild fish populations (genetics, competition, disease).', '**Logic Description:** Escaped farmed fish can impact wild populations.']
anthropogenic_aquaculture_stressors["Escaped Fish"]["Influences"] = ['* Wild fish populations (genetics, competition, disease).', '**Logic Description:** Escaped farmed fish can impact wild populations.']
anthropogenic_aquaculture_stressors["Escaped Fish"]["Logic Description"] = '---'
anthropogenic_aquaculture_stressors["Escaped Fish"]["Impact Function"] = "impact_escaped_fish_anthropogenic_aquaculture"

# --- Introduction of Non-Native Species ---
anthropogenic_aquaculture_stressors["Introduction of Non-Native Species"]["Impact on Area"] = 'Potential for establishment of invasive populations if species escape.'
anthropogenic_aquaculture_stressors["Introduction of Non-Native Species"]["Impact on Biodiversity"] = '* Competition with, predation on, and displacement of native species.\n**Influenced By (Stressors):**\n* Economic factors (selection of fast-growing species).\n* Lack of regulations.\n**Influences (Stressors):**\nAquaculture - Escaped Fish\n* Native species.\n**Logic Description:** The use of non-native species in aquaculture carries the risk of escapes and establishment of invasive populations.'
anthropogenic_aquaculture_stressors["Introduction of Non-Native Species"]["Influenced By"] = ['* Economic factors (selection of fast-growing species).', '* Lack of regulations.', '**Influences (Stressors):**', 'Aquaculture - Escaped Fish', '* Native species.', '**Logic Description:** The use of non-native species in aquaculture carries the risk of escapes and establishment of invasive populations.']
anthropogenic_aquaculture_stressors["Introduction of Non-Native Species"]["Influences"] = ['Aquaculture - Escaped Fish', '* Native species.', '**Logic Description:** The use of non-native species in aquaculture carries the risk of escapes and establishment of invasive populations.']
anthropogenic_aquaculture_stressors["Introduction of Non-Native Species"]["Logic Description"] = '---'
anthropogenic_aquaculture_stressors["Introduction of Non-Native Species"]["Impact Function"] = "impact_introduction_of_non_native_species_anthropogenic_aquaculture"

# --- Feed Sourcing ---
anthropogenic_aquaculture_stressors["Feed Sourcing"]["Metric"] = 'Source and sustainability of fish feed ingredients (e.g., fishmeal, soy); amount of feed used per unit of production.'
anthropogenic_aquaculture_stressors["Feed Sourcing"]["Data Sources"] = ['Aquaculture industry reports.', 'Research studies.', 'Life cycle assessments (LCAs).', '**Impact on Area:** Indirect, through impacts on wild fish populations and other ecosystems.', '**Impact on Biodiversity:**', 'Overfishing of "forage fish" (small pelagic fish used to make fishmeal and fish oil) can impact marine food webs.', 'Deforestation and habitat conversion for soy production (if soy is used in feed).', '**Influenced By (Stressors):**', 'Aquaculture - Demand for Fish Feed.', 'Aquaculture - Feed Formulation Practices.', 'Aquaculture - Availability and Cost of Sustainable Feed Ingredients.', '**Influences (Stressors):**', 'Overfishing (of forage fish).', 'Deforestation (if soy is used).', '**Logic Description:** The production of feed for aquaculture can have significant environmental impacts, particularly if it relies on unsustainable sources of fishmeal and fish oil (leading to overfishing of wild fish populations) or soy (leading to deforestation).']
anthropogenic_aquaculture_stressors["Feed Sourcing"]["Impact on Area"] = 'Indirect, through impacts on wild fish populations and other ecosystems.'
anthropogenic_aquaculture_stressors["Feed Sourcing"]["Impact on Biodiversity"] = 'Overfishing of "forage fish" (small pelagic fish used to make fishmeal and fish oil) can impact marine food webs.\nDeforestation and habitat conversion for soy production (if soy is used in feed).\n**Influenced By (Stressors):**\nAquaculture - Demand for Fish Feed.\nAquaculture - Feed Formulation Practices.\nAquaculture - Availability and Cost of Sustainable Feed Ingredients.\n**Influences (Stressors):**\nOverfishing (of forage fish).\nDeforestation (if soy is used).\n**Logic Description:** The production of feed for aquaculture can have significant environmental impacts, particularly if it relies on unsustainable sources of fishmeal and fish oil (leading to overfishing of wild fish populations) or soy (leading to deforestation).'
anthropogenic_aquaculture_stressors["Feed Sourcing"]["Influenced By"] = ['Aquaculture - Demand for Fish Feed.', 'Aquaculture - Feed Formulation Practices.', 'Aquaculture - Availability and Cost of Sustainable Feed Ingredients.', '**Influences (Stressors):**', 'Overfishing (of forage fish).', 'Deforestation (if soy is used).', '**Logic Description:** The production of feed for aquaculture can have significant environmental impacts, particularly if it relies on unsustainable sources of fishmeal and fish oil (leading to overfishing of wild fish populations) or soy (leading to deforestation).']
anthropogenic_aquaculture_stressors["Feed Sourcing"]["Influences"] = ['Overfishing (of forage fish).', 'Deforestation (if soy is used).', '**Logic Description:** The production of feed for aquaculture can have significant environmental impacts, particularly if it relies on unsustainable sources of fishmeal and fish oil (leading to overfishing of wild fish populations) or soy (leading to deforestation).']
anthropogenic_aquaculture_stressors["Feed Sourcing"]["Logic Description"] = '---'
anthropogenic_aquaculture_stressors["Feed Sourcing"]["Impact Function"] = "impact_feed_sourcing_anthropogenic_aquaculture"

# --- Genetic Impacts ---
anthropogenic_aquaculture_stressors["Genetic Impacts"]["Data Sources"] = ['* Genetic Studies', '**Impact on Area:** N/A', '**Impact on Biodiversity:**', '* Reduced genetic diversity in wild if interbreeding.', '**Influenced By (Stressors):**', '*  Aquaculture - Escaped Fish', '* Breeding Programs.', '**Influences (Stressors):**', '* Wild Fish populations.', '**Logic Description:** The genetics of farmed fish can impact wild populations if escapes and interbreeding occur.']
anthropogenic_aquaculture_stressors["Genetic Impacts"]["Impact on Area"] = 'N/A'
anthropogenic_aquaculture_stressors["Genetic Impacts"]["Impact on Biodiversity"] = '* Reduced genetic diversity in wild if interbreeding.\n**Influenced By (Stressors):**\n*  Aquaculture - Escaped Fish\n* Breeding Programs.\n**Influences (Stressors):**\n* Wild Fish populations.\n**Logic Description:** The genetics of farmed fish can impact wild populations if escapes and interbreeding occur.'
anthropogenic_aquaculture_stressors["Genetic Impacts"]["Influenced By"] = ['*  Aquaculture - Escaped Fish', '* Breeding Programs.', '**Influences (Stressors):**', '* Wild Fish populations.', '**Logic Description:** The genetics of farmed fish can impact wild populations if escapes and interbreeding occur.']
anthropogenic_aquaculture_stressors["Genetic Impacts"]["Influences"] = ['* Wild Fish populations.', '**Logic Description:** The genetics of farmed fish can impact wild populations if escapes and interbreeding occur.']
anthropogenic_aquaculture_stressors["Genetic Impacts"]["Logic Description"] = '---'
anthropogenic_aquaculture_stressors["Genetic Impacts"]["Impact Function"] = "impact_genetic_impacts_anthropogenic_aquaculture"

