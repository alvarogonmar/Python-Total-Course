#PROGRAMA DE COMISIONES

nombre = input('Cual es tu nombre?: \r\n')
ventas = float(input('Cantidad de dinero ganado por ventas: \r\n'))
ganancia = round(ventas*(13/100), 2)
print(f'{nombre}, tu comision de este mes es: {ganancia}')