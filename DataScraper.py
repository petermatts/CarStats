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
    'Number of Transmission Speeds',
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
    'Turning Diameter / Radius, curb to curb (feet)',
    'Base Curb Weight (pounds)',
    'Maximum Towing Capacity (pounds)'
]

# scrape the desired data from the given url
def scrapeData(driver):
    url = driver.current_url
    print('Current URL:', url)

    specs = {
        'URL': url
    }

    # aquire title specs
    # 0     /1/ 2            / 3     / 4     / 5   / 6
    # https://caranddrive.com/<brand>/<model>/specs/<year>
    title_stuff = url.split('/')
    specs['Brand'] = ' '.join(list(map(lambda w: w.capitalize(), title_stuff[3].split('-')))) 
    specs['Model'] = ' '.join(list(map(lambda w: w.capitalize(), title_stuff[4].split('-')))) 

    if url != 'https://www.caranddriver.com/error':
        year = driver.find_element(By.CLASS_NAME, 'css-1an3ngc.ezgaj230')
        specs['Year'] = year.text.split(' ')[0]
        specs['Trim'] = year.text.replace('-', ' ').replace(specs['Model'], '').replace(specs['Brand'], '').replace(specs['Year'], '').replace('Features And Specs', '').strip()
        price = driver.find_element(By.CLASS_NAME, 'css-48aaf9.e1l3raf11')
        specs['Price'] = price.text.replace(',', '')

        # below is the main specs section
        data = driver.find_elements(By.CLASS_NAME, 'css-1ajawdl.eqxeor30')

        rows = []
        for i in range(len(data)):
            row = data[i].find_elements(By.TAG_NAME, 'div')
            if len(row) != 0:
                rows.append((row[0].text, row[1].text))

        for i in rows:
            if i[0] in target_specs:
                specs[i[0]] = i[1]
        
        # print(specs)
        # print('\n\n')
        writeFile(parseSpecs(specs))
    else:
        print('Possibly bad link:', url)


def parseSpecs(webspecs: dict):
    specs = {}
    isElectric = webspecs['Engine Type and Required Fuel'] == 'Electric'

    for i in list(webspecs.keys()):
        if webspecs[i] != 'NA': #? or '-TBD-' or ''
            if i == 'Brand' or i == 'Model' or i == 'Year' or i == 'Price' or i == 'Trim' or i == 'URL':
                specs[i] = webspecs[i]
            elif i == 'EPA Classification':
                specs['EPA Class'] = webspecs[i]
                # TODO parse to clarify
            elif i == 'Drivetrain':
                dt = webspecs[i].replace('Four', '4')
                specs[i] = ''.join(list(filter(lambda c: c.isupper() or c.isdigit(), dt)))
            elif i == 'Engine Type and Required Fuel':
                if isElectric:
                    specs['Engine'] = 'Electric'
                    specs['Fuel'] = 'Electric'
                else:
                    isHybrid = "Gas/Electric" in webspecs[i]
                    engine = re.search('\w-?\d+', webspecs[i])
                    if engine != None:
                        engine = webspecs[i][engine.span()[0]:engine.span()[1]].replace('-', '')
                        # specs['Engine'] = engine[:1] + '-' + engine[1:]
                        specs['Engine'] = engine
                        
                        # check turbos
                        if "Twin Turbo" in webspecs[i]:
                            specs['Turbos'] = '2'
                        elif "Turbo" in webspecs[i]:
                            specs['Turbos'] = '1'
                        else:
                            specs['Turbos'] = '0'

                        # check hybrid
                        if isHybrid:
                            specs['Fuel'] = 'Hybrid'
                        else:
                            gas = re.search("Regular|Premium|Gas", webspecs[i])
                            specs['Fuel'] = webspecs[i][gas.span()[0]:gas.span()[1]]
            elif i == 'Displacement (liters/cubic inches)':
                specs['Displacement (liters)'] = webspecs[i].split('/')[0].replace('L', '').strip()
            elif i == 'Maximum Horsepower @ RPM':
                hp = webspecs[i].split(' @ ')
                specs['Max Horsepower'] = hp[0]
                if not isElectric or len(hp) > 1: 
                    specs['Max Horsepower RPM'] = hp[1]
            elif i == 'Maximum Torque @ RPM':
                tq = webspecs[i].split(' @ ')
                specs['Max Torque'] = tq[0]
                if not isElectric or len(tq) > 1: 
                    specs['Max Torque RPM'] = tq[1]
            elif i == 'Transmission Description':
                specs['Transmission'] = webspecs[i].split(' ')[0]
            elif i == 'Number of Transmission Speeds':
                specs['Transmission Speeds'] = webspecs[i]
            elif not isElectric and i == 'EPA Fuel Economy, combined/city/highway (mpg)':
                fe = webspecs[i].replace('N/A', '').split('/')
                specs['MPG (combined)'] = fe[0].strip().split(' ')[0]
                specs['MPG (city)'] = fe[1].strip().split(' ')[0]
                specs['MPG (highway)'] = fe[2].strip().split(' ')[0]
            elif isElectric and i == 'EPA Fuel Economy Equivalent (for hybrid and electric vehicles), combined/city/highway (MPGe)':
                fe = webspecs[i].replace('N/A', '').split('/')
                specs['MPGe (combined)'] = fe[0].strip().split(' ')[0]
                specs['MPGe (city)'] = fe[1].strip().split(' ')[0]
                specs['MPGe (highway)'] = fe[2].strip().split(' ')[0]
            elif i == 'Fuel Capacity / Gas Tank Size':
                specs['Fuel Cap. (Gal)'] = webspecs[i]
            elif i == 'Length (inches)':
                specs['Length (in)'] = webspecs[i]
            elif i == 'Width, without mirrors (inches)':
                specs['Width, no mirrors (in)'] = webspecs[i]
            elif i == 'Height (inches)':
                specs['Height (in)'] = webspecs[i]
            elif i == 'Wheelbase (inches)':
                specs['Wheelbase (in)'] = webspecs[i]
            elif i == 'Passenger / Seating Capacity':
                specs['Seating Cap'] = webspecs[i]
            elif i == 'Total Passenger Volume (cubic feet)':
                specs['Passenger Space (cu ft)'] = webspecs[i]
            elif i == 'Trunk Space (cubic feet)':
                specs['Trunk Space (cu ft)'] = webspecs[i]
            elif i == 'Turning Diameter / Radius, curb to curb (feet)':
                try:
                    #TODO format to a certain decimal place?
                    specs['Turn Radius (ft)'] = str(float(webspecs[i])/2) # curb to curb
                except:
                    pass
            elif i == 'Base Curb Weight (pounds)':
                specs['Weight (lbs)'] = webspecs[i]
            elif i == 'Maximum Towing Capacity (pounds)':
                specs['Max Towing (lbs)'] = webspecs[i]
            else:
                pass
    return specs


