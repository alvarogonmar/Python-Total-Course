from os import system
from pathlib import Path
import os

ruta = Path(Path.home(), 'd:\\Recetas')

def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob('**/*.txt'):
        contador += 1
    return contador

def inicio ():
    system('cls')
    print('Bienvenido al administrador de recetas')
    print(f'Las recetas se encuentran en {ruta}')
    print(f'Total recetas: {contar_recetas(ruta)}')
    print('*' * 50)

def mostrar_menu():
    print('Seleccione del Menu lo que desea hacer: ')
    print('1) Leer receta')
    print('2) Crear receta')
    print('3) Crear categoria')
    print('4) Eliminar receta')
    print('5) Eliminar categoria')
    print('6) Finalizar programa')

def mostrar_categoria(ruta):
    print('Categorias: ')
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir(): #Permite iterar dentro del directorio
        carpeta_str = str(carpeta.name)
        print(f'[{contador}] - {carpeta_str}')
        lista_categorias.append(carpeta)
        contador += 1
 
    return lista_categorias  

def elegir_categoria(lista):
    eleccion_correcta = 'x'

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input('\nElige una categoria: ')
    return lista[int(eleccion_correcta) - 1]

def mostrar_recetas(ruta):
    print('Recetas: ')
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f'[{contador}] - {receta_str}')
        lista_recetas.append(receta)
        contador += 1
    
    return lista_recetas

def elegir_receta(lista):
    eleccion_correcta = 'x'

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input('\nElige una receta: ')
    return lista[int(eleccion_correcta) - 1]

def leer_la_receta_elegida(receta):
    print(Path.read_text(receta))
    
def leer_receta():
    mis_categorias = mostrar_categoria(ruta)
    mi_categoria = elegir_categoria(mis_categorias)
    mis_recetas = mostrar_recetas(mi_categoria)
    if len(mis_recetas) < 1:
            print("No hay recetas en esta categoría.")
    else:
        mi_receta = elegir_receta(mis_recetas)
        leer_receta(mi_receta)
    volver_inicio()


def escribir_receta(ruta):
    existe = False

    while not existe:
        print('Escribe el nombre de tu receta: ')
        nombre_receta = input() + '.txt'
        print('Escribe tu nueva receta: \r\n')
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f'Tu receta {nombre_receta} ha sido creada')
            existe = True
        else:
            print('Esa receta ya existe')

def crear_receta(ruta):
    mis_categorias = mostrar_categoria(ruta)
    mi_categoria = elegir_categoria(mis_categorias)
    mi_nueva_receta = escribir_receta(mi_categoria)
    volver_inicio()

def crear_categoria(ruta):
    existe = False

    while not existe:
        print('Escribe el nombre de tu categoria: ')
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f'Tu categoria {nombre_categoria} ha sido creada')
            existe = True
        else:
            print('Esa categoria ya existe')

def elegir_receta_eliminada(receta):
    #unlink elimina un archivo
    Path(receta).unlink
    print('Receta Eliminada')

def eliminar_receta():
    mis_categorias = mostrar_categoria(ruta)
    mi_categoria = elegir_categoria(mis_categorias)
    mis_recetas = mostrar_recetas(mi_categoria)
    if len(mis_recetas) < 1:
            print("No hay recetas en esta categoría.")
    else:
        mi_receta = elegir_receta_eliminada(mi_receta)
        leer_receta(mi_receta)
    volver_inicio()

def elegir_categoria_eliminada(categoria):
    Path(categoria).rmdir()
    print('Categoria Eliminada')
    volver_inicio()

def eliminar_categoria():
    mis_categorias = mostrar_categoria(ruta)
    mi_categoria = elegir_categoria(mis_categorias)
    elegir_categoria_eliminada(mi_categoria)
    volver_inicio()

def volver_inicio():
    eleccion_regresar = 'x'

    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input('\nPresione V para volver al menu: ')
    system('cls')

def app():
        finalizar_programa = False
        while not finalizar_programa:
            inicio()

            preguntar = True
            while preguntar:
                mostrar_menu()
                opcion = input('Selecione una opcion: \r\n')
                opcion = int(opcion)

                if opcion == 1:
                    leer_receta()
                elif opcion == 2:
                    crear_receta(ruta)
                elif opcion == 3:
                    crear_categoria(ruta)
                elif opcion == 4:
                    eliminar_receta()
                elif opcion == 5:
                    eliminar_categoria()
                elif opcion == 6:
                    volver_inicio()
                else:
                    finalizar_programa = True


app()
