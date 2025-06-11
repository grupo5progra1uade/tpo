from datetime import datetime
from alumnos import *
registro = []
asistencias = []
"""
# Precarga de asistencias relacionadas con los alumnos de alumnos.py
registro.extend([
    {
        "fecha": "2024-08-20",
        "materia": "Matemática",
        "asistencias": [
            1,   # Ana López (presente)
            0,   # Bruno Martínez (ausente)
            -1,  # Clara Ramírez (media falta)
            1,   # Diego Suárez (presente)
            0    # Elena Fernández (ausente)
        ]
    },
    {
        "fecha": "2024-08-21",
        "materia": "Programación",
        "asistencias": [
            -1,  # Ana López (media falta)
            1,   # Bruno Martínez (presente)
            1,   # Clara Ramírez (presente)
            0,   # Diego Suárez (ausente)
            1    # Elena Fernández (presente)
        ]
    }
])
"""
#comento asistencia precargada

def registrar_asistencia(alumnos, registro, materias_tuple):
    
    fecha = datetime.today().strftime("%Y-%m-%d")
    
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
    while True:
        try:
            legajo = int(input("Ingrese legajo del alumno: "))
            break
        except ValueError:
            print("Ingrese un numero entero")
            
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
def modificar_asistencia_alumno(registro, materias, matriznx5):
    try:
        legajo = int(input("Ingrese legajo del alumno: "))
    except ValueError:
        print("Legajo inválido.")
        return

    # Buscar alumno y su índice
    indice_alumno = -1
    for i in range(len(matriznx5)):
        if matriznx5[i][0] == legajo:
            indice_alumno = i
            alumno = matriznx5[i]
            break

    if indice_alumno == -1:
        print("Alumno no encontrado.")
        return

    print(f"\nAsistencias registradas para {alumno[2]} {alumno[1]}:")

    for i in range(len(registro)):
        print(f"{i + 1}. {registro[i]['materia']} - {registro[i]['fecha']}")

    try:
        opcion = int(input("Seleccione una opción: ")) - 1
        if opcion < 0 or opcion >= len(registro):
            print("Opción fuera de rango.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    asistencias = registro[opcion]['asistencias']

    if indice_alumno >= len(asistencias):
        print("No hay registro de asistencia para este alumno en esa materia.")
        return

    try:
        nuevo_estado = int(input("Ingrese nuevo estado (1 = presente, 0 = ausente, -1 = media falta): "))
        if nuevo_estado in [1, 0, -1]:
            asistencias[indice_alumno] = nuevo_estado
            print("Asistencia modificada con éxito.")
        else:
            print("Estado inválido.")
    except ValueError:
        print("Entrada inválida.")


