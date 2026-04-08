import re
def validar_placa_vehiculo(placa):
    """
    Valida si una placa de vehículo colombiana tiene formato correcto.

    Formato válido: 3 letras mayúsculas + 3 dígitos (ej: ABC123)
    También válido con guion: ABC-123

    Ejemplos:
    validar_placa_vehiculo("ABC123") -> True
    validar_placa_vehiculo("ABC-123") -> True
    validar_placa_vehiculo("AB1234") -> False
    validar_placa_vehiculo("abc123") -> False
    """
    def validar_recursivo(cadena, paso):
        
        # PASO 1: validar 3 letras mayúsculas
        if paso == 0:
            if re.match(r'^[A-Z]{3}', cadena):
                return validar_recursivo(cadena[3:], 1)
            else:
                return False
        
        # PASO 2: validar guion opcional
        elif paso == 1:
            if cadena.startswith('-'):
                return validar_recursivo(cadena[1:], 2)
            else:
                return validar_recursivo(cadena, 2)
        
        # PASO 3: validar 3 números
        elif paso == 2:
            if re.match(r'^\d{3}$', cadena):
                return True
            else:
                return False
    
    return validar_recursivo(placa, 0)
    # TODO: Implementar con re.match o re.search

print(validar_placa_vehiculo("ABC123"))   # True
print(validar_placa_vehiculo("ABC-123"))  # True
print(validar_placa_vehiculo("AB1234"))   # False
print(validar_placa_vehiculo("abc123"))   # False


import re

def validar_placa_vehiculo(placa):
    patron = r'^[A-Z]{3}-?\d{3}$'
    return bool(re.match(patron, placa))
print(validar_placa_vehiculo("ABC123"))   # True
print(validar_placa_vehiculo("ABC-123"))  # True
print(validar_placa_vehiculo("AB1234"))   # False
print(validar_placa_vehiculo("abc123"))   # False
