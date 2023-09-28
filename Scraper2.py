from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
import datetime
import os
import re
import sys
import requests
import time
import yaml

def scrapeData(driver: webdriver, specs: dict = {}):
    specs['URL'] = driver.current_url

    # verify that link loads successfully
    r = requests.get(specs['URL'], timeout=5)

    if r.status_code != 200:
        raise ValueError(r.status_code)

    driver.implicitly_wait(10)
    price = driver.find_element(By.CLASS_NAME, 'css-11vbyw7.e1l3raf11')
    specs['Price'] = price.text.replace(',', '')

    data = driver.find_elements(By.CLASS_NAME, 'css-1ajawdl.eqxeor30')
    rows = []
    for i in range(len(data)):
        print('\tFind Data', i+1, end='\r')
        row = data[i].find_elements(By.TAG_NAME, 'div')
        if len(row) != 0:
            rows.append((row[0].text.replace(',', ''), row[1].text.replace(',', '')))
            key = row[0].text.replace(',', '')
            value = row[1].text.replace(',', '')
            if key != '':
                specs[key] = value
        else:
            break #? optimize

    # print()
    # print('Specifications:')
    # for i in specs:
    #     print(i, specs[i])

    # print('returining specs') # debugging

    return specs

def getSelectors(driver) -> tuple:
    select = driver.find_elements(By.CLASS_NAME, 'e1rdmryi0.cad-dropdown-filters__control.css-1l5x637-control')
    yearSelect, styleSelect, trimSelect = select
    return (yearSelect, styleSelect, trimSelect)

def scrapeBrand(brand_filename: str, modelname: str = None, year: int = None, latest: bool = False):
    """brand_filename is the path to the brands links in Links folder"""
    brand = brand_filename.split('/')[-1].replace('.txt', '')

    timeout = 5 #? can be changed (seconds)
    sleep_const = 3 #? can be changed (seconds)

    # get links
    with open(brand_filename, 'r') as file:
        links = file.readlines()
    
    # open debug file (open with defaults if it doesn't exist)
    debug_path = './Debug/' + brand + '.yaml'
    debug = openDebugFile(debug_path)
    u = debug['link_idx']

    while u < len(links):
        url = links[u]

        if modelname != None and url.split('/')[4].lower() != modelname.lower():
            # if model param is valid and url is not of the model... skip it
            u += 1
            continue


        opts = webdriver.ChromeOptions()
        opts.add_argument('start-maximized')
        opts.add_argument('--ignore-certificate-errors')
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(options=opts)
        driver.implicitly_wait(timeout) #? static, only needs to be called once per session

        model = links[u].split('/')[4]

        try:
            driver.get(url)
            r = requests.get(url, timeout=5)
            if r.status_code == 404: #? or do != 200
                # print('status', r.status_code)
                raise ValueError()
        except:
            print('Bad URL:', url)
            with open('Log/BadScrapeLinks.log', 'a') as file:
                file.write(url)
            u += 1
            debug['link_idx'] = u
            updateDebugFile(debug_path, debug)
            continue

        # iterative scraping over dropdown like in old scraper, updating debug file
        try:
            yearSelect, styleSelect, trimSelect = getSelectors(driver)
            yearSelect.click()
            years = driver.find_element(By.ID, 'react-select-2-listbox').find_elements(By.XPATH, './/*')[2:]
            years.reverse()

            time.sleep(sleep_const)

            y = debug['year_idx']
            s = debug['style_idx']
            t = debug['trim_idx']

            while y < len(years):
                time.sleep(sleep_const)
                years = driver.find_element(By.ID, 'react-select-2-listbox').find_elements(By.XPATH, './/*')[2:]
                years.reverse()

                if latest and y < len(years)-1:
                    # skip to latest year if latest param is true
                    y += 1
                    continue
                elif year != None and int(years[y].text) != year:
                    # only scrape specified year if year is defined
                    y += 1
                    continue

                debug['year_text'] = years[y].text
                years[y].click()
                time.sleep(sleep_const)

                styleSelect.click()
                styles = driver.find_element(By.ID, 'react-select-3-listbox').find_elements(By.XPATH, './/*')[2:]
                while s < len(styles):
                    time.sleep(sleep_const)
                    styles = driver.find_element(By.ID, 'react-select-3-listbox').find_elements(By.XPATH, './/*')[2:]
                    debug['style_text'] = styles[s].text
                    styles[s].click()
                    time.sleep(sleep_const)

                    trimSelect.click()
                    trims = driver.find_element(By.ID, 'react-select-4-listbox').find_elements(By.XPATH, './/*')[2:]
                    while t < len(trims):
                        time.sleep(sleep_const)
                        trims = driver.find_element(By.ID, 'react-select-4-listbox').find_elements(By.XPATH, './/*')[2:]
                        debug['trim_text'] = trims[t].text
                        trims[t].click()
                        time.sleep(sleep_const)

                        updateDebugFile(debug_path, debug)

                        init_specs = {
                            'Brand': brand,
                            'Year': debug['year_text'],
                            'Model': model,
                            'Style': debug['style_text'],
                            'Trim': debug['trim_text'],
                        }

                        print(debug['year_text'], debug['style_text'], debug['trim_text'])
                        data = None
                        try:
                            data = scrapeData(driver, init_specs)
                        except ValueError:
                            t += 1
                            debug['trim_idx'] = t
                            updateDebugFile(debug_path, debug)
                            return -1
                        except requests.HTTPError:
                            return -2

                        writeData(data)

                        try:
                            yearSelect, styleSelect, trimSelect = getSelectors(driver)
                        except:
                            pass
                        trimSelect.click()
                        t += 1
                        debug['trim_idx'] = t
                    try:
                        yearSelect, styleSelect, trimSelect = getSelectors(driver)
                    except:
                        pass
                    styleSelect.click()
                    s += 1
                    debug['style_idx'] = s
                    t = 0
                    debug['trim_idx'] = t
                    # debug['trim_text'] = ''
                try:
                    yearSelect, styleSelect, trimSelect = getSelectors(driver)
                except:
                    pass
                yearSelect.click()
                y += 1
                debug['year_idx'] = y
                s = 0
                debug['style_idx'] = s
                # debug['style_text'] = ''
        except TimeoutException:
            return -3
        # except NoSuchElementException:
        #   return -4
        # except ElementClickInterceptedException:
        #   #? advance to next iteration (trim/style/year)?
        #   return -5
        
        # sort of like a reset - resets years but not links
        y = 0
        debug['year_idx'] = y
        u += 1
        debug['link_idx'] = u
        updateDebugFile(debug_path, debug)

    return 1 # success :)


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


