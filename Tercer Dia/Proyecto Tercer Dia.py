#PROYECTO TERCER DIA

texto = input('Introduce un texto: \r\n')
letras = []

texto = texto.lower()

letras.append(input('Introduce la primer letra que quieras analizar: \r\n').lower())
letras.append(input('Introduce la segunda letra que quieras analizar: \r\n').lower())
letras.append(input('Introduce la tercer letra que quieras analizar: \r\n').lower())

print('CANTIDAD DE LETRAS')
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f'Hemos encontrado la letra "{letras[0]}" repetida {cantidad_letras1} veces')
print(f'Hemos encontrado la letra "{letras[1]}" repetida {cantidad_letras2} veces')
print(f'Hemos encontrado la letra "{letras[2]}" repetida {cantidad_letras3} veces')

print('\n')
# Dividir el texto en palabras utilizando split()
palabras = texto.split()
# Contar el número de palabras
num_palabras = len(palabras)
print(f"El texto tiene {num_palabras} palabras.")

primera_palabra = palabras[0]
ultima_palabra = palabras[-1]
print(f"La primera palabra es: {primera_palabra}")
print(f"La última palabra es: {ultima_palabra}")


palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f'Si ordenamos tu texto al reves va a decir "{texto_invertido}"')

buscar_python = 'python' in texto.lower()
dic = {True: 'si', False: 'no'}
print(f'La palabra "Python" {dic[buscar_python]} se encuentra en el texto')