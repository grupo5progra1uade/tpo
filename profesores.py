import pwinput


profesores = {
    1: {"nombre": "Maria", "apellido": "Gonzalez", "email": "maria@gmail.com", "contraseña": "Contra123" ,"seguridad": "pepita","materia": "Matematica"},
    2: {"nombre": "Juan",  "apellido": "Perez", "email": "juan@gmail.com", "contraseña": "Contra123","seguridad": "pepita", "materia": "Historia"},
    3: {"nombre": "Luis", "apellido": "Ramirez", "email": "luis@gmail.com", "contraseña": "Contra123","seguridad": "pepita", "materia": "Literatura"}
}

def mostrar_profesores():
    print("\nProfesores del curso:")
    print("Nombre             | Apellido                | Email                   | Materia")
    print("-" * 80)
    for id, prof in profesores.items():
        print(f"{prof['nombre']:<20} | {prof['apellido']:<20} | {prof['email']:<25} | {prof['materia']}")
    print("-" * 80)


def ingreso():

    intentos = 0
    max_intentos = 3

    while intentos < max_intentos:
        email = input("Ingrese su email: ").strip().lower()
        contraseña = pwinput.pwinput("Ingrese su contraseña: ", mask="*")

        for prof in profesores.values():
            if prof["email"].lower() == email and prof["contraseña"] == contraseña:
                print(" ------------------------------")
                print(f"Bienvenido {prof['nombre']} {prof['apellido']}")
                return True

        intentos += 1
        print(f"Email o contraseña incorrectos. Intento {intentos} de {max_intentos}.\n")

    print("Has superado el número máximo de intentos. Intenta más tarde.")
    return False


def cambiar_contraseña():
    intentos_email = 0
    max_intentos = 3

    while intentos_email < max_intentos:
        email = input("Ingrese su email: ").strip().lower()
        profesor = None

        
        for prof in profesores.values():
            if prof["email"] == email:
                profesor = prof
                break

        if profesor:
            intentos_seguridad = 0
            while intentos_seguridad < max_intentos:
                mascota = input("Ingrese el nombre de su mascota: ").lower()
                if profesor.get("seguridad") == mascota:
                    contraseña = input("Ingrese su nueva contraseña: ")
                    conf_contraseña = input("Confirme su nueva contraseña: ")
                    if contraseña == conf_contraseña:
                        profesor["contraseña"] = contraseña
                        print("Contraseña cambiada con éxito.")
                        return True
                    else:
                        print("Las contraseñas no coinciden. Intente nuevamente.")
                        return False
                else:
                    intentos_seguridad += 1
                    print(f"Respuesta de seguridad incorrecta. Intento {intentos_seguridad} de {max_intentos}.\n")

            print("Demasiados intentos fallidos con la respuesta de seguridad.")
            return False
        else:
            intentos_email += 1
            print(f"Email no encontrado. Intento {intentos_email} de {max_intentos}.\n")

    print("Demasiados intentos fallidos con el email.")
    return False

