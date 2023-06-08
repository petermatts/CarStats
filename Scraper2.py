from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import re
import datetime
import json
import yaml

def scrapeData(driver: webdriver, specs: dict = {}):
    url = driver.current_url

    # specs = {
    #     'URL': url
    # }
    specs['URL'] = url

    title_stuff = url.split('/')
    specs['Brand'] = ' '.join(list(map(lambda w: w.capitalize(), title_stuff[3].split('-')))) 
    model = ' '.join(list(map(lambda w: w.capitalize(), title_stuff[4].split('-')))) 
    m = re.search("\d{4}$", model)
    # if m != None:
    if m != None and specs['Brand'] != 'Ram':
        model = model[:-4].rstrip()
        # model = model[:m.span()[0]]
    specs['Model'] = model

    driver.implicitly_wait(10)
    year = driver.find_element(By.CLASS_NAME, 'css-1an3ngc.ezgaj230')
    driver.implicitly_wait(0.01)

    #TODO  detect year and trim from specs dropdown options
    specs['Year'] = year.text.split(' ')[0]
    specs['Trim'] = year.text.replace('-', ' ').replace(specs['Model'], '').replace(specs['Brand'], '').replace(specs['Year'], '').replace('Features And Specs', '').strip()
    price = driver.find_element(By.CLASS_NAME, 'css-48aaf9.e1l3raf11')
    specs['Price'] = price.text.replace(',', '')

    data = driver.find_elements(By.CLASS_NAME, 'css-1ajawdl.eqxeor30')
    # rows = []
    for i in range(len(data)):
        # print(i+1, '/', len(data), end='\r')
        print('\tFind Data', i+1, end='\r')
        row = data[i].find_elements(By.TAG_NAME, 'div')
        if len(row) != 0:
            # rows.append((row[0].text.replace(',', ''), row[1].text.replace(',', '')))
            key = row[0].text.replace(',', '')
            value = row[1].text.replace(',', '')
            if key != '':
                specs[key] = value
        else:
            break #? optimize

    print()
    print('Specifications:')
    for i in specs:
        print(i, specs[i])

    return specs


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
    writeJSONData(data)

def scrapeBrand():
    pass

def makeFile(path: str, ext: str = '') -> bool:
    """
    Creates a new json file for the given path containing an empty array []
    Returns True if the file was created successfully and False if file already exists
    """
    print(path)
    cwd = os.getcwd()

    dirs = path.split('/')
    for d in dirs[:-1]:
        if not os.path.isdir(d):
            os.mkdir(d)
        os.chdir(d)

    # check if path already exists
    if os.path.isfile(dirs[-1]):
        os.chdir(cwd)
        return False
    
    if ext.lower() == 'json':
        with open(dirs[-1], 'w') as file:
            file.write('[]')

    os.chdir(cwd)
    return True


def writeJSONData(specs: dict):
    brand = specs['Brand']
    model = specs['Model']
    year = specs['Year']

    # make data file
    # path = './Data/JSON/' + brand + '/' + year + '/' + model + '.json'
    path = './Data/YAML/' + brand + '/' + year + '/' + model + '.yaml'
    makeFile(path, ext='yaml')

    # read existing data and write the new data to the file
    # data = None
    # contents = None
    # with open(path, 'r') as file:
    #     contents = json.load(file)

    #     if specs in contents: # if data was already found
    #         #? more efficient to go by URLs manually?
    #         #TODO ^^^
    #         return
        
    #     contents.append(specs)
    #     data = json.dumps(contents, indent = 4)
    
    # with open(path, 'w') as outfile:
    #     outfile.write(data)

    with open(path, 'a') as file:
        data = yaml.dump([specs])
        file.write(data)


if __name__ == "__main__":
    start = time.time()

    # scrape here
    URL = 'https://www.caranddriver.com/honda/accord/specs'
    scrapeByURL(URL)

    finish = time.time()
    runtime = finish-start
    hours = int(runtime/3600)
    runtime = runtime % 3600
    minutes = int(runtime/60)
    runtime = runtime % 60
    seconds = runtime
    print('\nScraping took %dh:%2dm:%2.3fs' % (hours, minutes, seconds))
