def GetLinksTiktoks(link_cole):
    driver_chrome = scraping_utils.open_browser()

    #Change the tiktok link
    driver_chrome.get(link_cole)
    time.sleep(1)

    scraping_utils.scroll_page(driver_chrome,10)
    print("CORRECTO TODO")


    # this class may change, so make sure to inspect the page and find the correct class
    #LINK
    '''className = "tiktok-c83ctf-DivWrapper"
    script  = "let l = [];"
    script += "document.getElementsByClassName(\""
    script += className
    script += "\").forEach(item => { l.push(item.querySelector('a').href)});"
    script += "return l;"
    urlsToDownload = driver.execute_script(script)
    print(f"Found {len(urlsToDownload)} videos")
    return urlsToDownload'''


def get_links_videos_from_collection(link_colection):
    paths = scraping_utils.get_html_class()
    scraping_utils.open_browser()
    driver.get(link_colection)
    scraping_utils.scroll_page(1)

    # this class may change, so make sure to inspect the page and find the correct class
    #LINK
    className = paths["class_video_tiktok"]
    script  = "let l = [];"
    script += "document.getElementsByClassName(\""
    script += className
    script += "\").forEach(item => { l.push(item.querySelector('a').href)});"
    script += "return l;"

    urlsToDownload = driver.execute_script(script)
    print(f"Found {len(urlsToDownload)} videos")
    return urlsToDownload


Cabecera=True
totalvideos = []
# Abrir el archivo y leer sus líneas
with open("Link_cole.txt", mode='r', encoding='utf-8') as file:
    lines = file.readlines()
for line in lines:
    try:
        Cabecerasub=True
        num_cole, name_cole, link_cole = line.strip().split(',')
        print(name_cole)
        linkstiktok=GetLinksTiktoks(link_cole)
        totalvideos.append(name_cole+";"+str(len(linkstiktok)))
        #Save in main Database 
        with open("Links/LinksTikToks.csv", mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
        # Escribir la cabecera
            if Cabecera:
                writer.writerow(["ID_global","ID_colleccion","Name_Collecion","Link"])
            Cabecera=False
        SaveData(num_cole,name_cole,link_cole,linkstiktok,"Links/LinksTikToks.csv")
        #Save in sub-Database
        with open(f"Links/LinksTikToks{name_cole}.csv", mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
        # Escribir la cabecera
            if Cabecerasub:
                writer.writerow(["ID_global","ID_colleccion","Name_Collecion","Link"])
            Cabecerasub=False
        SaveData(num_cole,name_cole,link_cole,linkstiktok,f"Links/LinksTikToks{name_cole}.csv")
    except:
        with open("Links/Error.csv", mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(f"error en coleccion: {name_cole}")

with open("Links/Total_links.csv", mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
    # Escribir la cabecera
        writer.writerow(totalvideos)