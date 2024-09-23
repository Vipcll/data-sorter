import pandas as pd

# Cargar el archivo de Excel
df = pd.read_excel('Ordenando.xlsx')

# Función para llenar CELULAR y CelularRef
def fill_cells(row):
    if pd.notna(row['CELULAR']):
        # Si CELULAR tiene número, no hacer nada
        row['CelularRef'] = row.get('CelularRef', '')  # Mantener el valor existente
    elif pd.notna(row['CELULAR2']):
        # Si CELULAR está vacío y CELULAR2 tiene número
        row['CELULAR'] = row['CELULAR2']  # Mover el número de CELULAR2 a CELULAR
        row['CELULAR2'] = None  # Limpiar CELULAR2
        row['CelularRef'] = row['CelularRef2']  # Asignar CelularRef2 a CelularRef
        row['CelularRef2'] = None  # Limpiar CelularRef2
    else:
        # Si ambos están vacíos, usar Tel
        row['CELULAR'] = row['Tel']  # Asignar Tel a CelularRef
        row['CelularRef'] = "fijo"

    return row

# Aplicar la función a cada fila
df = df.apply(fill_cells, axis=1)

# Guardar el DataFrame modificado en un nuevo archivo de Excel
df.to_excel('Ordenando_Modificado.xlsx', index=False)

print("Proceso completado y archivo guardado como 'Ordenando_Modificado.xlsx'.")
