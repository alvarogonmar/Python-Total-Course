#PRIMERA FORMA SIN ENUMERATE
lista = ['a', 'b', 'c']
indice = 0

for item in lista:
    print(indice,item)
    indice += 1

#FORMA MAS ELEGANTE CON ENUMERATE
lista = ['a', 'b', 'c']

for item in enumerate(lista):
    print(item)

#CON RANGE
for indice,item in enumerate(range(50,55)):
    print(indice,item)

#TUPLE
lista = ['a', 'b', 'c']
mi_tuple = list(enumerate(lista))
print(mi_tuple)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for nombre in (lista_nombres):
    if nombre.startswith('M'):
        print(nombre)