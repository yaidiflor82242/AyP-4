import re

# =============================================================================
#  EJERCICIOS POSIBLES DE AJEDREZ — Algoritmos y Programación 4
# =============================================================================


# ─────────────────────────────────────────────────────────────────────────────
#  EJERCICIO 1 — MEMORIZACIÓN
#  ¿Cuántos caminos hay de (0,0) a (m,n) moviéndose solo derecha o abajo?
# ─────────────────────────────────────────────────────────────────────────────
#
#  Relación: f(m,n) = f(m-1,n) + f(m,n-1)
#  Casos base: si m==0 o n==0 → solo 1 camino (ir recto)

def caminos_tablero(m, n, memo=None):
    if memo is None: memo = {}
    if m == 0 or n == 0: return 1
    if (m, n) not in memo:
        memo[(m, n)] = caminos_tablero(m-1, n, memo) + caminos_tablero(m, n-1, memo)
    return memo[(m, n)]


# ─────────────────────────────────────────────────────────────────────────────
#  EJERCICIO 2 — MEMORIZACIÓN
#  Caminos en tablero con casillas bloqueadas (obstáculos)
#  0 = libre, 1 = bloqueada
# ─────────────────────────────────────────────────────────────────────────────
#
#  Igual que el anterior pero si la casilla está bloqueada retorna 0

def caminos_con_obstaculos(tablero, m, n, memo=None):
    if memo is None: memo = {}
    if tablero[m][n] == 1: return 0        # casilla bloqueada
    if m == 0 and n == 0: return 1         # llegamos al inicio
    if (m, n) not in memo:
        desde_arriba   = caminos_con_obstaculos(tablero, m-1, n, memo) if m > 0 else 0
        desde_izquierda = caminos_con_obstaculos(tablero, m, n-1, memo) if n > 0 else 0
        memo[(m, n)] = desde_arriba + desde_izquierda
    return memo[(m, n)]


# ─────────────────────────────────────────────────────────────────────────────
#  EJERCICIO 3 — MEMORIZACIÓN
#  Movimientos del caballo: ¿puede llegar de (0,0) a (dest_m, dest_n)
#  en exactamente k movimientos?
#  Retorna el número de formas distintas de llegar.
# ─────────────────────────────────────────────────────────────────────────────
#
#  El caballo se mueve en L: 8 posibles saltos
#  Relación: f(m, n, k) = suma de f(m', n', k-1) para cada salto válido

SALTOS_CABALLO = [
    (-2, -1), (-2, 1), (-1, -2), (-1, 2),
    ( 1, -2), ( 1, 2), ( 2, -1), ( 2,  1)
]

def caminos_caballo(m, n, k, filas, cols, memo=None):
    """
    ¿De cuántas formas puede el caballo llegar a (m,n) en exactamente k pasos
    partiendo desde (0,0) en un tablero de filas x cols?
    """
    if memo is None: memo = {}
    if k == 0:
        return 1 if (m == 0 and n == 0) else 0
    if (m, n, k) not in memo:
        total = 0
        for dm, dn in SALTOS_CABALLO:
            pm, pn = m - dm, n - dn       # posición anterior
            if 0 <= pm < filas and 0 <= pn < cols:
                total += caminos_caballo(pm, pn, k-1, filas, cols, memo)
        memo[(m, n, k)] = total
    return memo[(m, n, k)]


# ─────────────────────────────────────────────────────────────────────────────
#  EJERCICIO 4 — CONJUNTOS
#  Cada jugador tiene un conjunto de piezas capturadas.
#  Responde preguntas usando operaciones de conjuntos.
# ─────────────────────────────────────────────────────────────────────────────

piezas_blancas   = {"Rey", "Reina", "Torre", "Alfil", "Caballo", "Peón"}
piezas_negras    = {"Rey", "Reina", "Torre", "Alfil", "Caballo", "Peón"}

# Piezas capturadas durante la partida
capturadas_por_blancas = {"Reina", "Torre", "Peón", "Alfil"}
capturadas_por_negras  = {"Torre", "Peón", "Caballo", "Reina"}

