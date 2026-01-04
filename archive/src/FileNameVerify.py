"""
Script that corrects ill-formated YAML data file names and corrects them
"""

import os
import re
import argparse

def detect() -> list:
    flag = True
    for brand in os.listdir():
        if os.path.isdir(brand):
            os.chdir(brand)
            for year in os.listdir():
                if os.path.isdir(year):
                    os.chdir(year)

                    for f in os.listdir():
                        if re.search("-\d{4}.yaml$", f) and not re.search("(\d{4}|SILVERADO|SIERRA)-\d{4}.yaml$", f):
                            flag = False
                            print('Data/YAML/'+brand+'/'+year+'/'+f)

                    os.chdir('../')
            os.chdir('../')
            
    if flag:
        print('All filenames are good :)')


def fix():
    flag = True
    for brand in os.listdir():
        if os.path.isdir(brand):
            if brand.lower() == 'ram':
                continue # ram is basically a special case
            os.chdir(brand)
            for year in os.listdir():
                if os.path.isdir(year):
                    os.chdir(year)

                    for f in os.listdir():
                        if re.search("-\d{4}.yaml$", f) and not re.search("(\d{4}|SILVERADO|SIERRA)-\d{4}.yaml$", f):
                            flag = False
                            newname = f[:-10] + '.yaml'
                            print('Data/YAML/'+brand+'/'+year+'/'+f+' ---> '+'Data/YAML/'+brand+'/'+year+'/'+newname)
                            os.rename(f, newname)

                    os.chdir('../')
            os.chdir('../')
            
    if flag:
        print('There were no file names to fix :)')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-d', '--detect', type=bool, nargs='?', const=True, default=False, help="Detect files with name errors")
    group.add_argument('-f', '--fix', type=bool, nargs='?', const=True, default=False, help="Fix files with name errors by renaming them to the proper name")
    args = parser.parse_args()

    os.chdir('../Data/YAML')

    if args.detect:
        detect()
    elif args.fix:
        fix()
    else:
        print('This should never happen')  
