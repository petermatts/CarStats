from bs4 import BeautifulSoup
import requests
import re
import datetime
import os

def createAutoMakersTXT():
    # returns a list of all urls for each automaker
    def findAutoMakers(site: str = 'https://caranddriver.com'):
        r = requests.get(site)
        if r.status_code != 200:
            return

        s = BeautifulSoup(r.text, "html.parser")

        urls = []

        for i in s.find_all("a"):
            href = i.attrs['href']
            if href.startswith("/") and "search" not in href:
                site_n = site + href
                if site_n not in urls:
                    urls.append(site_n)
                    # print(site_n)

        # filter list of links down to all automakers
        urls = list(filter(lambda s: not s.endswith('/'), urls))
        urls = urls[0:len(urls)-2]

        return urls[:-1]
    
    if not os.path.isdir('Links'):
        os.mkdir('Links')

    site = 'https://caranddriver.com'
    autoMakers = findAutoMakers(site)
    for i in range(len(autoMakers)):
        autoMakers[i] = autoMakers[i] + '\n'

    autoMakersDotTXT = open("Links/AutoMakers.txt", "w")
    autoMakersDotTXT.writelines(autoMakers)
    autoMakersDotTXT.close()

# returns a list of links to all model specs for the given automaker
def scrapeAutoMakers(automaker: str):
    r = requests.get(automaker)
    # if r.status_code != 200:
    #     return

    s = BeautifulSoup(r.text, "html.parser")
    urls = []

    for i in s.find_all("a"):
        href = i.attrs['href']
        if href.startswith("/") and "search" not in href:
            # site_n = site + href
            site_n = automaker + href # ? I think this is right?
            if site_n not in urls and re.search('-\d\d\d\d$', site_n) == None and site_n.startswith(automaker):
                urls.append(site_n + '/specs')
                # print(site_n)

    urls = list(filter(lambda s: s.startswith(automaker), urls))
    urls = list(set(urls))

    # Why isnt it finding this, hopefully there arent others like this that the algorithm is missing
    if automaker == 'https://caranddriver.com/audi':
        urls.append('https://caranddriver.com/audi/s7/specs')

    urls.sort()
        
    return urls


def modelSpecLinks(site: str):
    base = 'https://caranddriver.com'
    print(site)
    r = requests.get(site)

    s = BeautifulSoup(r.text, "html.parser")

    links = []
    for i in s.find_all(class_ = 'css-gchatv ef885v21'):
        print('here')
        for j in i.children:
            links.append(base + j.get('href'))
   

    if len(links) > 1 and links[0] == site:
        year = str(datetime.date.today().year) # NOTE unsure if this will work come 2023
        y = links[1][len(links[1])-4:]
        # print(type(y), type(year))
        links[0] = links[1].replace(y, year)

    # print(links)

    # return links

    masterlist = []

    for l in links:
        masterlist += modelSpecLinksHelper(l)

    return masterlist

def modelSpecLinksHelper(model: str):
    r = requests.get(model)
    s = BeautifulSoup(r.text, 'html.parser')

    o = []
    for i in s.find_all(class_ = 'css-0 e88rz1k0'):
        if(i.text == 'Select...'):
            o = []
        else:
            o.append(model + '/' + i.attrs['value'])

    return o


def getAllModelLinks(site: str):
    urls = []
    a = scrapeAutoMakers(site)

    a.remove(site + '/specs')

    a.sort() # not necessary but would be nice for stuff to be somewhat ordered

    for i in a:
        brand = i.split('/')[-3:-2][0]
        model = i.split('/')[-2:-1][0]
        print(brand, model)
        urls += modelSpecLinks(i)
    
    # for i in urls:
    #     print(i)

    urls = list(set(urls))
    urls.sort()

    return urls

def organizedFiles(site: str):
    pass

def brandLinkFile(site: str):
    if not os.path.isdir('Links'):
        os.mkdir('Links')

    brand = site.split('/')[3]
    b = brand.split('-')
    for i in range(len(b)):
        b[i] = b[i].capitalize()
    brand = '-'.join(b) + '.txt'

    # print(brand)python

    urls = getAllModelLinks(site)
    for i in range(len(urls)):
        urls[i] = urls[i] + '\n'

    f = open("Links/"+brand, "w")
    f.writelines(urls)
    f.close()

def capHyphenize(string: str):
    s = string.split("-")
    for i in range(len(s)):
        s[i] = s[i].capitalize()
    return '-'.join(s)


if __name__ == '__main__':
    # createAutoMakersTXT()

    # f = open('Links/AutoMakers.txt', 'r')
    # autoMakers = f.readlines()
    # for i in range(len(autoMakers)):
    #     autoMakers[i] = autoMakers[i].strip()
    #     print(i, autoMakers[i])

    # for i in autoMakers:
    #     brandLinkFile(i)

    # a = scrapeAutoMakers('https://caranddriver.com/tesla')
    a = getAllModelLinks('https://caranddriver.com/tesla')
    for i in a:
        print(i)

    # NOTE do this one at a time from 0 - 56
    # TODO rerun after new years?
    # Could iterate but its possible the site could fail to respond after a bajillion requests
    """
        NOTE:
            6  (Bollinger)
            7  (Bugatti)
            9  (Byton)
            16 (Fisker)
            25 (Karma)
            27 (Koenigsegg)
            32 (Lordstown)
            34 (Lucid-Motors)
            40 (Mercedes-Maybach)
            43 (Nikola)
            48 (Rimac)
            49 (Rivian)
            54 (Vinfast)
        are empty (no specs links)
    """
    # brandLinkFile(autoMakers[56])
