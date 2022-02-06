print("Punto Nueve del Taller ")
'''
Datos de entrada
nombre para saber a quien se le va a pagar = Nomb
salario= salario por hora
hora_laborada= horas trabajadas 
descuento por conceptos de impuestos= 0.2

'''
#entradas
Nomb=str(input("Ingrese nombre "))
salario=float(input("ingrese salario basico por hora "))
hora_laborada= int(input("ingrese cantidad de horas trabajadas "))

#caja negra
salario_ordinario=(salario*hora_laborada)
retencion= (salario_ordinario*0.2)
Total= (salario_ordinario-retencion)

#salidas
print("valor a pagar para", Nomb, "por la suma de",Total)