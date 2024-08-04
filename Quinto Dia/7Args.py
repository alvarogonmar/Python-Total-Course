def suma(*args):
    total = 0

    for arg in args:
        total += arg
    return total

print(suma(5,6,7,8,9,9,8,8,7,7,7))

#FORMA REDUCIDA
def suma(*args):
    return sum(args)
print(suma(3,4,3,3,3,4,4))

