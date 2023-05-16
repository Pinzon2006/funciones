
#Primero le doy valor a la funcion 
def information(name,lastname,age):
    #Segundo: Se dijita lo que se desea mostrar en la consola
    print(f"Name: {name}\n Lastname: {lastname}\n age: {age}")

#Se le da valor a las variables name,lastname y age
name= input("Name:")
lastname= input("Lastname:")
age = input("Age:")
#Finalmente llamamos a la funcion information
information(name,lastname,age)
print("\n")
