import sqlite3
import pandas as pd





df = pd.read_csv("dataset.csv") 

conexion = sqlite3.connect("dataset.db")
columnas = df.columns 

# correcion = archivo.isnull().sum() 

archivo_null = df.dropna() 

archivo_column = df.drop(columns = ["Unnamed: 0"]) 



archivo.to_sql('dataset',conexion, if_exists='replace', index=False) 

cursor = conexion.cursor() 

sql_conection = cursor.execute("""
SELECT track_name, popularity 
    FROM dataset 
    ORDER BY popularity DESC 
    LIMIT 5

""")\

resultados = cursor.fetchall() 



archivo.to_csv("spotify_limpio.csv", index=False)

print("¡Archivo CSV creado con éxito!")

conexion.close() # cerramos la conexion


print(resultados)
