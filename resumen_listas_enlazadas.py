""""


 REGLA 1 — ¿QUÉ PONER EN EL CASO BASE?


    ¿Qué retorna la función?        ¿Qué poner en el caso base?
    ─────────────────────────────────────────────────────────────
    Un número (contar/sumar)    →   return 0
    Un nodo (reconstruir lista) →   return None
    Una lista nueva (filtrar)   →   return lista


 REGLA 2 — ¿CUÁNDO ACTUALIZAR self.inicio?


    ¿Modifico la lista original?  →  self.inicio = self._metodo_rec(self.inicio)
    ¿Creo una lista nueva?        →  return self._metodo_rec(self.inicio, nueva_lista)


 REGLA 3 — LOS 3 PATRONES DE RECURSIVIDAD


    PATRÓN 1 — Contar/Sumar:
        if nodo is None: return 0
        return (1 si cumple condición, sino 0) + recursion(siguiente)

    PATRÓN 2 — Filtrar a nueva lista:
        if nodo is None: return lista
        if cumple condición: nueva_lista.agregar(...)
        return recursion(siguiente, nueva_lista)

    PATRÓN 3 — Eliminar nodos:
        if nodo is None: return None
        if hay_que_eliminar: return recursion(siguiente)   # saltear
        nodo.siguiente = recursion(siguiente)              # conservar
        return nodo


 REGLA 4 — DOBLE LIGADA: los 3 momentos donde hay que actualizar anterior


    Al agregar:
        nueva.anterior = nodo
        if nodo.siguiente:
            nodo.siguiente.anterior = nueva

    Al limpiar (dentro de _limpiar_rec):
        if nodo.siguiente:
            nodo.siguiente.anterior = nodo

    Al limpiar el inicio:
        if self.inicio:
            self.inicio.anterior = None
"""

# ══════════════════════════════════════════════════════════════════════════════
#                        LISTA SIMPLE — PLANTILLA BASE
# ══════════════════════════════════════════════════════════════════════════════

class Nodo:
    def __init__(self, dato, valor_orden):
        self.dato = dato
        self.valor_orden = valor_orden  # el campo por el que se ordena
        self.procesado = False          # el campo booleano (completada, pagada, etc)
        self.siguiente = None

class ListaSimple:
    def __init__(self):
        self.inicio = None

    # ─── AGREGAR ORDENADO (mayor primero) ────────────────────────────────────
    def agregar(self, dato, valor_orden):
        nuevo = Nodo(dato, valor_orden)
        if self.inicio is None or self.inicio.valor_orden < nuevo.valor_orden:
            nuevo.siguiente = self.inicio
            self.inicio = nuevo
        else:
            self._agregar_rec(self.inicio, nuevo)

    def _agregar_rec(self, nodo, nuevo):
        if nodo.siguiente is None or nodo.siguiente.valor_orden < nuevo.valor_orden:
            nuevo.siguiente = nodo.siguiente
            nodo.siguiente = nuevo
        else:
            self._agregar_rec(nodo.siguiente, nuevo)

    # ─── CONTAR/SUMAR (patrón 1) ──────────────────────────────────────────────
    def contar(self, condicion_valor):
        return self._contar_rec(self.inicio, condicion_valor)

    def _contar_rec(self, nodo, condicion_valor):
        if nodo is None:
            return 0                                      # caso base → 0
        cuenta = 1 if nodo.dato == condicion_valor and not nodo.procesado else 0
        return cuenta + self._contar_rec(nodo.siguiente, condicion_valor)

    # ─── FILTRAR A NUEVA LISTA (patrón 2) ────────────────────────────────────
    def obtener_filtrados(self, minimo):
        nueva = ListaSimple()
        return self._filtrar_rec(self.inicio, nueva, minimo)

    def _filtrar_rec(self, nodo, lista, minimo):
        if nodo is None:
            return lista                                  # caso base → lista
        if nodo.valor_orden > minimo and not nodo.procesado:
            lista.agregar(nodo.dato, nodo.valor_orden)
        return self._filtrar_rec(nodo.siguiente, lista, minimo)

    # ─── ELIMINAR NODOS (patrón 3) ───────────────────────────────────────────
    def limpiar_procesados(self):
        self.inicio = self._limpiar_rec(self.inicio)     # actualiza inicio

    def _limpiar_rec(self, nodo):
        if nodo is None:
            return None                                   # caso base → None
        if nodo.procesado:
            return self._limpiar_rec(nodo.siguiente)     # saltear
        nodo.siguiente = self._limpiar_rec(nodo.siguiente)
        return nodo                                       # conservar

    # ─── MOSTRAR ─────────────────────────────────────────────────────────────
    def mostrar(self):
        actual = self.inicio
        if actual is None:
            print("Lista vacía")
            return
        while actual:
            estado = "✓" if actual.procesado else "○"
            print(f"[{estado}] {actual.dato} | orden:{actual.valor_orden}")
            actual = actual.siguiente


