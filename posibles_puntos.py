# 1. CAMINOS CON RESTRICCIONES
def caminos_restringidos(n):
    """
    Puedes subir 1 o 2 escalones,
    pero NO puedes dar dos pasos de 2 seguidos.
    
    DP: dp[i][0] = formas terminando en 1
         dp[i][1] = formas terminando en 2
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1  # [1]
    
    # dp[i][0]: formas para i escalones terminando en 1
    # dp[i][1]: formas para i escalones terminando en 2  
    dp = [[0, 0] for _ in range(n + 1)]
    dp[1][0] = 1  # [1]
    
    for i in range(2, n + 1):
        # Terminar en 1: desde cualquier posición anterior
        dp[i][0] = dp[i-1][0] + dp[i-1][1]
        # Terminar en 2: SOLO desde posición que terminó en 1
        if i >= 2:
            dp[i][1] = dp[i-2][0]
    
    return dp[n][0] + dp[n][1]

# 2. SUMAS DE NÚMEROS
def formas_sumar(n):
    """
    ¿De cuántas formas puedes sumar n usando 1, 2 y 3?
    Orden no importa: [1,2] == [2,1]
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    
    return formas_sumar(n-1) + formas_sumar(n-2) + formas_sumar(n-3)

# 3. SUBCONJUNTOS (MUY IMPORTANTE)
def subconjuntos(lista):
    """
    Retorna todos los subconjuntos de una lista
    [1,2] → [[], [1], [2], [1,2]]
    """
    if not lista:
        return [[]]
    
    sub_sin_primero = subconjuntos(lista[1:])
    sub_con_primero = [[lista[0]] + sub for sub in sub_sin_primero]
    
    return sub_sin_primero + sub_con_primero

# 4. PERMUTACIONES
def permutaciones(lista):
    """
    Retorna todas las permutaciones posibles
    [1,2] → [[1,2], [2,1]]
    """
    if len(lista) <= 1:
        return [lista[:]]
    
    resultado = []
    primer = lista[0]
    resto_perms = permutaciones(lista[1:])
    
    for perm in resto_perms:
        for i in range(len(perm) + 1):
            nueva_perm = perm[:i] + [primer] + perm[i:]
            resultado.append(nueva_perm)
    
    return resultado

# 5. TORRE DE HANOI
def hanoi(n, origen, auxiliar, destino):
    """
    Resolver torre de Hanoi
    """
    if n == 1:
        print(f"Mover disco 1 de {origen} → {destino}")
        return
    
    # Mover n-1 de origen → auxiliar
    hanoi(n-1, origen, destino, auxiliar)
    # Mover disco n de origen → destino
    print(f"Mover disco {n} de {origen} → {destino}")
    # Mover n-1 de auxiliar → destino
    hanoi(n-1, auxiliar, origen, destino)

# 6. BÚSQUEDA EN LISTA ENLAZADA
def buscar(nodo, valor):
    """
    Buscar un valor recursivamente
    Retorna el VALOR si lo encuentra, None si no
    """
    if nodo is None:
        return None
    if nodo.valor == valor:
        return nodo.valor  # Retorna el VALOR directamente
    return buscar(nodo.siguiente, valor)

# 7. CONTAR ELEMENTOS
def contar_pares(lista):
    """
    Contar números pares recursivamente
    """
    if not lista:
        return 0
    return (1 if lista[0] % 2 == 0 else 0) + contar_pares(lista[1:])

# 8. SUMA DE DÍGITOS
def suma_digitos(n):
    """
    Ej: 123 → 6
    """
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

# 9. PALÍNDROMO
def es_palindromo(texto):
    """
    Verificar si una palabra es palíndromo
    Ignora mayúsculas/minúsculas y espacios
    """
    texto = texto.lower().replace(" ", "")
    def helper(izq, der):
        if izq >= der:
            return True
        if texto[izq] != texto[der]:
            return False
        return helper(izq + 1, der - 1)
    return helper(0, len(texto) - 1)

