"""
═══════════════════════════════════════════════════════════════════════════════
        TALLER: ANÁLISIS DE ALGORITMOS
        Algoritmos y Programación 4
═══════════════════════════════════════════════════════════════════════════════

INSTRUCCIONES GENERALES:
------------------------
- Entregar archivo .py con todas las secciones resueltas
- El código debe ejecutar sin errores

DISTRIBUCIÓN:
- Sección A: Análisis teórico (1.0)         
- Sección B: Investigación (0.5)             
- Sección C: Resolver y optimizar (2.0)      
- Sección D: Proponer y justificar (1.5)     

═══════════════════════════════════════════════════════════════════════════════
"""

import time
import random


# ═══════════════════════════════════════════════════════════════════════════════
#                    SECCIÓN A: ANÁLISIS TEÓRICO (1.0)
#                         
# ═══════════════════════════════════════════════════════════════════════════════

"""
PUNTO A.1 (0.4): Clasificar complejidad

Para cada función, escribe:
  - La complejidad Big-O
  - UNA línea explicando por qué

Escribe tus respuestas como comentarios debajo de cada función.
"""


def alpha(lista):
    total = 0
    for x in lista:
        total += x
    promedio = total / len(lista)
    return promedio

# Complejidad: O(n)
# Porque:  recorro toda la lista una sola vez para sumar los elementos,
# así que el tiempo crece proporcional al tamaño de la lista.
    


def beta(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i] == lista[j] and i != j:
                return True
    return False

# Complejidad: O(n^2)
# Porque: Comparo cada elemento con todos los demás,
# entonces por cada elemento hago otro recorrido completo.

