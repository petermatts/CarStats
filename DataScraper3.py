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

        default = {
            'link_idx': 0,
            'year_idx': 0,
            'year_text': '',
            'style_idx': 0,
            'style_text': '',
            'trim_idx': 0,
            'trim_text': ''
        }

        with open(path, 'w') as f:
            data = yaml.dump(default)
            f.write(data)
    
    try:
        with open(path, 'r') as file:
            data = yaml.safe_load(file)
            return data
    except:
        makeDebugFile(path)
        return openDebugFile(path)


def updateDebugFile(path: str, debug_data: dict):
    with open(path, 'w') as f:
        f.write(yaml.dump(debug_data))


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

####################################################################################################

# the scraping algorithm is composed of the functions in this section

def scrape(brand_filename: str, modelname: str = None, year: int = None, latest = False, test = False):
    """brand_filename is the path to the brands links in Links folder"""
    brand = brand_filename.split('/')[-1].replace('.txt', '')

    # get model links
    with open(brand_filename, 'r') as file:
        links = file.readlines()

    # open debug file (open with defaults if it doesn't exist)
    debug_path = Path(__file__).parent / brand + '.yaml'
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
        opts.add_argument('--ignore-certificate-errors')
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = uc.Chrome(opts)
        driver.implicitly_wait(Timing.IMPLICIT_WAIT)

        # todo keep going

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
        brand_links = Path(__file__) / "Links" / brand + ".txt"

        if os.path.isfile(brand_links):
            if args.show:
                print(f"Here are all models of brand {brand}:\nf{getCLIString(getModelList(brand))}")
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



