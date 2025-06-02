profesores = {
    1: {"nombre": "Maria", "apellido": "Gonzalez", "email": "Maria@gmail.com", "contraseña": "Contra123", "materia": "Matematica"},
    2: {"nombre": "Juan",  "apellido": "Perez", "email": "Juan@gmail.com", "contraseña": "Contra123", "materia": "Historia"},
    3: {"nombre": "Luis", "apellido": "Ramirez", "email": "Luis@gmail.com", "contraseña": "Contra123", "materia": "Literatura"}
}

def mostrar_profesores():
    print("\nProfesores del curso:")
    print("Nombre             | Apellido                | Email                   | Materia")
    print("-" * 80)
    for id, prof in profesores.items():
        print(f"{prof['nombre']:<20} | {prof['apellido']:<20} | {prof['email']:<25} | {prof['materia']}")
    print("-" * 80)


def ingreso(email, contraseña):
    try:
        for prof in profesores.values():
            if prof["email"] == email and prof["contraseña"] == contraseña:
                print(" ------------------------------")
                return "Bienvenido " + prof["nombre"] + " " + prof["apellido"]
        
        # Si no encontró coincidencia, lanza un error manual
        raise ValueError("Email o contraseña incorrectos. Vuelva a intentarlo.")
    
    except ValueError as e:
        print(e)
        return None  # Devuelve None si hubo error


