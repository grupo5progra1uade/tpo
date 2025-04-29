from materias import mostrar_materias, agregar_materia, materias_tuple
from asistencia import registrar_asistencia, mostrar_asistencia_alumno, mostrar_asistencia_general
from alumnos import *
from utils import mostrar_menu

def main():
    materias = []
    matriznx5
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
            registrar_asistencia(matriznx5, asistencias, materias)
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

def consultar_asistencias(asistencias):
    while True:
       
        mostrar_menu("Asistencias", [
            "Por alumno",
            "Listado general",
            "Volver"
        ])
        
        opcion = input("Opción: ").strip()
        
        if opcion == "1":
            mostrar_asistencia_alumno(asistencias, matriznx5)
        elif opcion == "2":
            mostrar_asistencia_general(asistencias)
        elif opcion == "3":
            return
        else:
            input("Opción inválida. Presione Enter...")

if __name__ == "__main__":
    main()