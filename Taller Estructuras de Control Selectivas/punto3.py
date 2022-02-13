print("Punto 3 del taller")
"""
#Entradas#
A-D numeros enteros
#Saldias#
si d==0 o d>0
"""
a=int(input("Escriba dato a: "))
b=int(input("Escriba dato d: "))
c=int(input("Escriba dato c: "))
d=int(input("Escriba dato d: "))

if d==0:
    r= (a-c)**2
elif d>0:
    r=((a-b)**3)/d

print("el resultado es: ", r)
