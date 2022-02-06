print("punto Siete del Taller")

'''
Datos de entrada
#1 metro = 39.27 
#1 pie = 12 

'''

#entradas
M=int(input("Cantidad de metros a convertir "))
C=float(M*100)

#blackbox
PU= 39.27
FT=(PU/0.12)
X1=(C*PU)
X2=(C*FT)

#salidas
print(M, f"metros en Pulgada {int(X1)}")
print(M, f"metoros en pies {int(X2)}")