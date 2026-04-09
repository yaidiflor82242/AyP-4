"""
╔══════════════════════════════════════════════════════════════════╗
║              GUÍA COMPLETA — MEMOIZACIÓN EN PYTHON              ║
║                  Algoritmos y Programación 4                     ║
╚══════════════════════════════════════════════════════════════════╝

ÍNDICE:
  1. ¿Qué es memoización y por qué existe?
  2. El problema sin memoización (recursividad pura)
  3. La plantilla universal de memoización
  4. Ejercicio 1: Fibonacci (el clásico)
  5. Ejercicio 2: Escalones (el del parcial)
  6. Ejercicio 3: Factorial
  7. Ejercicio 4: Suma hasta N
  8. Ejercicio 5: Tribonacci (3 términos)
  9. Ejercicio 6: Potencia de 2
  10. Ejercicio 7: Cuadrícula de caminos (llave tupla)
  11. Ejercicio 8: Máxima suma en escalera
  12. Ejercicio 9: Cambio de monedas
  13. Comparación de rendimiento: con vs sin memo
  14. Errores más comunes
"""


# ══════════════════════════════════════════════════════════════════
# 1. ¿QUÉ ES MEMOIZACIÓN Y POR QUÉ EXISTE?
# ══════════════════════════════════════════════════════════════════
"""
La memoización es una técnica para hacer la recursividad más
eficiente GUARDANDO los resultados que ya calculaste.

ANALOGÍA DE LA VIDA REAL:
  Imagina que tu mamá te pregunta "¿cuánto es 347 × 89?"
  Tú te tardas 2 minutos en calcularlo: 30.883
  
  Al rato te pregunta lo mismo otra vez.
  ¿Vuelves a calcular? NO — simplemente recuerdas la respuesta.
  
  Eso es exactamente memoización:
  una "libreta" (diccionario) donde guardas cada resultado
  para no tener que calcularlo de nuevo.

¿CUÁNDO SE NECESITA?
  Cuando una función recursiva calcula LO MISMO múltiples veces.
  
  Esto pasa cuando el árbol de llamadas tiene ramas DUPLICADAS:
  
  fibonacci(5)
  ├── fibonacci(4)
  │   ├── fibonacci(3)     ← se calcula
  │   │   ├── fibonacci(2) ← se calcula
  │   │   └── fibonacci(1)
  │   └── fibonacci(2)     ← SE VUELVE A CALCULAR (desperdicio!)
  └── fibonacci(3)         ← SE VUELVE A CALCULAR (desperdicio!)
      ├── fibonacci(2)     ← SE VUELVE A CALCULAR (desperdicio!)
      └── fibonacci(1)
  
  Con memoización, fibonacci(2) y fibonacci(3) se calculan
  UNA SOLA VEZ y luego se consultan al instante.
"""


# ══════════════════════════════════════════════════════════════════
# 2. EL PROBLEMA SIN MEMOIZACIÓN
# ══════════════════════════════════════════════════════════════════

import time

def fibonacci_lento(n):
    """Recursividad pura — recalcula todo una y otra vez"""
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci_lento(n - 1) + fibonacci_lento(n - 2)

# Probemos cuánto tarda sin memo:
inicio = time.time()
resultado = fibonacci_lento(35)
fin = time.time()
print(f"fibonacci_lento(35) = {resultado}")
print(f"Tiempo sin memo: {fin - inicio:.3f} segundos")
# Resultado: varios segundos... y para n=50 sería años


# ══════════════════════════════════════════════════════════════════
# 3. LA PLANTILLA UNIVERSAL DE MEMOIZACIÓN
# ══════════════════════════════════════════════════════════════════
"""
Aprende esta estructura de memoria. Siempre es la misma:

def mi_funcion(n, memo=None):
    
    # PASO 1 — Si no me pasaron libreta, creo una nueva
    if memo is None:
        memo = {}
    
    # PASO 2 — Caso(s) base (siempre antes de buscar en memo)
    if n == caso_base:
        return valor_base
    
    # PASO 3 — ¿Ya calculé esto antes? Retorno directo
    if n in memo:
        return memo[n]
    
    # PASO 4 — No estaba → calculo
    resultado = mi_funcion(n - 1, memo) + ...   # ejemplo
    
    # PASO 5 — Guardo en la libreta ANTES de retornar
    memo[n] = resultado
    
    # PASO 6 — Retorno
    return resultado

ORDEN CRÍTICO:
  casos base → SIEMPRE antes de buscar en memo
  buscar en memo → SIEMPRE antes de calcular
  guardar en memo → SIEMPRE antes de retornar
"""


