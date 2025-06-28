from alumnos import get_alumnos

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


def mostrar_materias(lista_materias):
    print("\nMaterias del curso:")
    for i, materia in enumerate(lista_materias):
        print(f"{i+1}. {materia}")


def mostrar_asistencias_por_materia():
    if not asistencias_por_materia:
        print("\nNo hay asistencias registradas.")
        return

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



def agregar_materia(lista_materias):
    while True:
        try:
            nueva = input("Nombre de la nueva materia: ").capitalize()
    
            for palabra in nueva.split(): #separa el string para escribir materias de dos palabras
                if not palabra.isalpha():
                    raise ValueError("La materia debe contener solo letras y espacios")
    
            if nueva not in lista_materias:
                lista_materias.append(nueva)
                asistencias_por_materia[nueva] = []
                print("Materia agregada!")
            else:
                print("Ya existe!")
            return lista_materias
        except ValueError as error:
            print(f"Error: {error}. Vuelva a ingresar la materia")

def borrar_materia(lista_materias):
    materia_a_borrar = input("Nombre de la materia a borrar: ").strip().capitalize()
    
    materia_encontrada = None
    for materia in lista_materias:
        if materia == materia_a_borrar:
            materia_encontrada = materia
            break
    
    if materia_encontrada:
        confirmacion = input(f"¿Está seguro que desea eliminar la materia '{materia_encontrada}'? (s/n): ").strip().lower()
        if confirmacion == "s":
            lista_materias.remove(materia_encontrada)
            asistencias_por_materia.pop(materia_encontrada, None)
            print("¡Materia eliminada con éxito!")
        else:
            print("Operación cancelada. La materia no fue eliminada.")
    else:
        print("La materia no existe en la lista.")
    
    return lista_materias


def registrar_asistencia_en_materia(materias, alumnos):
    if materias not in asistencias_por_materia:
        print("Esa materia no existe.")
        return

    print(f"\nRegistrando asistencia para: {materias}")
    print("1 = presente, 0 = ausente, -1 = media falta\n")

    registros = []
    for alumno in alumnos:
        legajo = alumno[0]
        nombre_completo = f"{alumno[2]} {alumno[1]}"
        while True:
            estado = input(f"Asistencia de {nombre_completo} (legajo {legajo}): ")
            if estado in ["1", "0", "-1"]:
                registros.append([legajo, int(estado)])
                break
            else:
                print("Valor inválido. Usá 1, 0 o -1.")
    
    asistencias_por_materia[materias] = registros
    print("Asistencia registrada con éxito.")
