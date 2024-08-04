class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color =  color
        self.especie = especie
    
    def piar(self):
        #Cada vez que dentro de la clase construya un metodo necesito poner self
        print('pio, mi color es {}'.format(self.color))
    
    def volar(Self, metros):
        print(f'El pajaro ha volado {metros} metros')

    #A este tipo de metodos se le pone "cls"
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'Puso {cantidad} huevos')


    @staticmethod
    def mirar():
        print('El pajaro mira')


piolin = Pajaro('amarillo', 'canario')
Pajaro.poner_huevos(3)
Pajaro.mirar()