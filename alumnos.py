import json
from datetime import datetime
from utils import *
from functools import reduce
from validaciones import letras_validas, capitalizar

matriznx5 = []

# Precarga de alumnos
matriznx5.extend([
    [1001, "López",    "Ana",    "2024-08-15", 1],   # presente
    [1002, "Martínez", "Bruno",  "2024-08-16", 0],   # ausente
    [1003, "Ramírez",  "Clara",  "2024-08-17", -1],  # media falta
    [1004, "Suárez",   "Diego",  "2024-08-18", 1],
    [1005, "Fernández","Elena",  "2024-08-19", 0],
])

def cargar_datos():
    
    try:
        cantidad = int(input("¿Cuántos alumnos desea cargar?: "))
    except ValueError:
        print("Entrada inválida. Debe ser un número entero.")
        return

    legajos_existentes = {fila[0] for fila in matriznx5 if fila[0] is not None} 

    legajo_inicial = 1006 #empezamos en ese valor porque ya hay 5 alumnos precargados

    for fila in range(cantidad):
        #saco el while porque no hay adentro una condicion q pueda romper el bucle
        legajo = legajo_inicial + fila
        if legajo not in legajos_existentes:
            legajos_existentes.add(legajo)
                
        else:
            legajo += 1  # se evita repetir legajo si ya existe
            


        while True:
            apellido = input("Ingrese apellido del alumno: ").strip()
            if not apellido:
                print("El apellido no puede estar vacío. Vuelva a ingresarlo.")
            elif letras_validas(apellido):
                apellido = capitalizar(apellido)
                break
            else:
                print("Ingreso mal un apellido, vuelva a ingresarlo.")

        while True:
            nombre = input("Ingrese nombre del alumno: ").strip()
            if not nombre:
                print("El nombre no puede estar vacío. Vuelva a ingresarlo.")
            elif letras_validas(nombre):
                nombre = capitalizar(nombre)
                break
            else:
                print("Ingreso mal un nombre, vuelva a ingresarlo.")

        fecha = datetime.today().strftime("%Y-%m-%d")
        matriznx5.append([legajo, apellido, nombre, fecha, None])

def imprimir_matriz():
    print("Registro de asistencia")
    print("  Legajo  |    Apellido   |    Nombre     |     Fecha     | Presente")
    print("-" * 75)
    for fila in matriznx5:
        valor = fila[4] if fila[4] is not None else 'Sin registro'
        print(f"{str(fila[0]):<6} | {str(fila[1]):<18} | {str(fila[2]):<18} | {str(fila[3])} | {str(valor):<10}")


def imprimir_matriz_ordenada_por_apellido():
    print("Registro de asistencia (Ordenado por Apellido)")
    print("  Legajo  |    Apellido   |    Nombre     |     Fecha     | Presente")
    print("-" * 75)
    alumnos_ordenados = sorted(matriznx5, key=lambda alumno: alumno[1].lower())
    for fila in alumnos_ordenados:
        valor = fila[4] if fila[4] is not None else 'Sin registro'
        print(f"{fila[0]:<9} | {fila[1]:<13} | {fila[2]:<13} | {fila[3]:<13} | {valor:<10}")

def buscar_alumno_por_legajo():
    while True:
        try:
            legajo_buscado = int(input("Ingrese el numero de legajo a buscar: "))
            break #sino hay error sale del bucle
        except ValueError:
            print("Ingrese un numero entero")
    
    encontrado = False   
    for fila in matriznx5:
        if fila[0] == legajo_buscado:
            resultado = print("\nAlumno encontrado:")
            encontrado = True #se encuentra el legajo
            print(f"Legajo: {fila[0]} - Apellido: {fila[1]} - Nombre: {fila[2]} - Fecha: {fila[3]} - Presente: {fila[4]}")
            return
    if not encontrado:
        print("No se encontró un alumno con ese legajo.")
            

def get_alumnos():
    return matriznx5

def mostrar_alumnos():
    imprimir_matriz()

def ordenar_por_apellido():
    imprimir_matriz_ordenada_por_apellido()

def gestion_alumnos():
    while True:
        mostrar_menu("Gestión de Alumnos", [
            "Crear y cargar alumnos",
            "Listar alumnos",
            "Ordenar alumnos por apellido",
            "Buscar alumno por legajo",
            "Volver al menú principal"
        ])

        opcion = input("Opción: ").strip()

        if opcion == "1":
            cargar_datos()
        elif opcion == "2":
            mostrar_alumnos()
        elif opcion == "3":
            ordenar_por_apellido()
        elif opcion == "4":
            buscar_alumno_por_legajo()
        elif opcion == "5":
            break
        else:
            input("Opción inválida. Presione Enter para continuar...")

def nombres_completos():
    return list(map(lambda a: f"{a[2]} {a[1]}", matriznx5))

def alumnos_presentes():
    return list(filter(lambda a: a[4] == 1, matriznx5))

def asistencia_total_ponderada():
    return reduce(
        lambda acc, a: acc + (1 if a[4] == 1 else 0.5 if a[4] == -1 else 0),
        matriznx5,
        0
    )

def matriz_a_dict_alumnos(matriz):
    return {
        fila[0]: {
            "apellido": fila[1],
            "nombre":   fila[2],
            "fecha":    fila[3],
            "estado":   fila[4]
        }
        for fila in matriz
    }

