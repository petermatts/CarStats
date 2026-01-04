"""
Make the txt first with txt args, sort it then make the csv with the csv arg
"""

import os
import json
import argparse
from Conversion import Gather_Keys

cwd = os.getcwd()

def write_txt():
    keys = Gather_Keys()

    for k in range(len(keys)):
        keys[k] = keys[k] + '\n'
    
    with open('../../Docs/Base.txt', 'w') as f:
        f.writelines(keys)

def write_csv(unordered = False):
    with open('../../Docs/KeyGroups.json', 'r') as f:
        data = json.load(f)

    groups = data.keys()
    specs_t = []
    specs_f = []

    for g in groups:
        group_specs = data[g].keys()
        for s in group_specs:
            if unordered:
                specs_t.append(s)
            else:
                if data[g][s]:
                    specs_t.append(s)
                else:
                    specs_f.append(s)

    specs = specs_t + specs_f

    with open('../../Docs/Base.csv', 'w') as f:
        f.write(','.join(specs) + '\n')

def getYamlBase():
    keys = Gather_Keys(yamlfile=True)

    for k in range(len(keys)):
        keys[k] = keys[k] + '\n'
    
    with open('../../Docs/BaseYAML.txt', 'w') as f:
        f.writelines(keys)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-txt', '--txt', type=bool, nargs='?', const=True, default=False, help="Write all data column headers to txt file")
    group.add_argument('-csv', '--csv', type=bool, nargs='?', const=True, default=False, help="Write all data column headers to base csv file format")
    parser.add_argument('-u', '--unordered', type=bool, nargs='?', const=True, default=False, help="Only used with -csv|--csv flag. If specified base csv header will be unordered, it is ordered according to Docs/KeyGroups.json by default.")
    group.add_argument('-y', '--yaml', type=bool, nargs='?', const=True, default=False, help="Gets all YAML file data keys and writes them to Docs/BaseYAML.txt")

    args = parser.parse_args()
    if args.txt:
        write_txt()
    elif args.csv:
        write_csv(args.unordered)
    
    if args.yaml:
        getYamlBase()
