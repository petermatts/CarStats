from selenium import webdriver
from selenium.webdriver.common.by import By
import sys
import requests
import os
import time
import re
import datetime
import yaml
# import json

#? am I using async/await properly here? --- test to find out
async def scrapeData(driver: webdriver, specs: dict = {}):
    specs['URL'] = driver.current_url

    # verify that link loads successfully
    r = await requests.get(specs['URL'])
    # r.raise_for_status() #? use this instead of below conditional
    if r.status_code != 200:
        raise ValueError(r.status_code)

    driver.implicitly_wait(10)
    price = driver.find_element(By.CLASS_NAME, 'css-48aaf9.e1l3raf11')
    specs['Price'] = price.text.replace(',', '')

    data = driver.find_elements(By.CLASS_NAME, 'css-1ajawdl.eqxeor30')
    rows = []
    for i in range(len(data)):
        # print(i+1, '/', len(data), end='\r')
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

# for testing purposes
def scrapeByURL(url: str, start_year = datetime.date.today().year):
    opts = webdriver.ChromeOptions()
    opts.add_argument('start-maximized')
    
    driver = webdriver.Chrome(r"./driver/chromedriver", options=opts)
    driver.implicitly_wait(5)
    try:
        driver.get(url)
    except:
        print('Bad URL:', url)
        return
    
    url = driver.current_url
    year_buttons = driver.find_element(By.ID, 'yearSelect').find_elements(By.TAG_NAME, 'option')[1:]
    year_buttons.reverse()
    
    print(url)

    data = scrapeData(driver)
    writeData(data)


def scrapeBrand(brand_filename: str):
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
        opts = webdriver.ChromeOptions()
        opts.add_argument('start-maximized')
        driver = webdriver.Chrome(r"./driver/chromedriver", options=opts)
        driver.implicitly_wait(timeout) #? static, only needs to be called once per session

        model = links[u].split('/')[4]

        try:
            driver.get(url)
        except:
            print('Bad URL:', url)
            u += 1
            continue

        # iterative scraping over dropdown like in old scraper, updating debug file
        # TODO get it to call itself again with debug values if error occurs
        # ? move this into the try block for get(url)
        try:
            #! check to make sure driver did not find an error link

            year_buttons = driver.find_element(By.ID, 'yearSelect').find_elements(By.TAG_NAME, 'option')[1:]
            year_buttons.reverse()
            y = debug['year_idx']
            s = debug['style_idx']
            t = debug['trim_idx']

            while y < len(year_buttons):
                driver.implicitly_wait(timeout) #? static, only needs to be called once per session
                year_buttons = driver.find_element(By.ID, 'yearSelect').find_elements(By.TAG_NAME, 'option')[1:]
                year_buttons.reverse()

                debug['year_text'] = year_buttons[y].text
                year_buttons[y].click()
                time.sleep(sleep_const)

                style_buttons = driver.find_element(By.ID, 'styleSelect').find_elements(By.TAG_NAME, 'option')[1:]
                while s < len(style_buttons):
                    driver.implicitly_wait(timeout) #? static, only needs to be called once per session
                    style_buttons = driver.find_element(By.ID, 'styleSelect').find_elements(By.TAG_NAME, 'option')[1:]

                    debug['style_text'] = style_buttons[s].text
                    style_buttons[s].click()
                    time.sleep(sleep_const)

                    trim_buttons = driver.find_element(By.ID, 'trimSelect').find_elements(By.TAG_NAME, 'option')[1:]
                    while t < len(trim_buttons):
                        driver.implicitly_wait(timeout) #? static, only needs to be called once per session
                        trim_buttons = driver.find_element(By.ID, 'trimSelect').find_elements(By.TAG_NAME, 'option')[1:]                  
                        debug['trim_text'] = trim_buttons[t].text
                        trim_buttons[t].click()

                        updateDebugFile(debug_path, debug)

                        init_specs = {
                            'Brand': brand,
                            'Year': debug['year_text'],
                            'Model': model,
                            'Style': debug['style_text'],
                            'Trim': debug['trim_text'],
                        }

                        # scrapeData(driver)
                        print(debug['year_text'], debug['style_text'], debug['trim_text'])
                        data = scrapeData(driver, init_specs)

                        writeData(data)

                        # time.sleep(5) # for testing
                        # updateDebugFile(debug_path, debug)

                        t += 1
                        debug['trim_idx'] = t

                    s += 1
                    debug['style_idx'] = s
                    t = 0
                    debug['trim_idx'] = t
                    # debug['trim_text'] = ''

                y += 1
                debug['year_idx'] = y
                s = 0
                debug['style_idx'] = s
                # debug['style_text'] = ''
        except:
            pass
        
        # print(links[u].rstrip())
        y = 0
        debug['year_idx'] = y
        u += 1
        debug['link_idx'] = u
        updateDebugFile(debug_path, debug)


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
    # print('making file') # debugging
    makeFile(path, ext='yaml')
    # print('made file') # debugging

    # print('writing to file') # debugging
    with open(path, 'a') as file:
        data = yaml.dump([specs])
        file.write(data)
    # print('done') # debugging


def driver():
    """I hope anyone reading this can appreciate the pun that is this function name"""

    # TODO


if __name__ == "__main__":
    # start = time.time()

    # scrape here
    # URL = 'https://www.caranddriver.com/honda/accord/specs'
    # scrapeByURL(URL)

    # finish = time.time()
    # runtime = finish-start
    # hours = int(runtime/3600)
    # runtime = runtime % 3600
    # minutes = int(runtime/60)
    # runtime = runtime % 60
    # seconds = runtime
    # print('\nScraping took %dh:%2dm:%2.3fs' % (hours, minutes, seconds))

    # scrapeBrand('./Links/Honda.txt')
    scrapeBrand('./Links/Tesla.txt')



