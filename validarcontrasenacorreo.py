import re

def validar_correo(correo):
    patron = r'^[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.([a-zA-Z]{2,})+([\.a-zA-Z]{2,})?$'
    return re.match(patron, correo)


def validar_contrasena(contrasena):
    if len(contrasena) < 8:
        return False, "Mínimo 8 caracteres"
    if not re.search(r"[A-Z]", contrasena):
        return False, "Debe tener una mayúscula"
    if not re.search(r"[a-z]", contrasena):
        return False, "Debe tener una minúscula"
    if not re.search(r"[0-9]", contrasena):
        return False, "Debe tener un número"
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", contrasena):
        return False, "Debe tener un carácter especial"
    return True, ""


def registrar_usuario():
    while True:
        correo = input("Ingrese su correo: ")
        if validar_correo(correo):
            break
        else:
            print("Correo inválido (no se permite %)")

    while True:
        contrasena = input("Ingrese su contraseña: ")
        valida, mensaje = validar_contrasena(contrasena)

        if valida:
            print("\nUsuario registrado correctamente\n")
            break
        else:
            print("Error:", mensaje)


def menu():
    while True:
        print("===== MENÚ =====")
        print("1. Registrar usuario")
        print("2. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida\n")


menu()