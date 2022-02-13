print("Punto 12 del taller")
"""
Entradas
Dinero
Salidas
Cantidad de billetes 
Cantidad de monedas
"""
#Entradas
Dinero = int(input("Ingrese cantidad de dinero: "))
#Caja Negra 
#Billetes#
Billete1 = (Dinero-Dinero % 100_000)/100_000
Dinero = Dinero % 100_000
if Billete1 > 0:
    print(f"La Cantidad de billetes de 100000 es de: {int(Billete1)}")
Billete2 = (Dinero-Dinero % 50_000)/50_000
Dinero = Dinero % 50_000
if Billete2 > 0:
    print(f"La Cantidad de billetes de 50000 es de: {int(Billete2)}")
Billete3 = (Dinero-Dinero % 20_000)/20_000
Dinero = Dinero % 20_000
if Billete3 > 0:
    print(f"La Cantidad de billetes de 20000 es de: {int(Billete3)}")
Billete4 = (Dinero-Dinero % 10_000)/10_000
Dinero = Dinero % 10_000
if Billete4 > 0:
    print(f"La Cantidad de billetes de 10000 es de: {int(Billete4)}")
Billete5 = (Dinero-Dinero % 5_000)/5_000
Dinero = Dinero % 5_000
if Billete5 > 0:
    print(f"La Cantidad de billetes de 5000 es de: {int(Billete5)}")
Billete6 = (Dinero-Dinero % 2_000)/2_000
Dinero = Dinero % 2_000
if Billete6 > 0:
    print(f"La Cantidad de billetes de 2000 es de: {int(Billete6)}")
Billete7 = (Dinero-Dinero % 1_000)/1_000
Dinero = Dinero % 1_000
if Billete7 > 0:
    print(f"La Cantidad de billetes de 1000 es de: {int(Billete7)}")
#Monedas#
Moneda1 = (Dinero-Dinero % 500)/500
Dinero = Dinero % 500
if Moneda1 > 0:
    print(f"La Cantidad de monedas de 500 es de: {int(Moneda1)}")
Moneda2 = (Dinero-Dinero % 200)/200
Dinero = Dinero % 200
if Moneda2 > 0:
    print(f"La Cantidad de monedas de 200 es de: {int(Moneda2)}")
Moneda3 = (Dinero-Dinero % 100)/100
Dinero = Dinero % 100
if Moneda3 > 0:
    print(f"La Cantidad de monedas de 100 es de: {int(Moneda3)}")
Moneda4 = (Dinero-Dinero % 50)/50
Dinero = Dinero % 50
if Moneda4 > 0:
    print(f"La Cantidad de monedas de 50 es de: {int(Moneda4)}")