# ══════════════════════════════════════════════════════════════════════════════
#                      LISTA DOBLE — PLANTILLA BASE
# ══════════════════════════════════════════════════════════════════════════════

class NodoDoble:
    def __init__(self, dato, valor_orden):
        self.dato = dato
        self.valor_orden = valor_orden
        self.procesado = False
        self.siguiente = None
        self.anterior = None             # ← lo que la hace doble

class ListaDoble:
    def __init__(self):
        self.inicio = None

    # ─── AGREGAR ORDENADO (mayor primero) ────────────────────────────────────
    def agregar(self, dato, valor_orden):
        nuevo = NodoDoble(dato, valor_orden)
        if self.inicio is None or self.inicio.valor_orden < nuevo.valor_orden:
            nuevo.siguiente = self.inicio
            if self.inicio:
                self.inicio.anterior = nuevo             # ← actualizar anterior
            self.inicio = nuevo
        else:
            self._agregar_rec(self.inicio, nuevo)

    def _agregar_rec(self, nodo, nuevo):
        if nodo.siguiente is None or nodo.siguiente.valor_orden < nuevo.valor_orden:
            nuevo.siguiente = nodo.siguiente
            nuevo.anterior = nodo                        # ← nuevo apunta atrás
            if nodo.siguiente:
                nodo.siguiente.anterior = nuevo          # ← el de adelante apunta atrás
            nodo.siguiente = nuevo
        else:
            self._agregar_rec(nodo.siguiente, nuevo)

    # ─── CONTAR/SUMAR (patrón 1) ──────────────────────────────────────────────
    def contar(self, condicion_valor):
        return self._contar_rec(self.inicio, condicion_valor)

    def _contar_rec(self, nodo, condicion_valor):
        if nodo is None:
            return 0
        cuenta = 1 if nodo.dato == condicion_valor and not nodo.procesado else 0
        return cuenta + self._contar_rec(nodo.siguiente, condicion_valor)

    # ─── FILTRAR A NUEVA LISTA (patrón 2) ────────────────────────────────────
    def obtener_filtrados(self, minimo):
        nueva = ListaDoble()
        return self._filtrar_rec(self.inicio, nueva, minimo)

    def _filtrar_rec(self, nodo, lista, minimo):
        if nodo is None:
            return lista
        if nodo.valor_orden > minimo and not nodo.procesado:
            lista.agregar(nodo.dato, nodo.valor_orden)
        return self._filtrar_rec(nodo.siguiente, lista, minimo)

    # ─── ELIMINAR NODOS (patrón 3) ───────────────────────────────────────────
    def limpiar_procesados(self):
        self.inicio = self._limpiar_rec(self.inicio)
        if self.inicio:
            self.inicio.anterior = None                  # ← el nuevo inicio no tiene anterior

    def _limpiar_rec(self, nodo):
        if nodo is None:
            return None
        if nodo.procesado:
            return self._limpiar_rec(nodo.siguiente)
        nodo.siguiente = self._limpiar_rec(nodo.siguiente)
        if nodo.siguiente:
            nodo.siguiente.anterior = nodo               # ← actualizar anterior
        return nodo

    # ─── MOSTRAR ─────────────────────────────────────────────────────────────
    def mostrar(self):
        actual = self.inicio
        if actual is None:
            print("Lista vacía")
            return
        while actual:
            estado = "✓" if actual.procesado else "○"
            ant = actual.anterior.dato if actual.anterior else "None"
            sig = actual.siguiente.dato if actual.siguiente else "None"
            print(f"[{estado}] {actual.dato} | ant:{ant} | sig:{sig}")
            actual = actual.siguiente


