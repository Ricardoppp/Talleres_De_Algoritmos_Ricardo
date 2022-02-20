#Punto 5
#caja negra y salida
x=1
y=0
list = []
while (y<1000):
    y=(x**2+1)/x
    list.append(y)
    x=x+1
    print(len(list))