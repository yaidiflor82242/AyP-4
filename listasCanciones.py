# ============================================================================
# CLASE NODO DOBLE - Para la lista de reproducción de Spotify
# ============================================================================
class NodoDoble:
    """Representa una canción en la lista de reproducción"""
    def __init__(self, dato, duracion):
        # Almacena el nombre de la canción
        self.dato = dato
        # Almacena la duración en segundos
        self.duracion = duracion
        # Referencia a la siguiente canción
        self.siguiente = None
        # Referencia a la canción anterior
        self.anterior = None


# ============================================================================
# CLASE LISTA DOBLE - Simulación de una lista de reproducción Spotify
# ============================================================================
class ListaDoble:
    """Lista doblemente ligada para manejar canciones"""
    def __init__(self): 
        # Puntero al primer nodo (primera canción)
        self.cabeza = None
        # Puntero al último nodo (última canción)
        self.cola = None

    # ========================================================================
    # Verificar si la lista está vacía
    # ========================================================================
    def esta_vacia(self):
        """Retorna True si no hay canciones en la lista"""
        return self.cabeza is None

    # ========================================================================
    # Insertar canción al INICIO
    # ========================================================================
    def insertar_inicio(self, dato, duracion):
        """Agrega una canción al inicio de la lista"""
        nuevo = NodoDoble(dato, duracion)
        if self.esta_vacia():
            # Si es la primera canción, es cabeza y cola
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            # Insertar antes de la canción actual
            nuevo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo
            self.cabeza = nuevo

    # ========================================================================
    # Insertar canción al FINAL (Más usado en Spotify)
    # ========================================================================
    def insertar_final(self, dato, duracion):
        """Agrega una canción al final de la lista (como en Spotify)"""
        nuevo = NodoDoble(dato, duracion)
        if self.esta_vacia():
            # Si es la primera canción, es cabeza y cola
            self.cabeza = nuevo
            self.cola = nuevo
        else:
            # Agregar después de la última canción
            self.cola.siguiente = nuevo
            nuevo.anterior = self.cola
            self.cola = nuevo

    # ========================================================================
    # Eliminar la PRIMERA canción
    # ========================================================================
    def eliminar_inicio(self):
        """Elimina la primera canción de la lista"""
        if self.esta_vacia():
            print("❌ La lista está vacía")
            return None
        
        # Guardar el dato de la primera canción
        dato = self.cabeza.dato
        if self.cabeza == self.cola:
            # Si solo hay una canción
            self.cabeza = None
            self.cola = None
        else:
            # Mover cabeza al siguiente
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None

        return dato

    # ========================================================================
    # Eliminar la ÚLTIMA canción
    # ========================================================================
    def eliminar_final(self):
        """Elimina la última canción de la lista"""
        if self.esta_vacia():
            print("❌ La lista está vacía")
            return None
        dato = self.cola.dato
        if self.cabeza == self.cola:
            # Si solo hay una canción
            self.cabeza = None
            self.cola = None
        else:
            # Mover cola al anterior
            self.cola = self.cola.anterior
            self.cola.siguiente = None
        return dato    
    
    # ========================================================================
    # Recorrer la lista hacia ADELANTE
    # ========================================================================
    def recorrer_adelante(self):
        """Muestra todas las canciones en orden"""
        if self.esta_vacia():
            print("📭 Lista vacía")
            return
        print("\n🎵 CANCIONES (en orden):")
        actual = self.cabeza
        numero = 1
        while actual:
            minutos = actual.duracion // 60
            segundos = actual.duracion % 60
            print(f"   {numero}. {actual.dato} - {minutos}:{segundos:02d}")
            actual = actual.siguiente
            numero += 1

    # ========================================================================
    # Recorrer la lista hacia ATRÁS
    # ========================================================================
    def recorrer_atras(self):
         if self.esta_vacia():
              print("lista vacia")
              return

         print("fin<-> inicio", end=" ")
         actual=self.cola
         elementos=[]
         while actual:
              elementos.append(str(actual.dato))
              actual=actual.anterior
         print("<-> ".join(elementos))


    # ========================================================================
    # Buscar una canción
    # ========================================================================
    def buscar(self, dato):
        """Busca si una canción existe en la lista"""
        actual = self.cabeza
        while actual:
            if actual.dato.lower() == dato.lower():  # Búsqueda sin distinguir mayúsculas
                return True
            actual = actual.siguiente
        return False

    # ========================================================================
    # Obtener cantidad de canciones
    # ========================================================================
    def __len__(self):
        """Retorna la cantidad de canciones en la lista"""
        contador = 0
        actual = self.cabeza
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador
    
    # ========================================================================
    # Representación en texto
    # ========================================================================
    def __str__(self):
        """Convierte la lista a texto"""
        if self.esta_vacia():
            return "📭 Lista vacía"
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        return " <-> ".join(elementos)

