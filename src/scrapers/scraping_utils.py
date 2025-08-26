import time
import json
import os
from pathlib import Path
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common import exceptions


def open_browser():
    #Open the page in a chrome already open
    #First is necessary open chrome from the terminal: "chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Selenium"
    #Put the port 9222 and indicate that the user c:selenium will be the instance going to use
    print("Opening navegator")
    # command to execute in cmd
    command = r'start chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Selenium"'
    os.system(command)
    # Connect to depurate's port
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")  
    
    #open the driver that is already open
    driver = webdriver.Chrome(options=chrome_options)
    time.sleep(1)
    return driver

def scroll_page(driver, scroll_pause_time):
    #get the screen_height
    screen_height = driver.execute_script("return window.screen.height;")
    i = 1
    print("Scrolling page...")
    while True:
        #execute the scroll the size of the screen until arrive to end
        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
        i += 1
        time.sleep(scroll_pause_time)
        scroll_height = driver.execute_script("return document.body.scrollHeight;")  
        if (screen_height) * i > scroll_height:
            break


def get_html_class():

    with open("data/" "html_class_tk.json", "r") as f:
        return json.load(f)

def open_page_collection_from_profile(driver_chrome,paths):
    try:
        #Go to the page of the user
        driver_chrome.get(paths["link_home_page_tiktok"])
        #click in the button of favorite videos
        print("clicking in button Favorites")
        element = WebDriverWait(driver_chrome, 15).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(@class,'PFavorite')]"))
            )
        element.click()

        print("clicking in button collections")
        element = WebDriverWait(driver_chrome, 15).until(
        EC.element_to_be_clickable((By.ID, "collections"))
        )
        element.click()

        return True
    except exceptions.NoSuchElementException:
        print("Element didn't find" )
        return False
    except exceptions:
        print("Error Clicking the element" )
        return False
        