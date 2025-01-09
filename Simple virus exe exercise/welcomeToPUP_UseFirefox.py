import os
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import WebDriverException

# Needs Firefox to be installed in the machine
def check_if_firefox_isInstalled():
    firefox_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    if not os.path.exists(firefox_path):
        print("Error: Firefox is not installed")
        return False
    return True

# Closes the windows of the browser
def close_current_window(driver):
    try:
        print("Info: Closing current browser window....")
        driver.close
        time.sleep(1)
    except WebDriverException:
        print("Error: unable to close browser window.")

# Opens window with pup link
def open_new_window_with_link(url):
    try:
        print("Entering PUP website.....")
        gecko_path = os.path.join(os.path.dirname(__file__), "driver\geckodriver.exe")
        service = Service(gecko_path)
        options = webdriver.FirefoxOptions()
        options.add_argument("--new-window")
        driver = webdriver.Firefox(service=service, options=options)
        driver.get(url)
        return driver
    except WebDriverException:
        print("Error: Unable to open Firefox. Make sure Firefox is installed")
        return None
    
# Uses the pup link
if __name__ == "__main__":
    if not check_if_firefox_isInstalled():
        exit()

    url = "https://www.pup.edu.ph/"
    driver = open_new_window_with_link(url)

    if driver:
        close_current_window(driver)
        driver = open_new_window_with_link(url)