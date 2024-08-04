import bs4
import requests

resultado = requests.get('https://www.escueladirecta.com/courses/')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

imagenes = sopa.select('.course-box-image')
print(imagenes)

'''for i in imagenes:
    print(i)'''


#SOLAMENTE URL
imagenes = sopa.select('.course-box-image')[0]['src']
print(imagenes)

imagen_1 = requests.get(imagenes)

#GUARDAR IMAGEN
f = open('mi_imagen.jpg', 'wb')
f.write(imagen_1.content)
f.close


'''resultado = requests.get(url_base.format('1'))
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

libros = (sopa.select('.product_pod'))

#TOMAR TITULO DEL LIBRO
ejemplo = libros[0].select('a')[1]['title']
print(ejemplo)
'''
