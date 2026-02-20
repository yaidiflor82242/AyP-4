# Función recursiva para sumar los dígitos de un número
def suma_digitos(n):
    # Manejar números negativos
    #n = abs(n)
    if n == 0:
        return 0
    return (n % 10) + suma_digitos(n // 10)

# Ejemplo de uso
numero = 1503
print(f"La suma de los dígitos de {numero} es: {suma_digitos(numero)}")