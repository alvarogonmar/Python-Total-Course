menor = min(58,39,223,122,12)
mayor = max(58,39,223,122,12)
print(menor)
print(mayor)

lista = [58,39,223,122,12]
print(max(lista))
print(f'El menor es {min(lista)} y el mayor es {max(lista)}')

#STRINGS
nombres = ['Juan', 'Pablo', 'Alicia', 'Carlos']
print(min(nombres)) #IMPRIME EL PRIMERO EN ORDEN ALFABETICO

nombres = ['Carlos']
print(min(nombres)) #IMPRIME LA LETRA PRIMERA EN EL ABECEDARIO, PERO PRIMERO BUSCA EN LAS MAYUSCULAS DESPUES MINUSCULAS, PUEDES AGREGAR .LOWER

dic = {'c1':45, 'c2':11}
print(min(dic)) #SE FIJA EN LA CLAVE INFERIOR

#OBTENER EL VALOR MAS BAJO
dic = {'c1':45, 'c2':11}
print(min(dic.values()))