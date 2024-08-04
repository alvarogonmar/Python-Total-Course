import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

#OPCIONES DE VOZ
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

#ESCUCHAR MICROFONO Y DEVOLVER EL AUDIO COMO TEXTO
def transformar_audio_en_texto():

    # ALMACENAR RECOGNIZER EN VARIABLE
    r = sr.Recognizer()

    #CONFIGURAR EL MICROFONO
    with sr.Microphone() as origen:

        #Tiempo de espera
        r.pause_threshold = 0.8

        #INFORMAR QUE COMENZO LA GRABACION
        print('Ya puedes hablar')

        #Guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            #BUSCAR EN GOOGLE 
            pedido = r.recognize_google(audio, language='es-mx')

            #PRUEBA DE QUE PUDO INGRESAR
            print(f'Dijiste: {pedido}')

            #DEVOLVER PEDIDO
            return pedido
        
        #EN CASO DE QUE NO COMPRENDA EL AUDIO
        except sr.UnknownValueError:

            #PRUEBA DE QUE NO COMPRENDIO EL AUDIO
            print('Ups, no entendi')

            #Devolver error
            return 'Sigo esperando'
        
        #EN CASO DE NO RESOLVER EL PEDIDO

        except sr.RequestError:

            #PRUEBA DE QUE NO COMPRENDIO EL AUDIO
            print('Ups, no entendi')

            #Devolver error
            return 'Sigo esperando'
        
        #ERROR INESPERADO
        except:
            #PRUEBA DE QUE NO COMPRENDIO EL AUDIO
            print('Ups, algo ha salido mal')

            #Devolver error
            return 'Sigo esperando'
        
# FUNCION PARA QUE EL ASISTENTE PUEDA SER ESCUCHADO
def hablar(mensaje):

    # ENCENDER EL MOTOR DE PYTTSX3
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)

    #PRONUNCIAR MENSAJE
    engine.say(mensaje)
    engine.runAndWait()

#INFORMAR DIA DE LA SEMANA
def pedir_dia():

    #CREAR VARIABLE CON DATOS DE HOY
    dia = datetime.date.today()
    print(dia)

    #CREAR VARIABLE PARA EL DIA DE SEMANA
    dia_semana = dia.weekday()
    print(dia_semana)

    #diccionario con nombres de dias
    calendario = {0: 'Lunes',
                  1: 'Martes',
                  2: 'Miércoles',
                  3: 'Jueves',
                  4: 'Viernes',
                  5: 'Sábado',
                  6: 'Domingo'}
    
    #DECIR EL DIA DE LA SEMANA
    hablar(f'Hoy es {calendario[dia_semana]}')


#INFORMAR HORA
def pedir_hora():
    
    #CREAR VARIABLE CON DATOS DE LA HORA
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)

    #DECIR LA HORA
    hablar(hora)

#FUNCION SALUDO INICIAL
def saludo_inicial():

    #CREAR VARIABLE CON DATOS DE HORA
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour >20:
        momento = 'Buenas noches'
    elif  6 <= hora.hour < 13:
        momento = 'Buen dia'
    else:
        momento = 'Buenas tardes'

    #decir saludo
    hablar(f'{momento}, soy Jarvis, tu asistente personal. Por favor dime en que puedo ayudarte')


#FUNCION CENTRAL DEL ASISTENTE
def pedir_cosas():
    
    #ACTIVAR SALUDO INICIAL
    saludo_inicial()

    #VARIABLE DE CORTE
    comenzar = True
    
    #LOOP CENTRAL
    while comenzar:

        #ACTIVAR MICRO Y GUARDAR PEDIDO EN STRING
        pedido = transformar_audio_en_texto().lower()

        if 'abre youtube' in pedido:
            hablar('Con gusto, estoy abriendo youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abre el youtube' in pedido:
            hablar('Con gusto, estoy abriendo youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'abre google' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'abre el navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'abre navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            try:
                hablar('Buscando eso en wikipedia')
                pedido = pedido.replace('busca en wikipedia', '').strip()
                if pedido:
                    wikipedia.set_lang('es')
                    resultado = wikipedia.summary(pedido, sentences=1)
                    hablar(f'De acuerdo a lo que encontré en wikipedia: {resultado}')
                else:
                    hablar('Por favor, di lo que quieres buscar en wikipedia.')
            except wikipedia.exceptions.DisambiguationError as e:
                hablar('Por favor, di lo que quieres buscar en wikipedia.')
            except wikipedia.exceptions.PageError:
                hablar('No encontré ninguna página para esa búsqueda.')
            except:
                hablar('Ups, algo ha salido mal buscando en wikipedia.')
        elif 'busca en internet' in pedido:
            pedido = pedido.replace('busca en internet', '')
            hablar(f'Buscando {pedido}')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado en internet')
            continue
        elif 'reproduce' in pedido:
            pedido = pedido.replace('reproduce', '')
            hablar(f'Reproduciendo {pedido}')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'adiós' in pedido:
            hablar('Para servirte, cualquier cosa me llamas')
            break
        
pedir_cosas()
