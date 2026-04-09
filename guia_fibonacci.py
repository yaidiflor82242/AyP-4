"""
╔══════════════════════════════════════════════════════════════════╗
║         🎯 GUÍA MEMORIZACIÓN FIBONACCI Y CAMINOS                 ║
║                    VARIACIONES IMPORTANTES                      ║
╚══════════════════════════════════════════════════════════════════╝
"""

# ══════════════════════════════════════════════════════════════════
# 🎯 1. FIBONACCI CLÁSICO (MEMORIZAR BASE)
# ══════════════════════════════════════════════════════════════════

def fibonacci(n):
    """
    F(0)=0, F(1)=1
    F(n) = F(n-1) + F(n-2)
    
    0,1,1,2,3,5,8,13,21,34,55...
    """
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# RESULTADOS CLAVE (MEMORIZAR):
print("FIBONACCI:")
for i in range(11):
    print(f"F({i}) = {fibonacci(i)}")
# F(0)=0, F(1)=1, F(2)=1, F(3)=2, F(4)=3, F(5)=5, F(6)=8...

# ══════════════════════════════════════════════════════════════════
# 🎯 2. CAMINOS ESCALONES (1,2,3 PASOS)
# ══════════════════════════════════════════════════════════════════

def caminos_escalones(n):
    """
    Formas de subir n escalones con 1, 2 o 3 pasos
    C(n) = C(n-1) + C(n-2) + C(n-3)
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    return (caminos_escalones(n-1) + 
            caminos_escalones(n-2) + 
            caminos_escalones(n-3))

print("\nCAMINOS 1-2-3:")
for i in range(7):
    print(f"C({i}) = {caminos_escalones(i)}")
# C(0)=1, C(1)=1, C(2)=2, C(3)=4, C(4)=7, C(5)=13, C(6)=24

# ══════════════════════════════════════════════════════════════════
# 🎯 3. CAMINOS RESTRINGIDOS (NO 2 PASOS DE 2 SEGUIDOS)
# ══════════════════════════════════════════════════════════════════

def caminos_restringidos(n):
    """
    1 o 2 escalones, PERO NO DOS 2 SEGUIDOS
    
    DP: dp[i][0] = termina en 1
        dp[i][1] = termina en 2
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    dp = [[0, 0] for _ in range(n + 1)]
    dp[1][0] = 1  # termina en 1
    
    for i in range(2, n + 1):
        dp[i][0] = dp[i-1][0] + dp[i-1][1]  # termina en 1
        dp[i][1] = dp[i-2][0]               # termina en 2 (solo desde 1)
    
    return dp[n][0] + dp[n][1]

print("\nCAMINOS RESTRINGIDOS:")
for i in range(7):
    print(f"R({i}) = {caminos_restringidos(i)}")
# R(1)=1, R(2)=2, R(3)=3, R(4)=5, R(5)=6, R(6)=9

# ══════════════════════════════════════════════════════════════════
# 🎯 4. FORMAS SUMAR (PARTICIONES)
# ══════════════════════════════════════════════════════════════════

def formas_sumar(n):
    """
    Formas de sumar n con 1,2,3 (ORDEN NO IMPORTA)
    [1,2] == [2,1]
    """
    if n < 0:
        return 0
    if n == 0:
        return 1
    return formas_sumar(n-1) + formas_sumar(n-2) + formas_sumar(n-3)

print("\nFORMAS SUMAR:")
for i in range(7):
    print(f"S({i}) = {formas_sumar(i)}")
# S(0)=1, S(1)=1, S(2)=2, S(3)=2, S(4)=3, S(5)=4, S(6)=5

# ══════════════════════════════════════════════════════════════════
# 🎯 5. TABLA COMPARATIVA (MEMORIZAR)
# ══════════════════════════════════════════════════════════════════

print("\n" + "="*50)
print("📊 TABLA COMPARATIVA n=0...6")
print("="*50)
print("n | Fib | C123 | Rest | Sumar")
print("-" * 35)

for n in range(7):
    print(f"{n:2} | {fibonacci(n):3} | "
          f"{caminos_escalones(n):3} | "
          f"{caminos_restringidos(n):3} | "
          f"{formas_sumar(n):4}")

"""
0 |   0 |   1 |   0 |    1
1 |   1 |   1 |   1 |    1
2 |   1 |   2 |   2 |    2
3 |   2 |   4 |   3 |    2
4 |   3 |   7 |   5 |    3
5 |   5 |  13 |   6 |    4
6 |   8 |  24 |   9 |    5
"""

# ══════════════════════════════════════════════════════════════════
# 🎯 6. CASOS BASE SIEMPRE IGUALES (MEMORIZAR)
# ══════════════════════════════════════════════════════════════════

"""
TODOS LOS CASOS:

if n < 0: return 0
if n == 0: return 1  # hay 1 forma de no hacer nada
if n == 1: return 1  # solo 1 paso de 1

Luego: recursión según el problema
"""

# ══════════════════════════════════════════════════════════════════
# 🎯 7. OPTIMIZACIÓN DP (MEMORIZAR FÓRMULAS)
# ══════════════════════════════════════════════════════════════════

