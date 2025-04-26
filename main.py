from materias import mostrar_materias, agregar_materia
from asistencia import registrar_asistencia, mostrar_asistencia_alumno, mostrar_asistencia_general
from alumnos import gestion_alumnos, mostrar_alumnos, ordenar_por_apellido
from utils import mostrar_menu  #hay ver q hacemos con este archivo y q funciones metemos

def main():
    materias = [] #como definiamos las materias? poniamos algunas ya de por si? o dejamos vacio?
    alumnos = matriznx5
    asistencias = []

    while True:
        mostrar_menu("Sistema de Asistencia", [
            "Gestión de Alumnos",
            "Gestión de Materias",
            "Registrar Asistencia",
            "Consultar Asistencias",
            "Salir"
        ])
        
        opcion = input("Opción: ").strip()
        
        if opcion == "1":
            gestion_alumnos()
        elif opcion == "2":
            gestion_materias(materias)
        elif opcion == "3":
            registrar_asistencia(alumnos, asistencias)
        elif opcion == "4":
            consultar_asistencias(asistencias)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            input("Opción inválida. Presione Enter...")

def gestion_materias(materias):
    while True:
        
        mostrar_menu("Materias", [
            "Listar materias",
            "Agregar materia",
            "Volver"
        ])
        
        opcion = input("Opción: ").strip()
        
        if opcion == "1":
            mostrar_materias(materias)
        elif opcion == "2":
            agregar_materia(materias)
        elif opcion == "3":
            return
        else:
            input("Opción inválida. Presione Enter...")

def agregar_materias(materias):
    nueva = input("Nombre de la nueva materia: ").capitalize()
    if nueva not in materias:
        materias.append(nueva)
        print(f"Materia {nueva} agregada!")
    else:
        print("¡La materia ya existe!")
    input("Presione Enter para continuar...")
    return materias

def consultar_asistencias(asistencias):
    while True:
       
        mostrar_menu("Asistencias", [
            "Por alumno",
            "Listado general",
            "Volver"
        ])
        
        opcion = input("Opción: ").strip()
        
        if opcion == "1":
            mostrar_asistencia_alumno(asistencias)
        elif opcion == "2":
            mostrar_asistencia_general(asistencias)
        elif opcion == "3":
            return
        else:
            input("Opción inválida. Presione Enter...")

if __name__ == "__main__":
    main()