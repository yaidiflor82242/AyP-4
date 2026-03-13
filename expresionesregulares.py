#validar un fecha
import re

texto="15/03/2025"
resultado=re.findall(r"^(0[1-9]|[12][0-9]|3[01])[-/](0[1-9]|1[0-2])[-/](\d{4})$",texto)
print(f"fecha{resultado}")

#validar una placa de carro
import re

texto="ABD 987"
resultado=re.findall(r"^[A-Z]{3}\s? \d{3}$",texto)
print(f"placa{resultado}")

#validar un correo electronico
import re
texto="hola123@gmail.com"
resultado=re.findall(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",texto)
print(f"correo{resultado}") 

#validar un numero de celular colombiano
import re
texto="312 345 6789"
resultado=re.findall(r"^(3\d{2}[-\s]?\d{3}[-\s]?\d{2}[-\s]?\d{2})$",texto)
print(f"celular{resultado}")



"""registrar un usuario que pida un  correo y lo valide, y una contraseña, la contraseña debe tener 
minimo 8 caracteres, 1 letra mayuscula, 1 minuscula,1 numero, y 1 caracter especial"""
import re

def validar_correo(correo):
    return re.match(r"^[\w\.-]+@[A-Za-z0-9]+\.([A-Za-z]{3})+([\.A-Za-z]{2})?$", correo)

def validar_contraseña(password):
    return re.match(r"(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}", password)


while True:

    print("\nMENU")
    print("1. Registrar usuario")
    print("2. Salir")

    opcion = input("Seleccione una opción: ")

    match opcion:

        case "1":
            correo = input("Ingrese correo: ")

            if not validar_correo(correo):
                print("Correo inválido")
                continue

            contraseña = input("Ingrese contraseña: ")

            if not validar_contraseña(contraseña):
                print("Contraseña inválida")
                print("Debe tener mínimo 8 caracteres, mayúscula, minúscula, número y carácter especial")
                continue

            print("Usuario registrado correctamente")

        case "2":
            print("Saliendo...")
            break

        case _:
            print("Opción inválida")



"""registrar un usuario que pida un  correo y lo valide, y una contraseña, la contraseña debe tener 
minimo 8 caracteres, 1 letra mayuscula, 1 minuscula,1 numero, y 1 caracter especial
EJEMPLO PROFE"""
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
    print("-"*20,"EJEMPLO PROFESOR ","-"*20)
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