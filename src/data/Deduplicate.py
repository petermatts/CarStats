import os
import yaml
from iteration_utilities import unique_everseen

import sys

cwd = os.getcwd()

def deduplicate(remove: bool = False, verbose: bool = False):
    os.chdir('../../Data/YAML')
    brands = os.listdir()
    total = 0
    for b in brands:
        os.chdir(b)

        if not verbose:
            print(b, end='\r')

        years = os.listdir()
        brand_duplicates = 0

        for y in years:
            os.chdir(y)
            models = os.listdir()
            for m in models:
                with open(m, 'r') as f:
                    data = yaml.safe_load(f)

                dataset = list(unique_everseen(data, lambda x: x['URL']))
                duplicates = len(data) - len(dataset)
                brand_duplicates += duplicates

                if verbose:
                    fname = 'Data/YAML/' + b + '/' + y + '/' + m + ' = ' + str(duplicates)
                    print(fname)
                
                if remove:
                    with open(m, 'w') as f:
                        yml = yaml.dump(dataset)
                        f.write(yml)

            os.chdir('..')
        os.chdir('..')

        total += brand_duplicates
        print(b + " = " + str(brand_duplicates))

    os.chdir(cwd)

    final = "\n" + str(total) + " duplicates found "
    if remove:
        final += "and removed\n"
    else:
        final += "\n"

    print(final)
                

if __name__ == '__main__':
    verbose = "--verbose" in sys.argv or "-v" in sys.argv
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == 'detect':
            deduplicate(verbose=verbose)
        elif sys.argv[1].lower() == 'fix':
            # deduplicate(remove=True, verbose=verbose)
            pass
        elif sys.argv[1].lower() == '--help':
            msg = "\tdetect       = find duplicate YAML data entries\n"
            msg += "\tfix          = find and remove duplicate YAML data entries\n"
            msg += "\t-v|--verbose = print number of duplicates found (and removed) from every file that has duplicate"
            print(msg)    
        else:
            print("Invalid argument. Expected one of:\n\tdetect\n\tfix")
    else:
        msg = "Expected an argument:\n"
        msg += "\tdetect       = find duplicate YAML data entries\n"
        msg += "\tfix          = find and remove duplicate YAML data entries\n"
        msg += "\t-v|--verbose = print number of duplicates found (and removed) from every file that has duplicate"
        print(msg)