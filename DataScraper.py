from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time



# function to go through all Links/*/SUMARRY.txt files
def readAll():
    L = []
    os.chdir('Links')
    for x in os.listdir():
        if os.path.isdir(x):
            os.chdir(x)

            f = open("SUMMARY.txt", "r")
            L += f.readlines()
            f.close()

            os.chdir('../')
    os.chdir('../')

    file = open("AllLinks.txt", "w")
    file.writelines(L)
    file.close()


# scrape the desired data from the given url
def scrapeData(url: str):
    driver = webdriver.Chrome(r"./driver/chromedriver")
    driver.get(url)
    driver.maximize_window()
    time.sleep(2)

    data = driver.find_elements(By.CLASS_NAME, 'css-1ajawdl.eqxeor30')
    # print(data)
    # print(dir(data[0]))

    rows = []
    for i in range(len(data)):
        row = data[i].find_elements(By.TAG_NAME, 'div')
        # print(row)
        if len(row) != 0:
            rows.append((row[0].text, row[1].text))
        else:
            print(data[i].text)

    for i in rows:
        print(i)

    time.sleep(100)

if __name__ == '__main__':
    url = 'https://caranddriver.com/honda/accord/specs'
    scrapeData(url)
    