import re
 
# =============================================================================
# PARCIAL DE PYTHON
# =============================================================================
 
 
# =============================================================================
# 1. EXPRESIONES REGULARES AVANZADAS (20 pts)
#    Analizador de logs de servidor web
#
#    Línea de log real:
#    192.168.1.5 - - [10/Apr/2026:14:32:00] "GET /index.html HTTP/1.1" 200 1024
# =============================================================================
 
def parsear_log(linea):
    """
    Extrae de una línea de log:
      - ip:      string con la IP
      - metodo:  GET, POST, etc.
      - ruta:    /index.html, /api/users, etc.
      - codigo:  int con el código HTTP (200, 404, etc.)
      - bytes_:  int con los bytes transferidos
 
    Retorna un dict o None si no hace match.
 
    Ejemplo:
      parsear_log('192.168.1.5 - - [10/Apr/2026] "GET /api HTTP/1.1" 404 512')
      -> {'ip':'192.168.1.5','metodo':'GET','ruta':'/api','codigo':404,'bytes_':512}
    """
    patron = (
        r'(\d+\.\d+\.\d+\.\d+)'   # IP
        r'.+?"(\w+)\s(\S+)\sHTTP'  # método y ruta
        r'.+?"\s(\d{3})\s(\d+)'    # código y bytes
    )
    m = re.search(patron, linea)
    if not m:
        return None
    return {
        'ip':      m.group(1),
        'metodo':  m.group(2),
        'ruta':    m.group(3),
        'codigo':  int(m.group(4)),
        'bytes_':  int(m.group(5)),
    }
 
 
def contar_errores(logs):
    """
    Dado una lista de líneas de log, retorna cuántas
    tienen código HTTP >= 400 (errores del cliente/servidor).
    """
    return sum(
        1 for l in logs
        if (p := parsear_log(l)) and p['codigo'] >= 400
    )
 
 
# =============================================================================
# 2. LISTA DOBLEMENTE ENLAZADA (35 pts)
#    Historial de navegación
#    Cada nodo tiene puntero siguiente y anterior.
#    OBLIGATORIO: implementar con recursividad.
# =============================================================================
 
class Pagina:
    def __init__(self, url, tiempo):
        self.url       = url
        self.tiempo    = tiempo  # segundos en la página
        self.siguiente = None
        self.anterior  = None
 
 
class Historial:
    def __init__(self):
        self.cabeza = None
        self.cola   = None
 
    def agregar_al_final(self, url, tiempo):
        """Agrega al final. OBLIGATORIO recursividad."""
        nuevo = Pagina(url, tiempo)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo
            return
 
        def _ir_al_final(nodo):
            if nodo.siguiente is None:
                nodo.siguiente  = nuevo
                nuevo.anterior  = nodo
                self.cola       = nuevo
                return
            _ir_al_final(nodo.siguiente)
 
        _ir_al_final(self.cabeza)
 
    def tiempo_total(self):
        """Suma tiempo de todos los nodos. RECURSIVO."""
        def _suma(nodo):
            if nodo is None:
                return 0
            return nodo.tiempo + _suma(nodo.siguiente)
 
        return _suma(self.cabeza)
 
    def buscar(self, url):
        """
        Retorna el nodo con esa URL o None.
        Busca desde cabeza y también desde cola simultáneamente.
        RECURSIVO.
        """
        def _buscar(nodo):
            if nodo is None:
                return None
            if nodo.url == url:
                return nodo
            return _buscar(nodo.siguiente)
 
        return _buscar(self.cabeza)
 
    def eliminar(self, url):
        """
        Elimina el nodo con esa URL.
        Debe actualizar punteros anterior/siguiente.
        RECURSIVO.
        """
        def _elim(nodo):
            if nodo is None:
                return
            if nodo.url == url:
                if nodo.anterior:
                    nodo.anterior.siguiente = nodo.siguiente
                else:
                    self.cabeza = nodo.siguiente
                if nodo.siguiente:
                    nodo.siguiente.anterior = nodo.anterior
                else:
                    self.cola = nodo.anterior
                return
            _elim(nodo.siguiente)
 
        _elim(self.cabeza)
 
 
# =============================================================================
# 3. SETS — ANÁLISIS DE VENTAS (15 pts)
# =============================================================================
 
enero   = {"Alba", "Bruno", "Clara", "Diego", "Eva"}
febrero = {"Bruno", "Clara", "Fran", "Gema"}
marzo   = {"Clara", "Diego", "Gema", "Hugo"}
 
# a) Clientes que compraron los 3 meses (fieles)
fieles = enero & febrero & marzo
# -> {'Clara'}
 
# b) Clientes que compraron exactamente en 2 meses
dos_meses = ((enero & febrero) | (enero & marzo) | (febrero & marzo)) - fieles
# -> {'Bruno', 'Diego', 'Gema'}
 
# c) Clientes nuevos en marzo (no compraron en enero ni febrero)
nuevos_marzo = marzo - enero - febrero
# -> {'Hugo'}
 
# d) ¿Qué % de clientes totales son fieles (3 meses)?
todos      = enero | febrero | marzo
porcentaje = len(fieles) / len(todos) * 100
# -> 12.5%