import re

def normalize_phone_number(phone):
    # Eliminar todos los caracteres no numéricos
    digits = re.sub(r'\D', '', phone)
    
    # Si tiene 10 dígitos (número en formato nacional de México), formatear con +52
    if len(digits) == 10:
        return f'+52 {digits[:2]} {digits[2:6]} {digits[6:]}'
    
    # Si tiene 11 dígitos (número en formato nacional de México con lada nacional), formatear con +52
    elif len(digits) == 11:
        return f'+52 {digits[:2]} {digits[2:7]} {digits[7:]}'
    
    # Para números con menos de 10 dígitos o más de 11 dígitos, los consideramos incorrectos
    else:
        return f'Número incorrecto: {phone}'

def process_file(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        lines = file.readlines()
    
    normalized_numbers = [normalize_phone_number(line.strip()) for line in lines]
    
    with open(output_filename, 'w') as file:
        for number in normalized_numbers:
            file.write(number + '\n')

# Cambia 'input.txt' y 'output.txt' por los nombres de tus archivos
process_file('input.txt', 'output.txt')