# ══════════════════════════════════════════════════════════════════
# 4. EJERCICIO 1 — FIBONACCI
# ══════════════════════════════════════════════════════════════════
"""
Secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55...
fib(n) = fib(n-1) + fib(n-2)
fib(0) = 0
fib(1) = 1
"""

def fibonacci(n, memo=None):
    if memo is None:
        memo = {}                          # PASO 1: crear libreta
    
    if n == 0: return 0                    # PASO 2: caso base 1
    if n == 1: return 1                    # PASO 2: caso base 2
    
    if n in memo: return memo[n]           # PASO 3: consultar libreta
    
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)  # PASO 4+5
    return memo[n]                         # PASO 6

# Verificación:
print(fibonacci(0))   # 0
print(fibonacci(1))   # 1
print(fibonacci(10))  # 55
print(fibonacci(20))  # 6765
print(fibonacci(50))  # 12586269025  ← esto sería imposible sin memo

# Midiendo el tiempo con memo:
inicio = time.time()
resultado = fibonacci(35)
fin = time.time()
print(f"fibonacci(35) = {resultado}")
print(f"Tiempo con memo: {fin - inicio:.6f} segundos")
# Resultado: prácticamente 0 segundos


# ══════════════════════════════════════════════════════════════════
# 5. EJERCICIO 2 — ESCALONES (EL DEL PARCIAL)
# ══════════════════════════════════════════════════════════════════
"""
Escalera de N escalones. En cada paso puedes subir 1 o 2 escalones.
¿De cuántas formas distintas puedes llegar al escalón N?

N=1: 1 forma  → [1]
N=2: 2 formas → [1+1, 2]
N=3: 3 formas → [1+1+1, 1+2, 2+1]
N=4: 5 formas → [1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2]

El patrón es idéntico a Fibonacci:
escalones(n) = escalones(n-1) + escalones(n-2)
"""

def escalones_sin_memo(n):
    """Versión pura — sin memoización"""
    if n == 0: return 1    # hay 1 forma de "no subir"
    if n == 1: return 1    # solo 1 forma: subir 1
    return escalones_sin_memo(n-1) + escalones_sin_memo(n-2)

def escalones_con_memo(n, memo=None):
    """Versión con memoización"""
    if memo is None: memo = {}
    
    if n == 0: return 1
    if n == 1: return 1
    
    if n in memo: return memo[n]
    
    memo[n] = escalones_con_memo(n-1, memo) + escalones_con_memo(n-2, memo)
    return memo[n]

# Verificación:
for i in range(1, 8):
    print(f"escalones({i}) = {escalones_con_memo(i)}")
# 1, 2, 3, 5, 8, 13, 21 ← secuencia Fibonacci desplazada

print(escalones_con_memo(10))  # 89
print(escalones_con_memo(30))  # 1346269


# ══════════════════════════════════════════════════════════════════
# 6. EJERCICIO 3 — FACTORIAL
# ══════════════════════════════════════════════════════════════════
"""
factorial(n) = n × factorial(n-1)
factorial(0) = 1
factorial(5) = 5 × 4 × 3 × 2 × 1 = 120

Nota: para factorial la memo no mejora MUCHO porque no hay
ramas duplicadas, pero el profe puede pedirlo igual.
"""

def factorial_sin_memo(n):
    if n == 0: return 1
    return n * factorial_sin_memo(n - 1)

def factorial_con_memo(n, memo=None):
    if memo is None: memo = {}
    
    if n == 0: return 1             # caso base
    
    if n in memo: return memo[n]    # consultar
    
    memo[n] = n * factorial_con_memo(n - 1, memo)  # calcular y guardar
    return memo[n]

print(factorial_con_memo(0))   # 1
print(factorial_con_memo(5))   # 120
print(factorial_con_memo(10))  # 3628800


