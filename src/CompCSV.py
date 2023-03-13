# compile CSVs into master CSV files

import os

def AllData():
    base = open('../Docs/Base.csv', 'r')
    header = base.readline()
    base.close()

    L = [header]

    os.chdir('../Data')
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
    os.chdir('../Data')
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
    AllData()
    # removeCompCSVs()