texto = 'Este es el texto de Alvaro'

resultado = texto[2].upper() #agarrar solo una letra(indice)
print(resultado)

resultado = texto.lower()
print(resultado)

resultado = texto.split()
print(resultado)

resultado = texto.split('t') #CORTA CYANDO ENCUENTRA UNA 'T'
print(resultado)


a = 'Aprender'
b = 'Python'
c = 'es'
d = 'genial'
e = ' '.join([a,b,c,d])
print(e)

resultado = texto.find('s')
print(resultado)

resultado = texto.replace('Alvaro', 'todos')
print(resultado)