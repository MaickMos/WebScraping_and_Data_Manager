import time
import json
import os
from pathlib import Path
from selenium import webdriver

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def open_browser():
    #Open the page in a chrome already open
    #First is necessary open chrome from the terminal: "chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Selenium"
    #Put the port 9222 and indicate that the user c:selenium will be the instance going to use
    print("Abriendo navegador")
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

def click(driver_chrome,class_element):
    try:
        print("clicking in button collection")
        element = driver_chrome.find_element(By.XPATH, "//* [contains(@class, 'PFavorite')]")
        print("Waiting that existed the element")
        WebDriverWait(driver_chrome,10).until(
            EC.presence_of_all_elements_located(By.XPATH, "//* [contains(@class, 'PFavorite')]")
        )
        element.click()
        print("click")
        
    except Exception as error:
        print(f"Error en: {error}")

def get_html_class():

    with open("data/" "html_class_tk.json", "r") as f:
        return json.load(f)

def open_page_collection_from_profile(driver_chrome,paths):
    #Go to the page of the user
    driver_chrome.get(paths["link_home_page_tiktok"])
    
    #click in the button of favorite videos
    click(driver_chrome,"."+paths["class_button_favorite"])#.replace(" ","."))