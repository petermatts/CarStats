"""
This file maps the raw YAML data to JSON. Then JSON to CSV.

Reconfiguring it according to the design plans along the way.
"""

import os
import json
import yaml
import sys

# if os.getcwd() + '/../' not in sys.path:
    # sys.path.append(os.getcwd() + '/../')

# from Correction import Correction
from ConversionHelper import KeyMap

cwd = os.getcwd()

def YAML_TO_JSON(brand = None):
    if not os.path.exists('../../Data/JSON'):
        os.mkdir('../../Data/JSON')

    os.chdir('../../Data/YAML')

    brands = os.listdir()
    for b in brands:
        if brand != None and brand != b:
            continue
        # print("Converting", b)
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


def JSON_TO_CSV(brand = None):
    if not os.path.exists('../../Data/CSV'):
        os.mkdir('../../Data/CSV')

    with open('../../Docs/Base.csv', 'r') as f:
        header = f.readlines()[0]

    os.chdir('../../Data/JSON')

    brands = os.listdir()
    for b in brands:
        if brand != None and brand != b:
            continue
        # print("Converting", b)
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
                for d in data:
                    line = ''
                    # TODO intercept and make corrections here
                    for h in header.rstrip().split(','):
                        attr = d.get(h, '')
                        if attr is not None and attr.lower() not in ['na', 'n/a']:
                            line += attr
                        line += ','
                    lines.append(line[:-1] + '\n') # remove last comma and add newline

                print(fname[len('../../../CSV/'):])
                with open(fname, 'w') as f:
                    f.writelines(lines)

            os.chdir('..')
        os.chdir('..')


def Gather_Keys() -> list[str]:
    """"Helper for JSON_TO_CSV"""
    print("Gathering keys from...")
    keys = set()
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
                    data = yaml.safe_load(f)

                for d in data:
                    keys = keys.union(d.keys())
            
            os.chdir('..')
        os.chdir('..')

    print("                 ", end='\r')
    print('Done')
    os.chdir(cwd)
    return list(keys)

#??? write a clean up function before converting ???

if __name__ == '__main__':
    cwd = os.getcwd()
    os.chdir('../../Data/YAML')
    brands = list(map(lambda x: x.lower(), os.listdir()))
    os.chdir(cwd)

    brand = None
    if len(sys.argv) > 1:
        if len(sys.argv) > 2 and sys.argv[2].lower() in brands:
            brand = sys.argv[2]
        if sys.argv[1].lower() in ['yaml-json', 'yaml2json']:
            YAML_TO_JSON(brand)
        elif sys.argv[1].lower() in ['json-csv', 'json2csv']:
            JSON_TO_CSV(brand)
        else:
            print("Error Invalid Arg:", sys.argv[1])
    else:
        print("Error No Args. Expected one of:\n")
        print("YAML to JSON:\n\tyaml-json\n\tyaml2json\n\nJSON to CSV:\n\tjson-csv\n\tjson2csv")