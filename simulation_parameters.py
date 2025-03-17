# simulation_parameters.py
from ecosystem_parameters import ecosystems  # Import ecosystems at the top

# Define final baselines (remaining biodiversity fraction)
final_baselines = {
    'Amazon Rainforest': 0.05, 'Congo Rainforest': 0.05, 'Southeast Asian Rainforest': 0.05,
    'Coral Reefs': 0.03, 'Atlantic Ocean': 0.10, 'Pacific Ocean': 0.10, 'Southern Ocean': 0.10,
    'Arctic Sea Ice': 0.05, 'Arctic Polar': 0.10, 'Antarctic Polar': 0.10,
    'Boreal Forests': 0.10, 'African Savanna': 0.15, 'South American Cerrado': 0.15,
    'Australian Savanna': 0.15, 'Tropical Peatlands': 0.20, 'Temperate Marshes': 0.20,
    'Mangroves': 0.20, 'North American Temperate Forests': 0.15,
    'European Temperate Forests': 0.15, 'East Asian Temperate Forests': 0.15,
    'Sahara Desert': 0.50, 'Gobi Desert': 0.50, 'Atacama Desert': 0.50,
    'Arctic Tundra': 0.10, 'Alpine Tundra': 0.10, 'Andes Montane': 0.15,
    'Himalayas Montane': 0.15, 'Alps Montane': 0.15, 'Lakes': 0.10,
    'Rivers': 0.10, 'Deltas': 0.10, 'North American Prairies': 0.15,
    'Eurasian Steppes': 0.15, 'Pampas': 0.15, 'Seagrasses': 0.10,
    'Kelp Forests': 0.10, 'Urban Ecosystems': 0.30,
    'Intensive Croplands': 0.30, 'Pastoral Lands': 0.20, 'Agroforestry': 0.20,
    'Plantations': 0.30, 'Aquaculture': 0.30
}

# Define original consensus loss percentages
original_consensus_loss = {
    eco: {'2050': 20, '2100': 50, '2175': 75} if 'Rainforest' in eco else
         {'2050': 50, '2100': 80, '2175': 92} if eco == 'Coral Reefs' else
         {'2050': 80, '2100': 85, '2175': 90} if eco == 'Arctic Sea Ice' else
         {'2050': 20, '2100': 40, '2175': 60} if eco == 'Boreal Forests' else
         {'2050': 5, '2100': 20, '2175': 45} if 'Savanna' in eco or 'Prairies' in eco or 'Steppes' in eco or 'Pampas' in eco else
         {'2050': 20, '2100': 50, '2175': 70} if 'Wetlands' in eco or 'Peatlands' in eco or 'Marshes' in eco or 'Mangroves' in eco else
         {'2050': 30, '2100': 60, '2175': 80} if 'Ocean' in eco or eco in ['Lakes', 'Rivers', 'Deltas'] else
         {'2050': 15, '2100': 35, '2175': 50} if 'Temperate Forests' in eco else
         {'2050': 5, '2100': 15, '2175': 25} if 'Desert' in eco else
         {'2050': 25, '2100': 50, '2175': 70} if 'Tundra' in eco else
         {'2050': 15, '2100': 40, '2175': 60} if 'Montane' in eco else
         {'2050': 30, '2100': 60, '2175': 80} for eco in ecosystems
}

# Define adjusted loss potentials
adjusted_loss_potentials = {
    eco: {'2050': original_consensus_loss[eco]['2050'], '2100': original_consensus_loss[eco]['2100'], '2175': min(95, original_consensus_loss[eco]['2175'] + 15)} for eco in ecosystems
}

