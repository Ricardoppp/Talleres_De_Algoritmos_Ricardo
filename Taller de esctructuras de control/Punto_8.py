import math
print("punto Ocho del Taller")
'''
Datos de entrada
Longitud primer lado triangulo  = a  
Longitud segundo lado triangulo = b
Longitud tercer lado triangulo  = c

'''
#entrada

a=int(input("Ingrese valor a "))
b=int(input("Ingrese valor b "))
c=int(input("Ingrese valor c "))

#caja negra
s=float(input((a+b+c)/2))
d=math.sqrt((s(s-a)*(s-b)*(s-c))**0.5)

#salida
print(d)