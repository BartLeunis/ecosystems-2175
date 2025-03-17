# auto_populate_all_stressors.py

import os
import re
import copy
import importlib
import pandas as pd  # If you want to use the sanity check later
from stressor_templates import *

def parse_markdown_stressor(markdown_text):
    """Parses a Markdown stressor description into a dictionary."""
    stressor_dict = {}
    lines = markdown_text.strip().split("\n")

    # Extract the stressor name (Ecosystem is NOT extracted here)
    match = re.match(r"^### Stressor: (.*?)(?: \((.*?)\))?$", lines[0])
    if not match:
        return None  # Invalid header format
    stressor_dict["Stressor Name"] = match.group(1).strip()
    # Ecosystem is NOT extracted here; it's handled at a higher level

    # Extract other fields
    for line in lines[1:]:
        line = line.strip()
        if not line:
            continue

        if line.startswith("**Metric:**"):
            stressor_dict["Metric"] = line.replace("**Metric:**", "").strip()
        elif line.startswith("**Data Sources:**"):
            stressor_dict["Data Sources"] = [
                item.strip().replace("*   ", "") for item in lines[lines.index(line) + 1:] if item.strip().startswith("*")
            ]
        elif line.startswith("**Impact on Area:**"):
            stressor_dict["Impact on Area"] = line.replace("**Impact on Area:**", "").strip()
        elif line.startswith("**Impact on Biodiversity:**"):
            impact_lines = [item.strip().replace("*   ", "") for item in lines[lines.index(line) + 1:] if item.strip().startswith("*")]
            stressor_dict["Impact on Biodiversity"] = "\n".join(impact_lines)
        elif line.startswith("**Influenced By (Stressors):**"):
            stressor_dict["Influenced By"] = [
                item.strip().replace("*   ", "") for item in lines[lines.index(line) + 1:] if item.strip().startswith("*")
            ]
        elif line.startswith("**Influences (Stressors):**"):
            stressor_dict["Influences"] = [
                item.strip().replace("*   ", "") for item in lines[lines.index(line) + 1:] if item.strip().startswith("*")
            ]
        elif line.startswith("**Logic Description:**"):
            logic_start = lines.index(line) + 1
            logic_end = logic_start
            for i in range(logic_start, len(lines)):
                if lines[i].strip().startswith("**"):
                    logic_end = i
                    break
                else:
                    logic_end = len(lines)
            stressor_dict["Logic Description"] = "\n".join(lines[logic_start:logic_end]).strip()

    return stressor_dict



