from random import *
nombre = input('Introduzca su nombre: \r\n')
print('A continuacion vas a pensar en un numero del 1 al 100 y tendras 8 intentos para adivinarlo')

vidas = 8

aleatorio = randint(1,101)

intentos = 8 - vidas

while vidas > 0:
    numero = int(input('Introduzca su numero: \r\n'))
    if numero not in range(0,101):
        print('Por favor introduce numeros del 0-100')
    else:
        if numero == aleatorio:
            print(f'Numero correcto, Intentos restantes: {intentos}')
            break
        elif numero < aleatorio:
            print('Respuesta Incorrecta, haz elegido un numero menor al correcto')
            vidas -= 1
            print(f'Tienes {vidas} intentos restantes')

        elif numero > aleatorio:
            print('Respuesta Incorrecta, haz elegido un numero mayor al correcto')
            vidas -= 1
            print(f'Tienes {vidas} intentos restantes')
            

if numero != aleatorio:
    print(f'Lo siento se han agotado los intentos, el numero secreto era {aleatorio}')