nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65,29,42]
ciudades = ['Lima', 'Madrid', 'CDMX']

combinados = list(zip(nombres, edades,ciudades)) #TENEMOS QUE PONERLO DENTRO DE UNA LISTA
print(combinados)

for nombre,edad,ciudad in combinados:
    print(f'{nombre} tiene {edad} anios y vive en {ciudad}')