def modificar_alumno():
    while True:
        try:
            legajo_buscado = int(input("Ingrese el número de legajo del alumno a modificar: "))
            break
        except ValueError:
            print("Ingrese un numero entero")
            
    for fila in matriznx5:
        if fila[0] == legajo_buscado:
            print("\nAlumno encontrado:")
            print("Legajo: ", fila[0])
            print("Apellido: ",fila[1])
            print("Nombre: ", fila[2])
            print("Fecha: ", fila[3])
            print("Estado de presencia: ", fila[4])

            nuevo_apellido = input("Ingrese nuevo apellido (deje vacío para no modificar): ").strip()
            if nuevo_apellido.isalpha():
                fila[1] = nuevo_apellido.capitalize()

            nuevo_nombre = input("Ingrese nuevo nombre (deje vacío para no modificar): ").strip()
            if nuevo_nombre.isalpha():
                fila[2] = nuevo_nombre.capitalize()

            nuevo_estado = input("Ingrese nuevo estado de asistencia (-1, 0, 1) o deje vacío para no modificar: ").strip()
            if nuevo_estado in ["-1", "0", "1"]:
                fila[4] = int(nuevo_estado)
            print("\n¡Alumno modificado con éxito!")
            return

    print("No se encontró un alumno con ese legajo.")

def eliminar_alumno():
    while True:
        try:
            legajo_buscado = int(input("Ingrese el número de legajo del alumno a eliminar: "))
            break
        except ValueError:
            print("Ingrese un numero entero")
            
    for i in range(len(matriznx5)):
        if matriznx5[i][0] == legajo_buscado:
            print(f"\nEliminando alumno: {matriznx5[i][1]} {matriznx5[i][2]}")
            del matriznx5[i]
            print("Alumno eliminado con éxito.")
            return
    print("No se encontró un alumno con ese legajo.")

def exportar_alumnos_a_txt(nombre_archivo="alumnos_lista.txt"):
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("Legajo,Apellido,Nombre,Fecha,Presente\n")
            for fila in matriznx5:
                presente = fila[4] if fila[4] is not None else "Sin registro"
                archivo.write(f"{fila[0]},{fila[1]},{fila[2]},{fila[3]},{presente}\n")
        print(f"Archivo de texto generado correctamente.")
    except Exception as error:
        print(f"Error al generar el archivo: {error}")

#serializacion a JSON
def exportar_alumnos_a_json(nombre_archivo="alumnos_lista.json"):
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(matriz_a_dict_alumnos(matriznx5), archivo)
        print(f"Archivo .json generado correctamente.")
    except Exception as error:
        print(f"Error al generar el archivo: {error}")
      
# falta de JSON a python

def crud_alumnos_json(nombre_archivo="alumnos_lista.json"):
    while True:
        mostrar_menu("CRUD Alumnos (JSON)", [
            "Listar alumnos",
            "Agregar alumno",
            "Modificar alumno",
            "Eliminar alumno",
            "Volver"
        ])
        opcion = input("Opción: ").strip()

        # Leer archivo JSON
        try:
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                alumnos = json.load(archivo)
        except (FileNotFoundError):
            alumnos = {}

        if opcion == "1":
            print("Legajo | Apellido | Nombre | Fecha | Estado")
            print("-" * 50)
            for legajo in alumnos:
                datos = alumnos[legajo]
                print(f"{legajo} | {datos['apellido']} | {datos['nombre']} | {datos['fecha']} | {datos['estado']}")
            input("Presione Enter para continuar...")

        elif opcion == "2":
            try:
                legajo = int(input("Ingrese legajo: "))
                if str(legajo) in alumnos:
                    print("Ya existe un alumno con ese legajo.")
                    continue
            except ValueError:
                print("Legajo inválido.")
                continue
            apellido = input("Apellido: ").strip().capitalize()
            nombre = input("Nombre: ").strip().capitalize()
            fecha = datetime.today().strftime("%Y-%m-%d")
            try:
                estado = int(input("Estado de asistencia (-1, 0, 1): "))
                if estado not in [-1, 0, 1]:
                    raise ValueError
            except ValueError:
                print("Estado inválido.")
                continue
            alumnos[str(legajo)] = {
                "apellido": apellido,
                "nombre": nombre,
                "fecha": fecha,
                "estado": estado
            }
            matriznx5.extend([[legajo, apellido, nombre, fecha, estado]]) #aca se guarda y actualiza la matriznx5
            print("Alumno agregado.")

        elif opcion == "3":
            legajo = input("Ingrese legajo a modificar: ").strip()
            if legajo not in alumnos:
                print("No existe ese legajo.")
                continue
            print(f"Actual: {alumnos[legajo]}")
            apellido = input("Nuevo apellido (deje vacío para no modificar): ").strip()
            nombre = input("Nuevo nombre (deje vacío para no modificar): ").strip()
            estado = input("Nuevo estado de asistencia (-1, 0, 1, vacío para no modificar): ").strip()
            if apellido:
                alumnos[legajo]["apellido"] = apellido.capitalize()
            if nombre:
                alumnos[legajo]["nombre"] = nombre.capitalize()
            if estado in ["-1", "0", "1"]:
                alumnos[legajo]["estado"] = int(estado)
            print("Alumno modificado.")

        elif opcion == "4":
            legajo = input("Ingrese legajo a eliminar: ").strip()
            if legajo in alumnos:
                del alumnos[legajo]
                print("Alumno eliminado.")
            else:
                print("No existe ese legajo.")

        elif opcion == "5":
            break

        else:
            print("Opción inválida.")

        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(alumnos, archivo)

