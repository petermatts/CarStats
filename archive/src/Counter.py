# count sizes of each brand in number of models and print/log counts

import json

brand_models = json.load(open("../AllBrandsAndModels.json"))

# print(brand_models)

# counts = {}
for i in brand_models.keys():
    # counts[i] = len(brand_models[i])
    print(i, "\b:", len(brand_models[i]))

