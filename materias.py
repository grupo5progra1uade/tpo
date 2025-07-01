import json
from alumnos import get_alumnos

ARCHIVO_MATERIAS = "materias.json"

# Intenta cargar el archivo, y si no existe, lo crea con datos iniciales
def cargar_materias():
    try:
        with open(ARCHIVO_MATERIAS, "r", encoding="utf-8") as archivo:
            data = json.load(archivo)
            if "asistencias" not in data:
                data["asistencias"] = {}
                for materia in data["materias"]:
                    data["asistencias"][materia] = [
                        [alumno[0], 0] for alumno in get_alumnos()
                    ]
            return data
    except FileNotFoundError:
        # Si no existe, lo crea con valores iniciales
        materias = ["Matematica", "Historia", "Programacion"]
        data = {
            "materias": materias,
            "asistencias": {}
        }
        for materia in materias:
            data["asistencias"][materia] = [
                [alumno[0], 0] for alumno in get_alumnos()
            ]
        guardar_materias(data)
        return data
    
def guardar_materias(data):
    solo_materias = {
        "materias": data["materias"]
    }
    with open(ARCHIVO_MATERIAS, "w", encoding="utf-8") as archivo:
        json.dump(solo_materias, archivo, indent=4)

# Precarga de materias
materias = ["Matematica", "Historia", "Programacion"]


# Precarga de asistencias relacionadas con los alumnos de alumnos.py
asistencias_por_materia = {
    "Matematica": [
        [1001, 1], [1002, 0], [1003, -1], [1004, 1], [1005, 0]
    ],
    "Historia": [
        [1001, 1], [1002, 1], [1003, 1], [1004, 0], [1005, -1]
    ],
    "Programacion": [
        [1001, -1], [1002, 0], [1003, 1], [1004, 1], [1005, 1]
    ]
}


# Traemos alumnos precargados
alumnos_precargados = get_alumnos()

# Precargamos asistencia para cada materia usando el estado del alumno
for materia in materias:
    asistencias_por_materia[materia] = [
        [alumno[0], 0] for alumno in alumnos_precargados  # Inicializa el estado en 0 (ausente) o el valor que corresponda
    ]

def mostrar_materias():
    data = cargar_materias()
    print("\nMaterias del curso:")
    for i, materia in enumerate(data["materias"]):
        print(f"{i+1}. {materia}")


def mostrar_asistencias_por_materia():
    data = cargar_materias()
    asistencias_por_materia = data["asistencias"]
    alumnos_dict = {alumno[0]: f"{alumno[2]} {alumno[1]}" for alumno in get_alumnos()}

    for materia, asistencias in asistencias_por_materia.items():
        print(f"\n Asistencias registradas para: {materia}")
        print("Legajo | Nombre              | Estado")
        print("-" * 40)
        for legajo, estado in asistencias:
            nombre = alumnos_dict.get(legajo, "Desconocido")
            estado_str = (
                "Presente" if estado == 1 else
                "Ausente" if estado == 0 else
                "Media falta" if estado == -1 else
                "Sin registro"
            )
            print(f"{legajo:<6} | {nombre:<20} | {estado_str}")


def agregar_materia():
    data = cargar_materias()
    while True:
        try:
            nueva = input("Nombre de la nueva materia: ").strip().capitalize()

            # Validar si está vacía
            if not nueva:
                print("La materia no puede estar vacía.")
                continue

            # Validar que todas las palabras sean letras
            for palabra in nueva.split():
                if not palabra.isalpha():
                    raise ValueError("La materia debe contener solo letras y espacios.")

            # Verificar si ya existe
            if nueva in data["materias"]:
                print("¡Ya existe!")
            else:
                data["materias"].append(nueva)
                data["asistencias"][nueva] = [
                    [alumno[0], 0] for alumno in get_alumnos()
                ]
                guardar_materias(data)
                print("¡Materia agregada!")
                return

        except ValueError as error:
            print(f"Error: {error}. Vuelva a ingresar la materia.")

def borrar_materia():
    data = cargar_materias()
    materia_a_borrar = input("Nombre de la materia a borrar: ").strip().capitalize()
    
    if materia_a_borrar in data["materias"]:
        confirmacion = input(f"¿Está seguro que desea eliminar la materia '{materia_a_borrar}'? (s/n): ").strip().lower()
        if confirmacion == "s":
            data["materias"].remove(materia_a_borrar)
            data["asistencias"].pop(materia_a_borrar, None)
            guardar_materias(data)
            print("¡Materia eliminada con éxito!")
        else:
            print("Operación cancelada. La materia no fue eliminada.")      
    else:
        print("La materia no existe en la lista.")
    
    return


def registrar_asistencia_en_materia(nombre_materia):
    data = cargar_materias()
    
    if nombre_materia not in data["materias"]:
        print("Esa materia no existe.")
        return

    print(f"\nRegistrando asistencia para: {materias}")
    print("1 = presente, 0 = ausente, -1 = media falta\n")

    registros = []
    for alumno in get_alumnos():
        legajo = alumno[0]
        nombre_completo = f"{alumno[2]} {alumno[1]}"
        while True:
            estado = input(f"Asistencia de {nombre_completo} (legajo {legajo}): ")
            if estado in ["1", "0", "-1"]:
                registros.append([legajo, int(estado)])
                break
            else:
                print("Valor inválido. Usá 1, 0 o -1.")
    
    data["asistencias"][nombre_materia] = registros
    guardar_materias(data)
    print("Asistencia registrada con éxito!")
