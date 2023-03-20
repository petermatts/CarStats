"""
Script that corrects ill-formated data file names and corrects them
"""

import os
import re
# import sys

def detect() -> list:
    flag = True
    for brand in os.listdir():
        if os.path.isdir(brand):
            os.chdir(brand)
            for year in os.listdir():
                if os.path.isdir(year):
                    os.chdir(year)

                    for f in os.listdir():
                        if re.search("-\d{4}.csv$", f) and not re.search("(\d{4}|Silverado|Sierra)-\d{4}.csv$", f):
                            flag = False
                            print('Data/'+brand+'/'+year+'/'+f)

                    os.chdir('../')
            os.chdir('../')
            
    if flag:
        print('All filenames are good :)')


def fix():
    flag = True
    for brand in os.listdir():
        if os.path.isdir(brand):
            os.chdir(brand)
            for year in os.listdir():
                if os.path.isdir(year):
                    os.chdir(year)

                    for f in os.listdir():
                        if re.search("-\d{4}.csv$", f) and not re.search("(\d{4}|Silverado|Sierra)-\d{4}.csv$", f):
                            flag = False
                            newname = f[:-9] + '.csv'
                            print('Data/'+brand+'/'+year+'/'+f+' ---> '+'Data/'+brand+'/'+year+'/'+newname)
                            os.rename(f, newname)

                    os.chdir('../')
            os.chdir('../')
            
    if flag:
        print('There were no file names to fix :)')


if __name__ == '__main__':
    os.chdir('../Data')
    detect()
    # fix()

    
