import re




texto = 'Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online'

patron = 'ayuda'

busqueda = re.search(patron, texto)
print(busqueda)
#Ubicacion de la palabra
print(busqueda.span())
#Ubicacion del comienzo de la palabra
print(busqueda.start())
#Ubicacion final
print(busqueda.end())


#Encontrar mas de una palabra
busqueda = re.findall(patron, texto)
print(busqueda)

#Encontrar ubicaciones de los elementos
for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())



#PATRON 2

texto = 'llama al 564-525-6588 ya mismo'

patron = r'\d\d\d-\d\d\d-\d\d\d\d' 

resultado = re.search(patron, texto)
print(resultado)

#Obtener el telefono
print(resultado.group())

#CUantificador y mostrar solo un grupo
patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado = re.search(patron, texto)

print(resultado.group(2))


"""Clave
clave = input('Clave: ')
patron = r'\D{1}\w{7}'
checar = re.search(patron, clave)
print(checar)"""

#
texto = 'No atendemos los lunes por la tarde'

buscar = re.search(r'lunes|martes', texto)
print(buscar)

#MOSTRAR LAS LETRAS DE ANTES DE LA PALABRA ENCONTRADA

buscar = re.search(r'...demos.....', texto)
print(buscar)

#VER SI UN PATRON SE INDICA AL COMIENZO DE UN STRING

buscar = re.search(r'^\D', texto)
print(buscar)


#CHECAR CON LO QUE FINALIZA
buscar = re.search(r'\D$', texto)
print(buscar)

#EXCLUIR
buscar = re.findall(r'[^\s]+', texto)
print(buscar)