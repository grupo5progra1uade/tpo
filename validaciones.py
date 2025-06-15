import re

#Validaciones de texto

def letras_validas(texto):
        patron_nombre = r"^[A-Za-zÁÉÍÓÚáéíóúÑñ]+(?: [A-Za-zÁÉÍÓÚáéíóúÑñ]+)*$" #permite espacios entre nombre y apellido
        return bool(re.match(patron_nombre, texto))

def capitalizar(texto):
        return " ".join([palabra.capitalize() for palabra in texto.split(" ")]).strip() #el strip es para evitar aalgun espacio accidental

def validar_psw(nueva_contra): #crud profes
        patron = r'^(?=.*[0-9])(?=.*[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-=|]).{8,}$'
        if re.match(patron, nueva_contra):
                print("Contraseña válidada correctamente")
                return True
        else:
                print("Contraseña inválida. (Debe tener al menos 8 caracteres, un numero y un caracter especial)")
                return False
        
def validar_mail(correo):
        patron = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
        return re.match(patron, correo) is not None

def pedir_entero(mensaje):
        while True:
                entrada = input(mensaje)
                try:
                        return int(entrada)
                except ValueError:
                        print("Debe ingresar un número entero")