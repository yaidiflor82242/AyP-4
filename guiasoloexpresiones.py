"""
╔══════════════════════════════════════════════════════════════════╗
║         GUÍA COMPLETA — EXPRESIONES REGULARES EN PYTHON         ║
║                  Algoritmos y Programación 4                     ║
╚══════════════════════════════════════════════════════════════════╝

ÍNDICE:
  1. ¿Qué es una expresión regular?
  2. Las tres funciones principales: match, search, findall
  3. Caracteres básicos: . \d \D \w \W \s \S
  4. Cuantificadores: * + ? {n} {n,m} {n,}
  5. Anclas: ^ $
  6. Clases de caracteres: [abc] [a-z] [^abc]
  7. Grupos y alternativas: (abc) a|b
  8. Escapar caracteres especiales: \. \$ \+ etc.
  9. Ejemplos completos tipo parcial
  10. Errores más comunes
"""

import re



# ══════════════════════════════════════════════════════════════════
# 1. ¿QUÉ ES UNA EXPRESIÓN REGULAR?
# ══════════════════════════════════════════════════════════════════
"""
Una expresión regular (regex) es un PATRÓN que describe cómo debe
verse un texto. Es como una regla que le dices a Python:
"busca texto que se vea así".

Siempre se escribe con r'' (raw string) para evitar problemas
con la barra invertida \

  CORRECTO:  r'^[A-Z]{3}\d{3}$'
  CUIDADO:    '^[A-Z]{3}\\d{3}$'   (también funciona pero menos legible)
"""

# ══════════════════════════════════════════════════════════════════
# 2. LAS TRES FUNCIONES PRINCIPALES
# ══════════════════════════════════════════════════════════════════

texto = "Mi código postal es 110111 y el teléfono es 3101234567"

# re.match() → busca SOLO al inicio del string
# Retorna un objeto Match si encuentra, None si no
resultado = re.match(r'\d', texto)
print(resultado)  # None — el texto no empieza con dígito

# re.search() → busca en CUALQUIER parte, retorna el PRIMERO que encuentre
resultado = re.search(r'\d+', texto)
print(resultado.group())  # "110111" — el primer número que encontró

# re.findall() → busca en CUALQUIER parte, retorna TODOS en una lista
resultado = re.findall(r'\d+', texto)
print(resultado)  # ["110111", "3101234567"]

# re.match() con bool → para validar True/False
def es_valido(patron, texto):
    return bool(re.match(patron, texto))


# ══════════════════════════════════════════════════════════════════
# 3. CARACTERES BÁSICOS
# ══════════════════════════════════════════════════════════════════

# ─── . (punto) ───────────────────────────────────────────────────
# Acepta CUALQUIER carácter excepto salto de línea \n
print(bool(re.match(r'^.$', 'a')))   # True  — una letra
print(bool(re.match(r'^.$', '5')))   # True  — un número
print(bool(re.match(r'^.$', '@')))   # True  — un símbolo
print(bool(re.match(r'^.$', '\n')))  # False — salto de línea NO

# ⚠️ TRAMPA COMÚN: el punto acepta cosas que no quieres
print(bool(re.match(r'3.14', '3.14')))  # True  ✓
print(bool(re.match(r'3.14', '3X14')))  # True  ✗ ERROR! el . acepta X
print(bool(re.match(r'3\.14', '3X14'))) # False ✓ con \. solo acepta punto

# ─── \d y \D ─────────────────────────────────────────────────────
# \d  → dígito, equivale a [0-9]
# \D  → todo lo que NO es dígito
print(bool(re.match(r'^\d$', '7')))    # True
print(bool(re.match(r'^\d$', 'a')))    # False
print(bool(re.match(r'^\D$', 'a')))    # True
print(bool(re.match(r'^\D$', '7')))    # False

