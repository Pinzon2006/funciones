#Funcion sin parametros
#Primero le doy valor a la funcion
def login(name,age,email):
    print(f"Tu nombre de usuario es {name}, ti enes {age} años y tu correo es {email}")

name = input("Ingrese su nombre de Usuario:")
edad = input("Ingrese su contraseña: ")
email = input("Ingrese su correo:")

login(name,edad,email)
