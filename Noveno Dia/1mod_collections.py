from collections import Counter

#Contar letras en una palabra
print(Counter('misisisisisipipi'))

#Contar palabras de una oracion
frase = 'al pan pan al vino vino'
print(Counter(frase.split()))   #split quita los espacios en blanco

#Metodos de counter:

serie = Counter([1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3])
#Mas comun
print(serie.most_common())
#Lista
print(list(serie))




from collections import defaultdict

mi_dic = defaultdict(lambda:'nada')

mi_dic['uno'] = 'verde'
print(mi_dic['dos'])

print(mi_dic)


#ACCEDER A TUPLAS A TRAVES DE UN NOMBRE
from collections import namedtuple

Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.90, 100)

print(ariel)