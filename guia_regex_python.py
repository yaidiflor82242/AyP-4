# =========================================
# GUÍA RÁPIDA REGEX EN PYTHON (PARCIAL)
# =========================================

import re

# =========================================
# 1. VALIDACIONES COMUNES
# =========================================

def validar_placa(placa):
    # ABC123 o ABC-123
    return bool(re.match(r'^[A-Z]{3}-?\d{3}$', placa))


def validar_telefono(tel):
    # 3001234567 o +573001234567
    return bool(re.match(r'^(\+57)?3\d{9}$', tel))


def validar_correo(correo):
    return bool(re.match(r'^[\w\.\+\-]+@[\w\-]+\.[\w\.\-]+$', correo))


# =========================================
# 2. EXTRACCIÓN
# =========================================

def extraer_numeros(texto):
    return re.findall(r'\d+', texto)


def extraer_hashtags(texto):
    return re.findall(r'#\w+', texto)


def extraer_menciones(texto):
    return re.findall(r'@\w+', texto)


# =========================================
# 3. SÍMBOLOS IMPORTANTES
# =========================================

# \d  → números
# \w  → letras/números/_
# .    → cualquier carácter
# *    → 0 o más
# +    → 1 o más
# ?    → opcional
# ^    → inicio
# $    → fin


# =========================================
# 4. ERRORES COMUNES
# =========================================

# ❌ SIN anclas
re.match(r'[A-Z]{3}\d{3}', 'ABC123xxx')  # True (mal)

# ✅ CON anclas
re.match(r'^[A-Z]{3}\d{3}$', 'ABC123xxx')  # False (bien)


# =========================================
# 5. PLANTILLAS PARA EXAMEN
# =========================================

def plantilla_validar(texto):
    patron = r''
    return bool(re.match(patron, texto))


def plantilla_extraer(texto):
    return re.findall(r'', texto)


# =========================================
# 6. PRUEBAS RÁPIDAS
# =========================================

if __name__ == "__main__":
    print(validar_placa("ABC123"))       # True
    print(validar_telefono("3101234567"))# True
    print(validar_correo("test@gmail.com"))
    print(extraer_hashtags("Hola #python #code"))


"""
╔══════════════════════════════════════════════════════════════════╗
║           🎯 GUÍA DE MEMORIZACIÓN REGEX PYTHON                   ║
║                    TABLA DE REFERENCIA RÁPIDA                    ║
╚══════════════════════════════════════════════════════════════════╝
"""

import re

# ══════════════════════════════════════════════════════════════════
# 🎯 1. LAS 3 FUNCIONES BÁSICAS (MEMORIZAR)
# ══════════════════════════════════════════════════════════════════

# re.match(patron, texto)    → busca SOLO al INICIO
# re.search(patron, texto)   → busca en CUALQUIER PARTE (primera coincidencia)
# re.findall(patron, texto)  → busca TODAS las coincidencias → LISTA

# ✅ SIEMPRE usar bool() para validar:
def es_valido(patron, texto):
    return bool(re.match(patron, texto))  # True/False

# ══════════════════════════════════════════════════════════════════
# 🎯 2. CARACTERES ESPECIALES (TABLA)
# ══════════════════════════════════════════════════════════════════

"""
CARÁCTER     | SIGNIFICADO                    | EQUIVALENTE
─────────────┼───────────────────────────────┼───────────────
.            | CUALQUIER carácter (no \n)    |
\d           | DÍGITO [0-9]                  |
\D           | NO dígito                     |
\w           | Letra/Número/_ [A-Za-z0-9_]   |
\W           | NO \w                         |
\s           | ESPACIO BLANCO (esp,tab,\n)   |
\S           | NO espacio                    |
^            | INICIO del string             |
$            | FINAL del string              |
"""

# ══════════════════════════════════════════════════════════════════
# 🎯 3. CUANTIFICADORES (ORDEN DE PRIORIDAD)
# ══════════════════════════════════════════════════════════════════

"""
CUANTIFICADOR | CANTIDAD               | EJEMPLO r'aX'
──────────────┼────────────────────────┼───────────────
*             | 0 o más                 | aaaa, a, ''
+             | 1 o más                 | aaaa, a
?             | 0 o 1 (opcional)        | aa, a
{n}           | EXACTAMENTE n           | aaaa (n=4)
{n,}          | MÍNIMO n                | aaaa, aaaaa...
{n,m}         | ENTRE n y m             | aaaa (n=3,m=5)
"""

# ══════════════════════════════════════════════════════════════════
# 🎯 4. CLASES [ ] Y NEGACIÓN
# ══════════════════════════════════════════════════════════════════

"""
[a-z]     → minúsculas
[A-Z]     → mayúsculas
[0-9]     → dígitos
[A-Za-z]  → letras
[A-Za-z0-9] → alfanumérico

[^abc]    → CUALQUIER cosa EXCEPTO a,b,c
[^0-9]    → NO dígitos
[^A-Za-z] → NO letras
"""

# ══════════════════════════════════════════════════════════════════
# 🎯 5. PATRONES DE PARCIAL (MEMORIZAR)
# ══════════════════════════════════════════════════════════════════

