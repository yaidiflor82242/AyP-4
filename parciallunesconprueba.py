import re

# ==================== PUNTO 1 (20%) ====================
def validar_placa_vehiculo(placa):
    return bool(re.match(r'^[A-Z]{3}-?\d{3}$', placa))

def extraer_hashtags(texto):
    return re.findall(r'#\w+', texto)

# ==================== PUNTO 2 (30%) ====================
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

    def _agregar_rec(self, nodo, nuevo):
        if nodo.siguiente is None:
            nodo.siguiente = nuevo
        else:
            self._agregar_rec(nodo.siguiente, nuevo)

    def _valor_pendiente_rec(self, nodo):
        if nodo is None:
            return 0
        valor_actual = nodo.valor if not nodo.entregado else 0
        return valor_actual + self._valor_pendiente_rec(nodo.siguiente)

    def _eliminar_entregados_rec(self, nodo):
        if nodo is None:
            return None
        nodo.siguiente = self._eliminar_entregados_rec(nodo.siguiente)
        if nodo.entregado:
            return nodo.siguiente
        return nodo

    def agregar(self, cliente, direccion, valor):
        nuevo = Pedido(cliente, direccion, valor)
        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            self._agregar_rec(self.cabeza, nuevo)

    def valor_pendiente(self):
        return self._valor_pendiente_rec(self.cabeza)

    def eliminar_entregados(self):
        self.cabeza = self._eliminar_entregados_rec(self.cabeza)

# ==================== PUNTO 3 (20%) ====================
club_ciencias  = {"Ana", "Carlos", "Diana", "Elena", "Felipe"}
club_deportes  = {"Carlos", "Felipe", "Gabriel", "Hugo", "Isabel"}
club_arte      = {"Ana", "Diana", "Gabriel", "Julia", "Karen"}

def estudiantes_en_todos():
    return club_ciencias & club_deportes & club_arte

def solo_un_club():
    solo_ciencias = club_ciencias  - club_deportes - club_arte
    solo_deportes = club_deportes  - club_ciencias  - club_arte
    solo_arte     = club_arte      - club_ciencias  - club_deportes
    return solo_ciencias | solo_deportes | solo_arte

def clubes_de_estudiante(nombre):
    clubes = []
    if nombre in club_ciencias:  clubes.append("Ciencias")
    if nombre in club_deportes:  clubes.append("Deportes")
    if nombre in club_arte:      clubes.append("Arte")
    return clubes

# ==================== PUNTO 4 (30%) ====================
def escalones_sin_memo(n):
    if n == 0: return 1
    if n == 1: return 1
    return escalones_sin_memo(n - 1) + escalones_sin_memo(n - 2)

def escalones_con_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n == 0: return 1
    if n == 1: return 1
    if n not in memo:
        memo[n] = escalones_con_memo(n - 1, memo) + escalones_con_memo(n - 2, memo)
    return memo[n]


# ═══════════════════════════════════════════════════════════════════════════════
# CÓDIGO DE PRUEBA - NO MODIFICAR
# ═══════════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":

    # ── Punto 1 ───────────────────────────────────────────────
    print("=" * 60)
    print("         PRUEBAS PUNTO 1 - EXPRESIONES REGULARES")
    print("=" * 60)

    print("\n🚗 Validación de placas:")
    print("  validar_placa_vehiculo('ABC123')  ->", validar_placa_vehiculo("ABC123"))
    print("  Esperado: True")
    print("  validar_placa_vehiculo('ABC-123') ->", validar_placa_vehiculo("ABC-123"))
    print("  Esperado: True")
    print("  validar_placa_vehiculo('AB1234')  ->", validar_placa_vehiculo("AB1234"))
    print("  Esperado: False")
    print("  validar_placa_vehiculo('abc123')  ->", validar_placa_vehiculo("abc123"))
    print("  Esperado: False")

    print("\n#️⃣  Extracción de hashtags:")
    texto = "Hola #python es #genial y #100dias de código"
    print(f"  texto: '{texto}'")
    print("  extraer_hashtags(texto) ->", extraer_hashtags(texto))
    print("  Esperado: ['#python', '#genial', '#100dias']")

    # ── Punto 2 ───────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("         PRUEBAS PUNTO 2 - LISTA DE PEDIDOS")
    print("=" * 60)

    pedidos = ListaPedidos()
    pedidos.agregar("Ana",   "Calle 1", 25000)
    pedidos.agregar("Luis",  "Calle 2", 30000)
    pedidos.agregar("María", "Calle 3", 15000)

    print("\n📦 Lista de pedidos inicial:")
    pedidos.mostrar()

    print("\n💰 Valor total pendiente:", pedidos.valor_pendiente())
    print("   Esperado: 45000")

    pedidos.cabeza.entregado = True              # Ana entregada
    print("\n✓ Después de entregar a Ana:")
    print("   Valor pendiente:", pedidos.valor_pendiente())
    print("   Esperado: 45000")

    pedidos.cabeza.siguiente.entregado = True    # Luis entregado
    print("\n✓ Después de entregar a Luis:")
    print("   Valor pendiente:", pedidos.valor_pendiente())
    print("   Esperado: 15000")

    print("\n🗑️  Eliminando pedidos entregados...")
    pedidos.eliminar_entregados()
    print("   Lista resultante:")
    pedidos.mostrar()
    print("   Esperado: solo María")

    # ── Punto 3 ───────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("         PRUEBAS PUNTO 3 - CLUBES")
    print("=" * 60)

    print("\n🎯 Estudiantes en los 3 clubes:", estudiantes_en_todos())
    print("   Esperado: set() (nadie está en los 3)")

    print("\n🎯 Estudiantes en exactamente un club:", solo_un_club())
    print("   Esperado: {'Elena', 'Hugo', 'Isabel', 'Julia', 'Karen'}")

    print("\n🎯 Clubes de Carlos:", clubes_de_estudiante("Carlos"))
    print("   Esperado: ['Ciencias', 'Deportes']")

    print("\n🎯 Clubes de Julia:", clubes_de_estudiante("Julia"))
    print("   Esperado: ['Arte']")

    print("\n🎯 Clubes de Ana:", clubes_de_estudiante("Ana"))
    print("   Esperado: ['Ciencias', 'Arte']")

    # ── Punto 4 ───────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("         PRUEBAS PUNTO 4 - ESCALONES")
    print("=" * 60)

    print("\n🪜 Escalones sin memo:")
    for n, esp in [(1,1),(2,2),(3,3),(4,5),(5,8)]:
        print(f"  escalones_sin_memo({n}) -> {escalones_sin_memo(n)}   Esperado: {esp}")

    print("\n🪜 Escalones con memo:")
    for n, esp in [(1,1),(2,2),(3,3),(4,5),(5,8),(10,89),(30,1346269)]:
        print(f"  escalones_con_memo({n}) -> {escalones_con_memo(n)}   Esperado: {esp}")