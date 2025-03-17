from stressor_templates import *
import copy

aquatic_seamounts_stressors = {
    "Bottom Trawling": {},
    "Deep-Sea Mining": {},
    "Climate Change": copy.deepcopy(climate_change_template),
    "Plastic Pollution": copy.deepcopy(pollution_template),
}

# --- Bottom Trawling ---
aquatic_seamounts_stressors["Bottom Trawling"]["Metric"] = 'Area of seamounts trawled (km²/year); frequency of trawling; damage to coral and sponge communities.'
aquatic_seamounts_stressors["Bottom Trawling"]["Data Sources"] = ['Fisheries data (often incomplete for seamounts).', 'Vessel Monitoring System (VMS) data.', 'Underwater surveys (using ROVs and submersibles).', 'Research publications.', '**Impact on Area:** Severe physical destruction of benthic habitats; removal of habitat-forming species (corals, sponges).', '**Impact on Biodiversity:**', 'High mortality of benthic organisms, including long-lived and slow-growing species.', 'Loss of biodiversity hotspots.', 'Disruption of seamount food webs.', 'Reduced structural complexity.', '**Influenced By (Stressors):**', 'Demand for Deep-Sea Fish: (e.g., orange roughy, which often aggregate on seamounts).', 'Fishing Technology.', 'Weak Governance and Enforcement.', '**Influences (Stressors):**', 'Habitat Destruction (primary impact).', '**Logic Description:** Bottom trawling is *extremely* destructive to seamount ecosystems, physically destroying the fragile habitats and the diverse communities they support. Recovery, if possible, takes centuries.']
aquatic_seamounts_stressors["Bottom Trawling"]["Impact on Area"] = 'Severe physical destruction of benthic habitats; removal of habitat-forming species (corals, sponges).'
aquatic_seamounts_stressors["Bottom Trawling"]["Impact on Biodiversity"] = 'High mortality of benthic organisms, including long-lived and slow-growing species.\nLoss of biodiversity hotspots.\nDisruption of seamount food webs.\nReduced structural complexity.\n**Influenced By (Stressors):**\nDemand for Deep-Sea Fish: (e.g., orange roughy, which often aggregate on seamounts).\nFishing Technology.\nWeak Governance and Enforcement.\n**Influences (Stressors):**\nHabitat Destruction (primary impact).\n**Logic Description:** Bottom trawling is *extremely* destructive to seamount ecosystems, physically destroying the fragile habitats and the diverse communities they support. Recovery, if possible, takes centuries.'
aquatic_seamounts_stressors["Bottom Trawling"]["Influenced By"] = ['Demand for Deep-Sea Fish: (e.g., orange roughy, which often aggregate on seamounts).', 'Fishing Technology.', 'Weak Governance and Enforcement.', '**Influences (Stressors):**', 'Habitat Destruction (primary impact).', '**Logic Description:** Bottom trawling is *extremely* destructive to seamount ecosystems, physically destroying the fragile habitats and the diverse communities they support. Recovery, if possible, takes centuries.']
aquatic_seamounts_stressors["Bottom Trawling"]["Influences"] = ['Habitat Destruction (primary impact).', '**Logic Description:** Bottom trawling is *extremely* destructive to seamount ecosystems, physically destroying the fragile habitats and the diverse communities they support. Recovery, if possible, takes centuries.']
aquatic_seamounts_stressors["Bottom Trawling"]["Logic Description"] = '---'
aquatic_seamounts_stressors["Bottom Trawling"]["Impact Function"] = "impact_bottom_trawling_aquatic_seamounts"

# --- Deep-Sea Mining ---
aquatic_seamounts_stressors["Deep-Sea Mining"]["Metric"] = 'Area of seamounts licensed for exploration or exploitation (km²); concentrations of target minerals (e.g., cobalt crusts).'
aquatic_seamounts_stressors["Deep-Sea Mining"]["Data Sources"] = ['International Seabed Authority (ISA).', 'National government data.', 'Research publications.', 'Environmental Impact Assessments (EIAs).', '**Impact on Area:** Removal of cobalt crusts (which form on seamounts); potential for sediment plumes.', '**Impact on Biodiversity:**', 'Destruction of habitat and associated communities.', 'Potential for long-term impacts.', 'Release of toxic substances.', '**Influenced By (Stressors):**', 'Demand for Cobalt and Other Minerals.', 'Technological Advancements.', 'International Regulations.', '**Influences (Stressors):**', '* Habitat destruction', 'Water Quality.', '**Logic Description:** Mining for cobalt crusts on seamounts poses a significant threat, involving the direct removal of the substrate and the diverse communities that live on it.']
aquatic_seamounts_stressors["Deep-Sea Mining"]["Impact on Area"] = 'Removal of cobalt crusts (which form on seamounts); potential for sediment plumes.'
aquatic_seamounts_stressors["Deep-Sea Mining"]["Impact on Biodiversity"] = 'Destruction of habitat and associated communities.\nPotential for long-term impacts.\nRelease of toxic substances.\n**Influenced By (Stressors):**\nDemand for Cobalt and Other Minerals.\nTechnological Advancements.\nInternational Regulations.\n**Influences (Stressors):**\n* Habitat destruction\nWater Quality.\n**Logic Description:** Mining for cobalt crusts on seamounts poses a significant threat, involving the direct removal of the substrate and the diverse communities that live on it.'
aquatic_seamounts_stressors["Deep-Sea Mining"]["Influenced By"] = ['Demand for Cobalt and Other Minerals.', 'Technological Advancements.', 'International Regulations.', '**Influences (Stressors):**', '* Habitat destruction', 'Water Quality.', '**Logic Description:** Mining for cobalt crusts on seamounts poses a significant threat, involving the direct removal of the substrate and the diverse communities that live on it.']
aquatic_seamounts_stressors["Deep-Sea Mining"]["Influences"] = ['* Habitat destruction', 'Water Quality.', '**Logic Description:** Mining for cobalt crusts on seamounts poses a significant threat, involving the direct removal of the substrate and the diverse communities that live on it.']
aquatic_seamounts_stressors["Deep-Sea Mining"]["Logic Description"] = '---'
aquatic_seamounts_stressors["Deep-Sea Mining"]["Impact Function"] = "impact_deep_sea_mining_aquatic_seamounts"

