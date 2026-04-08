import re

def escapar_no_recursivo(texto):
    return re.escape(texto)
print(escapar_no_recursivo("hola. (mundo)?"))
def escapar_recursivo(texto):
    
    especiales = ".^$*+?{}[]\\|()"
    
    def helper(cadena):
        if cadena == "":
            return ""
        
        primer = cadena[0]
        
        # Si es caracter especial → lo escapamos
        if primer in especiales:
            return "\\" + primer + helper(cadena[1:])
        else:
            return primer + helper(cadena[1:])
    
    return helper(texto)
print(escapar_recursivo("hola. (mundo)?"))

"""traer lo que esta antes del carcter"""
import re

def antes_del_caracter_no_recursivo(texto, caracter):
    patron = rf'^[^{re.escape(caracter)}]*'
    resultado = re.match(patron, texto)
    return resultado.group() if resultado else ""
print(antes_del_caracter_no_recursivo("hola#mundo", "#"))  # hola
print(antes_del_caracter_no_recursivo("123|456", "|"))     # 123
print(antes_del_caracter_no_recursivo("abc@xyz", "@"))     # abc

def antes_del_caracter_recursivo(texto, caracter):
    
    if texto == "" or texto[0] == caracter:
        return ""
    
    return texto[0] + antes_del_caracter_recursivo(texto[1:], caracter)
print(antes_del_caracter_recursivo("hola#mundo", "#"))  # hola
print(antes_del_caracter_recursivo("123|456", "|"))     # 123
print(antes_del_caracter_recursivo("abc@xyz", "@"))     # abc


