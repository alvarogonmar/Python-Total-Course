mi_archivo = open('prueba.txt')
#Leer archivo
print(mi_archivo.read())

#Leer una linea
print(mi_archivo.readline())

#Si quiero leer las demas lineas: repetir
una_linea = mi_archivo.readline()
print(una_linea)

una_linea = mi_archivo.readline()
print(una_linea.rstrip) #Quitar saltos de linea

una_linea = mi_archivo.readline()
print(una_linea)


mi_archivo.close()