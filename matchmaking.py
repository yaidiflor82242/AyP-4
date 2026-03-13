#MATCHMAKING ITERATIVO
class Jugador:
    def __init__(self, id, nivel):
        self.id = id
        self.nivel = nivel

class Matchmaking:
    def __init__(self):
        self.cola = []

    def agregar_jugador(self, id, nivel):
        nuevo = Jugador(id, nivel)

        for jugador in self.cola:
            if abs(jugador.nivel - nivel) <= 150:
                print(f"Match: {jugador.id} vs {nuevo.id}")
                self.cola.remove(jugador)
                return

        self.cola.append(nuevo)
        print(f"Jugador {id} agregado a la cola")

    def mostrar_cola(self):
        for j in self.cola:
            print(j.id, j.nivel)
m = Matchmaking()

m.agregar_jugador(1,1000)
m.agregar_jugador(2,1400)
m.agregar_jugador(3,1100)
m.agregar_jugador(4,1450)
m.agregar_jugador(5,2000)

"""# Clase que representa a un jugador del juego
class Jugador:
    
    # Constructor del jugador
    def __init__(self, id, nivel):
        self.id = id        # ID único del jugador
        self.nivel = nivel  # Nivel de habilidad del jugador (0 - 3000)


# Clase que maneja el sistema de matchmaking
class Matchmaking:

    # Constructor del sistema
    def __init__(self):
        # Lista que funcionará como la cola de espera de jugadores
        self.cola = []


    # Método para agregar un jugador al sistema
    def agregar_jugador(self, id, nivel):

        # Se crea un nuevo objeto jugador con su id y nivel
        nuevo = Jugador(id, nivel)

        # Se recorre la cola para buscar un jugador compatible
        for jugador in self.cola:

            # Se calcula la diferencia de nivel
            # abs() devuelve el valor absoluto de la resta
            if abs(jugador.nivel - nivel) <= 150:

                # Si cumple la condición, se genera el match
                print(f"Match: {jugador.id} vs {nuevo.id}")

                # Se elimina el jugador de la cola porque ya fue emparejado
                self.cola.remove(jugador)

                # Se termina la función porque ya se encontró pareja
                return

        # Si no se encontró ningún jugador compatible
        # el nuevo jugador se agrega al final de la cola
        self.cola.append(nuevo)

        # Se informa que el jugador queda esperando
        print(f"Jugador {id} agregado a la cola")


    # Método para mostrar los jugadores que están esperando
    def mostrar_cola(self):

        # Recorre la cola
        for j in self.cola:

            # Muestra el id y nivel de cada jugador
            print(j.id, j.nivel)
"""

#MATCHMAKING RECURSIVIDAD
class Jugador:
    def __init__(self, id, nivel):
        self.id = id
        self.nivel = nivel


class Matchmaking:
    def __init__(self):
        self.cola = []

    def agregar_jugador(self, id, nivel):
        nuevo = Jugador(id, nivel)

        # buscar rival de forma recursiva
        encontrado = self.buscar_match(nuevo, 0)

        if not encontrado:
            self.cola.append(nuevo)
            print(f"Jugador {id} agregado a la cola")


    # función recursiva
    def buscar_match(self, nuevo, indice):

        # caso base: llegamos al final de la cola
        if indice >= len(self.cola):
            return False

        jugador = self.cola[indice]

        # verificar diferencia de nivel
        if abs(jugador.nivel - nuevo.nivel) <= 150:
            print(f"Match: {jugador.id} vs {nuevo.id}")
            self.cola.pop(indice)
            return True

        # llamada recursiva
        return self.buscar_match(nuevo, indice + 1)


    def mostrar_cola(self):
        for j in self.cola:
            print(j.id, j.nivel)
m = Matchmaking()

m.agregar_jugador(1, 1000)
m.agregar_jugador(2, 1400)
m.agregar_jugador(3, 1100)
m.agregar_jugador(4, 1450)
m.agregar_jugador(5, 2000)


