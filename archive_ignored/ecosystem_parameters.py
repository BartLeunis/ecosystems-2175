# ecosystem_parameters.py

# Define the detailed list of ecosystems (41 ecosystems from prior work)
ecosystems = [
    'Amazon Rainforest', 'Congo Rainforest', 'Southeast Asian Rainforest',
    'Coral Reefs', 'Atlantic Ocean', 'Pacific Ocean', 'Southern Ocean',
    'Arctic Sea Ice', 'Arctic Polar', 'Antarctic Polar',
    'Boreal Forests', 'African Savanna', 'South American Cerrado',
    'Australian Savanna', 'Tropical Peatlands', 'Temperate Marshes',
    'Mangroves', 'North American Temperate Forests',
    'European Temperate Forests', 'East Asian Temperate Forests',
    'Sahara Desert', 'Gobi Desert', 'Atacama Desert',
    'Arctic Tundra', 'Alpine Tundra', 'Andes Montane',
    'Himalayas Montane', 'Alps Montane', 'Lakes', 'Rivers', 'Deltas',
    'North American Prairies', 'Eurasian Steppes', 'Pampas',
    'Seagrasses', 'Kelp Forests', 'Urban Ecosystems',
    'Intensive Croplands', 'Pastoral Lands', 'Agroforestry',
    'Plantations', 'Aquaculture'
]

# Real-world areas (in km², approximate based on literature)
real_world_areas_km2 = {
    'Amazon Rainforest': 5_500_000,  # WWF estimates
    'Congo Rainforest': 1_800_000,
    'Southeast Asian Rainforest': 1_200_000,
    'Coral Reefs': 284_300,  # Global coral reef area
    'Atlantic Ocean': 106_400_000,
    'Pacific Ocean': 155_600_000,
    'Southern Ocean': 20_300_000,
    'Arctic Sea Ice': 14_000_000,  # Average extent
    'Arctic Polar': 5_000_000,
    'Antarctic Polar': 14_000_000,
    'Boreal Forests': 12_000_000,
    'African Savanna': 13_000_000,
    'South American Cerrado': 2_000_000,
    'Australian Savanna': 1_900_000,
    'Tropical Peatlands': 441_000,
    'Temperate Marshes': 300_000,
    'Mangroves': 150_000,
    'North American Temperate Forests': 2_500_000,
    'European Temperate Forests': 1_000_000,
    'East Asian Temperate Forests': 800_000,
    'Sahara Desert': 9_200_000,
    'Gobi Desert': 1_300_000,
    'Atacama Desert': 105_000,
    'Arctic Tundra': 5_000_000,
    'Alpine Tundra': 1_000_000,
    'Andes Montane': 500_000,
    'Himalayas Montane': 400_000,
    'Alps Montane': 200_000,
    'Lakes': 2_500_000,  # Global freshwater lakes
    'Rivers': 500_000,  # Estimated riverine area
    'Deltas': 300_000,
    'North American Prairies': 1_400_000,
    'Eurasian Steppes': 3_000_000,
    'Pampas': 750_000,
    'Seagrasses': 300_000,
    'Kelp Forests': 200_000,
    'Urban Ecosystems': 1_000_000,  # Estimated urban land
    'Intensive Croplands': 15_000_000,
    'Pastoral Lands': 5_000_000,
    'Agroforestry': 1_000_000,
    'Plantations': 2_000_000,
    'Aquaculture': 500_000
}

# Compute normalized areas (summing to 1.0)
total_area_km2 = sum(real_world_areas_km2.values())
ecosystem_areas = {eco: area / total_area_km2 for eco, area in real_world_areas_km2.items()}

# Real-world biodiversity densities (vertebrate species/km², approximate based on literature)
real_world_biodiversity_density = {
    'Amazon Rainforest': 50,  # High biodiversity, ~400 bird species per 100 km²
    'Congo Rainforest': 45,
    'Southeast Asian Rainforest': 40,
    'Coral Reefs': 40,  # High marine biodiversity
    'Atlantic Ocean': 2,
    'Pacific Ocean': 2,
    'Southern Ocean': 1,
    'Arctic Sea Ice': 1,
    'Arctic Polar': 1,
    'Antarctic Polar': 1,
    'Boreal Forests': 10,
    'African Savanna': 25,
    'South American Cerrado': 20,
    'Australian Savanna': 20,
    'Tropical Peatlands': 30,
    'Temperate Marshes': 25,
    'Mangroves': 30,
    'North American Temperate Forests': 20,
    'European Temperate Forests': 15,
    'East Asian Temperate Forests': 15,
    'Sahara Desert': 1,
    'Gobi Desert': 1,
    'Atacama Desert': 0.5,
    'Arctic Tundra': 3,
    'Alpine Tundra': 3,
    'Andes Montane': 15,
    'Himalayas Montane': 15,
    'Alps Montane': 10,
    'Lakes': 20,
    'Rivers': 20,
    'Deltas': 25,
    'North American Prairies': 15,
    'Eurasian Steppes': 10,
    'Pampas': 15,
    'Seagrasses': 15,
    'Kelp Forests': 15,
    'Urban Ecosystems': 5,
    'Intensive Croplands': 3,
    'Pastoral Lands': 8,
    'Agroforestry': 8,
    'Plantations': 3,
    'Aquaculture': 2
}

# Compute biodiversity density ratios (relative to Temperate Forests as baseline = 1.0)
baseline_density = real_world_biodiversity_density['North American Temperate Forests']  # 20 species/km²
biodiversity_density_ratios = {eco: density / baseline_density for eco, density in real_world_biodiversity_density.items()}

# Compute initial biodiversity (area * density ratio, in relative units)
initial_biodiversity = {eco: ecosystem_areas[eco] * biodiversity_density_ratios[eco] for eco in ecosystems}