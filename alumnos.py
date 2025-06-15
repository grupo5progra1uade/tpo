import json
from datetime import datetime
from utils import *
from functools import reduce
from validaciones import *

matriznx5 = []

# Precarga de alumnos
matriznx5.extend([
    [1001, "López",    "Ana",    "2024-08-15", None],  
    [1002, "Martínez", "Bruno",  "2024-08-16", None],  
    [1003, "Ramírez",  "Clara",  "2024-08-17", None],  
    [1004, "Suárez",   "Diego",  "2024-08-18", None],  #None para que no haya
    [1005, "Fernández","Elena",  "2024-08-19", None],
    [1006, "Gómez",    "Francisco", "2024-08-20", None],
    [1007, "Pérez",    "Gabriela",  "2024-08-21", None],
    [1008, "Sánchez",  "Hugo",      "2024-08-22", None],
    [1009, "Torres",   "Isabel",    "2024-08-23", None],
    [1010, "Vega",     "Julián",    "2024-08-24", None],
])

def cargar_datos():
    
    try:
        cantidad = int(input("¿Cuántos alumnos desea cargar?: "))
    except ValueError:
        print("Entrada inválida. Debe ser un número entero.")
        return

    legajos_existentes = {fila[0] for fila in matriznx5 if fila[0] is not None} 

    legajo_inicial = 1011 #empezamos en ese valor porque ya hay 5 alumnos precargados

    for fila in range(cantidad):
        legajo = legajo_inicial + fila
        if legajo not in legajos_existentes:
            legajos_existentes.add(legajo)    
        else:
            legajo += 1  # se evita repetir legajo si ya existe

        while True:
            apellido = input("Ingrese apellido del alumno: ").strip()
            if not apellido:
                print("El apellido no puede estar vacío, vuelva a ingresarlo.")
            elif letras_validas(apellido):
                apellido = capitalizar(apellido)
                break
            else:
                print("Ingreso mal un apellido, vuelva a ingresarlo.")

        while True:
            nombre = input("Ingrese nombre del alumno: ").strip()
            if not nombre:
                print("El nombre no puede estar vacío, vuelva a ingresarlo.")
            elif letras_validas(nombre):
                nombre = capitalizar(nombre)
                break
            else:
                print("Ingreso mal un nombre, vuelva a ingresarlo.")

        fecha = datetime.today().strftime("%Y-%m-%d")
        matriznx5.append([legajo, apellido, nombre, fecha, None])

def imprimir_matriz():
    print("Registro de asistencia")
    print("Legajo |    Apellido        |   Nombre          |    Fecha     ")
    print("-" * 60)  # Ajusté la línea de separación porque ahora es más corta
    for fila in matriznx5:
        # Ya no necesitamos valor ni la columna presente
        print(f"{str(fila[0]):<6} | {str(fila[1]):<18} | {str(fila[2]):<18} | {str(fila[3])}")

def imprimir_matriz_ordenada_por_apellido():
    print("Registro de asistencia (Ordenado por Apellido)")
    print("  Legajo  |    Apellido   |    Nombre     |     Fecha     ")
    print("-" * 60)
    alumnos_ordenados = sorted(matriznx5, key=lambda alumno: alumno[1].lower())
    for fila in alumnos_ordenados:
        print(f"{fila[0]:<9} | {fila[1]:<13} | {fila[2]:<13} | {fila[3]:<13}")

def buscar_alumno_por_legajo():
    while True:
        try:
            legajo_buscado = int(input("Ingrese el número de legajo del alumno: "))
            break #sino hay error sale del bucle
        except ValueError:
            print("Debe ingresar un número entero")
            return buscar_alumno_por_legajo() #vuelve a pedir el legajo
    
    encontrado = False   
    for fila in matriznx5:
        if fila[0] == legajo_buscado:
            resultado = print("\nAlumno encontrado:")
            encontrado = True #se encuentra el legajo
            print(f"Legajo: {fila[0]} - Apellido: {fila[1]} - Nombre: {fila[2]} - Fecha: {fila[3]} - Presente: {fila[4]}")
            return
    if not encontrado:
        print("No se encontró un alumno con ese legajo.")
    return buscar_alumno_por_legajo()

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
            print("Debe ingresar un número entero")

    for fila in matriznx5:
        if fila[0] == legajo_buscado:
            print("\nAlumno encontrado:")
            print("Legajo: ", fila[0])
            print("Apellido: ",fila[1])
            print("Nombre: ", fila[2])
            print("Fecha: ", fila[3])
            print("Estado de presencia: ", fila[4])

            while True:
                nuevo_apellido = input("Ingrese un nuevo apellido (o deje vacío para no modificar): ").strip()
                if not nuevo_apellido:
                    break
                elif letras_validas(nuevo_apellido):
                    fila[1] = nuevo_apellido.capitalize()
                    break
                else:
                    print("Solo puede ingresar letras o no modificar")
            
            while True:
                nuevo_nombre = input("Ingrese un nuevo nombre (o deje vacío para no modificar): ").strip()
                if not nuevo_nombre:
                    break
                elif letras_validas(nuevo_nombre):
                    fila[2] = nuevo_nombre.capitalize()
                    break
                else:
                    print("Solo puede ingresar letras o no modifcar")

            print("Estado de presencia (no modificable)", fila[4])
            
            print("\n¡Alumno modificado con éxito!")
            exportar_alumnos_a_json()
            return

    print("No se encontró un alumno con ese legajo.")

