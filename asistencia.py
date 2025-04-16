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
    
    def letras_validas(texto): #funcion para que no se puedan ingresar caracteres que no sean correspondientes a un nombre
        for c in texto:
            if not (c.isalpha()or c in " -"):
                return False
        return True
    
    def asistencia(valor): #verifica que se ingrese solo (-1, 0, 1)
        if valor.startswith('-'):
            return valor[1:].isdigit()
        return valor.isdigit()
    
    def capitalizar(texto): #funcion para escribir la mayuscula en caso de que no se cargue correctamente
        return " ".join([palabra.capitalize() for palabra in texto.split(" ")])

    for fila in range(filas):
        legajo = int(input("Ingrese nro de legajo: "))
        
        while True:
            apellido = input("Ingrese apellido del alumno: ").strip()
            if letras_validas(apellido):
                apellido = capitalizar(apellido)
                break
            else:
                print("Ingreso mal un apellido, vuelva a ingresarlo")
                
        while True:
            nombre = input("Ingrese nombre del alumno: ").strip()
            if letras_validas(nombre):
                nombre = capitalizar(nombre)
                break
            else:
                print("Ingreso mal un nombre, vuelva a ingresarlo")
                
        fecha = datetime.today().strftime("%Y-%m-%d")
        
        while True:
            presente = input("Ingrese 0.Ausente -1.Media asistencia 1.Presente: ").strip()
            if asistencia(presente):
                presente = int(presente)
                if presente in [-1, 0, 1]:
                    break
                else:
                    print("Ingreso incorrectamente el valor de la falta, vuelva a ingresarla")
        
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
 

def registrar_asistencia(alumnos, registro):
    fecha_actual = datetime.now().strftime("%Y - %m - %d")
    asistencias = []
    for alumno in alumnos:
        print(f"Alumno: {alumno[2]} {alumno[1]}")
        estado = input("¿Presente? (s/n): ").lower()
        asistencias.append(1 if estado == 's' else 0)
    registro.append([fecha_actual, asistencias])
    print("Asistencia registrada")

def mostrar_asistencia_alumno(registro):
    legajo = int(input("Ingrese legajo del alumno: "))
    for fecha, asistencias in registro:
        print(f"Fecha: {fecha} - {'Presente' if asistencias[legajo] == 1 else 'Ausente'}")

def mostrar_asistencia_general(registro):
    for fecha, asistencias in registro:
        print(f"\nFecha: {fecha}")
        print(f"Presentes: {sum(asistencias)}/{len(asistencias)}")


def gestion_alumnos():
    crear_matriz()
    cargar_datos()
    imprimir_matriz_ordenada_por_apellido()

def mostrar_alumnos():
    imprimir_matriz()

def ordenar_por_apellido():
    imprimir_matriz_ordenada_por_apellido()


crear_matriz()
cargar_datos()
imprimir_matriz_practica()
imprimir_matriz()
print("lista ordenada", imprimir_matriz_ordenada_por_apellido())