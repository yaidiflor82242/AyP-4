def busqueda_binaria_recursiva(arr, objetivo, izquierda, derecha):
    if izquierda > derecha:
        return -1  # No encontrado
    
    medio = (izquierda + derecha) // 2
    
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] > objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, izquierda, medio - 1)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, derecha)

# Ejemplo de uso
arr = [1, 3, 5, 7, 9, 11, 13]
objetivo = 7
resultado = busqueda_binaria_recursiva(arr, objetivo, 0, len(arr) - 1)
if resultado != -1:
    print(f"El elemento {objetivo} se encuentra en el índice {resultado}")
else:
    print(f"El elemento {objetivo} no se encuentra en la lista")