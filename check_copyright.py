#! /usr/bin/env python3

import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def check_copyright_text():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://fyi.ai/")
    time.sleep(5)
    footer = driver.find_element(By.XPATH, "//footer//p")
    copyright_text = footer.text
    correct_copyright_text = "©2024 FYI.FYI, Inc."
    if correct_copyright_text in copyright_text:
        print("Test Passed")
    else:
        print("Test Failed")
    driver.quit()

check_copyright_text()