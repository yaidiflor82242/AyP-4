#creacion de conjuntos
# Con llaves
frutas = {"manzana", "naranja", "pera"}
# Con set() - elimina duplicados
numeros = set([1, 2, 2, 3, 3, 3])
print(numeros) # {1, 2, 3}
# Conjunto vacío (NO usar {})
vacio = set()
# Desde string
letras = set("mississippi")
print(letras) # {'m', 'i', 's', 'p'}

#operaciones con conjuntos
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
# Unión
print(A | B) # {1, 2, 3, 4, 5, 6, 7, 8}
# Intersección
print(A & B) # {4, 5}
# Diferencia
print(A - B) # {1, 2, 3}
# Diferencia simétrica

#metodos útiles
colores = {"rojo", "verde", "azul"}
# Agregar elemento
colores.add("amarillo")
# Eliminar elemento
colores.remove("rojo") # Error si no existe
colores.discard("negro") # Sin error
# Verificar pertenencia
print("verde" in colores) # True
# Verificar subconjunto
A = {1, 2}
B = {1, 2, 3}
print(A <= B) # True (A es subconjunto de B)

"""
═══════════════════════════════════════════════════════════════════════════════
EJEMPLO 1: CONJUNTOS EN PYTHON (set)
Algoritmos y Programación 4 - Semana 6
═══════════════════════════════════════════════════════════════════════════════

Un CONJUNTO es una colección de elementos:
- Sin duplicados (cada elemento aparece una sola vez)
- Sin orden específico
- Los elementos deben ser inmutables (no listas ni diccionarios)

Python tiene el tipo 'set' incorporado que usaremos para entender
los conceptos antes de implementar nuestra propia estructura.
"""

# ═══════════════════════════════════════════════════════════════════════════════
# 1. Crear conjuntos
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("1. Crear conjuntos")
print("=" * 60)

# Con llaves {}
frutas = {"manzana", "naranja", "pera"}
print(f"Frutas: {frutas}")

# Con set() a partir de una lista
numeros = set([1, 2, 3, 2, 1, 4])  # Duplicados se eliminan
print(f"Números (sin duplicados): {numeros}")

# Conjunto vacío (NO usar {}, eso es diccionario vacío)
vacio = set()
print(f"Conjunto vacío: {vacio}")
print(f"Tipo de {{}}: {type({})}")  # dict
print(f"Tipo de set(): {type(set())}")  # set


# ═══════════════════════════════════════════════════════════════════════════════
# 2. Características de los conjuntos
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("2. Características")
print("=" * 60)

# No hay duplicados
letras = set("mississippi")
print(f"set('mississippi'): {letras}")  # Solo m, i, s, p

# No hay orden garantizado
numeros = {5, 2, 8, 1, 9}
print(f"Conjunto: {numeros}")  # El orden puede variar

# Cardinalidad (tamaño)
print(f"Cardinalidad: {len(numeros)}")


# ═══════════════════════════════════════════════════════════════════════════════
# 3. Pertenencia (membership)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("3. Pertenencia")
print("=" * 60)

colores = {"rojo", "verde", "azul"}

# Verificar si un elemento está en el conjunto
print(f"'rojo' in colores: {'rojo' in colores}")      # True
print(f"'amarillo' in colores: {'amarillo' in colores}")  # False
print(f"'rojo' not in colores: {'rojo' not in colores}")  # False


# ═══════════════════════════════════════════════════════════════════════════════
# 4. Agregar y eliminar elementos
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("4. Agregar y eliminar")
print("=" * 60)

animales = {"perro", "gato"}
print(f"Original: {animales}")

# Agregar un elemento
animales.add("pájaro")
print(f"Después de add('pájaro'): {animales}")

# Agregar duplicado (no hace nada)
animales.add("perro")
print(f"Después de add('perro'): {animales}")  # Sin cambio

# Eliminar elemento (error si no existe)
animales.remove("gato")
print(f"Después de remove('gato'): {animales}")

# Eliminar elemento (sin error si no existe)
animales.discard("elefante")  # No lanza error
print(f"Después de discard('elefante'): {animales}")

# Eliminar y retornar elemento arbitrario
elemento = animales.pop()
print(f"pop() retornó: {elemento}")


# ═══════════════════════════════════════════════════════════════════════════════
# 5. Iterar sobre un conjunto
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("5. Iterar")
print("=" * 60)

numeros = {10, 20, 30, 40, 50}

print("Elementos del conjunto:")
for num in numeros:
    print(f"  - {num}")

# Convertir a lista si necesitas orden
lista_ordenada = sorted(numeros)
print(f"Ordenados: {lista_ordenada}")


