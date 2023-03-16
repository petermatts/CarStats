# Script to gather a set of all values in (parameter) specified columns of the data CSV files 

import os
import sys

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
    """
        Index : Attribute
        0     : Year
        1     : Brand
        2     : Model
        3     : Trim
        4     : Price
        5     : EPA Class
        6     : Engine
        7     : Turbos
        8     : Fuel
        9     : Displacement (liters)
        10    : Max Horsepower
        11    : Max Horsepwer RPM
        12    : Max Torque
        13    : Max Torque RPM
        14    : Transmission
        15    : Transmission Speeds
        16    : MPG (combined)
        17    : MPG (city)
        18    : MPG (highway)
        19    : MPGe (combined)
        20    : MPGe (city)
        21    : MPGe (highway)
        22    : Fuel Cap. (Gal)
        23    : Length (in)
        24    : Width no mirrors (in) #! issue from here down see issue #24
        25    : Wheelbase (in)
        26    : Seating Cap
        27    : Passenger Space (cu ft)
        28    : Trunk Space (cu ft)
        29    : Turn Radius (ft)
        30    : Weight (lbs)
        31    : Max Towing (lbs)
        32    : URL
    """
    
    # use excel file to find index of brand
    # collect_attr(attribute col number, brand index number)
    collect_attr(0, 0)