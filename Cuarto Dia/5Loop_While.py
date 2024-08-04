monedas = 5

#PARAR EL PROGRAMA CUANDO YA NO HAYA MONEDAS
while monedas > 0:
    print(f'Tengo {monedas}')
    monedas -= 1
else:
    print('No tengo mas dinero')


respuesta = 's'

while respuesta == 's':
    respuesta = input ('quieres seguir? (s/n)')
else: 
    print('Gracias')

#PASS (NO HACE NADA EL WHILE)
while respuesta == 's':
      pass

#BREAK PARA CORTAR EL LOOP
nombre = input('Nombre: ')
for letra in nombre:
    if letra == 'r':
        break
    print(letra)

#CONTINUE, (EN ESTE CASO QUITA LA R Y DESPUES CONTINUA)
nombre = input('Nombre: ')
for letra in nombre:
    if letra == 'r':
        continue
    print(letra)