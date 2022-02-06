print("punto Diecinueve del Taller")
'''
Datos de entradas 
cantidad de naranjas = N1
precio 12na naranjas = N2
precio que se vendio = P

Datos de salida
inv = precio al que el mayorista compro las naranjas al agricultor
g= ganancia obtenida

'''
#entradas 
N1=int(input("Cantidad de naranjas compradas "))
N2=int(input("Precio por la docena de naranjas "))
P=int(input("Precio en el que vendio las naranjas a los detallistas "))


#blackbox
inv=((N1*N2)/12) # Precio en el que el mayorista compro las naranjas al agricultor
g=(((P-inv)*100)/inv) # Porcentaje de ganancia obtenido en la inversion 



# Salidas
print(f"El Porcentaje de ganancia obtenido en la inversion es del {int(g)}%")






















