from materias import *
from asistencia import *
from alumnos import * 
from utils import mostrar_menu
from profesores import *


def pre_menu():
    
    while True:
        print("\nMenú de Profesores")
        print("1. Ingresar")
        print("2. Cargar nuevo profesor")
        print("3. Modificar profesor")
        print("4. Mostrar listado de profesores")
        print("5. Cambiar contraseña")
        print("6. Eliminar profesor")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            if ingreso():
                return True

        elif opcion == "2":
            if agregar_profesor(profesores):
                return True
            
        elif opcion == "3":
                palabra_clave = input("Ingrese la palabra clave para modificar: ").strip()
                if modificar_profesor(profesores, palabra_clave):  
                    return True

        elif opcion == "4":
            if mostrar_profesores():  
                return True  

        elif opcion == "5":
            cambiar_contraseña()

        elif opcion == "6":
            eliminar_profesor(profesores)

        elif opcion == "7":
            print("Saliendo...")
            return False  
        else:
            print("Opción inválida. Intente nuevamente.")


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
            mostrar_alumnos()
            input("Presione Enter para continuar...")
        elif opcion == "2":
            cargar_datos()
        elif opcion == "3":
            modificar_alumno()
        elif opcion == "4":
            eliminar_alumno()
            exportar_alumnos_a_json()
        elif opcion == "5":
            buscar_alumno_por_legajo()
            input("Presione Enter para continuar...")
        elif opcion == "6":
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
        exportar_alumnos_a_json()
        main()

