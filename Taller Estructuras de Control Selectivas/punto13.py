print("Punto 13 del taller")
"""

"""
#entrada
import datetime
x=datetime.datetime.now()
fecha_nacimiento = input("digite en este formato 'dd/mm/yy': ")
day, month, year= fecha_nacimiento.split("/")
dia=int(day)
mes=int(month)
año_nacimiento=int(year)
#Caja negra
mes_actual=int(x.strftime("%m"))
año_actual=int(x.strftime("%Y"))
dia_actual=int(x.strftime("%d"))
años=(año_actual-año_nacimiento)
signo=""
if mes==11 and dia>=22 or mes==12 and dia<=21:
    signo=("Sagitario ")
elif mes==12 and dia>=22 or mes==1 and dia<=20:
    signo=("Capricornio ")
elif mes==1 and dia>=21 or mes==2 and dia<=19:
    signo=("Acuario ")
elif mes==2 and dia>=20 or mes==3 and dia<=19:
    signo=("Piscis ") 
elif mes==3 and dia>=21 or mes==4 and dia<=20:
    signo=("Aries ")
elif mes==4 and dia>=21 or mes==5 and dia<=21:
    signo=("Tauro ")
elif mes==5 and dia>=22 or mes==6 and dia<=21:
    signo=("Geminis ")
elif mes==6 and dia>=22 or mes==7 and dia<=22:
    signo=("Cancer ")
elif mes==7 and dia>=23 or mes==8 and dia<=23:
    signo=("Leo ")
elif mes==8 and dia>=24 or mes==9 and dia<=22:
    signo=("Virgo ")

elif mes==9 and dia>=23 or mes==10 and dia<=22:
    signo=(" Libra ")
elif mes==10 and dia>=23 or mes==11 and dia<=21:
    signo=("Escorpion ")
#salida
print(f" Su signo del Zodiaco es {signo} ")
print(" Su edad es de :", años,"años ")