# ─── \w y \W ─────────────────────────────────────────────────────
# \w  → letra, número o guion bajo [A-Za-z0-9_]
# \W  → todo lo que NO es \w (espacios, símbolos, etc.)
print(bool(re.match(r'^\w+$', 'hola_123')))  # True
print(bool(re.match(r'^\w+$', 'hola!')))     # False — el ! no es \w
print(bool(re.match(r'^\W$', '!')))          # True
print(bool(re.match(r'^\W$', 'a')))          # False

# ─── \s y \S ─────────────────────────────────────────────────────
# \s  → espacio en blanco (espacio, \t tab, \n nueva línea)
# \S  → todo lo que NO es espacio
print(bool(re.match(r'^\s$', ' ')))          # True  — espacio
print(bool(re.match(r'hola\smundo', 'hola mundo')))  # True
print(bool(re.match(r'^\S+$', 'sinEspacios')))       # True
print(bool(re.match(r'^\S+$', 'con espacios')))      # False


# ══════════════════════════════════════════════════════════════════
# 4. CUANTIFICADORES — ¿CUÁNTAS VECES SE REPITE?
# ══════════════════════════════════════════════════════════════════

# ─── * (cero o más) ──────────────────────────────────────────────
# El carácter anterior puede aparecer 0 o más veces
print(bool(re.match(r'^a*$', '')))      # True  — 0 veces
print(bool(re.match(r'^a*$', 'aaa')))  # True  — 3 veces
print(bool(re.match(r'^a*$', 'b')))    # False — b no es a

# ─── + (uno o más) ───────────────────────────────────────────────
# El carácter anterior debe aparecer AL MENOS 1 vez
print(bool(re.match(r'^a+$', 'a')))    # True
print(bool(re.match(r'^a+$', 'aaa')))  # True
print(bool(re.match(r'^a+$', '')))     # False — necesita mínimo 1

# ─── ? (opcional) ────────────────────────────────────────────────
# El carácter anterior puede estar (1 vez) o no estar (0 veces)
print(bool(re.match(r'^colou?r$', 'color')))   # True  — sin u
print(bool(re.match(r'^colou?r$', 'colour')))  # True  — con u
print(bool(re.match(r'^-?\d+$', '42')))        # True  — positivo
print(bool(re.match(r'^-?\d+$', '-42')))       # True  — negativo

# ─── {n} (exactamente n veces) ───────────────────────────────────
print(bool(re.match(r'^[A-Z]{3}$', 'ABC')))    # True  — exactamente 3
print(bool(re.match(r'^[A-Z]{3}$', 'AB')))     # False — faltan
print(bool(re.match(r'^[A-Z]{3}$', 'ABCD')))   # False — sobran

# ─── {n,m} (entre n y m veces) ───────────────────────────────────
print(bool(re.match(r'^\d{6,10}$', '123456')))     # True  — 6 dígitos
print(bool(re.match(r'^\d{6,10}$', '1234567890'))) # True  — 10 dígitos
print(bool(re.match(r'^\d{6,10}$', '12345')))      # False — muy poco
print(bool(re.match(r'^\d{6,10}$', '12345678901')))# False — demasiado

# ─── {n,} (mínimo n veces, sin máximo) ───────────────────────────
print(bool(re.match(r'^\d{3,}$', '123')))       # True  — mínimo 3
print(bool(re.match(r'^\d{3,}$', '123456789'))) # True  — más también
print(bool(re.match(r'^\d{3,}$', '12')))        # False — menos de 3


# ══════════════════════════════════════════════════════════════════
# 5. ANCLAS — ^ Y $
# ══════════════════════════════════════════════════════════════════
"""
^ → el patrón debe empezar desde el INICIO del string
$ → el patrón debe terminar al FINAL del string

Sin anclas, el patrón puede estar "escondido" en cualquier parte.
"""

# Sin anclas — peligroso para validación
print(bool(re.match(r'\d{3}', 'abc123def')))   # False (match busca inicio)
print(bool(re.search(r'\d{3}', 'abc123def')))  # True — search encuentra en medio

