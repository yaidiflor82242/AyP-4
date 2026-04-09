# ================================
# PARCIALES DE PRÁCTICA - PYTHON
# Algoritmos y Programación
# ================================

# ========== VARIANTE 1=========
import re

# ===== 1. REGEX =====
def validar_placa_moto(placa):
    """
    Formato:
    - 3 letras + 2 números + 1 letra
    Ej: ABC12D
    No se permiten minúsculas.
    """
    patron = r'^[A-Z]{3}\d{2}[A-Z]$'
    return bool(re.match(patron, placa))

def extraer_menciones(texto):
    """
    Extraer menciones tipo @usuario
    Ej: "@juan hola @maria" → ["@juan", "@maria"]
    """
    return re.findall(r'@\w+', texto)

# ===== 2. LISTA ENLAZADA =====
class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.siguiente = None

class Inventario:
    def __init__(self):
        self.cabeza = None

    def agregar(self, nombre, precio, stock):
        """
        Insertar ORDENADO por precio (menor a mayor)
        (RECURSIVO)
        """
        nuevo = Producto(nombre, precio, stock)
        if self.cabeza is None or precio <= self.cabeza.precio:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
        else:
            self._agregar_recursivo(self.cabeza, nuevo)
    
    def _agregar_recursivo(self, actual, nuevo):
        if actual.siguiente is None or nuevo.precio <= actual.siguiente.precio:
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
        else:
            self._agregar_recursivo(actual.siguiente, nuevo)

    def valor_total(self):
        """
        precio * stock (RECURSIVO)
        """
        return self._valor_total_recursivo(self.cabeza)
    
    def _valor_total_recursivo(self, actual):
        if actual is None:
            return 0
        return (actual.precio * actual.stock) + self._valor_total_recursivo(actual.siguiente)

    def eliminar_sin_stock(self):
        """
        Eliminar productos con stock = 0 (RECURSIVO)
        """
        self.cabeza = self._eliminar_sin_stock_recursivo(self.cabeza)
    
    def _eliminar_sin_stock_recursivo(self, actual):
        if actual is None:
            return None
        
        actual.siguiente = self._eliminar_sin_stock_recursivo(actual.siguiente)
        return None if actual.stock == 0 else actual

# ===== 3. CONJUNTOS =====
A = {"Ana","Luis","Pedro"}
B = {"Luis","Pedro","Carlos"}
C = {"Pedro","Carlos","Maria"}

def en_al_menos_dos():
    """En al menos 2 grupos"""
    return (A & B) | (A & C) | (B & C)

def en_solo_uno():
    """Solo en exactamente 1 grupo"""
    solo_a = A - B - C
    solo_b = B - A - C
    solo_c = C - A - B
    return solo_a | solo_b | solo_c

