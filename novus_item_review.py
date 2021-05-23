import os
import time 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#### 23 Second Best Script Run Time ####


options = webdriver.ChromeOptions()
# Set the folder you want to download the report to
# prefs = {'download.default_directory' : '~/devs/data/item_review/'}
# options.add_experimental_option('prefs', prefs)
options.headless = True 
driver = webdriver.Chrome(options=options)


def wait_for_xlsx_download():
    print('Waiting for downloaded excel file...', end='')
    while not any([filename.endswith('.xlsx') for filename in os.listdir('/Users/jacksonprice/devs/Python/scripts/selenium/')]):

        time.sleep(2)
        print('.', end='')

    print('done!')


#### HIT LANDING PAGE
driver.get('https://www.novusreach.com/')
# Wait for the url to appear
driver.implicitly_wait(10)


#### AUTH ####
# Click the log in button to pop out creds modal
driver.find_element(By.ID, "userLoginButtonIcon").click()

# Input username and password for login
username = driver.find_element(By.XPATH, "//input[@data-bind='hasFocus: promptFocus(), textInput: userName']")
username.send_keys(os.environ.get('NOVUS_USERNAME'))

password = driver.find_element(By.XPATH, "//input[@type='password']")
password.send_keys(os.environ.get('NOVUS_PASSWORD'))

# Click the login button
driver.find_element(By.XPATH, "//button[@type='submit']").click()
# Wait to login
driver.implicitly_wait(10)


#### SELECT ITEM REVIEW REPORT ####
driver.find_element(By.XPATH, "//li[@class='ui-sortable-handle'][9]").click()
# Wait for item review form to appear
time.sleep(1)
download_button = driver.find_element(By.XPATH, "//button[@title='Download Center']")

# # Use JS to click on button cus it DGAF
driver.execute_script("arguments[0].click();", download_button)

time.sleep(1)
locator = (By.XPATH, "//button[@data-bind='click: download']")
driver.find_element(*locator).click()
print('Download Final Clicked')

# Waits for all the files to be completed and returns the paths
wait_for_xlsx_download()
# paths = WebDriverWait(driver, 120, 1).until(wait_for_downloads)
# print(paths)

driver.get_screenshot_as_file('novus_capture.png')
driver.quit()

