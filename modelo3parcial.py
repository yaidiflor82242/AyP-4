import re
import time

# =============================================================================
# ALGORITMOS Y PROGRAMACIÓN 4 — MODELO A
# Listas enlazadas · Conjuntos · Memoización · Regex · Big O  |  100 pts
# =============================================================================


# =============================================================================
# 1. EXPRESIONES REGULARES (20 pts)
# =============================================================================

def validar_ip(ip):
    """
    Valida si una cadena es una dirección IPv4 válida.
    Formato: 4 números del 0-255 separados por puntos.
    Ejemplos:
      validar_ip("192.168.1.1")   -> True
      validar_ip("256.0.0.1")     -> False
      validar_ip("192.168.1")     -> False
      validar_ip("abc.def.g.h")   -> False
    """
    octeto = r'(25[0-5]|2[0-4]\d|1?\d\d?)'   # 0-255 con regex hace match a números válidos
    patron = rf'^{octeto}\.{octeto}\.{octeto}\.{octeto}$'
    return bool(re.match(patron, ip))


def extraer_urls(texto):
    """
    Extrae todas las URLs (http o https) de un texto.
    Ejemplos:
      extraer_urls("visita https://google.com y http://python.org")
      -> ["https://google.com", "http://python.org"]
    """
    patron = r'https?://[^\s]+'
    return re.findall(patron, texto)


# =============================================================================
# 2. LISTA ENLAZADA CON RECURSIVIDAD (30 pts)
#    Sistema de turnos para una clínica
# =============================================================================

class Turno:
    def __init__(self, paciente, prioridad, atendido=False):
        self.paciente  = paciente
        self.prioridad = prioridad  # "alta", "media", "baja"
        self.atendido  = atendido
        self.siguiente = None


class ColaTurnos:
    def __init__(self):
        self.cabeza = None

    def _agregar_inicio_rec(self, nodo, nuevo):
        # Caso base: lista vacía
        if nodo is None:
            return nuevo
        
        # Caso recursivo:
        nuevo.siguiente = nodo
        return nuevo


    def agregar_inicio(self, paciente, prioridad):
        nuevo = Turno(paciente, prioridad)
        self.cabeza = self._agregar_inicio_rec(self.cabeza, nuevo)

    def _contar(self, nodo, p):
        if nodo is None:
            return 0
        cuenta = 1 if (nodo.prioridad == p and not nodo.atendido) else 0
        return cuenta + self._contar(nodo.siguiente, p)

    def contar_por_prioridad(self, prioridad):
        return self._contar(self.cabeza, prioridad)

    def _invertir(self, nodo):
        if nodo is None or nodo.siguiente is None:
            return nodo
        nueva_cabeza             = self._invertir(nodo.siguiente)
        nodo.siguiente.siguiente = nodo
        nodo.siguiente           = None
        return nueva_cabeza

    def invertir(self):
        self.cabeza = self._invertir(self.cabeza)


# =============================================================================
# 3. CONJUNTOS (20 pts)
# =============================================================================

ingles  = {"Ana", "Luis", "Pedro", "Sofía", "Marta"}
frances = {"Luis", "Sofía", "Tomás", "Elena"}
aleman  = {"Pedro", "Tomás", "Ana", "Raúl"}

# a) Todos los estudiantes de idiomas (sin duplicados)
todos = ingles | frances | aleman
# -> {'Ana','Luis','Pedro','Sofía','Marta','Tomás','Elena','Raúl'}  (8)

# b) Estudiantes que estudian inglés Y francés
ingles_y_frances = ingles & frances
# -> {'Luis', 'Sofía'}

# c) Estudiantes que estudian SOLO inglés (no los demás)
solo_ingles = ingles - frances - aleman
# -> {'Marta'}

# d) Estudiantes que estudian los TRES idiomas
los_tres = ingles & frances & aleman
# -> set()  (ninguno está en los tres)

# e) ¿Qué porcentaje del total estudia al menos dos idiomas?
dos_o_mas  = (ingles & frances) | (ingles & aleman) | (frances & aleman)
# -> {'Luis','Sofía','Pedro','Ana','Tomás'}  (5)
porcentaje = len(dos_o_mas) / len(todos) * 100
# -> 62.5%


# =============================================================================
# 4. RECURSIVIDAD Y MEMOIZACIÓN — ESCALERA CON SALTOS VARIABLES (30 pts)
# =============================================================================

def escalones3_sin_memo(n):
    """
    Cuenta formas de subir n escalones dando 1, 2 o 3 pasos.
    Casos base: n==0 -> 1, n==1 -> 1, n==2 -> 2
    Sin memoización.  Complejidad: O(3^n)
    """
    if n == 0: return 1
    if n == 1: return 1
    if n == 2: return 2
    return (escalones3_sin_memo(n - 1)
          + escalones3_sin_memo(n - 2)
          + escalones3_sin_memo(n - 3))


def escalones3_con_memo(n, memo=None):
    """
    Misma función con memoización en diccionario.
    escalones3_con_memo(20) -> 121415
    Complejidad: O(n)
    """
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0: return 1
    if n == 1: return 1
    if n == 2: return 2
    memo[n] = (escalones3_con_memo(n - 1, memo)
             + escalones3_con_memo(n - 2, memo)
             + escalones3_con_memo(n - 3, memo))
    return memo[n]


# Medición de tiempo con n=30
t0 = time.time()
print("Sin memo:", escalones3_sin_memo(30))
print("Tiempo sin memo:", round(time.time() - t0, 6), "s")

t0 = time.time()
print("Con memo:", escalones3_con_memo(30))
print("Tiempo con memo:", round(time.time() - t0, 6), "s")

# Complejidades:
#   escalones3_sin_memo -> O(3^n)  (árbol de llamadas se triplica en cada nivel)
#   escalones3_con_memo -> O(n)    (cada subproblema se calcula una sola vez)