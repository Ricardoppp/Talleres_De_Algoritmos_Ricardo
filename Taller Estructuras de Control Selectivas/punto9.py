"""
##entradas
nombre 
compra que se realizo      = compra
##salidas
% del descuento            = d
de cuanto es el descuento  = Des
valor a pagar total        = Pagar
"""
#entradas
Nombre = str(input("Digite su nombre: "))
Compra= float(input("Digite el monto de su compra: "))
# Caja Negra
if Compra < 50000:
    Des   = Compra*0
    d     = "0 %"
    Pagar = Compra - Des
elif Compra >= 50000 and Compra < 100000:
    Des   = Compra*0.05
    d     = "5 %"
    Compra = Compra- Des
elif Compra >= 100000 and Compra < 700000:
    Des   = Compra*0.11
    d     = "11 %"
    Pagar = Compra - Des
elif Compra >= 700000 and Compra < 1500000:
    Des   = Compra*0.18
    d     = "18 %"
    Pagar = Compra - Des
else:
    Des   = Compra*0.25
    d     = "18 %"
    Pagar = Compra - Des
# Salidas
print(f"Sr/a: {Nombre}")
print(f"Se realiza una compra por: {float(Compra)}$ COP")
print(f"Se ha aplicado un descuento del {d} equivalente a: {int(Des)}$ COP")
print(f"EL total a pagar es de: {int(Pagar)}$ COP")