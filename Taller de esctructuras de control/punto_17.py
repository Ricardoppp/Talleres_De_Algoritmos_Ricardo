print("punto diecisiete del Taller")
'''
Datos de entrada

presupuesto anual= p1
ginecología      = gin - 30%
traumatología    = tra - 30%
pediatría        = pe  - 30%
   area     //     presupuesto
   
'''
#entradas
p1=(int(input("Ingrese presupuesto anual del Hospital: ")))

#caja negra
gin=(p1*0.40)
tra=(p1*0.30)
pe=(p1*0.30)

#salidas
print(f"El valor para Ginecologiía es un total de: {int(gin)}")
print(f"El valor total para Traumatología es de: {int(tra)}")
print(f"y el valor destinado a pediatría es de: {int(pe)}")