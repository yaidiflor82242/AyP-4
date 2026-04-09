# =========================================
# 🎮 JUEGOS BÁSICOS CON CONJUNTOS (SET)
# =========================================


# =========================================
# 1. VALIDAR FILA DE SUDOKU
# =========================================

def validar_fila_sudoku(fila):
    """
    Verifica si una fila de sudoku es válida (sin repetir números del 1 al 9)
    """
    return len(fila) == len(set(fila)) and all(1 <= x <= 9 for x in fila)


# PRUEBA
print("Sudoku válido:", validar_fila_sudoku([1,2,3,4,5,6,7,8,9]))
print("Sudoku inválido:", validar_fila_sudoku([1,2,2,4,5,6,7,8,9]))


# =========================================
# 2. TRES EN RAYA (TIC TAC TOE)
# =========================================

def verificar_ganador(movimientos):
    """
    movimientos: set de posiciones (1 a 9)
    """
    combinaciones = [
        {1,2,3}, {4,5,6}, {7,8,9},  # filas
        {1,4,7}, {2,5,8}, {3,6,9},  # columnas
        {1,5,9}, {3,5,7}            # diagonales
    ]
    
    for combo in combinaciones:
        if combo.issubset(movimientos):
            return True
    return False


# PRUEBA
jugador = {1, 2, 3}
print("Ganó:", verificar_ganador(jugador))


# =========================================
# 3. JUEGO DE ADIVINAR NÚMEROS
# =========================================

def adivinar_numero(numero_secreto, intentos):
    """
    intentos: set de números intentados
    """
    if numero_secreto in intentos:
        return "¡Adivinaste!"
    else:
        faltantes = {numero_secreto} - intentos
        return f"No adivinaste. Faltaba: {faltantes}"


# PRUEBA
print(adivinar_numero(7, {1,2,3,7}))
print(adivinar_numero(5, {1,2,3}))


# =========================================
# 4. MINI AJEDREZ (MOVIMIENTOS DE TORRE)
# =========================================

def movimientos_torre(posicion):
    """
    posicion: (fila, columna) en tablero 8x8
    Retorna todas las posiciones posibles
    """
    fila, col = posicion
    
    movimientos = set()
    
    # misma fila
    for c in range(8):
        if c != col:
            movimientos.add((fila, c))
    
    # misma columna
    for f in range(8):
        if f != fila:
            movimientos.add((f, col))
    
    return movimientos


# PRUEBA
print("Movimientos torre desde (0,0):")
print(movimientos_torre((0,0)))


# =========================================
# 5. JUEGO DE CARTAS (SIN REPETIR)
# =========================================

def repartir_cartas():
    baraja = {f"{n}{p}" for n in range(1,14) for p in ["♠","♥","♦","♣"]}
    
    import random
    cartas = set(random.sample(list(baraja), 5))
    
    return cartas


# PRUEBA
print("Cartas:", repartir_cartas())


# =========================================
# 6. DETECTAR NÚMEROS REPETIDOS
# =========================================

def hay_repetidos(lista):
    return len(lista) != len(set(lista))


# PRUEBA
print("Repetidos:", hay_repetidos([1,2,3,4,5]))
print("Repetidos:", hay_repetidos([1,2,2,3]))


# =========================================
# 7. JUEGO: INTERSECCIÓN DE JUGADORES
# =========================================

def jugadores_comunes(equipo1, equipo2):
    return equipo1 & equipo2


# PRUEBA
print(jugadores_comunes({"Ana","Luis"}, {"Luis","Pedro"}))


# =========================================
# FIN
# =========================================

# =========================================
# ♟️ AJEDREZ BÁSICO CON CONJUNTOS
# =========================================

# Tablero: coordenadas (fila, columna) de 0 a 7

# =========================================
# 1. POSICIONES INICIALES
# =========================================