def process_markdown_files(docs_dir="docs", stressor_dir="ecosystem_stressors"):
    """Processes Markdown files, parsing stressors by ecosystem."""

    for filename in os.listdir(docs_dir):
        if filename.endswith(".md") and filename.startswith("Stressors_"):
            filepath = os.path.join(docs_dir, filename)
            print(f"Processing: {filename}")

            with open(filepath, "r") as f:
                markdown_content = f.read()

            # Extract Ecosystem Name from Filename
            ecosystem = filename[len("Stressors_"):-3].replace("_", " ")

            # Split by Stressor Heading (###) ONLY
            stressor_sections = re.split(r"(?m)^### Stressor:", markdown_content)
            stressor_sections = [s for s in stressor_sections if s.strip()]

            # Build the stressor dictionary IN MEMORY
            stressors_data = {}
            for stressor_section in stressor_sections:
                stressor_info = parse_markdown_stressor("### Stressor:" + stressor_section)
                if stressor_info:
                    # Add impact function name *here*
                    stressor_func_name = "impact_" + stressor_info["Stressor Name"].lower().replace(" ", "_").replace("-", "_") + "_" + ecosystem.lower().replace(" ", "_").replace("(", "").replace(")", "")
                    stressor_info["Impact Function"] = stressor_func_name

                    stressors_data[stressor_info["Stressor Name"]] = stressor_info


            # --- Create/Populate the Python File ---
            output_filename = ecosystem.lower().replace(" ", "_").replace("(", "").replace(")", "") + "_stressors.py"
            output_filepath = os.path.join(stressor_dir, output_filename)

            with open(output_filepath, "w") as f:
                f.write("from stressor_templates import *\n")
                f.write("import copy\n\n")
                var_name = ecosystem.lower().replace(' ', '_').replace('(', '').replace(')', '') + "_stressors"
                f.write(f"{var_name} = {{\n")

                for stressor_name, stressor_info in stressors_data.items():
                    template_name = None
                    # Determine which template to use
                    if "climate change" in stressor_name.lower() or "temperature increase" in stressor_name.lower() or "changes in precipitation" in stressor_name.lower():
                        template_name = "climate_change_template"
                    elif "deforestation" in stressor_name.lower():
                        template_name = "deforestation_template"
                    elif "infrastructure development" in stressor_name.lower():
                        template_name = "infrastructure_development_template"
                    elif "overfishing" in stressor_name.lower() or "Overfishing" in stressor_name.lower():
                        template_name = "overfishing_template"
                    elif "pollution" in stressor_name.lower() or "Pollution" in stressor_name.lower():
                        template_name = "pollution_template"
                    elif "invasive species" in stressor_name.lower() or "Invasive" in stressor_name.lower():
                        template_name = "invasive_species_template"
                    elif "water extraction" in stressor_name.lower() or "Water Extraction" in stressor_name.lower() or "Water Diversion" in stressor_name.lower() or "Water Withdrawals" in stressor_name.lower() :
                        template_name = "water_extraction_template"
                    elif "hydrology" in stressor_name.lower() or "Hydrology" in stressor_name.lower():
                        template_name = "altered_hydrology_template"
                    elif "wildfires" in stressor_name.lower() or "fire" in stressor_name.lower() or "Wildfires" in stressor_name.lower():
                        template_name = "fire_regime_template"
                    elif "Overgrazing" in stressor_name.lower():
                        template_name = "overgrazing_template"
                    elif "Permafrost Thaw" in stressor_name.lower():
                        template_name = "permafrost_thaw_template"
                    elif "Sea Ice Loss" in stressor_name.lower():
                        template_name = "sea_ice_loss_template"
                    elif "Land-Use Change" in stressor_name.lower():
                        template_name = "land_use_change_template"
                    elif "Poaching" in stressor_name.lower():
                        template_name = "poaching_template"
                    elif "Acidification" in stressor_name.lower():
                        template_name = "acidification_template"
                    elif "Mining" in stressor_name.lower():
                        template_name = "mining_template"
                    elif "Eutrophication" in stressor_name.lower():
                        template_name = "eutrophication_template"
                    elif "Fragmentation" in stressor_name.lower():
                        template_name = "fragmentation_template"
                    elif "Sedimentation" in stressor_name.lower():
                        template_name = "sedimentation_template"
                    # Add more template names as needed!

                    f.write(f'    "{stressor_name}": ')
                    if template_name:
                        f.write(f"copy.deepcopy({template_name}),\n")
                    else:
                        f.write("{},\n") # Create an empty dictionary if no template

                f.write("}\n\n")

                # Now, add the specific details for each stressor, correctly!
                for stressor_name, stressor_info in stressors_data.items():
                    f.write(f'# --- {stressor_name} ---\n')
                    for key, value in stressor_info.items():
                        if key == "Impact Function":
                            f.write(f'{var_name}["{stressor_name}"]["{key}"] = "{stressor_info[key]}"\n')
                        elif key not in ["Stressor Name", "Ecosystem"]:
                            f.write(f'{var_name}["{stressor_name}"]["{key}"] = {repr(value)}\n')
                    f.write("\n")


            print(f"Populated file: {filepath}")


def main():
    docs_dir = "docs"
    stressor_dir = "ecosystem_stressors"

    if not os.path.exists(stressor_dir):
        os.makedirs(stressor_dir)

    process_markdown_files(docs_dir, stressor_dir)
    print("Finished processing all Markdown files.")


if __name__ == "__main__":
    main()