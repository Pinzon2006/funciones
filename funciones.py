#Funciones
#Ejemplo Formulario
#Nombre - Apellido - Edad - Ciudad - Correo - Años de Experiencia - Salario
#Definir la funcion
def formulario(nombres, apellidos, edad, ciudad, correo, years, salario): 
    #Se muestra los datos requeridos
    print(f"\n\nLos Datos del Formulario enviado son:\nNombres: {nombres}\nApellidos: {apellidos}\nEdad: {edad}\nCiudad: {ciudad}\nCorreo: {correo}\nAños de Experiencia: {years}\nSalario: {salario}") 

#difine el nombre del usuario
nombres = input("Ingrese sus Nombres: ")
#defines los apellidos
apellidos = input("Ingrese sus Apellidos: ")
#define la edad
edad = int(input("Ingrese su Edad: "))
#define la cuidadn de donde es
ciudad = input("Ingrese su Ciudad: ")
#ingresar el correo electronico
correo = input("Ingrese su correo: ")
#definir los años de experiencia
years = int(input("Ingrese sus Años de Experiencia: "))
#define su salario 
salario = float(input("Ingrese su expectativa de Salario a ganar: "))

#funcion y sus variables
formulario(nombres,apellidos,edad,ciudad,correo,years,salario)
