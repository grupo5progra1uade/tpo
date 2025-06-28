import json
from datetime import datetime
from utils import *
from functools import reduce
from validaciones import *

matriznx5 = []

# Precarga de alumnos
matriznx5.extend([
    [1001, "López", "Ana"],
    [1002, "Martínez", "Bruno"],
    [1003, "Ramírez", "Clara"],
    [1004, "Suárez", "Diego"],
    [1005, "Fernández", "Elena"],
    [1006, "Gómez", "Francisco"],
    [1007, "Pérez", "Gabriela"],
    [1008, "Sánchez", "Hugo"],
    [1009, "Torres", "Isabel"],
    [1010, "Vega", "Julián"],
])

def validar_matriz():
    """Valida que todos los elementos de la matriz tengan al menos 3 campos"""
    return all(len(fila) >= 3 for fila in matriznx5)

def legajo_existe(legajo):
    """Verifica si un legajo ya existe en la matriz"""
    return any(fila[0] == legajo for fila in matriznx5 if len(fila) >= 1)

def obtener_siguiente_legajo():
    """Obtiene el siguiente legajo disponible"""
    if not matriznx5:
        return 1001
    legajos_existentes = [fila[0] for fila in matriznx5 if len(fila) >= 1 and fila[0] is not None]
    return max(legajos_existentes) + 1 if legajos_existentes else 1001

def limpiar_matriz():
    """Elimina filas inválidas de la matriz y retorna la matriz limpia"""
    matriz_limpia = [fila for fila in matriznx5 if len(fila) >= 3 and fila[0] is not None]
    return matriz_limpia

def cargar_datos():
    
    try:
        cantidad = int(input("¿Cuántos alumnos desea cargar?: "))
        if cantidad <= 0:
            print("La cantidad debe ser un número positivo.")
            return
    except ValueError:
        print("Entrada inválida. Debe ser un número entero.")
        return

    # Validar matriz antes de cargar
    if not validar_matriz():
        print("Advertencia: La matriz contiene datos inválidos.")
    
    alumnos_agregados = 0
    
    for fila in range(cantidad):
        # Obtener siguiente legajo disponible
        legajo = obtener_siguiente_legajo()
        
        while True:
            apellido = input(f"Ingrese apellido del alumno {fila + 1}: ").strip()
            if not apellido:
                print("El apellido no puede estar vacío, vuelva a ingresarlo.")
            elif letras_validas(apellido):
                apellido = capitalizar(apellido)
                break
            else:
                print("Ingreso mal un apellido, vuelva a ingresarlo.")

        while True:
            nombre = input(f"Ingrese nombre del alumno {fila + 1}: ").strip()
            if not nombre:
                print("El nombre no puede estar vacío, vuelva a ingresarlo.")
            elif letras_validas(nombre):
                nombre = capitalizar(nombre)
                break
            else:
                print("Ingreso mal un nombre, vuelva a ingresarlo.")

        fecha = datetime.today().strftime("%Y-%m-%d")
        matriznx5.append([legajo, apellido, nombre, fecha, None])
        alumnos_agregados += 1
        print(f"Alumno {nombre} {apellido} agregado con legajo {legajo}")

    # Guardar automáticamente en JSON después de cargar
    if alumnos_agregados > 0:
        guardar_alumnos_a_json()
        print(f"\nSe agregaron {alumnos_agregados} alumnos exitosamente.")

def imprimir_matriz():
    print("Registro de asistencia")
    print("Legajo |    Apellido        |   Nombre          |    Fecha     ")
    print("-" * 60)  # Ajusté la línea de separación porque ahora es más corta
    for fila in matriznx5:
        # Verificar que la fila tenga al menos 3 elementos
        if len(fila) >= 3:
            legajo = str(fila[0]) if fila[0] is not None else ""
            apellido = str(fila[1]) if fila[1] is not None else ""
            nombre = str(fila[2]) if fila[2] is not None else ""
            fecha = str(fila[3]) if len(fila) > 3 and fila[3] is not None else ""
            print(f"{legajo:<6} | {apellido:<18} | {nombre:<18} | {fecha}")

