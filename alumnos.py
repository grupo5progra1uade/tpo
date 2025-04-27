from datetime import datetime
from utils import *
from functools import reduce


matriznx5 = []

def crear_matriz():
    filas = int(input("Ingrese el número de alumnos: ")) 
    columnas = 4
    matriznx5.clear()

    for i in range(filas):
        matriznx5.append([None] * columnas)

def cargar_datos():
    filas = len(matriznx5)

    legajos_existentes = {fila[0] for fila in matriznx5 if fila[0] is not None}
    
    def letras_validas(texto):
        for c in texto:
            if not (c.isalpha() or c in " -"):
                return False
        return True

    def asistencia(valor):
        if valor.startswith('-'):
            return valor[1:].isdigit()
        return valor.isdigit()

    def capitalizar(texto):
        return " ".join([palabra.capitalize() for palabra in texto.split(" ")])

    legajos_existentes = set()  # Conjunto para controlar legajos únicos

    for fila in range(filas):
        while True:
            try:
                legajo = int(input("Ingrese nro de legajo: "))
                if legajo in legajos_existentes:
                    print("¡Legajo ya existente! Ingrese otro.")
                else:
                    legajos_existentes.add(legajo)
                    break
            except ValueError:
                print("Debe ingresar un número válido.")

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
        # Extraigo año, mes y día con slicing
        año, mes, día = fecha[:4], fecha[5:7], fecha[8:]
        print(f"[DEBUG] Año: {año}, Mes: {mes}, Día: {día}")


        while True:
            presente = input("Ingrese 0.Ausente -1.Media asistencia 1.Presente: ").strip()
            if asistencia(presente):
                presente = int(presente)
                if presente in [-1, 0, 1]:
                    break
                else:
                    print("Ingreso incorrectamente el valor de la falta, vuelva a ingresarla.")
            else:
                print("Ingrese un número válido (-1, 0 o 1).")

        matriznx5[fila] = [legajo, apellido, nombre, fecha, presente]

def imprimir_matriz_practica():
    for fila in matriznx5:
        print(fila)

def imprimir_matriz():
    print("Registro de asistencia")
    print("Legajo | Apellido   | Nombre    | Fecha      | Presente")
    print("-" * 60)
    for fila in matriznx5:
        print(f"{fila[0]:<6} | {fila[1]:<10} | {fila[2]:<10} | {fila[3]} | {fila[4]:<8}")

def imprimir_matriz_ordenada_por_apellido():
    print("Registro de asistencia (Ordenado por Apellido)")
    print("Legajo | Apellido   | Nombre    | Fecha      | Presente")
    print("-" * 60)

    alumnos_ordenados = sorted(matriznx5, key=lambda alumno: alumno[1].lower())

    for fila in alumnos_ordenados:
        print(f"{fila[0]:<6} | {fila[1]:<10} | {fila[2]:<10} | {fila[3]} | {fila[4]:<8}")

def buscar_alumno_por_legajo():
    legajo_buscado = int(input("Ingrese el número de legajo a buscar: "))
    encontrado = False
    for fila in matriznx5:
        if fila[0] == legajo_buscado:
            print("\nAlumno encontrado:")
            print(f"Legajo: {fila[0]} - Apellido: {fila[1]} - Nombre: {fila[2]} - Fecha: {fila[3]} - Presente: {fila[4]}")
            encontrado = True
            break
    if not encontrado:
        print("No se encontró un alumno con ese legajo.")


def get_alumnos():
    return matriznx5


    for i in range(len(matriznx5) - 1):
        for j in range(len(matriznx5) - i - 1):
            if matriznx5[j][1].lower() > matriznx5[j + 1][1].lower():
                matriznx5[j], matriznx5[j + 1] = matriznx5[j + 1], matriznx5[j]

    for fila in matriznx5:
        print(f"{fila[0]:<6} | {fila[1]:<10} | {fila[2]:<10} | {fila[3]} | {fila[4]:<8}")

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
            crear_matriz()
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
def mostrar_alumnos():
    imprimir_matriz()

def ordenar_por_apellido():
    imprimir_matriz_ordenada_por_apellido()

# Función que devuelve una lista con los nombres completos de los alumnos
# Se usa map() para aplicar una función lambda que combina el nombre (a[2]) y el apellido (a[1]) de cada alumno

def nombres_completos():
    return list(map(lambda a: f"{a[2]} {a[1]}", matriznx5))

def alumnos_presentes():
    return list(filter(lambda a: a[4] == 1, matriznx5))

# Función que calcula la asistencia total ponderada de todos los alumnos
# Se usa reduce() para recorrer todos los registros y sumar las asistencias ponderadas:
#   1 para presente (a[4] == 1), 0.5 para media falta (a[4] == -1) y 0 para ausente (a[4] == 0)
def asistencia_total_ponderada():
    return reduce(
        lambda acc, a: acc + (1 if a[4] == 1 else 0.5 if a[4] == -1 else 0),
        matriznx5,
        0
    )

def matriz_a_dict_alumnos(matriz):
    """
    Convierte cualquier matriz de alumnos (listas de listas) en un
    diccionario con legajo como clave.
    """
    return {
        fila[0]: {
            "apellido": fila[1],
            "nombre":   fila[2],
            "fecha":    fila[3],
            "estado":   fila[4]
        }
        for fila in matriz
    }
