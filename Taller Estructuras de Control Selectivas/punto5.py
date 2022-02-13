print("Punto 5 del taller")
"""
Entrada
Salario base=SB
Ventas departamento 1 = depto1
Ventas departamento 2 = depto2
Ventas departamento 3 = depto3
Salidas
Venta totales de los departamentos si exeden el 33%
"""
#entrada
SalarioBase=float(input("Digite el sueldo base: "))
depto1=float(input("Digite el valor de ventas departamento 1: "))
depto2=float(input("Digite el valor de ventas departamento 2: "))
depto3=float(input("Digite el valor de ventas departamaneto 3: "))
#caja negra
x1=depto1+depto2+depto3
x2=(33*x1)/100
#salida
if(depto1>x2):
    print("El salario del departamento 1 es de:"+str(SalarioBase+(SalarioBase*0.20)))
else:
    print("El salario del departamento 1 es de:"+str(SalarioBase))
if(depto2>x2):
    print("El salario del departamento 2 es de:"+str(SalarioBase+(SalarioBase*0.20)))
else:
    print("El salario del departamento 2 es de:"+str(SalarioBase))
if(depto3>x2):
    print("El salario del departamento 3 es de:"+str(SalarioBase+(SalarioBase*0.20)))
else:
    print("El salario del departamento 3 es de:"+str(SalarioBase+(SalarioBase*0.20)))