palabra = 'python'

lista = []

for letra in palabra:
    lista.append(letra)
print(lista)

#COMPRENSION DE LISTAS (ELIMINAR LINEAS DE CODIGO)
palabra = 'python'

lista = [letra for letra in palabra]
print(lista)

#OTRA FORMA CON MENOS LINEAS

lista = [letra for letra in 'python']
print(lista)

#VALORES NUMERICOS
lista = [n for n in range(0,21,2)]
print(lista)

#HACER OPERACIONES 
lista = [n/2 for n in range(0,21,2)]
print(lista)

#INCORPORAR IF
lista = [n for n in range(0,21,2) if n*2>10 ]
print(lista)

# 2da OPCION IF CON ELSE
lista = [n if n*2>10 else 'no' for n in range(0,21,2) ]
print(lista)

pies = [10,20,30,40,50]
metros = [n / 3.281 for n in pies]
print(metros)

