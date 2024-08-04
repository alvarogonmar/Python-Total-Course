import os

archivo = open('curso.txt', 'w')
archivo.write('texto de prueba')
archivo.close()

print(os.listdir())

#Abrir archivos

import shutil

shutil.move('curso.txt', 'C\\Users\\Win0\\Desktop')

#Eliminar archivos
os.unlink