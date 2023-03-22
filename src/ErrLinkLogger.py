# Log all links that produce an error so that potential corrections may be sought out manually

import requests
import time
import os
import re
# import sys

# Traverse Links Directory
def getLinks():
    L = []

    # TODO  traverse link directory and call checkLink on each brand \
    #   alternatively use Docs/AllLinks.txt but Links directory should be better
    # TODO print percent progress of checking each brand
    # TODO be sure to sleep for a small amount of time between requests

    os.chdir('../Links')
    for brand in os.listdir():
        f = open(brand, 'r')
        links = f.readlines()
        f.close()

        for l in range(len(links)):
            if l != len(links)-1:
                print(brand.replace('.txt', ''), format(100*l/len(links), '.1f'), '\b%', end='\r')
            else:
                print(brand.replace('.txt', ''), '100.0 %')
            checkLink(links[l].rstrip(), L) # line that makes all the magic happen

    # Tests
    # checkLink('https://www.caranddriver.com/mercedes-amg/glc-class/specs', L) # status 404
    # checkLink('https://www.caranddriver.com/lamborghini/hurac%EF%BF%BDn/specs', L) # status 404
    # checkLink('https://www.caranddriver.com/honda/accord/specs', L) # status 200
    # checkLink('https://www.caranddriver.com/honda/civic/specs', L) # status 200
    # checkLink('https://www.caranddriver.com/tesla/cybertruck/specs', L) # status 404


    os.chdir('../')
    if not os.path.isdir('Log'):
        os.mkdir('Log')
    os.chdir('Log')

    #? make it a csv instead and put corrected link in next col
    # file = open('../ErrorLinks.txt', 'w')
    file = open('ErrorLinks.csv', 'w')
    file.writelines(L)
    file.close()

# Verify if link is good or bad (gives error code)
def checkLink(url: str, L: list):
    r = requests.get(url)
    # print(r.status_code)

    if r.status_code != 200:
        L.append(url + ',' + str(r.status_code) + ',\n')


def no_code_links():
    os.chdir('../Data')

    links = []

    for d in os.listdir():
        if os.path.isdir(d):
            os.chdir(d)
            print(os.getcwd())
            for y in os.listdir():
                if os.path.isdir(y):
                    os.chdir(y)

                    for f in os.listdir():
                        file = open(f, 'r')
                        lines = file.readlines()
                        file.close() 

                        idx = lines[0].split(",").index("URL")

                        for i in range(1, len(lines)):
                            temp = lines[i].split(",")
                            if not re.search("\d{6}$", temp[idx]) and temp[idx] != "":
                                links.append(temp[idx] + '\n')
                            # if temp[idx] == "":
                            # if temp[idx].isdecimal():
                                # print(os.getcwd())
                    os.chdir('../')
            os.chdir('../')


    os.chdir('../')
    if not os.path.isdir('Log'):
        os.mkdir('Log')
    os.chdir('Log')

    f = open("IncompleteLinks.txt", "w")
    f.writelines(links)
    f.close()

if __name__ == '__main__':
    # no_code_links()
    getLinks()
