# Script to gather a set of all values in (parameter) specified columns of the data CSV files 

import argparse
import csv as CSV
import os
import sys
from pathlib import Path

if (Path(__file__).parent / "..").resolve().__str__() not in sys.path:
    sys.path.append((Path(__file__).parent / "..").resolve().__str__())

from common import *

def gatherBrand(attr: str, year: int = None, model: str = None):
    """Gathers all data amongst attribute. Function run within brand directory"""
    values = set()
    
    years = list(filter(lambda x: ".csv" not in x, os.listdir()))
    for y in years:
        if year != None and int(y) != year:
            continue

        os.chdir(y)
        models = os.listdir()
        for m in models:
            if model != None and m.split('.')[0] != model:
                continue

            with open(m, 'r') as f:
                reader = CSV.DictReader(f)
                data = list()
                for row in reader:
                    data.append(row)

            for d in data:
                v = d.get(attr, None)
                if v != None:
                    values.add(v)
        os.chdir('..')
    return values

def getAttr(attr: str, brand: str = None, year: int = None, model: str = None) -> set:
    cwd = os.getcwd()
    os.chdir((Path(__file__).parent / "../../Data").resolve())
    values = set()

    if brand != None:
        os.chdir(brand)
        values = gatherBrand(attr, year, model)
    else:
        brands = list(filter(lambda x: ".csv" not in x, os.listdir()))
        values = set()
        for b in brands:
            os.chdir(b)
            values = values.union(gatherBrand(attr, year, model))
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
    brands = getBrandList()
    attrs = getAttrList()

    if args.attr not in attrs:
        print("Invalid attribute\n\nValid options are:\n\n" + getCLIstr(attrs, 2))
        return
    
    if args.brand != None:
        if args.brand not in brands:
            print("Invalid brand\n\nValid options are:\n\n" + getCLIstr(brands))
            return
        models = getModelList(args.brand)
        years = getYearList(args.brand)
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
    
    return getAttr(args.attr, brand=args.brand, year=args.year, model=args.model)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--attr', '--attribute', required=True, type=str, help="The data attribute to collect (required).")
    parser.add_argument('-b', '--brand', type=str, help="The brand to collect data from")
    parser.add_argument('-m', '--model', type=str, help="The model to collect data from")
    parser.add_argument('-y', '--year', type=int, help="The year to collect data from")

    result = run(parser.parse_args())
    if result != None:
        result = list(result)
        result.sort()
        print(result)
