class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaCircular:
    def __init__(self):
        self.cola = None

    def insertar(self, dato):
        nuevo = Nodo(dato)

        if self.cola is None:
            self.cola = nuevo
            nuevo.siguiente = nuevo
        else:
            nuevo.siguiente = self.cola.siguiente
            self.cola.siguiente = nuevo
            self.cola = nuevo

    def mostrar(self):
        if self.cola is None:
            print("Lista vacía")
            return

        actual = self.cola.siguiente

        while True:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente

            if actual == self.cola.siguiente:
                break

        print("(regresa al inicio)")


# Prueba
lista = ListaCircular()

lista.insertar(10)
lista.insertar(20)
lista.insertar(30)

lista.mostrar()
