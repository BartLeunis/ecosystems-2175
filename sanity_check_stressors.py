# sanity_check_stressors.py

import os
import importlib
import pandas as pd
from ecosystem_parameters import ecosystems, ecosystem_areas, biodiversity_density_ratios, initial_biodiversity
from simulation_parameters import final_baselines, original_consensus_loss, adjusted_loss_potentials, transform_targets, cascade_effects, logistic_params
from stressor_templates import *  # Import all templates

def check_stressor_structure(stressor_dict, stressor_name, ecosystem_name):
    """Checks if a stressor dictionary has the expected keys."""
    expected_keys = [
        "Metric", "Data Sources", "Impact on Area", "Impact on Biodiversity",
        "Influenced By", "Influences", "Logic Description", "Impact Function"
    ]
    missing_keys = [key for key in expected_keys if key not in stressor_dict]
    if missing_keys:
        print(f"WARNING: Stressor '{stressor_name}' in ecosystem '{ecosystem_name}' is missing keys: {missing_keys}")
        return False
    return True

def check_template_usage(stressor_dict, stressor_name, ecosystem_name, templates):
    """Checks if a stressor dictionary is based on a template."""
    if "Impact Function" not in stressor_dict:
      return

    if not stressor_dict["Impact Function"].startswith("impact_"):
        print(f"WARNING: Stressor '{stressor_name}' in ecosystem '{ecosystem_name}' does not have a valid impact function.")
        return False

    return True #We'll assume that if an impact function exists, it's been copied correctly.

