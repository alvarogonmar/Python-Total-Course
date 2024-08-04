lista = ['a', 'b', 'c']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f'Letra {numero_letra}: {letra}')

#BUSCAR NOMBRES QUE EMPIECEN CON DETERMINADA LETRA
lista = ['pablo', 'laura', 'fede', 'luis', 'julia']
for nombre in lista:
    if nombre.startswith('l'):
        print(nombre)


numeros = [1,2,3,4,5]
mi_valor = 0

#AQUI DARA EL RESULTADO TODO JUNTO
for numero in numeros:
    mi_valor = mi_valor + numero
print(mi_valor)

#AQUI VA A DAR RESULTADO POR CADA NUMERO
for numero in numeros:
    mi_valor = mi_valor + numero
    print(mi_valor)

#TIPO DELETREAR UNA PALABRA
palabra = 'python'
for letra in palabra:
    print(letra)

print('\n')
#OTRA FORMA DE DELETREAR 
for letra in 'python':
    print(letra)

print('\n')
for objeto in [[1,2], [3,4], [5,6]]:
    print(objeto)

print('\n')
#ITERAR UNA LISTA DENTRO DE OTRA LISTA, a es para el primer objeto de la lista, b es para el segundo
for a,b in [[1,2], [3,4], [5,6]]:
    print(a)
    print(b)

dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}
for item in dic.items(): #PARA VER TODAS LAS CLAVES CON VALORES
    print(item)

dic = {'clave1': 'a', 'clave2': 'b', 'clave3': 'c'}
for item in dic.values(): #SOLO VER VALORES
    print(item)  