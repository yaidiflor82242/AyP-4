# ═══════════════════════════════════════════════════════════════════════════════
#  PARCIAL - ALGORITMOS Y PROGRAMACIÓN 4
#  Politécnico Colombiano Jaime Isaza Cadavid
#  Profesor: Juan Esteban Gómez Tirado
# ═══════════════════════════════════════════════════════════════════════════════


# ───────────────────────────────────────────────────────────────────────────────
# PREGUNTA 1 · VALOR 10% — EXPRESIONES REGULARES
# ───────────────────────────────────────────────────────────────────────────────
# Se analizan las opciones dadas en el parcial:
#
# CORREO ELECTRÓNICO (e.g. usuario@dominio.com):
#   Respuesta correcta: c) ^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$
#   - a) falla: el punto no está escapado (. = cualquier carácter, no un punto literal)
#   - b) falla: estructura incorrecta, empieza con dígitos y @ en posición equivocada
#   - d) falla: solo acepta dígitos antes del @
#   - c) ✓ acepta letras/números/guiones antes del @, subdominios y TLD de 2-7 letras
#
# TELÉFONO (+57 300 1234567):
#   Respuesta correcta: d) ^\+57 \d{3} \d{7}$
#   - a) falla: no incluye el + inicial
#   - b) y c) fallan: el + sin escapar significa "uno o más" en regex, no el símbolo +
#   - d) ✓ \+ escapa el signo literal, 57 fijo, luego 3 y 7 dígitos exactos

import re

def verificar_regex_correo(correo):
    """Valida un correo usando la regex correcta de la pregunta 1."""
    patron = r'^[\w-]+(\.[\w-]+)*@([\w-]+\.)+[a-zA-Z]{2,7}$'
    return bool(re.match(patron, correo))

def verificar_regex_telefono(telefono):
    """Valida un teléfono colombiano usando la regex correcta de la pregunta 1."""
    patron = r'^\+57 \d{3} \d{7}$'
    return bool(re.match(patron, telefono))


# ───────────────────────────────────────────────────────────────────────────────
# PREGUNTA 2 · VALOR 35% — MEMOIZACIÓN (RUTAS DEL ROBOT)
# ───────────────────────────────────────────────────────────────────────────────
# Problema: un robot va de (0,0) a (m,n) moviéndose solo → o ↓.
# La versión recursiva original recalcula los mismos subproblemas exponencialmente:
#   Complejidad original → O(2^(m+n))
#
# Solución: MEMOIZACIÓN — guardar cada resultado (m, n) en un diccionario.
# Si ya calculamos ese par, lo devolvemos directamente sin recursión adicional.
#   Complejidad con memo → O(m × n)  ← cada par se calcula UNA sola vez
#
# Nota: usamos memo=None en lugar de memo={} como parámetro por defecto porque
# en Python los objetos mutables por defecto se comparten entre llamadas,
# lo que causaría bugs si se llama la función varias veces.

def contar_rutas(m, n, memo=None):
    """
    Cuenta las rutas posibles de (0,0) a (m,n) moviéndose solo → o ↓.
    Usa memoización para evitar recálculos: O(m*n) en lugar de O(2^(m+n)).
    """
    if memo is None:
        memo = {}

    # Caso base: en el borde de la cuadrícula solo existe 1 ruta posible
    if m == 0 or n == 0:
        return 1

    # Si ya calculamos este par, lo retornamos directo (evita recálculo)
    if (m, n) in memo:
        return memo[(m, n)]

    # Calculamos sumando rutas desde arriba y desde la izquierda
    memo[(m, n)] = contar_rutas(m - 1, n, memo) + contar_rutas(m, n - 1, memo)
    return memo[(m, n)]


# ───────────────────────────────────────────────────────────────────────────────
# PREGUNTA 3 · VALOR 35% — OPERACIONES CON CONJUNTOS (STREAMING)
# ───────────────────────────────────────────────────────────────────────────────
# Los conjuntos (set) de Python tienen operadores nativos para analizar suscripciones:
#
#   Unión          (|)  → todos los usuarios sin duplicados
#   Intersección   (&)  → usuarios con ambos planes
#   Diferencia     (-)  → usuarios solo en un plan específico
#   Dif. simétrica (^)  → usuarios en exactamente uno de los dos planes
#   Pertenencia   (in)  → verificar si un usuario está en un conjunto

