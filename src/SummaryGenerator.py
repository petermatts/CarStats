"""
From the file AllBrandsAndModels.json, this script generates link summary files 
"""

import json
import os
import sys

def generateSummaryTXT():
    os.chdir('../')
    data = json.load(open("AllBrandsAndModels.json"))
    if not os.path.isdir('Links'):
        os.mkdir('Links')

    os.chdir('Links')

    keys = list(data.keys())

    for i in keys:
        writeSummary(i.replace(" ", "-"), data[i])


def writeSummary(brand: str, models: list[str]):
    file = open(brand+".txt", "w")

    base_url = 'https://www.caranddriver.com/'
    L = []

    for i in models:
        m = i.replace(" / ", "-").replace("/", "-").replace(".", "-").replace(" ", "-").lower()
        url = base_url + brand.lower() + '/' + m + '/specs\n'
        L.append(url)

    file.writelines(L)
    file.close()


def makeAllLinksTXT():
    L = []
    os.chdir('../Links')
    for x in os.listdir():
        if os.path.isfile(x):
            f = open(x, "r")
            L += f.readlines()
            f.close()
    os.chdir('../Docs')

    file = open("AllLinks.txt", "w")
    file.writelines(L)
    file.close()
    os.chdir('../')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == 'all':
            makeAllLinksTXT()
        elif sys.argv[1].lower() == 'summary':
            generateSummaryTXT()
        else:
            print("Invalid argument. Expected one of:\n\tall\n\tsummary")
    else:
        print("Expected an argument:\n\tall\n\tsummary")
