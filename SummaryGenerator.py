import json
import os

def generateSummaryTXT():
    data = json.load(open("AllBrandsAndModels.json"))
    if not os.path.isdir('Links'):
        os.mkdir('Links')

    os.chdir('Links')

    keys = list(data.keys())

    for i in keys:
        d = i.replace(" ", "-")
        if not os.path.isdir(d):
            os.mkdir(d)
        
        os.chdir(d)
        writeSummary(d, data[i])
        os.chdir('../')


def writeSummary(brand: str, models: list[str]):
    file = open("SUMMARY.txt", "w")

    base_url = 'https://caranddriver.com/'
    L = []

    for i in models:
        m = i.replace(" / ", "-").replace(" ", "-").lower()
        url = base_url + brand + '/' + m + '/specs\n'
        L.append(url)

    file.writelines(L)
    file.close()

if __name__ == '__main__':
    generateSummaryTXT()