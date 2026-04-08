"""Tienes una escalera de N escalones. En cada paso puedes subir 1 o 2 escalones.
¿De cuántas formas distintas puedes llegar al escalón N?
Ejemplo:
 N=1: 1 forma → [1]
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
    # Casos base
    if n == 0:
        return 1
    if n == 1:
        return 1
    
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
    escalones_con_memo(30) -> 1346269 (sin memo esto tardaría mucho)
    """
    if memo is None:
        memo = {}
    
    # Si ya lo calculé → lo retorno
    if n in memo:
        return memo[n]
    
    # Casos base
    if n == 0:
        return 1
    if n == 1:
        return 1
    
    # Guardar resultado antes de retornarlo
    memo[n] = escalones_con_memo(n-1, memo) + escalones_con_memo(n-2, memo)
    
    return memo[n]
    # TODO: Implementar
    pass

print(escalones_sin_memo(4))   # 5
print(escalones_con_memo(4))   # 5

print(escalones_con_memo(10))  # 89
print(escalones_con_memo(30))  # 1346269
