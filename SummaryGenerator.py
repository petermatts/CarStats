"""
From the file AllBrandsAndModels.json, this script generates link summary files 
"""

import json
import os

def generateSummaryTXT():
    data = json.load(open("AllBrandsAndModels.json"))
    if not os.path.isdir('Links'):
        os.mkdir('Links')

    os.chdir('Links')

    keys = list(data.keys())

    for i in keys:
        writeSummary(i.replace(" ", "-"), data[i])


def writeSummary(brand: str, models: list[str]):
    file = open(brand+".txt", "w")

    base_url = 'https://caranddriver.com/'
    L = []

    for i in models:
        m = i.replace(" / ", "-").replace(" ", "-").lower()
        url = base_url + brand.lower() + '/' + m + '/specs\n'
        L.append(url)

    file.writelines(L)
    file.close()

if __name__ == '__main__':
    generateSummaryTXT()