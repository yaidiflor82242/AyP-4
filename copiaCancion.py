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

    # -----------------------------
    # INSERTAR (se deja iterativo)
    # -----------------------------
    def insertar_final(self, dato):
        nuevo = NodoDoble(dato)

        if self.esta_vacia():
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo

    # -----------------------------
    # MOSTRAR RECURSIVO
    # -----------------------------
    def mostrar(self):
        if self.esta_vacia():
            print("📭 Lista vacía")
        else:
            print("\n🎵 LISTA DE CANCIONES:")
            self._mostrar_recursivo(self.cabeza, 1)
            print()

    def _mostrar_recursivo(self, nodo, contador):
        if nodo is None:
            return

        print(f"{contador}. {nodo.dato}")
        self._mostrar_recursivo(nodo.siguiente, contador + 1)

    # -----------------------------
    # BUSCAR RECURSIVO
    # -----------------------------
    def buscar_por_nombre(self, nombre):
        return self._buscar_recursivo(self.cabeza, nombre)

    def _buscar_recursivo(self, nodo, nombre):
        if nodo is None:
            return None

        if nodo.dato.nombre.lower() == nombre.lower():
            return nodo

        return self._buscar_recursivo(nodo.siguiente, nombre)

    # -----------------------------
    # ELIMINAR RECURSIVO
    # -----------------------------
    def eliminar_por_nombre(self, nombre):
        nodo = self.buscar_por_nombre(nombre)

        if nodo is None:
            return False

        # único nodo
        if nodo == self.cabeza and nodo == self.cola:
            self.cabeza = None
            self.cola = None

        # primero
        elif nodo == self.cabeza:
            self.cabeza = nodo.siguiente
            self.cabeza.anterior = None

        # último
        elif nodo == self.cola:
            self.cola = nodo.anterior
            self.cola.siguiente = None

        # en medio
        else:
            nodo.anterior.siguiente = nodo.siguiente
            nodo.siguiente.anterior = nodo.anterior

        return True

    # -----------------------------
    # REPRODUCIR (usa buscar recursivo)
    # -----------------------------
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
        self.duracion = duracion

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
    print("2️⃣  Mostrar canciones (recursivo)")
    print("3️⃣  Buscar canción (recursivo)")
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
                print("⚠️ Duración inválida")
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
            print("✅ Encontrada:", resultado.dato)
        else:
            print("❌ No encontrada")

    elif opcion == "4":
        nombre = input("Nombre a eliminar: ")
        if playlist.eliminar_por_nombre(nombre):
            print("🗑️ Eliminada correctamente")
        else:
            print("❌ No encontrada")

    elif opcion == "5":
        nombre = input("Nombre a reproducir: ")
        playlist.reproducir(nombre)

    elif opcion == "6":
        print("👋 Hasta luego")
        break

    else:
        print("⚠️ Opción inválida")
