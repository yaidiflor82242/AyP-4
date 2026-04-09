
import re

# 1. Regex
def validar_contraseña(pwd):
    """
    - mínimo 8 caracteres
    - al menos 1 número
    - al menos 1 mayúscula
    """
    patron = r'^(?=.*\d)(?=.*[A-Z])[a-zA-Z0-9@$!%*?&]{8,}$'
    return bool(re.match(patron, pwd))

def extraer_palabras_largas(texto):
    """
    palabras de más de 5 letras
    """
    palabras = re.findall(r'\b\w{6,}\b', texto)
    return palabras

# 2. Lista enlazada
class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        self.siguiente = None

class ListaEstudiantes:
    def __init__(self):
        self.cabeza = None

    def agregar(self, nombre, nota):
        """Ordenado por nota (RECURSIVO)"""
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
        """Promedio (RECURSIVO)"""
        total, count = self._promedio_recursivo(self.cabeza)
        return total / count if count > 0 else 0
    
    def _promedio_recursivo(self, actual):
        if actual is None:
            return 0, 0
        total_siguiente, count_siguiente = self._promedio_recursivo(actual.siguiente)
        return actual.nota + total_siguiente, 1 + count_siguiente

    def eliminar_reprobados(self):
        """nota < 3.0 (RECURSIVO)"""
        self.cabeza = self._eliminar_reprobados_recursivo(self.cabeza)
    
    def _eliminar_reprobados_recursivo(self, actual):
        if actual is None:
            return None
        actual.siguiente = self._eliminar_reprobados_recursivo(actual.siguiente)
        return None if actual.nota < 3.0 else actual

# 3. Conjuntos
X = {"Ana","Luis","Pedro"}
Y = {"Luis","Pedro","Juan"}
Z = {"Pedro","Juan","Maria"}

def solo_en_uno():
    """Elementos que están en exactamente 1 conjunto"""
    solo_x = X - Y - Z
    solo_y = Y - X - Z
    solo_z = Z - X - Y
    return solo_x | solo_y | solo_z

def en_todos():
    """Elementos en los 3 conjuntos"""
    return X & Y & Z

# 4. Recursividad
def formas_sumar(n):
    """
    sumar con 1 y 2 (igual escalones)
    Ej: formas_sumar(3) = 3 formas: [1,1,1], [1,2], [2,1]
    """
    if n == 0:
        return 1
    if n < 0:
        return 0
    
    # Usar 1 + resto
    con_uno = formas_sumar(n - 1)
    # Usar 2 + resto  
    con_dos = formas_sumar(n - 2)
    
    return con_uno + con_dos

# Regex
print(validar_contraseña("Pass123A"))  # True
print(extraer_palabras_largas("Hola mundo extraordinariamente"))  
# ['mundo', 'extraordinariamente']

# Estudiantes
lista = ListaEstudiantes()
lista.agregar("Ana", 4.5)
lista.agregar("Luis", 2.8)
lista.agregar("Pedro", 4.0)
print(lista.promedio())  # 3.766...

# Conjuntos
print(solo_en_uno())  # {'Ana', 'Juan', 'Maria'}
print(en_todos())     # {'Pedro'}

# Formas sumar
print(formas_sumar(3))  # 3
print(formas_sumar(4))  # 5