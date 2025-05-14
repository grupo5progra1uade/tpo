from materias import mostrar_materias, agregar_materia, borrar_materia
from asistencia import mostrar_asistencia_alumno, mostrar_asistencia_general
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
            "Consultar Asistencias",
            "Salir"
        ])
        
        opcion = input("Opción: ").strip()
        
        if opcion == "1":
            gestion_alumnos()
        elif opcion == "2":
            gestion_materias(materias)
        elif opcion == "3":
            consultar_asistencias(asistencias)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            input("Opción inválida. Presione Enter...")

def gestion_alumnos():
    while True:
        mostrar_menu("Gestión de Alumnos", [
            "Crear y cargar alumnos",
            "Listar alumnos",
            "Ordenar alumnos por apellido",
            "Buscar alumno por legajo",
            "Modificar alumno",
            "Eliminar alumno",
            "Volver"
        ])
        
        opcion = input("Opción: ").strip()
        
        if opcion == "1":
            crear_matriz()
            cargar_datos()
        elif opcion == "2":
            mostrar_alumnos()
        elif opcion == "3":
            ordenar_por_apellido()
        elif opcion == "4":
            buscar_alumno_por_legajo()
        elif opcion == "5":
            modificar_alumno()
        elif opcion == "6":
            eliminar_alumno()
        elif opcion == "7":
            return
        else:
            input("Opción inválida. Presione Enter para continuar...")

def gestion_materias(materias):
    while True:
        mostrar_menu("Materias", [
            "Listar materias",
            "Agregar materia",
            "Borrar materia",
            "Volver"
        ])
        
        opcion = input("Opción: ").strip()
        
        if opcion == "1":
            mostrar_materias(materias)
        elif opcion == "2":
            agregar_materia(materias)
        elif opcion == "3":
            borrar_materia(materias)
        elif opcion == "4":
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
