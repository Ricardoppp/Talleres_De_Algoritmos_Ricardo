print("Punto 8 del taller")
"""
Entradas
P=P
Q=Q
Salidas
Expresion=E
"""
#entrada
P=int(input("Digite el valor de P:"))
Q=int(input("Digite el valor de Q:"))
#caja negra
E=(P**3)+(Q**4)-(2*(P**2))
if(E<=680):
   print(f"{P} y {Q} satisfacen la expresion")
else:
    print(f"{P} y {Q} no satisfacen la expresion")