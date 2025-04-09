from datetime import datetime

matriz5x5=[]

def crear_matriz():
    filas= 5
    columnas=5
    # Lo habia hecho asi con la forma que dijo el profe pero pero bueno era mas orientado a los numeros.
    #agregabamos append 0 en cad iteracion

    #for fila in range(filas):
        #matriz5x5.append([])  
     #   for columna in range(columnas):
      #      matriz5x5[fila].append(0)
    
    #.... forma simple
    for fila in range(filas):
         matriz5x5.append([None]* columnas) #agrega none a cada fila *columna osea todo none


def cargar_datos():
    filas=len(matriz5x5)

    for fila in range(filas):
        nombre= input("Ingrese nombre del alumno:")
        legajo= int(input("Ingrese nro de legajo:"))
        fecha= datetime.today().strftime("%Y-%m-%d")
        presente= int(input("Ingrese 0.Ausente 1.Presente"))
        mediafalta= int(input("Mediafalta: 1.No 2. Si"))
        
        matriz5x5[fila]= [nombre,legajo,fecha,presente,mediafalta]
    
           

def imprimir_matriz_practica():
    for fila in matriz5x5:
            print(fila)

def imprimir_matriz_ordenada():
    print("Registro de asistencia")
    print("Nombre    |Legajo | Fecha      | Presente | Media Falta")
    print("-"* 50)

    for fila in matriz5x5:
        print(f"{fila[0]:<10} | {fila[1]:<6} | {fila[2]} | {fila[3]:<8} | {fila[4]:<10}")


crear_matriz()
cargar_datos()
imprimir_matriz_practica()
imprimir_matriz_ordenada()

