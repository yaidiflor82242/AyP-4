import re

def extraer_hashtags(texto):
    patron = r'#\w+'
    return re.findall(patron, texto)
print(extraer_hashtags("Hola #python es #genial y #100dias"))
print(extraer_hashtags("#hola! #mundo? #python3"))

 #contar unicos
def contar_hashtags_unicos(texto):
    hashtags = extraer_hashtags(texto)
    return len(set(hashtags))
print(contar_hashtags_unicos("Hola #python es #genial y #100dias"))
print(contar_hashtags_unicos("Hola #python es #genial y #100dias #python")) 

#validar si es correcto
import re

def es_hashtag_valido(hashtag):
    return bool(re.fullmatch(r'#\w+', hashtag))
print(es_hashtag_valido("#python"))   # True
print(es_hashtag_valido("#py thon")) # False
print(es_hashtag_valido("python"))   # False


def extraer_hashtags_recursivo_puro(texto):
    
    def es_valido(c):
        return c.isalnum() or c == "_"
    
    def construir_hashtag(cadena, actual):
        if cadena == "" or not es_valido(cadena[0]):
            return actual, cadena
        
        return construir_hashtag(cadena[1:], actual + cadena[0])
    
    def helper(cadena):
        if cadena == "":
            return []
        
        if cadena[0] == "#":
            hashtag, resto = construir_hashtag(cadena[1:], "#")
            return [hashtag] + helper(resto)
        
        return helper(cadena[1:])
    
    return helper(texto)
print(extraer_hashtags_recursivo_puro("Hola #python es #genial y #100dias"))