# ===== 4. CAMINOS =====
def caminos(n):
    """
    Puedes subir 1, 2 o 3 escalones.
    ¿Cuántas formas hay?
    n=3 → 4 formas: [1,1,1], [1,2], [2,1], [3]
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    return caminos(n-1) + caminos(n-2) + caminos(n-3)

# ===== REGEX =====
print("=== REGEX ===")
print(validar_placa_moto("ABC12D"))     # True
print(validar_placa_moto("abc12d"))     # False
print(validar_placa_moto("AB12D"))      # False
print(extraer_menciones("@juan hola @maria"))  # ['@juan', '@maria']

# ===== INVENTARIO =====
print("\n=== INVENTARIO ===")
inv = Inventario()
inv.agregar("Lápiz", 1000, 50)
inv.agregar("Cuaderno", 5000, 20)
inv.agregar("Borrador", 2000, 0)
print(f"Valor total: ${inv.valor_total()}")  # 150000

inv.eliminar_sin_stock()
print("Después de eliminar sin stock - OK")

# ===== CONJUNTOS =====
print("\n=== CONJUNTOS ===")
print("En al menos 2:", en_al_menos_dos())     # {'Luis', 'Pedro', 'Carlos'}
print("Solo en uno:", en_solo_uno())           # {'Ana', 'Maria'}

# ===== CAMINOS =====
print("\n=== CAMINOS ===")
print(caminos(0))  # 1
print(caminos(1))  # 1
print(caminos(2))  # 2
print(caminos(3))  # 4
print(caminos(4))  # 7


# ===== VARIANTE 2 =====

import re

# 1. REGEX
def validar_password(pwd):
    """
    - mínimo 8 caracteres
    - al menos 1 número
    - al menos 1 mayúscula
    """
    patron = r'^(?=.*\d)(?=.*[A-Z])[a-zA-Z0-9@$!%*?&]{8,}$'
    return bool(re.match(patron, pwd))

def extraer_palabras_mayus(texto):
    """
    Extraer palabras que empiecen en mayúscula
    """
    return re.findall(r'\b[A-Z]\w*', texto)

# 2. LISTA ENLAZADA
class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        self.siguiente = None

class Lista:
    def __init__(self):
        self.cabeza = None

    def agregar(self, nombre, nota):
        """
        Ordenado de MAYOR a MENOR nota (RECURSIVO)
        """
        nuevo = Estudiante(nombre, nota)
        if self.cabeza is None or nota >= self.cabeza.nota:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
        else:
            self._agregar_recursivo(self.cabeza, nuevo)
    
    def _agregar_recursivo(self, actual, nuevo):
        if actual.siguiente is None or nuevo.nota >= actual.siguiente.nota:
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
        else:
            self._agregar_recursivo(actual.siguiente, nuevo)

    def promedio(self):
        """
        Calcular promedio (RECURSIVO)
        """
        total, count = self._promedio_recursivo(self.cabeza)
        return total / count if count > 0 else 0
    
    def _promedio_recursivo(self, actual):
        if actual is None:
            return 0, 0
        total_siguiente, count_siguiente = self._promedio_recursivo(actual.siguiente)
        return actual.nota + total_siguiente, 1 + count_siguiente

    def eliminar_reprobados(self):
        """
        nota < 3.0 (RECURSIVO)
        """
        self.cabeza = self._eliminar_reprobados_recursivo(self.cabeza)
    
    def _eliminar_reprobados_recursivo(self, actual):
        if actual is None:
            return None
        actual.siguiente = self._eliminar_reprobados_recursivo(actual.siguiente)
        return None if actual.nota < 3.0 else actual

# 3. CONJUNTOS
X = {1,2,3,4}
Y = {3,4,5,6}
Z = {4,5,6,7}

def exactamente_dos():
    """Elementos en exactamente 2 conjuntos"""
    xy = (X & Y) - Z
    xz = (X & Z) - Y
    yz = (Y & Z) - X
    return xy | xz | yz

def en_todos():
    """Elementos en los 3 conjuntos"""
    return X & Y & Z

# 4. SUMA DE COMBINACIONES (SUBSET SUM)
def suma_combinaciones(lista, objetivo):
    """
    Retorna cuántas combinaciones suman el objetivo.
    """
    def helper(indice, suma_actual):
        if indice == len(lista):
            return 1 if suma_actual == objetivo else 0
        
        # No incluir este elemento
        total = helper(indice + 1, suma_actual)
        # Incluir este elemento
        if suma_actual + lista[indice] <= objetivo:
            total += helper(indice + 1, suma_actual + lista[indice])
        
        return total
    
    return helper(0, 0)

# ===== 1. REGEX =====
print("=== REGEX ===")
print(validar_password("Pass123A"))  # True
print(validar_password("pass123a"))  # False
print(extraer_palabras_mayus("Hola Mundo Python Ejemplo"))  # ['Hola', 'Mundo', 'Python', 'Ejemplo']

# ===== 2. LISTA ESTUDIANTES =====
print("\n=== LISTA ESTUDIANTES ===")
lista = Lista()
lista.agregar("Ana", 4.5)
lista.agregar("Luis", 2.8)
lista.agregar("Pedro", 4.0)
lista.agregar("Maria", 3.5)

print(f"Promedio inicial: {lista.promedio():.2f}")  # 3.70

lista.eliminar_reprobados()
print(f"Promedio sin reprobados: {lista.promedio():.2f}")  # 4.00

# ===== 3. CONJUNTOS =====
print("\n=== CONJUNTOS ===")
print("Exactamente 2:", exactamente_dos())  # {4}
print("En todos:", en_todos())              # {4, 5, 6}? Wait no: {4}

# ===== 4. SUMA COMBINACIONES =====
print("\n=== SUMA COMBINACIONES ===")
print(suma_combinaciones([1,2,3], 3))   # 2: [3], [1,2]
print(suma_combinaciones([2,4,6], 8))   # 1: [2,6]
print(suma_combinaciones([1,2,3,4], 5)) # 2: [1,4], [2,3]

# ===== VARIANTE 3 =====

import re

# 1. REGEX
def validar_url(url):
    """
    Validar:
    http:// o https://
    dominio.com
    """
    patron = r'^https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron, url))

def extraer_numeros_grandes(texto):
    """
    Extraer números de 3 o más dígitos
    """
    return re.findall(r'\b\d{3,}\b', texto)

# 2. LISTA ENLAZADA
class Pedido:
    def __init__(self, cliente, valor):
        self.cliente = cliente
        self.valor = valor
        self.siguiente = None

class ListaPedidos:
    def __init__(self):
        self.cabeza = None

    def agregar(self, cliente, valor):
        """
        Insertar al FINAL (RECURSIVO)
        """
        if self.cabeza is None:
            self.cabeza = Pedido(cliente, valor)
        else:
            self._agregar_al_final_recursivo(self.cabeza, cliente, valor)
    
    def _agregar_al_final_recursivo(self, actual, cliente, valor):
        if actual.siguiente is None:
            actual.siguiente = Pedido(cliente, valor)
        else:
            self._agregar_al_final_recursivo(actual.siguiente, cliente, valor)

    def mayor_pedido(self):
        """
        Retorna el pedido con mayor valor (RECURSIVO)
        """
        return self._mayor_recursivo(self.cabeza)
    
    def _mayor_recursivo(self, actual):
        if actual is None:
            return None
        if actual.siguiente is None:
            return actual
        
        mayor_siguiente = self._mayor_recursivo(actual.siguiente)
        if actual.valor >= mayor_siguiente.valor:
            return actual
        return mayor_siguiente

    def eliminar_menores(self, limite):
        """
        Eliminar pedidos < limite (RECURSIVO)
        """
        self.cabeza = self._eliminar_menores_recursivo(self.cabeza, limite)
    
    def _eliminar_menores_recursivo(self, actual, limite):
        if actual is None:
            return None
        
        actual.siguiente = self._eliminar_menores_recursivo(actual.siguiente, limite)
        return None if actual.valor < limite else actual

# 3. CONJUNTOS
A = {"A","B","C"}
B = {"B","C","D"}
C = {"C","D","E"}

def exactamente_uno():
    """Elementos en exactamente 1 conjunto"""
    solo_a = A - B - C
    solo_b = B - A - C
    solo_c = C - A - B
    return solo_a | solo_b | solo_c

def al_menos_dos():
    """Elementos en al menos 2 conjuntos"""
    return (A & B) | (A & C) | (B & C)

# 4. SUBCONJUNTOS
def subconjuntos(lista):
    """
    Retornar TODOS los subconjuntos
    [1,2] → [[], [1], [2], [1,2]]
    """
    if not lista:
        return [[]]
    
    sin_primero = subconjuntos(lista[1:])
    con_primero = [[lista[0]] + sub for sub in sin_primero]
    
    return sin_primero + con_primero

    # ===== 1. REGEX =====
print("=== REGEX ===")
print(validar_url("http://google.com"))   # True
print(validar_url("https://ejemplo.com")) # True
print(validar_url("ftp://test.com"))      # False
print(extraer_numeros_grandes("123 45 6789 abc 1234"))  # ['123', '6789', '1234']

# ===== 2. LISTA PEDIDOS =====
print("\n=== LISTA PEDIDOS ===")
pedidos = ListaPedidos()
pedidos.agregar("Ana", 1000)
pedidos.agregar("Luis", 5000)
pedidos.agregar("Pedro", 3000)
pedidos.agregar("Maria", 7000)

mayor = pedidos.mayor_pedido()
print(f"Mayor pedido: {mayor.cliente} - ${mayor.valor}")

pedidos.eliminar_menores(4000)
print("Después de eliminar menores a $4000 - OK")

# ===== 3. CONJUNTOS =====
print("\n=== CONJUNTOS ===")
print("Exactamente 1:", exactamente_uno())  # {'A', 'E'}
print("Al menos 2:", al_menos_dos())       # {'B', 'C', 'D'}

# ===== 4. SUBCONJUNTOS =====
print("\n=== SUBCONJUNTOS ===")
print("Subconjuntos [1,2]:", subconjuntos([1,2]))
# [[], [1], [2], [1, 2]]
print("Cantidad:", len(subconjuntos([1,2,3])))  # 8