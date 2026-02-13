n = int(input("Ingrese un número: "))

resultado = 1

for i in range(1, n + 1):
    resultado = resultado * i

print("El factorial es:", resultado)