# Piezas blancas
torres_blancas = {(7,0), (7,7)}
caballos_blancos = {(7,1), (7,6)}
alfiles_blancos = {(7,2), (7,5)}
reina_blanca = {(7,3)}
rey_blanco = {(7,4)}
peones_blancos = {(6,i) for i in range(8)}

# Piezas negras
torres_negras = {(0,0), (0,7)}
caballos_negros = {(0,1), (0,6)}
alfiles_negros = {(0,2), (0,5)}
reina_negra = {(0,3)}
rey_negro = {(0,4)}
peones_negros = {(1,i) for i in range(8)}


# =========================================
# 2. FUNCIONES DE MOVIMIENTO
# =========================================

def movimientos_torre(pos):
    fila, col = pos
    movs = set()

    for i in range(8):
        if i != col:
            movs.add((fila, i))
        if i != fila:
            movs.add((i, col))
    
    return movs


def movimientos_alfil(pos):
    fila, col = pos
    movs = set()

    for i in range(1,8):
        if fila+i < 8 and col+i < 8:
            movs.add((fila+i, col+i))
        if fila-i >= 0 and col-i >= 0:
            movs.add((fila-i, col-i))
        if fila+i < 8 and col-i >= 0:
            movs.add((fila+i, col-i))
        if fila-i >= 0 and col+i < 8:
            movs.add((fila-i, col+i))
    
    return movs


def movimientos_caballo(pos):
    fila, col = pos
    posibles = [
        (fila+2, col+1), (fila+2, col-1),
        (fila-2, col+1), (fila-2, col-1),
        (fila+1, col+2), (fila+1, col-2),
        (fila-1, col+2), (fila-1, col-2)
    ]
    
    return {
        (f, c)
        for f, c in posibles
        if 0 <= f < 8 and 0 <= c < 8
    }


def movimientos_rey(pos):
    fila, col = pos
    movs = set()

    for f in range(fila-1, fila+2):
        for c in range(col-1, col+2):
            if (f, c) != pos and 0 <= f < 8 and 0 <= c < 8:
                movs.add((f, c))
    
    return movs


def movimientos_peon(pos, color="blanco"):
    fila, col = pos
    movs = set()

    if color == "blanco":
        if fila-1 >= 0:
            movs.add((fila-1, col))
    else:
        if fila+1 < 8:
            movs.add((fila+1, col))
    
    return movs


# =========================================
# 3. MOSTRAR TABLERO
# =========================================

def mostrar_tablero():
    tablero = [["." for _ in range(8)] for _ in range(8)]

    for f,c in torres_blancas: tablero[f][c] = "T"
    for f,c in caballos_blancos: tablero[f][c] = "C"
    for f,c in alfiles_blancos: tablero[f][c] = "A"
    for f,c in reina_blanca: tablero[f][c] = "Q"
    for f,c in rey_blanco: tablero[f][c] = "K"
    for f,c in peones_blancos: tablero[f][c] = "P"

    for f,c in torres_negras: tablero[f][c] = "t"
    for f,c in caballos_negros: tablero[f][c] = "c"
    for f,c in alfiles_negros: tablero[f][c] = "a"
    for f,c in reina_negra: tablero[f][c] = "q"
    for f,c in rey_negro: tablero[f][c] = "k"
    for f,c in peones_negros: tablero[f][c] = "p"

    for fila in tablero:
        print(" ".join(fila))


# =========================================
# 4. PRUEBAS
# =========================================

if __name__ == "__main__":
    
    print("♟️ TABLERO INICIAL:")
    mostrar_tablero()

    print("\nMovimientos torre en (7,0):")
    print(movimientos_torre((7,0)))

    print("\nMovimientos alfil en (7,2):")
    print(movimientos_alfil((7,2)))

    print("\nMovimientos caballo en (7,1):")
    print(movimientos_caballo((7,1)))

    print("\nMovimientos rey en (7,4):")
    print(movimientos_rey((7,4)))

    print("\nMovimientos peón blanco en (6,0):")
    print(movimientos_peon((6,0), "blanco"))
