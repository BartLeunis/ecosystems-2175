# create_ecosystem_files.py

import os

# List of ALL ecosystems (from your original list, plus the ones we've added)
ecosystems = [
    'Amazon Rainforest', 'Congo Rainforest', 'Southeast Asian Rainforest',
    'Great Barrier Reef', 'Mesoamerican Reef', 'Coral Triangle', 'Florida Keys Reefs', 'Caribbean Reefs', 'Red Sea Reefs',
    'Kelp Forests California', 'Kelp Forests Pacific Northwest', 'Kelp Forests Australian', 'Kelp Forests South American', 'Kelp Forests North Atlantic',
    'Mangroves', #General, will be overwritten.
    'Sundarbans', 'Mesoamerican Mangroves', 'Southeast Asian Mangroves', 'East African Mangroves','Australian Mangroves',
    'Salt Marshes', #General
    'North American Atlantic Coast Salt Marshes', 'Gulf of Mexico Salt Marshes', 'European Salt Marshes', 'Australian Salt Marshes',
    'Seagrasses', #General
    'Mediterranean Seagrass', 'Florida Bay/Gulf of Mexico Seagrass', 'Southeast Asian Seagrass', 'Australian Seagrass',
    'Open Ocean',  # General
    'Deep Sea', #General
    'Seamounts', 'Hydrothermal Vents', 'Cold-Water Corals', 'Abyssal Plains',
    'Lakes', #General
    'Great Lakes', 'Lake Baikal', 'African Great Lakes', 'Smaller Lakes and Ponds',
    'Rivers',  # General
    'Rivers Amazon', 'Rivers Mississippi', 'Rivers Yangtze', 'Rivers Danube', 'Rivers Murray-Darling',
    'Temperate Forests', #General
    'Appalachian Forests', 'Pacific Northwest Forests', 'European Temperate Forests', 'East Asian Temperate Forests', 'Chilean Temperate Rainforests',
    'Boreal Forests', #General
    'Canadian Boreal Forest', 'Russian Boreal Forest', 'Scandinavian and Finnish Boreal Forest',
    'Tundra', #General
    'Arctic Tundra', 'Alpine Tundra',
    'Deserts', #General
    'Sahara Desert', 'Arabian Desert', 'Gobi Desert', 'Australian Deserts', 'Kalahari Desert',
    'Namib Desert', 'Atacama Desert', 'Mojave Desert', 'Sonoran Desert', 'Chihuahuan Desert',
    'Grasslands', #General
    'North American Prairies', 'African Savannas', 'Eurasian Steppes', 'South American Pampas', 'Australian Grasslands',
    'Mountains', #General
    'Andes Montane', 'Himalayas Montane', 'Alps Montane', 'Rocky Mountains', 'Ethiopian Highlands',
    'Wetlands', #General
    'Everglades', 'Pantanal', 'Okavango Delta', 'Inner Niger Delta',
    'Urban Ecosystems', #New - to be populated.
    'Intensive Croplands', #New
    'Pastoral Lands', #New
    'Agroforestry',#New
    'Plantations',#New
    'Aquaculture' #New
]

# Create a directory to store the stressor files
stressor_dir = "ecosystem_stressors"
if not os.path.exists(stressor_dir):
    os.makedirs(stressor_dir)

# Loop and create empty .py files
for eco in ecosystems:
    filename = eco.lower().replace(" ", "_").replace("(", "").replace(")", "") + "_stressors.py"
    filepath = os.path.join(stressor_dir, filename)

    # Only create the file if it doesn't already exist
    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            f.write("from stressor_templates import *\n")
            f.write("import copy\n\n")
            f.write(f"{eco.lower().replace(' ', '_').replace('(', '').replace(')', '')}_stressors = {{\n")
            f.write("    # TODO: Populate this dictionary with stressors specific to this ecosystem,\n")
            f.write("    # using the templates from stressor_templates.py and modifying them as needed.\n")
            f.write("}\n")
        print(f"Created file: {filepath}")
    else:
        print(f"Skipping existing file: {filepath}")

print("Done creating ecosystem stressor files.")