import heapq
from datetime import datetime, timedelta
#timedelta calcular diferentes de tiempo
#datetime fecha+hora actual 

cola = []

try:
    n = int(input("¿Cuántas tareas va a ingresar?: "))
except ValueError:
    print("Número inválido, asumiendo 0 tareas.")
    n = 0

i = 0
contador=0
while i < n:

    tarea = input("Ingrese la tarea: ")

    cantidad = int(input("¿En cuántos días desea hacer la tarea?: "))

    # fecha actual
    hoy = datetime.now()

    # calcular fecha futura
    fecha = hoy + timedelta(days=cantidad)

    heapq.heappush(cola, (fecha, tarea))

    print("Tarea agregada:", tarea, "| Fecha programada:", fecha.date())
    contador+=1
    i += 1


print("\nOrden de tareas:")

while cola:

    fecha, tarea = heapq.heappop(cola)

    print(f"Próxima tarea: {tarea} (fecha: {fecha.date()})")
