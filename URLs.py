from bs4 import BeautifulSoup
import requests
import re

urls = []

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
            if site_n not in urls:
                urls.append(site_n)
                # print(site_n)

    urls = list(filter(lambda s: s.startswith(automaker), urls))
    # for i in urls:
    #     print(i)
        
    return urls

def pageURLs(site: str):
    reqs = requests.get(site)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    
    urls = []
    for link in soup.find_all('a'):
        # print(link.get('href'))
        urls.append(link.get('href'))
    
    return urls


#function not efficient because it is constantly making requests
def getModelSpecLinks(autoMaker: str):
    maker = scrapeAutoMakers(autoMaker)
    # print(maker)

    urls = []
    for i in range(1, len(maker)):
        # r = requests.get(maker[i]+'/specs')
        # if r.status_code == 200:
            # urls.append(r.url)
        if re.search('-\d\d\d\d$', maker[i]) == None:
            urls.append(maker[i]+'/specs')

    print(urls)
    return urls

def test():
    # r = requests.get('https://caranddriver.com/tesla/cybertruck/specs')
    r = requests.get('https://caranddriver.com/tesla/specs')
    print(r.status_code)

if __name__ == '__main__':
    site = 'https://caranddriver.com'
    autoMakers = findAutoMakers(site)
    for i in range(len(autoMakers)):
        print(i, autoMakers[i])
    # scrapeAutoMakers(autoMakers[3]) # Audi
    # scrapeAutoMakers(autoMakers[52]) # Tesla

    # getModelSpecLinks(autoMakers[3])
    getModelSpecLinks(autoMakers[52])


    
