print("Punto Catorce del Taller")
'''
Datos de entrada
mes 1 con su lectura = m1 
mes 2 con su lectura = m2
costo por kilovatio  = costo_k

resultado a pagar del mes 1 = total1
resultado a pagar del mes 2 = total2 

'''

#entradas
m1=float(input("Ingrese valor de la lectura anterior: "))
m2=float(input("Ingrese valor de la lectura actual: "))
costo_k=float(487.86)
#caja negra
total1= m1*costo_k
total2= m2*costo_k
#salidas
print(f"El costo anterior es de {int(total1)} pesos.")
print(f"El costo actual es de {int(total2)} pesos.")