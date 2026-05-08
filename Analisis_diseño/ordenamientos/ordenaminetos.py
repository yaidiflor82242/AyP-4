import random
import time

def generar_jugadores(n):
    paises = ["COL", "MEX", "ARG", "BRA", "ESP","USA", "JAP", "KOR"]
    nombres = ["Alex", "Sam", "Juan", "Camila", "Alicia", "Camilo"]

    jugadores =[]

    for i in range(n):
        jugadores.append({
            "id": i + 1,
            "nombre": f"{random.choice(nombres)}_{i}",
            "puntos": random.randint(100,10000),
            "horas": random.randint(10,1000),
            "pais": random.choice(paises)
        })
    return jugadores

lista_jugadores = generar_jugadores(1000)
print(lista_jugadores)

def merge(izq, der):
    resultado= []
    i= j= 0
    while i < len(izq) and j < len(der):
        a = izq[i]
        b = der[j]

        if a["puntos"] > b["puntos"]:
            resultado.append(a)
            i += 1
        elif a["puntos"] == b["puntos"] and a["horas"] < b["horas"]:
            resultado.append(a)
            i += 1
        else:
            resultado.append(b)
            j += 1
        
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    return resultado

def merge_sort(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izq = merge_sort(lista[:medio])
    der = merge_sort(lista[medio:])
    return merge(izq, der)


lista_ordenada = merge_sort(lista_jugadores)
print(lista_ordenada)


def heapify(arr, n, i):
    mayor = i
    izq = 2 * i + 1
    der = 2 * i + 2

    if izq < n and arr[izq]["puntos"] > arr[mayor]["puntos"]:
        mayor = izq
    
    if der < n and arr[der]["puntos"] > arr[mayor]["puntos"]:
        mayor = der
    
    if mayor != i:
        arr[i], arr[mayor] = arr[mayor], arr[i]
        heapify(arr, n, mayor)

def heap_sort(lista,k):

    arr= lista.copy(9)
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    resultado = []
    tamaño=n

    for i in range(min(k,n)):
        resultado.append(arr[0])
        
        tamaño -= 1
        heapify(arr, tamaño, 0)
    return resultado