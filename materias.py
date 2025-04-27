#crear matriz con materias 
#funciones para mostrar mostrar materias y agregar materias 

materias = []  #solo guarda nombre de las materias

def cargar_materias(lista_materias):
    cantidad = int(input("¿Cuántas materias querés cargar?: "))
    for _ in range(cantidad):
        nombre = input("Nombre de la materia: ").capitalize()
        lista_materias.append(nombre)
    return lista_materias

def mostrar_materias(lista_materias):
    print("\nMaterias del curso:")
    for i in range(len(lista_materias)):
        print(f"{i+1}. {lista_materias[i]}")

def agregar_materia(lista_materias):
    nueva = input("Nombre de la nueva materia: ").capitalize()
    if nueva not in lista_materias:
        lista_materias.append(nueva)
        print("Materia agregada!")
    else:
        print("Ya existe!")
    return lista_materias

#Convertir la lista de materias en una tupla (inmutable)
materias_tuple = tuple([materia[0] for materia in materias]) # Solo tomamos los nombres de las materias
