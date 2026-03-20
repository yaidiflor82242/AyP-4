class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None  # cada nodo es un elemento del conjunto


class Conjunto:
    def __init__(
        self, elementos=None
    ):  # si no le paso el paramentro None se iniciliaza en O
        self.cabeza = None
        self.tamaño = 0
        if elementos:
            for e in elementos:
                self.agregar(e)

    def esta_vacio(self):
        return self.cabeza is None

    def cardinalidad(
        self,
    ):  # metdo para obtener la cantidad de elementos del conjunto, devuelve un entero
        return self.tamaño

    def pertenece(
        self, x
    ):  # metodo para verificar si un elemento pertenece al conjunto, devuelve True o False
        actual = self.cabeza
        while actual:
            if (
                actual.dato == x
            ):  # compara el dato del nodo con el elemento que quiero agregar
                return True
            actual = actual.siguiente  # avanzar al siguiente nodo
        return False

    def agregar(self, x):
        if self.pertenece(x):
            return False
        nuevo = Nodo(x)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo
        self.tamaño += 1
        return True

    def eliminar(
        self, x
    ):  # metodo para eliminar un elemento del conjunto, devuelve True si se elimino el elemento, False si el elemento no pertenece al conjunto
        if self.esta_vacio():
            return False
        if self.cabeza.dato == x:  # si el elemento a eliminar es el primero de la lista
            self.cabeza = self.cabeza.siguiente
            self.tamaño -= 1  # decrementar el tamaño del conjunto
            return True
        actual = self.cabeza
        while actual.siguiente:
            if (
                actual.siguiente.dato == x
            ):  # si el elemento a eliminar es el siguiente del nodo actual
                actual.siguiente = actual.siguiente.siguiente
                self.tamaño -= 1  # decrementar el tamaño del conjunto
                return True
            actual = actual.siguiente
        return False

    def vaciar(
        self,
    ):  # metodo para vaciar el conjunto, elimina todos los elementos del conjunto
        self.cabeza = None  # eliminar la referencia a los nodos, el recolector de basura se encargara de liberar la memoria
        self.tamaño = 0  # reiniciar el tamaño a 0

    def union(self, otro):
        resultado = Conjunto()  # crear conjunto nuevo vacio
        actual = self.cabeza  # recorrerlo y agregarlo al resultado
        while actual:
            resultado.agregar(actual.dato)  # agregar el elemento al resultado
            actual = actual.siguiente
        actual = otro.cabeza  # recorrer el otro conjunto y agregarlo al resultado
        while actual:
            resultado.agregar(actual.dato)  # agregar el elemento al resultado
            actual = actual.siguiente
        return resultado

    def interseccion(self, otro):
        resultado = Conjunto()  # crear conjunto nuevo vacio
        actual = self.cabeza  # recorrerlo y agregarlo al resultado
        while actual:
            if otro.pertenece(
                actual.dato
            ):  # si el elemento del primer conjunto pertenece al otro conjunto
                resultado.agregar(actual.dato)  # agregar el elemento al resultado
            actual = actual.siguiente
        return resultado

    def diferencia(
        self, otro
    ):  # metodo para obtener la diferencia entre dos conjuntos, devuelve un conjunto con los elementos que pertenecen al primer conjunto pero no al segundo conjunto
        resultado = Conjunto()  # crear conjunto nuevo vacio
        actual = self.cabeza  # recorrerlo y agregarlo al resultado
        while actual:
            if not otro.pertenece(
                actual.dato
            ):  # si el elemento del primer conjunto no pertenece al otro conjunto
                resultado.agregar(actual.dato)  # agregar el elemento al resultado
            actual = actual.siguiente
        return resultado

    def diferencia_simetrica(
        self, otro
    ):  # metodo para obtener la diferencia simetrica entre dos conjuntos, devuelve un conjunto con los elementos que pertenecen a uno de los conjuntos pero no a ambos conjuntos
        return self.diferencia(otro).union(otro.diferencia(self))  # (A - B) ∪ (B - A)

    """ó return self.union(otro).diferencia(self.interseccion(otro)) --- (A ∪ B) - (A ∩ B)"""

    def a_lista(
        self,
    ):  # metodo para convertir el conjunto a una lista, devuelve una lista con los elementos del conjunto
        resultado = []
        actual = self.cabeza
        while actual:
            resultado.append(actual.dato)  # agregar el elemento al resultado
            actual = actual.siguiente
        return resultado

    def __str__(
        self,
    ):  # metodo para representar el conjunto como una cadena de texto, devuelve una cadena con los elementos del conjunto separados por comas
        return (
            "{" + ", ".join(str(x) for x in self.a_lista()) + "}"
        )  # utiliza el metodo a_lista para obtener una lista con los elementos del conjunto y luego los une con comas y los encierra entre llaves


A = Conjunto(["a", "b", "c"])
print(A)
B = Conjunto(["c", "d", "e"])
print(B)
C = A.union(B)
print(f"Union: {C}")
D = A.interseccion(B)
print(f"Interseccion: {D}")
E = A.diferencia(B)
print(f"Diferencia A - B: {E}")
F = A.diferencia_simetrica(B)
print(f"Diferencia simetrica: {F}")
