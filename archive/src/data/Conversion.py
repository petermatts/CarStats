"""
This file maps the raw YAML data to JSON. Then JSON to CSV.

Reconfiguring it according to the design plans along the way.
"""

import os
import json
import yaml
import sys
import argparse

from Correction import Correction
from ConversionHelper import KeyMap

cwd = os.getcwd()

def YAML_TO_JSON(brand: str = None):
    if not os.path.exists('../../Data/JSON'):
        os.mkdir('../../Data/JSON')

    os.chdir('../../Data/YAML')

    brands = os.listdir()
    for b in brands:
        if brand != None and brand != b:
            continue

        os.chdir(b)
        if not os.path.exists('../../JSON/' + b):
            os.mkdir('../../JSON/' + b)
        years = os.listdir()
        
        for y in years:
            os.chdir(y)
            if not os.path.exists('../../../JSON/' + b + '/' + y):
                os.mkdir('../../../JSON/' + b + '/' + y)
            models = os.listdir()

            for m in models:
                fname = m
                with open(fname, 'r') as f:
                    data = yaml.safe_load(f)

                fname = m.split('.')[0] + '.json' # change to JSON file name
                fname = '../../../JSON/' + b + '/' + y + '/' + fname 

                # data is a list of dicts
                for d in range(len(data)):
                    data[d] = KeyMap(data[d]) # process data

                print(fname[len('../../../JSON/'):])
                data = json.dumps(data, indent=4)
                with open(fname, 'w') as f:
                    f.write(data)

            os.chdir('..')
        os.chdir('..')


def JSON_TO_CSV(brand: str = None):
    C = Correction()

    if not os.path.exists('../../Data/CSV'):
        os.mkdir('../../Data/CSV')

    with open('../../Docs/Base.csv', 'r') as f:
        header = f.readlines()[0]

    os.chdir('../../Data/JSON')

    brands = os.listdir()
    for b in brands:
        B = b.replace('-', '')

        if brand != None and brand != b:
            continue

        os.chdir(b)
        if not os.path.exists('../../CSV/' + b):
            os.mkdir('../../CSV/' + b)
        years = os.listdir()
        
        for y in years:
            os.chdir(y)
            if not os.path.exists('../../../CSV/' + b + '/' + y):
                os.mkdir('../../../CSV/' + b + '/' + y)
            models = os.listdir()

            for m in models:
                fname = m
                with open(fname, 'r') as f:
                    data = json.load(f)

                fname = m.split('.')[0] + '.csv' # change to JSON file name
                fname = '../../../CSV/' + b + '/' + y + '/' + fname

                lines = [header]
                for D in data:
                    line = ''

                    d = C.fix(D, B) # intercept and make corrections here

                    for h in header.rstrip().split(','):
                        attr = d.get(h, '')
                        if attr is not None and attr.lower() not in ['na', 'n/a', '-TBD-', '-tbd-']:
                            line += attr
                        line += ','
                    lines.append(line[:-1] + '\n') # remove last comma and add newline

                print(fname[len('../../../CSV/'):])
                with open(fname, 'w') as f:
                    f.writelines(lines)

            os.chdir('..')
        os.chdir('..')


def Gather_Keys(yamlfile: bool = False) -> list[str]:
    """"
    Helper for JSON_TO_CSV via base files

    @Param yaml: boolean flag for gathering YAML file keys, defualt false (JSON)
    """
    print("Gathering keys from...")
    keys = set()
    if yamlfile:
        os.chdir('../../Data/YAML')
    else:
        os.chdir('../../Data/JSON')

    brands = os.listdir()
    for b in brands:
        print(b)
        os.chdir(b)
        years = os.listdir()
        
        for y in years:
            os.chdir(y)
            models = os.listdir()

            for m in models:
                with open(m, 'r') as f:
                    if yamlfile:
                        data = yaml.safe_load(f)
                    else:
                        data = json.load(f)

                for d in data:
                    keys = keys.union(d.keys())
            
            os.chdir('..')
        os.chdir('..')

    print("                 ", end='\r')
    print('Done')
    os.chdir(cwd)
    return list(keys)

#??? write a clean up function before converting ???

def driver(args: argparse.Namespace):
    cwd = os.getcwd()
    os.chdir('../../Data/YAML')
    brands = os.listdir()
    os.chdir(cwd)

    def getBrandList() -> str:
        options = os.listdir('../../Links')
        longest = 0
        for i in range(len(options)):
            options[i] = options[i][:-4]
            if len(options[i]) > longest:
                longest = len(options[i])

        brands = ''
        for i in range(len(options)):
            brands += options[i]
            brands += ' '*(longest - len(options[i]) + 2)
            if i % 5 == 4:
                brands += '\n'
        os.chdir(cwd)
        return brands

    brand = args.brand
    if brand not in brands and brand != None:
        print("Invalid brand", brand, '\n\nValid brands are:\n\n' + getBrandList())
        return

    if args.yaml_json:
        YAML_TO_JSON(brand)
    elif args.json_csv:
        JSON_TO_CSV(brand)
    else:
        print("This should not happen")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--yaml-json', '--yaml2json', type=bool, nargs='?', const=True, default=False, help="Converts YAML data files to JSON")
    group.add_argument('--json-csv', '--json2csv', type=bool, nargs='?', const=True, default=False, help="Converts JSON data files to CSV")
    parser.add_argument('--brand', type=str, help="Convert only the specified brand")

    driver(parser.parse_args())
