#crear matriz con materias 
#funciones para mostrar mostrar materias y agregar materias 

materias = []  # Variable global para almacenar las materias

def cargar_materias():
    global materias
    cantidad_materias = int(input("¿Cuántas materias querés cargar?: "))
    materias = []

    for i in range(cantidad_materias):
        nombre = input(f"Ingresá el nombre de la materia {i+1}: ")
        codigo = input("Ingresá el código de la materia: ")
        materias.append([nombre, codigo])

    print("Materias cargadas:")
    print("Nombre           | Código")
    print("-"*30)
    for fila in materias:
        print("Materia:", fila[0], "| Código:", fila[1])

def mostrar_materias(lista_materias):
    print("\nMaterias del curso:")
    for i, materia in enumerate(lista_materias, 1):
        print(f"{i}. {materia}")

def agregar_materia(lista_materias):
    nueva = input("Nombre de la nueva materia: ").capitalize()
    if nueva not in lista_materias:
        lista_materias.append(nueva)
        print("¡Materia agregada con éxito!")
    else:
        print("¡La materia ya existe!")
    return lista_materias