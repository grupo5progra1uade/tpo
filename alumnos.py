import json
from datetime import datetime
from utils import *
from functools import reduce
from validaciones import *

# Archivo JSON para almacenar alumnos
ARCHIVO_ALUMNOS = "alumnos_lista.json"

def cargar_alumnos_json():
    """Carga los alumnos desde el archivo JSON"""
    try:
        with open(ARCHIVO_ALUMNOS, 'r', encoding='utf-8') as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        # Si no existe el archivo, crear con datos por defecto
        alumnos_default = {
            "1001": {"apellido": "López", "nombre": "Ana"},
            "1002": {"apellido": "Martínez", "nombre": "Bruno"},
            "1003": {"apellido": "Ramírez", "nombre": "Clara"},
            "1004": {"apellido": "Suárez", "nombre": "Diego"},
            "1005": {"apellido": "Fernández", "nombre": "Elena"},
            "1006": {"apellido": "Gómez", "nombre": "Francisco"},
            "1007": {"apellido": "Pérez", "nombre": "Gabriela"},
            "1008": {"apellido": "Sánchez", "nombre": "Hugo"},
            "1009": {"apellido": "Torres", "nombre": "Isabel"},
            "1010": {"apellido": "Vega", "nombre": "Julián"}
        }
        guardar_alumnos_json(alumnos_default)
        return alumnos_default

def guardar_alumnos_json(alumnos_dict):
    """Guarda los alumnos en el archivo JSON"""
    try:
        with open(ARCHIVO_ALUMNOS, 'w', encoding='utf-8') as archivo:
            json.dump(alumnos_dict, archivo, ensure_ascii=False, indent=4)
        print("Alumnos guardados en JSON correctamente.")
        return True
    except Exception as error:
        print(f"Error crítico al guardar alumnos: {error}")
        return False

def obtener_siguiente_legajo():
    """Obtiene el siguiente legajo disponible"""
    alumnos = cargar_alumnos_json()
    if not alumnos:
        return 1001
    legajos_existentes = [int(legajo) for legajo in alumnos.keys()]
    return max(legajos_existentes) + 1 if legajos_existentes else 1001

def validar_alumnos(alumnos_dict):
    """Valida que el diccionario de alumnos sea válido"""
    # Verificar que alumnos_dict no sea None y tenga contenido
    if alumnos_dict is None:
        return False
    # Verificar que sea un diccionario (sin usar isinstance)
    try:
        # Intentar acceder a keys() para verificar que es un diccionario
        alumnos_dict.keys()
        return True
    except:
        return False

#def cargar_datos():

def cargar_datos():
    try:
        cantidad = int(input("¿Cuántos alumnos desea cargar?: "))
        if cantidad <= 0:
            print("La cantidad debe ser un número positivo.")
            return
    except ValueError:
        print("Entrada inválida. Debe ser un número entero.")
        return

    alumnos = cargar_alumnos_json()
    alumnos_agregados = 0

    # Obtener el siguiente legajo solo una vez
    legajo = obtener_siguiente_legajo()

    for fila in range(cantidad):
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

        legajo_str = str(legajo)
        alumnos[legajo_str] = {
            "apellido": apellido,
            "nombre": nombre
        }
        alumnos_agregados += 1
        print(f"Alumno {nombre} {apellido} agregado con legajo {legajo}")

        legajo += 1  # Incrementar para el próximo alumno

    # Guardar automáticamente en JSON después de cargar
    if alumnos_agregados > 0:
        guardar_alumnos_json(alumnos)
        print(f"\nSe agregaron {alumnos_agregados} alumnos exitosamente.")

def imprimir_matriz():
    alumnos = cargar_alumnos_json()
    print("\nRegistro de alumnos\n")
    print("Legajo |      Apellido      |    Nombre    ")
    print("-" * 45)
    for legajo, datos in alumnos.items():
        legajo_str = str(legajo)
        apellido = datos.get("apellido", "")
        nombre = datos.get("nombre", "")
        print(f"{legajo_str:<6} | {apellido:<18} | {nombre:<18}")

def imprimir_matriz_ordenada_por_apellido():
    alumnos = cargar_alumnos_json()
    print("\nRegistro de alumnos (Ordenado por Apellido)\n")
    print("  Legajo  |   Apellido    |    Nombre    ")
    print("-" * 45)
    
    # Ordenar por apellido
    alumnos_ordenados = sorted(alumnos.items(), key=lambda x: x[1]["apellido"].lower())
    for legajo, datos in alumnos_ordenados:
        legajo_str = str(legajo)
        apellido = datos.get("apellido", "")
        nombre = datos.get("nombre", "")
        print(f"{legajo_str:<9} | {apellido:<13} | {nombre:<13}")

