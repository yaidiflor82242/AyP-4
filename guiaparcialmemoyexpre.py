# =============================================================================
#  GUÍA COMPLETA DE PARCIAL — Algoritmos y Programación 4
#  Temas: Expresiones Regulares + Memorización
# =============================================================================

import re


# ─────────────────────────────────────────────────────────────────────────────
#  PARTE 1 — EXPRESIONES REGULARES
# ─────────────────────────────────────────────────────────────────────────────

# ┌─────────────────────────────────────────────────────────────┐
# │  CARACTERES ESPECIALES                                      │
# ├────────────┬────────────────────────────────────────────────┤
# │  .         │  cualquier carácter excepto salto de línea     │
# │  \d        │  dígito (0-9)                                  │
# │  \D        │  NO es dígito                                  │
# │  \w        │  letra, dígito o guion bajo                    │
# │  \W        │  NO es \w                                      │
# │  \s        │  espacio, tab, salto de línea                  │
# │  \S        │  NO es espacio                                 │
# └────────────┴────────────────────────────────────────────────┘

# ┌─────────────────────────────────────────────────────────────┐
# │  CUANTIFICADORES — ¿cuántas veces?                         │
# ├────────────┬────────────────────────────────────────────────┤
# │  *         │  0 o más veces                                 │
# │  +         │  1 o más veces                                 │
# │  ?         │  0 o 1 vez (opcional)                          │
# │  {n}       │  exactamente n veces                           │
# │  {n,m}     │  entre n y m veces                             │
# │  {n,}      │  n o más veces                                 │
# └────────────┴────────────────────────────────────────────────┘

# ┌─────────────────────────────────────────────────────────────┐
# │  ANCLAS — posición en el texto                             │
# ├────────────┬────────────────────────────────────────────────┤
# │  ^         │  inicio del texto (FUERA de [])                │
# │  $         │  fin del texto                                 │
# │  ^ y $     │  texto completo exacto                         │
# └────────────┴────────────────────────────────────────────────┘

# ┌─────────────────────────────────────────────────────────────┐
# │  CLASES  []                                                 │
# ├─────────────────────────────────────────────────────────────┤
# │  [ABC]      exactamente A, B o C                            │
# │  [A-Z]      cualquier mayúscula                             │
# │  [a-z]      cualquier minúscula                             │
# │  [0-9]      cualquier dígito  (= \d)                        │
# │  [A-Za-z]   cualquier letra                                 │
# │  [^abc]     cualquier cosa EXCEPTO a, b, c                  │
# │             ↑ ^ dentro de [] = negación (NO inicio)         │
# └─────────────────────────────────────────────────────────────┘

# ⚠️  EL ^ TIENE DOS SIGNIFICADOS:
#   ^abc     → fuera de [] → inicio del texto
#   [^abc]   → dentro de [] → negación (ni a, ni b, ni c)


# ─────────────────────────────────────────────────────────────────────────────
#  LAS 4 FUNCIONES PRINCIPALES
# ─────────────────────────────────────────────────────────────────────────────

# re.match()  → busca solo al INICIO del string
re.match(r'\d+', '123abc')    # ✅ encuentra '123'
re.match(r'\d+', 'abc123')    # ❌ no encuentra nada

# re.search() → busca en CUALQUIER parte del string
re.search(r'\d+', 'abc123')   # ✅ encuentra '123'
re.search(r'\d+', 'abcXYZ')   # ❌ no hay dígitos

# re.findall() → retorna TODAS las coincidencias como lista
re.findall(r'\d+', 'a1 b22 c333')          # ['1', '22', '333']
re.findall(r'#\w+', 'Hola #python #100d')  # ['#python', '#100d']

# re.sub() → reemplaza coincidencias
re.sub(r'\d+', '#', 'a1 b22 c3')    # 'a# b# c#'
re.sub(r'\s+', ' ', 'hola   mundo') # 'hola mundo'

# ── match vs search ───────────────────────────────────────────
# match  → solo busca al INICIO. Si no coincide desde el primer
#          carácter, retorna None.
# search → escanea TODO el string buscando la primera coincidencia.
# Para validar texto completo: usa match con ^ y $


# ─────────────────────────────────────────────────────────────────────────────
#  EJERCICIOS TÍPICOS DE PARCIAL — REGEX
# ─────────────────────────────────────────────────────────────────────────────


