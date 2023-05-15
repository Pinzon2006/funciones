#Funciones y Return
#porcentaje de hombres y mujeres en un trabajo
print("PARAMETRO")
def porcentaje_de_trabajadores(Mujeres,Hombres):
    print(f"El porcentaje total de Mujeres en el trabajo es de: {MujeresPorce:.2f}\nEl porcentaje total de Hombres en el trabajo es de:{HombresPorce:.2f}")

Mujeres=86
Hombres=54

PersonalEnTotal=Mujeres+Hombres 
HombresPorce=(Mujeres/PersonalEnTotal)*100
MujeresPorce=(Hombres/PersonalEnTotal)*100

porcentaje_de_trabajadores( MujeresPorce,HombresPorce)
print("")
#return
print("RETURN")
def introducción(lina,sebastian,marlon,kevin,nicolas):
    return print(f"Hola, nuestros apellidos son: ,\n {lina},\n{sebastian},\n{marlon},\n{kevin},\n{nicolas}")
 
lina = "Barrios Hernández"
sebastian = "Pinzon Soacha"
marlon = "Lopez Bustos"
kevin = "Londoño Gutierrez"
Nicolas = "Paulo Vega"

introducción(lina,sebastian,marlon,kevin,Nicolas)
