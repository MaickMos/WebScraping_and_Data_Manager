import json
from pathlib import Path
import pandas as pd
import psycopg2

def get_data_from_CSV(file):
    #A JSON is used to save all the path from the desktop
    #We obtain the main path of the project
    try:
        #for pyhton file .py
        base_dir = Path(__file__).resolve().parent
    except NameError:
        #For Jupyter Notebook
        base_dir = Path().resolve()
    #path(): returns a object type path
    #.resolve: resolve posible issues eith the path
    with open(base_dir / "config.json", "r") as f:
        paths = json.load(f)
        #Convert a file json in a dictonary
    #Creacion de DataFrame en pandas
    datos= pd.read_csv(base_dir / paths[file])
    return datos

def ConnectionDB(database):
    try:
        global connection
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password = '1234',
            database = database
        )
        print("Correct connection to database")
        return True

    except Exception as ex:
        print(f" Error connecting to database: {ex}")
        return False


def Insert_in_column(database,table,datos):
    #for psycopg2 the table is necessary to be in lowercase, even declarad in the DB
    if ConnectionDB(database):
        
        try:
            cursor=connection.cursor()
            encabezados = datos.columns
            
            #datos['ID_global'].iloc[1] #to get a specific data based in index
            for i,_ in enumerate(datos.iterrows()):
                row = datos.iloc[i]
                
                value = "("
                for j,_ in enumerate(encabezados):
                    if isinstance(row[encabezados[j]],str):
                        value += f"'{row[encabezados[j]]}',"
                    else:
                        value += f"{str(row[encabezados[j]])},"

                    #value = value+str(row[encabezados[j]])+","
                value = value[:-1]+")"
                
                try:
                    cursor.execute(f"INSERT INTO {table} VALUES {value}")
                    print("executed: "+f"INSERT INTO {table} VALUES {value}")
                except Exception as ex:
                    print(f"error in the transaction: {ex}")

            connection.commit()
            print("Upload Correctly")
            return True
            
        except Exception as error:
            print(f"Error modifying the table: {error}")
            connection.rollback()  # revert the transaction if there is a error
        finally:
            cursor.close()
            connection.close()

def Querry(database,consult):
    #Connecto to DB
    if ConnectionDB(database):
        try:
            cursor = connection.cursor()
            cursor.execute(consult)
            
            #if a querry:
            if consult.strip().upper().startswith("SELECT"):
                result= cursor.fetchall()
                print("Querry successful")
                return result
            
            #if diferent to a Querry
            connection.commit()
            print("Changes applied")
            

        except Exception as ex:
            print(f"Error al conectar a la base de datos: {ex}")
            connection.rollback()  # revert the transaction if there is a error
        finally:
            cursor.close()
            connection.close()
        
def get_data_from_DB(database,table):
        #database = "collection_tk"
    #table = "tiktok_links_v1"
    #get the links of collections from DB
    #get the number of collections
    consult = f"SELECT COUNT(name) FROM {table}"
    resultado = Querry(database,consult)
    print(resultado)
    for i in len(resultado):
        consult = f"SELECT * FROM {table} where ID = {i}"
        resultado = Querry(database,consult)
        #DB.Insert_in_column(database,table,resultado)
        #agregar una comprobacion de los datos antes de subir a la base de datos

#function main, is execute when the script is running directly
def main():
    raise NotImplementedError
#check if this file is execute like a module or directly.
#If is a module not execute the function main
if __name__ == "__main__":
    main()