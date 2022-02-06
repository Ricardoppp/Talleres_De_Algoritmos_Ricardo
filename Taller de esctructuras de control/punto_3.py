print("Punto Tres del taller")
'''
Datos de entrada
Salario base = Sa
Descuento = De
valor venta 1 = v1
valor venta 2 = v2
valor venta 3 = v3

'''
#entradas
Sa=float(input("valor salarial es de "))
De=float(input("cuanto equivale la comisión por venta "))
v1=float(input("comision por venta N.1 "))
v2=float(input("comision por venta N.2 "))
v3=float(input("comision por venta N.3 "))

#caja negra 
total=(v1+v2+v3)

total_2=(total*De)/100

total_3=(total_2*0.1)

total_4=int(Sa+total_3)

#salida
print(f"la comision extra tiene un valor de {int(total_2)}")
print(f"El total ganado generado en el mes es de {int(total_4)}")