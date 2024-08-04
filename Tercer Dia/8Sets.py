mi_set = set([1,2,3,4,5])
print(mi_set)

otro_set = {1,2,3}
print(otro_set)

mi_set = set((1,2,(1,2,3),4,5)) #TUPLE SI SE PUEDE PONER PQ TMB ES INMUTABLE
print(mi_set)

mi_set = set([1,2,3,4,5])
print(2 in mi_set) #BUSCAR UN ELEMENTO

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2) #UNIR SETS
print(s3)

s1 = {1,2,3}
s1.add(4) #AGREGAR UN ELEMENTO
print(s1)

s1 = {1,2,3}
s1.remove(3) #ELIMINAR UN ELEMENTO
print(s1)

s1 = {1,2,3}
s1.discard(2) #DESCARTAR UN ELEMENTO
print(s1)

s1 = {1,2,3}
sorteo = s1.pop() #ELIMINA UN ELEMENTO ALEATORIO (SORTEOS)
print(sorteo)

s1 = {1,2,3}
s1.clear() #VACIA NUESTRO SET
print(s1)

#CHECAR NOTAS