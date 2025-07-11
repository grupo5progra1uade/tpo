import pwinput
import json
from validaciones import *
from materias import * 

# Archivo JSON para almacenar profesores
ARCHIVO_PROFESORES = "profesores.json"

def cargar_profesores():
    """Carga los profesores desde el archivo JSON"""
    try:
        with open(ARCHIVO_PROFESORES, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No se encontró el archivo de profesores o está corrupto. Se usará el diccionario por defecto.")
        profesores = profesores_default()
        guardar_profesores(profesores)
        return profesores

def profesores_default():
    """Retorna el diccionario de profesores por defecto"""
    return {
        "1": {"nombre": "Maria", "apellido": "Gonzalez", "email": "maria@gmail.com", "contraseña": "Contra123", "materia": "Matematica"},
        "2": {"nombre": "Juan",  "apellido": "Perez", "email": "juan@gmail.com", "contraseña": "Contra123", "materia": "Historia"},
        "3": {"nombre": "Luis", "apellido": "Ramirez", "email": "luis@gmail.com", "contraseña": "Contra123", "materia": "Literatura"}
    }

def guardar_profesores(profesores):
    """Guarda los profesores en el archivo JSON"""
    try:
        with open(ARCHIVO_PROFESORES, 'w', encoding='utf-8') as archivo:
            json.dump(profesores, archivo, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error al guardar profesores: {e}")
        return False

# Cargar profesores al importar el módulo
profesores = cargar_profesores()

def mostrar_profesores():
    # Cargar datos actualizados del archivo JSON
    profesores_actuales = cargar_profesores()
    
    print("\nProfesores del curso:")
    print("Nombre             | Apellido                | Email                   | Materia")
    print("-" * 80)
    for id, prof in profesores_actuales.items():
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
            intentos_contraseña = 0
            while intentos_contraseña < max_intentos:
                contraseña_actual = input("Ingrese su contraseña actual: ")
                if profesor["contraseña"] == contraseña_actual:
                    nueva_contraseña = input("Ingrese su nueva contraseña: ")
                    conf_contraseña = input("Confirme su nueva contraseña: ")
                    if nueva_contraseña == conf_contraseña:
                        if validar_psw(nueva_contraseña):
                            profesor["contraseña"] = nueva_contraseña
                            # Guardar cambios en JSON
                            if guardar_profesores(profesores):
                                print("Contraseña cambiada con éxito.")
                                return True
                            else:
                                print("Error al guardar los cambios. La contraseña no fue modificada.")
                                return False
                        else:
                            print("La nueva contraseña no cumple con los requisitos de seguridad.")
                            return False
                    else:
                        print("Las contraseñas no coinciden. Intente nuevamente.")
                        return False
                else:
                    intentos_contraseña += 1
                    print(f"Contraseña incorrecta. Intento {intentos_contraseña} de {max_intentos}.\n")

            print("Demasiados intentos fallidos con la contraseña.")
            return False
        else:
            intentos_email += 1
            print(f"Email no encontrado. Intento {intentos_email} de {max_intentos}.\n")

    print("Demasiados intentos fallidos con el email.")
    return False

def agregar_profesor(dic_profes):
    data = cargar_materias()
    
    # Obtener siguiente ID disponible
    if dic_profes:
        max_id = max(int(i) for i in dic_profes.keys())
        nuevo_id = str(max_id + 1)
    else:
        nuevo_id = "1"

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
        contra = input("Ingrese su nueva contraseña: ")
        if not contra:
            print("No puede ingresar sino tiene contraseña")
        elif validar_psw(contra):
            break
        else:
            print("La contraseña es inválida")

    while True:
        asignatura = input("Ingrese el nombre de la materia: ").strip()
        if not asignatura:
            print("La materia no puede quedar vacía.")
        elif letras_validas(asignatura):
            asignatura = capitalizar(asignatura)
            # Agregar la materia si no existe
            if asignatura not in data["materias"]:
                data["materias"].append(asignatura)
                guardar_materias(data)
                print(f"Materia '{asignatura}' agregada automáticamente a la lista de materias.")
            break
        else:
            print("Nombre de materia inválido. Ingrese solo letras.")

    # Agregamos los datos al diccionario
    dic_profes[nuevo_id] = {
        "nombre": nombre,
        "apellido": apellido,
        "email": email,
        "contraseña": contra,
        "materia": asignatura
    }
    
    materia_profesor = dic_profes[nuevo_id]["materia"]
    
    if materia_profesor not in data["materias"]:
        data["materias"].append(materia_profesor)
        guardar_materias(data)
        print("La materia fue agregada al sistema con éxito!")
    else:
        print("La materia ya se encuentra en el sistema")
    
    # Guardar cambios en JSON
    if guardar_profesores(dic_profes):
        print(f"\n¡Profesor agregado con éxito! ID asignado: {nuevo_id}")
        return True
    else:
        print("Error al guardar los cambios. El profesor no fue agregado.")
        # Eliminar profesor en caso de error
        dic_profes.pop(nuevo_id, None)
        return False

def modificar_profesor(dic, id_profesor):
    data = cargar_materias()
    profesor_encontrado = None

    if id_profesor in dic:
        profesor_encontrado = dic[id_profesor]
    else:
        print(f"No se encontró un profesor con el ID {id_profesor}.")
        return False

    print("\nProfesor encontrado:")
    print("ID: ", id_profesor)
    print("Nombre: ", profesor_encontrado["nombre"])
    print("Apellido: ", profesor_encontrado["apellido"])
    print("Email: ", profesor_encontrado["email"])
    print("Contraseña: ", profesor_encontrado["contraseña"])
    print("Materia: ", profesor_encontrado["materia"])

    while True:
        nuevo_apellido = input("Ingrese nuevo apellido (deje vacío para no modificar): ").strip()
        if not nuevo_apellido or letras_validas(nuevo_apellido):
            break
        else:
            print("Debe ingresar un apellido que solo contenga letras")
    if nuevo_apellido:
        nuevo_apellido = capitalizar(nuevo_apellido)

    while True:
        nuevo_nombre = input("Ingrese nuevo nombre (deje vacío para no modificar): ").strip()
        if not nuevo_nombre or letras_validas(nuevo_nombre):
            break
        else:
            print("Debe ingresar un nombre que contenga solo letras")
    if nuevo_nombre:
        nuevo_nombre = capitalizar(nuevo_nombre)

    while True:
        nuevo_email = input("Ingrese nuevo email (deje vacío para no modificar): ").strip()
        if not nuevo_email or validar_mail(nuevo_email):
            break
        else:
            print("Debe ingresar un mail válido")
    if nuevo_email:
        nuevo_email = nuevo_email.lower()

    while True:
        nueva_psw = input("Ingrese su nueva contraseña (deje vacío para no modificar): ").strip()
        if not nueva_psw or validar_psw(nueva_psw):
            break
        
    while True:
        nueva_materia = input("Ingrese nueva materia (deje vacío para no modificar): ").strip()
        if not nueva_materia or letras_validas(nueva_materia):
            break
        else:
            print("La materia debe contener solo letras")
    if nueva_materia:
        nueva_materia = capitalizar(nueva_materia)

    # Actualizaciones
    if nuevo_apellido:
        profesor_encontrado["apellido"] = nuevo_apellido

    if nuevo_nombre:
        profesor_encontrado["nombre"] = nuevo_nombre

    if nuevo_email:
        profesor_encontrado["email"] = nuevo_email

    if nueva_psw:
        profesor_encontrado["contraseña"] = nueva_psw

    if nueva_materia:
        profesor_encontrado["materia"] = nueva_materia

    materia_profesor = profesor_encontrado["materia"]
    
    if materia_profesor not in data["materias"]:
        data["materias"].append(materia_profesor)
        guardar_materias(data)
        print("La materia fue agregada al sistema con éxito!")
    else:
        print("La materia ya se encuentra en el sistema")
        
    # Guardar cambios en JSON
    if guardar_profesores(dic):
        print("\n¡Profesor modificado con éxito!")
        return True
    else:
        print("Error al guardar los cambios. Las modificaciones no fueron aplicadas.")
        return False

def eliminar_profesor(dic_profes):
    """Elimina un profesor del sistema"""
    print("\n=== ELIMINAR PROFESOR ===")
    
    # Mostrar lista de profesores disponibles
    print("\nProfesores disponibles:")
    print("ID  | Nombre             | Apellido                | Email                   | Materia")
    print("-" * 85)
    for id_prof, prof in dic_profes.items():
        print(f"{id_prof:<4} | {prof['nombre']:<20} | {prof['apellido']:<20} | {prof['email']:<25} | {prof['materia']}")
    print("-" * 85)
    
    # Solicitar ID del profesor a eliminar
    while True:
        id_eliminar = input("\nIngrese el ID del profesor a eliminar: ").strip()
        if id_eliminar in dic_profes:
            break
        else:
            print("ID no válido. Ingrese un ID de la lista anterior.")
    
    # Confirmar eliminación
    profesor = dic_profes[id_eliminar]
    print(f"\nProfesor a eliminar:")
    print(f"Nombre: {profesor['nombre']} {profesor['apellido']}")
    print(f"Email: {profesor['email']}")
    print(f"Materia: {profesor['materia']}")
    
    confirmacion = input("\n¿Está seguro que desea eliminar este profesor? (s/n): ").strip().lower()
    
    if confirmacion in ['s', 'si', 'sí', 'y', 'yes']:
        # Eliminar profesor
        profesor_eliminado = dic_profes.pop(id_eliminar)
        
        # Guardar cambios en JSON
        if guardar_profesores(dic_profes):
            print(f"\n¡Profesor {profesor_eliminado['nombre']} {profesor_eliminado['apellido']} eliminado con éxito!")
            return True
        else:
            print("Error al guardar los cambios. El profesor no fue eliminado.")
            # Restaurar profesor en caso de error
            dic_profes[id_eliminar] = profesor_eliminado
            return False
    else:
        print("Eliminación cancelada.")
        return False