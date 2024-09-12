"""
This is DataScraper V3

New features include:
- by passing bot detection using undetected_chromedriver module
- better and cleaner source code (I am a better SWE now than when I wrote DataScrapers V1 and V2)
- more optimized code design towards maintaiablity and usability


Date: 09/04/2024
"""

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
import undetected_chromedriver as uc
import argparse
import yaml
import time
import requests
import re
import os
import sys

common_path = str(Path(__file__).parent / "src" / "common")
if common_path not in sys.path:
    sys.path.append(common_path)

from src.common import *


# Helper/Setup Functions
####################################################################################################

def openDebugFile(path: str):
    def makeDebugFile(path: str):
        """Assumes valid path and only needs to make file"""

        with open(path, 'w') as f:
            f.write(yaml.dump(DEBUG_DEFAULT))
    
    try:
        with open(path, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        makeDebugFile(path)
        return openDebugFile(path)


def updateDebugFile(path: str, debug_data: dict):
    with open(path, 'w') as f:
        f.write(yaml.dump(debug_data))


def resetDebugFile(path: str):
    with open(path, 'w') as f:
        f.write(yaml.dump(DEBUG_DEFAULT))


def makeArgs() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    brand_group = parser.add_mutually_exclusive_group(required=True)
    brand_group.add_argument('--brand', type=str, help="The car brand to scrape (required)")
    brand_group.add_argument('--list', type=bool, nargs='?', const=True, default=False, help="Lists all valid brand options")

    model_group = parser.add_mutually_exclusive_group()
    model_group.add_argument('--model', type=str, help="The model to scrape")
    model_group.add_argument('--show', type=bool, nargs='?', const=True, default=False, help="Show models options of brand listed")

    year_group = parser.add_mutually_exclusive_group()
    year_group.add_argument('--latest', type=bool, nargs='?', const=True, default=False, help="Scrape the latest year data for model is avaiable (cannot be used with --year flag)")
    year_group.add_argument('--year', type=int, help="The year to scrape model data (cannot be used with --latest flag)")

    parser.add_argument('--test', type=bool, nargs='?', const=True, default=False, help="Test the scraper by printing output to see if it is operating correctly")

    return parser.parse_args()


def getSelectors(driver: uc.Chrome) -> tuple[uc.WebElement,uc.WebElement,uc.WebElement]:
    select = driver.find_elements(By.CLASS_NAME, "eb99zkn0.eqh7ajx0.css-1pdk0xo-container")
    if len(select) != 3:
        raise ValueError(f"{len(select)} dropdowns found, expected 3. Expected to see Year, Style, and Trim.")
    
    yearSelect, styleSelect, trimSelect = select
    return yearSelect, styleSelect, trimSelect

####################################################################################################

# the scraping algorithm is composed of the functions in this section

def scrape(brand_filename: str, modelname: str = None, year: int = None, latest = False, test = False):
    """brand_filename is the path to the brands links in Links folder"""
    brand = brand_filename.split('/')[-1].replace('.txt', '')

    # get model links
    with open(brand_filename, 'r') as file:
        links = file.readlines()

    # open debug file (open with defaults if it doesn't exist)
    debug_path = Path(__file__).parent / "Debug" / (brand + '.yaml')
    debug = openDebugFile(debug_path)
    u = debug['link_idx']

    # iterate over links in brand
    while u < len(links):
        url = links[u]
        model = url.split('/')[4]

        # if model param is valid and url is not of the model... skip it
        if modelname != None and model.lower() != modelname.lower():
            u += 1
            continue

        # create the webdriver and options
        opts = uc.ChromeOptions()
        opts.add_argument('start-maximized')
        # opts.add_argument('--ignore-certificate-errors')
        # opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = uc.Chrome(opts, use_subprocess=False)
        driver.implicitly_wait(Timing.IMPLICIT_WAIT)

        try:
            driver.get(url)
            r = requests.get(url, timeout = 5)
            if r.status_code == 404:
                raise ValueError()
        except ValueError:
            print(f"Bad URL: {url}")
            with open(Path(__file__).parent / "Log" / "Bad ScrapeLinks.log", 'a') as file:
                file.write(url)
            u += 1
            debug['link_idx'] = u
            updateDebugFile(debug_path, debug)
            continue

        #iteratively scrape over the dropdown, updating debug file as we go
        try:
            yearSelect, styleSelect, trimSelect = getSelectors(driver)
            yearSelect.click()

            years = driver.find_element(By.ID, 'react-select-2-listbox').find_elements(By.XPATH, './/*')[2:]
            print(list(map(lambda e: e.text, years))) # todo remove this
            years.reverse()

            time.sleep(Timing.SLEEP)

            y, s, t = debug['year_idx'], debug['style_idx'], debug['trim_idx']


            if latest: # skip to the latest year if latest param is true
                y = len(years) - 1 

            while y < len(years):
                time.sleep(Timing.SLEEP)
                years = driver.find_element(By.ID, 'react-select-2-listbox').find_elements(By.XPATH, './/*')[2:]
                years.reverse()

                if year != None and int(years[y].text) != year:
                    # only scrape the specified year if the year parameter is defined
                    y += 1
                    continue

                debug['year_text'] = years[y].text
                years[y].click()
                time.sleep(Timing.SLEEP)

                styleSelect.click()
                styles = driver.find_element(By.ID, 'react-select-3-listbox').find_elements(By.XPATH, './/*')[2:]
                print(list(map(lambda e: e.text, styles))) # todo remove this
                while s < len(styles):
                    time.sleep(Timing.SLEEP)
                    styles = driver.find_element(By.ID, 'react-select-3-listbox').find_elements(By.XPATH, './/*')[2:]
                    debug['style_text'] = styles[s].text
                    styles[s].click()
                    time.sleep(Timing.SLEEP)

                    trimSelect.click()
                    trims = driver.find_element(By.ID, 'react-select-4-listbox').find_elements(By.XPATH, './/*')[2:]
                    print(list(map(lambda e: e.text, trims)))
                    while t < len(trims):
                        time.sleep(Timing.SLEEP)
                        trims = driver.find_element(By.ID, 'react-select-4-listbox').find_elements(By.XPATH, './/*')[2:]
                        debug['trim_text'] = trims[t].text
                        trims[t].click()
                        time.sleep(Timing.SLEEP)



            time.sleep(3600) # todo remove this
        except Exception:
            pass #todo


####################################################################################################

# define the driver function that continues scraping if errors occur

def driver(args: argparse.Namespace) -> int:
    """I hope anyone reading this can appreciate the pun that is this function name"""

    brandList = getBrandList()

    # get option parameters for the scraper
    brand = args.brand
    model = args.model
    year = args.year
    latest = args.latest
    test = args.test

    if not args.list:
        brand_links = str(Path(__file__).parent / "Links" / (brand + ".txt"))

        if os.path.isfile(brand_links): 
            if args.show:
                print(f"Here are all models of brand {brand}:\n{getCLIString(getModelList(brand))}")
                return Results.BAD
            
            result = 0
            while result <= 0:
                result = scrape(brand_links, modelname=model, year=year, latest=latest, test=test)
                #? change to a match case
                if result == Results.BAD_LINK:
                    print("Bad link encountered, skipping")
                    time.sleep(Timing.BAD_LINK)
                elif result == Results.REQUEST_TIMEOUT:
                    print(f"Request timeout encountered, waiting {Timing.TIMEOUT}s before retrying")
                    time.sleep(Timing.TIMEOUT)
                elif result == Results.SELENIUM_TIMEOUT:
                    print(f"Selenium timeout encountered, waiting {Timing.TIMEOUT}s before retrying")
                    time.sleep(Timing.TIMEOUT)
                elif result == Results.SELENIUM_NO_SUCH_ELEMENT:
                    print(f"Selenium NoSuchElementException encountered, waiting {Timing.NO_SUCH_ELEMENT}s before retrying")
                    time.sleep(Timing.NO_SUCH_ELEMENT)
                elif result == Results.SELENIUM_CLICK_INTERCEPTED:
                    print(f"Selenium ElementClickInterceptedException encountered, waiting {Timing.CLICK_INTERCEPTED}s before retrying")
                    time.sleep(Timing.CLICK_INTERCEPTED)
                else:
                    pass # todo nothing?
        else:
            print(f"Invalid brand option {brand}. Valid options are:\n{getCLIString(brandList)}")
    else:
        print(f"\nValid brand options:\n{getCLIString(brandList)}")
        return Results.BAD
    
    return Results.GOOD


####################################################################################################

# main section to run script

if __name__ == "__main__":
    args = makeArgs()

    start = time.time()
    status = driver(args)
    finish = time.time()

    hours, minutes, seconds = getTime(finish-start)

    # if status ==
    print("\nScraping took %0.2dh:%0.2dm:%2.3fs" % (hours, minutes, seconds))



