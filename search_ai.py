#!/usr/bin/env python3

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

def search_ai():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://help.fyi.me/")
    search_box = driver.find_element(By.NAME, "query")
    search_box.send_keys("AI")
    search_box.submit()
    time.sleep(5)
    search_results = BeautifulSoup(driver.page_source, "html.parser").find("h1").text
    if "15 results for" in search_results:
        print("Correct search results")
    else:
        print("Incorrect search results")
        print(f"Expected: 15 results for \"AI\"")
        print(f"Actual: {search_results}")
    driver.quit()

search_ai()