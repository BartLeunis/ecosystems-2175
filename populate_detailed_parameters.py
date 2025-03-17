# populate_detailed_parameters.py

import os
import importlib
import shutil
from sub_ecosystem_areas import sub_ecosystem_areas  # Import the new dictionary

def create_detailed_parameter_files(original_eco_params, original_sim_params, detailed_eco_params, detailed_sim_params):
    """Copies and renames the original parameter files to create detailed versions."""

    shutil.copyfile(original_eco_params, detailed_eco_params)
    shutil.copyfile(original_sim_params, detailed_sim_params)
    print(f"Created detailed parameter files: {detailed_eco_params}, {detailed_sim_params}")

def load_stressor_data(stressor_dir="ecosystem_stressors"):
    """Loads stressor data from individual ecosystem files.  We don't actually need this
      to *get* the area anymore, but we still need to know *which* stressors exist
      so we can create entries for them."""
    all_stressors = {}
    for filename in os.listdir(stressor_dir):
        if filename.endswith("_stressors.py"):
            ecosystem_name = filename.replace("_stressors.py", "").replace("_", " ").title()
            module_name = f"ecosystem_stressors.{filename[:-3]}"
            try:
                module = importlib.import_module(module_name)
                stressor_dict = getattr(module, f"{ecosystem_name.lower().replace(' ', '_').replace('(', '').replace(')', '')}_stressors")
                all_stressors[ecosystem_name] = stressor_dict #We just need the names.
            except Exception as e:
                print(f"ERROR: Could not load stressors for {ecosystem_name}: {e}")
                continue
    return all_stressors

