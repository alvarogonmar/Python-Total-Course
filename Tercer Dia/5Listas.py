lista = ['a', 'b', 'c']
resultado = len(lista)
print(resultado)

lista = ['a', 'b', 'c']
resultado = lista[0]
print(resultado)

lista = ['a', 'b', 'c']
resultado = lista[0:2]
print(resultado)

lista = ['a', 'b', 'c']
lista2 = ['d', 'e', 'f']
print(lista + lista2)

lista = ['a', 'b', 'c']
lista2 = ['d', 'e', 'f']
lista[0] = 'CHOCOLATE' #CAMBIAR ELEMENTOS
print(lista + lista2)

lista = ['a', 'b', 'c']
lista2 = ['d', 'e', 'f']
lista3 = lista + lista2
lista3[0] = 'CHOCOLATE'
lista3.append('VAINILLA') #AGREGAR ELEMENTOS
print(lista3)

lista = ['a', 'b', 'c']
lista2 = ['d', 'e', 'f']
lista3 = lista + lista2
lista3[0] = 'CHOCOLATE'
lista3.pop(0) #ELIMINAR ELEMENTOS
print(lista3)

lista = ['a', 'b', 'c']
lista2 = ['d', 'e', 'f']
lista3 = lista + lista2
lista3[0] = 'CHOCOLATE'
eliminado = lista3.pop(0) #IMPRIMIR EL ELEMENTO ELIMINADO
print(lista3)
print(eliminado)

lista = ['a', 'z', 'e', 'g']
lista.sort() #ORDENAR LAS LISTAS PERO NO DEVUELVE NADA, ASI QUE NO SE LE PUEDE ASIGNAR UNA VARIABLE
print(lista)

lista = ['a', 'z', 'e', 'g']
lista.sort()
lista.reverse() #PONE DE LO ULTIMO A LO PRIMERO
print(lista)