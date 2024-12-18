import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Connection_DB as DB

def ScrollPage(scroll_pause_time):
    #get the screen_height tes 
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

def Click(class_element):
    try:
        print("Doing Click in button collection")
        element = driver.find_element(By.CSS_SELECTOR, class_element)
        print("Waiting that existed the element")
        WebDriverWait(driver,10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR,class_element))
        )
        element.click()
        print("click")
        
    except Exception as error:
        print(f"Error en: {error}")

def Getlinkstiktoksfrompage(className,class_label):
    print("Getting links of videos...")

    wait = WebDriverWait(driver, 10)  # Espera hasta 10 segundos
    if className[0] == ".":
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,className.replace(" ","."))))
    else:
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "."+className.replace(" ","."))))
    
    #get the link
    script  = "let l = []; "
    script += "Array.from(document.getElementsByClassName(\"" +className + "\")).forEach(item => { "
    script += "    let link = item.querySelector('a'); "
    script += "    if (link) { l.push(link.href); } "
    script += "}); "
    script += "return l;"
    urlsToDownload = driver.execute_script(script)

    #get the label ////////Falta correr y hacer pruebas
    script  = "let l = []; "
    script += "Array.from(document.getElementsByClassName(\"" +class_label + "\")).forEach(item => { "
    script += "    let label = item.querySelector('span'); "
    script += "    if (label) { l.push(label.span); } "
    script += "}); "
    script += "return l;"


    print(f"Found {len(urlsToDownload)} links")

    return number,urlsToDownload,name,count

def OpenMainPageUser(link_home_page_tiktok):
    #driver = webdriver.Chrome()
    #Open the page in a chrome already open
    #First is necessary open chrome from the terminal: "chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Selenium"
    #Put the port 9222 and indicate that the user c:selenium will be the instance going to use
    print("Abriendo navegador")
    # Comando que deseas ejecutar
    command = r'start chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\Selenium"'
    # Ejecutar el comando
    os.system(command)

    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")  # Connect to depurate's port

    #open the driver that is already open
    global driver
    driver = webdriver.Chrome(options=chrome_options)
    #Go to the page of the user
    driver.get(link_home_page_tiktok)
    #click in the button of favorite videos
    Click("."+class_button_favorite.replace(" ","."))



link_home_page_tiktok = "https://www.tiktok.com/@maickmos"
class_button_favorite = "css-1wncxfu-PFavorite e1jjp0pq3"
class_collection = "css-13fa1gi-DivWrapper e1cg0wnj1"
class_tiktok_video = "css-8dx572-DivContainer-StyledDivContainerV2 eq741c50"
class_label = "css-12lihtw"
OpenMainPageUser(link_home_page_tiktok)

#get the list of the links of the collections
number,link,name,count = Getlinkstiktoksfrompage(class_collection,class_label)

print(number,link,name,count )
#Save in the database
database = "collection_tk"
table = "tiktok_links_v1"
#DB.Insert_in_column(table,table,collections)

#links = Getlinkstiktoksfrompage(class_tiktok_video)
#print(links)


print("Esperando para cerrar...")
time.sleep(60)
