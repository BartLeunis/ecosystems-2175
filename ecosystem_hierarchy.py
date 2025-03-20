# ecosystem_hierarchy.py
ecosystem_hierarchy = {
    "Forests": {
        "Tropical Rainforests": [
            "Amazon Rainforest",
            "Congo Rainforest",
            "Southeast Asian Rainforest",
            "Sundaland Rainforest",
            "New Guinea Rainforest",
            "Atlantic Forest",
            "Mesoamerican Forests"
        ],
        "Temperate Forests": [
            "Appalachian Temperate Forests",
            "Chilean Temperate Forests",
            "East Asian Temperate Forests",
            "European Temperate Forests",
            "Pacific Northwest Temperate Forests"
        ],
        "Boreal Forests": [
            "Canadian Boreal Forests",
            "Russian Boreal Forests",
            "Scandinavian and Finnish Boreal Forests"
        ]
    },
    "Grasslands and Savannas": {
        "Prairies": ["North American Prairies"],
        "Savannas": ["African Savannas", "South American Cerrado"],
        "Steppes": ["Eurasian Steppes"],
        "Pampas": ["South American Pampas"],
        "Grasslands": ["Australian Grasslands"]
    },
    "Mountains": [
        "Alps Mountains",
        "Andes Mountains",
        "Ethiopian Highlands Mountains",
        "Himalayas Mountains",
        "Rocky Mountains"
    ],
    "Tundra": [
        "Alpine Tundra",
        "Arctic Tundra"
    ],
    "Wetlands": {
        "Freshwater Wetlands": [
            "Camargue Wetlands",
            "Danube Delta Wetlands",
            "Everglades Wetlands",
            "Inner Niger Delta Wetlands",
            "Mesopotamian Marshes Wetlands",
            "Okavango Delta Wetlands",
            "Pantanal Wetlands"
        ],
        "Coastal Wetlands": ["Sundarbans Wetlands"]
    },
    "Deserts": [
        "Arabian Deserts",
        "Atacama Deserts",
        "Australian Deserts",
        "Chihuahuan Deserts",
        "Gobi Deserts",
        "Kalahari Deserts",
        "Mojave Deserts",
        "Namib Deserts",
        "Sahara Deserts",
        "Sonoran Deserts"
    ],
    "Agroecosystems": [
        "Agroforestry",
        "Aquaculture",
        "Intensive Croplands",
        "Pastoral Lands",
        "Plantations"
    ],
    "Urban": ["Urban Ecosystems"],
    "Marine and Aquatic": {
        "Coral Reefs": [
            "Great Barrier Reef",
            "Mesoamerican Reef",
            "Coral Triangle",
            "Florida Keys Reefs",
            "Caribbean Reefs",
            "Red Sea Reefs",
            "Cold-Water Corals"
        ],
        "Kelp Forests": [
            "Australian Kelp Forests",
            "California Kelp Forests",
            "North Atlantic Kelp Forests",
            "Pacific Northwest Kelp Forests",
            "South American Kelp Forests"
        ],
        "Mangroves": [
            "Australian Mangroves",
            "East African Mangroves",
            "Mesoamerican Mangroves",
            "Southeast Asian Mangroves",
            "Sundarbans Mangroves"
        ],
        "Salt Marshes": [
            "Australian Salt Marshes",
            "European Salt Marshes",
            "Gulf of Mexico Salt Marshes",
            "North American Atlantic Coast Salt Marshes",
            "San Francisco Bay Salt Marshes"
        ],
        "Seagrass Meadows": [
            "Australian Seagrass",
            "Florida Bay Seagrass",
            "Mediterranean Seagrass",
            "Southeast Asian Seagrass"
        ],
        "Open Ocean": [
            "Open Ocean",
            "Abyssal Plains",
            "Hydrothermal Vents",
            "Seamounts"
        ],
        "Freshwater Lakes": [
            "African Great Lakes",
            "Great Lakes",
            "Lake Baikal",
            "Smaller Lakes and Ponds"
        ],
        "Rivers": [
            "Amazon Rivers",
            "Danube Rivers",
            "Mississippi Rivers",
            "Murray-Darling Rivers",
            "Yangtze Rivers"
        ]
    }
}

def get_ecosystem_category(ecosystem_name):
    for top_level, sub_levels in ecosystem_hierarchy.items():
        if isinstance(sub_levels, list):
            if ecosystem_name in sub_levels:
                return top_level
        else:
            for sub_level, ecosystems in sub_levels.items():
                if ecosystem_name in ecosystems:
                    return f"{top_level} > {sub_level}"
    return None