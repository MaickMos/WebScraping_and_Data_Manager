
def print_main_menu():
    print("----- // Downloader videos and data Tiktok // -----")
    print("---- Select what opction want to do: -----")
    print("1. Get Links of Collections from Web")
    print("2. Get Data from .csv and save in database")
    print("3.")

    option = "1"

    def get_link_collection():
        
        #link_tiktok_profile = input("Insert the link of the tiktok profile: ")
        return {
            "option": "1",
            }

    def load_csv():
        name_file_csv = input("Insert the name of the CVS file: ")
        database = input("Insert the name of the database")
        table = input("Insert the name of the table")
        return {
                "option": "2",
                "name_file_csv":name_file_csv,
                "database" : database,
                "table" : table,
                }

    menu_option = {
        "1": get_link_collection,
        "2": load_csv,
    }

    return menu_option.get(option,lambda: {"error": "Invalid"})()

