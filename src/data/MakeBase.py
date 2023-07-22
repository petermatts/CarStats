"""
Make the txt first with txt args, sort it then make the csv with the csv arg
"""

import os
import sys
from Conversion import Gather_Keys

cwd = os.getcwd()

def write_txt():
    keys = Gather_Keys()

    for k in range(len(keys)):
        keys[k] = keys[k] + '\n'
    
    with open('../../Docs/Base.txt', 'w') as f:
        f.writelines(keys)

def write_csv():
    s = ""
    with open('../../Docs/Base.txt', 'r') as f:
        keys = f.readlines()

    for k in keys:
        s += k.rstrip() + ','

    s = s[:-1] + '\n'
    with open('../../Docs/Base.csv', 'w') as f:
        f.write(s)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == 'txt':
            write_txt()
        elif sys.argv[1] == 'csv':
            write_csv()
    else:
        print('\nError No Args\n')
