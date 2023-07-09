"""
This file maps the raw YAML data to JSON. Then JSON to CSV.

Reconfiguring it according to the design plans along the way.
"""

import os
import json
import yaml

from ConversionHelper import KeyMap

cwd = os.getcwd()

def YAML_TO_JSON():
    os.chdir('../../Data/YAML')

    brands = os.listdir()

    for b in brands:
        os.chdir(b)
        years = os.listdir()
        
        for y in years:
            os.chdir(y)
            models = os.listdir()

            for m in models:
                fname = m
                with open(fname, 'r') as f:
                    data = yaml.safe_load(f)

                fname = m.split('.')[0] + '.json' # change to JSON file name

                # todo filter duplicates in data

                #! data is a list of dicts
                for d in range(len(data)):
                    data[d] = KeyMap(data[d]) # process data

                data = json.dump(data, indent=4)
                with open(fname, 'w') as f:
                    f.write(data)


def JSON_TO_CSV():
    pass # TODO

if __name__ == '__main__':
    pass
