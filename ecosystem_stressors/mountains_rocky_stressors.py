from stressor_templates import *
import copy

mountains_rocky_stressors = {
    "Wildfires": copy.deepcopy(fire_regime_template),
    "Insect Outbreaks": {},
    "Climate Change": copy.deepcopy(climate_change_template),
    "Resource Extraction": {},
}

# --- Wildfires ---
mountains_rocky_stressors["Wildfires"]["Metric"] = 'Fire frequency; fire intensity; area burned; fire season length.'
mountains_rocky_stressors["Wildfires"]["Data Sources"] = ['US Forest Service data.', 'Canadian Forest Service data.', 'Remote sensing data.', 'Research publications.', '**Impact on Area:** *Large-scale* changes in forest structure and composition; increased erosion.', '**Impact on Biodiversity:**', 'Loss of habitat for some species.', 'Creation of habitat for other species (fire-adapted species).', 'Increased risk of invasive species establishment.', '**Influenced By (Stressors):**', 'Climate Change: Hotter, drier conditions increase fire risk.', 'Forest Management Practices: Fire suppression has led to a buildup of fuels in some areas.', 'Insect Outbreaks: (e.g., mountain pine beetle) can create large areas of dead trees, increasing fire risk.', '**Influences (Stressors):**', 'Forest Structure.', 'Biodiversity.', 'Water Quality (erosion).', 'Air Quality', '**Logic Description:** Wildfires are a *major* and increasing stressor in the Rocky Mountains, driven by climate change, forest management practices, and insect outbreaks.']
mountains_rocky_stressors["Wildfires"]["Impact on Area"] = '*Large-scale* changes in forest structure and composition; increased erosion.'
mountains_rocky_stressors["Wildfires"]["Impact on Biodiversity"] = 'Loss of habitat for some species.\nCreation of habitat for other species (fire-adapted species).\nIncreased risk of invasive species establishment.\n**Influenced By (Stressors):**\nClimate Change: Hotter, drier conditions increase fire risk.\nForest Management Practices: Fire suppression has led to a buildup of fuels in some areas.\nInsect Outbreaks: (e.g., mountain pine beetle) can create large areas of dead trees, increasing fire risk.\n**Influences (Stressors):**\nForest Structure.\nBiodiversity.\nWater Quality (erosion).\nAir Quality\n**Logic Description:** Wildfires are a *major* and increasing stressor in the Rocky Mountains, driven by climate change, forest management practices, and insect outbreaks.'
mountains_rocky_stressors["Wildfires"]["Influenced By"] = ['Climate Change: Hotter, drier conditions increase fire risk.', 'Forest Management Practices: Fire suppression has led to a buildup of fuels in some areas.', 'Insect Outbreaks: (e.g., mountain pine beetle) can create large areas of dead trees, increasing fire risk.', '**Influences (Stressors):**', 'Forest Structure.', 'Biodiversity.', 'Water Quality (erosion).', 'Air Quality', '**Logic Description:** Wildfires are a *major* and increasing stressor in the Rocky Mountains, driven by climate change, forest management practices, and insect outbreaks.']
mountains_rocky_stressors["Wildfires"]["Influences"] = ['Forest Structure.', 'Biodiversity.', 'Water Quality (erosion).', 'Air Quality', '**Logic Description:** Wildfires are a *major* and increasing stressor in the Rocky Mountains, driven by climate change, forest management practices, and insect outbreaks.']
mountains_rocky_stressors["Wildfires"]["Logic Description"] = '---'

