print("Punto 7 del taller")
"""
Entrada
Kilometros recorridos= distancia
Salida
Cobro al usuario
"""
#entrada
Distancia=float(input("Digite los kilometros recorrida: "))
#caja negra
if(Distancia<300):
    Valor=50000

elif((Distancia>=300) and (Distancia<1000)):
    Valor=70000+(Distancia-300)*30000
    
elif(Distancia>1000):
    Valor=150000+(Distancia-1000)*9000


print(f"El valor a pagar es: ${Valor}")