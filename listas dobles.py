# ============================================================================
# CLASE NODO - La unidad básica de la lista doblemente ligada
# ============================================================================
class Nodo:
    """
    Representa un nodo en la lista doblemente ligada.
    Cada nodo contiene un dato y dos referencias: siguiente y anterior.
    """
    def __init__(self, dato):
        # Almacena el valor/dato que queremos guardar en el nodo
        self.dato = dato
        
        # Referencia al siguiente nodo (hacia la derecha en la lista)
        # Inicialmente es None porque no hay siguiente nodo aún
        self.siguiente = None
        
        # Referencia al nodo anterior (hacia la izquierda en la lista)
        # Inicialmente es None porque no hay nodo anterior aún
        self.anterior = None

# ============================================================================
# CLASE LISTA DOBLEMENTE LIGADA - Estructura de datos para manejo de nodos
# ============================================================================
class ListaDoblementeLigada:
    """
    Una lista que permite navegación bidireccional.
    Puedes moverte hacia adelante Y hacia atrás.
    """
    
    def __init__(self):
        # Inicializar la cabeza (primer nodo) como None porque la lista está vacía
        # Cuando insertemos el primer elemento, cabeza apuntará a ese nodo
        self.cabeza = None
    
    # ========================================================================
    # MÉTODO: Insertar al inicio de la lista
    # ========================================================================
    def insertar_inicio(self, dato):
        """
        Inserta un nuevo nodo al INICIO de la lista.
        El nuevo nodo se convierte en la nueva cabeza.
        
        Ejemplo: Si la lista es [5, 10, 15]
                 Al insertar 3 al inicio, queda [3, 5, 10, 15]
        """
        # Crear un nuevo nodo con el dato proporcionado
        nuevo = Nodo(dato)
        
        # CASO 1: Si la lista está vacía (cabeza es None)
        if self.cabeza is None:
            # El nuevo nodo se convierte en el primer nodo
            self.cabeza = nuevo
        # CASO 2: Si la lista ya tiene elementos
        else:
            # El nuevo nodo apunta al actual primer nodo (cabeza)
            nuevo.siguiente = self.cabeza
            
            # El actual primer nodo apunta hacia atrás al nuevo nodo
            self.cabeza.anterior = nuevo
            
            # Actualizar la cabeza para que sea el nuevo nodo
            self.cabeza = nuevo
    
    # ========================================================================
    # MÉTODO: Insertar al final de la lista
    # ========================================================================
    def insertar_final(self, dato):
        """
        Inserta un nuevo nodo al FINAL de la lista.
        
        Ejemplo: Si la lista es [5, 10, 15]
                 Al insertar 20 al final, queda [5, 10, 15, 20]
        """
        # Crear un nuevo nodo con el dato proporcionado
        nuevo = Nodo(dato)
        
        # CASO 1: Si la lista está vacía (cabeza es None)
        if self.cabeza is None:
            # El nuevo nodo se convierte en el primer nodo
            self.cabeza = nuevo
        # CASO 2: Si la lista ya tiene elementos
        else:
            # Variable para recorrer la lista desde el inicio
            actual = self.cabeza
            
            # Recorrer hasta encontrar el último nodo
            # El último nodo es el que tiene siguiente = None
            while actual.siguiente:
                actual = actual.siguiente
            
            # El último nodo apunta al nuevo nodo
            actual.siguiente = nuevo
            
            # El nuevo nodo apunta hacia atrás al anterior último nodo
            nuevo.anterior = actual
    
    # ========================================================================
    # MÉTODO: Mostrar la lista hacia ADELANTE (de inicio a final)
    # ========================================================================
    def mostrar_adelante(self):
        """
        Recorre la lista desde el inicio hacia el final.
        Muestra todos los elementos en orden.
        
        Ejemplo: Si la lista es [5, 10, 20]
                 Imprime: 5 <-> 10 <-> 20 <-> None
        """
        # Empezar desde la cabeza (primer nodo)
        actual = self.cabeza
        
        # Recorrer mientras haya nodos (mientras actual no sea None)
        while actual:
            # Imprimir el dato del nodo actual
            print(actual.dato, end=" <-> ")
            
            # Avanzar al siguiente nodo
            actual = actual.siguiente
        
        # Al final, indicar que la lista terminó
        print("None")

    # ========================================================================
    # MÉTODO: Mostrar la lista hacia ATRÁS (de final a inicio)
    # ========================================================================
    def mostrar_atras(self):
        """
        Recorre la lista desde el final hacia el inicio.
        Esto demuestra la característica de lista DOBLEMENTE ligada.
        
        Ejemplo: Si la lista es [5, 10, 20]
                 Imprime: 20 <-> 10 <-> 5 <-> None
        """
        # Empezar desde la cabeza
        actual = self.cabeza
        
        # Si la lista está vacía, mostrar mensaje y salir
        if actual is None:
            print("La lista está vacía.")
            return
        
        # Recorrer hacia adelante hasta encontrar el último nodo
        # El último nodo tiene siguiente = None
        while actual.siguiente:
            actual = actual.siguiente
        
        # Ahora 'actual' apunta al último nodo
        # Recorrer hacia atrás usando la referencia anterior
        while actual:
            # Imprimir el dato del nodo actual
            print(actual.dato, end=" <-> ")
            
            # Retroceder al nodo anterior
            actual = actual.anterior
        
        # Al final, indicar que la lista terminó
        print("None")



# ============================================================================
# SECCIÓN DE PRUEBA - Demostración del funcionamiento
# ============================================================================

# Crear una nueva lista doblemente ligada vacía
lista = ListaDoblementeLigada()

# --- Paso 1: Insertar elementos al inicio ---
# insertar_inicio(10) -> Lista: [10]
lista.insertar_inicio("vallenato")
# insertar_inicio(5) -> Lista: [5, 10]
lista.insertar_inicio("carranga")

# --- Paso 2: Insertar elementos al final ---
# insertar_final(20) -> Lista: [5, 10, 20]
lista.insertar_final("rock")
# insertar_final(30) -> Lista: [5, 10, 20, 30]
lista.insertar_final("pop")

# --- Paso 3: Mostrar la lista de adelante hacia atrás ---
print("Recorrido hacia adelante:")
print("(De izquierda a derecha, del inicio al final)")
lista.mostrar_adelante()

# --- Paso 4: Mostrar la lista de atrás hacia adelante ---
print("\nRecorrido hacia atrás:")
print("(De derecha a izquierda, del final al inicio)")
print("Esto demuestra que es DOBLEMENTE ligada (puedes ir en ambas direcciones)")
lista.mostrar_atras()
        
