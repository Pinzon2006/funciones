#Funciones
#Ejemplo Formulario
#Nombre - Apellido - Edad - Ciudad - Correo - Años de Experiencia - Salario
def formulario(nombres, apellidos, edad, ciudad, correo, years, salario):
    print(f"\n\nLos Datos del Formulario enviado son:\nNombres: {nombres}\nApellidos: {apellidos}\nEdad: {edad}\nCiudad: {ciudad}\nCorreo: {correo}\nAños de Experiencia: {years}\nSalario: {salario}")
    
nombres = input("Ingrese sus Nombres: ")
apellidos = input("Ingrese sus Apellidos: ")
edad = int(input("Ingrese su Edad: "))
ciudad = input("Ingrese su Ciudad: ")
correo = input("Ingrese su correo: ")
years = int(input("Ingrese sus Años de Experiencia: "))
salario = float(input("Ingrese su expectativa de Salario a ganar: "))

formulario(nombres, apellidos,edad,ciudad,correo,years,salario)