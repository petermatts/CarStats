from bs4 import BeautifulSoup
import requests
import re
import datetime

# returns a list of all urls for each automaker
def findAutoMakers(site: str):
    # site = 'https://caranddriver.com'
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

    return urls


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
            site_n = site + href
            if site_n not in urls and re.search('-\d\d\d\d$', site_n) == None and site_n.startswith(automaker):
                urls.append(site_n + '/specs')
                # print(site_n)

    # urls = list(filter(lambda s: s.startswith(automaker), urls))
    urls = list(set(urls))
        
    return urls


def modelSpecLinks(site: str):
    base = 'https://caranddriver.com'
    r = requests.get(site)

    s = BeautifulSoup(r.text, "html.parser")

    links = []
    for i in s.find_all(class_ = 'css-gchatv ef885v21'):
        for j in i.children:
            links.append(base + j.get('href'))
   

    if len(links) > 1 and links[0] == site:
        year = str(datetime.date.today().year) # NOTE unsure if this will work come 2023
        y = links[1][len(links[1])-4:]
        # print(type(y), type(year))
        links[0] = links[1].replace(y, year)

    # print(links)

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

    for i in a:
        brand = i.split('/')[-3:-2][0]
        model = i.split('/')[-2:-1][0]
        print(brand, model)
        urls += modelSpecLinks(i)
    
    for i in urls:
        print(i)

    urls = list(set(urls))
    urls.sort()

    return urls

def getAll():
    site = 'https://caranddriver.com'
    autoMakers = findAutoMakers(site)

    urls = []


def test():
    # r = requests.get('https://caranddriver.com/tesla/cybertruck/specs')
    r = requests.get('https://caranddriver.com/tesla/specs')
    print(r.status_code)

# TODO create reference function that shows what index all outmakers are, make it write to a txt file?

if __name__ == '__main__':
    site = 'https://caranddriver.com'
    autoMakers = findAutoMakers(site)
    # for i in range(len(autoMakers)):
        # print(i, autoMakers[i])

    # a = scrapeAutoMakers(autoMakers[3]) # Audi
    # a = scrapeAutoMakers(autoMakers[20]) # Honda
    # a = scrapeAutoMakers(autoMakers[52]) # Tesla
    # for i in a:
        # l = modelSpecLinks(i)
        # for j in l:
            # print(j)

    for i in getAllModelLinks(autoMakers[52]):
        # print(i)
        pass