def fibonacci_dp(n):
    """Fibonacci O(n)"""
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def caminos_dp(n):
    """Caminos 1-2-3 O(n)"""
    if n == 0:
        return 1
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = dp[i-1] if i-1 >= 0 else 0
        dp[i] += dp[i-2] if i-2 >= 0 else 0
        dp[i] += dp[i-3] if i-3 >= 0 else 0
    return dp[n]

print("\n✅ OPTIMIZACIONES:")
print(f"Fibonacci DP(10): {fibonacci_dp(10)}")      # 55
print(f"Caminos DP(10): {caminos_dp(10)}")         # 274

# ══════════════════════════════════════════════════════════════════
# 🎯 8. RECURSIONES COMBINADAS (PARCIALES)
# ══════════════════════════════════════════════════════════════════

from functools import lru_cache

# =========================================
# 1. SIN MEMOIZACIÓN
# =========================================
def cambio_minimo(monedas, total):
    """
    MÍNIMO número de monedas para dar cambio (recursivo puro)
    """
    if total == 0:
        return 0
    if total < 0 or not monedas:
        return float('inf')
    
    incluir = 1 + cambio_minimo(monedas, total - monedas[0])
    excluir = cambio_minimo(monedas[1:], total)
    
    return min(incluir, excluir)


# =========================================
# 2. CON MEMOIZACIÓN (manual)
# =========================================
def cambio_minimo_memo(monedas, total, memo=None):
    if memo is None:
        memo = {}
    
    clave = (tuple(monedas), total)
    
    if clave in memo:
        return memo[clave]
    
    if total == 0:
        return 0
    if total < 0 or not monedas:
        return float('inf')
    
    incluir = 1 + cambio_minimo_memo(monedas, total - monedas[0], memo)
    excluir = cambio_minimo_memo(monedas[1:], total, memo)
    
    resultado = min(incluir, excluir)
    memo[clave] = resultado
    
    return resultado


# =========================================
# 3. CON LRU_CACHE
# =========================================
@lru_cache(maxsize=None)
def cambio_minimo_cache(monedas, total):
    if total == 0:
        return 0
    if total < 0 or len(monedas) == 0:
        return float('inf')
    
    incluir = 1 + cambio_minimo_cache(monedas, total - monedas[0])
    excluir = cambio_minimo_cache(monedas[1:], total)
    
    return min(incluir, excluir)


# =========================================
# PRUEBAS
# =========================================
if __name__ == "__main__":

    print("=== CAMBIO MÍNIMO SIN MEMO ===")
    print(cambio_minimo([1, 5, 10, 25], 36))  # 3
    print(cambio_minimo([1, 5, 10, 25], 49))  # 7 (25+10+10+1+1+1+1)
    print(cambio_minimo([1, 5, 10], 13))      # 4 (10+1+1+1)
    print(cambio_minimo([5, 10], 3))          # inf

    print("\n=== CON MEMOIZACIÓN ===")
    print(cambio_minimo_memo([1, 5, 10, 25], 36))  # 3

    print("\n=== CON LRU_CACHE ===")
    # 🔥 IMPORTANTE: usar tupla
    print(cambio_minimo_cache((1, 5, 10, 25), 36))  # 3
   
# ══════════════════════════════════════════════════════════════════
# 🎯 9. TABLA DE FORMULAS (IMPRIMIR)
# ══════════════════════════════════════════════════════════════════

FORMULAS = """
📊 FÓRMULAS DE MEMORIZACIÓN:

1. FIBONACCI:
   F(n) = F(n-1) + F(n-2)
   F(0)=0, F(1)=1

2. CAMINOS 1-2-3:
   C(n) = C(n-1) + C(n-2) + C(n-3)
   C(0)=1, C(1)=1

3. CAMINOS RESTRINGIDOS:
   R(n)[1] = R(n-1)[1] + R(n-1)[2]
   R(n)[2] = R(n-2)[1]
   Total = R(n)[1] + R(n)[2]

4. FORMAS SUMAR:
   S(n) = S(n-1) + S(n-2) + S(n-3)
   S(0)=1

5. CAMBIO MÍNIMO:
   min(1 + cambio(total-monedas[0]), cambio(total))
"""

print("\n" + "="*60)
print(FORMULAS)
print("="*60)

# ══════════════════════════════════════════════════════════════════
# 🎯 10. ERRORES COMUNES (NUNCA COMETER)
# ══════════════════════════════════════════════════════════════════

ERRORES = """
❌ 1. Olvidar n<0 → return 0
❌ 2. F(0)=1 en Fibonacci (es 0)
❌ 3. No manejar n=0 en caminos
❌ 4. Recursión sin memoización → TLE
❌ 5. Confundir orden importa/no importa
"""

print("⚠️ ERRORES FATALES:")
print(ERRORES)

print("\n" + "="*60)
print("✅ ¡FIBONACCI MEMORIZADO!")
print("🎓 Casos base: n<0=0, n=0=1, n=1=1")
print("🎓 Fibonacci: F(n-1)+F(n-2)")
print("🎓 Caminos: C(n-1)+C(n-2)+C(n-3)")
print("="*60)