from datetime import datetime

matriznx5=[]

def crear_matriz():
    filas = int(input("Ingrese el número de alumnos: ")) 
    columnas = 4
    matriznx5.clear()  

    for i in range(filas):
        matriznx5.append([None] * columnas) 
     


def cargar_datos():
    filas = len(matriznx5)

    for fila in range(filas):
        legajo = int(input("Ingrese nro de legajo: "))  
        apellido = input("Ingrese apellido del alumno: ")
        nombre = input("Ingrese nombre del alumno: ")
        fecha = datetime.today().strftime("%Y-%m-%d")
        presente = int(input("Ingrese 0.Ausente -1.Media asistencia 1.Presente: "))
        
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



# funcion ordenar
def imprimir_matriz_ordenada_por_apellido():
    print("Registro de asistencia (Ordenado por Apellido)")
    print("Legajo | Apellido   | Nombre    | Fecha      | Presente")
    print("-" * 60)

    # ordenar la matriz manualmente por el segundo elemento (apellido)
    for i in range(len(matriznx5) - 1):
        for j in range(len(matriznx5) - i - 1):
            if matriznx5[j][1].lower() > matriznx5[j + 1][1].lower(): # Comparar apellidos en minúsculas
                matriznx5[j], matriznx5[j + 1] = matriznx5[j + 1], matriznx5[j]

    # imprimir la matriz ordenada
    for fila in matriznx5:
        print(f"{fila[0]:<6} | {fila[1]:<10} | {fila[2]:<10} | {fila[3]} | {fila[4]:<8}")

#funcion de asistencia
def asistencia(presente):
     total_asistencia=0
     if presente==1:
          total_asistencia =+1
     if  presente==-1:
          total_asistencia+=0.5
     else: presente==0
 
crear_matriz()
cargar_datos()
imprimir_matriz_practica()
imprimir_matriz()
print("lista ordenada", imprimir_matriz_ordenada_por_apellido())