def populate_detailed_parameters(stressor_data, original_eco_params, original_sim_params, detailed_eco_params, detailed_sim_params):
    """Populates the detailed parameter files with data from stressors and original params."""

    # --- Load Original Parameters ---
    original_eco = importlib.import_module(original_eco_params.replace(".py", ""))
    original_sim = importlib.import_module(original_sim_params.replace(".py", ""))

    # --- Mapping Dictionary (CRITICAL) ---
    ecosystem_mapping = {
        "Boreal Forests": "Forests",
        "Temperate Forests": "Forests",
        "Rainforests": "Forests",
        "Freshwater Rivers And Streams": "Freshwater",
        "Freshwater Lakes And Ponds": "Freshwater",
        "Salt Marshes And Estuaries": "Aquatic",
        "Seagrass": "Aquatic",
        "Mangrove": "Aquatic",
        "Kelp Forests": "Aquatic",
        "Coral Reefs": "Aquatic",
        "Pelagic (Open Ocean)": "Aquatic",
        "Deep Sea": "Aquatic",
        "Grasslands": "Grasslands",
        "Tundra": "Tundra",
        "Deserts": "Deserts",
        "Mountains": "Mountains",
        "Wetlands": "Wetlands"
    }

    # --- Prepare New Parameter Dictionaries ---
    detailed_eco_data = {
        "ecosystems": [],
        "ecosystem_areas": {},
        "biodiversity_density_ratios": {},
        "initial_biodiversity": {},
    }
    detailed_sim_data = {
        "final_baselines": {},
        "original_consensus_loss": {},
        "adjusted_loss_potentials": {},
        "transform_targets": {},
        "cascade_effects": {},
        "logistic_params": {},
    }

    # --- Populate Detailed Parameters ---
    #for sub_ecosystem, data in stressor_data.items(): #We don't get data from here anymore
    for sub_ecosystem in stressor_data:  # Iterate through the *names* of the stressors.
        original_ecosystem = ecosystem_mapping[sub_ecosystem]

        # --- Ecosystem Parameters ---
        detailed_eco_data["ecosystems"].append(sub_ecosystem)
        detailed_eco_data["ecosystem_areas"][sub_ecosystem] = sub_ecosystem_areas[sub_ecosystem]  # Get area from sub_ecosystem_areas.py
        detailed_eco_data["biodiversity_density_ratios"][sub_ecosystem] = original_eco.biodiversity_density_ratios[original_ecosystem]  # Copy
        detailed_eco_data["initial_biodiversity"][sub_ecosystem] = original_eco.initial_biodiversity[original_ecosystem] * sub_ecosystem_areas[sub_ecosystem] / original_eco.ecosystem_areas[original_ecosystem] # Scale initial bio

        # --- Simulation Parameters ---
        detailed_sim_data["final_baselines"][sub_ecosystem] = original_sim.final_baselines[original_ecosystem]  # Copy
        detailed_sim_data["original_consensus_loss"][sub_ecosystem] = original_sim.original_consensus_loss[original_ecosystem] #Copy
        detailed_sim_data["adjusted_loss_potentials"][sub_ecosystem] = original_sim.adjusted_loss_potentials[original_ecosystem]  # Copy

        #transform targets
        if original_ecosystem in original_sim.transform_targets:
            if original_sim.transform_targets[original_ecosystem] is not None:
                # Find the sub-ecosystem that corresponds to the original transform target
                for sub_eco, orig_eco in ecosystem_mapping.items():
                    if orig_eco == original_sim.transform_targets[original_ecosystem]:
                        detailed_sim_data["transform_targets"][sub_ecosystem] = sub_eco
                        break  # Assuming only one sub-eco maps to a target
            else:
                detailed_sim_data["transform_targets"][sub_ecosystem] = None
        else:
          detailed_sim_data["transform_targets"][sub_ecosystem] = None #Explicitly state None

        # Cascade Effects
        if original_ecosystem in original_sim.cascade_effects:
            detailed_sim_data["cascade_effects"][sub_ecosystem] = {}  # Initialize
            for target_eco, multiplier in original_sim.cascade_effects[original_ecosystem].items():
                 # Find the sub-ecosystem that corresponds to the original cascade target
                for sub_eco, orig_eco in ecosystem_mapping.items():
                    if orig_eco == target_eco:
                        detailed_sim_data["cascade_effects"][sub_ecosystem][sub_eco] = multiplier
                        break
        else:
            detailed_sim_data["cascade_effects"][sub_ecosystem] = {} #Ensure it exists, even if empty.

        detailed_sim_data["logistic_params"][sub_ecosystem] = original_sim.logistic_params[original_ecosystem]  # Copy
    # --- Write to Files ---
    with open(detailed_eco_params, "w") as f:
        f.write("ecosystems = " + repr(detailed_eco_data["ecosystems"]) + "\n")
        f.write("ecosystem_areas = " + repr(detailed_eco_data["ecosystem_areas"]) + "\n")
        f.write("biodiversity_density_ratios = " + repr(detailed_eco_data["biodiversity_density_ratios"]) + "\n")
        f.write("initial_biodiversity = " + repr(detailed_eco_data["initial_biodiversity"]) + "\n")

    with open(detailed_sim_params, "w") as f:
        f.write("final_baselines = " + repr(detailed_sim_data["final_baselines"]) + "\n")
        f.write("original_consensus_loss = " + repr(detailed_sim_data["original_consensus_loss"]) + "\n")
        f.write("adjusted_loss_potentials = " + repr(detailed_sim_data["adjusted_loss_potentials"]) + "\n")
        f.write("transform_targets = " + repr(detailed_sim_data["transform_targets"]) + "\n")
        f.write("cascade_effects = " + repr(detailed_sim_data["cascade_effects"]) + "\n")
        f.write("logistic_params = " + repr(detailed_sim_data["logistic_params"]) + "\n")

    print(f"Populated detailed parameters in: {detailed_eco_params}, {detailed_sim_params}")

def main():
    original_eco_params = "ecosystem_parameters.py"
    original_sim_params = "simulation_parameters.py"
    detailed_eco_params = "ecosystem_parameters_detailed.py"
    detailed_sim_params = "simulation_parameters_detailed.py"

    # 1. Create new, empty parameter files.
    create_detailed_parameter_files(original_eco_params, original_sim_params, detailed_eco_params, detailed_sim_params)

    # 2. Load stressor data (we just need the names, not the areas).
    stressor_data = load_stressor_data()

    # 3. Populate the new files.
    populate_detailed_parameters(stressor_data, original_eco_params, original_sim_params, detailed_eco_params, detailed_sim_params)

if __name__ == "__main__":
    main()