# ============================================================================
# PROGRAMA - Reproductor de Canciones con Lista Doblemente Ligada
# ============================================================================

import time

# Crear la lista de reproducción
playlist = ListaDoble()

def convertir_tiempo(segundos):
    """Convierte segundos a formato minutos:segundos"""
    minutos = segundos // 60
    segs = segundos % 60
    return f"{minutos}:{segs:02d}"

def reproducir_cancion(nombre, duracion_segundos):
    """Simula la reproducción de una canción"""
    print(f"\n{'='*60}")
    print(f"▶️  REPRODUCIENDO: {nombre}")
    print(f"⏱️  DURACIÓN TOTAL: {convertir_tiempo(duracion_segundos)}")
    print(f"{'='*60}")
    
    for segundo_actual in range(duracion_segundos):
        tiempo_actual = convertir_tiempo(segundo_actual)
        tiempo_restante = convertir_tiempo(duracion_segundos - segundo_actual)
        barra_progreso = int((segundo_actual / duracion_segundos) * 20)
        barra = "█" * barra_progreso + "░" * (20 - barra_progreso)
        print(f"\r[{barra}] {tiempo_actual} / {convertir_tiempo(duracion_segundos)} | Restante: {tiempo_restante}", end="", flush=True)
        time.sleep(1)
    
    print(f"\n✅ Canción terminada: {nombre}")
    print("="*60)

def mostrar_lista():
    """Muestra la lista de canciones agregadas"""
    print(f"\n{'='*60}")
    print("📋 LISTA DE CANCIONES AGREGADAS:")
    print(f"{'='*60}")
    playlist.recorrer_adelante()
    print(f"{'='*60}\n")

# Programa principal
print("\n" + "🎵"*30)
print("🎵 REPRODUCTOR DE CANCIONES 🎵")
print("🎵"*30 + "\n")

while True:
    # Pedir datos de la canción
    print("\n" + "-"*60)
    cancion = input("📝 Ingresa el nombre de la canción (o 'salir' para terminar): ").strip()
    
    if cancion.lower() == "salir":
        break
    
    if not cancion:
        print("⚠️  Debes ingresar un nombre de canción")
        continue
    
    try:
        duracion = int(input("⏱️  Ingresa la duración en segundos: ").strip())
        if duracion <= 0:
            print("⚠️  La duración debe ser mayor a 0 segundos")
            continue
        
        # Agregar a la lista
        playlist.insertar_final(cancion, duracion)
        
        # Reproducir inmediatamente
        reproducir_cancion(cancion, duracion)
        
        # Mostrar la lista actual
        mostrar_lista()
        
    except ValueError:
        print("⚠️  Debes ingresar un número válido para la duración")

# Mostrar lista final
print("\n" + "="*60)
print("🎵 LISTA FINAL DE REPRODUCCIÓN 🎵")
print("="*60)
playlist.recorrer_adelante()
print("👋 ¡Gracias por usar el reproductor!")
print("="*60 + "\n")


