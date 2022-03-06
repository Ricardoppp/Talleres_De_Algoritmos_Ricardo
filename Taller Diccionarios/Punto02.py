'''
Recorre un diccionario y crea una lista solo con los valores que contiene, sin añadir valores
duplicados.
'''
Ejemplo={'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7,'Maite': 5}
#Resultado=[3, 8, 12, 5, 7]
lista=[]
for value in Ejemplo.items():
    valor=((value))
    lista.append(valor)
organizar=(set(lista))
print (list(organizar))