def piezas_capturadas_por_ambos():
    """Piezas que ambos jugadores lograron capturar."""
    return capturadas_por_blancas & capturadas_por_negras

def piezas_solo_blancas_capturaron():
    """Piezas que solo las blancas capturaron."""
    return capturadas_por_blancas - capturadas_por_negras

def piezas_solo_negras_capturaron():
    """Piezas que solo las negras capturaron."""
    return capturadas_por_negras - capturadas_por_blancas

def todas_las_piezas_capturadas():
    """Todas las piezas capturadas en la partida."""
    return capturadas_por_blancas | capturadas_por_negras

def piezas_que_sobrevivieron():
    """Piezas que no fueron capturadas por ninguno."""
    todas = piezas_blancas | piezas_negras
    return todas - todas_las_piezas_capturadas()

def jugadores_que_capturaron(pieza):
    """Retorna qué jugadores capturaron esa pieza."""
    jugadores = []
    if pieza in capturadas_por_blancas: jugadores.append("Blancas")
    if pieza in capturadas_por_negras:  jugadores.append("Negras")
    return jugadores


# ─────────────────────────────────────────────────────────────────────────────
#  EJERCICIO 5 — LISTA ENLAZADA
#  Historial de movimientos de una partida de ajedrez.
#  Cada nodo representa un movimiento.
# ─────────────────────────────────────────────────────────────────────────────

class Movimiento:
    def __init__(self, pieza, origen, destino, captura=None):
        self.pieza    = pieza       # ej: "Caballo"
        self.origen   = origen      # ej: "e2"
        self.destino  = destino     # ej: "f4"
        self.captura  = captura     # pieza capturada o None
        self.siguiente = None

    def __str__(self):
        cap = f" captura {self.captura}" if self.captura else ""
        return f"{self.pieza}: {self.origen} → {self.destino}{cap}"

class HistorialPartida:
    def __init__(self):
        self.cabeza = None

    def mostrar(self):
        actual = self.cabeza
        if actual is None:
            print("  Sin movimientos")
            return
        turno = 1
        while actual:
            print(f"  {turno}. {actual}")
            actual = actual.siguiente
            turno += 1

    # ── helpers recursivos ──────────────────────────────────

    def _agregar_rec(self, nodo, nuevo):
        if nodo.siguiente is None:
            nodo.siguiente = nuevo
        else:
            self._agregar_rec(nodo.siguiente, nuevo)

    def _contar_rec(self, nodo):
        if nodo is None: return 0
        return 1 + self._contar_rec(nodo.siguiente)

    def _contar_capturas_rec(self, nodo):
        if nodo is None: return 0
        hubo_captura = 1 if nodo.captura else 0
        return hubo_captura + self._contar_capturas_rec(nodo.siguiente)

    def _eliminar_sin_captura_rec(self, nodo):
        if nodo is None: return None
        nodo.siguiente = self._eliminar_sin_captura_rec(nodo.siguiente)
        if nodo.captura is None:
            return nodo.siguiente
        return nodo

    # ── métodos públicos ────────────────────────────────────

    def agregar(self, pieza, origen, destino, captura=None):
        nuevo = Movimiento(pieza, origen, destino, captura)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            self._agregar_rec(self.cabeza, nuevo)

    def total_movimientos(self):
        return self._contar_rec(self.cabeza)

    def total_capturas(self):
        return self._contar_capturas_rec(self.cabeza)

    def eliminar_sin_captura(self):
        """Deja solo los movimientos donde hubo captura."""
        self.cabeza = self._eliminar_sin_captura_rec(self.cabeza)


# ─────────────────────────────────────────────────────────────────────────────
#  EJERCICIO 6 — REGEX
#  Validar notación algebraica de ajedrez
# ─────────────────────────────────────────────────────────────────────────────
#
#  Formatos válidos:
#    Movimiento de peón:   e4, d5, a1        (columna a-h + fila 1-8)
#    Movimiento de pieza:  Nf3, Bb5, Qd8     (letra mayúscula + columna + fila)
#    Captura:              Nxf3, exd5        (pieza o columna + x + destino)
#    Enroque corto:        O-O
#    Enroque largo:        O-O-O
#    Jaque:                e4+, Nf3+
#    Jaque mate:           Qd8#

