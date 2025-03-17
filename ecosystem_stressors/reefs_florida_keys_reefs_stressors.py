from stressor_templates import *
import copy

reefs_florida_keys_reefs_stressors = {
    "Ocean Warming and Bleaching": {},
    "Physical Damage": {},
}

# --- Ocean Warming and Bleaching ---
reefs_florida_keys_reefs_stressors["Ocean Warming and Bleaching"]["Metric"] = 'Sea surface temperature (SST); frequency and severity of bleaching events; Degree Heating Weeks (DHW).'
reefs_florida_keys_reefs_stressors["Ocean Warming and Bleaching"]["Data Sources"] = ['NOAA Coral Reef Watch.', 'FKNMS monitoring data.', 'Research publications.', '**Impact on Area:** Coral bleaching; reduced coral growth rates.', '**Impact on Biodiversity:**', 'Coral mortality (if bleaching is severe or prolonged).', 'Shifts in coral species composition.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Coral Disease (bleached corals are more susceptible).', 'Reef Resilience.', '**Logic Description:** Rising ocean temperatures, driven by climate change, cause coral bleaching, which can lead to coral mortality and impact the overall health of the reef.']
reefs_florida_keys_reefs_stressors["Ocean Warming and Bleaching"]["Impact on Area"] = 'Coral bleaching; reduced coral growth rates.'
reefs_florida_keys_reefs_stressors["Ocean Warming and Bleaching"]["Impact on Biodiversity"] = 'Coral mortality (if bleaching is severe or prolonged).\nShifts in coral species composition.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\n**Influences (Stressors):**\nCoral Disease (bleached corals are more susceptible).\nReef Resilience.\n**Logic Description:** Rising ocean temperatures, driven by climate change, cause coral bleaching, which can lead to coral mortality and impact the overall health of the reef.'
reefs_florida_keys_reefs_stressors["Ocean Warming and Bleaching"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Coral Disease (bleached corals are more susceptible).', 'Reef Resilience.', '**Logic Description:** Rising ocean temperatures, driven by climate change, cause coral bleaching, which can lead to coral mortality and impact the overall health of the reef.']
reefs_florida_keys_reefs_stressors["Ocean Warming and Bleaching"]["Influences"] = ['Coral Disease (bleached corals are more susceptible).', 'Reef Resilience.', '**Logic Description:** Rising ocean temperatures, driven by climate change, cause coral bleaching, which can lead to coral mortality and impact the overall health of the reef.']
reefs_florida_keys_reefs_stressors["Ocean Warming and Bleaching"]["Logic Description"] = '---'
reefs_florida_keys_reefs_stressors["Ocean Warming and Bleaching"]["Impact Function"] = "impact_ocean_warming_and_bleaching_reefs_florida_keys_reefs"

# --- Physical Damage ---
reefs_florida_keys_reefs_stressors["Physical Damage"]["Metric"] = 'Number of boat groundings; diver contacts with corals; anchor damage.'
reefs_florida_keys_reefs_stressors["Physical Damage"]["Data Sources"] = ['FKNMS reports.', 'Observations by researchers and dive operators.', '**Impact on Area:** Direct physical damage to corals.', '**Impact on Biodiversity:**', 'Coral breakage and mortality.', 'Loss of reef structure.', '**Influenced By (Stressors):**', 'High Boating Traffic: In popular reef areas.', 'Lack of Awareness: Among boaters and divers.', 'Inadequate Mooring Buoys.', '**Influences (Stressors):**', 'Coral Cover (localized impacts).', '**Logic Description:** Physical damage from boat anchors, groundings, and diver/snorkeler contact can cause localized but significant damage to corals.']
reefs_florida_keys_reefs_stressors["Physical Damage"]["Impact on Area"] = 'Direct physical damage to corals.'
reefs_florida_keys_reefs_stressors["Physical Damage"]["Impact on Biodiversity"] = 'Coral breakage and mortality.\nLoss of reef structure.\n**Influenced By (Stressors):**\nHigh Boating Traffic: In popular reef areas.\nLack of Awareness: Among boaters and divers.\nInadequate Mooring Buoys.\n**Influences (Stressors):**\nCoral Cover (localized impacts).\n**Logic Description:** Physical damage from boat anchors, groundings, and diver/snorkeler contact can cause localized but significant damage to corals.'
reefs_florida_keys_reefs_stressors["Physical Damage"]["Influenced By"] = ['High Boating Traffic: In popular reef areas.', 'Lack of Awareness: Among boaters and divers.', 'Inadequate Mooring Buoys.', '**Influences (Stressors):**', 'Coral Cover (localized impacts).', '**Logic Description:** Physical damage from boat anchors, groundings, and diver/snorkeler contact can cause localized but significant damage to corals.']
reefs_florida_keys_reefs_stressors["Physical Damage"]["Influences"] = ['Coral Cover (localized impacts).', '**Logic Description:** Physical damage from boat anchors, groundings, and diver/snorkeler contact can cause localized but significant damage to corals.']
reefs_florida_keys_reefs_stressors["Physical Damage"]["Logic Description"] = '---'
reefs_florida_keys_reefs_stressors["Physical Damage"]["Impact Function"] = "impact_physical_damage_reefs_florida_keys_reefs"