# Con anclas — correcto para validar
print(bool(re.match(r'^\d{3}$', '123')))       # True  — solo 3 dígitos
print(bool(re.match(r'^\d{3}$', '1234')))      # False — tiene más
print(bool(re.match(r'^\d{3}$', 'a123')))      # False — empieza con letra

# Ejemplo clásico: sin $ la validación falla silenciosamente
print(bool(re.match(r'^[A-Z]{3}', 'ABCxxx')))  # True  ← SIN $ acepta basura
print(bool(re.match(r'^[A-Z]{3}$', 'ABCxxx'))) # False ← CON $ es estricto


# ══════════════════════════════════════════════════════════════════
# 6. CLASES DE CARACTERES — [ ]
# ══════════════════════════════════════════════════════════════════

# ─── [abc] — uno de estos ────────────────────────────────────────
print(bool(re.match(r'^[aeiou]$', 'a')))   # True  — vocal
print(bool(re.match(r'^[aeiou]$', 'b')))   # False — no es vocal
print(bool(re.match(r'^[ABC]$', 'B')))     # True

# ─── [a-z] — rango ───────────────────────────────────────────────
print(bool(re.match(r'^[a-z]+$', 'hola')))      # True  — solo minúsculas
print(bool(re.match(r'^[a-z]+$', 'Hola')))      # False — H es mayúscula
print(bool(re.match(r'^[A-Za-z]+$', 'HolaMundo'))) # True — ambas
print(bool(re.match(r'^[A-Za-z0-9]+$', 'user123')))# True — alfanumérico

# ─── [^abc] — negación ───────────────────────────────────────────
# ^ DENTRO de corchetes = "ninguno de estos"
print(bool(re.match(r'^[^aeiou]+$', 'rytm')))  # True  — cero vocales
print(bool(re.match(r'^[^aeiou]+$', 'hola')))  # False — tiene vocales
print(bool(re.match(r'^[^0-9]+$', 'abc')))     # True  — ningún dígito
print(bool(re.match(r'^[^0-9]+$', 'abc1')))    # False — tiene el 1


# ══════════════════════════════════════════════════════════════════
# 7. GRUPOS Y ALTERNATIVAS
# ══════════════════════════════════════════════════════════════════

# ─── (abc) — grupo ───────────────────────────────────────────────
# Agrupa para aplicar cuantificadores al grupo completo
print(bool(re.match(r'^(ab)+$', 'ab')))      # True  — "ab" 1 vez
print(bool(re.match(r'^(ab)+$', 'ababab')))  # True  — "ab" 3 veces
print(bool(re.match(r'^(ab)+$', 'aba')))     # False — grupo incompleto

# También para capturar partes del texto
m = re.match(r'^(\d{3})-(\d{7})$', '300-1234567')
if m:
    print(m.group(1))  # "300"       — primer grupo
    print(m.group(2))  # "1234567"   — segundo grupo

# ─── a|b — alternativa (OR) ──────────────────────────────────────
print(bool(re.match(r'^(gato|perro)$', 'gato')))   # True
print(bool(re.match(r'^(gato|perro)$', 'perro')))  # True
print(bool(re.match(r'^(gato|perro)$', 'pez')))    # False
print(bool(re.match(r'^(si|no|tal vez)$', 'no')))  # True


# ══════════════════════════════════════════════════════════════════
# 8. ESCAPAR CARACTERES ESPECIALES
# ══════════════════════════════════════════════════════════════════
"""
Estos caracteres tienen significado especial en regex:
  . * + ? ^ $ { } [ ] ( ) | \

Para usarlos como caracteres LITERALES hay que escaparlos con \
"""

# \. → punto literal (no "cualquier carácter")
print(bool(re.match(r'^\d+\.\d+$', '3.14')))   # True  — decimal
print(bool(re.match(r'^\d+\.\d+$', '3X14')))   # False — X no es punto

# \$ → signo de dólar literal
print(bool(re.match(r'^\$\d+$', '$100')))       # True
print(bool(re.match(r'^\$\d+$', '100')))        # False — sin $

