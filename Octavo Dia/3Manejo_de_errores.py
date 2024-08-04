def suma():
    n1 = int(input('numero 1 :  '))
    n2 = int(input('numero 2:   '))
    print(n1+n2)
    print('Gracias por sumar' + n1)



'''#CODIGO QUE QUEREMOS PROBAR
try:
    suma()

#CODIGO A EJECUTAR SI HAY ERROR
except TypeError:
    print('Estas intentando concatenar tipos distintos')

except ValueError:
    print('Ese no es un numero')
#Codigo a ejecutar si no hay un error
else:
    print('Hiciste todo bien')

#CODIGO QUE SE VA EJECUTAR DE TODOS MODOS
finally:
    print('Eso fue todo')'''

def pedir_numero():
    while True:
        try:
            numero = int(input('Dame un numero: '))
        except:
            print('Ese no es un numero')
        else:
            print(f'Ingresaste el numero {numero}')
            break
print('Gracias')

pedir_numero()