# --- Insect Outbreaks ---
mountains_rocky_stressors["Insect Outbreaks"]["Metric"] = 'Area affected by mountain pine beetle and other bark beetles; tree mortality.'
mountains_rocky_stressors["Insect Outbreaks"]["Data Sources"] = ['US Forest Service data.', 'Canadian Forest Service data.', 'Aerial surveys.', 'Research publications.', '**Impact on Area:** *Widespread* tree mortality.', '**Impact on Biodiversity:**', 'Loss of forest habitat.', 'Changes in forest structure and composition.', 'Increased risk of wildfires.', '**Influenced By (Stressors):**', 'Climate Change: Warmer winters allow more beetles to survive.', 'Drought Stress: Weakens trees and makes them more susceptible to attack.', 'Forest Management Practices: Dense, even-aged forests are more vulnerable.', '**Influences (Stressors):**', 'Forest Structure.', 'Wildfire Risk.', 'Water Resources (changes in snowpack and runoff).', '**Logic Description:** Insect outbreaks, particularly mountain pine beetle, have caused *massive* tree mortality in the Rocky Mountains, driven by climate change and forest conditions.']
mountains_rocky_stressors["Insect Outbreaks"]["Impact on Area"] = '*Widespread* tree mortality.'
mountains_rocky_stressors["Insect Outbreaks"]["Impact on Biodiversity"] = 'Loss of forest habitat.\nChanges in forest structure and composition.\nIncreased risk of wildfires.\n**Influenced By (Stressors):**\nClimate Change: Warmer winters allow more beetles to survive.\nDrought Stress: Weakens trees and makes them more susceptible to attack.\nForest Management Practices: Dense, even-aged forests are more vulnerable.\n**Influences (Stressors):**\nForest Structure.\nWildfire Risk.\nWater Resources (changes in snowpack and runoff).\n**Logic Description:** Insect outbreaks, particularly mountain pine beetle, have caused *massive* tree mortality in the Rocky Mountains, driven by climate change and forest conditions.'
mountains_rocky_stressors["Insect Outbreaks"]["Influenced By"] = ['Climate Change: Warmer winters allow more beetles to survive.', 'Drought Stress: Weakens trees and makes them more susceptible to attack.', 'Forest Management Practices: Dense, even-aged forests are more vulnerable.', '**Influences (Stressors):**', 'Forest Structure.', 'Wildfire Risk.', 'Water Resources (changes in snowpack and runoff).', '**Logic Description:** Insect outbreaks, particularly mountain pine beetle, have caused *massive* tree mortality in the Rocky Mountains, driven by climate change and forest conditions.']
mountains_rocky_stressors["Insect Outbreaks"]["Influences"] = ['Forest Structure.', 'Wildfire Risk.', 'Water Resources (changes in snowpack and runoff).', '**Logic Description:** Insect outbreaks, particularly mountain pine beetle, have caused *massive* tree mortality in the Rocky Mountains, driven by climate change and forest conditions.']
mountains_rocky_stressors["Insect Outbreaks"]["Logic Description"] = '---'

# --- Climate Change ---
mountains_rocky_stressors["Climate Change"]["Metric"] = 'Temperature increase; changes in snowpack; changes in precipitation.'
mountains_rocky_stressors["Climate Change"]["Data Sources"] = ['* Climate models.', '* Historical Records', '**Impact on Area:** Changes to ecosystems', '**Impact on Biodiversity:**', '* Shifts in distributions.', '* Increased stress', '**Influenced By (Stressors):**', '* Global GHG', '**Influences (Stressors):**', '* Water, fires, insects', '**Logic Description:** Climate change is a major driver of many stressors.']
mountains_rocky_stressors["Climate Change"]["Impact on Area"] = 'Changes to ecosystems'
mountains_rocky_stressors["Climate Change"]["Impact on Biodiversity"] = '* Shifts in distributions.\n* Increased stress\n**Influenced By (Stressors):**\n* Global GHG\n**Influences (Stressors):**\n* Water, fires, insects\n**Logic Description:** Climate change is a major driver of many stressors.'
mountains_rocky_stressors["Climate Change"]["Influenced By"] = ['* Global GHG', '**Influences (Stressors):**', '* Water, fires, insects', '**Logic Description:** Climate change is a major driver of many stressors.']
mountains_rocky_stressors["Climate Change"]["Influences"] = ['* Water, fires, insects', '**Logic Description:** Climate change is a major driver of many stressors.']
mountains_rocky_stressors["Climate Change"]["Logic Description"] = '---'

# --- Resource Extraction ---
mountains_rocky_stressors["Resource Extraction"]["Metric"] = 'Area affected by mining and logging; pollution levels.'
mountains_rocky_stressors["Resource Extraction"]["Data Sources"] = ['* Government records', '* Research', '**Impact on Area:** Habitat loss and fragmentation; pollution.', '**Impact on Biodiversity:**', '* Direct and indirect impacts on species.', '**Influenced By (Stressors):**', '* Demand for resources.', '**Influences (Stressors):**', '* Habitat loss', '* Pollution', '**Logic Description:** Resource extraction continues to be a stressor.']
mountains_rocky_stressors["Resource Extraction"]["Impact on Area"] = 'Habitat loss and fragmentation; pollution.'
mountains_rocky_stressors["Resource Extraction"]["Impact on Biodiversity"] = '* Direct and indirect impacts on species.\n**Influenced By (Stressors):**\n* Demand for resources.\n**Influences (Stressors):**\n* Habitat loss\n* Pollution\n**Logic Description:** Resource extraction continues to be a stressor.'
mountains_rocky_stressors["Resource Extraction"]["Influenced By"] = ['* Demand for resources.', '**Influences (Stressors):**', '* Habitat loss', '* Pollution', '**Logic Description:** Resource extraction continues to be a stressor.']
mountains_rocky_stressors["Resource Extraction"]["Influences"] = ['* Habitat loss', '* Pollution', '**Logic Description:** Resource extraction continues to be a stressor.']
mountains_rocky_stressors["Resource Extraction"]["Logic Description"] = '---'

