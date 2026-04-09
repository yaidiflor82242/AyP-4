import re

# re.match() → busca el patrón desde el INICIO del string
# re.search() → busca el patrón EN CUALQUIER PARTE
# re.findall() → retorna TODOS los matches como lista
""" 
    Valida si una placa de vehículo colombiana tiene formato correcto. 
     
    Formato válido: 3 letras mayúsculas + 3 dígitos (ej: ABC123) 
    También válido con guion: ABC-123 
     
    Ejemplos: 
        validar_placa_vehiculo("ABC123") -> True 
        validar_placa_vehiculo("ABC-123") -> True 
        validar_placa_vehiculo("AB1234") -> False 
        validar_placa_vehiculo("abc123") -> False 
    """ 
def validar_placa_vehiculo(placa):
    # ^        → inicio del string
    # [A-Z]{3} → exactamente 3 letras mayúsculas
    # -?       → guion opcional (el ? significa "0 o 1 vez")
    # [0-9]{3} → exactamente 3 dígitos
    # $        → fin del string
    patron = r'^[A-Z]{3}-?[0-9]{3}$'
    return bool(re.match(patron, placa))

""" 
    Extrae todos los hashtags de un texto. 
    Un hashtag empieza con # seguido de letras, números o guion bajo. 
     
    Ejemplo: 
        extraer_hashtags("Hola #python es #genial y #100dias") 
        -> ["#python", "#genial", "#100dias"] 
    """

def extraer_hashtags(texto):
    # #        → literal #
    # \w+      → una o más letras, números o guion bajo
    patron = r'#\w+'
    return re.findall(patron, texto)

