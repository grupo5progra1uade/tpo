from materias import *
from asistencia import *
from alumnos import * 
from utils import mostrar_menu
from profesores import *

#cargar alumnos desde el JSON y armar matriznx5
with open("alumnos_lista.json", encoding="utf-8") as a:
    alumnos_dict = json.load(a)
matriznx5 = []
for legajo, datos in alumnos_dict.items():
    matriznx5.append([int(legajo), datos["apellido"], datos["nombre"]])

def pre_menu():
    while True:
        print("\n" + "="*60)
        print("      BIENVENIDO AL SISTEMA DE ASISTENCIA DE ALUMNOS")
        print("="*60)
        print("\nMENÚ DE PROFESORES")
        print("-"*60)
        print("En este menú puede gestionar el acceso y los datos de los profesores.\n")
        print("Seleccione una opción para continuar:\n")
        print("1. Ingresar (acceder al sistema principal)")
        print("2. Cargar nuevo profesor (alta)")
        print("3. Modificar profesor (editar datos)")
        print("4. Mostrar listado de profesores")
        print("5. Cambiar contraseña de profesor")
        print("6. Eliminar profesor (baja)")
        print("7. Salir del sistema")
        print("-"*60)
        
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "1":
            if ingreso():
                return True

        elif opcion == "2":
            print("\n--- ALTA DE NUEVO PROFESOR ---")
            agregar_profesor(profesores)
            
        elif opcion == "3":
            print("\n--- MODIFICAR DATOS DE PROFESOR ---")
            id_profesor = input("Ingrese el ID del profesor a modificar: ").strip()
            modificar_profesor(profesores, id_profesor)

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
            registro = cargar_registro_desde_txt()
            registrar_asistencia(matriznx5)
        elif opcion == "3":
            cargar_materias()
            gestion_materias()
        elif opcion == "4":
            cargar_materias()
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
            
def registrar_asistencia_menu(matriznx5, ARCHIVO_MATERIAS):
    while True:
        mostrar_menu("Registro de Asistencia", [
            "Cargar asistencia",
            "Volver"
        ])
    
        opcion = input("Opcion: ").strip()
        
        if opcion == "1":
            cargar_materias()
            registrar_asistencia(matriznx5, ARCHIVO_MATERIAS)
        elif opcion == "2":
            return
        else:
            input("Opción inválida. Presione Enter para continuar...")

def gestion_materias():
    while True:
        mostrar_menu("Materias", [
            "Listar materias",
            "Agregar materia",
            "Borrar materia",
            "Volver"
        ])
        
        opcion = input("Opción: ").strip()
        
        if opcion == "1":
            cargar_materias()
            mostrar_materias()
        elif opcion == "2":
            cargar_materias()
            agregar_materia()
        elif opcion == "3":
            cargar_materias()
            borrar_materia()
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
            mostrar_asistencia_alumno(matriznx5)
        elif opcion == "2":
            mostrar_asistencia_general(registro)
        elif opcion == "3":
            return
        else:
            input("Opción inválida. Presione Enter...")

if __name__ == "__main__":
    if pre_menu() == True:
        main()