# ══════════════════════════════════════════════════════════════════════════════
#              REFERENCIA RÁPIDA — TODOS LOS MÉTODOS Y SUS PATRONES
# ══════════════════════════════════════════════════════════════════════════════
"""
MÉTODO                  MODIFICA ORIGINAL?   CASO BASE      PATRÓN
──────────────────────────────────────────────────────────────────────
limpiar_completadas()   SÍ → self.inicio =   return None    Eliminar
limpiar_agregados()     SÍ → self.inicio =   return None    Eliminar
eliminar_inactivos()    SÍ → self.inicio =   return None    Eliminar

obtener_caros()         NO → return          return lista   Filtrar
obtener_urgentes()      NO → return          return lista   Filtrar
obtener_elite()         NO → return          return lista   Filtrar

contar_pendientes()     NO → return          return 0       Contar
calcular_total()        NO → return          return 0       Sumar
"""


# ══════════════════════════════════════════════════════════════════════════════
#                     EJEMPLO COMPLETO — SISTEMA DE TAREAS
# ══════════════════════════════════════════════════════════════════════════════

class Tarea:
    def __init__(self, descripcion, prioridad):
        self.descripcion = descripcion
        self.prioridad = prioridad      # 1 (baja) a 5 (urgente)
        self.completada = False
        self.siguiente = None

class ListaTareas:
    def __init__(self):
        self.inicio = None

    def agregar(self, descripcion, prioridad):
        nueva_tarea = Tarea(descripcion, prioridad)
        if self.inicio is None or self.inicio.prioridad < prioridad:
            nueva_tarea.siguiente = self.inicio
            self.inicio = nueva_tarea
        else:
            self._agregar_recursivo(self.inicio, nueva_tarea)

    def _agregar_recursivo(self, nodo_actual, nueva_tarea):
        if nodo_actual.siguiente is None or nodo_actual.siguiente.prioridad < nueva_tarea.prioridad:
            nueva_tarea.siguiente = nodo_actual.siguiente
            nodo_actual.siguiente = nueva_tarea
        else:
            self._agregar_recursivo(nodo_actual.siguiente, nueva_tarea)

    def contar_pendientes(self, prioridad):
        return self._contar_pendientes_recursivo(self.inicio, prioridad)

    def _contar_pendientes_recursivo(self, nodo, prioridad):
        if nodo is None:
            return 0
        cuenta = 1 if nodo.prioridad == prioridad and not nodo.completada else 0
        return cuenta + self._contar_pendientes_recursivo(nodo.siguiente, prioridad)

    def obtener_urgentes(self):
        nueva_lista = ListaTareas()
        return self._obtener_urgentes_recursivo(self.inicio, nueva_lista)

    def _obtener_urgentes_recursivo(self, nodo, nueva_lista):
        if nodo is None:
            return nueva_lista
        if nodo.prioridad >= 4 and not nodo.completada:
            nueva_lista.agregar(nodo.descripcion, nodo.prioridad)
        return self._obtener_urgentes_recursivo(nodo.siguiente, nueva_lista)

    def limpiar_completadas(self):
        self.inicio = self._limpiar_completadas_recursivo(self.inicio)

    def _limpiar_completadas_recursivo(self, nodo):
        if nodo is None:
            return None
        if nodo.completada:
            return self._limpiar_completadas_recursivo(nodo.siguiente)
        nodo.siguiente = self._limpiar_completadas_recursivo(nodo.siguiente)
        return nodo

    def completar(self, descripcion):
        actual = self.inicio
        while actual:
            if actual.descripcion == descripcion:
                actual.completada = True
                return
            actual = actual.siguiente

    def mostrar(self):
        actual = self.inicio
        if actual is None:
            print("Lista de tareas vacía")
            return
        while actual:
            estado = "✓" if actual.completada else "○"
            print(f"[{estado}] {actual.descripcion} (Prioridad: {actual.prioridad})")
            actual = actual.siguiente


