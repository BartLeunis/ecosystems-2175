from stressor_templates import *
import copy

aquatic_cold_water_corals_stressors = {
    "Bottom Trawling": {},
    "Climate Change": copy.deepcopy(climate_change_template),
    "Ocean Acidification": {},
}

# --- Bottom Trawling ---
aquatic_cold_water_corals_stressors["Bottom Trawling"]["Metric"] = 'Area of cold-water coral habitats trawled; frequency of trawling; damage to coral structures.'
aquatic_cold_water_corals_stressors["Bottom Trawling"]["Data Sources"] = ['Fisheries data (often incomplete).', 'Vessel Monitoring System (VMS) data.', 'Underwater surveys (using ROVs and submersibles).', 'Research publications.', '**Impact on Area:** Severe physical destruction of coral structures; removal of habitat-forming species.', '**Impact on Biodiversity:**', 'High mortality of corals and associated organisms.', 'Loss of biodiversity hotspots.', 'Disruption of deep-sea food webs.', 'Extremely slow recovery rates (centuries or millennia).', '**Influenced By (Stressors):**', 'Demand for Deep-Sea Fish: That may occur near coral habitats.', 'Fishing Technology.', 'Weak Governance and Enforcement.', '**Influences (Stressors):**', 'Habitat Destruction (the overwhelming impact).', '**Logic Description:** Bottom trawling is *by far* the greatest threat to cold-water coral ecosystems, causing severe and often irreversible damage to these slow-growing and fragile habitats.']
aquatic_cold_water_corals_stressors["Bottom Trawling"]["Impact on Area"] = 'Severe physical destruction of coral structures; removal of habitat-forming species.'
aquatic_cold_water_corals_stressors["Bottom Trawling"]["Impact on Biodiversity"] = 'High mortality of corals and associated organisms.\nLoss of biodiversity hotspots.\nDisruption of deep-sea food webs.\nExtremely slow recovery rates (centuries or millennia).\n**Influenced By (Stressors):**\nDemand for Deep-Sea Fish: That may occur near coral habitats.\nFishing Technology.\nWeak Governance and Enforcement.\n**Influences (Stressors):**\nHabitat Destruction (the overwhelming impact).\n**Logic Description:** Bottom trawling is *by far* the greatest threat to cold-water coral ecosystems, causing severe and often irreversible damage to these slow-growing and fragile habitats.'
aquatic_cold_water_corals_stressors["Bottom Trawling"]["Influenced By"] = ['Demand for Deep-Sea Fish: That may occur near coral habitats.', 'Fishing Technology.', 'Weak Governance and Enforcement.', '**Influences (Stressors):**', 'Habitat Destruction (the overwhelming impact).', '**Logic Description:** Bottom trawling is *by far* the greatest threat to cold-water coral ecosystems, causing severe and often irreversible damage to these slow-growing and fragile habitats.']
aquatic_cold_water_corals_stressors["Bottom Trawling"]["Influences"] = ['Habitat Destruction (the overwhelming impact).', '**Logic Description:** Bottom trawling is *by far* the greatest threat to cold-water coral ecosystems, causing severe and often irreversible damage to these slow-growing and fragile habitats.']
aquatic_cold_water_corals_stressors["Bottom Trawling"]["Logic Description"] = '---'

# --- Climate Change ---
aquatic_cold_water_corals_stressors["Climate Change"]["Metric"] = 'Changes in water temperature, oxygen levels, and pH, currents.'
aquatic_cold_water_corals_stressors["Climate Change"]["Data Sources"] = ['* Oceanographic data', '* Climate Models', '**Impact on Area:** Changes in environment', '**Impact on Biodiversity:**', '* Possible range shifts', '* Physiological impacts.', '**Influenced By (Stressors):**', '* Global emissions.', '**Influences (Stressors):**', '*  Ocean Acidification.', '**Logic Description:** Climate change can impact cold water corals, though the extent is still being investigated.']
aquatic_cold_water_corals_stressors["Climate Change"]["Impact on Area"] = 'Changes in environment'
aquatic_cold_water_corals_stressors["Climate Change"]["Impact on Biodiversity"] = '* Possible range shifts\n* Physiological impacts.\n**Influenced By (Stressors):**\n* Global emissions.\n**Influences (Stressors):**\n*  Ocean Acidification.\n**Logic Description:** Climate change can impact cold water corals, though the extent is still being investigated.'
aquatic_cold_water_corals_stressors["Climate Change"]["Influenced By"] = ['* Global emissions.', '**Influences (Stressors):**', '*  Ocean Acidification.', '**Logic Description:** Climate change can impact cold water corals, though the extent is still being investigated.']
aquatic_cold_water_corals_stressors["Climate Change"]["Influences"] = ['*  Ocean Acidification.', '**Logic Description:** Climate change can impact cold water corals, though the extent is still being investigated.']
aquatic_cold_water_corals_stressors["Climate Change"]["Logic Description"] = '---'

# --- Ocean Acidification ---
aquatic_cold_water_corals_stressors["Ocean Acidification"]["Metric"] = 'pH levels and carbonate saturation'
aquatic_cold_water_corals_stressors["Ocean Acidification"]["Data Sources"] = ['* Oceanographic data', '* Models', '**Impact on Area**: Reduced calcification rates', '**Impact on Biodiversity:**', '* Coral skeleton weakening', '* Reduced growth', '**Influenced By (Stressors):**', '* Atmospheric CO2', '**Influences (Stressors):**', '* Coral health.', '**Logic Description:**  Acidification hinders the ability to build skeletons.']
aquatic_cold_water_corals_stressors["Ocean Acidification"]["Impact on Biodiversity"] = '* Coral skeleton weakening\n* Reduced growth\n**Influenced By (Stressors):**\n* Atmospheric CO2\n**Influences (Stressors):**\n* Coral health.\n**Logic Description:**  Acidification hinders the ability to build skeletons.'
aquatic_cold_water_corals_stressors["Ocean Acidification"]["Influenced By"] = ['* Atmospheric CO2', '**Influences (Stressors):**', '* Coral health.', '**Logic Description:**  Acidification hinders the ability to build skeletons.']
aquatic_cold_water_corals_stressors["Ocean Acidification"]["Influences"] = ['* Coral health.', '**Logic Description:**  Acidification hinders the ability to build skeletons.']
aquatic_cold_water_corals_stressors["Ocean Acidification"]["Logic Description"] = '---'