"""
═══════════════════════════════════════════════════════════════════════════════
EJEMPLO 2: OPERACIONES BÁSICAS ENTRE CONJUNTOS
Algoritmos y Programación 4 - Semana 6
═══════════════════════════════════════════════════════════════════════════════

Operaciones fundamentales:
- Unión (∪): elementos en A o en B
- Intersección (∩): elementos en A y en B
- Diferencia (-): elementos en A que no están en B
- Diferencia simétrica (△): elementos en A o B, pero no en ambos
"""

# ═══════════════════════════════════════════════════════════════════════════════
# Conjuntos de ejemplo
# ═══════════════════════════════════════════════════════════════════════════════

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("=" * 60)
print("Conjuntos de trabajo")
print("=" * 60)
print(f"A = {A}")
print(f"B = {B}")


# ═══════════════════════════════════════════════════════════════════════════════
# 1. UNIÓN (A ∪ B)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("1. UNIÓN (A ∪ B)")
print("   Elementos que están en A o en B (o en ambos)")
print("=" * 60)

# Método 1: operador |
union1 = A | B
print(f"A | B = {union1}")

# Método 2: método union()
union2 = A.union(B)
print(f"A.union(B) = {union2}")

# Visualización
print("""
    ┌─────────────────────────────┐
    │    A         B              │
    │  ┌─────┬─────┬─────┐        │
    │  │ 1,2,│ 4,5 │ 6,7,│        │
    │  │  3  │     │  8  │        │
    │  └─────┴─────┴─────┘        │
    │  ←───── UNIÓN ─────→        │
    └─────────────────────────────┘
""")


# ═══════════════════════════════════════════════════════════════════════════════
# 2. INTERSECCIÓN (A ∩ B)
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("2. INTERSECCIÓN (A ∩ B)")
print("   Elementos que están en A y en B")
print("=" * 60)

# Método 1: operador &
interseccion1 = A & B
print(f"A & B = {interseccion1}")

# Método 2: método intersection()
interseccion2 = A.intersection(B)
print(f"A.intersection(B) = {interseccion2}")

# Visualización
print("""
    ┌─────────────────────────────┐
    │    A         B              │
    │  ┌─────┬─────┬─────┐        │
    │  │     │ 4,5 │     │        │
    │  │     │ ^^^ │     │        │
    │  └─────┴─────┴─────┘        │
    │       INTERSECCIÓN          │
    └─────────────────────────────┘
""")


# ═══════════════════════════════════════════════════════════════════════════════
# 3. DIFERENCIA (A - B)
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("3. DIFERENCIA (A - B)")
print("   Elementos en A que NO están en B")
print("=" * 60)

# Método 1: operador -
diferencia1 = A - B
print(f"A - B = {diferencia1}")

# Método 2: método difference()
diferencia2 = A.difference(B)
print(f"A.difference(B) = {diferencia2}")

# La diferencia NO es conmutativa
print(f"\nB - A = {B - A}")
print("Nota: A - B ≠ B - A")


# ═══════════════════════════════════════════════════════════════════════════════
# 4. DIFERENCIA SIMÉTRICA (A △ B)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("4. DIFERENCIA SIMÉTRICA (A △ B)")
print("   Elementos en A o B, pero NO en ambos")
print("=" * 60)

# Método 1: operador ^
simetrica1 = A ^ B
print(f"A ^ B = {simetrica1}")

# Método 2: método symmetric_difference()
simetrica2 = A.symmetric_difference(B)
print(f"A.symmetric_difference(B) = {simetrica2}")

# Equivalencia: (A - B) ∪ (B - A)
equivalente = (A - B) | (B - A)
print(f"(A - B) | (B - A) = {equivalente}")


# ═══════════════════════════════════════════════════════════════════════════════
# 5. Resumen de operadores
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("RESUMEN DE OPERADORES")
print("=" * 60)
print("""
┌────────────────────┬──────────┬─────────────────────────┐
│ Operación          │ Operador │ Método                  │
├────────────────────┼──────────┼─────────────────────────┤
│ Unión              │    |     │ .union()                │
│ Intersección       │    &     │ .intersection()         │
│ Diferencia         │    -     │ .difference()           │
│ Diferencia simét.  │    ^     │ .symmetric_difference() │
└────────────────────┴──────────┴─────────────────────────┘
""")

"""
═══════════════════════════════════════════════════════════════════════════════
EJEMPLO 3: RELACIONES ENTRE CONJUNTOS
Algoritmos y Programación 4 - Semana 6
═══════════════════════════════════════════════════════════════════════════════

Relaciones:
- Subconjunto (⊆): todos los elementos de A están en B
- Subconjunto propio (⊂): A ⊆ B y A ≠ B
- Superconjunto (⊇): B contiene todos los elementos de A
- Igualdad (=): A y B tienen exactamente los mismos elementos
- Disjuntos: A y B no tienen elementos en común
"""

