mi_tuple = (1,2,3,4)
print(mi_tuple[2])

mi_tuple = (1,2,(10,20) ,4)
print(mi_tuple[2][0])

#mi_tuple = list(mi_tuple) CONVERTIRLO EN LISTA

t = (1,2,3)
x,y,z = t
print(x,y,z)

mi_tuple = (1,2,3,4,1)
print(mi_tuple.count(1)) # CONTAR LA CANTIDAD DE APARICIONES DE UN VALOR DENTRO DE UN TUPLE
print(mi_tuple.index(2)) #TE DICE EN QUE LUGAR SE ENCUENTRA