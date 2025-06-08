import re

#Validaciones de texto

def letras_validas(texto):
        patron_nombre = r"^[A-Za-zÁÉÍÓÚáéíóúÑñ]+(?: [A-Za-zÁÉÍÓÚáéíóúÑñ]+)*$" #permite espacios entre nombre y apellido
        return bool(re.match(patron_nombre, texto))

def capitalizar(texto):
        return " ".join([palabra.capitalize() for palabra in texto.split(" ")]).strip() #el strip es para evitar aalgun espacio accidental
    
def validar_psw(nueva_psw): #crud profes
                patron = r'^(?=.*[0-9])(?=.*[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-=|]).{8,}$'
                if re.match(patron, nueva_psw):
                    print("Contraseña válidada correctamente")
                    return True
                else:
                    print("Contraseña inválida. (Debe tener al menos 8 caracteres, un nuemro y un caracter especial)")
                    return False