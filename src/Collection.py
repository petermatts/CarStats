# Script to gather a set of all values in (parameter) specified columns of the data CSV files 

import os

# TODO make this adaptable to only check within a brand.
# ../Data/Brand/Brand.csv or ../Data/AllData.csv

def collect_attr(attr: int, idx = -1):
    file_path = '../Data/AllData.csv'
    if idx >= 0:
        cwd = os.getcwd()
        os.chdir('../Data')
        brands = []
        for i in os.listdir():
            if os.path.isdir(i):
                brands.append(i)
        os.chdir(cwd)

        # print(brands)
        file_path = '../Data/' + brands[idx] + '/' + brands[idx] + '.csv'

    file = open(file_path, 'r')
    lines = file.readlines()
    file.close()

    data = []
    header = lines[0].split(',')[attr]
    for i in lines[1:]:
        data.append(i.rstrip().split(',')[attr])

    collection = list(set(data))

    collection.sort() # feel free to comment this out if you please
    
    print(header)
    print(collection)


if __name__ == '__main__':
    """"""
    # use excel file to find index of brand
    # collect_attr(attribute col number, brand index number)
    collect_attr(0, 0)