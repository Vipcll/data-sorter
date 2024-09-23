import pandas as pd
import re

def extract_number_and_ref(text):
    # Extraer el número y la referencia de un texto
    match = re.match(r'(\d[\d\s]*)\s*(.*)', text.strip())
    if match:
        number = match.group(1).strip()
        ref = match.group(2).strip()
        return number, ref
    return '', ''

def process_data(row):
    # Inicializar valores predeterminados
    celular1, ref1, celular2, ref2 = '', '', '', ''
    
    # Procesar CELULAR
    celular = str(row['CELULAR']).strip()
    if pd.notna(celular):
        # Dividir en partes antes y después de la barra
        parts = celular.split('/')
        
        # Procesar la parte antes de la barra
        if len(parts) > 0:
            part1 = parts[0].strip()
            # Determinar si es número o referencia
            if re.match(r'^\d', part1):
                celular1, ref1 = extract_number_and_ref(part1)
            else:
                ref1 = part1
        
        # Procesar la parte después de la barra
        if len(parts) > 1:
            part2 = parts[1].strip()
            # Determinar si es número o referencia
            if re.match(r'^\d', part2):
                celular2, ref2 = extract_number_and_ref(part2)
            else:
                ref2 = part2
    
    # Devolver los valores procesados
    return pd.Series([celular1, ref1, celular2, ref2], index=['CELULAR', 'CelularRef', 'CELULAR2', 'CelularRef2'])

def process_excel(input_file, output_file):
    # Leer el archivo Excel
    df = pd.read_excel(input_file)
    
    # Aplicar la función de procesamiento a cada fila
    df[['CELULAR', 'CelularRef', 'CELULAR2', 'CelularRef2']] = df.apply(process_data, axis=1)
    
    # Guardar el archivo modificado
    df.to_excel(output_file, index=False)

# Define el archivo de entrada y salida
input_file = 'sort.xlsx'
output_file = 'processed_sort.xlsx'

# Procesar el archivo
process_excel(input_file, output_file)