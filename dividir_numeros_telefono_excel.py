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


"""" 
Importa las bibliotecas necesarias: pandas para el manejo de datos y os para operaciones relacionadas 
con el sistema de archivos.

Define las rutas de los archivos: Usa os.path.join y os.path.dirname(__file__) para construir las rutas 
absolutas del archivo de entrada (sort.xlsx) y del archivo de salida (sort_modificado.xlsx), 
asumiendo que ambos archivos están en la misma carpeta que el script.

Carga el archivo Excel: Lee el archivo sort.xlsx usando pandas con el motor openpyxl.

Muestra los nombres de las columnas: Imprime los nombres de las columnas del DataFrame cargado para verificar
 su estructura.

Procesa la columna 'TEL 1':

Extrae el contenido después de '/': Si en una celda de 'TEL 1' hay un '/', extrae el contenido después de este
carácter y lo coloca en una nueva columna llamada 'TEL 2'.

Actualiza la columna 'TEL 1': Modifica 'TEL 1' para que solo contenga el contenido antes del '/' 
(o la celda original si no hay '/').

Guarda el archivo Excel modificado: Escribe el DataFrame modificado en un nuevo archivo 
llamado sort_modificado.xlsx, sin incluir los índices del DataFrame.

El propósito de este script es dividir el contenido de la columna 'TEL 1' en dos columnas, 
separadas por el carácter '/' y guardar los resultados en un nuevo archivo.

"""