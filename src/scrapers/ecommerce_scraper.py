from scrapers import scraping_utils
import time
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def open_page_collection():
    try:
        paths = scraping_utils.get_html_class()
        driver_chrome = scraping_utils.open_browser()
        if scraping_utils.open_page_collection_from_profile(driver_chrome, paths):
            return driver_chrome, paths
        else:
            raise RuntimeError("Can't open the page collection")
    except:
        raise RuntimeError("Error while open the page collection")

    
def get_links_collections_from_page(driver_chrome,paths):
    print("Getting links from collection page")
    time.sleep(5)
    scraping_utils.scroll_page(driver_chrome,10)
    script = """
    let collections = [];
    document.querySelectorAll('[data-e2e="collection-list-item"]').forEach(item => {
        let linkElem = item.querySelector("a");
        let footer = item.querySelector('[data-e2e="collection-card-footer"]');
        if(linkElem && footer){
            let spans = footer.querySelectorAll("span");
            let name = spans.length > 0 ? spans[0].textContent : "";
            let count = spans.length > 1 ? spans[1].textContent : "";
            collections.push({
                name: name,
                count: count,
                link: linkElem.href
            });
        }
    });
    return collections;
    """
    return driver_chrome.execute_script(script)
     


