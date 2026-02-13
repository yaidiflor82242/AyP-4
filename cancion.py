class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoble:
    def __init__(self): 
        self.cabeza = None
        self.cola = None

    def esta_vacia(self):
        return self.cabeza is None

    def insertar_inicio(self, dato):
        nuevo = NodoDoble(dato)
        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo

    def insertar_final(self, dato):
        nuevo = NodoDoble(dato)
        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo

    def eliminar_inicio(self):
        if self.esta_vacia():
            return None
        
        dato = self.cabeza.dato
        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None

        return dato

    def eliminar_final(self):
        if self.esta_vacia():
            return None
        dato = self.cola.dato
        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None
        else:
            self.cola = self.cola.anterior
            self.cola.siguiente = None
        return dato

    def eliminar_por_nombre(self, nombre):
        """Elimina una canción por nombre"""
        actual = self.cabeza
        while actual:
            if actual.dato.nombre.lower() == nombre.lower(): 
                # Si es el único nodo
                if actual == self.cabeza and actual == self.cola:
                    self.cabeza = None
                    self.cola = None
                # Si es el primer nodo
                elif actual == self.cabeza:
                    self.cabeza = actual.siguiente
                    self.cabeza.anterior = None
                # Si es el último nodo
                elif actual == self.cola:
                    self.cola = actual.anterior
                    self.cola.siguiente = None
                # Si está en el medio
                else:
                    actual.anterior.siguiente = actual.siguiente
                    actual.siguiente.anterior = actual.anterior
                return True
            actual = actual.siguiente
        return False
    
    def recorrer_adelante(self):
        if self.esta_vacia():
            print("📭 Lista vacía")
            return
        print("\n🎵 CANCIONES EN LA LISTA:")
        actual = self.cabeza
        numero = 1
        while actual:
            print(f"   {numero}. {actual.dato}")
            actual = actual.siguiente
            numero += 1
        print()

    def buscar(self, dato):
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False

    def __len__(self):
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador
    
    def __str__(self):
        if self.esta_vacia():
            return "📭 Lista vacía"
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " <-> ".join(elementos)     
#se crea una clase cancion 
class Cancion:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion  # en segundos

    def tiempo_formato(self):
        minutos = self.duracion // 60
        segundos = self.duracion % 60
        return f"{minutos}:{segundos:02d}"

    def __str__(self):
        return f"{self.nombre} ({self.tiempo_formato()})"

import time

# Crear lista de reproducción
playlist = ListaDoble()

print("🎵 REPRODUCTOR DE CANCIONES 🎵\n")

# Pedir canciones al usuario
while True:
    print("-" * 50)
    nombre = input("📝 Ingrese el nombre de la canción: ").strip()
    
    if not nombre:
        print("⚠️  Debe ingresar un nombre")
        continue
    
    try:
        duracion = int(input("⏱️  Ingrese duración en segundos: "))
        if duracion <= 0:
            print("⚠️  La duración debe ser mayor a 0")
            continue
    except ValueError:
        print("⚠️  Ingrese un número válido")
        continue
    
    # Crear canción y agregar a la lista
    cancion = Cancion(nombre, duracion)
    playlist.insertar_final(cancion)
    
    # Mostrar reproducción
    print(f"\n▶️  REPRODUCIENDO: {cancion.nombre}")
    print(f"⏱️  DURACIÓN: {cancion.tiempo_formato()}\n")
    
    # Mostrar opciones
    print("="*50)
    print("1️⃣  - Agregar otra canción")
    print("2️⃣  - Ver lista de canciones")
    print("3️⃣  - Reproducir una canción")
    print("4️⃣  - Salir")
    print("="*50)
    
    while True:
        opcion = input("\n📍 Seleccione una opción (1-4): ").strip()
        
        if opcion == "1":
            break  # Volver al inicio del bucle para agregar otra canción
        
        elif opcion == "2":
            playlist.recorrer_adelante()
        
        elif opcion == "3":
            playlist.recorrer_adelante()
            cancion_reproducir = input("\n🎵 Ingrese el nombre de la canción a reproducir: ").strip()
            
            # Buscar y reproducir la canción
            actual = playlist.cabeza
            encontrada = False
            while actual:
                # Comparar nombres en minúsculas para no importar si están en MAYÚSCULAS o minúsculas
                # .lower() convierte el texto a minúsculas (ej: "JUAN" → "juan", "JuAn" → "juan")
                if actual.dato.nombre.lower() == cancion_reproducir.lower():
                    print(f"\n▶️  REPRODUCIENDO: {actual.dato.nombre}")
                    print(f"⏱️  DURACIÓN: {actual.dato.tiempo_formato()}\n")
                    encontrada = True
                    break
                actual = actual.siguiente
            
            if not encontrada:
                print(f"❌ Canción '{cancion_reproducir}' no encontrada\n")
        
        elif opcion == "4":
            print("\n👋 ¡Gracias por usar el reproductor!")
            exit()
        
        else:
            print("⚠️  Opción no válida")
    
    else:
        print("⚠️  Opción no válida")

print("\n👋 ¡Gracias por usar el reproductor!")
