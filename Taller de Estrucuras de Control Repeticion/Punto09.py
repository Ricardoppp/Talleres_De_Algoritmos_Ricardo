Alcool = 0
Gasolina = 0
Diesel = 0
while True:
    C = int(input())
    if C == 1:
        Alcool = Alcool + 1
    elif C == 2:
        Gasolina = Gasolina + 1
    elif C == 3:
        Diesel = Diesel + 1
    elif C == 4:
        break
    else:
        C = C
print("MUITO OBRIGADO")
print(f"Alcool: {Alcool}")
print(f"Gasolina: {Gasolina}")
print(f"Diesel: {Diesel}")