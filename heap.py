datos=[5,3,8,1,2,9,4]
#para utilizawr heap hay que importar la libreria
import heapq
heapq.heapify(datos)
print("Heap:", datos)
heapq.heappush(datos, 6)
print("Después de agregar 6:", datos)
minimo=heapq.heappop(datos)
print("Elemento mínimo extraído:", minimo)
print("Heap después de extraer el mínimo:", datos)
datos2=[(2, 'A'), (1, 'B'), (3, 'C'),(2, 'B')]
heapq.heapify(datos2)
print("Heap 2con tuplas:", datos2)

minimo=heapq.heappushpop(datos,7)
print("Después de agregar 7 y extraer el mínimo:", minimo)
print("Heap después de pushpop:", datos)