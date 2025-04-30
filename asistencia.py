from datetime import datetime
from alumnos import get_alumnos
registro = []
matriznx5=[]

def crear_matriz():
    filas = int(input("Ingrese el número de alumnos: ")) 
    columnas = 4
    matriznx5.clear()  

    for i in range(filas):
        matriznx5.append([None] * columnas)


def cargar_datos():
    filas = len(matriznx5)
    
    def letras_validas(texto):
        if not texto:  # Si texto está vacío
            return False
        for c in texto:
            if not (c.isalpha() or c in " -"):
                return False
        return True

    def asistencia_valida(valor):
        if valor.startswith('-'):
            return valor[1:].isdigit()
        return valor.isdigit()

    def capitalizar(texto):
        return " ".join([palabra.capitalize() for palabra in texto.split(" ")])

    legajos_existentes = [fila[0] for fila in matriznx5 if fila[0] is not None]

    for fila in range(filas):
        while True:
            legajo = input("Ingrese nro de legajo: ").strip()
            
            es_numero = True
            for c in legajo:
                if c not in "0123456789":
                    es_numero = False
                    break
            
            if es_numero and legajo:  
                legajo = int(legajo)
                if legajo in legajos_existentes:
                    print("Legajo repetido, ingrese otro.")
                else:
                    legajos_existentes.append(legajo)
                    break
            else:
                print("Ingrese un número válido de legajo.")

        while True:
            apellido = input("Ingrese apellido del alumno: ").strip()
            if apellido and letras_validas(apellido):
                apellido = capitalizar(apellido)
                break
            else:
                print("Apellido inválido o vacío, vuelva a ingresarlo.")
                
        while True:
            nombre = input("Ingrese nombre del alumno: ").strip()
            if nombre and letras_validas(nombre):
                nombre = capitalizar(nombre)
                break
            else:
                print("Nombre inválido o vacío, vuelva a ingresarlo.")
                
        fecha = datetime.today().strftime("%Y-%m-%d")

        while True:
            presente = input("Ingrese 0.Ausente -1.Media asistencia 1.Presente: ").strip()
            if asistencia_valida(presente):
                presente = int(presente)
                if presente in [-1, 0, 1]:
                    break
                else:
                    print("Valor de asistencia incorrecto, vuelva a ingresarlo.")
            else:
                print("Valor inválido, ingrese un número (-1, 0, 1).")

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

    # ordenar la matriz x apellido
    for i in range(len(matriznx5) - 1):
        for j in range(len(matriznx5) - i - 1):
            if matriznx5[j][1].lower() > matriznx5[j + 1][1].lower(): # Comparar apellidos en minúsculas
                matriznx5[j], matriznx5[j + 1] = matriznx5[j + 1], matriznx5[j]

    #imprimir la matriz ordenada
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
 

def registrar_asistencia(alumnos, registro, materias_tuple):
    
    fecha = datetime.today().strftime("%Y-%m-%d")
    asistencias = []
    
    print("\nSeleccionar materia:")
    for i in range(len(materias_tuple)):
        print(f"{i+1}. {materias_tuple[i]}")

    opcion = None
    while opcion is None:
        entrada = input("Opción: ").strip()

        #Validar que la entrada tenga solo caracteres entre '0' y '9'
        valido = True
        if len(entrada) == 0:
            valido = False
        else:
            for c in entrada:
                if c < '0' or c > '9':
                    valido = False
                    break

        if valido:
            #Convertir a numero
            num = int(entrada) 

            if num >= 1 and num <= len(materias_tuple):
                opcion = num
            else:
                print("Número fuera de rango, intente nuevamente.")
        else:
            print("Entrada inválida, debe ser un número entero positivo.")

    materia = materias_tuple[opcion - 1]

    for alumno in alumnos:
        print(f"Alumno: {alumno[2]} {alumno[1]}")
        
        while True:
            estado = input("¿Presente (1), Media falta (-1), Ausente (0)?: ").strip()
            if estado == "1":
                asistencias.append(1)
                break
            elif estado == "-1":
                asistencias.append(-1)
                break
            elif estado == "0":
                asistencias.append(0)
                break
            else:
                print("Entrada inválida. Ingrese 1, -1 o 0.")
    
    registro.append({
    "fecha": fecha,
    "materia": materia,
    "asistencias": asistencias
    })
    print("Asistencia registrada correctamente.")


def mostrar_asistencia_alumno(registro, matriznx5): 
    legajo = int(input("Ingrese legajo del alumno: "))
    indice_alumno = None
    
    #busca indice del alumno
    for i in range(len(matriznx5)):
        if matriznx5[i][0] == legajo:
            indice_alumno = i
            break

    if indice_alumno is None:
        print("No se encontró un alumno con ese legajo.")
        return

    print(f"Asistencia de {matriznx5[indice_alumno][2]} {matriznx5[indice_alumno][1]}:")
    
    for item in registro:
        if len(item['asistencias']) > indice_alumno:
            estado = item['asistencias'][indice_alumno]
            if estado == 1:
                texto = "Presente"
            elif estado == -1:
                texto = "Media falta"
            else:
                texto = "Ausente"
            print(f"Materia: {item['materia']} | Fecha: {item['fecha']} - {texto}")

def mostrar_asistencia_general(registro):
    print("\nResumen general de asistencias:")
    
    for item in registro:  
        asistencias = item['asistencias']
        total = len(asistencias)
        presentes = 0
        medias = 0
    
        for a in asistencias:
            if a == 1:
                presentes += 1
            elif a == -1:
                medias += 1
    
        ausentes = total - presentes - medias
        porcentaje = (presentes + medias * 0.5) / total * 100 if total > 0 else 0
    
        print(f"\nMateria: {item['materia']} | Fecha: {item['fecha']}")
        print(f"Presentes: {presentes} | Medias faltas: {medias} | Ausentes: {ausentes}")
        print(f"Asistencia efectiva: {porcentaje:.2f}%")



