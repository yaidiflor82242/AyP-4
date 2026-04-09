import re

def validar_correo(correo):
    validar = re.search(r'^[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.([a-zA-Z]{2,})+([\.a-zA-Z]{2,})?$', correo)
    return bool(validar)

def validar_contrasena(contrasena):
    if len(contrasena) < 8:
        return False
    elif not bool(re.search(r'[A-Z]', contrasena)):
        return False
    elif not bool(re.search(r'[a-z]', contrasena)):
        return False
    elif not bool(re.search(r'[0-9]', contrasena)):
        return False
    elif not bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', contrasena)):
        return False
    return True

persona = []

while True:
    print("Seleccione una opción:")
    print("1. Registrar usuario")
    print("2. Salir")

    opcion = int(input())

    if opcion == 1:
        correo = input("Ingrese su correo: ")
        if validar_correo(correo):
            print("Correo válido")
            contrasena = input("Ingrese su contraseña: ")
            if validar_contrasena(contrasena):
                persona.append((correo, contrasena))
                print("Usuario registrado correctamente")
            else:
                print("Contraseña inválida")

        else:
            print("Correo inválido")
            print("-" * 40)
            print("-" * 40)
            print("-" * 40)

    elif opcion == 2:
        print("Saliendo del sistema...")
        break