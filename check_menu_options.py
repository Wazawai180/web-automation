#!/usr/bin/env python3

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def check_menu_options():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://fyi.ai/")
    #Click hamburger menu to expand menu options
    hamburger_menu = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@class='menu-collapse']")))
    hamburger_menu.click()
    #Wait for menu to open
    time.sleep(2)
    #Find options in menu
    menu_options = driver.find_elements(By.XPATH, "//*[@class='u-nav-item']/a")
    menu_options_text = [option.text.strip() for option in menu_options if option.text.strip() != '']
    correct_menu_options = ['Home', 'Help', 'About us', 'The Team', 'Press', 'Terms of Service', 'Privacy Policy']
    if menu_options_text == correct_menu_options:
        print("Test Passed")
    else:
        print("Test Failed")
        print(f"Expected: {correct_menu_options}")
        print(f"Actual: {menu_options_text}")
    driver.quit()

check_menu_options()