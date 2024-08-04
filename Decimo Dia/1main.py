import pygame
import os
import random
import math
from pygame import mixer

#Iniciar
pygame.init()

#CREAR pantalla
pantalla = pygame.display.set_mode((800, 600))

#TITULO E ICONO
pygame.display.set_caption('Invasion Espacial')
icono = pygame.image.load('d:\\Python Total Curso\\Decimo Dia\\ovni.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('d:\\Python Total Curso\\Decimo Dia\\fondo.jpg')

#AGREGAR MUSICA
mixer.music.load('d:\\Python Total Curso\\Decimo Dia\\MusicaFondo.mp3')
mixer.music.play(-1) #-1 CADA VEZ QUE TERMINA SE REPITE

#VARIABLES DEL JUGADOR
img_jugador = pygame.image.load('d:\\Python Total Curso\\Decimo Dia\\cohete.png')
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

#VARIABLE ENEMIGOS
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load('d:\\Python Total Curso\\Decimo Dia\\enemigo.png'))
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(50,200))
    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(50)

#VARIABLE BALA
img_bala = pygame.image.load('d:\\Python Total Curso\\Decimo Dia\\bala.png')
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 0.6
bala_visible = False

#PUNTAJE
puntaje = 0
fuente = pygame.font.Font('freesansbold.ttf', 32) #TIPO DE FUENTE
texto_x = 10
texto_y = 10

#TEXTO FINAL DEL JUEGO
fuente_final = pygame.font.Font('freesansbold.ttf', 40)

def texto_final():
    mi_fuente_final = fuente_final.render('Juego Terminado', True, (255,255,255))
    pantalla.blit(mi_fuente_final, (250,250))


#FUNCION MOSTRAR PUNTAJE
def mostrar_puntaje(x, y):
    texto = fuente.render(f'Puntaje: {puntaje}', True, (255,255,255))
    pantalla.blit(texto, (x,y))


#Funcion jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y)) #ARROJAR
    
#Funcion ENEMIGO
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y)) #ARROJAR

#FUNCION DISPARAR BALA 
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))

#FUNCION DETECTAR COLISION
def hay_colision(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distancia < 27:
        return True
    else:
        return False
    

#NUEVA FUNCION
choque_nave = False

#Funcion colision con nave
def colision_nave(x_1, y_1, x_2, y_2):
    global choque_nave
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))

    if distancia < 50:
        choque_nave = True
    
    if choque_nave:
        return True
    else:
        return False


#LOOP DEL JUEGO
se_ejecuta = True
while se_ejecuta:

    #IMAGEN DE FONDO
    pantalla.blit(fondo, (0, 0))

    #ITERAR EVENTOS
    for evento in pygame.event.get():

        #EVENTO CERRAR
        if evento.type == pygame.QUIT: #Picarle para cerrar el programa
            se_ejecuta = False

        #EVENTO PRESIONAR TECLAS
        if evento.type == pygame.KEYDOWN: #tecla presionada
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.5
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.5
            if evento.key == pygame.K_SPACE:
                if bala_visible == False:
                    sonido_bala = mixer.Sound('d:\\Python Total Curso\\Decimo Dia\\disparo.mp3')
                    sonido_bala.play()
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        #EVENTO SOLTAR FLECHAS
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    #MODIFICAR UBICACION JUGADOR
    jugador_x += jugador_x_cambio

    #MANTENER DENTRO DE BORDES JUGADOR
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x=736


    #MOVIMIENTO BALA
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio


    #MODIFICAR UBICACION ENEMIGO
    for e in range(cantidad_enemigos):
        choque_nave = colision_nave(enemigo_x[e], enemigo_y[e], jugador_x, jugador_y)

        #FIN DEL JUEGO
        if enemigo_y[e] > 436 and choque_nave:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]

    #MANTENER DENTRO DE BORDES ENEMIGO
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.3
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.3
            enemigo_y[e] += enemigo_y_cambio[e]


        #COLISION
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound('d:\\Python Total Curso\\Decimo Dia\\golpe.mp3')
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1  
            enemigo_x[e] = random.randint(0,736)
            enemigo_y[e] = random.randint(50,200)

        enemigo(enemigo_x[e], enemigo_y[e], e)

    jugador(jugador_x, jugador_y)


    mostrar_puntaje(texto_x, texto_y)
    #ACTUALIZAR
    pygame.display.update()