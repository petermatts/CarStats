import requests
from bs4 import BeautifulSoup

def test(site: str):
    # r = requests.post(site, data={'year': 2021, })
    base = 'https://caranddriver.com'
    r = requests.get(site)
    # print(r.status_code)
    # print(r.text)

    s = BeautifulSoup(r.text, "html.parser")
    # for i in s.find_all("select"):
    links = []
    for i in s.find_all(class_ = 'css-gchatv ef885v21'):
        for j in i.children:
            # print(j.get('href'))
            links.append(base + j.get('href'))

    # css-gchatv ef885v21
    for i in links:
        print(i)
    pass

if __name__ == '__main__':
    # site = 'https://caranddriver.com/audi/rs3/specs'
    site = 'https://caranddriver.com/tesla/model-s/specs'
    test(site)
