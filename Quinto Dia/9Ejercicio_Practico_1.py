
def devolver_distintos(a, b, c):
    
    suma = a + b + c
    numeros = [a, b, c]
    
    if suma > 15:
        return max(numeros)
    else: 
        pass
    if suma < 10:
        return min(numeros)
    else:
        numeros.sort()
        return numeros[1]

print(devolver_distintos(11,1,3))
