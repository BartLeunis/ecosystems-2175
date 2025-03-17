# stressor_interactions.py
import os
import importlib
# This dictionary will hold the interaction matrix.  It's initialized
# as an empty dictionary, and we'll populate it programmatically.
stressor_matrix = {}

# List of all ecosystems and stressors (we'll build this dynamically)
all_stressors = []

def initialize_interaction_matrix():
    """
    Initializes the stressor interaction matrix with all stressors and sets
    all interactions to 0 (no influence).  We'll populate the actual
    interactions later.
    """
    global stressor_matrix, all_stressors  # Access the global variables

    # 1.  Gather all stressors from all ecosystem files
    stressor_dir = "ecosystem_stressors"
    for filename in os.listdir(stressor_dir):
        if filename.endswith("_stressors.py"):
            ecosystem_name = filename.replace("_stressors.py", "").replace("_", " ").title()
            module_name = f"ecosystem_stressors.{filename[:-3]}"  # Remove '.py'
            try:
                module = importlib.import_module(module_name)
                stressor_dict = getattr(module, f"{ecosystem_name.lower().replace(' ', '_').replace('(', '').replace(')', '')}_stressors")

                for stressor_name in stressor_dict.keys():
                    full_stressor_name = f"{ecosystem_name} - {stressor_name}"
                    all_stressors.append(full_stressor_name)

            except Exception as e:
                print(f"ERROR: Could not load stressors for {ecosystem_name}: {e}")
                continue

    # 2. Create the matrix with initial values of 0
    for source_stressor in all_stressors:
        stressor_matrix[source_stressor] = {}
        for target_stressor in all_stressors:
            stressor_matrix[source_stressor][target_stressor] = 0 # No influence initially
            #Add a tuple, with (current impact, previous impact)
            #stressor_matrix[source_stressor][target_stressor] = (0,0)


# Call the initialization function to create the empty matrix
initialize_interaction_matrix()

# The matrix is now ready to be populated. We'll do that manually,
# ecosystem by ecosystem, using the "Influences" sections of the
# stressor descriptions.  For example:

# Example (you would NOT include this in the actual file,
# it's just to show how you'd populate it):
# stressor_matrix["Amazon Rainforest - Deforestation"]["Amazon Rainforest - Wildfires"] = 1
# stressor_matrix["Amazon Rainforest - Deforestation"]["Amazon Rainforest - Temperature Increase"] = 0.5
# ... and so on ...

# We will now create a populate_stressor_matrix.py script to automatically populate based on the stressors

# You can print the matrix (for debugging) to see its structure:
# import pprint
# pprint.pprint(stressor_matrix)
# print (all_stressors) #debug