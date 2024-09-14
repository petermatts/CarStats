"""
Migrates CSV data from the Data-Old folder to the Data folder
"""

import os
from pandas import read_csv, concat, DataFrame
from pathlib import Path

cols_to_keep = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,27,28,29,30,31,54,55,80,130]

def mergeCSVs(*inputs: str | os.PathLike, output: str | os.PathLike) -> None:
    """
    Merge all input CSVs into one CSV file (in order they are passed in) to 1 csv file
    todo?: not sure if this functionality is necessary but it could be nice
    """


def getHeader() -> DataFrame:
    base_path = (Path(__file__).parent / '..' / '..' / 'Docs' / 'Base-Old.csv').resolve()

    header = read_csv(base_path, header=None)[cols_to_keep]
    header.to_csv(base_path / '..' / 'Base.csv', index=False, header=None)

    return header


def migrateFile(old: str | os.PathLike, new: str | os.PathLike) -> None:
    """"""
    header = getHeader()

    data = read_csv(old, skiprows=1, header=None, encoding='cp1252')[cols_to_keep].fillna("")
    data = concat([header, data])
    data.to_csv(new, index=False, header=None)


def migrate() -> None:
    #? remove/skip compiled old csv files
    old_data_path = (Path(__file__).parent / '..' / '..' / 'Data-Old' / 'CSV').resolve()
    new_data_path = (Path(__file__).parent / '..' / '..' / 'Data').resolve()

    brands = os.listdir(old_data_path)
    for b in brands:
        years = os.listdir(old_data_path / b)

        for y in years:
            new_dir = new_data_path / b / y
            models = os.listdir(old_data_path / b / y)

            l = 0
            for m in models:
                os.makedirs(new_dir, exist_ok=True)

                print(" "*(2*l), end='\r')
                print(f"{b}/{y}/{m}", end='\r')
                l = len(f"{b}/{y}/{m}")

                migrateFile(old_data_path / b / y / m, new_dir / m)


if __name__ == "__main__":
    migrate()
