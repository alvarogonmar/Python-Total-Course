import datetime

mi_hora = datetime.time(17, 35)

#Imprimir hora
print(mi_hora)

#Imprimir minutos
print(mi_hora.minute)

#Imprimir hora
print(mi_hora.hour)

mi_dia = datetime.date(2025, 10, 17)
print(mi_dia)

#Imprimir anio
print(mi_dia.year)

#Otro formato
print(mi_dia.ctime())

#Fecha Hoy
print(mi_dia.today())


from datetime import datetime

mi_fecha = datetime(2025, 5, 15, 22, 10, 15, 2500)
#Modificar un dato
mi_fecha = mi_fecha.replace(month = 11)
print(mi_fecha)


from datetime import date

nacimiento = date(1995, 3, 5)
defuncion = date(2095, 6, 19)

vida = defuncion - nacimiento
print(vida)


from datetime import datetime

despierta = datetime(2022, 10, 5, 7, 30)
duerme = datetime (2022, 10, 5, 23, 45)

vigilia = duerme - despierta

print(vigilia)