def validar_movimiento_ajedrez(mov):
    patron = r'^(O-O-O|O-O|[NBRQK]?[a-h]?x?[a-h][1-8][+#]?)$'
    return bool(re.match(patron, mov))

# Desglose:
#   O-O-O        → enroque largo (se evalúa primero)
#   O-O          → enroque corto
#   [NBRQK]?     → pieza opcional (N=caballo, B=alfil, R=torre, Q=reina, K=rey)
#   [a-h]?       → columna origen opcional (para desambiguar)
#   x?           → captura opcional
#   [a-h]        → columna destino (obligatoria)
#   [1-8]        → fila destino (obligatoria)
#   [+#]?        → jaque o jaque mate opcional

def extraer_movimientos(texto):
    """Extrae todos los movimientos de ajedrez de un texto."""
    patron = r'\b(O-O-O|O-O|[NBRQK]?[a-h]?x?[a-h][1-8][+#]?)\b'
    return re.findall(patron, texto)


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA - NO MODIFICAR
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":

    # ── Ejercicio 1 ───────────────────────────────────────────
    print("=" * 60)
    print("     PRUEBAS EJERCICIO 1 - CAMINOS EN TABLERO")
    print("=" * 60)

    print("\n♟️  Caminos moviéndose solo derecha o abajo:")
    print("  caminos_tablero(1, 1) ->", caminos_tablero(1, 1))
    print("  Esperado: 2")
    print("  caminos_tablero(2, 2) ->", caminos_tablero(2, 2))
    print("  Esperado: 6")
    print("  caminos_tablero(3, 3) ->", caminos_tablero(3, 3))
    print("  Esperado: 20")
    print("  caminos_tablero(7, 7) ->", caminos_tablero(7, 7))
    print("  Esperado: 3432  (tablero 8x8 completo)")

    # ── Ejercicio 2 ───────────────────────────────────────────
    print("\n" + "=" * 60)
    print("     PRUEBAS EJERCICIO 2 - CAMINOS CON OBSTÁCULOS")
    print("=" * 60)

    tablero_libre = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    tablero_bloqueado = [
        [0, 0, 0],
        [0, 1, 0],   # centro bloqueado
        [0, 0, 0]
    ]

    print("\n♟️  Tablero 3x3 sin obstáculos:")
    print("  caminos(2, 2) ->", caminos_con_obstaculos(tablero_libre, 2, 2))
    print("  Esperado: 6")

    print("\n♟️  Tablero 3x3 con centro bloqueado:")
    print("  caminos(2, 2) ->", caminos_con_obstaculos(tablero_bloqueado, 2, 2))
    print("  Esperado: 2  (el centro bloquea muchos caminos)")

    # ── Ejercicio 3 ───────────────────────────────────────────
    print("\n" + "=" * 60)
    print("     PRUEBAS EJERCICIO 3 - MOVIMIENTOS DEL CABALLO")
    print("=" * 60)

    print("\n♞  Formas de llegar con el caballo en k movimientos (tablero 8x8):")
    print("  caminos_caballo(1, 2, 1, 8, 8) ->", caminos_caballo(1, 2, 1, 8, 8))
    print("  Esperado: 1  (un solo salto directo a (1,2))")
    print("  caminos_caballo(2, 1, 2, 8, 8) ->", caminos_caballo(2, 1, 2, 8, 8))
    print("  Esperado: 1")
    print("  caminos_caballo(0, 0, 2, 8, 8) ->", caminos_caballo(0, 0, 2, 8, 8))
    print("  Esperado: formas de volver al origen en 2 saltos")

    # ── Ejercicio 4 ───────────────────────────────────────────
    print("\n" + "=" * 60)
    print("     PRUEBAS EJERCICIO 4 - CONJUNTOS DE PIEZAS")
    print("=" * 60)

    print("\n♟️  Piezas capturadas por ambos jugadores:")
    print("  ->", piezas_capturadas_por_ambos())
    print("  Esperado: {'Reina', 'Torre', 'Peón'}")

    print("\n♟️  Piezas que solo capturaron las blancas:")
    print("  ->", piezas_solo_blancas_capturaron())
    print("  Esperado: {'Alfil'}")

    print("\n♟️  Piezas que solo capturaron las negras:")
    print("  ->", piezas_solo_negras_capturaron())
    print("  Esperado: {'Caballo'}")

    print("\n♟️  Todas las piezas capturadas:")
    print("  ->", todas_las_piezas_capturadas())
    print("  Esperado: {'Reina', 'Torre', 'Peón', 'Alfil', 'Caballo'}")

    print("\n♟️  Quién capturó la Torre:")
    print("  ->", jugadores_que_capturaron("Torre"))
    print("  Esperado: ['Blancas', 'Negras']")

    print("\n♟️  Quién capturó el Alfil:")
    print("  ->", jugadores_que_capturaron("Alfil"))
    print("  Esperado: ['Blancas']")

    # ── Ejercicio 5 ───────────────────────────────────────────
    print("\n" + "=" * 60)
    print("     PRUEBAS EJERCICIO 5 - HISTORIAL DE PARTIDA")
    print("=" * 60)

    historial = HistorialPartida()
    historial.agregar("Peón",    "e2", "e4")
    historial.agregar("Peón",    "e7", "e5")
    historial.agregar("Caballo", "g1", "f3")
    historial.agregar("Caballo", "b8", "c6")
    historial.agregar("Alfil",   "f1", "b5", captura=None)
    historial.agregar("Peón",    "d4", "e5", captura="Peón")
    historial.agregar("Torre",   "h1", "e1", captura="Reina")

    print("\n📋 Historial completo:")
    historial.mostrar()

    print("\n🔢 Total de movimientos:", historial.total_movimientos())
    print("   Esperado: 7")

    print("\n⚔️  Total de capturas:", historial.total_capturas())
    print("   Esperado: 2")

    print("\n🗑️  Eliminando movimientos sin captura...")
    historial.eliminar_sin_captura()
    print("   Movimientos restantes (solo capturas):")
    historial.mostrar()
    print("   Esperado: Peón e4xd5 y Torre h1xe1")

    # ── Ejercicio 6 ───────────────────────────────────────────
    print("\n" + "=" * 60)
    print("     PRUEBAS EJERCICIO 6 - REGEX NOTACIÓN AJEDREZ")
    print("=" * 60)

    print("\n♟️  Validación de movimientos:")
    movimientos = [
        ("e4",    True,  "peón avanza"),
        ("Nf3",   True,  "caballo a f3"),
        ("Bb5",   True,  "alfil a b5"),
        ("Nxf3",  True,  "caballo captura en f3"),
        ("exd5",  True,  "peón captura en d5"),
        ("O-O",   True,  "enroque corto"),
        ("O-O-O", True,  "enroque largo"),
        ("Qd8+",  True,  "reina da jaque"),
        ("Qd8#",  True,  "jaque mate"),
        ("e9",    False, "fila 9 no existe"),
        ("Xe4",   False, "X no es pieza válida"),
        ("44",    False, "solo números"),
    ]
    for mov, esperado, descripcion in movimientos:
        resultado = validar_movimiento_ajedrez(mov)
        print(f"  validar('{mov}') -> {resultado}   Esperado: {esperado}   ({descripcion})")

    print("\n📜 Extraer movimientos de un texto:")
    cronica = "La partida inició con e4 e5 luego Nf3 Nc6 y terminó con Qd8#"
    print(f"  texto: '{cronica}'")
    print("  extraer_movimientos() ->", extraer_movimientos(cronica))
    print("  Esperado: ['e4', 'e5', 'Nf3', 'Nc6', 'Qd8#']")