from interface import print_main_menu

import handlers_db as DB
import scrapers.ecommerce_scraper as scraper



info = print_main_menu()

if(info.get("option") == "1"):
    try:
        driver_chrome, paths = scraper.open_page_collection()
        links_collections = scraper.get_links_collections_from_page(driver_chrome,paths)
    except:
        raise RuntimeError("Can't get links collections")


if(info.get("option") == "2"):
    data = DB.get_data_from_CSV(info.get("name_file_csv"))
    print(data)
    DB.Insert_in_column(info.get("database"),info.get("table"),info.get("data"))

if __name__ == "__main__":
    pass