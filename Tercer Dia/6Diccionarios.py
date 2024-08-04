diccionario = {'c1':'valor1', 'c2':'valor2'} #SI SE PUEDE REPETIR LOS VALORES PERO LAS CLAVES NO
print(diccionario)

resultado = diccionario['c1'] #HACER UNA BUSQUEDA
print(resultado)

cliente = {'nombre':'Juan', 'apellido':'Fuentes', 'peso':88, 'estatura':1.98}
consulta = (cliente['apellido'])
print(consulta)

diccionario = {'c1':55, 'c2':[10,20,30], 'c3':{'s1':100, 's2':200}}
print(diccionario['c2'][1]) #IMPRIME LA POSICION #1 DE LA CLAVE DOS

diccionario = {'c1':55, 'c2':[10,20,30], 'c3':{'s1':100, 's2':200}}
print(diccionario['c3']['s2']) #BUSCAR EN UN DICCIONARIO LO QUE HAY DENTRO DE UN DICCIONARIO

diccionario = {'c1': ['a', 'b', 'c'], 'c2': ['d', 'e', 'f']}
print(diccionario['c2'][1].upper())

diccionario = {1:'a', 2:'b'}
print(diccionario)
diccionario[3] = 'c' #MODIDICAR DICCIONARIOS
print(diccionario)

diccionario = {1:'a', 2:'b'}
print(diccionario)
diccionario[2] = 'B' #SOBREESCRIBIR DICCIONARIOS
print(diccionario)

print(diccionario.keys()) #IMPRIME LAS CLAVES DE LOS DICCIONARIOS
print(diccionario.values()) #IMPRIME LOS VALORES DE LOS DICCIONARIOS
print(diccionario.items()) #IMPRIME TODOS LOS ELEMENTOS DE LOS DICCIONARIOS