def imprimir_matriz_ordenada_por_apellido():
    print("Registro de asistencia (Ordenado por Apellido)")
    print("  Legajo  |    Apellido   |    Nombre     |     Fecha     ")
    print("-" * 60)
    # Filtrar solo filas que tengan al menos 3 elementos
    filas_validas = [fila for fila in matriznx5 if len(fila) >= 3]
    alumnos_ordenados = sorted(filas_validas, key=lambda alumno: alumno[1].lower() if alumno[1] else "")
    for fila in alumnos_ordenados:
        legajo = str(fila[0]) if fila[0] is not None else ""
        apellido = str(fila[1]) if fila[1] is not None else ""
        nombre = str(fila[2]) if fila[2] is not None else ""
        fecha = str(fila[3]) if len(fila) > 3 and fila[3] is not None else ""
        print(f"{legajo:<9} | {apellido:<13} | {nombre:<13} | {fecha:<13}")

def buscar_alumno_por_legajo():
    # Validar matriz antes de operar
    if not validar_matriz():
        print("Error: La matriz contiene datos inválidos.")
    
    if not matriznx5:
        print("No hay alumnos para buscar.")
        return
    
    try:
        legajo_buscado = int(input("Ingrese el número de legajo del alumno: "))
        if legajo_buscado <= 0:
            print("El legajo debe ser un número positivo.")
            return
    except ValueError:
        print("Debe ingresar un número entero válido.")
        return
    
    encontrado = False   
    for fila in matriznx5:
        if len(fila) >= 3 and fila[0] == legajo_buscado:
            print("\nAlumno encontrado:")
            encontrado = True
            print(f"Legajo: {fila[0]}")
            print(f"Apellido: {fila[1]}")
            print(f"Nombre: {fila[2]}")
            print(f"Fecha: {fila[3] if len(fila) > 3 else 'No disponible'}")
            print(f"Presente: {fila[4] if len(fila) > 4 else 'No disponible'}")
            return
    
    if not encontrado:
        print(f"No se encontró un alumno con el legajo {legajo_buscado}.")
        print("Use la opción 'Listar alumnos' para ver los legajos disponibles.")

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
    # Validar matriz antes de operar
    if not validar_matriz():
        print("Error: La matriz contiene datos inválidos.")
    
    if not matriznx5:
        print("No hay alumnos para modificar.")
        return
    
    try:
        legajo_buscado = int(input("Ingrese el número de legajo del alumno a modificar: "))
        if legajo_buscado <= 0:
            print("El legajo debe ser un número positivo.")
            return
    except ValueError:
        print("Debe ingresar un número entero válido.")
        return

    for fila in matriznx5:
        if len(fila) >= 1 and fila[0] == legajo_buscado:
            print("\nAlumno encontrado:")
            print("Legajo: ", fila[0])
            print("Apellido: ",fila[1])
            print("Nombre: ", fila[2])
            print("Fecha: ", fila[3] if len(fila) > 3 else "No disponible")
            print("Estado de presencia: ", fila[4] if len(fila) > 4 else "No disponible")

            cambios_realizados = False

            while True:
                nuevo_apellido = input("Ingrese un nuevo apellido (o deje vacío para no modificar): ").strip()
                if not nuevo_apellido:
                    break
                elif letras_validas(nuevo_apellido):
                    fila[1] = nuevo_apellido.capitalize()
                    cambios_realizados = True
                    break
                else:
                    print("Solo puede ingresar letras o no modificar")
            
            while True:
                nuevo_nombre = input("Ingrese un nuevo nombre (o deje vacío para no modificar): ").strip()
                if not nuevo_nombre:
                    break
                elif letras_validas(nuevo_nombre):
                    fila[2] = nuevo_nombre.capitalize()
                    cambios_realizados = True
                    break
                else:
                    print("Solo puede ingresar letras o no modificar")

            print("Estado de presencia (no modificable)", fila[4] if len(fila) > 4 else "No disponible")
            
            if cambios_realizados:
                print("\n¡Alumno modificado con éxito!")
                if guardar_alumnos_a_json():
                    print("Cambios guardados en JSON.")
                else:
                    print("Error: Los cambios no se pudieron guardar.")
            else:
                print("\nNo se realizaron cambios.")
            return

    print(f"No se encontró un alumno con el legajo {legajo_buscado}.")
    print("Use la opción 'Listar alumnos' para ver los legajos disponibles.")

