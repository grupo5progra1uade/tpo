from materias import *
from asistencia import *
from alumnos import * 
from utils import mostrar_menu
from profesores import *


def pre_menu():
    while True:
        print("\n" + "="*60)
        print("      BIENVENIDO AL SISTEMA DE ASISTENCIA DE ALUMNOS")
        print("="*60)
        print("\nMENÚ DE PROFESORES")
        print("-"*60)
        print("En este menú puede gestionar el acceso y los datos de los profesores.")
        print("Seleccione una opción para continuar:")
        print("1. Ingresar (acceder al sistema principal)")
        print("2. Cargar nuevo profesor (alta)")
        print("3. Modificar profesor (editar datos)")
        print("4. Mostrar listado de profesores")
        print("5. Cambiar contraseña de profesor")
        print("6. Eliminar profesor (baja)")
        print("7. Salir del sistema")
        print("-"*60)
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            if ingreso():
                return True

        elif opcion == "2":
            print("\n--- ALTA DE NUEVO PROFESOR ---")
            agregar_profesor(profesores)
            
        elif opcion == "3":
            print("\n--- MODIFICAR DATOS DE PROFESOR ---")
            palabra_clave = input("Ingrese la palabra clave para modificar: ").strip()
            modificar_profesor(profesores, palabra_clave)

        elif opcion == "4":
            print("\n--- LISTADO DE PROFESORES ---")
            mostrar_profesores()

        elif opcion == "5":
            print("\n--- CAMBIAR CONTRASEÑA DE PROFESOR ---")
            cambiar_contraseña()

        elif opcion == "6":
            print("\n--- ELIMINAR PROFESOR ---")
            eliminar_profesor(profesores)

        elif opcion == "7":
            print("Saliendo... ¡Hasta luego!")
            return False  
        else:
            print("Opción inválida. Intente nuevamente.")


def main():
    while True:
        print("\n" + "="*60)
        print("         SISTEMA DE ASISTENCIA - MENÚ PRINCIPAL")
        print("="*60)
        print("En este menú puede gestionar alumnos, registrar asistencias, materias y consultar información.")
        print("Seleccione una opción para continuar:")
        mostrar_menu("Sistema de Asistencia", [
            "Gestión de Alumnos",
            "Registrar Asistencia",
            "Gestión de Materias",
            "Consultar Asistencias",
            "Salir"
        ])
        
        opcion = input("Opción: ").strip()
        
        if opcion == "1":
            gestion_alumnos()
        elif opcion == "2":
            registrar_asistencia(matriznx5, registro, materias)
        elif opcion == "3":
            gestion_materias(materias)
        elif opcion == "4":
            consultar_asistencias(registro, matriznx5)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            input("Opción inválida. Presione Enter...")

def gestion_alumnos():
    while True:
        print("\n" + "-"*60)
        print("           GESTIÓN DE ALUMNOS - ADMINISTRACIÓN")
        print("-"*60)
        print("En este menú puede listar, agregar, modificar, eliminar y buscar alumnos.")
        print("Seleccione una opción para continuar:")
        mostrar_menu("Gestión de Alumnos", [
            "Listar alumnos",
            "Agregar alumno",
            "Modificar alumno",
            "Eliminar alumno",
            "Buscar alumno por legajo",
            "Ordenar alumnos por apellido",
            "Volver"
        ])
        
        opcion = input("Opción: ").strip()
        
        if opcion == "1":
            print("\n--- LISTADO DE ALUMNOS ---")
            mostrar_alumnos()
            input("Presione Enter para continuar...")
        elif opcion == "2":
            print("\n--- ALTA DE NUEVO ALUMNO ---")
            cargar_datos()
        elif opcion == "3":
            print("\n--- MODIFICAR DATOS DE ALUMNO ---")
            modificar_alumno()
        elif opcion == "4":
            print("\n--- ELIMINAR ALUMNO ---")
            eliminar_alumno()
        elif opcion == "5":
            print("\n--- BUSCAR ALUMNO POR LEGAJO ---")
            buscar_alumno_por_legajo()
            input("Presione Enter para continuar...")
        elif opcion == "6":
            print("\n--- ORDENAR ALUMNOS POR APELLIDO ---")
            ordenar_por_apellido()
            input("Presione Enter para continuar...")
        elif opcion == "7":
            return
        else:
            input("Opción inválida. Presione Enter para continuar...")
            
def registrar_asistencia_menu(matriznx5, registro, materias):
    while True:
        mostrar_menu("Registro de Asistencia", [
            "Cargar asistencia",
            "Volver"
        ])
    
        opcion = input("Opcion: ").strip()
        
        if opcion == "1":
            registrar_asistencia(matriznx5, registro, materias)
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

def consultar_asistencias(registro, matriznx5):
    while True:
        mostrar_menu("Asistencias", [
            "Por alumno",
            "Listado general",
            "Volver"
        ])
        
        opcion = input("Opción: ").strip()
        
        if opcion == "1":
            mostrar_asistencia_alumno(registro, matriznx5)
        elif opcion == "2":
            mostrar_asistencia_general(registro)
        elif opcion == "3":
            return
        else:
            input("Opción inválida. Presione Enter...")

if __name__ == "__main__":
    if pre_menu() == True:
        main()

