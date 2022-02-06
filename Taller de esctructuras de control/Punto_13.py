print("Punto Trece del Taller ")
'''

Datos de entrada
los valores v1 al v8 son los billetes que toca sumar
estos valores son int

los valores x1 al x8 es la sumatoria de todos lo billetes
que tiene en el banco para que el resultado sea 
un monto de billetes, su resultado es #suma=float#

'''
#entradas
v1=(int(input("Cuandos billetes de 50.000 ")))
v2=(int(input("Cuandos billetes de 20.000 ")))
v3=(int(input("Cuandos billetes de 10.000 ")))
v4=(int(input("Cuandos billetes de 5.000 ")))
v5=(int(input("Cuandos billetes de 2.000 ")))
v6=(int(input("Cuandos billetes de 1.000 ")))
v7=(int(input("Cuandos billetes de 500 ")))
v8=(int(input("Cuandos billetes de 100 ")))

#caja negra
x1=float(v1*50000)
x2=float(v2*20000)
x3=float(v3*10000)
x4=float(v4*5000)
x5=float(v5*2000)
x6=float(v6*1000)
x7=float(v7*500)
x8=float(v8*100)

suma=float(x1+x2+x3+x4+x5+x6+x7+x8)

#salidas
print(f"La cantidad total es de {float(suma)}")