# \+ → signo más literal
print(bool(re.match(r'^\d\+\d$', '3+5')))       # True
print(bool(re.match(r'^\+\d{2}$', '+57')))      # True — código de país

# \( y \) → paréntesis literales
print(bool(re.match(r'^\(\d{3}\)$', '(123)')))  # True


# ══════════════════════════════════════════════════════════════════
# 9. EJEMPLOS COMPLETOS TIPO PARCIAL
# ══════════════════════════════════════════════════════════════════

# ─── Placa vehicular colombiana ──────────────────────────────────
def validar_placa_vehiculo(placa):
    """
    Formato válido: 3 letras mayúsculas + guion opcional + 3 dígitos
    ABC123 → True
    ABC-123 → True
    abc123 → False (minúsculas)
    AB1234 → False (2 letras, 4 dígitos)
    """
    patron = r'^[A-Z]{3}-?\d{3}$'
    return bool(re.match(patron, placa))

print(validar_placa_vehiculo("ABC123"))   # True
print(validar_placa_vehiculo("ABC-123"))  # True
print(validar_placa_vehiculo("abc123"))   # False
print(validar_placa_vehiculo("AB1234"))   # False

# ─── Correo electrónico ──────────────────────────────────────────
def validar_correo(correo):
    """
    Formato: texto@dominio.extension
    Acepta: letras, números, puntos, guiones, + antes del @
    """
    patron = r'^[\w\.\+\-]+@[\w\-]+\.[\w\.\-]+$'
    return bool(re.match(patron, correo))

print(validar_correo("usuario@gmail.com"))       # True
print(validar_correo("user.name@uni.edu.co"))    # True
print(validar_correo("sinArroba.com"))           # False
print(validar_correo("@sinusuario.com"))         # False

# ─── Cédula colombiana ───────────────────────────────────────────
def validar_cedula(cedula):
    """Entre 6 y 10 dígitos, solo números"""
    patron = r'^\d{6,10}$'
    return bool(re.match(patron, cedula))

print(validar_cedula("1234567890"))   # True
print(validar_cedula("12345"))        # False — muy corta
print(validar_cedula("12345678901"))  # False — muy larga
print(validar_cedula("123abc789"))    # False — tiene letras

# ─── Extraer hashtags ────────────────────────────────────────────
def extraer_hashtags(texto):
    """Extrae todos los #hashtags del texto"""
    return re.findall(r'#\w+', texto)

print(extraer_hashtags("Hola #python es #genial y #100dias"))
# → ['#python', '#genial', '#100dias']

# ─── Extraer menciones ───────────────────────────────────────────
def extraer_menciones(texto):
    """Extrae todas las @menciones del texto"""
    return re.findall(r'@\w+', texto)

print(extraer_menciones("Hola @juan y @maria_99, cc @bot3"))
# → ['@juan', '@maria_99', '@bot3']

# ─── Extraer precios ─────────────────────────────────────────────
def extraer_precios(texto):
    """Extrae precios con formato $3.500 o $12,000"""
    return re.findall(r'\$[\d\.,]+', texto)

print(extraer_precios("El café vale $3.500 y el almuerzo $12.000"))
# → ['$3.500', '$12.000']

# ─── Número de teléfono colombiano ───────────────────────────────
def validar_telefono(tel):
    """
    Celular colombiano: empieza con 3, exactamente 10 dígitos
    También acepta +57 al inicio
    """
    patron = r'^(\+57)?3\d{9}$'
    return bool(re.match(patron, tel))

print(validar_telefono("3101234567"))     # True
print(validar_telefono("+573101234567"))  # True
print(validar_telefono("3001234567"))     # True
print(validar_telefono("123456789"))      # False


# ══════════════════════════════════════════════════════════════════
# 10. ERRORES MÁS COMUNES
# ══════════════════════════════════════════════════════════════════

# ERROR 1: Olvidar ^ y $ — el patrón acepta basura extra
patron_malo  = r'[A-Z]{3}\d{3}'      # ← sin anclas
patron_bueno = r'^[A-Z]{3}\d{3}$'    # ← con anclas

