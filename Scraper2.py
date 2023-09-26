from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import sys
import requests
import os
import time
import datetime
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

def scrapeBrand(brand_filename: str):
    """brand_filename is the path to the brands links in Links folder"""
    brand = brand_filename.split('/')[-1].replace('.txt', '')

    timeout = 5 #? can be changed (seconds)
    sleep_const = 5 #? can be changed (seconds)

    # get links
    with open(brand_filename, 'r') as file:
        links = file.readlines()
    
    # open debug file (open with defaults if it doesn't exist)
    debug_path = './Debug/' + brand + '.yaml'
    debug = openDebugFile(debug_path)
    u = debug['link_idx']

    while u < len(links):
        url = links[u]
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
                years = driver.find_element(By.ID, 'react-select-2-listbox').find_elements(By.XPATH, './/*')[2:]
                years.reverse()
                debug['year_text'] = years[y].text
                years[y].click()
                time.sleep(sleep_const)

                styleSelect.click()
                styles = driver.find_element(By.ID, 'react-select-3-listbox').find_elements(By.XPATH, './/*')[2:]
                while s < len(styles):
                    styles = driver.find_element(By.ID, 'react-select-3-listbox').find_elements(By.XPATH, './/*')[2:]
                    debug['style_text'] = styles[s].text
                    styles[s].click()
                    time.sleep(sleep_const)

                    trimSelect.click()
                    trims = driver.find_element(By.ID, 'react-select-4-listbox').find_elements(By.XPATH, './/*')[2:]
                    while t < len(trims):
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

    # make data file
    path = './Data/YAML/' + brand + '/' + year + '/' + model.upper() + '.yaml'
    makeFile(path, ext='yaml')

    with open(path, 'a') as file:
        data = yaml.dump([specs])
        file.write(data)


def driver():
    """I hope anyone reading this can appreciate the pun that is this function name"""

    if len(sys.argv) > 1:
        


        path = './Links/' + sys.argv[1] + '.txt'

        if os.path.isfile(path):
            result = scrapeBrand(path)
            if result < 0:
                if result == -1:
                    print("Bad link encountered, skipping")
                    time.sleep(5)
                elif result == -2:
                    print("Request timeout encountered, waiting a bit before retrying")
                    time.sleep(180)
                elif result == -3:
                    print("Selenium timeout encountered, waiting a bit before retrying")
                    time.sleep(180)
                driver() # recursive call until successful completion of scrapping
        else:
            print('Invalid Brand Arguement. Valid Arguments are:')
            options = os.listdir('./Links')
            longest = 0
            for i in range(len(options)):
                options[i] = options[i][:-4]
                if len(options[i]) > longest:
                       longest = len(options[i])

            msg = ''
            for i in range(len(options)):
                msg += options[i]
                msg += ' '*(longest - len(options[i]) + 2)
                if i % 5 == 4:
                    msg += '\n'
            msg += '\n'
            print(msg)
    else:
        # I could probably clean this up a bit but its ok
        options = os.listdir('./Links')
        longest = 0
        for i in range(len(options)):
            options[i] = options[i][:-4]
            if len(options[i]) > longest:
                    longest = len(options[i])

        msg = ''
        for i in range(len(options)):
            msg += options[i]
            msg += ' '*(longest - len(options[i]) + 2)
            if i % 5 == 4:
                msg += '\n'
        msg += '\n'
        print('\nNo Scrapping brand arguments. Expected one of\n')
        print(msg)



"""
    To run: `python Scraper2.py {brand} {model} {--latest}`

    @param {brand} is REQUIRED
    @param {model} is optional
    @param {--latest} is optional
"""
if __name__ == "__main__":
    start = time.time()

    # scrape here
    # URL = 'https://www.caranddriver.com/honda/accord/specs'
    # scrapeByURL(URL)
    driver()

    finish = time.time()
    runtime = finish-start
    hours = int(runtime/3600)
    runtime = runtime % 3600
    minutes = int(runtime/60)
    runtime = runtime % 60
    seconds = runtime

    print('\nScraping took %dh:%2dm:%2.3fs' % (hours, minutes, seconds))
