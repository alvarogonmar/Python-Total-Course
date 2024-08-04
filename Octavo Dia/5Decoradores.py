def mayuscula(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())

#PASAR UNA FUNCION COMO VARIABLE
mi_funcion = mayuscula
mi_funcion('Python')

def una_funcion(funcion):
    return funcion

una_funcion(mayuscula('probando'))

#DEFINIR FUNCIONES DENTRO DE OTRAS FUNCIONES
def cambiar_letras(tipo):
    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo == 'may':
        return mayuscula
    elif tipo == 'min':
        return minuscula
    
operacion = cambiar_letras('may')

operacion ('palabra')

#
def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    return otra_funcion

@decorar_saludo
def mayusculas2(texto):
    print(texto.upper())

def minuscula2(texto):
    print(texto.lower())

mayusculas2('caca')

mayuscula_decorada = decorar_saludo(mayusculas2)
mayuscula_decorada('fede')