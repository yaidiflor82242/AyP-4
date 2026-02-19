# -----------------------------
# Clase NodoDoble
# -----------------------------
class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None


# -----------------------------
# Clase ListaDoble
# -----------------------------
class ListaDoble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def esta_vacia(self):
        return self.cabeza is None

    # Insertar al final
    def insertar_final(self, dato):
        nuevo = NodoDoble(dato)

        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo

    # Mostrar canciones
    def mostrar(self):
        if self.esta_vacia():
            print("📭 Lista vacía")
            return

        print("\n🎵 LISTA DE CANCIONES:")
        actual = self.cabeza
        contador = 1

        while actual:
            print(f"{contador}. {actual.dato}")
            actual = actual.siguiente
            contador += 1
        print()

    # Buscar canción por nombre
    def buscar_por_nombre(self, nombre):
        actual = self.cabeza

        while actual:
            if actual.dato.nombre.lower() == nombre.lower():
                return actual
            actual = actual.siguiente

        return None

    # Eliminar por nombre
    def eliminar_por_nombre(self, nombre):
        actual = self.buscar_por_nombre(nombre)

        if actual is None:
            return False

        # Si es el único nodo
        if actual == self.cabeza and actual == self.cola:
            self.cabeza = None
            self.cola = None

        # Si es el primero
        elif actual == self.cabeza:
            self.cabeza = actual.siguiente
            self.cabeza.anterior = None

        # Si es el último
        elif actual == self.cola:
            self.cola = actual.anterior
            self.cola.siguiente = None

        # Si está en el medio
        else:
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior

        return True

    # Reproducir canción
    def reproducir(self, nombre):
        nodo = self.buscar_por_nombre(nombre)

        if nodo:
            print(f"\n▶️ REPRODUCIENDO: {nodo.dato.nombre}")
            print(f"⏱️ DURACIÓN: {nodo.dato.tiempo_formato()}\n")
        else:
            print("❌ Canción no encontrada")


# -----------------------------
# Clase Cancion
# -----------------------------
class Cancion:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion  # segundos

    def tiempo_formato(self):
        minutos = self.duracion // 60
        segundos = self.duracion % 60
        return f"{minutos}:{segundos:02d}"

    def __str__(self):
        return f"{self.nombre} ({self.tiempo_formato()})"


# -----------------------------
# PROGRAMA PRINCIPAL
# -----------------------------
playlist = ListaDoble()

while True:
    print("\n" + "=" * 50)
    print("🎵 REPRODUCTOR DE MÚSICA 🎵")
    print("1️⃣  Agregar canción")
    print("2️⃣  Mostrar canciones")
    print("3️⃣  Buscar canción")
    print("4️⃣  Eliminar canción")
    print("5️⃣  Reproducir canción")
    print("6️⃣  Salir")
    print("=" * 50)

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre de la canción: ").strip()

        try:
            duracion = int(input("Duración en segundos: "))
            if duracion <= 0:
                print("⚠️ La duración debe ser mayor que 0")
                continue
        except ValueError:
            print("⚠️ Ingrese un número válido")
            continue

        cancion = Cancion(nombre, duracion)
        playlist.insertar_final(cancion)
        print("✅ Canción agregada")

    elif opcion == "2":
        playlist.mostrar()

    elif opcion == "3":
        nombre = input("Nombre a buscar: ")
        resultado = playlist.buscar_por_nombre(nombre)

        if resultado:
            print("✅ Canción encontrada:", resultado.dato)
        else:
            print("❌ No encontrada")

    elif opcion == "4":
        nombre = input("Nombre a eliminar: ")

        if playlist.eliminar_por_nombre(nombre):
            print("🗑️ Canción eliminada")
        else:
            print("❌ Canción no encontrada")

    elif opcion == "5":
        nombre = input("Nombre a reproducir: ")
        playlist.reproducir(nombre)

    elif opcion == "6":
        print("👋 Gracias por usar el reproductor")
        break

    else:
        print("⚠️ Opción inválida")
