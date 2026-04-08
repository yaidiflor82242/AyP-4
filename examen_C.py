"""
═══════════════════════════════════════════════════════════════════════════════
                        PARCIAL 1 - ESTRUCTURAS DE DATOS
                                  EXAMEN C
                    Sistema de Cola de Atención al Cliente
═══════════════════════════════════════════════════════════════════════════════

CONTEXTO:
---------
Un banco necesita un sistema para gestionar la cola de clientes en espera.
Los clientes tienen diferentes tipos de atención (preferencial, normal) y
se debe poder atender, consultar y gestionar la cola.

INSTRUCCIONES:
--------------
1. Diseñar la clase Nodo (Cliente) con los atributos necesarios
2. Diseñar la clase Lista (Cola) con los métodos requeridos
3. Usar RECURSIVIDAD en los métodos donde se indique
4. No usar listas de Python [], solo tu estructura de nodos
5. Tiempo: 90 minutos
6. Calificación: 0.0 a 5.0

═══════════════════════════════════════════════════════════════════════════════
REQUERIMIENTOS DEL SISTEMA
═══════════════════════════════════════════════════════════════════════════════

PUNTO 1 (1.0): DISEÑO DE ESTRUCTURAS
------------------------------------
Diseña las clases necesarias:

a) Clase NODO (Cliente):
   - Debe almacenar: nombre, tipo de atención (preferencial/normal), 
     tiempo estimado de atención en minutos
   - Debe poder enlazarse con otro cliente

b) Clase LISTA (Cola):
   - Los clientes preferenciales van al INICIO
   - Los clientes normales van al FINAL


PUNTO 2 (1.0): AGREGAR CLIENTE - RECURSIVO
------------------------------------------
Implementa un método para agregar un cliente.
- Si es preferencial: insertar al inicio de los preferenciales
- Si es normal: insertar al final de la cola
- OBLIGATORIO usar recursividad para encontrar la posición


PUNTO 3 (1.0): TIEMPO DE ESPERA - RECURSIVO
-------------------------------------------
Implementa un método que calcule el tiempo de espera de un cliente
dado su nombre (suma de tiempos de todos los que están antes).
- OBLIGATORIO usar recursividad
- Retorna -1 si el cliente no está en la cola


PUNTO 4 (1.0): ATENDER SIGUIENTE
--------------------------------
Implementa un método que retire y retorne el primer cliente de la cola.
- Retorna None si la cola está vacía


PUNTO 5 (1.0): CONTAR POR TIPO - RECURSIVO
------------------------------------------
Implementa un método que cuente cuántos clientes hay de cada tipo.
- OBLIGATORIO usar recursividad
- Retorna una tupla (preferenciales, normales)

═══════════════════════════════════════════════════════════════════════════════
ESCRIBE TU CÓDIGO AQUÍ ABAJO
═══════════════════════════════════════════════════════════════════════════════
"""

# PUNTO 1a: Clase Nodo (Cliente)
class Cliente:
    def __init__(self, nombre, tipo, tiempo):
        self.nombre = nombre
        self.tipo = tipo  # "preferencial" o "normal"
        self.tiempo = tiempo
        self.siguiente = None

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - {self.tiempo} min"


# PUNTO 1b: Clase Lista (Cola)
class Cola:
    def __init__(self):
        self.cabeza = None
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual)
            actual = actual.siguiente
    def agregar(self, nombre, tipo, tiempo):
        nuevo = Cliente(nombre, tipo, tiempo)

        # Si la lista está vacía
        if self.cabeza is None:
            self.cabeza = nuevo
            return

        # Si es preferencial → insertar antes del primer normal
        if tipo == "preferencial":
            # Si el primero ya es normal
            if self.cabeza.tipo == "normal":
                nuevo.siguiente = self.cabeza
                self.cabeza = nuevo
                return
            
            def insertar_pref(nodo):
                if nodo.siguiente is None or nodo.siguiente.tipo == "normal":
                    nuevo.siguiente = nodo.siguiente
                    nodo.siguiente = nuevo
                    return
                insertar_pref(nodo.siguiente)
            
            insertar_pref(self.cabeza)

        # Si es normal → al final
        else:
            def insertar_final(nodo):
                if nodo.siguiente is None:
                    nodo.siguiente = nuevo
                    return
                insertar_final(nodo.siguiente)
            
            insertar_final(self.cabeza)
    def tiempo_espera(self, nombre):
        
        def calcular(nodo, acumulado):
            if nodo is None:
                return -1
            
            if nodo.nombre == nombre:
                return acumulado
            
            return calcular(nodo.siguiente, acumulado + nodo.tiempo)
        
        return calcular(self.cabeza, 0)
    def atender(self):
        if self.cabeza is None:
            return None
        
        atendido = self.cabeza
        self.cabeza = self.cabeza.siguiente
        return atendido
    def contar_por_tipo(self):
        
        def contar(nodo):
            if nodo is None:
                return (0, 0)
            
            pref, norm = contar(nodo.siguiente)
            
            if nodo.tipo == "preferencial":
                return (pref + 1, norm)
            else:
                return (pref, norm + 1)
        
        return contar(self.cabeza)


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA
# ═══════════════════════════════════════════════════════════════════════════════


if __name__ == "__main__":
    cola = Cola()
    
    # Agregar clientes
    cola.agregar("Juan", "normal", 10)
    cola.agregar("María", "preferencial", 5)
    cola.agregar("Pedro", "normal", 15)
    cola.agregar("Ana", "preferencial", 8)
    
    # Orden esperado: María, Ana, Juan, Pedro (preferenciales primero)
    cola.mostrar()
    
    # Tiempo de espera de Pedro: 5 + 8 + 10 = 23 minutos
    print("Espera de Pedro:", cola.tiempo_espera("Pedro"))
    
    # Contar por tipo: (2 preferenciales, 2 normales)
    print("Por tipo:", cola.contar_por_tipo())
    
    # Atender siguiente (María)
    atendido = cola.atender()
    print("Atendido:", atendido.nombre)