# ══════════════════════════════════════════════════════════════════════════════
#                     EJEMPLO COMPLETO — CARRITO DE COMPRAS
# ══════════════════════════════════════════════════════════════════════════════

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.agregado = False
        self.siguiente = None

class Carrito:
    def __init__(self):
        self.inicio = None

    def agregar_producto(self, nombre, precio, cantidad):
        nuevo = Producto(nombre, precio, cantidad)
        if self.inicio is None or self.inicio.precio < nuevo.precio:
            nuevo.siguiente = self.inicio
            self.inicio = nuevo
        else:
            self._agregar_producto(self.inicio, nuevo)

    def _agregar_producto(self, nodo, nuevo):
        if nodo.siguiente is None or nodo.siguiente.precio < nuevo.precio:
            nuevo.siguiente = nodo.siguiente
            nodo.siguiente = nuevo
        else:
            self._agregar_producto(nodo.siguiente, nuevo)

    def calcular_total(self):
        return self._calcular_total_rec(self.inicio)

    def _calcular_total_rec(self, nodo):
        if nodo is None:
            return 0
        return (nodo.precio * nodo.cantidad) + self._calcular_total_rec(nodo.siguiente)

    def obtener_caros(self, maximo):
        nueva_lista = Carrito()
        return self._obtener_caros(self.inicio, nueva_lista, maximo)

    def _obtener_caros(self, nodo, lista, maximo):
        if nodo is None:
            return lista
        if nodo.precio > maximo and not nodo.agregado:
            lista.agregar_producto(nodo.nombre, nodo.precio, nodo.cantidad)
        return self._obtener_caros(nodo.siguiente, lista, maximo)

    def limpiar_agregados(self):
        self.inicio = self._limpiar_rec(self.inicio)

    def _limpiar_rec(self, nodo):
        if nodo is None:
            return None
        if nodo.agregado:
            return self._limpiar_rec(nodo.siguiente)
        nodo.siguiente = self._limpiar_rec(nodo.siguiente)
        return nodo

    def marcar_agregado(self, nombre):
        actual = self.inicio
        while actual:
            if actual.nombre == nombre:
                actual.agregado = True
                return
            actual = actual.siguiente

    def mostrar(self):
        actual = self.inicio
        if actual is None:
            print("Carrito vacío")
            return
        while actual:
            estado = "✓" if actual.agregado else "○"
            print(f"[{estado}] {actual.nombre} | ${actual.precio:,} | x{actual.cantidad}")
            actual = actual.siguiente


# ══════════════════════════════════════════════════════════════════════════════
#              EJEMPLO COMPLETO — BIBLIOTECA MUSICAL (DOBLE LIGADA)
# ══════════════════════════════════════════════════════════════════════════════

class Cancion:
    def __init__(self, titulo, artista, reproducciones):
        self.titulo = titulo
        self.artista = artista
        self.reproducciones = reproducciones
        self.favorita = False
        self.siguiente = None
        self.anterior = None

