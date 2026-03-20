import conjuntos_listas_ligadas #importamos el modulo de conjuntos para usar la clase Conjunto que hemos creado en el ejercicio anterior
from conjuntos_listas_ligadas import Conjunto

"""1.cuales son las canciones que ambos escuchan"""

canciones_juan = {
    "Despacito",
    "Shape of You",
    "Blinding Lights",
    "Uptown Funk",
    "Havana",
}
canciones_maria = {
    "Blinding Lights",
    "Uptown Funk",
    "Can't Stop the Feeling",
    "Shut Up and Dance",
    "Happy",
}

canciones_comunes = canciones_juan.intersection(canciones_maria)
print("Canciones que ambos escuchan:", canciones_comunes)


def interseccion(canciones_juan, canciones_maria):
    resultado = set()  # conjunto nuevo vacio
    for cancion in canciones_juan:  # recorrer el primer conjunto
        if (
            cancion in canciones_maria
        ):  # si la cancion del primer conjunto pertenece al otro conjunto
            resultado.add(cancion)  # agregar la cancion al resultado
    return resultado


print(
    "Canciones que ambos escuchan (funcion):",
    interseccion(canciones_juan, canciones_maria),
)

canciones_juan_clases = Conjunto(
    ["Despacito", "Shape of You", "Blinding Lights", "Uptown Funk", "Havana"]
)

canciones_maria_clases = Conjunto(
    [
        "Blinding Lights",
        "Uptown Funk",
        "Can't Stop the Feeling",
        "Shut Up and Dance",
        "Happy",
    ]
)

compartidad_clases = canciones_juan_clases.interseccion(canciones_maria_clases)
print("Canciones que ambos escuchan (clases):", compartidad_clases)

"""2. que canciones le puedo recomendar a juan """

recomendaciones_juan = canciones_maria - canciones_juan
print("Recomendaciones para Juan:", recomendaciones_juan)

"""3. catalogo de canciones (UNION)"""

union = canciones_maria.union(canciones_juan)
print("Catalogo de canciones:", union)


"""REDES"""

algoritmos={"ana","juan","pedro","maria","carlos","laura"}

bases_datos={"pedro","maria","sofia","diego","ana","juan","jose"}

redes={"juan","maria","sofia","diego","ana","carlos", "ricardo"}

"""estudiantes que solo estan viendo una materia """


union_3_conjuntos=algoritmos.union(bases_datos).union(redes)
una_sola_materia=union_3_conjuntos-(algoritmos.intersection(bases_datos)).union(algoritmos.intersection(redes)).union(bases_datos.intersection(redes))  

print("Estudiantes que solo estan viendo una materia:", una_sola_materia)


"""contar cuantos estudinates hya en las 3 materias"""

total_estudiantes=algoritmos.union(bases_datos).union(redes)
print("Total de estudiantes en las 3 materias:", len(total_estudiantes))

"""como puedo saber que todos los de lagoritmos estan biendo bases de datos"""

if algoritmos <= bases_datos:
    print("Todos los estudiantes de algoritmos están viendo bases de datos.")   
else:    print("No todos los estudiantes de algoritmos están viendo bases de datos.")   


"""EJERCIO TIPO EXAMEN"""
catalogo = {
    "Inception": {"ciencia ficcion", "accion", "thriller"},
    "Titanic": {"romance", "drama"},
    "The Dark Knight": {"accion", "drama", "crimen"},
    "Avengers: Endgame": {"accion", "ciencia ficcion", "aventura"},
    "Interstellar": {"ciencia ficcion", "drama", "aventura"},
    "Frozen": {"animacion", "fantasia", "musical"},
    "Joker": {"drama", "crimen", "thriller"},
    "Toy Story": {"animacion", "aventura", "comedia"},
    "The Conjuring": {"terror", "misterio", "thriller"},
    "Spider-Man": {"accion", "aventura", "ciencia ficcion"}
}

