from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import re

target_specs = [
    'EPA Classification',
    'Drivetrain',
    'Engine Type and Required Fuel',
    'Displacement (liters/cubic inches)',
    'Maximum Horsepower @ RPM',
    'Maximum Torque @ RPM',
    'Transmission Description',
    'Number of Transmission Speeds', #?
    'EPA Fuel Economy, combined/city/highway (mpg)',
    'EPA Fuel Economy Equivalent (for hybrid and electric vehicles), combined/city/highway (MPGe)',
    'Fuel Capacity / Gas Tank Size',
    'Length (inches)',
    'Width, without mirrors (inches)',
    'Height (inches)',
    'Wheelbase (inches)',
    'Passenger / Seating Capacity',
    'Total Passenger Volume (cubic feet)',
    'Trunk Space (cubic feet)',
    'Base Curb Weight (pounds)',
    'Maximum Towing Capacity (pounds)' #?
]

# function to go through all Links/*/SUMARRY.txt files
# Doesn't really do anything important rn... should play important role later
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

    specs = {}

    # aquire title specs
    # 0     /1/ 2            / 3     / 4     / 5   / 6
    # https://caranddrive.com/<brand>/<model>/specs/<year>
    title_stuff = url.split('/')
    specs['Brand'] = title_stuff[3].capitalize()
    specs['Model'] = title_stuff[4].capitalize()
    # ! specs['trim']

    price = driver.find_element(By.CLASS_NAME, 'css-48aaf9.e1l3raf11')
    specs['Price'] = price.text

    year = driver.find_element(By.CLASS_NAME, 'css-1an3ngc.ezgaj230')
    specs['Year'] = year.text.split(' ')[0]

    # below is the main specs section
    data = driver.find_elements(By.CLASS_NAME, 'css-1ajawdl.eqxeor30')
    # print(data)
    # print(dir(data[0]))

    rows = []
    for i in range(len(data)):
        row = data[i].find_elements(By.TAG_NAME, 'div')
        # print(row)
        if len(row) != 0:
            rows.append((row[0].text, row[1].text))
        # else:
        #     print(data[i].text)

    for i in rows:
        # print(i)
        if i[0] in target_specs:
            specs[i[0]] = i[1]
    
    print(specs)
    print('\n\n\n\n')
    print(parseSpecs(specs))

    time.sleep(100)

def parseSpecs(webspecs: dict):
    specs = {}

    #! still need to handle trim
    #! still need to handle hybrids
    #! still need to handle Fuel Type!
    #! still need to handle turbos
    #NOTE need to update CarStatsTargetData.pdf and CarStatsTargetData.xlsx

    for i in list(webspecs.keys()):
        if i == 'Brand' or i == 'Model' or i == 'Year' or i == 'Price':
            specs[i] = webspecs[i]
        elif i == 'EPA Classification':
            specs['EPA Class'] = webspecs[i]
        elif i == 'Drivetrain':
            specs[i] = ''.join(list(filter(lambda c: c.isupper(), webspecs[i])))
        elif i == 'Engine Type and Required Fuel':
            # TODO handle hybrids
            engine = re.search('\w-?\d+', webspecs[i])
            if engine != None:
                specs['Engine'] = webspecs[i][engine.span()[0]:engine.span()[1]]
            else:
                if webspecs[i] == 'Electric':
                    specs['Engine'] = webspecs[i]
        elif i == 'Displacement (liters/cubic inches)':
            specs['Displacement (liters)'] = webspecs[i].split('/')[0]
        elif i == 'Maximum Horsepower @ RPM':
            hp = webspecs[i].split(' @ ')
            specs['Max Horsepower'] = hp[0] #? need the Max part of the name?
            if len(hp) > 1: 
                specs['Max HP RPM'] = hp[1] #? rename
        elif i == 'Maximum Torque @ RPM':
            tq = webspecs[i].split(' @ ')
            specs['Max Torque'] = tq[0] #? need the Max part of the name?
            if len(tq) > 1: 
                specs['Max Torque RPM'] = tq[1]
        elif i == 'Transmission Description':
            specs['Transmission'] = webspecs[i].split(' ')[0]
        elif i == 'Number of Transmission Speeds':
            specs['Transmission Speeds'] = webspecs[i]
        elif i == 'EPA Fuel Economy, combined/city/highway (mpg)':
            fe = webspecs[i].split(' ')
            specs['MPG (combined)'] = fe[0].split(' ')[0]
            specs['MPG (city)'] = fe[1].split(' ')[0]
            specs['MPG (highway)'] = fe[2].split(' ')[0]
        elif i == 'EPA Fuel Economy Equivalent (for hybrid and electric vehicles), combined/city/highway (MPGe)':
            specs['MPGe (combined)'] = fe[0].split(' ')[0]
            specs['MPGe (city)'] = fe[1].split(' ')[0]
            specs['MPGe (highway)'] = fe[2].split(' ')[0]
        elif i == 'Fuel Capacity / Gas Tank Size':
            specs['Fuel Cap. (Gal)'] = webspecs[i]
        elif i == 'Length (inches)':
            specs['Length (in)'] = webspecs[i]
        elif i == 'Width, without mirrors (inches)':
            specs['Width *no mirrors* (in)'] = webspecs[i] # ? rename
        elif i == 'Height (inches)':
            specs['Height (in)'] = webspecs[i]
        elif i == 'Wheelbase (inches)':
            specs['Wheelbase (in)'] = webspecs[i]
        elif i == 'Passenger / Seating Capacity':
            specs['Seating Cap'] = webspecs[i]
        elif i == 'Total Passenger Volume (cubic feet)':
            specs['Passenger Space (cu. ft.)'] = webspecs[i]
        elif i == 'Trunk Space (cubic feet)':
            specs['Trunk Space (cu. ft.)'] = webspecs[i]
        elif i == 'Base Curb Weight (pounds)':
            specs['Weight (lbs)'] = webspecs[i]
        elif i == 'Maximum Towing Capacity (pounds)':
            specs['Max Towing (lbs)'] = webspecs[i]
        else:
            pass

    return specs

def writeFile(specs: dict):
    # move to/write output directory
    if not os.path.isdir('Data'):
        os.mkdir('Data')
    os.chdir('Data')
    if not os.path.isdir(specs['Brand']):
        os.mkdir(specs['Brand'])
    os.chdir(specs['Brand'])
    if not os.path.isdir(specs['Year']):
        os.mkdir(specs['Year'])
    os.chdir(specs['Year'])

if __name__ == '__main__':
    url = 'https://caranddriver.com/honda/accord/specs'
    scrapeData(url)
    