print(bool(re.match(patron_malo,  'ABC123!!!!')))  # True  ← acepta basura
print(bool(re.match(patron_bueno, 'ABC123!!!!')))  # False ← correcto

# ERROR 2: Usar . cuando quieres punto literal
patron_malo  = r'^\d+.\d+$'    # el . acepta cualquier cosa
patron_bueno = r'^\d+\.\d+$'   # \. es punto de verdad

print(bool(re.match(patron_malo,  '3X14')))  # True  ← acepta X!!
print(bool(re.match(patron_bueno, '3X14')))  # False ← correcto

# ERROR 3: Olvidar que re.match() solo busca al inicio
# Si quieres buscar en cualquier parte, usa re.search()
texto = "El número es 12345"
print(bool(re.match(r'\d+', texto)))    # False — no empieza con dígito
print(bool(re.search(r'\d+', texto)))   # True  — lo encuentra en medio

# ERROR 4: [^abc] vs ^ fuera de corchetes — significados DISTINTOS
# ^ fuera de [] = inicio del string
# ^ dentro de [] = negación de la clase
print(bool(re.match(r'^abc', 'abc123')))   # True  — empieza con abc
print(bool(re.match(r'^[^abc]', 'xyz')))   # True  — empieza con algo que NO es a,b,c
print(bool(re.match(r'^[^abc]', 'abc')))   # False — empieza con a que sí está en [abc]


# ══════════════════════════════════════════════════════════════════
# RESUMEN VISUAL DE TODOS LOS SÍMBOLOS
# ══════════════════════════════════════════════════════════════════
"""
BÁSICOS:
  .        → cualquier carácter (menos \n)
  \d       → dígito [0-9]
  \D       → no dígito
  \w       → letra, número o _ [A-Za-z0-9_]
  \W       → no \w
  \s       → espacio en blanco (espacio, \t, \n)
  \S       → no espacio

CUANTIFICADORES (van después del carácter):
  *        → 0 o más veces
  +        → 1 o más veces
  ?        → 0 o 1 vez (opcional)
  {n}      → exactamente n veces
  {n,m}    → entre n y m veces
  {n,}     → mínimo n veces

ANCLAS:
  ^        → inicio del string
  $        → fin del string

CLASES:
  [abc]    → exactamente uno de: a, b o c
  [a-z]    → cualquiera en el rango a-z
  [A-Z]    → cualquiera en el rango A-Z
  [0-9]    → cualquiera en el rango 0-9
  [^abc]   → cualquiera EXCEPTO a, b y c

GRUPOS:
  (abc)    → agrupa para cuantificar o capturar
  a|b      → a OR b

ESCAPAR ESPECIALES:
  \.       → punto literal
  \$       → dólar literal
  \+       → más literal
  \(  \)   → paréntesis literales
  \\       → barra invertida literal
"""
# ===================== LOOKAHEAD (?=...) EN REGEX =====================
#
# (?=...)  → Lookahead positivo
#
# ✔ Sirve para VERIFICAR que algo exista en la cadena
# ✔ NO consume caracteres (no forma parte del match)
# ✔ Solo impone una condición
#
# ---------------------------------------------------------------
# 🧠 IDEA CLAVE:
# "Debe existir X en algún lugar del texto, pero no importa dónde"
#
# ---------------------------------------------------------------
# 🔹 Ejemplo 1: Verificar que haya un número
#
# Regex:
# r'(?=.*\d)'
#
# Explicación:
# .*  → cualquier cantidad de caracteres
# \d  → un número
#
# ✔ "abc123"     → válido
# ❌ "abcdef"     → inválido
#
# ---------------------------------------------------------------
# 🔹 Ejemplo 2: Verificar que haya una mayúscula
#
# Regex:
# r'(?=.*[A-Z])'
#
# ✔ "holaMundo"  → válido
# ❌ "holamundo" → inválido
#
# ---------------------------------------------------------------
# 🔹 Ejemplo 3: Contraseña completa
#
# Regex:
# r'^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$'
#
# Explicación:
# ^                 → inicio
# (?=.*[A-Z])       → al menos una mayúscula
# (?=.*\d)          → al menos un número
# [A-Za-z\d]{8,}    → mínimo 8 caracteres (solo letras y números)
# $                 → fin
#
# ✔ "Abcdefg1"     → válido
# ❌ "abcdefg1"     → no tiene mayúscula
# ❌ "ABCDEFGH"     → no tiene número
# ❌ "Abc123"       → muy corta
#
# ---------------------------------------------------------------
# 🔥 IMPORTANTE:
# Los lookaheads se pueden combinar para exigir varias condiciones:
#
# (?=.*A)(?=.*B)(?=.*C)
#
# → "Debe haber A, B y C en cualquier parte"
#
# ---------------------------------------------------------------
# 🚀 RESUMEN:
# (?=...) → verifica condición sin consumir texto
# Ideal para validaciones (contraseñas, correos, etc.)
# =====================================================================


