import json
from pathlib import Path
import psycopg2


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


def Querry(database,querry):
    if ConnectionDB(database):
        try:
            cursor = connection.cursor()
            cursor.execute(querry)
            connection.commit()
            print("Querry Exitosa")

        except Exception as ex:
            print(f"Error al conectar a la base de datos: {ex}")
            connection.rollback()  # revert the transaction if there is a error
        finally:
            cursor.close()
            connection.close()