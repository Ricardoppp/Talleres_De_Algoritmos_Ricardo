print("Punto  del taller")

"""
##Entradas
Cantidad invertida=invertir
Tasa de intereses= tasa
##Salidas
Saldo
"""
invertir=float(input("cantidad de dinero a invertir: "))
tasa=int(input("tasa de interes: "))

x=invertir*tasa

if x>100000:
    print(f"la cantidad generada por concepto de intereses es de  {int(x)} superando los 100.000")
else:
    print(f"la cantidad generada por concepto de intereses es de {int(x)} no superando los 100.000")

print(f"saldo de cuenta es de: {int(invertir+x)}")