"""Sistema de gestión de pedidos para un restaurante de domicilios. 
Cada pedido tiene: cliente, dirección, valor y si está entregado. 
Los pedidos se almacenan en una lista enlazada. 
""" 
 
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
            print("  Sin pedidos") 
            return 
        while actual: 
            print(f"  {actual}") 
            actual = actual.siguiente 
 
    """ 
        Agrega un nuevo pedido al FINAL de la lista. 
        OBLIGATORIO usar recursividad. 
        """ 
    def agregar(self, cliente, direccion, valor):
        nuevo = Pedido(cliente, direccion, valor)
        # Usamos helper recursivo que recibe el nodo actual
        self.cabeza = self._agregar_rec(self.cabeza, nuevo)
    
   
    def _agregar_rec(self, nodo, nuevo):
        if nodo is None:          # Caso base: llegamos al final
            return nuevo          # El nuevo nodo va aquí
        nodo.siguiente = self._agregar_rec(nodo.siguiente, nuevo)
        return nodo               # Retornamos el nodo actual intacto
    

    """ 
        Retorna la suma de valores de pedidos NO entregados. 
        OBLIGATORIO usar recursividad. 
         
        Ejemplo: 
            Pedido1 (entregado, $25000) + Pedido2 (pendiente, $30000)  
            + Pedido3 (pendiente, $15000) 
            -> Retorna 45000 
        """ 
    def valor_pendiente(self):
        return self._valor_rec(self.cabeza)
    
    def _valor_rec(self, nodo):
        if nodo is None:          # Caso base: no hay más nodos
            return 0
        # Si NO está entregado, sumo su valor + el resto de la lista
        if not nodo.entregado:
            return nodo.valor + self._valor_rec(nodo.siguiente)
        else:
            return self._valor_rec(nodo.siguiente)
        

    """ 
        Elimina todos los pedidos que ya fueron entregados. 
        OBLIGATORIO usar recursividad. 
        Modifica la lista original. 
        """ 
    def eliminar_entregados(self):
        self.cabeza = self._eliminar_rec(self.cabeza)
    
    def _eliminar_rec(self, nodo):
        if nodo is None:          # Caso base
            return None
        nodo.siguiente = self._eliminar_rec(nodo.siguiente)
        # Si este nodo está entregado, lo "saltamos" retornando su siguiente
        if nodo.entregado:
            return nodo.siguiente
        return nodo


    """Un colegio tiene 3 clubes extracurriculares. Cada club tiene un conjunto 
    de estudiantes inscritos. Responde las preguntas usando operaciones de conjuntos. 
    """ 
    
    club_ciencias = {"Ana", "Carlos", "Diana", "Elena", "Felipe"} 
    club_deportes = {"Carlos", "Felipe", "Gabriel", "Hugo", "Isabel"} 
    club_arte = {"Ana", "Diana", "Gabriel", "Julia", "Karen"}


    """ 
        Retorna el conjunto de estudiantes inscritos en LOS TRES clubes. 
        (Intersección de los tres) 
        """ 

    def estudiantes_en_todos():
        # Intersección: elementos que están en LOS TRES
        return club_ciencias & club_deportes & club_arte
        # Resultado: set() — nadie está en los 3

    """ 
        Retorna el conjunto de estudiantes que están en EXACTAMENTE un club. 
        
        Pista: Un estudiante está en exactamente un club si está en ese club 
        pero NO en los otros dos. 
        
        Ejemplo esperado: {"Elena", "Hugo", "Isabel", "Julia", "Karen"} 
        """ 

    def solo_un_club():
        # Está en ciencias pero NO en los otros dos:
        solo_ciencias  = club_ciencias  - club_deportes - club_arte
        solo_deportes  = club_deportes  - club_ciencias  - club_arte
        solo_arte      = club_arte      - club_ciencias  - club_deportes
        return solo_ciencias | solo_deportes | solo_arte
    
    """ 
    Retorna una lista con los nombres de los clubes a los que pertenece 
    el estudiante. 
     
    Ejemplo: 
        clubes_de_estudiante("Carlos") -> ["Ciencias", "Deportes"] 
        clubes_de_estudiante("Julia") -> ["Arte"] 
    """

    def clubes_de_estudiante(nombre):
        clubes = []
        if nombre in club_ciencias:  clubes.append("Ciencias")
        if nombre in club_deportes:  clubes.append("Deportes")
        if nombre in club_arte:      clubes.append("Arte")
        return clubes
    
    """Tienes una escalera de N escalones. En cada paso puedes subir 1 o 2 escalones. 
¿De cuántas formas distintas puedes llegar al escalón N? 
 
Ejemplo: 
    N=1: 1 forma  → [1] 
    N=2: 2 formas → [1+1, 2] 
    N=3: 3 formas → [1+1+1, 1+2, 2+1] 
    N=4: 5 formas → [1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2] 
""" 
def escalones_sin_memo(n): 
    """ 
    Calcula de cuántas formas se puede subir una escalera de n escalones. 
    En cada paso puedes subir 1 o 2 escalones. 
     
    Implementar con recursividad pura (sin memorización). 
     
    Casos base: 
        n == 0 -> 1 (hay una forma de "no subir") 
        n == 1 -> 1 
     
    Caso recursivo: 
        escalones(n) = escalones(n-1) + escalones(n-2) 
    """ 
    def escalones_sin_memo(n):
    # Casos base
        if n == 0: return 1
        if n == 1: return 1
        # Caso recursivo
        return escalones_sin_memo(n-1) + escalones_sin_memo(n-2)
    # TODO: Implementar 
    pass 
 
def escalones_con_memo(n, memo=None): 
    """ 
    Misma función pero usando un diccionario para guardar resultados 
    ya calculados y evitar recalcular. 
     
    Ejemplo: 
        escalones_con_memo(10) -> 89 
        escalones_con_memo(30) -> 1346269  (sin memo esto tardaría mucho) 
    """ 
    def escalones_con_memo(n, memo=None):
        if memo is None:
            memo = {}              # Inicializar el diccionario
        if n == 0: return 1
        if n == 1: return 1
        if n in memo:
            return memo[n]         # ← Ya lo calculé antes, lo devuelvo directo
        resultado = escalones_con_memo(n-1, memo) + escalones_con_memo(n-2, memo)
        memo[n] = resultado        # ← Guardo antes de retornar
    return resultado
    # TODO: Implementar 
    pass 

    