def eliminar_alumno():
    # Validar matriz antes de operar
    if not validar_matriz():
        print("Error: La matriz contiene datos inválidos.")
    
    if not matriznx5:
        print("No hay alumnos para eliminar.")
        return
    
    try:
        legajo_buscado = int(input("Ingrese el número de legajo del alumno a eliminar: "))
        if legajo_buscado <= 0:
            print("El legajo debe ser un número positivo.")
            return
    except ValueError:
        print("Debe ingresar un número entero válido.")
        return

    alumno_encontrado = None
    for i in range(len(matriznx5)-1, -1, -1):  # Recorre al revés
        if len(matriznx5[i]) >= 1 and matriznx5[i][0] == legajo_buscado:
            alumno_encontrado = matriznx5[i]
            print(f"\nAlumno encontrado: {matriznx5[i][1]} {matriznx5[i][2]} (Legajo: {matriznx5[i][0]})")
            confirmacion = input("¿Está seguro que desea eliminar este alumno? (s/n): ").strip().lower()
            if confirmacion in ['s', 'si', 'sí', 'y', 'yes']:
                del matriznx5[i]
                print("Alumno eliminado con éxito.")
                if guardar_alumnos_a_json():
                    print("Cambios guardados en JSON.")
                else:
                    print("Error: Los cambios no se pudieron guardar.")
            else:
                print("Operación cancelada. El alumno no fue eliminado.")
            return

    if not alumno_encontrado:
        print(f"No se encontró un alumno con el legajo {legajo_buscado}.")
        print("Use la opción 'Listar alumnos' para ver los legajos disponibles.")

def guardar_alumnos_a_json(nombre_archivo="alumnos_lista.json"):
    """Guarda solo los alumnos de la matriz actual en JSON, sin sincronizar"""
    try:
        # Validar matriz antes de guardar
        if not validar_matriz():
            print("Advertencia: La matriz contiene datos inválidos.")
        
        alumnos_dict = {}
        for fila in matriznx5:
            if len(fila) >= 3 and fila[0] is not None:  # Solo filas válidas
                legajo = str(fila[0])
                alumnos_dict[legajo] = {
                    "apellido": fila[1] if fila[1] else "",
                    "nombre": fila[2] if fila[2] else ""
                }
        
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            json.dump(alumnos_dict, archivo, ensure_ascii=False, indent=4)
        print("Alumnos guardados en JSON correctamente.")
        return True
    except Exception as error:
        print(f"Error crítico al guardar alumnos: {error}")
        print("Los cambios no se guardaron. Verifique el espacio en disco y permisos.")
        return False

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
                    datos["nombre"]
                ])

        # 2. Actualizar o agregar los alumnos de la matriz al JSON
        for fila in matriznx5:
            legajo = str(fila[0])
            alumnos_existentes[legajo] = {
                "apellido": fila[1],
                "nombre":   fila[2]
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
            print("  Legajo  |    Apellido   |    Nombre     ")            
            print("-" * 40)
            for legajo in alumnos:
                datos = alumnos[legajo]
                print(f"{legajo:<9} | {datos['apellido']:<13} | {datos['nombre']:<13}")
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
                    
            # No guardar fecha ni estado
            alumnos[str(legajo)] = {
                "apellido": apellido,
                "nombre": nombre
            }
            if not any(fila[0] == legajo for fila in matriznx5): #evita creacion de legajos duplicados x error
                matriznx5.append([legajo, apellido, nombre, None, None])
            else:
                print("Advertencia: el alumno ya existía, por ello, no se duplicó.")
                
            print("Alumno agregado con éxito!")

        elif opcion == "3":
                legajo = pedir_entero("Ingrese legajo a modificar: ", 1) #minimo 1 para que si o si sean (+)
                legajo_str = str(legajo)
                    
                if legajo_str not in alumnos:
                    print("No existe ese legajo.")
                    continue
                    
                print(f"Apellido actual: {alumnos[legajo_str]['apellido']}")
                print(f"Nombre actual: {alumnos[legajo_str]['nombre']}")

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
                            
                if apellido and apellido != alumnos[legajo_str]['apellido']:
                    alumnos[legajo_str]['apellido'] = apellido
                if nombre and nombre != alumnos[legajo_str]['nombre']:
                    alumnos[legajo_str]['nombre'] = nombre
                    
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
            json.dump(alumnos, archivo, ensure_ascii=False, indent=4)
            

def inicializar_alumnos():
    """Inicializa y valida la matriz de alumnos al cargar el módulo"""
    
    # Validar matriz inicial
    if not validar_matriz():
        print("Advertencia: La matriz de alumnos contiene datos inválidos.")
    
    # Verificar que no haya legajos duplicados
    legajos = []
    for fila in matriznx5:
        if len(fila) >= 1 and fila[0] is not None:
            if fila[0] in legajos:
                print(f"Advertencia: Legajo duplicado encontrado: {fila[0]}")
            else:
                legajos.append(fila[0])
    
    # No mostrar mensaje de inicialización al usuario

# Inicializar al cargar el módulo
inicializar_alumnos()
            
