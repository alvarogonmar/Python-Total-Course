def funcion(*args):
    contador = 0

    for num in args:
        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1
    return False

print(funcion(1,3,5,5,0,3,23,34,54,0))