def buscar_alumno_por_legajo():
    alumnos = cargar_alumnos_json()
    
    if not validar_alumnos(alumnos):
        print("Error: No hay alumnos para buscar.")
        return
    
    try:
        legajo_buscado = input("Ingrese el número de legajo del alumno: ").strip()
        if not legajo_buscado:
            print("Debe ingresar un legajo válido.")
            return
    except:
        print("Debe ingresar un legajo válido.")
        return
    
    if legajo_buscado in alumnos:
        datos = alumnos[legajo_buscado]
        print("\nAlumno encontrado:")
        print(f"Legajo: {legajo_buscado}")
        print(f"Apellido: {datos.get('apellido', '')}")
        print(f"Nombre: {datos.get('nombre', '')}")
    else:
        print(f"No se encontró un alumno con el legajo {legajo_buscado}.")
        print("Use la opción 'Listar alumnos' para ver los legajos disponibles.")

def get_alumnos():
    return cargar_alumnos_json()

def mostrar_alumnos():
    imprimir_matriz()

def ordenar_por_apellido():
    imprimir_matriz_ordenada_por_apellido()

def nombres_completos():
    alumnos = cargar_alumnos_json()
    return [f"{datos['nombre']} {datos['apellido']}" for datos in alumnos.values()]

def alumnos_presentes():
    # Esta función necesitaría datos de asistencia separados
    # Por ahora retorna lista vacía
    return []

def asistencia_total_ponderada():
    # Esta función necesitaría datos de asistencia separados
    # Por ahora retorna 0
    return 0

def matriz_a_dict_alumnos(matriz):
    # Esta función ya no es necesaria
    return cargar_alumnos_json()

def modificar_alumno():
    alumnos = cargar_alumnos_json()
    
    if not validar_alumnos(alumnos):
        print("Error: No hay alumnos para modificar.")
        return
    
    try:
        legajo_buscado = input("Ingrese el número de legajo del alumno a modificar: ").strip()
        if not legajo_buscado:
            print("Debe ingresar un legajo válido.")
            return
    except:
        print("Debe ingresar un legajo válido.")
        return

    if legajo_buscado in alumnos:
        datos = alumnos[legajo_buscado]
        print("\nAlumno encontrado:")
        print("Legajo: ", legajo_buscado)
        print("Apellido: ", datos.get("apellido", ""))
        print("Nombre: ", datos.get("nombre", ""))

        cambios_realizados = False

        while True:
            nuevo_apellido = input("Ingrese un nuevo apellido (o deje vacío para no modificar): ").strip()
            if not nuevo_apellido:
                break
            elif letras_validas(nuevo_apellido):
                datos["apellido"] = nuevo_apellido.capitalize()
                cambios_realizados = True
                break
            else:
                print("Solo puede ingresar letras o no modificar")
        
        while True:
            nuevo_nombre = input("Ingrese un nuevo nombre (o deje vacío para no modificar): ").strip()
            if not nuevo_nombre:
                break
            elif letras_validas(nuevo_nombre):
                datos["nombre"] = nuevo_nombre.capitalize()
                cambios_realizados = True
                break
            else:
                print("Solo puede ingresar letras o no modificar")
        
        if cambios_realizados:
            print("\n¡Alumno modificado con éxito!")
            if guardar_alumnos_json(alumnos):
                print("Cambios guardados en JSON.")
            else:
                print("Error: Los cambios no se pudieron guardar.")
        else:
            print("\nNo se realizaron cambios.")
    else:
        print(f"No se encontró un alumno con el legajo {legajo_buscado}.")
        print("Use la opción 'Listar alumnos' para ver los legajos disponibles.")

def eliminar_alumno():
    alumnos = cargar_alumnos_json()
    
    if not validar_alumnos(alumnos):
        print("Error: No hay alumnos para eliminar.")
        return
    
    try:
        legajo_buscado = input("Ingrese el número de legajo del alumno a eliminar: ").strip()
        if not legajo_buscado:
            print("Debe ingresar un legajo válido.")
            return
    except:
        print("Debe ingresar un legajo válido.")
        return

    if legajo_buscado in alumnos:
        datos = alumnos[legajo_buscado]
        print(f"\nAlumno encontrado: {datos.get('nombre', '')} {datos.get('apellido', '')} (Legajo: {legajo_buscado})")
        confirmacion = input("¿Está seguro que desea eliminar este alumno? (s/n): ").strip().lower()
        if confirmacion in ['s', 'si', 'sí', 'y', 'yes']:
            del alumnos[legajo_buscado]
            print("Alumno eliminado con éxito.")
            if guardar_alumnos_json(alumnos):
                print("Cambios guardados en JSON.")
            else:
                print("Error: Los cambios no se pudieron guardar.")
        else:
            print("Operación cancelada. El alumno no fue eliminado.")
    else:
        print(f"No se encontró un alumno con el legajo {legajo_buscado}.")
        print("Use la opción 'Listar alumnos' para ver los legajos disponibles.")

def inicializar_alumnos():
    """Inicializa y valida los alumnos al cargar el módulo"""
    alumnos = cargar_alumnos_json()
    
    # Verificar que no haya legajos duplicados
    legajos = []
    for legajo in alumnos.keys():
        if legajo in legajos:
            print(f"Advertencia: Legajo duplicado encontrado: {legajo}")
        else:
            legajos.append(legajo)

# Inicializar al cargar el módulo
inicializar_alumnos()
            
