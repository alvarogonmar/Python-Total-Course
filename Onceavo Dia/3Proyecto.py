import bs4
import requests

url_base = 'https://books.toscrape.com/catalogue/page-{}.html'


#LISTA DE TITULOS CON 4 O 5 ESTRELLAS
titulos_rating_alto = []

#iterar paginas
for pagina in range(1,51):

    #CREAR SOPA EN CADA PAGINA
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    #SELECCIONAR DATOS DE LOS LIBROS
    libros = sopa.select('.product_pod')

    #ITERAR LIBROS
    for libro in libros:

        #CHECAR QUE TENGAN 4 O 5 ESTRELLAS
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:

            #Guardar titulo en variable
            titulo_libro = libro.select('a')[1]['title']

            #AGREGAR LIBRO A LA LISTA
            titulos_rating_alto.append(titulo_libro)

#ver los libros de 4 y 5 estrellas en consola
for t in titulos_rating_alto:
    print(t)