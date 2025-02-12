import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def contact_support_check():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://help.fyi.me/")
    #Find Contact Support button on page
    contact_support_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Contact Support']")))
    contact_support_button.click()
    #Wait to load Submit Request page
    time.sleep(5)
    #Verify page title
    page_title = driver.title
    if page_title == "Submit a request – FYI":
        print("Correct redirect")
    else:
        print("Incorrect redirect")
        print(f"Expected title: 'Submit a request – FYI'")
        print(f"Actual title: {page_title}")
    driver.quit()

contact_support_check()