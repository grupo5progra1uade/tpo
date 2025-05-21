from materias import *
from asistencia import *
from alumnos import * 
from utils import mostrar_menu

def main():

    while True:
        mostrar_menu("Sistema de Asistencia", [
            "Gestión de Alumnos",
            "Registrar Asistencia",
            "Gestión de Materias",
            "Consultar Asistencias",
            "Salir"
        ])
        
        opcion = input("Opción: ").strip()
        
        if opcion == "1":
            gestion_alumnos(matriznx5)
        elif opcion == "2":
            registrar_asistencia(matriznx5, asistencias, materias)
        elif opcion == "3":
            gestion_materias(materias)
        elif opcion == "4":
            consultar_asistencias(asistencias, matriznx5)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            input("Opción inválida. Presione Enter...")

def gestion_alumnos(matriznx5):
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
            
def registrar_asistencia_menu(matriznx5, asistencias, materias):
    while True:
        mostrar_menu("Registro de Asistencia", [
            "Cargar asistencia",
            "Volver"
        ])
    
        opcion = input("Opcion: ").strip()
        
        if opcion == "1":
            registrar_asistencia(matriznx5, asistencias, materias)
        elif opcion == "2":
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

def consultar_asistencias(asistencias, matriznx5):
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
            mostrar_asistencia_general(registro)
        elif opcion == "3":
            return
        else:
            input("Opción inválida. Presione Enter...")

if __name__ == "__main__":
    main()
