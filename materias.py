materias = []  # solo guarda nombres de materias
asistencias_por_materia = {}  # materia -> lista de [legajo, estado]

def cargar_materias(lista_materias):
    cantidad = int(input("¿Cuántas materias querés cargar?: "))
    for _ in range(cantidad):
        nombre = input("Nombre de la materia: ").capitalize()
        if nombre not in lista_materias:
            lista_materias.append(nombre)
            asistencias_por_materia[nombre] = []  # inicializa lista vacía
    return lista_materias

def mostrar_materias(lista_materias):
    print("\nMaterias del curso:")
    for i, materia in enumerate(lista_materias):
        print(f"{i+1}. {materia}")

def agregar_materia(lista_materias):
    nueva = input("Nombre de la nueva materia: ").capitalize()
    if nueva not in lista_materias:
        lista_materias.append(nueva)
        asistencias_por_materia[nueva] = []
        print("Materia agregada!")
    else:
        print("Ya existe!")
    return lista_materias

def borrar_materia(lista_materias):
    materia_a_borrar = input("Nombre de la materia a borrar: ").capitalize()
    if materia_a_borrar in lista_materias:
        lista_materias.remove(materia_a_borrar)
        asistencias_por_materia.pop(materia_a_borrar, None)
        print("Materia eliminada con éxito!")
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

def menu_materias(lista_materias, alumnos):
    while True:
        print("\n--- Gestión de Materias ---")
        print("1. Mostrar materias")
        print("2. Cargar materias")
        print("3. Agregar materia")
        print("4. Borrar materia")
        print("5. Tomar asistencia en una materia")
        print("6. Volver")
        opcion = input("Elegí una opción: ")

        if opcion == "1":
            mostrar_materias(lista_materias)
        elif opcion == "2":
            cargar_materias(lista_materias)
        elif opcion == "3":
            agregar_materia(lista_materias)
        elif opcion == "4":
            borrar_materia(lista_materias)
        elif opcion == "5":
            mostrar_materias(lista_materias)
            materia = input("Ingresá el nombre exacto de la materia: ").capitalize()
            registrar_asistencia_en_materia(materia, alumnos)
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")
