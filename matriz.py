from datetime import datetime

matriz4x4=[]

def crear_matriz():
    filas= 2
    columnas=4
    #lo habia hecho asi con la forma que dijo el profe pero pero bueno era mas orientado a los numero 
    #agregabamos append 0 en cad iteracion

    #for fila in range(filas):
        #matriz5x5.append([])  
     #   for columna in range(columnas):
      #      matriz5x5[fila].append(0)
    
    #.... forma simple
    for fila in range(filas):
         matriz4x4.append([None]* columnas) #agrega none a cada fila *columna osea todo none


def cargar_datos():
    filas=len(matriz4x4)

    for fila in range(filas):
        nombre= input("Ingrese nombre del alumno:")
        legajo= int(input("Ingrese nro de legajo:"))
        fecha= datetime.today().strftime("%Y-%m-%d")
        presente= int(input("Ingrese 0.Ausente -1.Media asistencia 1.Presente"))
        
        matriz4x4[fila]= [nombre,legajo,fecha,presente]

   

def imprimir_matriz_practica():
    for fila in matriz4x4:
            print(fila)

def imprimir_matriz_ordenada():
    print("Registro de asistencia")
    print("Nombre    |Legajo | Fecha      | Presente")
    print("-"* 50)

    for fila in matriz4x4:
        print(f"{fila[0]:<10} | {fila[1]:<6} | {fila[2]} | {fila[3]:<8}")

# funcion ordenar
def ordenar(matriz):
     matriz.sort()
     return matriz
      

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
imprimir_matriz_ordenada()
print("lista ordenada", ordenar(matriz4x4))