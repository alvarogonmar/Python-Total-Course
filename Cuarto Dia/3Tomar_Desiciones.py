if 10 > 9:
    print('SI')


x = True
if x:
    print('Correcto')


if 5 == 2:
    print('Correcto')
else:
    print('Incorrecto')


mascota = 'perro'
if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
else:
    print('No se que animal tengas')

edad = 16
calificacion = 9
if edad < 18:
    print('Eres menor de edad')
    if calificacion >= 7:
        print('Aprobado')
    else:
        print('No aprobado')
else:
    print('Eres adulto')