class Biblioteca:
    def __init__(self):
        self.inicio = None

    def agregar(self, titulo, artista, reproducciones):
        nueva = Cancion(titulo, artista, reproducciones)
        if self.inicio is None or self.inicio.reproducciones < nueva.reproducciones:
            nueva.siguiente = self.inicio
            if self.inicio:
                self.inicio.anterior = nueva
            self.inicio = nueva
        else:
            self._agregar_rec(self.inicio, nueva)

    def _agregar_rec(self, nodo, nueva):
        if nodo.siguiente is None or nodo.siguiente.reproducciones < nueva.reproducciones:
            nueva.siguiente = nodo.siguiente
            nueva.anterior = nodo
            if nodo.siguiente:
                nodo.siguiente.anterior = nueva
            nodo.siguiente = nueva
        else:
            self._agregar_rec(nodo.siguiente, nueva)

    def contar_no_favoritas(self, artista):
        return self._contar_rec(self.inicio, artista)

    def _contar_rec(self, nodo, artista):
        if nodo is None:
            return 0
        cuenta = 1 if nodo.artista == artista and not nodo.favorita else 0
        return cuenta + self._contar_rec(nodo.siguiente, artista)

    def obtener_populares(self, minimo):
        nueva = Biblioteca()
        return self._populares_rec(self.inicio, nueva, minimo)

    def _populares_rec(self, nodo, lista, minimo):
        if nodo is None:
            return lista
        if nodo.reproducciones > minimo and not nodo.favorita:
            lista.agregar(nodo.titulo, nodo.artista, nodo.reproducciones)
        return self._populares_rec(nodo.siguiente, lista, minimo)

    def limpiar_favoritas(self):
        self.inicio = self._limpiar_rec(self.inicio)
        if self.inicio:
            self.inicio.anterior = None

    def _limpiar_rec(self, nodo):
        if nodo is None:
            return None
        if nodo.favorita:
            return self._limpiar_rec(nodo.siguiente)
        nodo.siguiente = self._limpiar_rec(nodo.siguiente)
        if nodo.siguiente:
            nodo.siguiente.anterior = nodo
        return nodo

    def marcar_favorita(self, titulo):
        actual = self.inicio
        while actual:
            if actual.titulo == titulo:
                actual.favorita = True
                return
            actual = actual.siguiente

    def mostrar(self):
        actual = self.inicio
        if actual is None:
            print("Biblioteca vacía")
            return
        while actual:
            estado = "✓" if actual.favorita else "○"
            print(f"[{estado}] {actual.titulo} | {actual.artista} | {actual.reproducciones} rep")
            actual = actual.siguiente


# ══════════════════════════════════════════════════════════════════════════════
#                              PRUEBAS DE TODO
# ══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":

    print("=" * 60)
    print("           PRUEBA — LISTA DE TAREAS")
    print("=" * 60)
    lista = ListaTareas()
    lista.agregar("Tarea urgente", 5)
    lista.agregar("Tarea baja", 1)
    lista.agregar("Tarea media", 3)
    lista.agregar("Otra urgente", 5)
    lista.mostrar()
    print(f"Pendientes prioridad 5: {lista.contar_pendientes(5)}")
    lista.completar("Tarea urgente")
    print("\nUrgentes sin completar:")
    lista.obtener_urgentes().mostrar()
    lista.limpiar_completadas()
    print("\nDespués de limpiar completadas:")
    lista.mostrar()

    print("\n" + "=" * 60)
    print("           PRUEBA — CARRITO DE COMPRAS")
    print("=" * 60)
    carrito = Carrito()
    carrito.agregar_producto("Jabon", 1000, 1)
    carrito.agregar_producto("Shampoo", 12000, 2)
    carrito.agregar_producto("Acondicionador", 23000, 1)
    carrito.mostrar()
    print(f"Total: ${carrito.calcular_total():,}")
    carrito.marcar_agregado("Acondicionador")
    print("\nCaros (> $10000) no agregados:")
    carrito.obtener_caros(10000).mostrar()
    carrito.limpiar_agregados()
    print("\nDespués de limpiar agregados:")
    carrito.mostrar()

    print("\n" + "=" * 60)
    print("        PRUEBA — BIBLIOTECA (DOBLE LIGADA)")
    print("=" * 60)
    b = Biblioteca()
    b.agregar("Cancion A", "Artista 1", 1000)
    b.agregar("Cancion B", "Artista 2", 300)
    b.agregar("Cancion C", "Artista 1", 750)
    b.mostrar()
    print(f"No favoritas de Artista 1: {b.contar_no_favoritas('Artista 1')}")
    b.marcar_favorita("Cancion A")
    print("\nPopulares (> 400 rep) no favoritas:")
    b.obtener_populares(400).mostrar()
    b.limpiar_favoritas()
    print("\nDespués de limpiar favoritas:")
    b.mostrar()
