import pwinput
from validaciones import *

profesores = {
    1: {"nombre": "Maria", "apellido": "Gonzalez", "email": "maria@gmail.com", "contraseña": "Contra123" ,"seguridad": "Pepita","materia": "Matematica"},
    2: {"nombre": "Juan",  "apellido": "Perez", "email": "juan@gmail.com", "contraseña": "Contra123","seguridad": "pepitas", "materia": "Historia"},
    3: {"nombre": "Luis", "apellido": "Ramirez", "email": "luis@gmail.com", "contraseña": "Contra123","seguridad": "pepita", "materia": "Literatura"}
}

def construir_indice(dic):
    return {datos["seguridad"]: id_prof for id_prof, datos in dic.items()} #crea un indice para seguridad

indice_seguridad = construir_indice(profesores)

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
                clave = input("Ingrese su palabra de seguridad: ").strip()
                if profesor.get("seguridad") == clave:
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


def agregar_profesor(dic_profes):
    while True:
        clave = input("Ingrese la palabra de seguridad que utilizará: ").strip()
        if clave.isalpha():
            break
        print("Error: La palabra de seguridad debe contener solo letras.")

    while True:
        nombre = input("Ingrese el nombre del profesor: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío.")
        elif letras_validas(nombre):
            nombre = capitalizar(nombre)
            break
        else:
            print("Nombre inválido. Ingrese solo letras.")

    while True:
        apellido = input("Ingrese el apellido del profesor: ").strip()
        if not apellido:
            print("El apellido no puede estar vacío.")
        elif letras_validas(apellido):
            apellido = capitalizar(apellido)
            break
        else:
            print("Apellido inválido. Ingrese solo letras.")

    while True:
        email = input("Ingrese el email del profesor: ").strip().lower()
        if validar_mail(email):
            break
        else:
            print("Email inválido. Intente nuevamente.")
            
    while True:
        contra = input("Ingrese su nueva contraseña")
        if not contra:
            print("No puede ingresar sino tiene contraseña")
        elif validar_psw(contra):
            break
        else:
            print("La contraseña es invalida")

    while True:
        asignatura = input("Ingrese el nombre de la materia: ").strip()
        if not asignatura:
            print("La materia no puede quedar vacía.")
        elif letras_validas(asignatura):
            asignatura = capitalizar(asignatura)
            break
        else:
            print("Nombre de materia inválido. Ingrese solo letras.")

    # Agregamos los datos al diccionario
    dic_profes[clave] = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "contraseña": contra,
        "seguridad": clave,
        "materia": asignatura
    }

    print("Profesor agregado con éxito.")


def modificar_profesor(dic, clave, indice):
    id_profesor = indice.get(clave)

    if id_profesor is None:
        print("No se encontró un profesor con esa palabra clave")
        return

    datos = dic[id_profesor]

    print("\nProfesor encontrado:")
    print("Nombre: ", datos["nombre"])
    print("Apellido: ", datos["apellido"])
    print("Email: ", datos["email"])
    print("Contraseña: ", datos["contraseña"])
    print("Materia: ", datos["materia"])

    nuevo_apellido = input("Ingrese nuevo apellido (deje vacío para no modificar): ").strip()
    if nuevo_apellido:
        datos["apellido"] = nuevo_apellido.capitalize()

    nuevo_nombre = input("Ingrese nuevo nombre (deje vacío para no modificar): ").strip()
    if nuevo_nombre:
        datos["nombre"] = nuevo_nombre.capitalize()

    nuevo_email = input("Ingrese nuevo email (deje vacío para no modificar): ").strip()
    if nuevo_email:
        datos["email"] = nuevo_email.lower()

    nueva_psw = input("Ingrese su nueva contraseña (deje vacío para no modificar): ").strip()
    if nueva_psw:
        datos["contraseña"] = validar_psw(nueva_psw)

    nueva_materia = input("Ingrese nueva materia (deje vacío para no modificar): ").strip()
    if nueva_materia:
        datos["materia"] = nueva_materia.capitalize()

    print("\n¡Profesor modificado con éxito!")