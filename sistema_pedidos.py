"""Sistema de gestión de pedidos para un restaurante de domicilios.
Cada pedido tiene: cliente, dirección, valor y si está entregado.
Los pedidos se almacenan en una lista enlazada."""

class Pedido:
    def __init__(self, cliente, direccion, valor, entregado=False):
        self.cliente = cliente
        self.direccion = direccion
        self.valor = valor
        self.entregado = entregado
        self.siguiente = None
    def __str__(self):
        estado = "✓" if self.entregado else "○"
        return f"[{estado}] {self.cliente} - ${self.valor:,} - {self.direccion}"
    
class ListaPedidos:
    def __init__(self):
        self.cabeza = None
    def mostrar(self):
        actual = self.cabeza
        if actual is None:
            print(" Sin pedidos")
            return
        while actual:
            print(f" {actual}")
            actual = actual.siguiente    

    def agregar(self, cliente, direccion, valor):
        """
        Agrega un nuevo pedido al FINAL de la lista.
        OBLIGATORIO usar recursividad.
        """
        nuevo = Pedido(cliente, direccion, valor)

        def buscar_ultimo(nodo):
            # Si es el último nodo
            if nodo.siguiente is None:
                nodo.siguiente = nuevo
                return

            buscar_ultimo(nodo.siguiente)

        # Lista vacía
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            buscar_ultimo(self.cabeza)

    def valor_pendiente(self):
        """
        Retorna la suma de valores de pedidos NO entregados.
        OBLIGATORIO usar recursividad.

        Ejemplo:
        Pedido1 (entregado, $25000) + Pedido2 (pendiente, $30000)
        + Pedido3 (pendiente, $15000)
        -> Retorna 45000
        """
        def sumar_pendientes(nodo):
            if nodo is None:
                return 0
            
            if not nodo.entregado:
                return nodo.valor + sumar_pendientes(nodo.siguiente)
            else:
                return sumar_pendientes(nodo.siguiente)
        
        return sumar_pendientes(self.cabeza)
        # TODO: Implementar
        pass

    def eliminar_entregados(self):
        """
        Elimina todos los pedidos que ya fueron entregados.
        OBLIGATORIO usar recursividad.
        Modifica la lista original.
        """
        def eliminar_recursivo(nodo):
            if nodo is None:
                return None
            
            # Si está entregado → lo eliminamos
            if nodo.entregado:
                return eliminar_recursivo(nodo.siguiente)
            
            # Si NO está entregado → lo mantenemos
            nodo.siguiente = eliminar_recursivo(nodo.siguiente)
            return nodo
        
        self.cabeza = eliminar_recursivo(self.cabeza)
        # TODO: Implementar
        pass

# Crear la lista
lista = ListaPedidos()

# Agregar pedidos
lista.agregar("Juan", "Calle 10", 25000)
lista.agregar("Ana", "Carrera 50", 30000)
lista.agregar("Pedro", "Av 80", 15000)
lista.agregar("Luis", "Calle 30", 20000)

# Marcar algunos como entregados
lista.cabeza.entregado = True              # Juan
lista.cabeza.siguiente.siguiente.entregado = True  # Pedro

print("📦 LISTA ORIGINAL:")
lista.mostrar()
