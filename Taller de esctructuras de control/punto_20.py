print("punto Veinte del Taller")
'''
Datos de entrada
precio por compra de contado = c
intereses = recargo 

#Datos de salida
porcentaje de intereses = inC

'''
#entradas 
c=int(input("Precio de la compra de contado "))
recargo=float(input("Intereses de de la compra por cada cuota "))

#blackbox
cuotas=(c/12)
reC=(((c/12)*(recargo/100))+cuotas)
inC=(((reC-cuotas)*100)/cuotas)

#salidas
print("intereses del computador por cuota: ", inC, "%")
print(f"cuota total mas intereses: {int(reC)}")





















