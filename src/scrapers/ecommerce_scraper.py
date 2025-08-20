from scrapers import scraping_utils
import time
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def get_links_collection_from_profile_page():
    paths = scraping_utils.get_html_class()
    driver_chrome = scraping_utils.open_browser()
    
    scraping_utils.open_page_collection_from_profile(driver_chrome, paths)


