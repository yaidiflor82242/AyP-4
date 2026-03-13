
"""A={1,2,3}
B={} diccionario
B=set() # conjunto vacio"""
 #eliminar los duplicados de la lista
A=[5,6,4,5,3,4,5,6,3,2,5,6,4,6,5]
resultado=set(A)
print(resultado)

#cuantas personas en la red social, cuantos amigos en comun ordenados alfabeticamente
amigos_juan ={"Maria","Pedro","Ana","Carlos","Laura"}
amigos_maria ={"Pedro","Laura","Sofia","Diego","Ana","Juan"}

amigos_comunes = amigos_juan.intersection(amigos_maria)
amigos_total={len(amigos_juan.union(amigos_maria))}
print(f"Amigos en total: {amigos_total}")
print("Amigos en comun:" ,amigos_comunes)
print(f"Cantidad de amigos en comun: {len(amigos_comunes)}")
ordenados=sorted(amigos_comunes)
print(f"Amigos en comun ordenados alfabeticamente: {ordenados}")

#ejemplo profesor
print(f"EJEMPLO PROFESOR ","-"*20)
print(f"cantidad de personas en la red social: {len(amigos_juan.union(amigos_maria))}")
amigos_en_comun=sorted(amigos_juan.intersection(amigos_maria))
print("amigos en comun" ,amigos_en_comun)
print(f"Amigos que no son en comun: {amigos_juan^amigos_maria}")