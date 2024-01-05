# Script to gather a set of all values in (parameter) specified columns of the data CSV files 

import json
import yaml
import os
import sys

# Collects data from JSON

def _getBrands():
    cwd = os.getcwd()
    os.chdir("../Data/JSON")
    brands = os.listdir()
    os.chdir(cwd)
    return brands

def _getAttrs():
    with open("../Docs/Base.txt") as f:
        attributes = f.readlines()
    
    for a in range(len(attributes)):
        attributes[a] = attributes[a].strip()

    return attributes

def gatherBrand(attr: str, yam: bool):
    """Gathers all data amoungst attribute. Function run within brand directory"""
    values = set()
    
    years = os.listdir()
    for y in years:
        os.chdir(y)
        models = os.listdir()
        for m in models:
            with open(m, 'r') as f:
                if yam:
                    data = yaml.safe_load(f)
                else:
                    data = json.load(f)

            for d in data:
                v = d.get(attr, None)
                if v != None:
                    values.add(v)
        os.chdir('..')
    return values

def getAttr(attr: str, brand: str = None, yam: bool = False):
    cwd = os.getcwd()
    if yam:
        os.chdir("../Data/YAML")
    else:
        os.chdir("../Data/JSON")
    values = set()

    if brand != None:
        os.chdir(brand)
        values = gatherBrand(attr, yam)
    else:
        brands = os.listdir()
        values = set()
        for b in brands:
            os.chdir(b)
            values.union(gatherBrand(attr, yam))
            os.chdir('..')

    os.chdir(cwd)
    return values

"""
NOTE running with YAML you must supply raw feild key
Below are exuivalent examples for each data save type
Example JSON: python3 Collection.py Honda Transmission
Example YAML: python3 Collection.py Honda "Transmission Description" YAML"
"""
def run():
    args = sys.argv[1:]

    brands = _getBrands()
    attrs = _getAttrs()
    
    yam = "yaml" in map(lambda x: x.lower(), args)

    if len(args) >= 2:
        brand = args[0]
        attr = args[1]
        if not yam and attr not in attrs:
            print("Invalid attribute")
            return
        if brand not in brands:
            print("Invalid brand")
            return
        
        return getAttr(attr, brand=brand, yam=yam)
    elif len(args) >= 1:
        print("Warning, action not recommented - gathering attribute values for all brands")
        attr = args[0]
        if attr in brands:
            print("Missing attribute")
        elif not yam and attr not in attrs:
            print("Invalid attribute")
            return
        
        return getAttr(attr, yam=yam)
    else:
        print("Wrong number of arguments")
        return

if __name__ == '__main__':
   result = run()
   if result != None:
        result = list(result)
        result.sort()
        print(result)