""" 1. encontrar peliculas similaresque comparta por lo menos 2 generos (que devuelva pelicula 1, pelicula 2 y lista de genero que comparten)
2.  """

"""def peliculas_similares(catalogo):#metodo que recibe el catalogo de peliculas
    peliculas=list(catalogo.keys())#obtener la lista apartir de las claves del catalogo
    similares=[]#creamos una lista vacia para guardar las peliculas similares
    for i in range(len(peliculas)):#recorre la lista
        for j in range(i+1,len(peliculas)):#recorrer apartir de la siguiente posicion
            pelicula1=peliculas[i]#pelocula 1 es la pelicula en la posicion i
            pelicula2=peliculas[j]#pelicula 2 es la pelicula en la posicion j
            generos_comunes=catalogo[pelicula1].intersection(catalogo[pelicula2])#interseccionde los generos 
            if len(generos_comunes)>=2:#si la cantidad de generos comunes es mayor o igual a 2
                similares.append((pelicula1,pelicula2,generos_comunes)) #agregar a la lista de similares una tupla con la pelicula 1, pelicula 2 y los generos comunes

    return similares            
peliculas_similares_resultado=peliculas_similares(catalogo)#llamamos a la funcion para obtener las peliculas similares
print("Peliculas similares:", peliculas_similares_resultado)"""

peliculas_con_generos_comunes=[]#lista vacia para guardar las peliculas con generos comunes
peliculas=list(catalogo.keys())#obtener la lista apartir de las claves del catalogo
for i in range(len(peliculas)):#recorre la lista
    for j in range(i+1,len(peliculas)):#recorrer apartir de la siguiente posicion
        p1,p2=peliculas[i],peliculas[j]#pelocula 1 es la pelicula en la posicion i y pelicula 2 es la pelicula en la posicion j
        comunes= catalogo[p1] & catalogo[p2]#interseccionde los generos
        if len(comunes)>=2:#si la cantidad de generos comunes es mayor o igual a 2
            peliculas_con_generos_comunes.append((p1,p2,sorted(comunes))) #agregar a la lista de similares una tupla con la pelicula 1, pelicula 2 y los generos comunes

peliculas_similares=peliculas_con_generos_comunes#asignamos la lista de peliculas con generos comunes a la variable peliculas_similares
print("Peliculas similares:", peliculas_similares)

favoritos={"accion","crimen","aventura"}

"""estos son mis generos favortios del dicicionario que peliculas me recomienda y con que porcentaje,
si tiene estos 3 favoritos con un 100% si tiene 2 de mis favoritos con un 66% y si tiene 1 de mis favoritos con
 un 33% y ordenados de mayor a menor porcentaje"""
 
recomendaciones = []#lista vacia para guardar las recomendaciones

for pelicula in catalogo:#recorrer el catalogo de peliculas

    comunes = catalogo[pelicula] & favoritos#interseccion de los generos de la pelicula con mis favoritos para obtener los generos comunes
    cantidad = len(comunes) #cantidad de generos comunes
    porcentaje = int((cantidad / len(favoritos)) * 100)#calcular el porcentaje de coincidencia dividiendo la cantidad de generos comunes entre la cantidad total de favoritos y multiplicando por 100 para obtener el porcentaje

    if cantidad > 0:#si tiene al menos 1 genero favorito
        recomendaciones.append((pelicula, porcentaje, sorted(comunes)))#agregar a la lista de recomendaciones una tupla con el nombre de la pelicula, el porcentaje de coincidencia y los generos comunes ordenados alfabeticamente

# ordenar de mayor a menor
recomendaciones.sort(key=lambda x: x[1], reverse=True)#ordenar la lista de recomendaciones por el porcentaje de coincidencia de mayor a menor

# imprimir resultados
for pelicula, porcentaje, comunes in recomendaciones:
    print(f"{pelicula} -> {porcentaje}% | Coincide en: {comunes}")


