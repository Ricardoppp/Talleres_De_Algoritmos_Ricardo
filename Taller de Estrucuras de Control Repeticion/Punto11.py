#
listas=[]
aguardiente=0
ron=0
cerveza=0
tequila=0
whisky=0
otro=0
respuesta=0
listpreferencias=[]
menor_edad_muejer=[]
list_edad=[]
list_hombres=[]
list_cerveza=[]
list_whisky=[]
aguila=[]   

#entradas, caja negra y salidas
respuesta=int(input("Consume usted licor si inserte 1 / no , Inserte 2 "))

while True:
    if(respuesta==1):
        edad=int(input("¿cual es su edad?: "))
        list_edad.append(edad)
        sexo=str(input("¿Cual es su genero? 'M' para masculino y 'F' para femenino: "))
        if(edad<=18)and(sexo=="F"):
            mujeres_menores=edad
            menor_edad_muejer.append(mujeres_menores)   
        preferencia=int(input("¿Licor preferido?: 1 aguardiente, 2 ron, 3 cerveza, 4 tequila, 5 whisky, 6 otro: "))
        listas.append(preferencia)
        print(" Continuar con la encuesta")
        respuesta=int(input("¿desea continuar con la encuesta? '1' para SI, '2' para NO "))        
        if(preferencia==1):
            aguardiente=aguardiente+1
        elif(preferencia==2):
            ron=ron+1
        elif(preferencia==3):
            cerveza=cerveza+1
            list_cerveza.append(cerveza)
            if(preferencia==3 and edad>0):
                pref_cerveza=edad
                aguila.append(pref_cerveza)
                continue
        elif(preferencia==4):
            tequila=tequila+1   
        elif(preferencia==5):
            whisky=whisky+1
            list_whisky.append(whisky)
        elif(preferencia==6):
            otro=otro+1   
        elif(edad>=0):
            list_edad.append(edad)
            continue
        elif(20>=edad<=25)and(sexo=="M") and (preferencia!=1):
            hombres=edad+sexo
            if(preferencia!=1):
                list_hombres.append(hombres)
                continue
    elif((respuesta==2)):
        cerveza_suma=sum(list_cerveza)
        if(cerveza_suma==0):
            list_cerveza=[1]
            print(f" El total de personas que consumen licor: {(aguardiente+ron+cerveza+tequila+whisky+otro) }")
            print(f" Total de mujeres menores de edad : {len(menor_edad_muejer)}")
            print(f" Hombre entre 20 y 25 años que no consumen aguardiente: {len(list_hombres)}")
            print(f" Personas que consumen cerveza es de :{sum(aguila)/sum(list_cerveza)}")
            print(f" Porcentaje de personas que consumen whisky en relación con el total encuestado: {(len(list_whisky)/len(listas))*100} %")
            break
        else:
            print(f" El total de personas que consumen licor: {(aguardiente+ron+cerveza+tequila+whisky+otro) }")
            print(f" Total de mujeres menores de edad : {len(menor_edad_muejer)}")
            print(f" Hombre entre 20 y 25 años que no consumen aguardiente:{len(list_hombres)}")
            print(f" Personas que consumen cerveza es de :{sum(aguila)/sum(list_cerveza)}")
            print(f" Porcentaje de personas que consumen whisky en relación con el total encuestado: {(len(list_whisky)/len(listas))*100} %")
            break