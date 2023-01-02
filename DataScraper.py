import requests
from bs4 import BeautifulSoup

def scrape():
    link = 'https://www.caranddriver.com/honda/accord-2022/specs/2012/honda_accord_honda-accord-sedan_2012/337640'
    # link = 'https://www.caranddriver.com/tesla/model-s/specs/2022/tesla_model-s_tesla-model-s_2022/425838'
    # link = 'https://www.caranddriver.com/audi/rs3/specs/2022/audi_rs3_audi-rs3_2022/427686'

    r = requests.get(link)
    s = BeautifulSoup(r.text, 'html.parser')


if __name__ == "__main__":
    pass