def makeFile(path: str, ext: str = '') -> bool:
    """
    Creates a new json file for the given path containing an empty array []
    Returns True if the file was created successfully and False if file already exists
    """
    # print(path)

    # check path exists before doing anything else
    if os.path.isfile(path):
        return False

    cwd = os.getcwd()

    dirs = path.split('/')
    for d in dirs[:-1]:
        if not os.path.isdir(d):
            os.mkdir(d)
        os.chdir(d)

    # check if path already exists
    # if os.path.isfile(dirs[-1]):
    #     os.chdir(cwd)
    #     return False
    
    if ext.lower() == 'json':
        with open(dirs[-1], 'w') as file:
            file.write('[]')

    os.chdir(cwd)
    return True


def writeData(specs: dict[str, str]):
    brand = specs['Brand']
    model = specs['Model']
    year = specs['Year']

    print("\tWriting data ", end="\r")

    # make data file
    path = './Data/YAML/' + brand + '/' + year + '/' + model.upper() + '.yaml'
    makeFile(path, ext='yaml')

    with open(path, 'a') as file:
        data = yaml.dump([specs])
        file.write(data)

    print("\tDone!        ", end="\r")


def driver():
    """I hope anyone reading this can appreciate the pun that is this function name"""

    def getBrandList():
        options = os.listdir('./Links')
        longest = 0
        for i in range(len(options)):
            options[i] = options[i][:-4]
            if len(options[i]) > longest:
                    longest = len(options[i])

        brands = ''
        for i in range(len(options)):
            brands += options[i]
            brands += ' '*(longest - len(options[i]) + 2)
            if i % 5 == 4:
                brands += '\n'
        brands += '\n'
        return brands

    def getModelList():
        # NOTE: precondition that --help flag must be supplied after brand
        with open('./Links/'+sys.argv[1]+'.txt', 'r') as f:
            lines = f.readlines()

        options = []
        longest = 0
        for line in lines:
            model = line.split('/')[4]
            options.append(model)
            if len(model) > longest:
                longest = len(model)

        models = ''
        for i in range(len(options)):
            models += options[i]
            models += ' '*(longest - len(options[i]) + 2)
            if i % 5 == 4:
                models += '\n'
        models += '\n'
        return models  

    brands = getBrandList()

    # get option parameters for scraper
    model = None
    year = None
    latest = "--latest" in sys.argv
    r = re.compile("--\d\d\d\d") # find year arguement
    ys = list(filter(r.match, sys.argv))
    if len(ys) == 1:
        year = int(ys[0].split('-')[-1])
    # end option configuration

    if len(sys.argv) > 1:
        path = './Links/' + sys.argv[1] + '.txt'

        if os.path.isfile(path):
            if len(sys.argv) > 2 and sys.argv[2] == "--help":
                print("Here are all models of brand", sys.argv[1] + ":\n")
                print(getModelList())
                return -1
            elif len(sys.argv) > 2:
                model = sys.argv[2]

            result = scrapeBrand(path, modelname=model, year=year, latest=latest)
            if result < 0:
                if result == -1:
                    print("Bad link encountered, skipping")
                    time.sleep(5)
                elif result == -2:
                    print("Request timeout encountered, waiting 2m before retrying")
                    time.sleep(120)
                elif result == -3:
                    print("Selenium timeout encountered, waiting 2m before retrying")
                    time.sleep(120)
                elif result == -4:
                    print("Selenium NoSuchElementException encountered, waiting 10s before retrying")
                    time.sleep(10)
                elif result == -5:
                    print("Selenium ElementClickInterceptedException encountered, waiting 30s before retrying")
                    time.sleep(30)

                driver() # recursive call until successful completion of scrapping
        else:
            print('Invalid Brand Arguement. Valid Arguments are:')
            print(brands)
            return -1
    else:
        print('\nNo Scrapping brand arguments. Expected one of\n')
        print(brands)
        return -1

    return 1


"""
    To run: `python Scraper2.py {brand} {model|--help} {--latest|--year}`

    @param {brand} is REQUIRED
    @param {model} is optional
    @param {--help} is optional
    @param {--latest} is optional
    @param {--year} is optional (example --2024)

    Important note: {model} and {--help} parameters cannot be used together
    Important note: {--latest} and {--year} parameters cannot be used together
"""
if __name__ == "__main__":
    start = time.time()

    # scrape here
    # URL = 'https://www.caranddriver.com/honda/accord/specs'
    # scrapeByURL(URL)
    status = driver()

    finish = time.time()
    runtime = finish-start
    hours = int(runtime/3600)
    runtime = runtime % 3600
    minutes = int(runtime/60)
    runtime = runtime % 60
    seconds = runtime

    if status == 1:
        print('\nScraping took %dh:%2dm: %2.3fs' % (hours, minutes, seconds))
