print("Punto Cuatro del taller")
'''
Datos de entrada
Compra total = Co
Descuento = De (en este caso como es del 15% se pone solo 15)
se hace 3 salidas ya que se necesita los valores sin descuento, 
cuanto es el descuento y el valor total a pagar con el descuento incluido

'''

#entradas
Co=float(input("Valor total de la compra es de "))
De=float(input("Con un descuento del "))
 
#Blackbox
Descuento=(Co*De)/100
cantminus=(Co-Descuento)

#Salidas
print(f"El valor sin descuento es de {int(Co)} pesos")
print(f"El descuento del 15% es de  {int(Descuento)} pesos")
print(f"valor total a pagar es de  {int(cantminus)} pesos")