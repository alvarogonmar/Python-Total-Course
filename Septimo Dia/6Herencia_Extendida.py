class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color


    def nacer(self):
        print('Este animal ha nacido')
    
    def hablar(self):
        print('Este animal emite un sonido')


class Pajaro(Animal):
    #Funcion unica para especifico
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color) #PONER LAS QUE YA TENIAS EN LA PRIMER CLASS
        self.altura_vuelo = altura_vuelo

    #Funcion modificada 
    def hablar(self):
        print('pio')

    #Funcion que no existe en el padre
    def volar(self, metros):
        print(f'El pajaro vuela {metros} metros')

piolin = Pajaro(3, 'amarillo', 90)
piolin.hablar()
piolin.volar(100)

print('*' * 60)

class Padre:
    def hablar(self):
        print('hola')
    
class Madre:
    def reir(self):
        print('JA JA')
    
    def hablar(self): 
        print('TONTO')

class Hijo(Padre, Madre): #Hijo va decir lo que dice su padre al hablar, ya que padre esta primero en los parentesis
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()
#Ver el orden de donde hereda
print(Nieto.__mro__) 