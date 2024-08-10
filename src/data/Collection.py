# Script to gather a set of all values in (parameter) specified columns of the data CSV files 

import json
import yaml
import csv as CSV
import os
import argparse

# Collects data from JSON

def _getBrands() -> list[str]:
    cwd = os.getcwd()
    os.chdir("../../Data/YAML")
    brands = os.listdir()
    os.chdir(cwd)
    return brands

def _getYears(brand: str) -> list[str]:
    cwd = os.getcwd()
    os.chdir("../../Data/YAML/"+brand)
    years = os.listdir()
    os.chdir(cwd)
    return years

def _getModels(brand: str) -> list[str]:
    cwd = os.getcwd()
    os.chdir("../../Data/YAML/"+brand)
    years = os.listdir()
    models = set()
    for y in years:
        for m in os.listdir(y):
            models.add(m[:-5]) # chop of the .yaml
    os.chdir(cwd)
    models = list(models)
    models.sort()
    return models

def _getAttrs(yaml: bool = None) -> list[str]:
    if yaml:
        with open("../../Docs/BaseYAML.txt") as f:
            attributes = f.readlines()
    else:
        with open("../../Docs/Base.txt") as f:
            attributes = f.readlines()
        
    for a in range(len(attributes)):
        attributes[a] = attributes[a].strip()

    return attributes

def yearHasModel(brand: str, year: str, model: str) -> bool:
    cwd = os.getcwd()
    os.chdir("../../Data/YAML/"+brand+"/"+year)
    models = os.listdir()
    for m in models:
        if model == m.split(".")[0]:
            os.chdir(cwd)
            return True
    os.chdir(cwd)
    return False

def gatherBrand(attr: str, yam: bool, csv: bool, year: int = None, model: str = None):
    """Gathers all data amongst attribute. Function run within brand directory"""
    values = set()
    
    years = os.listdir()
    for y in years:
        if year != None and int(y) != year:
            continue

        os.chdir(y)
        models = os.listdir()
        for m in models:
            if model != None and m.split('.')[0] != model:
                continue

            with open(m, 'r') as f:
                if yam:
                    data = yaml.safe_load(f)
                elif csv:
                    reader = CSV.DictReader(f)
                    data = list()
                    for row in reader:
                        data.append(row)
                else:
                    data = json.load(f)

            for d in data:
                v = d.get(attr, None)
                if v != None:
                    values.add(v)
        os.chdir('..')
    return values

def getAttr(attr: str, brand: str = None, yam: bool = False, csv: bool = False, year: int = None, model: str = None) -> set:
    cwd = os.getcwd()
    if yam:
        os.chdir("../../Data/YAML")
    elif csv:
        os.chdir("../../Data/CSV")
    else:
        os.chdir("../../Data/JSON")
    values = set()

    if brand != None:
        os.chdir(brand)
        values = gatherBrand(attr, yam, csv, year, model)
    else:
        brands = os.listdir()
        values = set()
        for b in brands:
            os.chdir(b)
            values = values.union(gatherBrand(attr, yam, csv, year, model))
            os.chdir('..')

    os.chdir(cwd)
    return values

def getCLIstr(x: list[str], numPerRow: int = 5) -> str:
    longest = len(max(x, key = len))
    if longest > 25:
        numPerRow = 2

    s = ''
    for i in range(len(x)):
        s += x[i]
        s += ' '*(longest - len(x[i]) + 2)
        if i % numPerRow == numPerRow - 1:
            s += '\n'
    return s


"""
NOTE running with YAML you must supply raw feild key
"""
def run(args: argparse.Namespace):
    brands = _getBrands()
    attrs = _getAttrs(args.yaml)

    if args.attr not in attrs:
        print("Invalid attribute\n\nValid options are:\n\n" + getCLIstr(attrs, 2))
        return
    
    if args.brand != None:
        if args.brand not in brands:
            print("Invalid brand\n\nValid options are:\n\n" + getCLIstr(brands))
            return
        models = _getModels(args.brand)
        years = _getYears(args.brand)
        if args.model != None and args.model not in models:
            print("Invalid model for " + args.brand + "\n\nValid options are:\n\n" + getCLIstr(models))
            return
        if args.year != None and str(args.year) not in years:
            print("Invalid year for " + args.brand + "\n\nValid options are:\n\n" + getCLIstr(years))
            return
        if args.year is not None and not yearHasModel(args.brand, str(args.year), args.model):
            print("No data for " + args.brand + " " + str(args.year) + " " + args.model)
            return
    else:
        print("Warning, action not recommended - gathering attribute values for all brands. This may take a bit...")
    
    return getAttr(args.attr, brand=args.brand, yam=args.yaml, csv=args.csv, year=args.year, model=args.model)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--attr', '--attribute', required=True, type=str, help="The data attribute to collect (required). IMPORTANT: if --yaml flag is used you must use the raw attribute feild names")
    parser.add_argument('-b', '--brand', type=str, help="The brand to collect data from")
    parser.add_argument('-m', '--model', type=str, help="The model to collect data from")
    parser.add_argument('-y', '--year', type=int, help="The year to collect data from")

    dir_group = parser.add_mutually_exclusive_group()
    dir_group.add_argument('--yaml', type=bool, nargs='?', const=True, default=False, help="Collect data from YAML data the folder is (default is JSON)")
    dir_group.add_argument('--csv', type=bool, nargs='?', const=True, default=False, help="Collect data from CSV data the folder is (default is JSON)")

    result = run(parser.parse_args())
    if result != None:
        result = list(result)
        result.sort()
        print(result)
