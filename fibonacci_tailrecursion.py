# Función para calcular el n-ésimo número de Fibonacci utilizando recursión de cola
def fibanacci(n, actual=0, siguiente=1):
    if n == 0:
        return actual
    elif n == 1:
        return siguiente
    else:
        return fibanacci(n - 1, siguiente, actual + siguiente)
    
#medir tiempo y hora actual

import time
inicio = time.time()
print(fibanacci(40))
print(time.time() - inicio)

    