# ── 1. CORREO ELECTRÓNICO ────────────────────────────────────────────────────
#  Formato: usuario@dominio.extension  (ej: hola@gmail.com)

def validar_correo(correo):
    patron = r'^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron, correo))

# Desglose del patrón:
#   ^           → inicio
#   [\w.-]+     → usuario: letras, dígitos, punto, guion (1 o más)
#   @           → arroba literal
#   [\w.-]+     → dominio
#   \.          → punto literal  ← el \ escapa el punto
#   [a-zA-Z]{2,}→ extensión: mínimo 2 letras (com, co, org...)
#   $           → fin

print(validar_correo("hola@gmail.com"))     # True
print(validar_correo("hola@gmail"))         # False — falta extensión
print(validar_correo("hola gmail.com"))     # False — falta @
print(validar_correo("@gmail.com"))         # False — falta usuario


# ── 2. PLACA DE VEHÍCULO COLOMBIANA ─────────────────────────────────────────
#  Formato: 3 letras mayúsculas + 3 dígitos (ABC123 o ABC-123)

def validar_placa(placa):
    return bool(re.match(r'^[A-Z]{3}-?\d{3}$', placa))

# Desglose:
#   [A-Z]{3}   → exactamente 3 letras mayúsculas
#   -?         → guion opcional
#   \d{3}      → exactamente 3 dígitos

print(validar_placa("ABC123"))    # True
print(validar_placa("ABC-123"))   # True
print(validar_placa("abc123"))    # False — minúsculas
print(validar_placa("AB1234"))    # False — formato incorrecto
print(validar_placa("ABCD123"))   # False — 4 letras


# ── 3. TELÉFONO COLOMBIANO ───────────────────────────────────────────────────
#  Formato: 3001234567  o  +573001234567

def validar_telefono(tel):
    patron = r'^(\+57)?[0-9]{10}$'
    return bool(re.match(patron, tel))

# Desglose:
#   (\+57)?    → prefijo +57 opcional  (el + se escapa con \)
#   [0-9]{10}  → exactamente 10 dígitos

print(validar_telefono("3001234567"))      # True
print(validar_telefono("+573001234567"))   # True
print(validar_telefono("300123"))          # False — muy corto
print(validar_telefono("30012345678"))     # False — muy largo


# ── 4. CONTRASEÑA SEGURA ─────────────────────────────────────────────────────
#  Reglas: mínimo 8 chars, al menos 1 mayúscula, 1 minúscula, 1 dígito

def validar_contrasena(pwd):
    tiene_upper  = bool(re.search(r'[A-Z]', pwd))
    tiene_lower  = bool(re.search(r'[a-z]', pwd))
    tiene_digito = bool(re.search(r'\d', pwd))
    largo_ok     = len(pwd) >= 8
    return tiene_upper and tiene_lower and tiene_digito and largo_ok

# Nota: se usa search (no match) porque la mayúscula puede estar
# en cualquier posición del string, no necesariamente al inicio.

print(validar_contrasena("Hola1234"))   # True
print(validar_contrasena("hola1234"))   # False — falta mayúscula
print(validar_contrasena("HOLA1234"))   # False — falta minúscula
print(validar_contrasena("Hola123"))    # False — muy corta


# ── 5. FECHA (DD/MM/AAAA) ───────────────────────────────────────────────────

def validar_fecha(fecha):
    return bool(re.match(r'^\d{2}/\d{2}/\d{4}$', fecha))

# Desglose:
#   \d{2}   → exactamente 2 dígitos (día)
#   /       → barra literal
#   \d{2}   → exactamente 2 dígitos (mes)
#   /       → barra literal
#   \d{4}   → exactamente 4 dígitos (año)

print(validar_fecha("06/04/2026"))   # True
print(validar_fecha("6/4/2026"))     # False — no son 2 dígitos
print(validar_fecha("06-04-2026"))   # False — usa guion no barra
print(validar_fecha("06/04/26"))     # False — año de 2 dígitos


# ── 6. HASHTAGS ──────────────────────────────────────────────────────────────

def extraer_hashtags(texto):
    return re.findall(r'#\w+', texto)

# Desglose:
#   #    → símbolo # literal
#   \w+  → 1 o más letras, dígitos o guion bajo

