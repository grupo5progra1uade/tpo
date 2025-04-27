def mostrar_menu(titulo, opciones):
    print(f"\n{titulo}")
    for i in range(len(opciones)):
        print(f"{i+1}. {opciones[i]}")
    print("")
