from ecosystem_hierarchy import get_ecosystem_category
from all_stressors import all_stressors_data
for eco in all_stressors_data.keys():
    print(f"{eco}: {get_ecosystem_category(eco)}")