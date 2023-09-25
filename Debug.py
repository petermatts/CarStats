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

opts = webdriver.ChromeOptions()
opts.add_argument('start-maximized')
opts.add_argument('--ignore-certificate-errors')
opts.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=opts)

driver.get(url)

yearSelect = driver.find_element(By.CLASS_NAME, 'e1rdmryi0.cad-dropdown-filters__control.css-1l5x637-control')
yearSelect.click()
print(yearSelect)

styleSelect = driver.find_element(By.ID, 'react-select-2-listbox')
print(styleSelect)

time.sleep(30)