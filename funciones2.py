#Funciones y Return
#Despedir a un Usuario
def despedida(nombres, tiempo):
    print(f"Adios {nombres} por trabajar estos {tiempo} años")

nombres = input("Ingrese sus nombres: ")
tiempo = input("Ingrese numero de años trabajados: ")
    
despedida(nombres,tiempo)