# 10. LABERINTO (TOP NIVEL 💀)
def hay_camino(matriz, i, j):
    """
    Encontrar camino en matriz 0/1
    0 = camino libre, 1 = pared
    Desde (0,0) hasta (filas-1, cols-1)
    NO pasar por celdas visitadas
    """
    if not matriz or not matriz[0]:
        return False
    
    filas, cols = len(matriz), len(matriz[0])
    
    def dfs(x, y, visitados):
        # Fuera de límites o pared o ya visitado
        if (x < 0 or x >= filas or y < 0 or y >= cols or 
            matriz[x][y] == 1 or (x, y) in visitados):
            return False
        
        # Llegamos al final
        if x == filas - 1 and y == cols - 1:
            return True
        
        visitados.add((x, y))
        
        # 4 direcciones: abajo, derecha, arriba, izquierda
        direcciones = [(1,0), (0,1), (-1,0), (0,-1)]
        
        for dx, dy in direcciones:
            if dfs(x + dx, y + dy, visitados):
                return True
        
        visitados.remove((x, y))  # backtracking
        return False
    
    return dfs(0, 0, set())

# CLASE NODO para la búsqueda (auxiliar)
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# 11. COMBINACIONES
def combinaciones(n, k):
    """
    Elegir k elementos de n (C(n,k))
    """
    if k > n or k < 0:
        return 0
    if k == 0 or k == n:
        return 1
    return combinaciones(n-1, k-1) + combinaciones(n-1, k)

# 12. MÁXIMO EN LISTA
def maximo(lista):
    """
    Encontrar el mayor valor (recursivo)
    """
    if len(lista) == 1:
        return lista[0]
    return max(lista[0], maximo(lista[1:]))

# 13. COLOREAR GRAFOS
def colorear(nodos, colores):
    """
    Asignar colores sin que vecinos repitan
    nodos: lista de listas (grafo adyacencia)
    """
    colores_asignados = {}
    
    def es_seguro(nodo, color):
        for vecino in nodos[nodo]:
            if vecino in colores_asignados and colores_asignados[vecino] == color:
                return False
        return True
    
    def colorear_recursivo(nodo_actual):
        if nodo_actual == len(nodos):
            return True
        
        for color in range(colores):
            if es_seguro(nodo_actual, color):
                colores_asignados[nodo_actual] = color
                if colorear_recursivo(nodo_actual + 1):
                    return True
                del colores_asignados[nodo_actual]
        return False
    
    return colorear_recursivo(0), colores_asignados

# 14. N-REINAS (TOP 💀💀)
def n_reinas(n):
    """
    Colocar N reinas sin atacarse
    Retorna una solución válida
    """
    tablero = [[0]*n for _ in range(n)]
    
    def es_seguro(fila, col):
        # Verificar columna
        for i in range(fila):
            if tablero[i][col] == 1:
                return False
        # Diagonal superior izquierda
        for i, j in zip(range(fila-1, -1, -1), range(col-1, -1, -1)):
            if tablero[i][j] == 1:
                return False
        # Diagonal superior derecha  
        for i, j in zip(range(fila-1, -1, -1), range(col+1, n)):
            if tablero[i][j] == 1:
                return False
        return True
    
    def resolver(fila):
        if fila == n:
            return True
        for col in range(n):
            if es_seguro(fila, col):
                tablero[fila][col] = 1
                if resolver(fila + 1):
                    return True
                tablero[fila][col] = 0
        return False
    
    resolver(0)
    return tablero

# 15. CAMBIO DE MONEDAS
def cambio(monedas, total):
    """
    Formas de dar cambio (mínimo número de monedas)
    """
    if total == 0:
        return 0
    if not monedas or total < 0:
        return float('inf')
    
    # Incluir esta moneda
    incluir = 1 + cambio(monedas, total - monedas[0])
    # Excluir esta moneda
    excluir = cambio(monedas[1:], total)
    
    return min(incluir, excluir)

# 16. BACKTRACKING DE LABERINTO
def resolver_laberinto(matriz, i, j):
    """
    Encontrar camino desde (i,j) a salida
    Modifica matriz con 'X' para marcar camino
    """
    filas, cols = len(matriz), len(matriz[0])
    
    def dfs(x, y):
        # Condiciones de salida
        if (x < 0 or x >= filas or y < 0 or y >= cols or 
            matriz[x][y] != 0):
            return False
        
        # Llegamos a la salida (esquina inferior derecha)
        if x == filas-1 and y == cols-1:
            matriz[x][y] = 2  # Salida
            return True
        
        # Marcar como visitado
        matriz[x][y] = 1
        
        # 4 direcciones
        if (dfs(x+1, y) or dfs(x, y+1) or 
            dfs(x-1, y) or dfs(x, y-1)):
            matriz[x][y] = 2  # Camino válido
            return True
        
        matriz[x][y] = 3  # Camino muerto
        return False
    
    return dfs(i, j)