# ═══════════════════════════════════════════════════════════════════════════════
# 1. SUBCONJUNTO (A ⊆ B)
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("1. SUBCONJUNTO (A ⊆ B)")
print("   Todos los elementos de A están en B")
print("=" * 60)

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 3}

# Método 1: operador <=
print(f"A = {A}")
print(f"B = {B}")
print(f"A <= B (A es subconjunto de B): {A <= B}")  # True

# Método 2: issubset()
print(f"A.issubset(B): {A.issubset(B)}")  # True

# Un conjunto es subconjunto de sí mismo
print(f"\nA <= A: {A <= A}")  # True
print(f"A <= C: {A <= C}")  # True (son iguales)


# ═══════════════════════════════════════════════════════════════════════════════
# 2. SUBCONJUNTO PROPIO (A ⊂ B)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("2. SUBCONJUNTO PROPIO (A ⊂ B)")
print("   A ⊆ B y A ≠ B (B tiene al menos un elemento más)")
print("=" * 60)

# Operador < (subconjunto propio)
print(f"A = {A}")
print(f"B = {B}")
print(f"C = {C}")
print(f"\nA < B (A es subconjunto propio de B): {A < B}")  # True
print(f"A < C (A es subconjunto propio de C): {A < C}")  # False (son iguales)
print(f"A < A: {A < A}")  # False


# ═══════════════════════════════════════════════════════════════════════════════
# 3. SUPERCONJUNTO (A ⊇ B)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("3. SUPERCONJUNTO (A ⊇ B)")
print("   A contiene todos los elementos de B")
print("=" * 60)

# Operador >= o issuperset()
print(f"B >= A (B es superconjunto de A): {B >= A}")  # True
print(f"B.issuperset(A): {B.issuperset(A)}")  # True

# Superconjunto propio
print(f"B > A (B es superconjunto propio de A): {B > A}")  # True


# ═══════════════════════════════════════════════════════════════════════════════
# 4. IGUALDAD (A = B)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("4. IGUALDAD (A = B)")
print("   A y B tienen exactamente los mismos elementos")
print("=" * 60)

X = {1, 2, 3}
Y = {3, 2, 1}  # Mismo contenido, diferente orden
Z = {1, 2, 3, 4}

print(f"X = {X}")
print(f"Y = {Y}")
print(f"Z = {Z}")
print(f"\nX == Y: {X == Y}")  # True (el orden no importa)
print(f"X == Z: {X == Z}")  # False

# Equivalencia: A == B si y solo si A ⊆ B y B ⊆ A
print(f"\n(X <= Y) and (Y <= X): {(X <= Y) and (Y <= X)}")  # True


# ═══════════════════════════════════════════════════════════════════════════════
# 5. CONJUNTOS DISJUNTOS
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("5. CONJUNTOS DISJUNTOS")
print("   A y B no tienen elementos en común (A ∩ B = ∅)")
print("=" * 60)

pares = {2, 4, 6, 8}
impares = {1, 3, 5, 7}
primos = {2, 3, 5, 7}

print(f"pares = {pares}")
print(f"impares = {impares}")
print(f"primos = {primos}")

# Método isdisjoint()
print(f"\npares.isdisjoint(impares): {pares.isdisjoint(impares)}")  # True
print(f"pares.isdisjoint(primos): {pares.isdisjoint(primos)}")  # False (2 en común)
print(f"impares.isdisjoint(primos): {impares.isdisjoint(primos)}")  # False


# ═══════════════════════════════════════════════════════════════════════════════
# 6. Resumen de operadores de relación
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("RESUMEN DE RELACIONES")
print("=" * 60)
print("""
┌─────────────────────┬──────────┬─────────────────┐
│ Relación            │ Operador │ Método          │
├─────────────────────┼──────────┼─────────────────┤
│ Subconjunto         │    <=    │ .issubset()     │
│ Subconjunto propio  │    <     │ (no hay)        │
│ Superconjunto       │    >=    │ .issuperset()   │
│ Superconjunto propio│    >     │ (no hay)        │
│ Igualdad            │    ==    │ (no hay)        │
│ Disjuntos           │   (no)   │ .isdisjoint()   │
└─────────────────────┴──────────┴─────────────────┘
""")




"""
═══════════════════════════════════════════════════════════════════════════════
EJEMPLO 4: APLICACIONES PRÁCTICAS DE CONJUNTOS
Algoritmos y Programación 4 - Semana 6
═══════════════════════════════════════════════════════════════════════════════

Los conjuntos son útiles para:
- Eliminar duplicados
- Verificar pertenencia rápidamente
- Encontrar elementos comunes o diferentes
- Sistemas de etiquetas/tags
"""

# ═══════════════════════════════════════════════════════════════════════════════
# 1. Eliminar duplicados de una lista
# ═══════════════════════════════════════════════════════════════════════════════

