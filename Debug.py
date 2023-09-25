from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import sys
import requests
import os
import time
import datetime
import yaml

url = 'https://www.caranddriver.com/alfa-romeo/4c/specs'
sleep_const = 2

opts = webdriver.ChromeOptions()
opts.add_argument('start-maximized')
opts.add_argument('--ignore-certificate-errors')
opts.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=opts)
driver.implicitly_wait(5)

driver.get(url)

def getSelectors(driver) -> tuple:
    select = driver.find_elements(By.CLASS_NAME, 'e1rdmryi0.cad-dropdown-filters__control.css-1l5x637-control')
    yearSelect, styleSelect, trimSelect = select
    return (yearSelect, styleSelect, trimSelect)

yearSelect, styleSelect, trimSelect = getSelectors(driver)
yearSelect.click()
years = driver.find_element(By.ID, 'react-select-2-listbox').find_elements(By.XPATH, ".//*")[2:]
years.reverse()

y = 0
s = 0
t = 0

while y < len(years):
    years = driver.find_element(By.ID, 'react-select-2-listbox').find_elements(By.XPATH, ".//*")[2:]
    years.reverse()
    print(years[y].text)
    years[y].click()
    time.sleep(sleep_const)

    styleSelect.click()
    styles = driver.find_element(By.ID, 'react-select-3-listbox').find_elements(By.XPATH, ".//*")[2:]
    while s < len(styles):
        styles = driver.find_element(By.ID, 'react-select-3-listbox').find_elements(By.XPATH, ".//*")[2:]
        print('\t' + styles[s].text)
        styles[s].click()
        time.sleep(sleep_const)

        trimSelect.click()
        trims = driver.find_element(By.ID, 'react-select-4-listbox').find_elements(By.XPATH, ".//*")[2:]
        while t < len(trims):
            trims = driver.find_element(By.ID, 'react-select-4-listbox').find_elements(By.XPATH, ".//*")[2:]
            print('\t\t' + trims[t].text)
            trims[t].click()
            time.sleep(sleep_const)

            try:
                yearSelect, styleSelect, trimSelect = getSelectors(driver)
            except:
                pass
            trimSelect.click()
            t += 1
        try:
            yearSelect, styleSelect, trimSelect = getSelectors(driver)
        except:
            pass
        styleSelect.click()
        t = 0
        s += 1
    try:
        yearSelect, styleSelect, trimSelect = getSelectors(driver)
    except:
        pass
    yearSelect.click()
    s = 0
    y += 1

time.sleep(30)

"""
Note on issue:

react listboxers are:
    - react-select-2-listbox for years
    - react-select-3-listbox for styles
    - react-select-4-listbox for trims

"""