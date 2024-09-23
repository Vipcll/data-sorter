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
