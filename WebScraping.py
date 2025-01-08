import time
import json
import os
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    #get the labels <span>
    script  = "let labels = []; "
    script += "Array.from(document.getElementsByClassName('" + class_label + "')).forEach(item => { "
    script += "    let spans = item.querySelectorAll('span'); "
    script += "    spans.forEach(span => { labels.push(span.textContent); }); "  # Ad the text in a array
    script += "}); "
    script += "return labels;"
    labels = driver.execute_script(script)
    
    print(labels)
    
    number = []
    name = []
    count = []

    for text in labels:
        datos = text.split(".",1)
        if len(datos) == 2:
            number.append(datos[0])
            name.append(datos[1])
        else:
            name.append(datos[0])
        if 'videos' in datos:
            count.append(text.split()[0])

    return number,urlsToDownload,name,count
    #number,link,name,count

def OpenMainPageUser(link_home_page_tiktok,class_button_favorite):
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
    time.sleep(1)
    driver.get(link_home_page_tiktok)
    #click in the button of favorite videos
    Click("."+class_button_favorite.replace(" ","."))


#Get the path of the file, for .py or jupyter
try:
    #for pyhton file .py
    base_dir = Path(__file__).resolve().parent
except NameError:
    #For Jupyter Notebook
    base_dir = Path().resolve()

with open(base_dir / "html_class_tk.json", "r") as f:
    paths = json.load(f)

OpenMainPageUser(paths["link_home_page_tiktok"],paths["class_button_favorite"])

#get the list of the links of the collections
number,link,name,count = Getlinkstiktoksfrompage(paths["class_collection"],paths["class_label"])

print(number,link,name,count)
#Save in the database
database = "collection_tk"
table = "tiktok_links_v1"
#DB.Insert_in_column(table,table,collections)

#links = Getlinkstiktoksfrompage(class_tiktok_video)
#print(links)


print("Esperando para cerrar...")
time.sleep(60)