# ══════════════════════════════════════════════════════════════════
# 7. EJERCICIO 4 — SUMA HASTA N
# ══════════════════════════════════════════════════════════════════
"""
Calcula 1 + 2 + 3 + ... + N recursivamente.
suma(5) = 1+2+3+4+5 = 15
"""

def suma_hasta_sin_memo(n):
    if n == 0: return 0
    return n + suma_hasta_sin_memo(n - 1)

def suma_hasta_con_memo(n, memo=None):
    if memo is None: memo = {}
    
    if n == 0: return 0
    
    if n in memo: return memo[n]
    
    memo[n] = n + suma_hasta_con_memo(n - 1, memo)
    return memo[n]

print(suma_hasta_con_memo(5))   # 15
print(suma_hasta_con_memo(10))  # 55
print(suma_hasta_con_memo(100)) # 5050


# ══════════════════════════════════════════════════════════════════
# 8. EJERCICIO 5 — TRIBONACCI (3 TÉRMINOS)
# ══════════════════════════════════════════════════════════════════
"""
Como Fibonacci pero sumando los TRES anteriores:
trib(n) = trib(n-1) + trib(n-2) + trib(n-3)
trib(0) = 1
trib(1) = 1
trib(2) = 2

Necesita 3 casos base en vez de 2.
"""

def tribonacci_sin_memo(n):
    if n == 0: return 1    # caso base 1
    if n == 1: return 1    # caso base 2
    if n == 2: return 2    # caso base 3
    return (tribonacci_sin_memo(n-1) +
            tribonacci_sin_memo(n-2) +
            tribonacci_sin_memo(n-3))

def tribonacci_con_memo(n, memo=None):
    if memo is None: memo = {}
    
    if n == 0: return 1
    if n == 1: return 1
    if n == 2: return 2
    
    if n in memo: return memo[n]     # ← consultar DESPUÉS de casos base
    
    memo[n] = (tribonacci_con_memo(n-1, memo) +
               tribonacci_con_memo(n-2, memo) +
               tribonacci_con_memo(n-3, memo))
    return memo[n]

print(tribonacci_con_memo(5))   # 13
print(tribonacci_con_memo(10))  # 149


# ══════════════════════════════════════════════════════════════════
# 9. EJERCICIO 6 — POTENCIA DE 2
# ══════════════════════════════════════════════════════════════════
"""
potencia(n) = 2 × potencia(n-1)
potencia(0) = 1   (2^0 = 1)
"""

def potencia_de_2(n, memo=None):
    if memo is None: memo = {}
    
    if n == 0: return 1
    
    if n in memo: return memo[n]
    
    memo[n] = 2 * potencia_de_2(n - 1, memo)
    return memo[n]

print(potencia_de_2(0))   # 1
print(potencia_de_2(4))   # 16
print(potencia_de_2(8))   # 256
print(potencia_de_2(10))  # 1024


# ══════════════════════════════════════════════════════════════════
# 10. EJERCICIO 7 — CUADRÍCULA DE CAMINOS
#     ⚠️ LLAVE TUPLA — cuando cambian DOS parámetros
# ══════════════════════════════════════════════════════════════════
"""
Cuadrícula N×M. Solo puedes ir → derecha o ↓ abajo.
¿Cuántos caminos hay de (0,0) a (N-1, M-1)?

Para N=M=2:
  (0,0) → (0,1) → (1,1)   camino 1
  (0,0) → (1,0) → (1,1)   camino 2
  Total: 2

IMPORTANTE: cuando hay DOS parámetros que cambian,
la llave del memo es una TUPLA: (fila, col)
"""

def caminos_sin_memo(n, m):
    if n == 1 or m == 1: return 1     # borde: solo 1 camino posible
    return caminos_sin_memo(n-1, m) + caminos_sin_memo(n, m-1)

def caminos_con_memo(n, m, memo=None):
    if memo is None: memo = {}
    
    if n == 1 or m == 1: return 1     # caso base
    
    if (n, m) in memo: return memo[(n, m)]    # ← llave es una TUPLA
    
    memo[(n, m)] = (caminos_con_memo(n-1, m, memo) +
                    caminos_con_memo(n, m-1, memo))
    return memo[(n, m)]

