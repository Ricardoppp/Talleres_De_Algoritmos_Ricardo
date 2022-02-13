print("Punto 10 del taller")
# Entradas
S_B = int(input("Digite su salario bruto: "))
# Caja Negra
if S_B > 5000000:
    S_N = S_B+S_B*0.10
    C = 1
elif S_B > 4300000 and S_B <= 5000000:
    S_N = S_B+S_B*0.15
    C = 2
elif S_B > 3600000 and S_B <= 4300000:
    S_N = S_B+S_B*0.20
    C = 3
elif S_B > 2000000 and S_B <= 3600000:
    S_N = S_B+S_B*0.40
    C = 4
elif S_B > 900000 and S_B <= 2000000:
    S_N = S_B+S_B*0.60
    C = 5
else:
    S_N = "No existe ese sueldo"
    C = "No existe una categoria con ese sueldo"
# Salidas
print(f"Su salario neto corresponde a la categoría {C}, y es de: ${S_N} COP")