print("Punto 16 del taller")
"""
Entradas
A = A
B = B
C = C 
Discriminate = D
Salidas
X1
X2
"""
import math
#entrada
A=int(input("valor de A: "))
B=int(input("valor de B: "))
C=int(input("valor de C: "))
#caja negra
D=(B**2)-4*A*C
S=""
if(D==0):
  S=-B/(2*A)
  X1=S
  X2=S
elif(D>0):
  X1=(-B+math.sqrt(B**2-4*A*C))/(2*A)
  X2=(-B+math.sqrt(B**2-4*A*C))/(2*A)
elif(D<0):
  X1="No tiene solucion"
  X2="No tiene solucion"
#salida
print("solucion de segundo grado: "+str(X1))
print("solucion de segundo grado: "+str(X2))