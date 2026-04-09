import re
def validar_correo(correo):
    """
    Valida si un correo tiene formato correcto.

    Ejemplo válido:
    usuario@gmail.com

    Reglas:
    - letras, números, _ antes del @
    - dominio simple
    """
    patron = r'^[a-zA-Z0-9_]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron, correo))

def extraer_numeros(texto):
    """
    Extrae todos los números de un texto.

    Ejemplo:
    "Tengo 2 perros y 10 gatos" → ["2", "10"]
    """
    return re.findall(r'\d+', texto)

class Tarea:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad
        self.siguiente = None

class ListaTareas:
    def __init__(self):
        self.cabeza = None

    def agregar(self, nombre, prioridad):
        """
        Insertar al inicio si prioridad es alta,
        al final si es baja.
        (RECURSIVO)
        """
        if prioridad == "alta":
            nueva_tarea = Tarea(nombre, prioridad)
            nueva_tarea.siguiente = self.cabeza
            self.cabeza = nueva_tarea
        else:  # prioridad "baja"
            self._agregar_al_final_recursivo(self.cabeza, nombre, prioridad)
    
    def _agregar_al_final_recursivo(self, actual, nombre, prioridad):
        if actual is None:
            self.cabeza = Tarea(nombre, prioridad)
            return
        if actual.siguiente is None:
            actual.siguiente = Tarea(nombre, prioridad)
        else:
            self._agregar_al_final_recursivo(actual.siguiente, nombre, prioridad)

    def contar_altas(self):
        """
        Contar tareas con prioridad alta.
        (RECURSIVO)
        """
        return self._contar_altas_recursivo(self.cabeza)
    
    def _contar_altas_recursivo(self, actual):
        if actual is None:
            return 0
        return (1 if actual.prioridad == "alta" else 0) + \
               self._contar_altas_recursivo(actual.siguiente)

    def eliminar_bajas(self):
        """
        Eliminar tareas de prioridad baja.
        (RECURSIVO)
        """
        self.cabeza = self._eliminar_bajas_recursivo(self.cabeza)
    
    def _eliminar_bajas_recursivo(self, actual):
        if actual is None:
            return None
        
        actual.siguiente = self._eliminar_bajas_recursivo(actual.siguiente)
        return None if actual.prioridad == "baja" else actual

grupo1 = {"A", "B", "C", "D"}
grupo2 = {"C", "D", "E"}
grupo3 = {"D", "E", "F"}

def en_al_menos_dos():
    """Estudiantes en al menos 2 grupos"""
    return (grupo1 & grupo2) | (grupo1 & grupo3) | (grupo2 & grupo3)

def solo_en_grupo1():
    """Solo en grupo1"""
    return grupo1 - grupo2 - grupo3

def caminos(n):
    """
    Puedes avanzar 1, 2 o 3 pasos.
    ¿Cuántas formas hay?

    Ejemplo:
    n=3 → 4 formas
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    
    return caminos(n-1) + caminos(n-2) + caminos(n-3)

print(validar_correo("user_1@gmail.com"))  # True
print(extraer_numeros("Tengo 2 perros y 10 gatos"))  # ['2','10']

lista = ListaTareas()
lista.agregar("T1", "baja")
lista.agregar("T2", "alta")
lista.agregar("T3", "baja")

print("Altas:", lista.contar_altas())  # 1

lista.eliminar_bajas()

print(en_al_menos_dos())  # {'C','D','E'}
print(solo_en_grupo1())   # {'A','B'}

print(caminos(3))  # 4
