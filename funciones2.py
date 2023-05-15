#Funciones y Return
#Despedir a un Usuario
#Primero colocamos lo que queramos que haga la funcion con la cantidad de parametros que se implementen
def despedida(nombres, tiempo):
    #dijitamos lo que queremo que se muestre en la consola
    print(f"Adios {nombres} por trabajar estos {tiempo} años")

#escribimos las variables las cuales pueden ser identificadas en este caso se usan las variables de nombres y tiempo
nombres = input("Ingrese sus nombres: ")
tiempo = input("Ingrese numero de años trabajados: ")

#Finalmente llamamos a la funcion despedida
despedida(nombres,tiempo)
