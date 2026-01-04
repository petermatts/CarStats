import argparse
import os
import re
import pandas as pd

def _getAttrs() -> list[str]:
    with open("../../Docs/Base.csv") as f:
        attributes = f.readline()

    return attributes.rstrip().split(",")


def makeArgs() -> tuple[dict[str, str], dict[str, str]]:
    description = """""" # todo write helpful description
    parser = argparse.ArgumentParser(description=description)
    attributes = _getAttrs()

    # customization args
    parser.add_argument("-v", "--verbose", type=bool, nargs='?', const=True, default=False, help="Displays full dataframe of matches, beware generic searches will have a large result")
    parser.add_argument("-s", "--show", nargs='+', type=str, default=[], help="Additional specs to display but not filter over. Misspellings will be skipped. Syntax is the same as the arguement in --help but replace - with _ and -- with nothing")
    
    comp = parser.add_mutually_exclusive_group()
    comp.add_argument("--ge", type=bool, const=True, default=False, nargs='?', help="Run the search with comparisons >= (does not apply for standards for brand, model, style, trim)")
    comp.add_argument("--le", type=bool, const=True, default=False, nargs='?', help="Run the search with comparisons <= (does not apply for standards for brand, model, style, trim)")

    keymap = dict() # maps the keys to the right attribute name in the CSV

    seen = list()
    for attr in attributes:
        a = re.sub(r"@|ï¿½ |:|-|/|'|\(|\)", "", attr).lower()
        #? remove mulitple occurences of the same word (first occurence of duplicates)
        a = re.sub(r"\s+", "-", a)

        if a in seen:
            continue
        else:
            seen.append(a)

        parser.add_argument(f"--{a}", type=str)
        keymap[a.replace("-", "_")] = attr

    return vars(parser.parse_args()), keymap


def search(args: dict[str, str], keymap: dict[str,  str]) -> None:
    if all(v is None for v in args.values()):
        print("Error: must supply atleast 1 search key. Run --help for options.")
        return
    elif not os.path.isfile("../../Data/CSV/AllData.csv"):
        print("Error: AllData.csv does not exist. Run CompCSV.py --build")
        return

    data = pd.read_csv("../../Data/CSV/AllData.csv", encoding="cp1252", dtype=str)

    print_cols = list()
    for k,v in args.items():
        if v is not None and k not in ['show', 'verbose', 'ge', 'le']:
            if k not in ['brand', 'model', 'style', 'trim'] and args['ge']:
                data = data[data[keymap[k]] >= v]
            elif k not in ['brand', 'model', 'style', 'trim'] and args['le']:
                data = data[data[keymap[k]] <= v]
            else:
                data = data[data[keymap[k]] == v]

            print_cols.append(keymap[k])
        elif k in ["year", "brand", "model", "engine", "max_horsepower", "max_torque", "drivetrain"] + args['show']:
            print_cols.append(keymap[k])

    data = data.fillna('')

    if args['verbose']:
        pd.set_option('display.max_rows', len(data))
    print(data[print_cols])
    pd.reset_option('display.max_rows')


if __name__ == "__main__":
    args, keymap = makeArgs()
    search(args, keymap)
