def mi_funcion():
    return 4

def mi_generador():
    yield 4

g = mi_generador()

print(next(g))

#HACER LISTAS
def mi_generador():
    for x in range (1, 5):
        yield x * 10

h = mi_generador()

print(next(h))
print(next(h))
print(next(h))

def mi_generador():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

g = mi_generador()

print(next(g))