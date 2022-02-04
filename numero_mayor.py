"""
a=int(input("digite numero a: "))
b=int(input("digite numero b: "))
c=int(input("digite numero c: "))


if(a>=b and a>=c):
    print ("a es el mayor ")
elif(b>=c and b>=a):
    print ("b es el mayor ")
else:
    print(c)                
"""
#datos de entrada 
#salario= float
#datos de salida
#aumento= float

Salario=(int(input("ingrese cantidad de dinero ")))

if (Salario<=900_000):
    aumento=Salario*0.15
    print("su aumento sera del: " +str (aumento))
else:
    aumento= Salario*0.12+ Salario
    print ("su valor sera ") 

