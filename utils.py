
def mostrar_menu(titulo, opciones):
    print(f"\n{titulo}")
    for idx, opcion in enumerate(opciones, 1):
        print(f"{idx}. {opcion}")
    print("")