archivo = open('prueba.txt', 'w')
archivo.write('hola \n mundo \n')

#Escribir lineas y strings uno detras del otro
archivo.writelines(['Hola', 'mundo\n'])

#Lista
lista = ['Hola', 'mundo', 'aqui', 'estoy']
for p in lista:
    archivo.writelines(p + '\n')

#uSANDO METODO 'a' ESCRIBE AL FINAL DEL TEXTO QUE YA HAY
'''archivo = open('prueba.txt', 'a')
archivo.write('Bienvenido')
'''
archivo.close()