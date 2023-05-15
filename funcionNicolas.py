#Primero le doy valor a la funcion def
def information(name,lastname,age):
    #Segundo: Se dijita lo que se desea mostrar en la consola
    print(f"Name: {name}\n Lastname: {lastname}\n age: {age}")

#Se le da valor a las variables name,lastname y age
name= input("Name:")
lastname= input("Lastname:")
age = input("Age:")

#Finalmente se codifica lo que se necesita identificar en la funcion
information(name,lastname,age)