plan_cine   = {"Ana", "Luis", "Pedro", "Sofía", "Carlos", "Lucía"}
plan_series = {"Pedro", "Sofía", "Marta", "Andrés", "Lucía", "Valentina"}

# 1. Todos los usuarios sin duplicados → UNIÓN (|)
todos = plan_cine | plan_series

# 2. Suscritos a ambos planes → INTERSECCIÓN (&)
ambos_planes = plan_cine & plan_series

# 3. Solo en Cine, no en Series → DIFERENCIA (-)
solo_cine = plan_cine - plan_series

# 4. En exactamente un plan (no en los dos) → DIFERENCIA SIMÉTRICA (^)
exclusivos = plan_cine ^ plan_series

# 5. Verificar si "Carlos" está en plan Series → operador in
carlos_en_series = "Carlos" in plan_series

# 6. Porcentaje de usuarios que ya calificarían para el plan premium
#    (tienen ambos servicios)
premium      = ambos_planes
pct_vs_cine  = (len(premium) / len(plan_cine)) * 100   # respecto al plan Cine
pct_vs_total = (len(premium) / len(todos))     * 100   # respecto al total único


# ───────────────────────────────────────────────────────────────────────────────
# PREGUNTA 4 · VALOR 20% — COMPLEJIDAD BIG O
# ───────────────────────────────────────────────────────────────────────────────
# VERSIÓN ORIGINAL → O(n²)
# El bucle externo recorre n elementos y el interno hasta n-1, n-2...
# Total de comparaciones: n(n-1)/2 → O(n²)
# Si duplicamos la lista (n → 2n): el tiempo se CUADRUPLICA → (2n)² = 4n²
#
# VERSIÓN EFICIENTE → O(n)
# Para cada número calculamos su complemento (objetivo - numero) y buscamos
# en un set. La búsqueda en set es O(1), por lo que el bucle único es O(n).
# Si duplicamos la lista: el tiempo solo se DUPLICA → 2n

def encontrar_pares_original(lista, objetivo):
    """Versión original O(n²): dos bucles anidados."""
    n = len(lista)
    for i in range(n):              # O(n)
        for j in range(i + 1, n):  # O(n) → total O(n²)
            if lista[i] + lista[j] == objetivo:
                print(f"  Par: ({lista[i]}, {lista[j]})")

