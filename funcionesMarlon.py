# #return es para llamr la funcion
# def sumar(a, b):
#     return a+b
# #llamamos la funcion y la pasamos los argumentos
# resultado= sumar(18, 28)
# #imprimimos el resultado con la funcion f
# print(f"resultado de la suma es: {resultado}")

#funcion de parametros
def presentacion(nombre, edad, ciudad):
    return f"Hola, mi nombre es {nombre}, tengo {edad} años y soy de {ciudad}."

# Llamamos a la función y le pasamos los argumentos
mensaje = presentacion("Mrlon", 19, "de Ibague")

# Imprimimos el mensaje resultante
print(mensaje)