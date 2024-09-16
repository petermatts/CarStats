from copy import copy
from pathlib import Path
import os

def getBrandList() -> list[str]:
    """"""
    return list(filter(lambda x: ".csv" not in x, os.listdir(Path(__file__).parent / "../../Data")))


def getYearList(brand: str) -> list[str]:
    """"""
    assert brand in getBrandList()
    
    return list(filter(lambda x: ".csv" not in x, os.listdir(Path(__file__).parent / f"../../Data/{brand}")))


def getModelList(brand: str, year: int = None) -> list[str]:
    """"""
    assert brand in getBrandList()
    #? print out list of options if not in list?

    models = set()
    years = getYearList(brand)
    for y in years:
        if year is not None and y != year:
            continue

        for m in os.listdir(Path(__file__).parent / f"../../Data/{brand}/{y}"):
            models.add(m[:-4]) # chop off the .csv
    
    models = list(models)
    models.sort()
    return models


def getAttrList() -> list[str]:
    """"""
    with open(Path(__file__).parent / "../../Docs/Base.csv") as f:
        attributes = f.readline()

    return attributes.rstrip().split(",")


def yearHasModel(brand: str, year: str, model: str) -> bool:
    cwd = os.getcwd()
    
    try:
        os.chdir(Path(__file__).parent / f"../../Data/{brand}/{year}")
    except FileNotFoundError:
        return False
    
    models = os.listdir()
    for m in models:
        if model == m.split(".")[0]:
            os.chdir(cwd)
            return True
    os.chdir(cwd)
    return False


def getCLIString(array: list[str], num_per_row = 5) -> None:
    """"""
    longest = len(max(array, key = len))
    if longest > 25:
        num_per_row = 2

    s = ''
    for i in range(len(array)):
        s += array[i]
        s += ' '*(longest - len(array[i]) + 2)
        if i % num_per_row == num_per_row - 1:
            s += '\n'
    return s


def getTime(seconds: float) -> tuple[int, int, float]:
    """given a time duration in seconds returns a tuple of hours minutes and seconds"""
    assert seconds >= 0
    
    runtime = copy(seconds)
    hours = int(runtime/3600)
    runtime = runtime % 3600
    minutes = int(runtime/60)
    runtime = runtime % 60
    seconds = runtime
    return hours, minutes, seconds