print(caminos_con_memo(2, 2))   # 2
print(caminos_con_memo(3, 3))   # 6
print(caminos_con_memo(3, 4))   # 10
print(caminos_con_memo(5, 5))   # 70

# ⚠️ REGLA: si cambias N parámetros, la llave es una TUPLA de N valores
# 1 parámetro → memo[n]
# 2 parámetros → memo[(n, m)]
# 3 parámetros → memo[(a, b, c)]


# ══════════════════════════════════════════════════════════════════
# 11. EJERCICIO 8 — MÁXIMA SUMA EN ESCALERA
# ══════════════════════════════════════════════════════════════════
"""
En cada escalón hay un valor. Subes 1 o 2 escalones.
¿Cuál es la máxima suma que puedes acumular?

valores = [0, 3, 1, 5, 2, 4]  (escalón 0 al 5)
Mejor camino: 0→1→3→5 = 0+3+5+4 = 12
"""

valores = [0, 3, 1, 5, 2, 4]

def max_suma_sin_memo(n, valores):
    if n == 0: return valores[0]
    if n == 1: return valores[0] + valores[1]
    desde_uno = max_suma_sin_memo(n-1, valores) + valores[n]
    desde_dos = max_suma_sin_memo(n-2, valores) + valores[n]
    return max(desde_uno, desde_dos)

def max_suma_con_memo(n, valores, memo=None):
    if memo is None: memo = {}
    
    if n == 0: return valores[0]
    if n == 1: return valores[0] + valores[1]
    
    if n in memo: return memo[n]
    
    desde_uno = max_suma_con_memo(n-1, valores, memo) + valores[n]
    desde_dos = max_suma_con_memo(n-2, valores, memo) + valores[n]
    memo[n] = max(desde_uno, desde_dos)
    return memo[n]

print(max_suma_con_memo(5, valores))   # 12


# ══════════════════════════════════════════════════════════════════
# 12. EJERCICIO 9 — CAMBIO DE MONEDAS
# ══════════════════════════════════════════════════════════════════
"""
Tienes monedas de diferentes valores.
¿De cuántas formas puedes sumar exactamente el monto dado?

LLAVE = TUPLA porque cambian DOS parámetros: (monto, indice)
"""

def formas_cambio(monto, monedas, indice=0, memo=None):
    if memo is None: memo = {}
    
    if monto == 0: return 1      # llegamos exacto → cuenta como 1 forma
    if monto < 0 or indice >= len(monedas): return 0   # imposible
    
    clave = (monto, indice)       # ← TUPLA porque 2 parámetros cambian
    if clave in memo: return memo[clave]
    
    # Dos opciones: USAR esta moneda O SALTAR a la siguiente
    usar    = formas_cambio(monto - monedas[indice], monedas, indice, memo)
    no_usar = formas_cambio(monto, monedas, indice + 1, memo)
    
    memo[clave] = usar + no_usar
    return memo[clave]

print(formas_cambio(10, [1, 5, 10]))   # 4
print(formas_cambio(5,  [1, 5]))       # 2


# ══════════════════════════════════════════════════════════════════
# 13. COMPARACIÓN DE RENDIMIENTO: CON VS SIN MEMO
# ══════════════════════════════════════════════════════════════════

import time

def fib_sin(n):
    if n <= 1: return n
    return fib_sin(n-1) + fib_sin(n-2)

def fib_con(n, memo=None):
    if memo is None: memo = {}
    if n <= 1: return n
    if n in memo: return memo[n]
    memo[n] = fib_con(n-1, memo) + fib_con(n-2, memo)
    return memo[n]

n = 35

inicio = time.time()
fib_sin(n)
sin_memo = time.time() - inicio

inicio = time.time()
fib_con(n)
con_memo = time.time() - inicio

print(f"\nfibonacci({n})")
print(f"  Sin memo: {sin_memo:.4f} segundos")
print(f"  Con memo: {con_memo:.6f} segundos")
print(f"  La memo es {sin_memo/con_memo:.0f}x más rápida")
# La memo es miles de veces más rápida


# ══════════════════════════════════════════════════════════════════
# 14. ERRORES MÁS COMUNES
# ══════════════════════════════════════════════════════════════════