# 17. GENERAR CADENAS
def generar_binarios(n):
    """
    Cadenas de 0 y 1 de longitud n
    """
    if n == 0:
        return [""]
    
    anteriores = generar_binarios(n-1)
    return ["0" + s for s in anteriores] + ["1" + s for s in anteriores]

# 18. EXPRESIONES MATEMÁTICAS
def evaluar_expresion(exp):
    """
    Resolver expresiones simples: "2+3*4" → 14
    Prioridad: * / antes de + -
    """
    def aplicar_operador(a, b, op):
        if op == '+': return a + b
        if op == '-': return a - b
        if op == '*': return a * b
        if op == '/': return a / b
    
    def precedence(op):
        if op in '*/': return 2
        if op in '+-': return 1
        return 0
    
    def resolver(expresion, inicio, fin):
        if inicio > fin:
            return 0
        
        # Número
        if expresion[inicio].isdigit():
            num = 0
            while inicio <= fin and expresion[inicio].isdigit():
                num = num * 10 + int(expresion[inicio])
                inicio += 1
            return num, inicio
        
        # Paréntesis
        if expresion[inicio] == '(':
            resultado, inicio = resolver(expresion, inicio+1, fin-1)
            return resultado, inicio + 1
        
        return 0, inicio
    
    # Shunting-yard simplificado (versión básica)
    valores = []
    operadores = []
    
    i = 0
    while i < len(exp):
        if exp[i].isdigit():
            num = 0
            while i < len(exp) and exp[i].isdigit():
                num = num * 10 + int(exp[i])
                i += 1
            valores.append(num)
        elif exp[i] in '+-*/':
            while (operadores and 
                   precedence(operadores[-1]) >= precedence(exp[i])):
                op2 = valores.pop()
                op1 = valores.pop()
                op = operadores.pop()
                valores.append(aplicar_operador(op1, op2, op))
            operadores.append(exp[i])
            i += 1
        else:
            i += 1
    
    while operadores:
        op2 = valores.pop()
        op1 = valores.pop()
        op = operadores.pop()
        valores.append(aplicar_operador(op1, op2, op))
    
    return valores[0]

# 19. ÁRBOLES (MUY IMPORTANTE)
class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def recorrer_arbol(nodo):
    """
    Retorna (preorden, inorden, postorden)
    """
    if nodo is None:
        return [], [], []
    
    pre = [nodo.valor] + recorrer_arbol(nodo.izquierda)[0]
    pre += recorrer_arbol(nodo.derecha)[0]
    
    izq_in, der_in = recorrer_arbol(nodo.izquierda)[1], recorrer_arbol(nodo.derecha)[1]
    inorden = izq_in + [nodo.valor] + der_in
    
    izq_post, der_post = recorrer_arbol(nodo.izquierda)[2], recorrer_arbol(nodo.derecha)[2]
    post = izq_post + der_post + [nodo.valor]
    
    return pre, inorden, post

#EJEMPLOS DE USO 
print("=== METODO 1: CAMINOS RESTRINGIDOS ===")
# 1. Caminos restringidos
print(caminos_restringidos(3))  # 3: [1,1,1], [1,2], [2,1]
print(caminos_restringidos(4))  # 5

print("=== METODO 2: FORMAS SUMAR ===")
# 2. Formas sumar
print(formas_sumar(4))  # 7 formas

print("=== METODO 3: SUBCONJUNTOS ===")
# 3. Subconjuntos
print(subconjuntos([1,2]))
# [[], [1], [2], [1, 2]]

print("=== METODO 4: PERMUTACIONES ===")
# 4. Permutaciones  
print(len(permutaciones([1,2,3])))  # 6
print(permutaciones(['A','B']))
# [['A', 'B'], ['B', 'A']]

print("=== METODO 5: TORRE DE HANOI ===")
# 5. Hanoi
print("Torre de Hanoi con 2 discos:")
hanoi(2, 'A', 'B', 'C')
# Mover disco 1 de A → B
# Mover disco 2 de A → C  
# Mover disco 1 de B → C

print("=== METODO 6: BUSQUEDA EN LISTA ENLAZADA ===")
# 6. Búsqueda en lista enlazada
nodo1 = Nodo(10)
nodo2 = Nodo(20) 
nodo3 = Nodo(30)
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