print("=" * 60)
print("1. Eliminar duplicados")
print("=" * 60)

lista_con_duplicados = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
sin_duplicados = list(set(lista_con_duplicados))

print(f"Original: {lista_con_duplicados}")
print(f"Sin duplicados: {sin_duplicados}")

# Con strings
palabras = ["hola", "mundo", "hola", "python", "mundo", "hola"]
palabras_unicas = set(palabras)
print(f"\nPalabras únicas: {palabras_unicas}")


# ═══════════════════════════════════════════════════════════════════════════════
# 2. Encontrar elementos comunes (amigos en común)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("2. Amigos en común (intersección)")
print("=" * 60)

amigos_juan = {"María", "Pedro", "Ana", "Carlos", "Laura"}
amigos_maria = {"Pedro", "Laura", "Sofia", "Diego", "Ana"}

amigos_comunes = amigos_juan & amigos_maria
print(f"Amigos de Juan: {amigos_juan}")
print(f"Amigos de María: {amigos_maria}")
print(f"Amigos en común: {amigos_comunes}")

# Sugerencias de amistad (amigos de amigos que no conoces)
sugerencias_juan = amigos_maria - amigos_juan
print(f"Sugerencias para Juan: {sugerencias_juan}")


# ═══════════════════════════════════════════════════════════════════════════════
# 3. Sistema de etiquetas (tags)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("3. Sistema de etiquetas")
print("=" * 60)

# Artículos con sus etiquetas
articulo1 = {"python", "programación", "tutorial", "principiantes"}
articulo2 = {"python", "web", "django", "backend"}
articulo3 = {"javascript", "web", "frontend", "react"}

print(f"Artículo 1: {articulo1}")
print(f"Artículo 2: {articulo2}")
print(f"Artículo 3: {articulo3}")

# Artículos relacionados (tienen etiquetas en común)
print(f"\nEtiquetas comunes 1-2: {articulo1 & articulo2}")
print(f"Etiquetas comunes 2-3: {articulo2 & articulo3}")
print(f"Etiquetas comunes 1-3: {articulo1 & articulo3}")

# Todas las etiquetas usadas
todas_etiquetas = articulo1 | articulo2 | articulo3
print(f"\nTodas las etiquetas: {todas_etiquetas}")


# ═══════════════════════════════════════════════════════════════════════════════
# 4. Verificar requisitos (permisos)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("4. Sistema de permisos")
print("=" * 60)

permisos_admin = {"leer", "escribir", "eliminar", "crear_usuarios", "ver_logs"}
permisos_editor = {"leer", "escribir"}
permisos_usuario = {"leer"}

def tiene_permisos(usuario_permisos, permisos_requeridos):
    """Verifica si el usuario tiene todos los permisos requeridos"""
    return permisos_requeridos <= usuario_permisos

# Verificar acceso
accion_editar = {"leer", "escribir"}
accion_admin = {"crear_usuarios", "ver_logs"}

print(f"¿Editor puede editar? {tiene_permisos(permisos_editor, accion_editar)}")
print(f"¿Editor puede administrar? {tiene_permisos(permisos_editor, accion_admin)}")
print(f"¿Admin puede administrar? {tiene_permisos(permisos_admin, accion_admin)}")


# ═══════════════════════════════════════════════════════════════════════════════
# 5. Análisis de texto
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("5. Análisis de texto")
print("=" * 60)

texto1 = "python es un lenguaje de programación"
texto2 = "java es otro lenguaje de programación"

palabras1 = set(texto1.lower().split())
palabras2 = set(texto2.lower().split())

print(f"Texto 1: {texto1}")
print(f"Texto 2: {texto2}")
print(f"\nPalabras en común: {palabras1 & palabras2}")
print(f"Solo en texto 1: {palabras1 - palabras2}")
print(f"Solo en texto 2: {palabras2 - palabras1}")


# ═══════════════════════════════════════════════════════════════════════════════
# 6. Búsqueda eficiente
# ═══════════════════════════════════════════════════════════════════════════════

print("\n" + "=" * 60)
print("6. Búsqueda eficiente")
print("=" * 60)

# Lista vs Set para búsqueda
import time

# Crear datos
datos_lista = list(range(100000))
datos_set = set(range(100000))

# Buscar elemento
elemento = 99999

# Búsqueda en lista
inicio = time.time()
for _ in range(1000):
    _ = elemento in datos_lista
tiempo_lista = time.time() - inicio

# Búsqueda en set
inicio = time.time()
for _ in range(1000):
    _ = elemento in datos_set
tiempo_set = time.time() - inicio

print(f"Tiempo búsqueda en lista: {tiempo_lista:.4f}s")
print(f"Tiempo búsqueda en set: {tiempo_set:.4f}s")
print(f"Set es {tiempo_lista/tiempo_set:.0f}x más rápido")