# Define transform targets
transform_targets = {
    'Amazon Rainforest': 'South American Cerrado',
    'Congo Rainforest': 'African Savanna',
    'Southeast Asian Rainforest': 'Plantations',
    'Coral Reefs': 'Atlantic Ocean',
    'Atlantic Ocean': None,
    'Pacific Ocean': None,
    'Southern Ocean': None,
    'Arctic Sea Ice': 'Arctic Polar',
    'Arctic Polar': None,
    'Antarctic Polar': None,
    'Boreal Forests': 'North American Prairies',
    'African Savanna': 'Sahara Desert',
    'South American Cerrado': 'Intensive Croplands',
    'Australian Savanna': 'Pastoral Lands',
    'Tropical Peatlands': 'Plantations',
    'Temperate Marshes': 'Intensive Croplands',
    'Mangroves': 'Aquaculture',
    'North American Temperate Forests': 'Urban Ecosystems',
    'European Temperate Forests': 'Intensive Croplands',
    'East Asian Temperate Forests': 'Urban Ecosystems',
    'Sahara Desert': None,
    'Gobi Desert': None,
    'Atacama Desert': None,
    'Arctic Tundra': 'Alpine Tundra',
    'Alpine Tundra': None,
    'Andes Montane': None,
    'Himalayas Montane': None,
    'Alps Montane': None,
    'Lakes': 'Urban Ecosystems',
    'Rivers': 'Urban Ecosystems',
    'Deltas': 'Urban Ecosystems',
    'North American Prairies': 'Intensive Croplands',
    'Eurasian Steppes': 'Intensive Croplands',
    'Pampas': 'Intensive Croplands',
    'Seagrasses': 'Aquaculture',
    'Kelp Forests': 'Aquaculture',
    'Urban Ecosystems': None,
    'Intensive Croplands': None,
    'Pastoral Lands': 'Urban Ecosystems',
    'Agroforestry': None,
    'Plantations': 'Urban Ecosystems',
    'Aquaculture': 'Urban Ecosystems'
}

# Define cascade effects
cascade_effects = {
    eco: {
        target: 1.05 for target in ecosystems if 'Savanna' in target or 'Forests' in target or 'Tundra' in target or 'Montane' in target or 'Ocean' in target
    } for eco in ecosystems if 'Rainforest' in eco
}
# Add specific cascade effects, including self-cascades for ecosystems with tipping points
cascade_effects.update({
    'Coral Reefs': {'Atlantic Ocean': 1.05, 'Pacific Ocean': 1.05, 'Southern Ocean': 1.05, 'Arctic Polar': 1.05, 'Antarctic Polar': 1.05},
    'Arctic Sea Ice': {'Atlantic Ocean': 1.05, 'Pacific Ocean': 1.05, 'Southern Ocean': 1.05, 'Arctic Polar': 1.05, 'Coral Reefs': 1.1, 'Arctic Tundra': 1.05, 'Lakes': 1.05, 'Rivers': 1.05, 'Amazon Rainforest': 1.02},
    'Boreal Forests': {'North American Temperate Forests': 1.05, 'European Temperate Forests': 1.05, 'African Savanna': 1.05, 'Arctic Tundra': 1.05, 'Arctic Polar': 1.05},
    'Atlantic Ocean': {'Coral Reefs': 1.05, 'Arctic Polar': 1.05, 'Antarctic Polar': 1.05, 'Lakes': 1.05, 'Rivers': 1.05, 'Amazon Rainforest': 1.03},
    'Pacific Ocean': {'Coral Reefs': 1.05, 'Arctic Polar': 1.05, 'Antarctic Polar': 1.05, 'Lakes': 1.05, 'Rivers': 1.05, 'Amazon Rainforest': 1.03},
    'Southern Ocean': {'Coral Reefs': 1.05, 'Arctic Polar': 1.05, 'Antarctic Polar': 1.05, 'Lakes': 1.05, 'Rivers': 1.05, 'Amazon Rainforest': 1.03},
    'Arctic Tundra': {'Andes Montane': 1.05, 'Himalayas Montane': 1.05, 'Alps Montane': 1.05, 'African Savanna': 1.05, 'Arctic Polar': 1.05, 'Arctic Sea Ice': 1.05},
    'Alpine Tundra': {'Andes Montane': 1.05, 'Himalayas Montane': 1.05, 'Alps Montane': 1.05, 'African Savanna': 1.05, 'Arctic Polar': 1.05, 'Arctic Sea Ice': 1.05},
    'Amazon Rainforest': {'Amazon Rainforest': 1.1},  # Self-cascade for tipping point (threshold 20% loss)
    'Congo Rainforest': {'Congo Rainforest': 1.1},     # Self-cascade for tipping point (threshold 20% loss)
    'Coral Reefs': {'Coral Reefs': 1.1},              # Self-cascade for bleaching threshold (threshold 50% loss)
    'Arctic Sea Ice': {'Arctic Sea Ice': 1.1},        # Self-cascade for albedo feedback (threshold 50% loss)
    'Boreal Forests': {'Boreal Forests': 1.1}         # Self-cascade for permafrost/fire feedback (threshold 20% loss)
})

# Define logistic parameters
logistic_params = {
    eco: {'k': {'Mid': 0.012 if 'Rainforest' in eco else 0.022 if eco == 'Coral Reefs' else 0.038 if eco == 'Arctic Sea Ice' else 0.015 if 'Ocean' in eco else 0.005 if 'Savanna' in eco else 0.008 if 'Desert' in eco else 0.012}} for eco in ecosystems
}