"""
This script just generates the initial set of log xlsx files, from the migrated data in the Data
folder. Everything after this is to be manually updated and maintained.

Note this file outputs its generated log files to the Temp folder so as not to accidentally
overwrite anything in the Log folder
"""

import argparse 
import os
import sys
from pandas import read_csv
from pathlib import Path

if (Path(__file__).parent / "..").resolve().__str__() not in sys.path:
    sys.path.append((Path(__file__).parent / "..").resolve().__str__())

from common import *


def makeCoverageDataFiles() -> None:
    coverage_path = (Path(__file__).parent / "../../Log/Coverage").resolve()
    os.makedirs(coverage_path, exist_ok=True)
    os.makedirs(coverage_path / "plots", exist_ok=True)

    # writen to temp directory to avoid conflicts
    write_path = (Path(__file__).parent / "../../Temp/Coverage").resolve()
    os.makedirs(write_path, exist_ok=True)

    year_range = list(range(2004,2025)) # this can be hard coded as this will not change
    year_range = list(map(lambda x: str(x), year_range))

    brands = getBrandList()
    
    for b in brands:
        models = getModelList(b)
        #? formated whitespace could be a fun, but entirely unneccessary addition to these csvs
        with open(write_path / f"{b}.csv", 'w') as f:
            f.write(f",{','.join(year_range)}\n")
            for m in models:
                # f.write(f"{m}{','*len(year_range)}\n")
                f.write(f"{m},")
                for y in year_range:
                    if yearHasModel(b, y, m):
                        f.write("x")
                    if y != year_range[-1]:
                        f.write(",")
                f.write("\n")



def makeArgs() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    operation = parser.add_mutually_exclusive_group(required=True)

    operation.add_argument("--coverage", type=bool, nargs='?', const=True, default=False, help="")
    
    return parser.parse_args()


if __name__ == '__main__':
    args = makeArgs()

    if args.coverage:
        makeCoverageDataFiles()
    else:
        print("Invalid input arguement")