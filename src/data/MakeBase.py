"""
Make the txt first with txt args, sort it then make the csv with the csv arg
"""

import os
import sys
import json
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


if __name__ == '__main__':
    if len(sys.argv) > 1:
        unordered = False
        if len(sys.argv) > 2 and sys.argv[2].lower() == 'u':
            unordered = True
            
        if sys.argv[1] == 'txt':
            write_txt()
        elif sys.argv[1] == 'csv':
            write_csv(unordered)
    else:
        print('\nError No Args\n')