m.mostrar_cola()
"""
# Clase que representa a cada jugador
class Jugador:
    def __init__(self, id, nivel):
        self.id = id
        self.nivel = nivel


# Clase que maneja el sistema de matchmaking
class Matchmaking:
    def __init__(self):
        # Cola de jugadores esperando partida
        self.cola = []

    # Método para agregar jugadores
    def agregar_jugador(self, id, nivel):
        nuevo = Jugador(id, nivel)

        # Buscar match usando recursividad
        encontrado = self.buscar_match(nuevo, 0)

        # Si no se encontró rival se agrega a la cola
        if not encontrado:
            self.cola.append(nuevo)
            print(f"Jugador {id} agregado a la cola")

    # Función recursiva para buscar rival
    def buscar_match(self, nuevo, indice):

        # Caso base: llegamos al final de la cola
        if indice >= len(self.cola):
            return False

        jugador = self.cola[indice]

        # Comparar niveles
        if abs(jugador.nivel - nuevo.nivel) <= 150:
            print(f"Match: {jugador.id} vs {nuevo.id}")

            # Eliminar jugador emparejado
            self.cola.pop(indice)

            return True

        # Llamada recursiva para revisar el siguiente jugador
        return self.buscar_match(nuevo, indice + 1)

    # Mostrar jugadores en cola
    def mostrar_cola(self):
        print("Jugadores en cola:")
        for j in self.cola:
            print(f"ID: {j.id} Nivel: {j.nivel}")


# ----------- Ejemplo de uso -----------

m = Matchmaking()

m.agregar_jugador(1, 1000)
m.agregar_jugador(2, 1400)
m.agregar_jugador(3, 1100)
m.agregar_jugador(4, 1450)
m.agregar_jugador(5, 2000)

m.mostrar_cola()"""


"""MATCHMAKING heapq"""

import heapq
import time

class Jugador:
    def __init__(self, id, nivel):
        self.id = id
        self.nivel = nivel
        self.tiempo = time.time()

class Matchmaking:

    def __init__(self):
        self.cola = []   # heap

    def agregar_jugador(self, id, nivel):

        nuevo = Jugador(id, nivel)
        # Revisar primero al jugador que más tiempo lleva esperando
        if self.cola:

            tiempo, jugador = self.cola[0]   # primer jugador del heap

            # comparar niveles
            if abs(jugador.nivel - nuevo.nivel) <= 150:

                print(f"Match: {jugador.id} vs {nuevo.id}")

                # eliminar al jugador más antiguo
                heapq.heappop(self.cola)

                return


        # Si no hay rival se agrega al heap
        heapq.heappush(self.cola, (nuevo.tiempo, nuevo))
        print(f"Jugador {id} agregado a la cola")

    def mostrar_cola(self):

        print("Jugadores esperando:")

        for tiempo, jugador in self.cola:
            espera = time.time() - tiempo
            print(f"ID:{jugador.id} Nivel:{jugador.nivel} Espera:{round(espera,2)}s")


# Uso
m = Matchmaking()

m.agregar_jugador(1,1000)
time.sleep(1)

m.agregar_jugador(2,1200)
time.sleep(1)

m.agregar_jugador(3,1050)

m.mostrar_cola()


"""
import heapq
import time

class Jugador:
    def __init__(self, id, nivel):
        self.id = id
        self.nivel = nivel
        self.tiempo = time.time()

class Matchmaking:

    def __init__(self):
        self.cola = []   # heap

    def agregar_jugador(self, id, nivel):

        nuevo = Jugador(id, nivel)

        # Buscar rival compatible
        for i, (_, jugador) in enumerate(self.cola):

            if abs(jugador.nivel - nuevo.nivel) <= 150:

                print(f"Match: {jugador.id} vs {nuevo.id}")

                # eliminar del heap
                self.cola.pop(i)
                heapq.heapify(self.cola)

                return

        # Si no hay rival se agrega al heap
        heapq.heappush(self.cola, (nuevo.tiempo, nuevo))
        print(f"Jugador {id} agregado a la cola")

    def mostrar_cola(self):

        print("Jugadores esperando:")

        for tiempo, jugador in self.cola:
            espera = time.time() - tiempo
            print(f"ID:{jugador.id} Nivel:{jugador.nivel} Espera:{round(espera,2)}s")


# Uso
m = Matchmaking()

m.agregar_jugador(1,1000)
time.sleep(1)

m.agregar_jugador(2,1200)
time.sleep(1)

m.agregar_jugador(3,1050)

m.mostrar_cola()
"""