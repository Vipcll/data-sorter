import pandas as pd
import random

def generate_unique_number(existing_numbers):
    """Genera un número aleatorio de 4 dígitos que no esté en la lista existente."""
    while True:
        number = f'{random.randint(0, 9999):04d}'  # Genera un número de 4 dígitos con ceros a la izquierda
        if number not in existing_numbers:
            return number

def process_emails(input_filename, output_filename):
    # Leer el archivo Excel
    df = pd.read_excel(input_filename)

    # Asegurarnos de que el DataFrame tiene una columna llamada 'Email'
    if 'Email' not in df.columns:
        raise ValueError("El archivo Excel debe contener una columna llamada 'Email'")

    unique_numbers = set()  # Para almacenar los números únicos generados

    # Procesar la columna de correos
    def replace_na(email):
        if email == 'N/A@gmail.com' or pd.isna(email) or email == '':
            number = generate_unique_number(unique_numbers)
            unique_numbers.add(number)
            return f'N/A{number}@gmail.com'
        return email

    # Aplicar la función a la columna 'Email'
    df['Email'] = df['Email'].apply(replace_na)

    # Guardar el DataFrame modificado en un nuevo archivo Excel
    df.to_excel(output_filename, index=False)

# Cambia 'Sorteando.xlsx' y 'output.xlsx' por los nombres de tus archivos
process_emails('Sorteando.xlsx', 'output.xlsx')
