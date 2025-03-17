# sub_ecosystem_areas.py

# This dictionary defines the area (as a fraction of the total simulation area)
# for each *sub-ecosystem*.  THESE VALUES ARE ALL PLACEHOLDERS.
# YOU MUST REPLACE THEM WITH YOUR ACTUAL DATA.

sub_ecosystem_areas = {
    # Rainforests
    "Amazon Rainforest": 0.03,  # Example: 3% of total area
    "Congo Rainforest": 0.01,   # Example
    "Southeast Asian Rainforest": 0.01, # Example
    'Sundaland Rainforest': 0.01, # Example
    'New Guinea Rainforest': 0.005, #Example
    'Atlantic Forest': 0.003, #Example
    'Mesoamerican Forests': 0.002, #Example

    # Coral Reefs
    "Great Barrier Reef": 0.0002, # Example
    "Mesoamerican Reef": 0.0001, # Example
    "Coral Triangle": 0.0003, # Example
    "Florida Keys Reefs": 0.00005, # Example
    "Caribbean Reefs": 0.0001,  # Example
    "Red Sea Reefs": 0.00005, # Example

    # Kelp Forests
    "California Kelp Forests": 0.0001, # Example
    "Pacific Northwest Kelp Forests": 0.0001, # Example
    "Australian Kelp Forests": 0.0001,  # Example
    "South American Kelp Forests": 0.00005, # Example
    "North Atlantic Kelp Forests": 0.00005, #Example

    # Temperate Forests
    "Appalachian Forests": 0.002,   # Example
    "Pacific Northwest Forests": 0.002,  # Example
    "European Temperate Forests": 0.002, # Example
    "East Asian Temperate Forests": 0.001, # Example
    "Chilean Temperate Rainforests": 0.001, # Example

    # Boreal Forests
    "Canadian Boreal Forest": 0.01,  # Example
    "Russian Boreal Forest": 0.015,  # Example
    "Scandinavian and Finnish Boreal Forest": 0.004, # Example

    # Tundra
    "Arctic Tundra": 0.03, # Example
    "Alpine Tundra": 0.005, # Example

    # Grasslands
     "North American Prairies": 0.004, #Example
     "African Savannas": 0.04, #Example
     "Eurasian Steppes": 0.003, #Example
     "South American Cerrado": 0.003, #Example
     "Australian Savanna": 0.001, #Example
     "Pampas": 0.002, #Example

    # Wetlands
    "Everglades": 0.0005,  # Example
    "Pantanal": 0.0015, # Example
    "Okavango Delta": 0.0008, # Example
    "Inner Niger Delta": 0.0005, # Example
    "Sundarbans": 0.0004, # Example
     "Mesopotamian Marshes": 0.0003, # Example
    "Camargue": 0.0001, # Example
    "Danube Delta": 0.0002, # Example

    # Freshwater Lakes
     "Great Lakes": 0.004, #Example
     "Lake Baikal": 0.003, #Example
     "African Great Lakes": 0.005, #Example
     "Smaller Lakes and Ponds": 0.008, #Example

    # Rivers and Streams
      "Rivers Amazon": 0.001, #Example
      "Rivers Mississippi": 0.0002, #Example
      "Rivers Yangtze": 0.0003, #Example
      "Rivers Danube": 0.0002, #Example
      "Rivers Murray Darling": 0.0001, #Example

    # Deep Sea
    "Seamounts": 0.01,  # Example
    "Hydrothermal Vents": 0.0001, # Example
    "Cold-Water Corals": 0.001,  # Example
    "Abyssal Plains": 0.15,       # Example

    # Mangroves
 	"Sundarbans": 0.0003, #Example
 	"Mesoamerican Mangroves": 0.0001, #Example
	"Southeast Asian Mangroves": 0.0002, #Example
	"East African Mangroves": 0.0001, #Example
	"Australian Mangroves": 0.0001, #Example

    # Salt Marshes
       "North American Atlantic Coast Salt Marshes": 0.0002, #Example
       "Gulf of Mexico Salt Marshes": 0.0001, #Example
       "European Salt Marshes": 0.0001, #Example
        "Australian Salt Marshes": 0.0001, #Example
        "San Francisco Bay Salt Marshes": 0.00005, #Example
    # Seagrass
        "Mediterranean Seagrass": 0.0001,
        "Florida Bay": 0.0001,
        "Southeast Asian Seagrass": 0.0001,
        "Australian Seagrass": 0.0001,
    # Deserts
        "Sahara Desert": 0.02,
        "Arabian Desert": 0.005,
        "Gobi Desert": 0.001,
        "Australian Deserts": 0.008,
        "Kalahari Desert": 0.001,
        "Namib Desert": 0.0005,
        "Atacama Desert": 0.0001,
        "Mojave Desert": 0.0002,
        "Sonoran Desert": 0.0003,
        "Chihuahuan Desert": 0.0004,
    # Mountains
        "Andes Montane": 0.002,
        "Himalayas Montane": 0.0015,
        "Alps Montane": 0.0005,
        "Rocky Mountains": 0.002,
        "Ethiopian Highlands": 0.0008,
    # Open Ocean,
        "Pelagic (Open Ocean)": 0.30,
    # Anthropogenic
        "Urban Ecosystems": 0.005,
        "Intensive Croplands": 0.02,
        "Pastoral Lands": 0.01,
        "Agroforestry": 0.004,
        "Plantations": 0.008,
        "Aquaculture": 0.001
}

# Add a check to make sure it adds up to 1.0:
total_area = sum(sub_ecosystem_areas.values())
if not (0.999 < total_area < 1.001):
  print (f"WARNING. Areas in sub_ecosystem_areas.py add up to {total_area}, not 1")