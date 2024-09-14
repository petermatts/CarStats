# compile CSVs into master CSV files

import os
import argparse
from pathlib import Path

def getPaths(old=False) -> tuple[Path]:
    data_path = "../../Data-Old/CSV" if old else "../../Data"
    base_path = "../../Docs/Base-Old.csv" if old else "../../Docs/Base.csv"
    data_path = (Path(__file__).parent / data_path).resolve()
    base_path = (Path(__file__).parent / base_path).resolve()

    return data_path, base_path

def AllData(old=False):
    data_path, base_path = getPaths(old)

    cwd = os.getcwd()
    base = open(base_path, 'r')
    header = base.readline()
    base.close()

    L = [header]

    os.chdir(data_path)
    for brand in os.listdir():
        if not os.path.isdir(brand):
            continue

        os.chdir(brand)

        brand_lines = [header]
        print(os.getcwd())

        for year in os.listdir():
            if not os.path.isdir(year):
                continue

            os.chdir(year)
            
            for model in os.listdir():
                file = open(model, 'r')
                lines = file.readlines()
                file.close()
                brand_lines += lines[1:]

            os.chdir('../')
        
        # brand_file = open('../'+brand+'.csv', 'w')
        brand_file = open(brand+'.csv', 'w')
        brand_file.writelines(brand_lines)
        brand_file.close()

        L += brand_lines[1:] # remove header
        os.chdir('../')

    # print(os.getcwd())
    file = open('AllData.csv', 'w')
    file.writelines(L)
    file.close()

    os.chdir(cwd)

def removeCompCSVs(old=False):
    data_path, base_path = getPaths(old)

    os.chdir(data_path)
    for brand in os.listdir():
        try:
            filename = str(brand) + '/' + str(brand) + '.csv'
            os.remove(filename)
        except:
            pass

    try: 
        os.remove('AllData.csv')
    except:
        pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--make', '--build', type=bool, nargs='?', const=True, default=False, help="Create the data compiled csv files")
    group.add_argument('--remove', '--delete', '--clean', type=bool, nargs='?', const=True, default=False, help="Remove the data compiled csv files")
    parser.add_argument('--old', type=bool, nargs='?', const=True, default=False, help="Compile CSVs for old data")

    args = parser.parse_args()

    if args.make:
        AllData(old=args.old)
    elif args.remove:
        removeCompCSVs(old=args.old)
    else:
        print("This should not happen")
