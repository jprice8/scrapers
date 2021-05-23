import os
import time 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()

# Set the folder you want to download the report to
# prefs = {'download.default_directory' : '/path/to/dir/'}
# options.add_experimental_option('prefs', prefs)

# Indicate we want the browser to be headless
options.headless = True 
driver = webdriver.Chrome(options=options)


driver.get('https://03280.xdhosted.com/rapidship/#/home')


# Input username and password for login
username = driver.find_element(By.XPATH, "//input[@formcontrolname='username']")
username.send_keys(os.environ.get('LAB_LOGISTICS_USERNAME'))

password = driver.find_element(By.XPATH, "//input[@formcontrolname='password']")
password.send_keys(os.environ.get('LAB_LOGISTICS_PASSWORD'))

login_button = driver.find_element(By.XPATH, "//button[@type='submit']").click()

try:
    element = WebDriverWait(driver, 5).until(
        EC.url_changes('https://03280.xdhosted.com/rapidship/#/home')
    )
finally:
    driver.get_screenshot_as_file('capture.png')
    driver.quit()
