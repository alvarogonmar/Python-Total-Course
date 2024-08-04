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

piolin = Pajaro('amarillo', 'canario')
piolin.piar()
piolin.volar(50)