# ===================== REGEX: (), [], {} =====================
#
# 🔹 1. CORCHETES [ ]
#
# ✔ Representan UN SOLO carácter de una lista
#
# Ejemplos:
# [abc]        → "a" o "b" o "c"
# [a-z]        → cualquier letra minúscula
# [A-Z0-9]     → letras mayúsculas o números
#
# Ejemplo en uso:
# r'[aeiou]'   → encuentra una vocal
#
# ⚠️ IMPORTANTE:
# [abc] ≠ "abc"
# → solo coincide con UN carácter
#
# -------------------------------------------------------------
# 🔹 2. PARÉNTESIS ( )
#
# ✔ Agrupan expresiones completas
# ✔ Permiten aplicar operadores a grupos
# ✔ Sirven para capturar coincidencias
#
# Ejemplos:
# (ab)         → coincide con "ab"
# (ab)+        → "ab", "abab", "ababab"
# (hola|adios) → "hola" o "adios"
#
# Ejemplo en uso:
# r'(ha)+'     → "ha", "hahaha"
#
# 🔥 También se usan en:
# (?=...)      → lookahead positivo
# (?!...)      → lookahead negativo
#
# -------------------------------------------------------------
# 🔹 3. LLAVES { }
#
# ✔ Indican REPETICIONES exactas o rangos
#
# Ejemplos:
# a{3}     → "aaa" (exactamente 3 veces)
# a{2,5}   → entre 2 y 5 veces
# a{2,}    → mínimo 2 veces
#
# Ejemplo en uso:
# r'\d{4}' → exactamente 4 números (ej: 2024)
#
# -------------------------------------------------------------
# 🔥 COMBINACIONES IMPORTANTES
#
# r'[a-z]{3}'     → exactamente 3 letras minúsculas
# r'(ab){2}'      → "abab"
# r'[0-9]{2,4}'   → entre 2 y 4 dígitos
#
# -------------------------------------------------------------
# ⚠️ ERRORES COMUNES
#
# ❌ [abc]+  → cualquier combinación de a, b, c
# ✔ (abc)+   → repite "abc"
#
# ❌ (a-z)   → incorrecto para rangos
# ✔ [a-z]    → correcto
#
# -------------------------------------------------------------
# 🧠 RESUMEN CLAVE
#
# [ ] → un carácter de una lista
# ( ) → agrupar o capturar patrones
# { } → cuántas veces se repite algo
#
# =============================================================

"""VALIDAR CONTRASEÑA

import re

def validar(password):
    return (
        re.match(r'^[A-Za-z\d!@#$%]{8,}$', password) and
        re.search(r'[A-Z]', password) and
        re.search(r'[a-z]', password) and
        re.search(r'\d', password) and
        re.search(r'[!@#$%]', password)
    )
"""

def validar_nombre(nombre):
    patron= r'^[a-z]{1}([a-z]|\d){4,9}$'
    return bool(re.match(patron, nombre))

validar_nombre("juan")      # False (menos de 5 caracteres)