print("Punto Once del Taller ")
'''
Datos de entrada
nombre del tranbajador = nomb
horas trabajadas = horas_trabajadas
pago horas extras = Pagos_extras
numero de hijos = hijos

las deducciones son int
su saldo neto es int

'''
### Entradas 

nomb=str(input("Inserte nombre del trabajador: "))
Horas_trabajadas=int(input("Numero de horas trabajadas: "))
Pago_horas=float(input("pago por horas trabajadas: "))
Horas_extras=int(input("cantidad de horas extras trabajadas: "))
hijos=int(input("cuantos hijos tiene: "))

### Blackbox 
saladio_base=Pago_horas*(Horas_trabajadas)
asignaciones=(250000+173000*(Horas_extras)+180000)
descuento=saladio_base*(0.14)
des=(saladio_base+Pago_horas)
pago_extras=(Pago_horas+Horas_extras)
pago_h_extras=(pago_extras+0.25)+pago_extras 
salario_neto=(asignaciones+des+ pago_h_extras)

#salidas
print("Las asignacionesde ", asignaciones)
print(f"Las deducciones son de {int(descuento)}")
print(f"Sueldo neto que recibira {nomb} en el mes de diciembre es de {int(salario_neto)}")





















