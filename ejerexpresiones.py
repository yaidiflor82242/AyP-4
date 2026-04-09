import re

def validar_nombre(nombre):
    patron= r'^[a-z]{1}([a-z]|\d){4,9}$'
    return bool(re.match(patron, nombre))

print(validar_nombre("juan"))      # False (menos de 5 caracteres)

def validar_codigo_producto(codigo):
    patron=r'^[A-Z]{3}-\d{4}$'
    return bool(re.match(patron, codigo))
print(validar_codigo_producto("ABC-1234"))  # True

def placa_vehiculo(placa):
    patron= r'^[A-Z]{3}\d{3}$'
    return bool(re.match(patron, placa))
print(placa_vehiculo("ABC123"))  # True

def numero_decimal(numero):
    patron=r'^\d+\.\d{2}$'
    return bool(re.match(patron, numero))

def fecha_simple(fecha):
    patron=r'^(0[1-9]|[1-2][0-9]|3[0-1])/(0[1-9]|1[0-2])/\d{4}$'
    return bool(re.match(patron, fecha))
print(fecha_simple("01/01/2023"))  # True

def validar_fecha(fecha):
    correcta = re.search(r"^(0[1-9]|[12]\d|3[01])[-/](0[1-9]|1[0-2])[-/](19|20\d{2})$",fecha)
    return bool(correcta)

print(validar_fecha("12/03/2026"))


