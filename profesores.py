import pwinput
import re
#import validaciones import *

profesores = {
    1: {"nombre": "Maria", "apellido": "Gonzalez", "email": "maria@gmail.com", "contraseña": "Contra123" ,"seguridad": "Pepita","materia": "Matematica"},
    2: {"nombre": "Juan",  "apellido": "Perez", "email": "juan@gmail.com", "contraseña": "Contra123","seguridad": "pepitas", "materia": "Historia"},
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

"""def agregar_profesor(dic, name, apell, mail, clave, asigna):
    while True:
        try:
            clave = input("Ingrese la palabra de seguridad que utilizara: ").strip()
    
            if not clave.isalpha():
                raise ValueError("La palabra de seguridad debe contener solo letras")
            else:
                break

        except ValueError as error:
            print(f"Error: {error}. Vuelva a ingresar la palabra de seguridad")
    
    while True:
        apell = input("Ingrese apellido del profesor: ").strip()
        if apell == None:
            print("El apellido no puede estar vacío, ingrese uno.")
            apell = input("Ingrese apellido del profesor: ").strip()
        elif letras_validas(apell):
            apell = capitalizar(apell)
            break
        else:
            print("Ingreso mal un apellido, vuelva a ingresarlo.")

    while True:
            asigna = input("Ingrese el nombre de la materia: ").strip()
            if asigna is None:
                print("La casilla de materia no puede quedar vacia.")
                asigna = input("Vuelva a ingresarla: ").strip()
            elif letras_validas(asigna):
                asigna = capitalizar(asigna)
                break
            else:
                print("Ingreso mal la materia, vuelva a intentarlo")


def modificar_profesor():
    while True:
        try:
            seguridad = input("Ingrese palabra clave para modificar el profesor: ").strip()
            break
        except ValueError:
            print("Ingrese la palabra clave")
            
    for fila in profesores:
        if fila[4] == seguridad:
            print("\nProfesor encontrado:")
            print("nombre: ", fila[0])
            print("apellido: ",fila[1])
            print("email: ", fila[2])
            print("contraseña: ", fila[3])
            print("materia: ", fila[5])

            nuevo_apellido = input("Ingrese nuevo apellido (deje vacío para no modificar): ").strip()
            if nuevo_apellido.isalpha():
                fila[1] = nuevo_apellido.capitalize()

            nuevo_nombre = input("Ingrese nuevo nombre (deje vacío para no modificar): ").strip()
            if nuevo_nombre.isalpha():
                fila[0] = nuevo_nombre.capitalize()
                
            nuevo_email = input("Ingrese el nuevo email: ")
            if nuevo_email.isalpha():
                fila[2] = nuevo_email.lower()
                
            nueva_psw = input("Ingrese su nueva contraseña: ")
            fila[3] = validar_psw(nueva_psw)

            nueva_materia = input("Ingrese nueva materia para el nuevo profesor: ").strip()
            if nueva_materia is not fila[5]:
                fila[5] = nueva_materia.capitalize()
            else:
                print("La materia esta repetida")
                
            print("\n¡Profesor modificado con éxito!")
            return

    print("No se encontró un profesor con esa palabra clave")"""