# --- Climate Change ---
aquatic_seamounts_stressors["Climate Change"]["Metric"] = 'Changes in temperature, ocean currents, oxygen levels, and pH at seamount depths.'
aquatic_seamounts_stressors["Climate Change"]["Data Sources"] = ['Oceanographic data (sparse for seamounts).', 'Climate models.', '**Impact on Area:** Changes in the physical and chemical environment.', '**Impact on Biodiversity:**', 'Potential shifts in species distributions.', 'Impacts on physiology and reproduction.', '**Influenced By (Stressors):**', 'Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Ocean Acidification.', '**Logic Description:** While seamounts are less directly impacted by surface warming, changes in ocean currents, oxygen levels, and acidification driven by climate change could still affect seamount ecosystems.']
aquatic_seamounts_stressors["Climate Change"]["Impact on Area"] = 'Changes in the physical and chemical environment.'
aquatic_seamounts_stressors["Climate Change"]["Impact on Biodiversity"] = 'Potential shifts in species distributions.\nImpacts on physiology and reproduction.\n**Influenced By (Stressors):**\nGlobal Greenhouse Gas Emissions.\n**Influences (Stressors):**\nOcean Acidification.\n**Logic Description:** While seamounts are less directly impacted by surface warming, changes in ocean currents, oxygen levels, and acidification driven by climate change could still affect seamount ecosystems.'
aquatic_seamounts_stressors["Climate Change"]["Influenced By"] = ['Global Greenhouse Gas Emissions.', '**Influences (Stressors):**', 'Ocean Acidification.', '**Logic Description:** While seamounts are less directly impacted by surface warming, changes in ocean currents, oxygen levels, and acidification driven by climate change could still affect seamount ecosystems.']
aquatic_seamounts_stressors["Climate Change"]["Influences"] = ['Ocean Acidification.', '**Logic Description:** While seamounts are less directly impacted by surface warming, changes in ocean currents, oxygen levels, and acidification driven by climate change could still affect seamount ecosystems.']
aquatic_seamounts_stressors["Climate Change"]["Logic Description"] = '---'
aquatic_seamounts_stressors["Climate Change"]["Impact Function"] = "impact_climate_change_aquatic_seamounts"

# --- Plastic Pollution ---
aquatic_seamounts_stressors["Plastic Pollution"]["Metric"] = 'Plastic and microplastic abundance.'
aquatic_seamounts_stressors["Plastic Pollution"]["Data Sources"] = ['* ROV surveys.', '* Sediment samples.', '**Impact on Area:** Pollution', '**Impact on Biodiversity:**', '* Ingestion by animals.', '* Potential toxic effects.', '**Influenced By (Stressors):**', '* Plastic production and disposal.', '**Influences (Stressors):**', '* Marine life.', '**Logic Description:** Plastics reach even remote seamounts.']
aquatic_seamounts_stressors["Plastic Pollution"]["Impact on Area"] = 'Pollution'
aquatic_seamounts_stressors["Plastic Pollution"]["Impact on Biodiversity"] = '* Ingestion by animals.\n* Potential toxic effects.\n**Influenced By (Stressors):**\n* Plastic production and disposal.\n**Influences (Stressors):**\n* Marine life.\n**Logic Description:** Plastics reach even remote seamounts.'
aquatic_seamounts_stressors["Plastic Pollution"]["Influenced By"] = ['* Plastic production and disposal.', '**Influences (Stressors):**', '* Marine life.', '**Logic Description:** Plastics reach even remote seamounts.']
aquatic_seamounts_stressors["Plastic Pollution"]["Influences"] = ['* Marine life.', '**Logic Description:** Plastics reach even remote seamounts.']
aquatic_seamounts_stressors["Plastic Pollution"]["Logic Description"] = '---'
aquatic_seamounts_stressors["Plastic Pollution"]["Impact Function"] = "impact_plastic_pollution_aquatic_seamounts"

