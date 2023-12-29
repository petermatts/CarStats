# Script to gather a set of all values in (parameter) specified columns of the data CSV files 

import json
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

def gatherBrand(attr: str):
    """Gathers all data amoungst attribute. Function run within brand directory"""
    values = set()
    
    years = os.listdir()
    for y in years:
        os.chdir(y)
        models = os.listdir()
        for m in models:
            with open(m, 'r') as f:
                data = json.load(f)

            for d in data:
                v = d.get(attr, None)
                if v != None:
                    values.add(v)
        os.chdir('..')
    return values

def getAttr(attr: str, brand: str = None):
    cwd = os.getcwd()
    os.chdir("../Data/JSON")
    values = set()

    if brand != None:
        os.chdir(brand)
        values = gatherBrand(attr)
    else:
        brands = os.listdir()
        values = set()
        for b in brands:
            os.chdir(b)
            values.union(gatherBrand(attr))
            os.chdir('..')

    os.chdir(cwd)
    return values

def run():
    args = sys.argv[1:]

    brands = _getBrands()
    attrs = _getAttrs()
    
    if len(args) == 1:
        print("Warning, action not recommented - gathering attribute values for all brands")
        attr = args[0]
        if attr in brands:
            print("Missing attribute")
        elif attr not in attrs:
            print("Invalid attribute")
            return
        
        return getAttr(attr)
    elif len(args) == 2:
        brand = args[0]
        attr = args[1]
        if attr not in attrs:
            print("Invalid attribute")
            return
        if brand not in brands:
            print("Invalid brand")
            return
        
        return getAttr(attr, brand)
    else:
        print("Wrong number of arguments")
        return

if __name__ == '__main__':
   result = run()
   if result != None:
        result = list(result)
        result.sort()
        print(result)
