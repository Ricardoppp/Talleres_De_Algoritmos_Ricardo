print("Punto 4 del taller")
"""
##Entrada
Monto Total = int(Monto)
Cantidad a pagar po piezas = float(Cantidad)
##Salidas
Valor 
Inversion = I
Prestamo bancario = Prestamo
Credito bancario = CB
Monto a pagara por intereses= float(Intereses)
"""
#Entrada
Monto=int(input("digite el numero de piezas:"))
Cantidad=float(input("Digite el valor de cada pieza:"))
Valor=(Monto*Cantidad)
#Caja negra
if(Valor<5000000):
    I=(Valor*0.7)
    CB=(Valor*0.3)
    Intereses=(Valor*0.2)  
else:
    I=(Valor*0.55)
    Prestamo=(Valor*0.3)
    Intereses=(Valor*0.2)
    CB=(Valor*0.15)
#Salida
print("el valor que le corresponde pagar a la empresa es:"+str(I))
print("El valor del credito bancario es:"+str(CB))
print("El valor del interes es de:"+str(Intereses))
print("El valor que le corresponde pagar a la empresa es:"+str(I))
print("El valor del credito bancario es:"+str(CB))
print("El valor del interes es de:"+str(Intereses))
print("El valor del prestamo del banco es de:"+str(Prestamo))