"""
This file aquires the names of all brands and models and writes it to a file AllBrandsAndModels.json
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

opts = webdriver.ChromeOptions()
opts.add_argument('start-maximized')
# opts.add_argument('--ignore-certificate-errors')
# opts.add_argument("--allow-running-insecure-content")
opts.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=opts)
driver.get("https://caranddriver.com")
driver.implicitly_wait(5)
# time.sleep(2)

# Open Modal to scrape
button = driver.find_element(By.CLASS_NAME, "css-m1nbu6.e2dlv6s0")
button.click()
# time.sleep(2)


# Start Scraping brands
brands = driver.find_elements(By.TAG_NAME, "option")
brands = brands[1:-2]

# print(brands)
brands_text = list(brands)
for i in range(len(brands)):
    brands_text[i] = brands[i].text
    # print(brands[i].text)

sel = driver.find_elements(By.TAG_NAME, "select")

master = {}
# Scrape Models
length = len(brands)
for i in range(length):
    brands = driver.find_elements(By.TAG_NAME, "option")
    brands = brands[1:-2]
    brands[i].click()

    time.sleep(2)
    models = driver.find_elements(By.TAG_NAME, "option")

    index = 0
    for j in range(len(models)):
        if models[j].text == "Select a Model":
            index = j

    models = models[index+1:-1]

    models_text = list(models)
    for j in range(len(models_text)):
        models_text[j] = models[j].text

    print(brands_text[i])
    for j in range(len(models)):
        print("\t" + models_text[j])

    master[brands_text[i]] = models_text

driver.close()

with open("../AllBrandsAndModels.json", "w") as outfile:
    json.dump(master, outfile, indent = 4)

# time.sleep(10)