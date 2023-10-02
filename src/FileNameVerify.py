"""
Script that corrects ill-formated YAML data file names and corrects them
"""

import os
import re
import sys

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
    os.chdir('../Data/YAML')

    if len(sys.argv) > 1:
        if sys.argv[1].lower() == 'detect':
            detect()
        elif sys.argv[1].lower() == 'fix':
            fix()
        else:
            print("Invalid argument. Expected one of:\n\tdetect\n\tfix")
    else:
        print("Expected an argument:\n\tdetect\n\tfix")    
