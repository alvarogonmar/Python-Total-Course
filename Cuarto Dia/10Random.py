from random import *

aleatorio = randint(1,50)
print(aleatorio)

aleatorio = round(uniform(1,5),1) #ROUND PARA QUITAR DECIMALES
print(aleatorio)

#ELIGE UN NUMERO DECIMAL ENTRE 0 Y 1
aleatorio = random()
print(aleatorio)

#ELEGIR UN COLOR ALEATORIO
colores = ['azul', 'verde', 'rojo', 'amarillo']
aleatorio = choice(colores)
print(aleatorio)

#MEZCLAR LOS NUMEROS
numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)