print(buscar(nodo1, 20))  # 20
print(buscar(nodo1, 25))  # None
print(buscar(nodo1, 30))  # 30

print("=== METODO 7: CONTAR PARES ===")
# 7. Contar pares
print(contar_pares([1,2,3,4,5,6]))  # 3

print("=== METODO 8: SUMA DE DIGITOS ===")
# 8. Suma dígitos
print(suma_digitos(12345))  # 15

print("=== METODO 9: PALINDROMO ===")
# 9. Palíndromo
print(es_palindromo("Ana"))      # True
print(es_palindromo("racecar"))  # True
print(es_palindromo("Hola"))     # False

print("=== METODO 10: LABERINTO ===")
# 10. Laberinto
laberinto = [
    [0,0,0,0],
    [1,1,0,1], 
    [0,0,0,0],
    [0,1,1,0]
]
print(hay_camino(laberinto, 0, 0))  # True

print("=== METODO 11: COMBINACIONES ===")
# 11. Combinaciones
print(combinaciones(5, 2))  # 10

print("=== METODO 12: MAXIMO EN LISTA ===")
# 12. Máximo
print(maximo([3, 1, 4, 1, 5]))  # 5

print("=== METODO 13: COLOREAR GRAFO ===")
# 13. Colorear grafo
grafo = [[1], [0,2], [1]]  # triángulo
exito, colores = colorear(grafo, 3)
print(exito, colores)  # True {0: 0, 1: 1, 2: 2}

print("=== METODO 14: N-REINAS ===")
# 14. N-Reinas
print(n_reinas(4))  

print("=== METODO 15: CAMBIO DE MONEDAS ===")
# 15. Cambio monedas
print(cambio([1,5,10,25], 36))  # 3 monedas

print("=== METODO 16: GENERAR BINARIOS ===")
# 16. Binarios
print(generar_binarios(2))  # ['00','01','10','11']

print("=== METODO 17: RECORRER ARBOL ===")
# 17. Árbol
arbol = NodoArbol(1)
arbol.izquierda = NodoArbol(2)
arbol.derecha = NodoArbol(3)
print(recorrer_arbol(arbol))  # ([1,2,3], [2,1,3], [2,3,1])

print("=== METODO 18: EVALUAR EXPRESIONES ===")
# Ejemplos de prueba
print(evaluar_expresion("2+3*4"))     # 14 (3*4=12 +2=14)
print(evaluar_expresion("10-2*3"))    # 4 (2*3=6, 10-6=4)
print(evaluar_expresion("5+4/2"))     # 7 (4/2=2, 5+2=7)
print(evaluar_expresion("2*3+4"))     # 10 (2*3=6 +4=10)

print("=== METODO 19: RECORRER ARBOL DE EJEMPLO ===")
# Crear árbol de ejemplo:
#       1
#      / \
#     2   3
#    / \   \
#   4   5   6

raiz = NodoArbol(1)
raiz.izquierda = NodoArbol(2)
raiz.derecha = NodoArbol(3)
raiz.izquierda.izquierda = NodoArbol(4)
raiz.izquierda.derecha = NodoArbol(5)
raiz.derecha.derecha = NodoArbol(6)

pre, ino, post = recorrer_arbol(raiz)
print("Preorden: ", pre)   # [1, 2, 4, 5, 3, 6]
print("Inorden:  ", ino)   # [4, 2, 5, 1, 3, 6]
print("Postorden:", post)  # [4, 5, 2, 6, 3, 1]

print("=== EVALUADOR DE EXPRESIONES ===")
tests = ["2+3*4", "10-2*3", "5+4/2", "2*3+4"]
for test in tests:
    print(f"{test} = {evaluar_expresion(test)}")

print("\n=== RECORRIDO DE ÁRBOL ===")

# 2. Árbol
raiz = NodoArbol(1)
raiz.izquierda = NodoArbol(2)
raiz.derecha = NodoArbol(3)
raiz.izquierda.izquierda = NodoArbol(4)
raiz.izquierda.derecha = NodoArbol(5)
raiz.derecha.derecha = NodoArbol(6)

pre, ino, post = recorrer_arbol(raiz)
print(f"Preorden:  {pre}")
print(f"Inorden:   {ino}")
print(f"Postorden: {post}")