print("Punto diez del Taller ")
'''
Datos de entrada
El cambio de divisas en la bolsa de Madrid el 25/08/1987 fue el siguiente:
    100 chelines austríacos	=	956.871 pesetas
    1 dólar EEUU	        =	122.499 pesetas
    100 dracmas griegos     =	88.607 pesetas
    100 francos belgas	    =	323.728 pesetas
    1 franco francés	    =	20.110 pesetas
    1 libra esterlina	    =	178.938 pesetas
    100 liras italianas	    =	9.289 pesetas

# Lea una cantidad en chelines austriacos e imprima el equivalente en pesetas.
# Lea una cantidad en dracmas griegos e imprima su equivalente en francos franceses
# Lea una cantidad en pesetas e imprima su equivalente en dólares y liras italianas

'''

#entradas
v1=float(input("Cantidad chelines para convertir en pesetas "))
v2=float(input("Cantidad dracmas griegas para convertir francos: "))
v3=float(input("Cantidad pesetas para convertirlas en dolares y liras "))

#Blackbox 
x1=(v1*9568.71)
x2=((v2*8860.7)/20110)
x3=(v3*0.00000816)
x4=(v3/92.89)

#salidas
print("El equivalente de chelines a pesetas es de: ", x1) 
print("El equivalente de dragmas griegos a francos es de ", x2) 
print("El equivalente de pesetas a dolares ", x3, "y el equivalente a liras es de: ", x4) 

