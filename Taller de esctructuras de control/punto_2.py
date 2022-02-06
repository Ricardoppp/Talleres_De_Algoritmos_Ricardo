print("Punto Dos del Taller ")
'''
Datos de entrada
cap= capital que se va invertir
meses transcurridos = m
razon del pago = 0,02
tpo= total de ganancias 

'''
#entradas 
cap=int(input("capital para invertir es de: "))
m=int("cantidad de meses para su inversion ")

#caja negra 
ganancia=cap*(0.02*m)
tpo=(cap+ganancia)

#salidas
print("la ganancia por el capital invertido es de: ", ganancia)
print("la ganancia total con el capital invertido es de: ", tpo )