print(extraer_hashtags("Hola #python es #genial y #100dias"))
# ['#python', '#genial', '#100dias']


# ── 7. URL SIMPLE ────────────────────────────────────────────────────────────

def validar_url(url):
    patron = r'^https?://[\w.-]+\.[a-zA-Z]{2,}(/.*)?$'
    return bool(re.match(patron, url))

# Desglose:
#   https?      → http o https (la s es opcional)
#   ://         → literal
#   [\w.-]+     → dominio
#   \.          → punto literal
#   [a-zA-Z]{2,}→ extensión
#   (/.*)?      → ruta opcional

print(validar_url("https://google.com"))           # True
print(validar_url("http://sitio.com/pagina"))       # True
print(validar_url("ftp://sitio.com"))               # False
print(validar_url("google.com"))                    # False — falta http


# ── 8. CÉDULA COLOMBIANA ─────────────────────────────────────────────────────
#  Formato: entre 6 y 10 dígitos

def validar_cedula(cedula):
    return bool(re.match(r'^\d{6,10}$', cedula))

print(validar_cedula("1234567890"))   # True
print(validar_cedula("123"))          # False — muy corta
print(validar_cedula("123abc"))       # False — tiene letras


# ─────────────────────────────────────────────────────────────────────────────
#  PARTE 2 — MEMORIZACIÓN
# ─────────────────────────────────────────────────────────────────────────────

# ¿Qué es?
# ─────────
# Técnica para optimizar funciones recursivas.
# La primera vez que calculas algo → lo guardas en un diccionario.
# Las siguientes veces → lo buscas directamente, sin recalcular.
#
# Sin memo: O(2^n) → exponencial → lentísimo para n grande
# Con memo: O(n)   → lineal     → rápido siempre
#
# Cuándo usarla:
#   ✅ f(n) = f(n-1) + f(n-2)
#   ✅ "¿de cuántas formas...?"
#   ✅ n es grande (30, 50, 100...)
#   ✅ el resultado de f(n) siempre es el mismo para el mismo n


# ─────────────────────────────────────────────────────────────────────────────
#  PLANTILLA UNIVERSAL
# ─────────────────────────────────────────────────────────────────────────────

def mi_funcion(n, memo=None):
    if memo is None:           # Paso 1: crear libreta si no existe
        memo = {}              #         (NUNCA usar memo={} como default)

    # Paso 2: casos base (los que sabes sin calcular)
    if n == 0: return 1
    if n == 1: return 1

    # Paso 3: si no está en la libreta, calcular y guardar
    if n not in memo:
        memo[n] = mi_funcion(n-1, memo) + mi_funcion(n-2, memo)
        #                         ↑↑↑↑                   ↑↑↑↑
        #               SIEMPRE pasar memo a cada llamada recursiva

    # Paso 4: retornar desde la libreta
    return memo[n]


# ❌ ERROR MÁS COMÚN: olvidar pasar memo
# memo[n] = f(n-1) + f(n-2)           ← memo se pierde, no sirve de nada
# memo[n] = f(n-1, memo) + f(n-2, memo) ← correcto

# ❌ ERROR MÁS COMÚN: usar memo={} como default
# def f(n, memo={}):   ← Python crea ese dict UNA sola vez para siempre,
#                         todas las llamadas comparten el mismo → bugs raros
# def f(n, memo=None): ← correcto, crea uno nuevo cada vez


# ─────────────────────────────────────────────────────────────────────────────
#  EJERCICIOS TÍPICOS DE PARCIAL — MEMORIZACIÓN
# ─────────────────────────────────────────────────────────────────────────────


# ── 1. ESCALONES ─────────────────────────────────────────────────────────────
#  Problema: ¿de cuántas formas puedes subir N escalones
#            si puedes subir 1 o 2 a la vez?
#
#  Relación: f(n) = f(n-1) + f(n-2)
#  Casos base: f(0) = 1, f(1) = 1

def escalones_sin_memo(n):
    # Recursividad pura — lento para n > 35
    if n == 0: return 1
    if n == 1: return 1
    return escalones_sin_memo(n-1) + escalones_sin_memo(n-2)


def escalones_con_memo(n, memo=None):
    if memo is None: memo = {}
    if n == 0: return 1
    if n == 1: return 1
    if n not in memo:
        memo[n] = escalones_con_memo(n-1, memo) + escalones_con_memo(n-2, memo)
    return memo[n]