def eliminar_alumno():
    while True:
        try:
            legajo_buscado = int(input("Ingrese el número de legajo del alumno a eliminar: "))
            break
        except ValueError:
            print("Debe ingresar un número entero.")

    for i in range(len(matriznx5)):
        if matriznx5[i][0] == legajo_buscado:
            print(f"\nAlumno encontrado: {matriznx5[i][1]} {matriznx5[i][2]}")
            confirmacion = input("¿Está seguro que desea eliminar este alumno? (s/n): ").strip().lower()
            if confirmacion == "s":
                del matriznx5[i]
                print("Alumno eliminado con éxito.")
            else:
                print("Operación cancelada. El alumno no fue eliminado.")
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
    try: # Captura cualquier otro error que ocurra en la función
        
        try: # Leer los alumnos existentes del JSON
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                alumnos_existentes = json.load(archivo)
        except FileNotFoundError:
            alumnos_existentes = {}

        # 1. Sincronizar: agregar a la matriz los alumnos que están en el JSON pero no en la matriz
        legajos_matriz = {str(fila[0]) for fila in matriznx5}
        for legajo, datos in alumnos_existentes.items():
            if legajo not in legajos_matriz:
                matriznx5.append([
                    int(legajo),
                    datos["apellido"],
                    datos["nombre"],
                    datos["fecha"],
                    datos["estado"]
                ])

        # 2. Actualizar o agregar los alumnos de la matriz al JSON
        for fila in matriznx5:
            legajo = str(fila[0])
            alumnos_existentes[legajo] = {
                "apellido": fila[1],
                "nombre":   fila[2],
                "fecha":    fila[3],
                "estado":   fila[4]
            }

        # 3. Guardar el resultado actualizado
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(alumnos_existentes, archivo, ensure_ascii=False, indent=4)
        print(f"Archivo .json generado correctamente y sincronizado.")
    except Exception as error:
        print(f"Error al generar el archivo: {error}")

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
            print("  Legajo  |    Apellido   |    Nombre     |     Estado     ")            
            print("-" * 50)
            for legajo in alumnos:
                datos = alumnos[legajo]
                print(f"{legajo:<9} | {datos['apellido']:<13} | {datos['nombre']:<13} | {datos['estado']}")
            input("Presione Enter para continuar...")

        elif opcion == "2":
            # Generar legajo automáticamente
            if alumnos:
                max_legajo = max(int(i) for i in alumnos.keys())
                legajo = max_legajo + 1
            else:
                legajo = 1001
            print(f"Legajo asignado automáticamente: {legajo}")
            
            while True:
                apellido = input("Ingrese el apellido: ").strip()
                if not apellido:
                    print("El apellido no puede estar vacío")
                elif letras_validas(apellido):
                    apellido = capitalizar(apellido)
                    break
                else:
                    print("Apellido inválido, debe ingresar solo letras y espacios")
                    
            while True:
                nombre = input("Nombre: ").strip()
                if not nombre:
                    print("El nombre no puede quedar vacío")
                elif letras_validas(nombre):
                    nombre = capitalizar(nombre)
                    break
                else:
                    print("El nombre es inválido, debe ingresar solo letras y espacios")
                    
            fecha = datetime.today().strftime("%Y-%m-%d")
            estado = None  # Estado inicial es None
            
            alumnos[str(legajo)] = {
                "apellido": apellido,
                "nombre": nombre,
                "fecha": fecha,
                "estado": estado
            }
            if not any(fila[0] == legajo for fila in matriznx5): #evita creacion de legajos duplicados x error
                matriznx5.append([legajo, apellido, nombre, fecha, estado])
            else:
                print("Advertencia: el alumno ya existía, por ello, no se duplicó.")
                
            print("Alumno agregado con éxito!")

        elif opcion == "3":
                legajo = pedir_entero("Ingrese legajo a modificar: ", minimo=1) #minimo 1 para que si o si sean (+)
                    
                if legajo not in alumnos:
                    print("No existe ese legajo.")
                    continue
                    
                print(f"Apellido actual: {alumnos[legajo]['apellido']}")
                print(f"Nombre actual: {alumnos[legajo]['nombre']}")

                while True:
                    apellido = input("Nuevo apellido (deje vacío para no modificar): ").strip()
                    if not apellido:
                        break
                    elif letras_validas(apellido):
                        apellido = capitalizar(apellido)
                        break
                    else:
                        print("Apellido inválido, debe ingresar solo letras y espacios")

                while True:
                    nombre = input("Nuevo nombre (deje vacío para no modificar): ").strip()
                    if not nombre:
                        break
                    elif letras_validas(nombre):
                        nombre = capitalizar(nombre)
                        break
                    else:
                        print("El nombre es inválido, debe ingresar solo letras y espacios")
                            
                if apellido and apellido != alumnos[legajo]['apellido']:
                    alumnos[legajo]['apellido'] = apellido
                if nombre and nombre != alumnos[legajo]['nombre']:
                    alumnos[legajo]['nombre'] = nombre
                    
                print("Alumno modificado con éxito!")

        elif opcion == "4":
            legajo = input("Ingrese legajo a eliminar: ").strip()
            if legajo in alumnos:
                del alumnos[legajo]
                matriznx5[:] = [fila for fila in matriznx5 if str(fila[0]) != legajo]
                print("Alumno eliminado.")
            else:
                print("No existe ese legajo.")

        elif opcion == "5":
            break

        else:
            print("Opción inválida.")

        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(alumnos, archivo)
            