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
    celular, ref = '', ''
    
    # Procesar TEL2
    tel2 = str(row['Tel2']).strip()
    if pd.notna(tel2):
        # Extraer el número y la referencia usando la función
        celular, ref = extract_number_and_ref(tel2)
    
    # Devolver los valores procesados
    return pd.Series([celular, ref], index=['Tel2', 'TelRef2'])

def process_excel(input_file, output_file):
    # Leer el archivo Excel
    df = pd.read_excel(input_file)
    
    # Aplicar la función de procesamiento a cada fila
    df[['Tel2', 'TelRef2']] = df.apply(process_data, axis=1)
    
    # Guardar el archivo modificado
    df.to_excel(output_file, index=False)

# Define el archivo de entrada y salida
input_file = 'sort.xlsx'
output_file = 'processed_sort.xlsx'

# Procesar el archivo
process_excel(input_file, output_file)
