# =============================================================
#  PARCIAL MODELO 2 — Algoritmos y Programación 4
# =============================================================

import re


# ─────────────────────────────────────────────────────────────
# 1. EXPRESIONES REGULARES (20%)
# ─────────────────────────────────────────────────────────────

def validar_cedula(cedula):
    """
    Valida cédula colombiana: entre 6 y 10 dígitos, sin letras.
    validar_cedula("1234567890") -> True
    validar_cedula("123456")     -> True
    validar_cedula("12345")      -> False  (menos de 6)
    validar_cedula("12345678901")-> False  (más de 10)
    validar_cedula("123abc789")  -> False  (tiene letras)
    """
    patron = r'^\d{6,10}$'
    return bool(re.match(patron, cedula))


def extraer_precios(texto):
    """
    Extrae todos los precios de un texto.
    Formato: $ seguido de números (con posible punto o coma de miles)

    extraer_precios("El café vale $3.500 y el almuerzo $12.000")
    -> ["$3.500", "$12.000"]
    """
    patron = r'\$\d{1,3}(?:[.,]\d{3})*'
    return re.findall(patron, texto)


# ─────────────────────────────────────────────────────────────
# 2. LISTA ENLAZADA CON RECURSIVIDAD (30%)
# ─────────────────────────────────────────────────────────────

class Cancion:
    def __init__(self, titulo, duracion_seg, reproducida=False):
        self.titulo = titulo
        self.duracion_seg = duracion_seg
        self.reproducida = reproducida
        self.siguiente = None


class Playlist:
    def __init__(self):
        self.cabeza = None

    # ── helpers recursivos internos ──────────────────────────

    def _agregar_rec(self, nodo, titulo, duracion):
        """Recorre hasta el último nodo y agrega al final."""
        if nodo.siguiente is None:
            nodo.siguiente = Cancion(titulo, duracion)
        else:
            self._agregar_rec(nodo.siguiente, titulo, duracion)

    def _duracion_rec(self, nodo):
        """Suma recursiva de duraciones desde nodo."""
        if nodo is None:
            return 0
        return nodo.duracion_seg + self._duracion_rec(nodo.siguiente)

    def _eliminar_rec(self, nodo):
        """
        Retorna la nueva cabeza de la sublista con las canciones
        reproducidas eliminadas.
        """
        if nodo is None:
            return None
        nodo.siguiente = self._eliminar_rec(nodo.siguiente)
        if nodo.reproducida:
            return nodo.siguiente   # salta el nodo actual
        return nodo

    # ── métodos públicos ─────────────────────────────────────

    def agregar(self, titulo, duracion):
        """Agrega al final. OBLIGATORIO recursividad."""
        if self.cabeza is None:
            self.cabeza = Cancion(titulo, duracion)
        else:
            self._agregar_rec(self.cabeza, titulo, duracion)

    def duracion_total(self):
        """Suma duración de TODAS las canciones. Recursivo."""
        return self._duracion_rec(self.cabeza)

    def eliminar_reproducidas(self):
        """Elimina canciones ya reproducidas. Recursivo."""
        self.cabeza = self._eliminar_rec(self.cabeza)

    # ── utilidad para imprimir la lista ─────────────────────
    def __str__(self):
        canciones = []
        actual = self.cabeza
        while actual:
            estado = "✓" if actual.reproducida else " "
            canciones.append(f"[{estado}] {actual.titulo} ({actual.duracion_seg}s)")
            actual = actual.siguiente
        return "\n".join(canciones) if canciones else "(playlist vacía)"


# ─────────────────────────────────────────────────────────────
# 3. OPERACIONES CON CONJUNTOS (20%)
# ─────────────────────────────────────────────────────────────

python_devs = {"Ana", "Luis", "Marco", "Nina"}
java_devs   = {"Luis", "Oscar", "Paula", "Marco"}
js_devs     = {"Nina", "Oscar", "Rosa", "Ana"}


def fullstack():
    """Devs que saben los 3 lenguajes."""
    return python_devs & java_devs & js_devs


def especialistas():
    """Devs que saben exactamente 1 lenguaje."""
    resultado = set()
    for dev in python_devs | java_devs | js_devs:
        conteo = (dev in python_devs) + (dev in java_devs) + (dev in js_devs)
        if conteo == 1:
            resultado.add(dev)
    return resultado


def lenguajes_de(nombre):
    """Lista de lenguajes que domina el dev."""
    lenguajes = []
    if nombre in python_devs:
        lenguajes.append("Python")
    if nombre in java_devs:
        lenguajes.append("Java")
    if nombre in js_devs:
        lenguajes.append("JavaScript")
    return lenguajes


# ─────────────────────────────────────────────────────────────
# 4. RECURSIVIDAD CON MEMOIZACIÓN (30%)
# ─────────────────────────────────────────────────────────────
# f(n) = f(n-1) + f(n-2) + f(n-3)
# f(0)=1, f(1)=1, f(2)=2

def tribonacci_sin_memo(n):
    """Recursividad pura."""
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    return (tribonacci_sin_memo(n - 1)
            + tribonacci_sin_memo(n - 2)
            + tribonacci_sin_memo(n - 3))


def tribonacci_con_memo(n, memo=None):
    """
    Con memoización.
    tribonacci_con_memo(10) -> 149
    """
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    memo[n] = (tribonacci_con_memo(n - 1, memo)
               + tribonacci_con_memo(n - 2, memo)
               + tribonacci_con_memo(n - 3, memo))
    return memo[n]


# =============================================================
# PRUEBAS
# =============================================================

if __name__ == "__main__":

    print("=" * 55)
    print("1. EXPRESIONES REGULARES")
    print("=" * 55)
    print(validar_cedula("1234567890"))   # True
    print(validar_cedula("123456"))       # True
    print(validar_cedula("12345"))        # False
    print(validar_cedula("12345678901")) # False
    print(validar_cedula("123abc789"))   # False
    print(extraer_precios("El café vale $3.500 y el almuerzo $12.000"))
    # ["$3.500", "$12.000"]

    print("\n" + "=" * 55)
    print("2. LISTA ENLAZADA")
    print("=" * 55)
    pl = Playlist()
    pl.agregar("Blinding Lights", 200)
    pl.agregar("Levitating", 203)
    pl.agregar("Stay", 141)
    pl.cabeza.siguiente.reproducida = True   # marcar Levitating
    print("Antes de eliminar reproducidas:")
    print(pl)
    print(f"Duración total: {pl.duracion_total()}s")
    pl.eliminar_reproducidas()
    print("\nDespués de eliminar reproducidas:")
    print(pl)

    print("\n" + "=" * 55)
    print("3. CONJUNTOS")
    print("=" * 55)
    print("Fullstack:", fullstack())
    print("Especialistas:", especialistas())
    print("Lenguajes de Ana:", lenguajes_de("Ana"))
    print("Lenguajes de Luis:", lenguajes_de("Luis"))
    print("Lenguajes de Oscar:", lenguajes_de("Oscar"))

    print("\n" + "=" * 55)
    print("4. TRIBONACCI")
    print("=" * 55)
    print("Sin memo  tribonacci(10):", tribonacci_sin_memo(10))   # 149
    print("Con memo  tribonacci(10):", tribonacci_con_memo(10))   # 149
    print("Con memo  tribonacci(20):", tribonacci_con_memo(20))   # 35890