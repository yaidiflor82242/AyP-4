import re

def validar_correo(correo):
    """
    Valida si un correo electrónico tiene formato básico válido.
    Formato: texto@texto.texto
    
    validar_correo("usuario@gmail.com")  -> True
    validar_correo("user.name@uni.edu.co") -> True
    validar_correo("sinArroba.com")  -> False
    validar_correo("@sinusuario.com") -> False
    """
    patron = r'^[\w\.\+\-]+@[\w\-]+\.[\w\.\-]+$'
    return bool(re.match(patron, correo))
    # TODO: implementar
    pass

def extraer_menciones(texto):
    """
    Extrae todas las menciones (@usuario) de un texto.
    Una mención: @ seguido de letras, números o guion bajo.
    
    extraer_menciones("Hola @juan y @maria_99, cc @bot3")
    -> ["@juan", "@maria_99", "@bot3"]
    """
    return re.findall(r'@\w+', texto)
    # TODO: implementar con re.findall
    pass


"""Sistema de inventario de una tienda. Cada producto tiene nombre, precio y si está en oferta. Implementa los métodos usando recursividad obligatoriamente."""

class Producto:
    def __init__(self, nombre, precio, en_oferta=False):
        self.nombre = nombre
        self.precio = precio
        self.en_oferta = en_oferta
        self.siguiente = None

class ListaInventario:
    def agregar(self, nombre, precio):
        """Agrega al FINAL. OBLIGATORIO recursividad."""
        pass

    nuevo = Producto(nombre, precio)
    self.cabeza = self._agregar_rec(self.cabeza, nuevo)

    def _agregar_rec(self, nodo, nuevo):
        if nodo is None:   # caso base: llegué al final
            return nuevo
        nodo.siguiente = self._agregar_rec(nodo.siguiente, nuevo)
        return nodo


    def precio_total_oferta(self):
        """Suma precios de productos EN oferta. Recursivo."""
        pass
        return self._precio_rec(self.cabeza)
    
    def _precio_rec(self, nodo):
        if nodo is None: return 0   # caso base
        if nodo.en_oferta:
            return nodo.precio + self._precio_rec(nodo.siguiente)
        return self._precio_rec(nodo.siguiente)

    def contar_productos(self):
        """Retorna cuántos productos hay en la lista. Recursivo."""
        pass
        return self._contar_rec(self.cabeza)
    
    def _contar_rec(self, nodo):
        if nodo is None: return 0   # caso base
        return 1 + self._contar_rec(nodo.siguiente)
    
    sistemas   = {"Laura", "Pedro", "Sofia", "Tomas", "Valeria"}
    marketing  = {"Pedro", "Valeria", "Ximena", "Yuri"}
    finanzas   = {"Laura", "Sofia", "Ximena", "Zoe"}

    def en_dos_o_mas():
        """Empleados que están en al menos 2 departamentos."""
        pass
        en_sis_mkt = sistemas & marketing
        en_sis_fin = sistemas & finanzas
        en_mkt_fin = marketing & finanzas
        return en_sis_mkt | en_sis_fin | en_mkt_fin


    def solo_sistemas():
        """Empleados únicamente en sistemas, no en otros."""
        pass
        return sistemas - (marketing | finanzas)

    def todos_los_empleados():
        """Todos los empleados sin repetir."""
        pass
        return sistemas | marketing | finanzas


    """Tienes una cuadrícula de N×N. Solo puedes moverte hacia la derecha o hacia abajo. ¿De cuántas formas puedes ir desde la esquina (0,0) hasta (N-1, N-1)?"""   

# Ejemplo:
# N=2: 2 formas → [derecha-abajo, abajo-derecha]
# N=3: 6 formas

    def caminos_sin_memo(n):
        """Recursividad pura, sin memoización."""
        pass
        if n == 1: return 1
        return caminos_sin_memo(n - 1) + caminos_sin_memo(n - 1)


    def caminos_con_memo(n, memo=None):
        """Misma función con memoización."""
        if memo is None:
            memo = {}
        if n in memo:
            return memo[n]
        if n == 1:
            return 1
        memo[n] = caminos_con_memo(n - 1, memo) + caminos_con_memo(n - 1, memo)
        return memo[n]