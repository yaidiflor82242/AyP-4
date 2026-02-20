# Función recursiva para sumar los elementos de una lista
def suma_lista(lista, acumulador=0):
    if len(lista) == 0:
        return acumulador
    return suma_lista(lista[1:], acumulador + lista[0])

lista = [ 2, 3, 4]
print(f"La suma de los elementos de la lista es: {suma_lista(lista)}")

def potencia(base,exponente, acumulador=1):
    if exponente == 0:
        return acumulador
    
    return potencia(base, exponente - 1, acumulador * base)

lista = [2, 3, 4]
print(f"El resultado de la potencia es: {potencia(lista[0], lista[1])}")

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)
lista = [2, 3, 4]
print(f"El resultado de la potencia es: {potencia(lista[0], lista[1])}")