def main():
    stressor_dir = "ecosystem_stressors"
    templates = importlib.import_module("stressor_templates")

    all_stressors = {}  # Accumulate all stressor data

    # --- Load all ecosystem stressor files ---
    for filename in os.listdir(stressor_dir):
        if filename.endswith("_stressors.py"):
            ecosystem_name = filename.replace("_stressors.py", "").replace("_", " ").title()
            module_name = f"ecosystem_stressors.{filename[:-3]}"  # Remove '.py'
            try:
                module = importlib.import_module(module_name)
                stressor_dict = getattr(module, f"{ecosystem_name.lower().replace(' ', '_').replace('(', '').replace(')', '')}_stressors")
                all_stressors[ecosystem_name] = stressor_dict
            except Exception as e:
                print(f"ERROR: Could not load stressors for {ecosystem_name}: {e}")
                continue


    # --- Perform checks ---
    for ecosystem_name, stressors in all_stressors.items():
        for stressor_name, stressor_data in stressors.items():
            check_stressor_structure(stressor_data, stressor_name, ecosystem_name)
            check_template_usage(stressor_data, stressor_name, ecosystem_name, templates)

    # --- Create summary tables ---
    print("\n--- Summary Tables ---")

    #Load Parameters
    import ecosystem_parameters
    import simulation_parameters

    # Example 1: Ecosystem Parameters - Areas
    area_data = {eco: [area] for eco, area in ecosystem_parameters.ecosystem_areas.items()}  # Access via module
    df_area = pd.DataFrame.from_dict(area_data, orient='index', columns=['Area'])
    print("\nEcosystem Areas:")
    print(df_area)
    total_area = df_area['Area'].sum()
    if not (0.999 < total_area < 1.001): #Allow for tiny rounding errors.
        print(f"WARNING: Ecosystem areas sum to {total_area}, not 1.0")
    if (df_area['Area']<0).any() or (df_area['Area']>1).any():
        print("WARNING: Ecosystem areas contains values outside of [0,1] range")


    # Example 2: Ecosystem Parameters - Biodiversity Density
    density_data = {eco: [density] for eco, density in ecosystem_parameters.biodiversity_density_ratios.items()}  # Access via module
    df_density = pd.DataFrame.from_dict(density_data, orient='index', columns=['Density Ratio'])
    print("\nBiodiversity Density Ratios:")
    print(df_density)
    if (df_density['Density Ratio']<0).any():
        print("WARNING: Biodiversity Density Ratios contains values outside of [0,inf) range")

     # Example 3: Initial Biodiversity
    initial_bio_data = {eco: [bio] for eco, bio in ecosystem_parameters.initial_biodiversity.items()}  # Access via module
    df_initial_bio = pd.DataFrame.from_dict(initial_bio_data, orient='index', columns=['Initial Biodiversity'])
    print("\nInitial Biodiversity:")
    print(df_initial_bio)
    total_initial_bio = df_initial_bio['Initial Biodiversity'].sum()
    print(f"Total initial biodiversity: {total_initial_bio}") #Report the sum
    if (df_initial_bio['Initial Biodiversity']<0).any():
        print("WARNING: Initial Biodiversity contains values outside of [0,inf) range")


    # Example 4: Simulation Parameters - final_baselines
    baseline_data = {eco: [baseline] for eco, baseline in simulation_parameters.final_baselines.items()}  # Access via module
    df_baseline = pd.DataFrame.from_dict(baseline_data, orient='index', columns=['Final Baseline'])
    print("\nFinal Baselines:")
    print(df_baseline)
    if (df_baseline['Final Baseline']<0).any() or (df_baseline['Final Baseline']>1).any():
        print("WARNING: Final Baselines contains values outside of [0,1] range")

    #Example 5: original_consensus_loss
    #This one is a bit trickier, as it is a nested dict.

    #Find the maximum length of sub-dictionaries:
    max_len = 0
    for eco, loss_data in simulation_parameters.original_consensus_loss.items():  # Access via module
        if len(loss_data) > max_len:
            max_len = len(loss_data)

    consensus_loss_data = {}
    for eco, loss_data in simulation_parameters.original_consensus_loss.items():  # Access via module
        years = []
        losses = []
        for year,loss in loss_data.items():
            years.append(year)
            losses.append(loss)
        #Pad with None if less than max length:
        while len(losses) < max_len:
            losses.append(None)
        consensus_loss_data[eco] = losses

    df_consensus_loss = pd.DataFrame.from_dict(consensus_loss_data, orient = 'index', columns = list(simulation_parameters.original_consensus_loss.items())[0][1].keys())  # Access via module
    print("\nConsensus Loss:")
    print(df_consensus_loss)
    if (df_consensus_loss.values<0).any() or (df_consensus_loss.values>100).any():
        print("WARNING: original_consensus_loss contains values outside of [0,100] range")

    #Example 6: adjusted_loss_potentials. Very similar to example 5.

    #Find the maximum length of sub-dictionaries:
    max_len = 0
    for eco, loss_data in simulation_parameters.adjusted_loss_potentials.items():  # Access via module
        if len(loss_data) > max_len:
            max_len = len(loss_data)

    adjusted_loss_data = {}
    for eco, loss_data in simulation_parameters.adjusted_loss_potentials.items():  # Access via module
        years = []
        losses = []
        for year,loss in loss_data.items():
            years.append(year)
            losses.append(loss)
        #Pad with None if less than max length:
        while len(losses) < max_len:
            losses.append(None)
        adjusted_loss_data[eco] = losses
    df_adjusted_loss = pd.DataFrame.from_dict(adjusted_loss_data, orient = 'index', columns = list(simulation_parameters.adjusted_loss_potentials.items())[0][1].keys())  # Access via module
    print("\nAdjusted Loss Potential:")
    print(df_adjusted_loss)
    if ((df_adjusted_loss.values<0).any()) or ((df_adjusted_loss.values>100).any()):
        print("WARNING: adjusted_loss_potentials contains values outside of [0,100] range")

    #Example 7: logistic parameters
    #Find max length of sub-dictionaries
    max_len = 0
    for eco, scenario_data in simulation_parameters.logistic_params.items():  # Access via module
        for scenario, k_val in scenario_data.items():
            if isinstance(k_val, dict):
                if len(k_val) > max_len:
                    max_len = len(k_val)

    logistic_data = {}
    for eco, scenario_data in simulation_parameters.logistic_params.items():  # Access via module
        k_values = []
        for scenario, k_val in scenario_data.items():
            if isinstance(k_val, dict):
                k_values.append(k_val['Mid'])  # Extract the 'Mid' value.  This assumes it exists!
            else:
                k_values.append(None) #Should not happen, kept for safety
        while len(k_values) < max_len:
            k_values.append(None)
        logistic_data[eco] = k_values


    df_logistic = pd.DataFrame.from_dict(logistic_data, orient='index', columns=['k_Mid'])
    print("\nLogistic Parameters (k, Mid Scenario):")
    print(df_logistic)
    if (df_logistic['k_Mid']<0).any():
        print("WARNING: logistic parameters contains values outside of [0,inf) range")
    #Example 8: Transform Targets
    transform_targets_data = {eco: [target] if target else ["None"] for eco, target in simulation_parameters.transform_targets.items() }  # Access via module, Handle None
    df_transform = pd.DataFrame.from_dict(transform_targets_data, orient = 'index', columns = ['Target Ecosystem'])
    print("\nTransformation Targets:")
    print(df_transform)
    #Check if all targets actually are ecosystems:
    all_ecosystems = set(ecosystem_parameters.ecosystems) # Access via the module
    for target in df_transform['Target Ecosystem']:
        if target != "None" and target not in all_ecosystems:
            print(f"WARNING: Transform target '{target}' is not a valid ecosystem.")

    #Example 9: Cascade Effects:
    #This is the trickiest, because we have a dict of dicts.
    cascade_data = {}
    for source_eco, target_data in simulation_parameters.cascade_effects.items():  # Access via module
      target_list = []
      multiplier_list = []
      for target_eco, multiplier in target_data.items():
        target_list.append(target_eco)
        multiplier_list.append(multiplier)
      cascade_data[source_eco] = [", ".join(target_list), ", ".join([str(x) for x in multiplier_list])] #Join targets into single strings.
    df_cascade = pd.DataFrame.from_dict(cascade_data, orient = 'index', columns = ['Target Ecosystems', 'Multipliers'])
    print("\nCascade Effects:")
    print(df_cascade)
    #Check that all targets are valid ecosystems
    for targets in df_cascade['Target Ecosystems']:
        for target in targets.split(", "):
            if target not in all_ecosystems:
                print(f"WARNING: Cascade target '{target}' is not a valid ecosystem.")
    for mult_str in df_cascade['Multipliers']:
        for mult in mult_str.split(", "):
            try:
                val = float(mult)
                if val < 0:
                    print (f"WARNING: Negative multiplier found: {val}")
            except:
                print(f"WARNING: Could not parse multiplier {mult}")

if __name__ == "__main__":
    main()