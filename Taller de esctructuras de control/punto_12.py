print("Punto Doce del Taller ")
'''
Datos de entrada

notas de matematicas= mate1, mate2, mate3, examate

notas de fisica= fis1, fis2, examfisica

notas quimica= qui1, qui2, qui3, examquimica

notaM= promedio de matematicas
notaF= promedio de fisica
notaQ= Promedio de quimica
PromedioG= promedio de las 3 asignaturas 

todos los resultados en las notas son int

'''

#entrada
mate1=float(input("Inserte su primera nota tarea de matematicas: "))
mate2=float(input("Inserte su segunda nota tarea de matematicas: "))
mate3=float(input("Inserte su tercera nota tarea de matematicas: "))
examate=float(input("Nota examen de matematicas: "))
''
fis1=float(input("Inserte su primera nota tarea de fisica: "))
fis2=float(input("Inserte su segunda nota tarea de fisica: "))
examfisica=float(input("Nota examen de fisica: "))
''
qui1=float(input("Inserte su primera nota tarea de quimica: "))
qui2=float(input("Inserte su segunda nota tarea de quimica: "))
qui3=float(input("Inserte su tercera nota tarea de quimica: "))
examquimica=float(input("Nota examen de quimica: "))
''

# Caja Negra
NotaM=(((mate1+mate2+mate3)/3)*0.1)+examate*(0.9)
NotaF=(((fis1+fis2)/2)*0.2)+examfisica*(0.8) 
NotaQ=(((qui1+qui2+qui3)/3)*0.15)+examquimica*(0.85) 
ProgemidoG=((NotaM+NotaQ+NotaF)/3)

# Salidas
print(f"El promedio general de las tres materias: {int(ProgemidoG)}")
print(f"El Promedio de matematicas es de: {int(NotaM)}")
print(f"El Promedio de fisica es de: {int(NotaF)}")
print(f"El Promedio de quimica es de: {int(NotaQ)}")



























