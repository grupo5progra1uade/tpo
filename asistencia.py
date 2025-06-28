from datetime import datetime
from alumnos import *
registro = []
asistencias = []


def registrar_asistencia(alumnos, registro, materias_tuple):
    fecha = datetime.today().strftime("%Y-%m-%d")
    
    print("\nSeleccionar materia:")
    for i in range(len(materias_tuple)):
        print(f"{i+1}. {materias_tuple[i]}")

    opcion = None
    while opcion is None:
        entrada = input("Opción: ").strip()

        # Validar que la entrada tenga solo caracteres entre '0' y '9'
        valido = True
        if len(entrada) == 0:
            valido = False
        else:
            for c in entrada:
                if c < '0' or c > '9':
                    valido = False
                    break

        if valido:
            # Convertir a numero
            num = int(entrada) 

            if num >= 1 and num <= len(materias_tuple):
                opcion = num
            else:
                print("Número fuera de rango, intente nuevamente.")
        else:
            print("Entrada inválida, debe ser un número entero positivo.")

    materia = materias_tuple[opcion - 1]
    asistencias_dia = []

    with open("asistencias.txt", "a", encoding="utf-8") as archivo:
        for alumno in alumnos:
            print(f"Alumno: {alumno[2]} {alumno[1]}")
            
            while True:
                estado = input("¿Presente (1), Media falta (-1), Ausente (0)?: ").strip()
                if estado == "1":
                    asistencias_dia.append(1)
                    estado_txt = "Presente"
                    break
                elif estado == "-1":
                    asistencias_dia.append(-1)
                    estado_txt = "Media falta"
                    break
                elif estado == "0":
                    asistencias_dia.append(0)
                    estado_txt = "Ausente"
                    break
                else:
                    print("Entrada inválida. Ingrese 1, -1 o 0.")
            # escribir en el archivo la asistencia del alumno
            archivo.write(f"{fecha},{materia},{alumno[0]},{alumno[2]} {alumno[1]},{estado_txt}\n")
        # salto de línea solo al finalizar la asistencia de todos los alumnos
        archivo.write("\n")

    registro.append({
        "fecha": fecha,
        "materia": materia,
        "asistencias": asistencias_dia
    })
    print("Asistencia registrada correctamente y guardada en asistencias.txt.")

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

