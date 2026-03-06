"""#programa cada paciente tiene una prioridad de 1 a 3 donde 1 es mas importante en nel hospital deben saber quein es el sigueinte en atender con su nombre y prioridad
import heapq

class Paciente:
    def __init__(self, nombre, prioridad):
        # prioridad: 1 (más urgente) a 3 (menos urgente)
        self.nombre = nombre
        self.prioridad = prioridad

    def __lt__(self, other):
        # heapq utiliza el operador < para ordenar la cola de prioridad
        return self.prioridad < other.prioridad

    def __str__(self):
        return f"{self.nombre} (prioridad {self.prioridad})"


# ejemplo de uso
if __name__ == "__main__":
    # crear una lista vacía y utilizar heapq como cola de prioridad
    cola = []

    # añadir algunos pacientes
    pacientes = [
        Paciente("Ana", 2),
        Paciente("Luis", 1),
        Paciente("María", 3),
        Paciente("Carlos", 1),
    ]

    for p in pacientes:
        heapq.heappush(cola, p)
        print(f"Ingresó a la cola: {p}")

    print("\nOrden de atención:")
    # sacar de la cola en orden de prioridad y mostrar
    while cola:
        siguiente = heapq.heappop(cola)
        print(f"Atendiendo a: {siguiente}")

    # también se puede leer desde la entrada estándar:
    # nombre = input('Nombre: ')
    # prioridad = int(input('Prioridad (1-3): '))
    # heapq.heappush(cola, Paciente(nombre, prioridad))"""

import heapq

# cola de prioridad
cola = []

# cantidad de pacientes
n = int(input("¿Cuántos pacientes va a ingresar?: "))

# ingresar pacientes
for i in range(n):

    nombre = input("Nombre del paciente: ")
    prioridad = int(input("Prioridad (1-3): "))

    # se guarda como tupla (prioridad, nombre)
    heapq.heappush(cola, (prioridad, nombre))

    print("Paciente agregado:", (prioridad, nombre))


print("\nOrden de atención:")

# atender pacientes según prioridad
while cola:

    prioridad, nombre = heapq.heappop(cola)

    print("Atendiendo a:", nombre, "| Prioridad:", prioridad)
