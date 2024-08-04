class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice muuuu')

class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice beee')    
    

vaca1 = Vaca('Aurora')
oveja1 = Oveja('Nube')

animales = [vaca1, oveja1]

#Ejecutar el mismo metodo pero hacer cosas distintas
for animal in animales:
    animal.hablar()

#Lo mismo que arriba
def animal_hablar(animal):
    animal.hablar()

animal_hablar(vaca1)
animal_hablar(oveja1)