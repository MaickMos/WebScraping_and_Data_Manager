import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#Open the page in a chrome already open
#First is necessary open chrome from the terminal: chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Selenium"
#Put the port 9222 and indicate that the user c:selenium will be the instance going to use
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")  # Connect to depurate's port

def ScrollPage(scroll_pause_time):
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

link = "https://www.tiktok.com/@maickmos"
#driver = webdriver.Chrome()
driver = webdriver.Chrome(options=chrome_options)
driver.get(link)
time.sleep(10)

try:
    print("Doing Click in button Favorite")
    button_favorate = driver.find_element(By.CLASS_NAME, "css-1wncxfu-PFavorite e1jjp0pq3")
    button_favorate.click()
    time.sleep(10)
    print("Doing Click in button collection")
    button_favorate = driver.find_element(By.CLASS_NAME, "TUXButton-content")
    button_favorate.click()
    
except Exception as error:
    print("Error en: ")



input("Presiona Enter para continuar...")
