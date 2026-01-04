"""
From the file AllBrandsAndModels.json, this script generates link summary files 
"""

import json
import os
import argparse
# import re

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
        m = i.replace(" / ", "-").replace("/", "-").replace(" & ", "-").replace(".", "").replace(" ", "-").lower()
        m = m.replace("\u014d", "o").replace("\u00e1", "a") # special character replacements
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
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-s", "--summary", nargs='?', const=True, default=False, help="Generate summary file AllBrandsAndModels.json (this must be run before -a|--all)")
    group.add_argument("-a", "--all", nargs='?', const=True, default=False, help="Generate all brand link files and AllLinks.txt (this must be run after -s|--summary)")

    args = parser.parse_args()
    if args.all:
        makeAllLinksTXT()
    elif args.summary:
        generateSummaryTXT()
    else:
        print("This should never happen")
