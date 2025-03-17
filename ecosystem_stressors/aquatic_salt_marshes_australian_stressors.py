from stressor_templates import *
import copy

aquatic_salt_marshes_australian_stressors = {
    "Sea Level Rise": {},
    "Coastal Development": {},
    "Altered Hydrology": copy.deepcopy(altered_hydrology_template),
}

# --- Sea Level Rise ---
aquatic_salt_marshes_australian_stressors["Sea Level Rise"]["Metric"] = 'Rate of sea level rise (mm/year); marsh elevation; accretion rates.'
aquatic_salt_marshes_australian_stressors["Sea Level Rise"]["Data Sources"] = ['Tide gauge records.', 'Satellite altimetry.', 'Research publications (CSIRO).', 'Australian Bureau of Meteorology', '**Impact on Area:** Inundation; erosion; potential for landward migration (in some areas).', '**Impact on Biodiversity:**', 'Habitat loss.', 'Species shifts.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Coastal Erosion.', 'Habitat Loss.', '**Logic Description:** Sea level rise is a growing threat to Australian salt marshes.']
aquatic_salt_marshes_australian_stressors["Sea Level Rise"]["Impact on Area"] = 'Inundation; erosion; potential for landward migration (in some areas).'
aquatic_salt_marshes_australian_stressors["Sea Level Rise"]["Impact on Biodiversity"] = 'Habitat loss.\nSpecies shifts.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\n**Influences (Stressors):**\nCoastal Erosion.\nHabitat Loss.\n**Logic Description:** Sea level rise is a growing threat to Australian salt marshes.'
aquatic_salt_marshes_australian_stressors["Sea Level Rise"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Coastal Erosion.', 'Habitat Loss.', '**Logic Description:** Sea level rise is a growing threat to Australian salt marshes.']
aquatic_salt_marshes_australian_stressors["Sea Level Rise"]["Influences"] = ['Coastal Erosion.', 'Habitat Loss.', '**Logic Description:** Sea level rise is a growing threat to Australian salt marshes.']
aquatic_salt_marshes_australian_stressors["Sea Level Rise"]["Logic Description"] = '---'

# --- Coastal Development ---
aquatic_salt_marshes_australian_stressors["Coastal Development"]["Metric"] = 'Area converted, Length of hardened shoreline'
aquatic_salt_marshes_australian_stressors["Coastal Development"]["Data Sources"] = ['* Remote sensing', '* Government', '**Impact on Area:** Direct loss and fragmentation of habitat.', '**Impact on Biodiversity:**', '* Habitat loss', '**Influenced By (Stressors):**', '* Urban Expansion', '* Infrastructure', '**Influences (Stressors):**', '* Habitat loss', '* Coastal squeeze', '**Logic Description:** Coastal development removes marsh habitat and restricts landward migration.']
aquatic_salt_marshes_australian_stressors["Coastal Development"]["Impact on Area"] = 'Direct loss and fragmentation of habitat.'
aquatic_salt_marshes_australian_stressors["Coastal Development"]["Impact on Biodiversity"] = '* Habitat loss\n**Influenced By (Stressors):**\n* Urban Expansion\n* Infrastructure\n**Influences (Stressors):**\n* Habitat loss\n* Coastal squeeze\n**Logic Description:** Coastal development removes marsh habitat and restricts landward migration.'
aquatic_salt_marshes_australian_stressors["Coastal Development"]["Influenced By"] = ['* Urban Expansion', '* Infrastructure', '**Influences (Stressors):**', '* Habitat loss', '* Coastal squeeze', '**Logic Description:** Coastal development removes marsh habitat and restricts landward migration.']
aquatic_salt_marshes_australian_stressors["Coastal Development"]["Influences"] = ['* Habitat loss', '* Coastal squeeze', '**Logic Description:** Coastal development removes marsh habitat and restricts landward migration.']
aquatic_salt_marshes_australian_stressors["Coastal Development"]["Logic Description"] = '---'

# --- Altered Hydrology ---
aquatic_salt_marshes_australian_stressors["Altered Hydrology"]["Metric"] = 'Changes in freshwater inflow; presence of drainage structures.'
aquatic_salt_marshes_australian_stressors["Altered Hydrology"]["Data Sources"] = ['* Water management records.', '* Research.', '**Impact on Area:**', 'Changes in salinity.', '* Altered sedimentation.', '**Impact on Biodiversity:**', '* Shifts in plant communities.', '**Influenced By (Stressors):**', '* Drainage and Flood Mitigation.', '* Upstream Water Use.', '**Influences (Stressors):**', '* Salinity.', '* Sedimentation.', '**Logic Description:** Alterations to freshwater inflow and drainage patterns impact marsh ecosystems.']
aquatic_salt_marshes_australian_stressors["Altered Hydrology"]["Impact on Area"] = ''
aquatic_salt_marshes_australian_stressors["Altered Hydrology"]["Impact on Biodiversity"] = '* Shifts in plant communities.\n**Influenced By (Stressors):**\n* Drainage and Flood Mitigation.\n* Upstream Water Use.\n**Influences (Stressors):**\n* Salinity.\n* Sedimentation.\n**Logic Description:** Alterations to freshwater inflow and drainage patterns impact marsh ecosystems.'
aquatic_salt_marshes_australian_stressors["Altered Hydrology"]["Influenced By"] = ['* Drainage and Flood Mitigation.', '* Upstream Water Use.', '**Influences (Stressors):**', '* Salinity.', '* Sedimentation.', '**Logic Description:** Alterations to freshwater inflow and drainage patterns impact marsh ecosystems.']
aquatic_salt_marshes_australian_stressors["Altered Hydrology"]["Influences"] = ['* Salinity.', '* Sedimentation.', '**Logic Description:** Alterations to freshwater inflow and drainage patterns impact marsh ecosystems.']
aquatic_salt_marshes_australian_stressors["Altered Hydrology"]["Logic Description"] = '---'

