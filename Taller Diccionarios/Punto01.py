'''
Crea un programa que recorra una lista y cree un diccionario que contenga el número de veces que aparece cada número en la lista.
'''
lista=[12,23,5,12,92,5,12,5,29,92,64,23]
#Resultado: {12: 3, 23: 2, 5: 3, 92: 2, 29: 1, 64: 1}
a=list(set(lista))
print(a)
diccionario={}
tamaño=len(a)-1
while tamaño>=0:
    c=0
    for i in lista:
        if (a[tamaño]==i):
            c=c+1
        diccionario.update({a[tamaño]:c})
    tamaño=tamaño-1
print(diccionario)