def encontrar_pares_eficiente(lista, objetivo):
    """
    Versión eficiente O(n): un solo bucle con búsqueda en set O(1).
    Retorna lista de tuplas con los pares encontrados.
    """
    vistos = set()
    pares  = []
    for numero in lista:
        complemento = objetivo - numero
        if complemento in vistos:      # O(1) en un set
            pares.append((complemento, numero))
        vistos.add(numero)
    return pares


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA — NO MODIFICAR
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":

    # ── PRUEBAS PREGUNTA 1 ──────────────────────────────────────────────────
    print("=" * 60)
    print("         PRUEBAS PREGUNTA 1 — EXPRESIONES REGULARES")
    print("=" * 60)

    correos_validos   = ["usuario@dominio.com", "ana.garcia@empresa.co", "dev+test@sub.dominio.org"]
    correos_invalidos = ["sinArroba.com", "@sinusuario.com", "usuario@.com"]

    print("\n Correos VÁLIDOS (deben dar True):")
    for c in correos_validos:
        resultado = verificar_regex_correo(c)
        estado    = "PASA" if resultado else "FALLA"
        print(f"  {estado}  {c} → {resultado}")

    print("\n Correos INVÁLIDOS (deben dar False):")
    for c in correos_invalidos:
        resultado = verificar_regex_correo(c)
        estado    = "PASA" if not resultado else "FALLA"
        print(f"  {estado}  {c} → {resultado}")

    telefonos_validos   = ["+57 300 1234567", "+57 310 7654321"]
    telefonos_invalidos = ["57 300 1234567", "+57 30 1234567", "+57 300 123456"]

    print("\n Teléfonos VÁLIDOS (deben dar True):")
    for t in telefonos_validos:
        resultado = verificar_regex_telefono(t)
        estado    = "PASA" if resultado else "FALLA"
        print(f"  {estado}  {t} → {resultado}")

    print("\n Teléfonos INVÁLIDOS (deben dar False):")
    for t in telefonos_invalidos:
        resultado = verificar_regex_telefono(t)
        estado    = "PASA" if not resultado else "FALLA"
        print(f"  {estado}  {t} → {resultado}")

    # ── PRUEBAS PREGUNTA 2 ──────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("     PRUEBAS PREGUNTA 2 — RUTAS CON MEMOIZACIÓN")
    print("=" * 60)

    casos = [
        ((3, 3), 20,        "cuadrícula 3×3 del enunciado"),
        ((2, 2),  6,        "cuadrícula 2×2"),
        ((0, 5),  1,        "borde superior → 1 sola ruta"),
        ((1, 1),  2,        "cuadrícula 1×1"),
        ((15,15), 155117520,"caso grande — instantáneo con memo"),
    ]

    for (m, n), esperado, descripcion in casos:
        resultado = contar_rutas(m, n)
        estado    = "PASA" if resultado == esperado else "FALLA"
        print(f"\n  {estado}  contar_rutas({m}, {n})  [{descripcion}]")
        print(f"         Resultado : {resultado}")
        print(f"         Esperado  : {esperado}")

    # ── PRUEBAS PREGUNTA 3 ──────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("     PRUEBAS PREGUNTA 3 — OPERACIONES CON CONJUNTOS")
    print("=" * 60)

    print(f"\n1. Todos los usuarios (unión |):")
    print(f"   {sorted(todos)}")
    estado = "PASA" if len(todos) == 9 else "FALLA"
    print(f"   {estado}  Cantidad esperada: 9  →  Obtenida: {len(todos)}")

    print(f"\n2. Con ambos planes (intersección &):")
    print(f"   {sorted(ambos_planes)}")
    esperado_2 = {"Pedro", "Sofía", "Lucía"}
    estado = "PASA" if ambos_planes == esperado_2 else "FALLA"
    print(f"   {estado}  Esperado: {sorted(esperado_2)}")

    print(f"\n3. Solo en Cine (diferencia -):")
    print(f"   {sorted(solo_cine)}")
    esperado_3 = {"Ana", "Luis", "Carlos"}
    estado = "PASA" if solo_cine == esperado_3 else "FALLA"
    print(f"   {estado}  Esperado: {sorted(esperado_3)}")

    print(f"\n4. Exclusivos de un solo plan (dif. simétrica ^):")
    print(f"   {sorted(exclusivos)}")
    esperado_4 = {"Ana", "Luis", "Carlos", "Marta", "Andrés", "Valentina"}
    estado = "PASA" if exclusivos == esperado_4 else "FALLA"
    print(f"   {estado}  Cantidad esperada: 6  →  Obtenida: {len(exclusivos)}")

    print(f"\n5. ¿Carlos en plan Series? (operador in)")
    estado = "PASA" if not carlos_en_series else "FALLA"
    print(f"   {estado}  Resultado: {carlos_en_series}  →  Esperado: False")

    print(f"\n6. Plan premium (tienen ambos servicios):")
    print(f"   Usuarios premium   : {sorted(premium)}")
    print(f"   % respecto a Cine  : {pct_vs_cine:.1f}%   (esperado 50.0%)")
    print(f"   % respecto al total: {pct_vs_total:.1f}%   (esperado 33.3%)")
    estado = "PASA" if round(pct_vs_cine, 1) == 50.0 and round(pct_vs_total, 1) == 33.3 else "FALLA"
    print(f"   {estado}")

    # ── PRUEBAS PREGUNTA 4 ──────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("     PRUEBAS PREGUNTA 4 — COMPLEJIDAD BIG O")
    print("=" * 60)

    numeros  = [1, 3, 5, 7, 9]
    objetivo = 10

    print(f"\n  Lista  : {numeros}")
    print(f"  Objetivo: {objetivo}")

    print(f"\n  Versión O(n²) — original (imprime directamente):")
    encontrar_pares_original(numeros, objetivo)

    pares    = encontrar_pares_eficiente(numeros, objetivo)
    esperado = [(3, 7), (1, 9)]
    estado   = "PASA" if pares == esperado else "FALLA"
    print(f"\n  Versión O(n) — eficiente con set:")
    print(f"  Pares encontrados : {pares}")
    print(f"  Esperado          : {esperado}")
    print(f"  {estado}")

    print(f"\n  Comparación de crecimiento al duplicar la lista (n → 2n):")
    print(f"  O(n²) : tiempo se CUADRUPLICA  →  (2n)² = 4n²")
    print(f"  O(n)  : tiempo se DUPLICA      →  2n")

    print("\n" + "=" * 60)
    print("  FIN DE PRUEBAS")
    print("=" * 60)