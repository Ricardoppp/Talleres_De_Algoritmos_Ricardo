print("Punto 14 del taller")
"""
Entradas
Lectura Anterior = LaN
Lectura Actua    = LaC
Salidas
Total = T
"""
#entrada
LaN=int(input("Ingrese la lectura anterior: "))
LaC=int(input("Ingrese la lectura actual: "))
#caja negra
x1=abs(LaC-LaN)
if(LaN>=0 and LaC<=100):
  T=x1*4600
elif(LaN>=101 and LaC<=300):
  T=x1*80000
elif(LaN>=301 and LaC<=500):
  T=x1*100000
elif(LaN>=501 and LaC>501):
  T=x1*120000
#salida
print(f"El monto a pagar es:{(T)}")