def gamma(n):
    if n <= 1:
        return 1
    return gamma(n // 2) + 1

# Complejidad: O(log n)
# Porque: en cada llamada el número se divide a la mitad,
# así que el problema se hace cada vez más pequeño muy rápido.


def delta(lista):
    resultado = set()
    for x in lista:
        resultado.add(x)
    return resultado

# Complejidad: O(n)
# Porque:  paso una sola vez por la lista agregando elementos al set,
# y eso no depende más que del tamaño de la lista.


def epsilon(lista):
    for x in lista:
        if x in lista:
            pass

# Complejidad: O(n^2)
# Porque:recorro la lista y en cada paso vuelvo a buscar dentro de la misma lista,
# lo que hace que el trabajo se repita muchas veces.
# PISTA: ¿cuánto cuesta `x in lista`?


def zeta(n):
    for i in range(n):
        j = 1
        while j < n:
            j *= 3

# Complejidad: O(n log n)
# Porque: el ciclo externo se repite n veces,
# y el interno crece rápido (multiplicando por 3), por eso se ejecuta pocas veces (log n)


def eta(lista):
    if len(lista) <= 1:
        return lista
    medio = len(lista) // 2
    izq = eta(lista[:medio])
    der = eta(lista[medio:])
    return izq + der

# Complejidad: O(n log n)
#Porque: divido la lista en partes cada vez más pequeñas,
# pero en cada nivel tengo que copiar y juntar listas, lo cual cuesta recorrerlas.
# PISTA: ¿cuánto cuesta lista[:medio]?


def theta(n):
    i = 1
    while i * i <= n: 
        i += 1
    return i

# Complejidad: O(√n)
# Porque: el ciclo avanza de uno en uno hasta que i*i alcanza a n,
# o sea que realmente solo llega hasta la raíz cuadrada de n.

"""
PUNTO A.2 (0.3): Ordenar de menor a mayor complejidad

Ordena las siguientes complejidades de la MÁS RÁPIDA a la MÁS LENTA:

O(n!), O(1), O(n log n), O(2^n), O(n²), O(log n), O(n), O(n³), O(√n)

Tu respuesta (de más rápida a más lenta):
1. O(1)
2. O(log n)
3. O(√n)
4. O(n)
5. O(n log n)
6. O(n²)
7. O(n³)
8. O(2^n)
9. O(n!)
"""


"""
PUNTO A.3 (0.3): Verdadero o Falso

Escribe V o F y justifica brevemente las falsas.

1.  F O(2n) es más lento que O(n)
   Justificación: Falso, porque en Big-O se ignoran las constantes.
O(2n) y O(n) crecen al mismo ritmo, solo cambia un factor constante.

2. F Un algoritmo O(n²) siempre es más lento que uno O(n log n)
   Justificación: Falso, porque depende del tamaño de entrada.
Para valores pequeños de n, un O(n²) puede ser incluso más rápido
debido a constantes o menor sobrecosto.

3. F  Si un algoritmo tiene un for de n y dentro un for de 5,
su complejidad es O(n²)
    Justificación: Falso, porque el segundo ciclo no depende de n,
solo se repite 5 veces (constante), así que no afecta el orden.
La complejidad total es O(n).

4. F `x in set` tiene la misma complejidad que `x in list`
   Justificación: Falso, porque en listas se busca elemento por elemento (O(n)),
mientras que en un set se usa hashing, lo que permite búsqueda en tiempo constante O(1) en promedio.

5. F Un algoritmo recursivo que se llama a sí mismo 2 veces
       siempre es O(2^n)
   Justificación: Falso, porque depende de cuánto se reduce el problema en cada llamada.
Por ejemplo, si se divide entre 2 cada vez, puede ser O(n log n) o menor.

6. F O(n) + O(n²) = O(n³)
   Justificación:  Falso, porque en Big-O se toma el término dominante.
En este caso, O(n²) domina a O(n), por lo que el resultado es O(n²).

7. V La complejidad espacial de un algoritmo in-place es O(1)
   Justificación:  Verdadero, porque solo usa una cantidad fija de memoria adicional,
sin importar el tamaño de la entrada.

8. V Memorización mejora la complejidad temporal pero empeora la espacial
   Justificación: Verdadero, porque guarda resultados en memoria para evitar repetir cálculos,
lo que acelera el algoritmo pero consume más espacio.
"""


# ═══════════════════════════════════════════════════════════════════════════════
#                    SECCIÓN B: INVESTIGACIÓN (0.5)
#                         
# ═══════════════════════════════════════════════════════════════════════════════

"""
PUNTO B.1 (0.25): Complejidad de operaciones de Python

Investiga y completa la tabla con la complejidad de cada operación.
Agrega una justificación de por qué es la complejidad.
Puedes consultar: https://wiki.python.org/moin/TimeComplexity

┌──────────────────────────────┬──────────────┬──────────────┐
│ Operación                    │ Lista []     │ Set/Dict {}  │
├──────────────────────────────┼──────────────┼──────────────┤
│ Acceder por índice [i]       │ O(1)         │ N/A          │
│ Buscar elemento (x in ...)   │ O(n)         │ O(1)         │
│ Agregar al final (.append)   │ O(1)         │ O(1)         │
│ Insertar al inicio           │ O(n)         │ N/A          │
│ Eliminar por valor (.remove) │ O(n)         │ O(1)         │
│ Obtener longitud (len)       │ O(1)         │ O(1)         │
│ Ordenar (.sort / sorted)     │ O(n log n)   │ N/A          │
│ Copiar (.copy / [:])         │ O(n)         │ O(n)         │
└──────────────────────────────┴──────────────┴──────────────┘
"""


"""
PUNTO B.2 (0.25): Caso real

Investiga y responde:

1. ¿Qué algoritmo de ordenamiento usa Python internamente (sorted/list.sort)?
   Respuesta: Timsort

2. ¿Cuál es su complejidad en el mejor, peor y caso promedio?
   Mejor: O(n)
   Peor: O(n log n)
   Promedio: O(n log n)

3. ¿Por qué Python eligió ese algoritmo y no Quick Sort?
   Respuesta: Timsort es un algoritmo híbrido que combina merge sort y insertion sort, lo que lo hace
     muy eficiente para datos reales que a menudo están parcialmente ordenados.
"""


# ═══════════════════════════════════════════════════════════════════════════════
#                SECCIÓN C: RESOLVER Y OPTIMIZAR (2.0)
#                         
# ═══════════════════════════════════════════════════════════════════════════════

"""
En cada problema:
1. Analiza la versión LENTA y escribe su complejidad
2. Implementa la versión RÁPIDA
3. Escribe la complejidad de tu versión
4. Ejecuta las pruebas para verificar que funciona
"""


# ─── PROBLEMA C.1 (0.4): Elementos únicos ────────────────────────────────────

def unicos_lento(lista):
    """
    Retorna lista sin duplicados manteniendo el orden.
    COMPLEJIDAD: O(n^2)  ← analiza y escribe
    """
    resultado = []
    for x in lista:
        if x not in resultado:
            resultado.append(x)
    return resultado


def unicos_rapido(lista):
    """
    Misma funcionalidad pero más eficiente.
    USA un set auxiliar para búsqueda O(1).

    TODO: Implementar
    COMPLEJIDAD: O(n)"""
    resultado = []
    vistos = set()
    
    for x in lista:
        if x not in vistos:
            resultado.append(x)
            vistos.add(x)
    
    return resultado

# COMPLEJIDAD: O(n)
    



# ─── PROBLEMA C.2 (0.4): Frecuencia del más común ────────────────────────────

def mas_comun_lento(lista):
    """
    Retorna el elemento que más se repite y cuántas veces.
    COMPLEJIDAD: O(n^2)  ← analiza y escribe
    """
    max_elem = None
    max_count = 0
    for x in lista:
        count = 0
        for y in lista:
            if y == x:
                count += 1
        if count > max_count:
            max_count = count
            max_elem = x
    return max_elem, max_count


def mas_comun_rapido(lista):
    """
    Misma funcionalidad usando diccionario contador.

    TODO: Implementar
    COMPLEJIDAD: O(n)
    """
    conteo = {}
    
    for x in lista:
        conteo[x] = conteo.get(x, 0) + 1
    
    max_elem = None
    max_count = 0
    
    for x, c in conteo.items():
        if c > max_count:
            max_count = c
            max_elem = x
    
    return max_elem, max_count

# COMPLEJIDAD: O(n)
 



# ─── PROBLEMA C.3 (0.4): Pares que suman K ───────────────────────────────────

def pares_suma_lento(lista, k):
    """
    Retorna todos los pares (i, j) donde lista[i] + lista[j] == k.
    COMPLEJIDAD: O(n^2)  ← analiza y escribe
    """
    pares = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == k:
                pares.append((lista[i], lista[j]))
    return pares


def pares_suma_rapido(lista, k):
    """
    Misma funcionalidad usando set para buscar complementos.

    Estrategia:
    - Para cada x, el complemento es k - x
    - Si el complemento ya está en un set de "vistos", es un par

    TODO: Implementar
    COMPLEJIDAD: O(n)
    """
    vistos = set()
    pares = set()  # evita duplicados automáticamente
    
    for x in lista:
        complemento = k - x
        if complemento in vistos:
            pares.add(tuple(sorted((x, complemento))))
        vistos.add(x)
    
    return list(pares)

# COMPLEJIDAD: O(n)
   


# ─── PROBLEMA C.4 (0.4): Anagramas ───────────────────────────────────────────

def son_anagramas_lento(palabra1, palabra2):
    """
    Verifica si dos palabras son anagramas (mismas letras, diferente orden).
    COMPLEJIDAD: O(n log n)  ← analiza y escribe
    """
    if len(palabra1) != len(palabra2):
        return False
    return sorted(palabra1) == sorted(palabra2)


def son_anagramas_rapido(palabra1, palabra2):
    """
    Misma funcionalidad sin ordenar.

    Estrategia: contar frecuencia de cada letra con diccionario.

    TODO: Implementar
    COMPLEJIDAD: O(n)
    """
    if len(palabra1) != len(palabra2):
        return False
    
    conteo = {}
    
    for c in palabra1:
        conteo[c] = conteo.get(c, 0) + 1
    
    for c in palabra2:
        if c not in conteo:
            return False
        conteo[c] -= 1
        if conteo[c] == 0:
            del conteo[c]
    
    return len(conteo) == 0

# COMPLEJIDAD: O(n)
    


# ─── PROBLEMA C.5 (0.4): Subarray de suma máxima ─────────────────────────────

def max_subarray_lento(lista):
    """
    Encuentra la suma máxima de un subarray contiguo.
    Ejemplo: [-2, 1, -3, 4, -1, 2, 1, -5, 4] → 6 (subarray [4, -1, 2, 1])

    COMPLEJIDAD: O(n^3)  ← analiza y escribe
    """
    n = len(lista)
    max_suma = lista[0]
    for i in range(n):
        for j in range(i, n):
            suma = 0
            for k in range(i, j + 1):
                suma += lista[k]
            max_suma = max(max_suma, suma)
    return max_suma


def max_subarray_rapido(lista):
    """
    Algoritmo de Kadane: un solo recorrido.

    Idea: mantener la suma actual. Si se vuelve negativa, reiniciar.
    - suma_actual = max(x, suma_actual + x)
    - max_suma = max(max_suma, suma_actual)

    TODO: Implementar
    COMPLEJIDAD: O(n)
    """
    

    max_suma = lista[0]
    suma_actual = lista[0]
    
    for x in lista[1:]:
        suma_actual = max(x, suma_actual + x)
        max_suma = max(max_suma, suma_actual)
    
    return max_suma

# COMPLEJIDAD: O(n)
    


# ═══════════════════════════════════════════════════════════════════════════════
#                SECCIÓN D: PROPONER Y JUSTIFICAR (1.5)
#                         
# ═══════════════════════════════════════════════════════════════════════════════

"""
PUNTO D.1 (0.5): Diseñar un algoritmo

PROBLEMA: Sistema de autocompletado
Un buscador tiene una lista de 1 millón de palabras. Cuando el usuario
escribe las primeras letras, debe mostrar las 5 palabras que empiezan
con ese prefijo.

Ejemplo:
  palabras = ["python", "programar", "programa", "prueba", "pizza", ...]
  autocompletar("pro") → ["programar", "programa"]

Propón DOS soluciones con diferente complejidad:

SOLUCIÓN 1 (fuerza bruta):
  Descripción:  Se recorre toda la lista de palabras y se verifica para cada una
  si comienza con el prefijo usando startswith().
  El proceso se detiene cuando se encuentran las primeras 5 coincidencias.
  Complejidad: O(n)
  Código:
"""


def autocompletar_v1(palabras, prefijo):
    """
    Versión fuerza bruta.
    TODO: Implementar
    COMPLEJIDAD: O(n)
    """
    resultado = []

    for palabra in palabras:
        if palabra.startswith(prefijo):
            resultado.append(palabra)
            if len(resultado) == 5:
                break

    return resultado

  


"""
SOLUCIÓN 2 (optimizada):
  Descripción: búsqueda binaria + recorrido
  Complejidad: O(log n+k)
  ¿Qué estructura de datos usarías? 
  - Lista ordenada (para usar búsqueda binaria)
  - Trie (árbol de prefijos) como alternativa más eficiente en sistemas reales
  Código:
"""


import bisect
def autocompletar_v2(palabras_ordenadas, prefijo):
    """
    Versión optimizada.
    PISTA: Si las palabras están ordenadas, puedes usar búsqueda binaria
    para encontrar dónde empiezan las que tienen el prefijo.

    TODO: Implementar
    COMPLEJIDAD: O(log n+k)
    """
    resultado = []
# Encuentra la primera posición donde podría estar el prefijo
    inicio = bisect.bisect_left(palabras_ordenadas, prefijo)

    for i in range(inicio, len(palabras_ordenadas)):
        palabra = palabras_ordenadas[i]

        if palabra.startswith(prefijo):
            resultado.append(palabra)
            if len(resultado) == 5:
                break
        else:
            # Como la lista está ordenada, si ya no coincide,
            # no habrá más coincidencias después
            break

    return resultado


"""
PUNTO D.2 (0.5): Analizar un sistema real

ESCENARIO: Red social con 10 millones de usuarios.
Cada usuario tiene una lista de amigos (promedio 200 amigos).

Analiza la complejidad de estas operaciones y propón la mejor
estructura de datos para cada una:

1. Verificar si dos usuarios son amigos
   - Con lista de amigos: O(n)
   - Con set de amigos: O(1)
   - ¿Cuál elegirías? SET  Un set permite verificar si un usuario es amigo en tiempo constante,
   mientras que en una lista hay que recorrer todos los elementos

2. Encontrar amigos en común entre dos usuarios
   - Con listas: O(n^2)
   - Con sets: O(n)
   - ¿Cuál elegirías? SET Los sets permiten hacer intersección de forma eficiente,
   evitando comparar cada elemento con todos los demás.

3. Sugerir "personas que quizás conozcas" (amigos de amigos que no son tus amigos)
   - Describe tu algoritmo: _Descripción del algoritmo:

   Para un usuario dado, primero se obtiene el conjunto de sus amigos directos.
   Luego, se recorren los amigos de cada uno de esos amigos (amigos de amigos).

   Para cada candidato encontrado:
   - Se verifica que no sea el mismo usuario
   - Se verifica que no sea ya un amigo directo (usando un set para O(1))

   Si cumple estas condiciones, se cuenta cuántas veces aparece ese candidato,
   lo que indica cuántos amigos en común tiene con el usuario.

   Finalmente, se ordenan los candidatos de mayor a menor según la cantidad
   de amigos en común y se devuelven como sugerencias.

   - Complejidad estimada: O(n * k)
     donde:
       n = número de amigos del usuario
       k = número de amigos de cada amigo

   - En el peor caso (si n ≈ k): O(n²)

   - ¿Es viable para 10M de usuarios? 
    Sí, porque el algoritmo no recorre todos los usuarios del sistema,
    sino solo los amigos y amigos de amigos del usuario actual.

   Además, en la práctica es eficiente porque:
     - n es relativamente pequeño (≈ 200)
     - se usan estructuras como set para búsquedas rápidas O(1)
     - se limita el número de sugerencias
     - se pueden cachear resultados frecuentes


4. Si cada usuario tiene en promedio 200 amigos y hay 10M de usuarios:
   - ¿Cuánta memoria ocupa almacenar TODAS las relaciones de amistad?
  - Total de relaciones:
     10M usuarios × 200 amigos = 2,000M relaciones (2 × 10⁹)

   Nota importante:
   Cada amistad se cuenta dos veces (A tiene a B y B tiene a A),
   por lo que el número real de conexiones únicas sería la mitad.

   - Con lista:
     ≈ 2 × 10⁹ × 8 bytes ≈ 16 GB

   - Con set:
     ≈ 2 × 10⁹ × 16 bytes ≈ 32 GB

   Conclusión:
   Los sets consumen más memoria, pero ofrecen búsquedas mucho más rápidas,
   lo cual es fundamental en sistemas grandes como una red social.
"""


"""
PUNTO D.3 (0.5): Reflexión y comparación

Escribe un párrafo (mínimo 5 líneas) respondiendo:

¿Por qué es importante analizar la complejidad de un algoritmo
ANTES de implementarlo? Da un ejemplo concreto de un caso donde
elegir el algoritmo incorrecto podría causar problemas reales
(tiempo de espera, costos de servidor, mala experiencia de usuario, etc.)

Tu respuesta:

""

Analizar la complejidad de un algoritmo antes de implementarlo es fundamental
porque permite anticipar cómo se va a comportar cuando el volumen de datos crezca.
Un algoritmo puede parecer rápido cuando se prueba con pocos datos, pero al aumentar
la cantidad de información puede volverse muy lento e ineficiente.

Por ejemplo, en una red social con millones de usuarios, utilizar un algoritmo
de complejidad O(n²) para sugerir amigos implicaría comparar cada usuario con
muchos otros, lo que generaría tiempos de espera muy altos. Esto no solo afecta
la experiencia del usuario, sino que también incrementa el uso de recursos del
servidor, aumentando los costos de operación.

En cambio, si desde el inicio se elige un algoritmo más eficiente, como O(n) u
O(n log n), el sistema puede responder de manera rápida incluso con grandes
cantidades de datos. Por eso, analizar la complejidad no es solo un tema teórico,
sino una decisión clave para construir sistemas escalables, eficientes y que
funcionen correctamente en la práctica.



"""


# ═══════════════════════════════════════════════════════════════════════════════
#                         CÓDIGO DE PRUEBA
# ═══════════════════════════════════════════════════════════════════════════════

def medir(funcion, *args):
    inicio = time.time()
    resultado = funcion(*args)
    return resultado, time.time() - inicio


if __name__ == "__main__":
    print("=" * 70)
    print("     TALLER: ANÁLISIS DE ALGORITMOS - PRUEBAS SECCIÓN C")
    print("=" * 70)

    # ── C.1: Únicos ──────────────────────────────────────────────
    print("\n" + "─" * 70)
    print("C.1: ELEMENTOS ÚNICOS")
    print("─" * 70)

    for n in [1000, 5000, 10000]:
        lista = [random.randint(1, n // 2) for _ in range(n)]

        r1, t1 = medir(unicos_lento, lista)
        r2, t2 = medir(unicos_rapido, lista) if unicos_rapido(lista) is not None else (None, 0)

        print(f"  n={n:>6}: lento={t1:.4f}s  rápido={t2:.4f}s", end="")
        if r2 is not None:
            print(f"  ✓ correcto" if r1 == r2 else f"  ✗ DIFERENTE")
        else:
            print("  (sin implementar)")

    # ── C.2: Más común ───────────────────────────────────────────
    print("\n" + "─" * 70)
    print("C.2: ELEMENTO MÁS COMÚN")
    print("─" * 70)

    for n in [500, 2000, 5000]:
        lista = [random.randint(1, 20) for _ in range(n)]

        r1, t1 = medir(mas_comun_lento, lista)
        r2, t2 = medir(mas_comun_rapido, lista) if mas_comun_rapido(lista) is not None else (None, 0)

        print(f"  n={n:>6}: lento={t1:.4f}s  rápido={t2:.4f}s", end="")
        if r2 is not None:
            print(f"  ✓" if r1 == r2 else f"  resultado: {r1} vs {r2}")
        else:
            print("  (sin implementar)")

    # ── C.3: Pares que suman K ───────────────────────────────────
    print("\n" + "─" * 70)
    print("C.3: PARES QUE SUMAN K")
    print("─" * 70)

    for n in [500, 2000, 5000]:
        lista = [random.randint(1, 100) for _ in range(n)]
        k = 50

        r1, t1 = medir(pares_suma_lento, lista, k)
        r2, t2 = medir(pares_suma_rapido, lista, k) if pares_suma_rapido(lista, k) is not None else (None, 0)

        print(f"  n={n:>6}: lento={t1:.4f}s  rápido={t2:.4f}s", end="")
        if r2 is not None:
            print(f"  pares encontrados: {len(r1)} vs {len(r2)}")
        else:
            print("  (sin implementar)")

    # ── C.4: Anagramas ───────────────────────────────────────────
    print("\n" + "─" * 70)
    print("C.4: ANAGRAMAS")
    print("─" * 70)

    casos_anagramas = [
        ("listen", "silent", True),
        ("hello", "world", False),
        ("anagram", "nagaram", True),
        ("python", "typhon", True),
        ("abc", "abcd", False),
    ]

    for p1, p2, esperado in casos_anagramas:
        r_lento = son_anagramas_lento(p1, p2)
        r_rapido = son_anagramas_rapido(p1, p2) if son_anagramas_rapido(p1, p2) is not None else "N/A"
        marca = "✓" if r_rapido == esperado else "✗"
        print(f"  {marca} '{p1}' vs '{p2}': lento={r_lento}, rápido={r_rapido}, esperado={esperado}")

    # ── C.5: Subarray máximo ─────────────────────────────────────
    print("\n" + "─" * 70)
    print("C.5: SUBARRAY DE SUMA MÁXIMA")
    print("─" * 70)

    casos_subarray = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1, 2, 3, 4, 5],
        [-1, -2, -3, -4],
        [5, -9, 6, -2, 3],
    ]

    for lista in casos_subarray:
        r_lento = max_subarray_lento(lista)
        r_rapido = max_subarray_rapido(lista) 
        marca = "✓" if r_rapido == r_lento else "✗"
        print(f"  {marca} {lista} → lento={r_lento}, rápido={r_rapido}")    

    for n in [100,200]: # Se limita el tamaño porque la versión lenta es O(n^3),
    # lo que hace inviable probar con valores grandes como 50000
        lista = [random.randint(-50, 50) for _ in range(n)]
        r1, t1 = medir(max_subarray_lento, lista)
        r2, t2 = medir(max_subarray_rapido, lista) if max_subarray_rapido(lista) is not None else (None, 0)
        print(f"  n={n:>6}: lento={t1:.4f}s  rápido={t2:.4f}s")

    # ── D.1: Autocompletar ───────────────────────────────────────
    print("\n" + "─" * 70)
    print("D.1: AUTOCOMPLETAR")
    print("─" * 70)

    palabras = [f"palabra_{random.randint(1000, 9999)}" for _ in range(50000)]
    palabras.extend(["python", "programar", "programa", "prueba", "pizza",
                      "proyecto", "profesor", "promedio", "proceso", "producir"])
    random.shuffle(palabras)
    palabras_ord = sorted(palabras)

    for prefijo in ["pro", "pyt", "piz", "xyz"]:
        r1, t1 = medir(autocompletar_v1, palabras, prefijo)
        r2, t2 = medir(autocompletar_v2, palabras_ord, prefijo)
        print(f"  Prefijo '{prefijo}': v1={t1:.4f}s  v2={t2:.4f}s", end="")
        if r1 is not None:
            print(f"  → {len(r1)} resultados")
        else:
            print("  (sin implementar)")