"""como puedo mostrar todos los generos que hay en el catalogo sin repetir"""
todos_los_generos = set()  # conjunto vacío

for pelicula in catalogo:
    todos_los_generos |= catalogo[pelicula]  # unión de conjuntos

print("todos los geneeros:", todos_los_generos)

"""tenemos generos por peloculas, necesito el catalogo de generos con las peliculas que pertenecen a cada genero"""
  # diccionario vacío
generos_a_peliculas = {}#diccionario vacio

for pelicula in catalogo:#recorrer claves del catalogo
    for genero in catalogo[pelicula]:#recorrer los generos de cada pelicula
        
        # si el género no existe, lo creo
        if genero not in generos_a_peliculas:#si el genro no esta crearlo
            generos_a_peliculas[genero] = set()#crear un conjunto vacio para ese genero en el diccionario
        
        # agrego la película al género
        generos_a_peliculas[genero].add(pelicula)#agregar la pelicula al conjunto del genero correspondiente

print("generosa peliculas:" ,generos_a_peliculas)


"""necesito un metodo que reciba 2 peliculas y me devuelva el indice de similitud Jaccard"""

def indice_jaccard(pelicula1, pelicula2):
    generos1 = catalogo[pelicula1]#obtener los generos de la pelicula 1
    generos2 = catalogo[pelicula2]#obtener los generos de la pelicula 2

    interseccion = generos1 & generos2 #calcular la interseccion de los generos
    union = generos1 | generos2 #calcular la union de los generos

    if len(union) == 0: #si la union es vacia, el indice de jaccard es 0
        return 0.0

    # calcular índice
    indice = len(interseccion) / len(union)
    
    return indice
resultado = (indice_jaccard("Inception", "Spider-Man"), indice_jaccard("Toy Story", "Frozen"), indice_jaccard("The Dark Knight", "Joker"))

print(resultado)


STOPWORDS={"el","la","los","las","un","una","unos","unas","de","del","al",
           "a","en","con","por","para","que","y","o","e","es","son","pero","esta","se","estar","estas","estos"}

"mirar como se plagio comparando 2 textos, si tiene sun parecido del 60% o mas se considera plagio ignornaod las stopworsd"
def indice_plagio(texto1, texto2):
    palabras1 = set(texto1.lower().split()) - STOPWORDS #obtener las palabras del texto 1, convertir a minusculas, dividir en palabras y eliminar stopwords
    palabras2 = set(texto2.lower().split()) - STOPWORDS #obtener las palabras del texto 2, convertir a minusculas, dividir en palabras y eliminar stopwords

    interseccion = palabras1 & palabras2 #calcular la interseccion de las palabras
    union = palabras1 | palabras2 #calcular la union de las palabras

    if len(union) == 0: #si la union es vacia, el indice de plagio es 0
        return 0.0

    # calcular índice
    indice = len(interseccion) / len(union)
    # 👇 AQUÍ AGREGAS LA CONDICIÓN
    if indice >= 0.6:
        print("Plagio detectado")
    else:
        print("No es plagio")


    return indice

texto1 = "El perro juega en el parque con niños pequeños"
texto2 = "El perro corre en el parque con niños pequeños y juega felizmente"
plagio = indice_plagio(texto1, texto2)
print(f"El índice de plagio entre los textos es: {plagio }")

texto1="Hola Mundo"
texto2="Hola Mundo"
plagio = indice_plagio(texto1, texto2)      
print(f"El índice de plagio entre los textos es: {plagio }")


texto1 = "perro gato parque juega"
texto2 = "perro gato parque duerme"

plagio = indice_plagio(texto1, texto2)
print(f"El índice de plagio entre los textos es: {plagio }")

texto1 = "perro gato parque juega corre"
texto2 = "perro gato parque duerme come"
plagio = indice_plagio(texto1, texto2)
print(f"El índice de plagio entre los textos es: {plagio }")
