import sqlite3
import pandas as pd


# LIMPIEZA Y AJUSTES DE ARCHIVO DE PYTHON A POWER BI


df = pd.read_csv("dataset.csv") # leo el archivo con pandas

conexion = sqlite3.connect("dataset.db") # conecto el sqlite con el archivo pero como es csv debo ponerle extension .db

columnas = df.columns # muestra los nombres de las columnas. ( opcional)

# correcion = archivo.isnull().sum() # muestra los nulos y los cuenta, bueniisimo par al limpieza de datos.

archivo_null = df.dropna() # borra todas las filas con nulls

archivo_column = df.drop(columns = ["Unnamed: 0"]) # borra la columna que le nombro en el parametro por default.



archivo.to_sql('dataset',conexion, if_exists='replace', index=False) # convertimos ya el archivo pasado a bd arriba a tabla sql

cursor = conexion.cursor() # conexion del cursor que es el que toca al sql.

sql_conection = cursor.execute("""
SELECT track_name, popularity 
    FROM dataset 
    ORDER BY popularity DESC 
    LIMIT 5

""")\

resultados = cursor.fetchall() # hacemos el fetch importantisimo! 


# Exporta tu dataset limpio directamente a CSV para Power BI
archivo.to_csv("spotify_limpio.csv", index=False)

print("¡Archivo CSV creado con éxito!")

conexion.close() # cerramos la conexion


print(resultados)
