#crear matriz con materias 
#funciones para mostrar mostrar materias y agregar materias 

# Pedimos cuántas materias se van a cargar
cantidad_materias = int(input("¿Cuántas materias querés cargar?: "))

# Creamos la matriz vacía con esa cantidad de filas y 2 columnas (nombre y código)
materias = [[None]*2 for i in range(cantidad_materias)]

# Cargamos los datos en la matriz
for i in range(cantidad_materias):
    nombre = input(f"Ingresá el nombre de la materia {i+1}: ")
    codigo = input("Ingresá el código de la materia: ")
    materias[i] = [nombre, codigo]

# Mostramos la matriz cargada
print("Materias cargadas:")
print("Nombre           | Código")
print("-"*30)
for fila in materias:
    print("Materia:", fila[0], "| Código:", fila[1])
