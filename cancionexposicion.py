#ejemplo de un reproductor de canciones usando una lista doblemente enlazada de los que expusieron
class Cancion:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion
        self.siguiente = None
        self.anterior = None
    
    def duracion_formato(self):
        minutos = self.duracion// 60
        segundos = self.duracion % 60
        return f"{minutos}:{segundos:02d}"



class Reproductor:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.actual = None
        
    def esta_vacia(self):
        #Verifica si la lista esta vacia
        return self.cabeza is None  #retorna un booleano

    
    def insertar_inicio(self, nombre, duracion):
        nuevo = Cancion(nombre, duracion)

        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo


    def insertar_final(self, nombre, duracion):
        nuevo= Cancion(nombre, duracion)
        if self.esta_vacia():
            #Lista vacia:cabeza y cola apuntan al nuevo
            self.cabeza=nuevo
            self.cola=nuevo
            self.actual = nuevo   
        else:
             #conectar nuevo con la cola actual
            self.cola.siguiente=nuevo
            nuevo.anterior= self.cola
            self.cola=nuevo
            
        print("Canción agregada")

    # Mostrar lista de canciones
    def mostrar_lista(self):
        if self.esta_vacia():
            print("Lista vacia")
            return
        actual = self.cabeza
        print("\n Lista de canciones:")
        while actual:
            if actual == self.actual:
                print(f" {actual.nombre} ({actual.duracion_formato()})  <-- Reproduciendo")
            else:
                print(f"  {actual.nombre} ({actual.duracion_formato()})")

            actual = actual.siguiente

      

    # Reproducir canción actual
    def reproducir(self):
        if self.actual:
            print(f"Reproduciendo: {self.actual.nombre} ({self.actual.duracion_formato()})")
        else:
            print("No hay canciones")

    # Pasar a la siguiente canción
    def siguiente(self):
        if self.actual and self.actual.siguiente:
            self.actual = self.actual.siguiente
            self.reproducir()
        else:
            print("No hay siguiente canción")

    # Volver a la canción anterior
    def anterior(self):
        if self.actual and self.actual.anterior:
            self.actual = self.actual.anterior
            self.reproducir()
        else:
            print(" No hay canción anterior")

    # Eliminar una canción por nombre
    def eliminar_cancion(self, nombre):
        actual = self.cabeza

        while actual:
            if actual.nombre == nombre:
                # Si es la primera
                if actual.anterior is None:
                    self.cabeza = actual.siguiente
                    self.cabeza.anterior = None
                else:

                    actual.anterior.siguiente = actual.siguiente

                # Si no es la última
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior

                # Ajustar canción actual
                if self.actual == actual:
                    self.actual = actual.siguiente 
                else:
                    self.actual=actual.anterior

                print(" Canción eliminada")
                return

            actual = actual.siguiente

        print("Canción no encontrada")



def menu():
    print("\nREPRODUCTOR DE CANCIONES ")
    print("1. Agregar canción")
    print("2. Mostrar lista")
    print("3. Reproducir canción actual")
    print("4. Siguiente canción")
    print("5. Canción anterior")
    print("6. Eliminar canción")
    print("7. Salir")



reproductor = Reproductor()

while True:
    menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre de la canción: ")
        duracion = int(input("Duracion de la canción: "))

        reproductor.insertar_final(nombre, duracion)

    elif opcion == "2":
        reproductor.mostrar_lista()

    elif opcion == "3":
        reproductor.reproducir()

    elif opcion == "4":
        reproductor.siguiente()

    elif opcion == "5":
        reproductor.anterior()

    elif opcion == "6":
        nombre = input("Nombre de la canción a eliminar: ")
        reproductor.eliminar_cancion(nombre)

    elif opcion == "7":
        print("Saliendo del reproductor...")
        break

    else:
        print(" Opción inválida")