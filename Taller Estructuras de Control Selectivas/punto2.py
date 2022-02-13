print("Punto 2 del taller")
"""
#Entrada
Nombre
Salario sin ningun aumento ni descuento
#Salida
Valor total a pagar
"""

#Entrada
Nombre=str(input("Nombre del trabajador: "))
Salario=int(input("Escriba el salario bruto del trabajador: "))
#Caja negra
if Salario<900_000:
    p= Salario+(Salario*0.15)
else: 
    Salario>900_000
    p= Salario-(Salario*0.15)
#Salida
print (f"el salario neto a pagar para {str(Nombre)} es de {int(p)}$ pesos.") 