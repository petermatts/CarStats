import undetected_chromedriver as uc
from time import sleep

## Example Proxy
PROXY = "11.456.448.110:8080"

## Set Chrome Options
options = uc.ChromeOptions()
options.add_argument(f'--proxy-server={PROXY}')

## Create Undetected Chromedriver with Proxy
driver = uc.Chrome(options=options)

## Send Request
driver.get('https://caranddriver.com/mercedes-benz/e-class/specs')
sleep(60)