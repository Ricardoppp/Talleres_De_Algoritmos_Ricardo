print("punto dieciocho del Taller")
'''
Datos de entrada
bolivares prestados = Bo1
intereses pagados   = Bo2

Datos de salida
Con la formula de los intereses, se divide en los 4 años

'''
#entradas
Bo1=int(input("Cantidad de bolivares prestados: "))
Bo2=float(input("Cantidad de intereses pagados en 4 años: "))

#caja negra
R=((Bo2*100)/(Bo1*4))
p=(R/4)

#salidas
print(f"el porcentuaje anual de interese que paga en 4 años es de {float(p)}%")














