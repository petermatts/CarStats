# Log all links that produce an error so that potential corrections may be sought out manually

# https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

import requests
import time
import os
import re
import sys

# Traverse Links Directory
def getLinks():
    L = []
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
            time.sleep(0.05)

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

    # file = open('../ErrorLinks.txt', 'w')
    file = open('ErrorLinks.csv', 'w')
    file.writelines(L)
    file.close()

# Verify if link is good or bad (gives error code)
def checkLink(url: str, L: list):
    s = requests.Session()
    # s.max_redirects = 100
    try:
        r = s.get(url)
    except requests.exceptions.TooManyRedirects:
        L.append(url.replace('/specs', '') + ',302,\n') # too many redirects
        return
    except requests.exceptions.ConnectionError:
        print(url + " is thaving connection issues, sleeping for a minute then trying again", end='\r')
        time.sleep(60)
        checkLink(url, L)

    # print(r.status_code)

    if r.status_code != 200:
        L.append(url.replace('/specs', '') + ',' + str(r.status_code) + ',\n')


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


def fix():
    with open('../Log/ErrorLinks-Fix.csv', 'r') as f:
        L = f.readlines()

    fixes = {}
    for link in L:
        slice = link.split(',')
        if slice[2] != '':
            fix_link = slice[2]
            if '/specs' not in fix_link:
                fix_link += '/specs'
            fixes[slice[0]] = fix_link
    
    # print(fixes.values())

    os.chdir('../Links')
    for brand in os.listdir():
        links = []
        with open(brand, 'r') as f:
            links = f.readlines()

        for i in range(len(links)):
            new_link = fixes.get(links[i].replace('/specs', '').rstrip())
            if new_link != None:
                links[i] = new_link + '\n'

        with open(brand, 'w') as f:
            f.writelines(links)

    os.chdir('../src')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1].lower() == 'code':
            no_code_links()
        elif sys.argv[1].lower() == 'check':
            getLinks()
        elif sys.argv[1].lower() == 'fix':
            fix()
        else:
            print("Invalid arguement. Expected one of:\n\tcode\n\tcheck\n\tfix")
    else:
        print("Missing argument. Expected one of:\n\tcode\n\tcheck\n\tfix")
