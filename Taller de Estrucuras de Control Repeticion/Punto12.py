#listas
list_final=[]
list_nombres=[]
list_nombreypuntaje=[]
#entrada y caja negra
estudiantes=int(input(" Inserte la cantidad de estudiantes que presentaron la prueba : "))
for i in range(0, estudiantes):
    datos=input("Inserte su nombre y separado por una coma su puntaje en el examen final")
    nombre_puntajefinal=(nombre,puntaje_final)=datos.split(" ")
    puntaje_final=int(puntaje_final)
    nombre=str(nombre)
    list_final.append(puntaje_final)
    list_nombres.append(nombre)
    list_nombreypuntaje.append(nombre_puntajefinal)

    promedio_total=sum(list_final)/len(list_final)
    Promedio_abajo = [i for i in list_final if i<promedio_total]
    promedio_inferior=((sum(Promedio_abajo)/len(list_final))*100)
    promedio_encima = [i for i in list_final if i>promedio_total]
    promedio_superior=((sum(promedio_encima)/len(list_final))*100)
#salidas 
print(f"Nombre del estudiante con el puntaje más alto: ", (list_nombreypuntaje[list_final.index(max(list_final))]))
print(f"Nombre del estudiante con el puntaje más bajo: ", (list_nombreypuntaje[list_final.index(min(list_final))]))
print(f"Puntaje máximo obtenido: ", max(list_final))
print(f"Puntaje mínimo obtenido: ", min(list_final))
print("Promedio de todos los puntajes obtenidos: ", promedio_total)
print(f"Porcentaje de estudiantes con puntajes inferiores al promedio: {promedio_inferior}%")
print(f"Porcentaje de estudiantes con puntajes superiores al promedio: {promedio_superior}%") 
























