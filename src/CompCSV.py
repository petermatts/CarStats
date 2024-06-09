# compile CSVs into master CSV files

import os
import argparse

def AllData():
    base = open('../Docs/Base.csv', 'r')
    header = base.readline()
    base.close()

    L = [header]

    os.chdir('../Data/CSV')
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

        L += brand_lines
        os.chdir('../')

    # print(os.getcwd())
    file = open('AllData.csv', 'w')
    file.writelines(L)
    file.close()

    os.chdir('../')

def removeCompCSVs():
    os.chdir('../Data/CSV')
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

    args = parser.parse_args()
    print(args)

    if args.make:
        AllData()
    elif args.remove:
        removeCompCSVs()
    else:
        print("This should not happen")
