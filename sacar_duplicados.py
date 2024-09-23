import pandas as pd

# Leer los archivos Excel
df_casa_depto = pd.read_excel('Ordenando.xlsx')
df_auto_marca = pd.read_excel('Ordenando2.xlsx')

# Función para calcular la similitud entre dos cadenas
def similarity(a, b):
    if pd.isnull(a) or pd.isnull(b):  # Verificar si alguno es nulo
        return 0
    min_length = min(len(a), len(b))
    if min_length == 0:
        return 0
    differences = sum(1 for x, y in zip(a, b) if x != y)
    return (1 - differences / min_length) * 100

# Función para encontrar la mejor coincidencia
def find_best_match(name, choices, threshold=80):
    if not isinstance(name, str):
        return None
    best_match = None
    best_score = 0
    len_name = len(name)
    
    # Filtrar por longitud
    filtered_choices = [choice for choice in choices if abs(len(choice) - len_name) <= 2]
    
    for choice in filtered_choices:
        score = similarity(name, choice)
        if score > best_score:
            best_score = score
            best_match = choice
    return best_match if best_score >= threshold else None

# Crear una lista de nombres para comparación, eliminando duplicados
choices = df_auto_marca['Nombre'].dropna().unique().tolist()

# Inicializar una lista para almacenar los nombres correspondientes
correspondencias = []

# Buscar coincidencias y almacenar en la lista
for nombre in df_casa_depto['Nombre']:
    correspondencia = find_best_match(nombre, choices)
    correspondencias.append(correspondencia)

# Agregar la lista de correspondencias al DataFrame
df_casa_depto['Nombre_correspondiente'] = correspondencias

# Eliminar filas que tienen coincidencias
df_final = df_casa_depto[df_casa_depto['Nombre_correspondiente'].isna()]

# Guardar el resultado en un nuevo archivo Excel
df_final.to_excel('resultado_sin_coincidencias.xlsx', index=False)

print(f"¡Eliminación completada y guardada en 'resultado_sin_coincidencias.xlsx' con {len(df_final)} filas sin coincidencias!")
