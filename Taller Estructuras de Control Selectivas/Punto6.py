print("Punto 6 del taller")
"""
Entrada
A = A = N1
B = B = N2
C = C = N3
D = D = N4
Salidas
valor redondeado
"""
#entrada
A=int(input("Digite el valor A: "))
B=int(input("Digite el valor B: "))
C=int(input("Digite el valor C: "))
D=int(input("Digite el valor D: "))
N1=A
N2=B
N3=C
N4=D
#caja negra
if N3>5:
    N3=0
    N4=0
    N2=N2+1
elif(N3<5):
    N3=0
    N4=0
elif(N3==5):
    N4=0
elif(N2<5):
    N3=0
    N4=0
    N2=0
    N1=N1+1
#salida
print("el valor aproximado es de " +str(N1)+str(N2)+str(N3)+str(N4))