def writeFile(specs: dict):
    base = open('./Docs/Base.csv', 'r')
    header = base.readline()
    base.close()

    # move to/write output directory
    brand = ''
    year = ''
    model = ''

    try:
        brand = specs['Brand'].replace(' ', '-')
        year = specs['Year']
        model = specs['Model'].replace(' ', '-')
    except:
        print('\nFailed\n')
        return

    # create directories if they do not exist
    if not os.path.isdir('Data'):
        os.mkdir('Data')
    os.chdir('Data')
    if not os.path.isdir(brand):
        os.mkdir(brand)
    os.chdir(brand)
    if not os.path.isdir(year):
        os.mkdir(year)
    os.chdir(year)

    try:
        f = open(model+'.csv', 'x')
        f.close()
    except:
        pass # file already exists

    file = open(model+'.csv', 'r')
    lines = file.readlines()
    file.close()

    if len(lines) == 0:
        lines = [header]

    keys = lines[0].strip().split(',')
    newline = ''
    for i in range(len(keys)):
        try:
            newline += specs[keys[i]] + ','
        except:
            newline += ','
    newline += '\n'

    if newline not in lines:
        lines.append(newline)

    file = open(model+'.csv', 'w')
    file.writelines(lines)
    file.close()
    os.chdir('../../../')
    

# function to go through all Links/{Brand}.txt files
# runtime will be atrocious
def scrape(i = None):
    os.chdir('Links')
    brands = os.listdir()
    if i != None:
        scrapeHelper(brands[i])
    else:
        for i in range(len(brands)):
            scrapeHelper(brands[i])
            time.sleep(10)
    os.chdir('../')

def scrapeHelper(filename: str):
    file = open(filename, 'r')
    models = file.readlines()
    file.close()
    opts = webdriver.ChromeOptions()
    opts.add_argument('start-maximized')
    driver = webdriver.Chrome(r"./driver/chromedriver", options=opts)
    
    sleep_const = 4

    # i = 0
    for i in range(len(models)):
        url = models[i].rstrip()
        try:
            driver.get(url)
        except:
            print('Bad URL:', url)
            return
        
        time.sleep(sleep_const)

        year_buttons = driver.find_element(By.ID, 'yearSelect').find_elements(By.TAG_NAME, 'option')[1:]
        year_buttons.reverse()
        for y in range(len(year_buttons)):
            year_buttons = driver.find_element(By.ID, 'yearSelect').find_elements(By.TAG_NAME, 'option')[1:]
            year_buttons.reverse()
            year_buttons[y].click()
            time.sleep(sleep_const)
            style_buttons = driver.find_element(By.ID, 'styleSelect').find_elements(By.TAG_NAME, 'option')[1:]
            for s in range(len(style_buttons)):
                style_buttons = driver.find_element(By.ID, 'styleSelect').find_elements(By.TAG_NAME, 'option')[1:]
                style_buttons[s].click()
                time.sleep(sleep_const)
                trim_buttons = driver.find_element(By.ID, 'trimSelect').find_elements(By.TAG_NAME, 'option')[1:]
                for t in range(len(trim_buttons)):
                    trim_buttons = driver.find_element(By.ID, 'trimSelect').find_elements(By.TAG_NAME, 'option')[1:]
                    print(trim_buttons[t].text)
                    trim_buttons[t].click()
                    time.sleep(sleep_const)

                    os.chdir('../')
                    scrapeData(driver)
                    os.chdir('Links')
        time.sleep(5)
        driver.close()
    

if __name__ == '__main__':
    # url = 'https://caranddriver.com/honda/accord/specs'
    # url = 'https://www.caranddriver.com/tesla/model-s/specs/2023/tesla_model-s_tesla-model-s_2023/433992'
    # url = 'https://www.caranddriver.com/toyota/4runner/specs/2022/toyota_4runner_toyota-4runner_2022/422563'
    # url = 'https://www.caranddriver.com/alfa-romeo/giulia-quadrifoglio/specs/2022/alfa-romeo_giulia-quadrifoglio_alfa-romeo-giulia-quadrifoglio_2022'
    # url = 'https://www.caranddriver.com/ford/f-150-lightning/specs/2022/ford_f-150-electric_ford-f-150-lightning_2022'
    # url = 'https://caranddriver.com/bugatti/chiron/specs'
    # scrapeData(url)
    scrape(20)
    