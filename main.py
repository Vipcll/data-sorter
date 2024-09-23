import pandas as pd
import os

# Obtener la ruta del archivo en la misma carpeta que el script
ruta_del_archivo = os.path.join(os.path.dirname(__file__), 'sort.xlsx')
ruta_del_archivo_modificado = os.path.join(os.path.dirname(__file__), 'sort_modificado.xlsx')

# Cargar el archivo Excel
df = pd.read_excel(ruta_del_archivo, engine='openpyxl')

# Mostrar los nombres de las columnas (opcional, para verificar)
print("Nombres de las columnas:")
print(df.columns)

# Procesar la columna 'TEL 1' para extraer y mover el contenido después del '/'
df['TEL 2'] = df['TEL 1'].apply(lambda x: str(x).split('/')[1] if '/' in str(x) else '')
df['TEL 1'] = df['TEL 1'].apply(lambda x: str(x).split('/')[0] if '/' in str(x) else str(x))

# Guardar el archivo Excel modificado
df.to_excel(ruta_del_archivo_modificado, index=False, engine='openpyxl')

print("El archivo ha sido procesado y guardado correctamente.")
