import os
import yaml
from iteration_utilities import unique_everseen

cwd = os.getcwd()

def remove_yaml_duplicates():
    flag = False
    os.chdir('../../Data/YAML')

    brands = os.listdir()
    for b in brands:
        os.chdir(b)
        years = os.listdir()
        
        for y in years:
            os.chdir(y)
            models = os.listdir()

            for m in models:
                with open(m, 'r') as f:
                    data = yaml.safe_load(f)

                dataset = list(unique_everseen(data))

                fname = m.split('.')[0] + '.json' # change to JSON file name
                fname = b + '/' + y + '/' + fname 
                print(fname, len(data), len(dataset))

                if len(dataset) != len(data):
                    flag = True

                with open(m, 'w') as f:
                    yml = yaml.dump(dataset)
                    f.write(yml)

            os.chdir('..')
        os.chdir('..')

    os.chdir(cwd)

    if flag:
        print('\nDuplicates Found and Removed\n')
    else:
        print('\nNo Duplicates Found\n')

if __name__ == '__main__':
    remove_yaml_duplicates()