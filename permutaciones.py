# Escribe una función que reciba una lista y devuelva una lista con todas las permutaciones
#  posibles de los elementos de la lista.
def permutaciones(lista):
    if len(lista) <= 1:
        return [lista]

    resultado = []

    for i in range(len(lista)):
        elemento = lista[i]
        sublista = lista[:i] + lista[i+1:]

        for p in permutaciones(sublista):
            resultado.append([elemento] + p)

    return resultado


lista = [1, 2]
print(permutaciones(lista))
