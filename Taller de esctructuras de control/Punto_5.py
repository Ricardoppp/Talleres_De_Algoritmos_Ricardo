print("punto Cinco del Taller")
'''
Datos de entrada
P1= parcial 1 
P2= parcial 2
P3= parcial 3

P4= calificacion del examen final
P5= calificacion del trabajo final

55% del promedio de sus tres calificaciones parciales
30% de la calificación del examen final 
15% de la calificación de un trabajo final.

'''
#entrada
P1=int(input("parcial N.1 "))
P2=int(input("parcial N.2 "))
P3=int(input("parcial N.3 "))
P4=int(input("Calificacion su examen final "))
P5=int(input("Calificacion de su trabajo final "))
#blackbox
a=((P1+P2+P3)/3)*0.55
b=(P4*0.3)
c=(P5*0.15)
d=(c+b+a)
#salidas 
print(F"Su calificacion total es de {int(d)}")