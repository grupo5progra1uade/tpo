from datetime import datetime

matriznx5 = []

def crear_matriz():
    filas = int(input("Ingrese el número de alumnos: ")) 
    columnas = 4
    matriznx5.clear()

    for i in range(filas):
        matriznx5.append([None] * columnas)

def cargar_datos():
    filas = len(matriznx5)
    
    def letras_validas(texto):
        for c in texto:
            if not (c.isalpha() or c in " -"):
                return False
        return True

    def asistencia(valor):
        if valor.startswith('-'):
            return valor[1:].isdigit()
        return valor.isdigit()

    def capitalizar(texto):
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

def imprimir_matriz_ordenada_por_apellido():
    print("Registro de asistencia (Ordenado por Apellido)")
    print("Legajo | Apellido   | Nombre    | Fecha      | Presente")
    print("-" * 60)

def get_alumnos():
    return matriznx5


    for i in range(len(matriznx5) - 1):
        for j in range(len(matriznx5) - i - 1):
            if matriznx5[j][1].lower() > matriznx5[j + 1][1].lower():
                matriznx5[j], matriznx5[j + 1] = matriznx5[j + 1], matriznx5[j]

    for fila in matriznx5:
        print(f"{fila[0]:<6} | {fila[1]:<10} | {fila[2]:<10} | {fila[3]} | {fila[4]:<8}")

def gestion_alumnos():
    crear_matriz()
    cargar_datos()
    imprimir_matriz_ordenada_por_apellido()

def mostrar_alumnos():
    imprimir_matriz()

def ordenar_por_apellido():
    imprimir_matriz_ordenada_por_apellido()
