def alfabeto(palabra):
    mi_set = set()

    for letra in palabra:
        mi_set.add(letra)

    mi_lista = list(mi_set) #Agregarlas a la lista
    mi_lista.sort() #Ordenarlas alfabeticamente

    return mi_lista

print(alfabeto('entretenido'))

