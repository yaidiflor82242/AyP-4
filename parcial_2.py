import re

# 1. Regex
def validar_telefono(num):
    """
    Formato: 3001234567 (10 dígitos)
    """
    patron = r'^\d{10}$'
    return bool(re.match(patron, num))

def extraer_emails(texto):
    """
    Extraer correos de un texto
    """
    patron = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(patron, texto)

# 2. Lista enlazada
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.siguiente = None

class Inventario:
    def __init__(self):
        self.cabeza = None

    def agregar(self, nombre, precio):
        """Ordenado por precio (RECURSIVO)"""
        nuevo = Producto(nombre, precio)
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

    def total(self):
        """Suma de precios (RECURSIVO)"""
        return self._total_recursivo(self.cabeza)
    
    def _total_recursivo(self, actual):
        if actual is None:
            return 0
        return actual.precio + self._total_recursivo(actual.siguiente)

    def eliminar_caros(self, limite):
        """Eliminar > limite (RECURSIVO)"""
        self.cabeza = self._eliminar_caros_recursivo(self.cabeza, limite)
    
    def _eliminar_caros_recursivo(self, actual, limite):
        if actual is None:
            return None
        actual.siguiente = self._eliminar_caros_recursivo(actual.siguiente, limite)
        return None if actual.precio > limite else actual

# 3. Conjuntos
A = {1,2,3,4}
B = {3,4,5,6}
C = {4,5,6,7}

def en_exactamente_dos():
    """Elementos en exactamente 2 conjuntos"""
    ab = A & B - C
    ac = A & C - B
    bc = B & C - A
    return ab | ac | bc

def en_alguno():
    """Elementos en al menos uno"""
    return A | B | C

# 4. Recursividad
def fibonacci(n):
    """
    Fibonacci recursivo:
    F(0) = 0, F(1) = 1
    F(n) = F(n-1) + F(n-2)
    """
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Regex
print(validar_telefono("3001234567"))  # True
print(extraer_emails("Hola user@dominio.com y test@gmail.com"))  
# ['user@dominio.com', 'test@gmail.com']

# Inventario
inv = Inventario()
inv.agregar("Mouse", 20)
inv.agregar("Teclado", 50)
inv.agregar("Laptop", 1000)
print(inv.total())  # 1070

# Conjuntos
print(en_exactamente_dos())  # {3, 4}
print(en_alguno())          # {1, 2, 3, 4, 5, 6, 7}

# Fibonacci
print(fibonacci(6))  # 8
print(fibonacci(10)) # 55    