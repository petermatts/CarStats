import argparse
import os
import yaml
from iteration_utilities import unique_everseen

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
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', type=bool, nargs='?', const=True, default=False, help="Verbose deduplication print")
    parser.add_argument('-r', '-f', '--remove', '--fix', type=bool, nargs='?', const=True, default=False, help="Remove duplicate datapoints. If this flag is not specified they will only be detected.")
    args = parser.parse_args()
    print(args)

    deduplicate(remove=args.remove, verbose=args.verbose)
