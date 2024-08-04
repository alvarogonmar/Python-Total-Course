class CD:

    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f'Album: {self.titulo} de {self.autor}'
    
    def __len__(self):
        return self.canciones

    #MODIFICAR LA FUNCION del
    def __del__(self):
        print('SE HA ELIMINADO EL CD')

mi_cd = CD('Pink Floyd', 'The Wall', 24)
#DEVOLVER LARGO DE CANCIONES
print(len(mi_cd))
del mi_cd