from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

common_time = 10
options = webdriver.ChromeOptions()
options.add_argument('--headless')
# chrome_options.binary_location = '/Applications/Google Chrome   Canary.app/Contents/MacOS/Google Chrome Canary'`

s = Service(ChromeDriverManager().install())

# driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe', chrome_options=chrome_options)
driver = webdriver.Chrome(service=s, options=options)
login_path = "//button[text()='Login']"
email_path = "//input[@type='email']"
password_path = "//input[@type='password']"
login_button = "//button[@type='submit'][text()='Log in']"
title_announce_form = "//input[@name='title']"


# Functions
def waiter(by_type, path, time):
    WebDriverWait(driver, time).until(
        EC.presence_of_element_located((by_type, path)))


def sen_keys(by_type, path, text, time=common_time):
    waiter(by_type, path, time)
    driver.find_element(by_type, path).send_keys(text)


def just_clicker(by_type, path, time=common_time):
    waiter(by_type, path, time)
    driver.find_element(by_type, path).click()


def text_getter(by_type, path, time=common_time):
    waiter(by_type, path, time)
    return driver.find_element(by_type, path).text


def wait_till_invisibility(by_type, path, time=common_time):
    wait = WebDriverWait(driver, time)
    wait.until(EC.invisibility_of_element_located((by_type, path)))


def isDisplayed(by_type, path, time=common_time):
    wait = WebDriverWait(driver, time)
    wait.until(EC.presence_of_element_located((by_type, path)))
    return driver.find_element(by_type, title_announce_form).is_displayed()


driver.get("http://localhost:3000/signup")
driver.maximize_window()

# driver.set_context("content")

# driver.execute_script("document.body.style.zoom='80%'")
#
driver.implicitly_wait(common_time)

just_clicker(By.XPATH, login_path)
sen_keys(By.XPATH, email_path, "boomer@gmail.com")
sen_keys(By.XPATH, password_path, "Ravval01!")
just_clicker(By.XPATH, login_button)

if isDisplayed(By.XPATH, title_announce_form):
    print("Haraldo")

# sen_keys(By.XPATH, login_path)
# driver.find_element(By.XPATH, login_path)
