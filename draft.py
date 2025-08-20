

def get_links_collections_from_page(driver_chrome,class_collection,class_text):
    with open("data" / "html_class_tk.json", "r") as f:
        paths = json.load(f)

    className = paths["class_collection"]
    class_label = paths["class_text"]
    print("Getting links of videos...")

    wait = WebDriverWait(driver_chrome, 10)  # wait 10 seconds for cathcath

    #get the link
    script  = "let l = []; "
    script += "Array.from(document.getElementsByClassName(\"" +className + "\")).forEach(item => { "
    script += "    let link = item.querySelector('a'); "
    script += "    if (link) { l.push(link.href); } "
    script += "}); "
    script += "return l;"
    urlsToDownload = driver_chrome.execute_script(script)

    #get the labels <span>
    script  = "let labels = []; "
    script += "Array.from(document.getElementsByClassName('" + class_label + "')).forEach(item => { "
    script += "    let spans = item.querySelectorAll('span'); "
    script += "    spans.forEach(span => { labels.push(span.textContent); }); "  # Ad the text in a array
    script += "}); "
    script += "return labels;"
    labels = driver_chrome.execute_script(script)
    
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