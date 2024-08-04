def chequear_3_cifras(numero):
    return numero in range(100,1000)

resultado = chequear_3_cifras(658)
print(resultado)


#COMPROBAR NUMEROS DE 3 CIFRAS EN UNA LISTA
def chequear_3_cifras2(lista):

    for n in lista:
        if n in range(100,1000):
            return True
        else:
            pass
    
    return False #Para por si no hay ningun numero de 3 cifras, devuelve false
resultado = chequear_3_cifras2([55, 99, 6000])
print(resultado)

#LISTA QUE DEVUELVE LOS NUMEROS VERDADEROS
def chequear_3_cifras3(lista):

    lista_3_cifras = []

    for n in lista:
        if n in range(100,1000):
            lista_3_cifras.append(n)
        else:
            pass
    
    return lista_3_cifras
resultado = chequear_3_cifras3([554, 99, 600])
print(resultado)
