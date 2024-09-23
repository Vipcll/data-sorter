import pandas as pd
import os

# Obtener la ruta del archivo en la misma carpeta que el script
ruta_del_archivo = os.path.join(os.path.dirname(__file__), 'sort.xlsx')

# Cargar el archivo Excel
df = pd.read_excel(ruta_del_archivo, engine='openpyxl')

# Mostrar las primeras filas del DataFrame y los nombres de las columnas
print("Primeras filas del DataFrame:")
print(df.head())

print("\nNombres de las columnas:")
print(df.columns)


""" 
Importa las bibliotecas necesarias: pandas para el manejo de datos y os para operaciones relacionadas con el sistema de archivos.

Define la ruta del archivo: Usa os.path.join y os.path.dirname(__file__) para construir la ruta del archivo sort.xlsx, asumiendo que el archivo se encuentra en la misma carpeta que el script.

Carga el archivo Excel: Lee el archivo sort.xlsx en un DataFrame de pandas usando el motor openpyxl.

Muestra las primeras filas del DataFrame: Imprime las primeras filas del DataFrame para proporcionar una vista preliminar de los datos.

Muestra los nombres de las columnas: Imprime los nombres de las columnas del DataFrame para facilitar la verificación de la estructura del archivo.

"""