print("Punto Quince del Taller")
'''
Datos de entrada
precio final del producto = pf
precio de venta al publico= Co

x1 diferencia del la venta al publico y el precio final
x2 el descuento realizado al precio final

'''

#entradas
Pf=int(input("Inserte precio final pagado por el producto: "))
Co=float(input("Precio de venta al publico: "))

#blackbox
x1=(Co-Pf)
x2=(x1/Co)*100

#salidas
print(f"El porcentuaje de descuento es del: {int(x2)}%")