print(escalones_con_memo(10))   # 89
print(escalones_con_memo(30))   # 1346269


# ── 2. FIBONACCI ─────────────────────────────────────────────────────────────
#  Relación: F(n) = F(n-1) + F(n-2)
#  Casos base: F(0) = 0, F(1) = 1

def fibonacci(n, memo=None):
    if memo is None: memo = {}
    if n == 0: return 0
    if n == 1: return 1
    if n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

print(fibonacci(10))   # 55
print(fibonacci(50))   # 12586269025  (instantáneo con memo)


# ── 3. ESCALONES CON 1, 2 O 3 PELDAÑOS ──────────────────────────────────────
#  Variante: puedes subir 1, 2 o 3 escalones a la vez
#  Relación: f(n) = f(n-1) + f(n-2) + f(n-3)

def escalones_3(n, memo=None):
    if memo is None: memo = {}
    if n == 0: return 1
    if n == 1: return 1
    if n == 2: return 2
    if n not in memo:
        memo[n] = (escalones_3(n-1, memo) +
                   escalones_3(n-2, memo) +
                   escalones_3(n-3, memo))
    return memo[n]

print(escalones_3(5))    # 13
print(escalones_3(10))   # 274


# ── 4. CAMINOS EN CUADRÍCULA ─────────────────────────────────────────────────
#  Problema: ¿cuántos caminos hay de (0,0) a (m,n)
#            moviéndose solo hacia la derecha o hacia abajo?
#
#  Relación: f(m,n) = f(m-1,n) + f(m,n-1)
#  Casos base: si m==0 o n==0 → solo 1 camino (ir recto)

def caminos(m, n, memo=None):
    if memo is None: memo = {}
    if m == 0 or n == 0: return 1    # borde: solo un camino posible
    if (m, n) not in memo:
        memo[(m, n)] = caminos(m-1, n, memo) + caminos(m, n-1, memo)
    return memo[(m, n)]

print(caminos(2, 2))   # 6
print(caminos(3, 3))   # 20


# ── 5. POTENCIA RÁPIDA ───────────────────────────────────────────────────────
#  Truco: x^n = x^(n//2) * x^(n//2)   si n es par
#         x^n = x^(n//2) * x^(n//2) * x  si n es impar
#  → memo evita calcular x^(n//2) dos veces

def potencia(x, n, memo=None):
    if memo is None: memo = {}
    if n == 0: return 1
    if n == 1: return x
    if n not in memo:
        mitad = potencia(x, n // 2, memo)
        if n % 2 == 0:
            memo[n] = mitad * mitad
        else:
            memo[n] = mitad * mitad * x
    return memo[n]

print(potencia(2, 10))   # 1024
print(potencia(3, 5))    # 243


# ─────────────────────────────────────────────────────────────────────────────
#  RESUMEN — ERRORES MÁS COMUNES EN PARCIAL
# ─────────────────────────────────────────────────────────────────────────────

# REGEX ────────────────────────────────────────────────────────────────────────
#
#  ❌  Olvidar ^ y $    → r'\d{3}'   valida "123" pero también "abc123abc"
#  ✅  Siempre usar     → r'^\d{3}$' valida SOLO "123"
#
#  ❌  Punto sin escapar → r'gmail.com'   el . acepta cualquier carácter
#  ✅  Punto escapado    → r'gmail\.com'  el \. es punto literal
#
#  ❌  ^ dentro de []   → [^abc] NO es "empieza con abc"
#  ✅  ^ dentro de []   → [^abc] es "cualquier cosa EXCEPTO a, b, c"
#
#  ❌  Usar match para buscar en medio de texto
#  ✅  Usar search cuando el patrón puede estar en cualquier parte

# MEMORIZACIÓN ────────────────────────────────────────────────────────────────
#
#  ❌  No pasar memo:   memo[n] = f(n-1) + f(n-2)
#  ✅  Pasar memo:      memo[n] = f(n-1, memo) + f(n-2, memo)
#
#  ❌  def f(n, memo={}):    bug: dict compartido entre todas las llamadas
#  ✅  def f(n, memo=None):  correcto: dict nuevo en cada llamada externa
#
#  ❌  Olvidar casos base → recursión infinita → RecursionError
#  ✅  Siempre definir los casos base ANTES del bloque de memo