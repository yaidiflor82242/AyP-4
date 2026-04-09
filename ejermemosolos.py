"""1. Factorial con memo
El clásico. Factorial(n) = n × factorial(n-1). Impleméntalo sin memo y luego con memo.
"""

def factorial_sin_memo(n):
    if n == 0: return 1   # caso base
    return n * factorial_sin_memo(n-1)

def factorial_con_memo(n, memo=None):
    if memo is None: memo = {}
    if n == 0: return 1
    if n in memo: return memo[n]
    memo[n] = n * factorial_con_memo(n-1, memo)
    return memo[n]


"""Suma de 1 hasta N
Calcula 1+2+3+...+N recursivamente. Con y sin memo."""

def suma_sin_memo(n):
    if n == 0: return 0
    return n + suma_sin_memo(n-1)

def suma_con_memo(n, memo=None):
    if memo is None: memo = {}
    if n == 0: return 0
    if n in memo: return memo[n]
    memo[n] = n + suma_con_memo(n-1, memo)
    return memo[n]

# ORDEN SIEMPRE:
# 1. if memo is None → inicializar
# 2. casos base
# 3. if n in memo → retornar guardado
# 4. calcular y guardar en memo
# 5. retorn


"""Potencia de 2
Calcula 2^n recursivamente con memo. potencia(n) = 2 × potencia(n-1)"""

def potencia_sin_memo(n):
    if n == 0: return 1
    return 2 * potencia_sin_memo(n-1)


def potencia_con_memo(n, memo=None):
    if memo is None: memo = {}
    if n == 0: return 1
    if n in memo: return memo[n]
    memo[n] = 2 * potencia_con_memo(n-1, memo)
    return memo[n]


"""Contar formas de dar cambio
Tienes monedas de 1, 5 y 10 pesos. ¿De cuántas formas puedes sumar exactamente N pesos usando solo esos valores?"""
def formas_cambio_sin_memo(monto, monedas, indice=0):
    if monto == 0: return 1   # llegamos a 0 exacto, cuenta!
    if monto < 0 or indice >= len(monedas): return 0
    # Dos opciones: usar esta moneda O pasar a la siguiente
    usar = formas_cambio_sin_memo(monto - monedas[indice], monedas, indice)
    no_usar = formas_cambio_sin_memo(monto, monedas, indice+1)
    return usar + no_usar


def formas_cambio(monto, monedas, indice=0, memo=None):
    if memo is None: memo = {}
    if monto == 0: return 1   # llegamos a 0 exacto, cuenta!
    if monto < 0 or indice >= len(monedas): return 0
    clave = (monto, indice)   # la llave es una TUPLA
    if clave in memo: return memo[clave]
    # Dos opciones: usar esta moneda O pasar a la siguiente
    usar = formas_cambio(monto - monedas[indice], monedas, indice, memo)
    no_usar = formas_cambio(monto, monedas, indice+1, memo)
    memo[clave] = usar + no_usar
    return memo[clave]


"""6. Cuadrícula — caminos de esquina a esquina
Cuadrícula N×M. Solo puedes ir derecha o abajo. ¿Cuántos caminos hay de (0,0) a (n-1, m-1)?"""

def caminos_sin_memo(n, m):
    if n == 1 or m == 1: return 1  # borde: solo 1 camino
    return caminos_sin_memo(n - 1, m) + caminos_sin_memo(n, m - 1)

def caminos(n, m, memo=None):
    if memo is None: memo = {}
    if n == 1 or m == 1: return 1  # borde: solo 1 camino
    if (n, m) in memo: return memo[(n, m)]
    # Desde (n,m) puedo venir de arriba o de la izquierda
    memo[(n, m)] = caminos(n-1, m, memo) + caminos(n, m-1, memo)
    return memo[(n, m)]

# NOTA: cuando hay DOS parámetros que cambian,
# la llave del memo es una TUPLA: (n, m)


""". Máxima suma de una escalera
En cada escalón hay un valor. Subes de a 1 o 2 escalones. ¿Cuál es la máxima suma que puedes acumular llegando al tope?"""

def max_suma_escalera_sin_memo(escalones, indice=0):
    if indice >= len(escalones): return 0
    # Dos opciones: subir 1 o subir 2 escalones
    subir_1 = escalones[indice] + max_suma_escalera_sin_memo(escalones, indice+1)
    subir_2 = escalones[indice] + max_suma_escalera_sin_memo(escalones, indice+2)
    return max(subir_1, subir_2)

def max_suma(n, valores, memo=None):
    if memo is None: memo = {}
    if n == 0: return valores[0]
    if n == 1: return valores[0] + valores[1]
    if n in memo: return memo[n]
    # El máximo viene de llegar desde n-1 o desde n-2
    desde_uno = max_suma(n-1, valores, memo) + valores[n]
    desde_dos = max_suma(n-2, valores, memo) + valores[n]
    memo[n] = max(desde_uno, desde_dos)
    return memo[n]