from stressor_templates import *
import copy

aquatic_kelp_forests_australian_stressors = {
    "Ocean Warming": {},
    "Overgrazing": {},
    "Invasive Species": copy.deepcopy(invasive_species_template),
}

# --- Ocean Warming ---
aquatic_kelp_forests_australian_stressors["Ocean Warming"]["Metric"] = 'Sea surface temperature (SST) (°C); frequency and severity of marine heatwaves.'
aquatic_kelp_forests_australian_stressors["Ocean Warming"]["Data Sources"] = ['Australian Bureau of Meteorology (BOM) data.', 'Integrated Marine Observing System (IMOS).', 'Research publications (e.g., from CSIRO, universities).', '**Impact on Area:** *Major* kelp forest declines and die-offs, particularly in Western Australia and Tasmania.', '**Impact on Biodiversity:**', 'Loss of habitat.', 'Shifts in community structure (towards more warm-tolerant species and *turf algae*).', 'Range contractions of kelp species.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', 'Strengthening of the East Australian Current (EAC): Bringing warmer waters further south.', '**Influences (Stressors):**', '* Range shifts', '**Logic Description:** Ocean warming, particularly marine heatwaves, has caused *severe* and widespread kelp forest declines in parts of Australia, leading to significant ecosystem shifts. This is a major area of concern and research.']
aquatic_kelp_forests_australian_stressors["Ocean Warming"]["Impact on Area"] = '*Major* kelp forest declines and die-offs, particularly in Western Australia and Tasmania.'
aquatic_kelp_forests_australian_stressors["Ocean Warming"]["Impact on Biodiversity"] = 'Loss of habitat.\nShifts in community structure (towards more warm-tolerant species and *turf algae*).\nRange contractions of kelp species.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\nStrengthening of the East Australian Current (EAC): Bringing warmer waters further south.\n**Influences (Stressors):**\n* Range shifts\n**Logic Description:** Ocean warming, particularly marine heatwaves, has caused *severe* and widespread kelp forest declines in parts of Australia, leading to significant ecosystem shifts. This is a major area of concern and research.'
aquatic_kelp_forests_australian_stressors["Ocean Warming"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', 'Strengthening of the East Australian Current (EAC): Bringing warmer waters further south.', '**Influences (Stressors):**', '* Range shifts', '**Logic Description:** Ocean warming, particularly marine heatwaves, has caused *severe* and widespread kelp forest declines in parts of Australia, leading to significant ecosystem shifts. This is a major area of concern and research.']
aquatic_kelp_forests_australian_stressors["Ocean Warming"]["Influences"] = ['* Range shifts', '**Logic Description:** Ocean warming, particularly marine heatwaves, has caused *severe* and widespread kelp forest declines in parts of Australia, leading to significant ecosystem shifts. This is a major area of concern and research.']
aquatic_kelp_forests_australian_stressors["Ocean Warming"]["Logic Description"] = '---'

# --- Overgrazing ---
aquatic_kelp_forests_australian_stressors["Overgrazing"]["Metric"] = 'Sea urchin density; abundance of other herbivorous fish; kelp cover.'
aquatic_kelp_forests_australian_stressors["Overgrazing"]["Data Sources"] = ['* Underwater Surveys', '* Research', '**Impact on Area:** Formation of urchin barrens.', '**Impact on Biodiversity:**', 'Loss of kelp forest habitat.', '* Reduced biodiversity.', '**Influenced By (Stressors):**', 'Overfishing of Urchin Predators: (e.g., rock lobsters).', '* Ocean Warming', '**Influences (Stressors):**', 'Kelp Cover.', '**Logic Description:** Overgrazing by sea urchins (and in some areas, certain fish species) can lead to the formation of urchin barrens, particularly where predator populations have been reduced.']
aquatic_kelp_forests_australian_stressors["Overgrazing"]["Impact on Area"] = 'Formation of urchin barrens.'
aquatic_kelp_forests_australian_stressors["Overgrazing"]["Impact on Biodiversity"] = 'Loss of kelp forest habitat.\n* Reduced biodiversity.\n**Influenced By (Stressors):**\nOverfishing of Urchin Predators: (e.g., rock lobsters).\n* Ocean Warming\n**Influences (Stressors):**\nKelp Cover.\n**Logic Description:** Overgrazing by sea urchins (and in some areas, certain fish species) can lead to the formation of urchin barrens, particularly where predator populations have been reduced.'
aquatic_kelp_forests_australian_stressors["Overgrazing"]["Influenced By"] = ['Overfishing of Urchin Predators: (e.g., rock lobsters).', '* Ocean Warming', '**Influences (Stressors):**', 'Kelp Cover.', '**Logic Description:** Overgrazing by sea urchins (and in some areas, certain fish species) can lead to the formation of urchin barrens, particularly where predator populations have been reduced.']
aquatic_kelp_forests_australian_stressors["Overgrazing"]["Influences"] = ['Kelp Cover.', '**Logic Description:** Overgrazing by sea urchins (and in some areas, certain fish species) can lead to the formation of urchin barrens, particularly where predator populations have been reduced.']
aquatic_kelp_forests_australian_stressors["Overgrazing"]["Logic Description"] = '---'

# --- Invasive Species ---
aquatic_kelp_forests_australian_stressors["Invasive Species"]["Metric"] = 'Distribution and abundance of invasive species (e.g., *Undaria pinnatifida* - Japanese kelp).'
aquatic_kelp_forests_australian_stressors["Invasive Species"]["Data Sources"] = ['* Underwater surveys.', '* Research.', '**Impact on Area:** Competition with native kelp species.', '**Impact on Biodiversity:**', '* Can outcompete native kelp and alter habitat structure.', '**Influenced By (Stressors):**', '* Shipping (ballast water, hull fouling).', '* Aquaculture', '**Influences (Stressors):**', '* Native kelp populations', '**Logic Description**: Invasive species are a threat.']
aquatic_kelp_forests_australian_stressors["Invasive Species"]["Impact on Area"] = 'Competition with native kelp species.'
aquatic_kelp_forests_australian_stressors["Invasive Species"]["Impact on Biodiversity"] = '* Can outcompete native kelp and alter habitat structure.\n**Influenced By (Stressors):**\n* Shipping (ballast water, hull fouling).\n* Aquaculture\n**Influences (Stressors):**\n* Native kelp populations\n**Logic Description**: Invasive species are a threat.'
aquatic_kelp_forests_australian_stressors["Invasive Species"]["Influenced By"] = ['* Shipping (ballast water, hull fouling).', '* Aquaculture', '**Influences (Stressors):**', '* Native kelp populations', '**Logic Description**: Invasive species are a threat.']
aquatic_kelp_forests_australian_stressors["Invasive Species"]["Influences"] = ['* Native kelp populations', '**Logic Description**: Invasive species are a threat.']