# ─── ERROR 1: Olvidar inicializar memo ───────────────────────────
# MAL — el mismo diccionario se comparte entre todas las llamadas
def fib_malo(n, memo={}):        # ← {} se crea UNA sola vez
    if n <= 1: return n
    if n in memo: return memo[n]
    memo[n] = fib_malo(n-1) + fib_malo(n-2)
    return memo[n]

# BIEN — memo=None y se inicializa adentro
def fib_bien(n, memo=None):      # ← None por defecto
    if memo is None: memo = {}   # ← se crea cada vez que se llama sin memo
    if n <= 1: return n
    if n in memo: return memo[n]
    memo[n] = fib_bien(n-1, memo) + fib_bien(n-2, memo)
    return memo[n]

# ─── ERROR 2: Consultar memo ANTES de los casos base ─────────────
# MAL — puede buscar en memo algo que no tiene sentido
def escalones_mal(n, memo=None):
    if memo is None: memo = {}
    if n in memo: return memo[n]   # ← consulta ANTES del caso base
    if n == 0: return 1            # ← caso base después: tarde
    if n == 1: return 1

# BIEN — casos base primero, luego consultar memo
def escalones_bien(n, memo=None):
    if memo is None: memo = {}
    if n == 0: return 1            # ← caso base PRIMERO
    if n == 1: return 1            # ← caso base PRIMERO
    if n in memo: return memo[n]   # ← luego consultar

# ─── ERROR 3: Olvidar pasar memo en la llamada recursiva ─────────
# MAL — cada llamada crea su propia libreta → la memo no sirve
def fib_sin_pasar(n, memo=None):
    if memo is None: memo = {}
    if n <= 1: return n
    if n in memo: return memo[n]
    memo[n] = fib_sin_pasar(n-1) + fib_sin_pasar(n-2)   # ← olvida memo!
    return memo[n]

# BIEN — siempre pasar memo en cada llamada recursiva
def fib_pasando(n, memo=None):
    if memo is None: memo = {}
    if n <= 1: return n
    if n in memo: return memo[n]
    memo[n] = fib_pasando(n-1, memo) + fib_pasando(n-2, memo)  # ← pasa memo
    return memo[n]

# ─── ERROR 4: Con 2 parámetros, olvidar usar tupla como llave ────
# MAL — solo guarda uno de los parámetros
def caminos_mal(n, m, memo=None):
    if memo is None: memo = {}
    if n == 1 or m == 1: return 1
    if n in memo: return memo[n]                  # ← llave incompleta!
    memo[n] = caminos_mal(n-1, m) + caminos_mal(n, m-1)
    return memo[n]

# BIEN — la llave es una tupla con todos los parámetros que cambian
def caminos_bien(n, m, memo=None):
    if memo is None: memo = {}
    if n == 1 or m == 1: return 1
    if (n, m) in memo: return memo[(n, m)]        # ← llave es tupla
    memo[(n, m)] = (caminos_bien(n-1, m, memo) +
                    caminos_bien(n, m-1, memo))
    return memo[(n, m)]


# ══════════════════════════════════════════════════════════════════
# PLANTILLA FINAL PARA COPIAR Y ADAPTAR
# ══════════════════════════════════════════════════════════════════
"""
def mi_funcion(n, memo=None):
    # 1. Inicializar libreta
    if memo is None:
        memo = {}
    
    # 2. Casos base (SIEMPRE primero)
    if n == 0: return VALOR_BASE_0
    if n == 1: return VALOR_BASE_1
    
    # 3. Consultar libreta
    if n in memo:
        return memo[n]
    
    # 4. Calcular y guardar
    memo[n] = mi_funcion(n-1, memo) + mi_funcion(n-2, memo)
    
    # 5. Retornar
    return memo[n]


# Si tienes DOS parámetros que cambian:
def mi_funcion_2d(n, m, memo=None):
    if memo is None:
        memo = {}
    
    if n == CASO_BASE or m == CASO_BASE:
        return VALOR_BASE
    
    if (n, m) in memo:        # ← llave es TUPLA
        return memo[(n, m)]
    
    memo[(n, m)] = (mi_funcion_2d(n-1, m, memo) +
                    mi_funcion_2d(n, m-1, memo))
    return memo[(n, m)]
"""