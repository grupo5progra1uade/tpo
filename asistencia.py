from datetime import datetime
from alumnos import *

def cargar_registro_desde_txt():
    registro = []
    bloque = []

    try:
        with open("asistencias.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea = linea.strip()
                if linea == "":
                    if bloque:
                        registro.append(procesar_bloque(bloque))
                        bloque = []
                else:
                    bloque.append(linea)
            if bloque:  # último bloque sin salto al final
                registro.append(procesar_bloque(bloque))
    except FileNotFoundError:
        print("No se encontró el archivo 'asistencias.txt'... se creará al registrar asistencia.")
    
    return registro


def procesar_bloque(bloque_lineas):
    asistencias = []
    fecha = ""
    materia = ""

    for linea in bloque_lineas:
        partes = linea.split(",")  # fecha,materia,legajo,nombre apellido,estado
        if len(partes) < 5:
            continue
        fecha = partes[0].strip()
        materia = partes[1].strip()
        estado = partes[4].strip()

        if estado == "Presente":
            asistencias.append(1)
        elif estado == "Media falta":
            asistencias.append(-1)
        else:
            asistencias.append(0)

    return {"fecha": fecha, "materia": materia, "asistencias": asistencias}


def registrar_asistencia(alumnos, materias_tuple):
    fecha = datetime.today().strftime("%Y-%m-%d")
    
    print("\nSeleccionar materia:")
    for i in range(len(materias_tuple)):
        print(f"{i+1}. {materias_tuple[i]}")

    opcion = None
    while opcion is None:
        entrada = input("Opción: ").strip()
        if entrada.isdigit() and 1 <= int(entrada) <= len(materias_tuple):
            opcion = int(entrada)
        else:
            print("Entrada inválida, intente nuevamente.")

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

    print("Asistencia registrada correctamente y guardada en asistencias.txt.")
    return cargar_registro_desde_txt

def mostrar_asistencia_alumno(matriznx5):
    registro = cargar_registro_desde_txt()
    
    while True:
        try:
            legajo = int(input("Ingrese legajo del alumno: "))
            break
        except ValueError:
            print("Ingrese un numero entero")
            
    indice_alumno = None
    
    #busca indice del alumno
    for i, fila in enumerate(matriznx5):
        if fila[0] == legajo:
            indice_alumno = i
            break

    if indice_alumno is None:
        print("No se encontró un alumno con ese legajo.")
        return

    nombre = matriznx5[indice_alumno][2]
    apellido = matriznx5[indice_alumno][1]
    print(f"Asistencia de {nombre} {apellido}:")
    
    for item in registro:
        if indice_alumno < len(item["asistencias"]):
            estado_num = item["asistencias"][indice_alumno]
            texto = "Presente" if estado_num == 1 else "Media falta" if estado_num == -1 else "Ausente"
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