PATRONES_PARCIAL = {
    # Placa moto: ABC12D
    "placa_moto": r'^[A-Z]{3}\d{2}[A-Z]$',
    
    # Teléfono colombiano: 3101234567
    "telefono": r'^\d{10}$',
    
    # Correo básico
    "correo": r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',
    
    # Contraseña fuerte
    "password": r'^(?=.*\d)(?=.*[A-Z])[A-Za-z\d@$!%*?&]{8,}$',
    
    # Cédula: 6-10 dígitos
    "cedula": r'^\d{6,10}$',
    
    # Hashtags
    "hashtags": r'#\w+',
    
    # Menciones
    "menciones": r'@\w+',
    
    # Números grandes (3+ dígitos)
    "numeros_grandes": r'\b\d{3,}\b'
}

# ══════════════════════════════════════════════════════════════════
# 🎯 6. LOOKAHEAD — CONTRASEÑAS (IMPORTANTE)
# ══════════════════════════════════════════════════════════════════

"""
(?=...) → "debe existir más adelante"

CONTRASEÑA PERFECTA:
r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])[A-Za-z\d@$!]{8,}$'

1. (?=.*\d)        → al menos 1 NÚMERO
2. (?=.*[A-Z])     → al menos 1 MAYÚSCULA
3. (?=.*[a-z])     → al menos 1 minúscula
4. [A-Za-z\d@$!]{8,} → mínimo 8 caracteres válidos
"""

# ══════════════════════════════════════════════════════════════════
# 🎯 7. FUNCIÓN UNIVERSAL DE VALIDACIÓN
# ══════════════════════════════════════════════════════════════════

def validar(patron, texto):
    """Función reutilizable para TODOS los casos"""
    return bool(re.match(patron, texto))

def extraer(patron, texto):
    """Función reutilizable para extraer"""
    return re.findall(patron, texto)

# ══════════════════════════════════════════════════════════════════
# 🎯 8. PRUEBAS RÁPIDAS — MEMORIZAR RESULTADOS
# ══════════════════════════════════════════════════════════════════

# Crear archivo de pruebas
def pruebas_rapidas():
    print("🎯 PRUEBAS DE MEMORIZACIÓN")
    print()
    
    # Placa moto
    print("Placa moto ABC12D:", validar(r'^[A-Z]{3}\d{2}[A-Z]$', "ABC12D"))
    print("Placa moto abc12d:", validar(r'^[A-Z]{3}\d{2}[A-Z]$', "abc12d"))
    
    # Teléfono
    print("Teléfono 3101234567:", validar(r'^\d{10}$', "3101234567"))
    
    # Contraseña
    print("Password Pass123A:", validar(
        r'^(?=.*\d)(?=.*[A-Z])[A-Za-z\d@$!%*?&]{8,}$', "Pass123A"))
    
    # Extraer
    texto = "@juan #python 3101234567 ABC123"
    print("Menciones:", extraer(r'@\w+', texto))
    print("Hashtags:", extraer(r'#\w+', texto))
    print("Teléfonos:", extraer(r'\d{10}', texto))

pruebas_rapidas()

# ══════════════════════════════════════════════════════════════════
# 🎯 9. TABLA DE ESCAPE (MEMORIZAR)
# ══════════════════════════════════════════════════════════════════

"""
ESPECIALES → ESCAPAR CON \

.   *   +   ?   ^   $   {   }   [   ]   (   )   |   \

Ejemplos:
\. → punto literal
\$ → dólar literal
\+ → más literal
\$ → paréntesis literal
\\ → barra literal
"""

# ══════════════════════════════════════════════════════════════════
# 🎯 10. ERRORES FATALES (NUNCA OLVIDAR)
# ══════════════════════════════════════════════════════════════════

ERRORES_FATALES = """
❌ 1. Olvidar ^ y $ → acepta basura extra
❌ 2. Usar . en vez de \. → acepta cualquier carácter
❌ 3. match() en vez de search() → no busca en medio
❌ 4. [abc]+ en vez de (abc)+ → combina letras sueltas
❌ 5. ^ fuera de [] vs [^abc] → significados distintos
"""

print("\n" + "="*60)
print("✅ ¡GUÍA MEMORIZADA!")
print("🎓 Usa r'' siempre")
print("🎓 ^ y $ para validar")
print("🎓 (?=.*X) para lookaheads")
print("🎓 [a-z] para rangos")
print("🎓 {n,m} para repeticiones")
print("="*60)

"""🎯 PRUEBAS DE MEMORIZACIÓN

Placa moto ABC12D: True
Placa moto abc12d: False
Teléfono 3101234567: True
Password Pass123A: True
Menciones: ['@juan']
Hashtags: ['#python']
Teléfonos: ['3101234567']

FUNCIONES:     match() inicio | search() cualquier | findall() todas
CUANTIFICADORES: *0+ | +1+ | ?0-1 | {n}exacto | {n,m}rango
CARACTERES:    \d=dígito | \w=letra/número/_ | \s=espacio
VALIDAR:       ^inicio $final + bool()
LOOKAHEAD:     (?=.*\d) número | (?=.*[A-Z]) mayúscula
CLASES:        [a-z]minúsc | [A-Z]mayús | [^abc]excepto
ESCAPAR:       \. \$ \+ \$ \$ \\"""