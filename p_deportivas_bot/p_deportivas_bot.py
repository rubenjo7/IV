# -*- coding: utf-8 -*-
import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
import random
import datetime
import urllib3
import sqlite3 as lite
import consultas
import modificaciones
import os
import string

TOKEN = os.environ['token_bot'] #Nuestro tokken del bot (el que @BotFather nos dió).

bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.
en_conversacion_seleccion = False
en_conversacion_goles = False
contador_jugadores = 0
esta_seleccionando = 0
inserta_goles = 0
numero1 = -1
numero2 = -1

def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        if m.content_type == 'text': # Filtramos mensajes que sean tipo texto.
            cid = m.chat.id # Almacenaremos el ID de la conversación.
            mensajes = m.text
            if(mensajes == '/seleccionar' or mensajes == '/parar_seleccionar' or mensajes == '/goles' or mensajes == '/parar_goles' or not mensajes.startswith('/')):
                seleccion_goles(mensajes, cid)
            elif not mensajes == '/insertar' and not mensajes == '/borrar' and not mensajes == '/mostrar' and not mensajes == '/sortear' and not mensajes == '/cancelar_sorteo' and not mensajes == '/resultado' and not mensajes == '/clasificacion' and not mensajes == '/clasificacion_goles' and not mensajes == '/clasificacion_puntos':
                bot.send_message(cid, "Error. Comando no existente.")

            print "Fecha y hora: " + time.strftime("%c")
            print "[" + str(cid) + "]: " + m.text # Y haremos que imprima algo parecido a esto -> [52033876]: /start


def seleccion_goles(mensajes, cid):
    global en_conversacion_seleccion
    global contador_jugadores
    global esta_seleccionando
    global en_conversacion_goles
    global inserta_goles
    global numero1
    global numero2
    if mensajes == '/seleccionar' and esta_seleccionando == 0 and not inserta_goles == 1:
        en_conversacion_seleccion = True
        bot.send_message(cid, "Vamos a seleccionar jugadores, recuerda que deben estar añadidos.")
        esta_seleccionando = 1
        contador_jugadores = 0
        consultas.borraListaCompleta()
        consultas.borraEquipo1Goles()
        consultas.borraEquipo2Goles()
    elif mensajes == '/seleccionar' and inserta_goles == 1:
        bot.send_message(cid, "Error. Ahora se están insertando goles, usa /parar_goles para finalizar la inserción.")
    elif esta_seleccionando == 1 and mensajes == '/seleccionar':
        bot.send_message(cid, "Error. Ya estas usando esta opción.")
    elif esta_seleccionando == 0 and mensajes == '/parar_seleccionar':
        bot.send_message(cid, "Error. Tienes que estar seleccionando para poder cancelar la selección.")
    elif contador_jugadores < 2 and mensajes == '/parar_seleccionar':
        bot.send_message(cid, "Error. Tienes que añadir al menos dos jugadores para poder parar la selección.")
    elif mensajes == '/parar_seleccionar' and contador_jugadores >= 2:
        en_conversacion_seleccion = False
        bot.send_message(cid, "Finaliza selección de jugadores, has seleccionado " + str(contador_jugadores) + "  jugadores.")
        contador_jugadores = 0
        esta_seleccionando = 0
    elif not mensajes.startswith('/') and en_conversacion_seleccion:
        contador = consultas.consulta_por_valor(mensajes)
        if contador == 1 and not mensajes in consultas.getListaCompleta():
            bot.send_message(cid, mensajes + " seleccionado.")
            contador_jugadores+=1
            consultas.aniadeListaCompleta(mensajes)
        elif contador == 0:
            bot.send_message(cid, "Error. No existe el jugador.")
        elif mensajes in consultas.getListaCompleta():
            bot.send_message(cid, "Error. Jugador ya añadido.")
    elif numero1 == -1 and numero2 == -1 and mensajes == '/goles':
        bot.send_message(cid, "Error. Debes ingresar un resultado antes de añadir los goles.")
    elif mensajes == '/goles' and  esta_seleccionando == 1:
        bot.send_message(cid, "Error. Ahora se están seleccionando jugadores, usa /parar_seleccionar para finalizar la selección.")
    elif mensajes == '/goles' and not esta_seleccionando == 1 and inserta_goles == 0:
        en_conversacion_goles = True
        bot.send_message(cid, "Vamos a insertar goleadores, recuerda que deben estar añadidos a algun equipo.")
        inserta_goles = 1
    elif inserta_goles == 1 and mensajes == '/goles':
        bot.send_message(cid, "Error. Ya estas usando esta opción.")
    elif inserta_goles == 0 and mensajes == '/parar_goles':
        bot.send_message(cid, "Error. Tienes que estar insertando goles para poder cancelar la inserción de goles.")
    elif mensajes == '/parar_goles' and ((len(consultas.getEquipo1Goles()) == 0 or numero1 == 0) or (len(consultas.getEquipo2Goles()) == 0 or numero2 == 0)):
        en_conversacion_goles = False
        bot.send_message(cid, "Finaliza inserción de goles, puedes consultar el resultado en /clasificacion_goles")
        inserta_goles = 0
        numero1 = -1
        numero2 = -1
    elif mensajes == '/parar_goles' and ((not len(consultas.getEquipo1Goles()) == 0 or not numero1 == 0) or (not len(consultas.getEquipo2Goles()) == 0 or not numero2 == 0)):
        bot.send_message(cid, "Error. Resultado 1 o Resultado 2 no añadido en su totalidad.")
    elif not mensajes.startswith('/') and en_conversacion_goles and not len(mensajes.split()) == 2:
        bot.send_message(cid, "Error. Tienes que insertar goles de la forma: nombre numero")
    elif not mensajes.startswith('/') and en_conversacion_goles and len(mensajes.split()) == 2:
        tupla = mensajes.split()
        if tupla[0].isnumeric():
            bot.send_message(cid, "Error. El primer argumento tiene que ser un string.")
        elif not tupla[1].isnumeric():
            bot.send_message(cid, "Error. El segundo argumento tiene que ser un numero.")
        else:
            gol = int(float(tupla[1]))
            nom = str(tupla[0])
            if nom in consultas.getEquipo1Goles():
                if (numero1 - gol) < 0:
                    bot.send_message(cid, "Error. Estas ingresando mal el resultado 1.")
                else:
                    goles = consultas.goles_jugador(nom)
                    goles += gol
                    modificaciones.actualizar_goles(nom, goles)
                    consultas.borraIndiceEquipo1Goles(nom)
                    numero1 = numero1 - gol
                    if numero1 > 0:
                        bot.send_message(cid, "Quedan por ingresar " + str(numero1) + " goles en el resultado 1.")
                    else:
                        bot.send_message(cid, "Resultado 1 ingresado.")
            elif nom in consultas.getEquipo2Goles():
                if (numero2 - gol) < 0:
                    bot.send_message(cid, "Error. Estas ingresando mal el resultado 2.")
                else:
                    goles = consultas.goles_jugador(nom)
                    goles += gol
                    modificaciones.actualizar_goles(nom, goles)
                    consultas.borraIndiceEquipo2Goles(nom)
                    numero2 = numero2 - gol
                    if numero2 > 0:
                        bot.send_message(cid, "Quedan por ingresar " + str(numero2) + " goles en el resultado 2.")
                    else:
                        bot.send_message(cid, "Resultado 2 ingresado.")
            else:
                bot.send_message(cid, "Error. Este jugador no esta en ningún equipo.")
    elif not mensajes.startswith('/'):
        bot.send_message(cid, "Error. El mensaje no tiene sentido.")


@bot.message_handler(commands=['start', 'help', 'ayuda'])
def command_ayuda(m):
    cid = m.chat.id
    texto = "*Funcionamiento de Peñas deportivas:*\n\n• /insertar nombre\_Jugador: Inserta a un jugador en la peña.\n• /borrar id: Borrar a un jugador por su identificador. \n• /mostrar: Muestra a todos los jugadores y sus identificadores.\n• /seleccionar: Inicia conversación con el bot para añadir jugadores para el sorteo. \n• /parar\_seleccionar: Finaliza la selección de jugadores. Debe haber al menos dos jugadores seleccionados. \n• /sortear: Sortea dos equipos de manera aleatoria. \n• /cancelar\_sorteo: Cancela el sorteo.\n• /resultado x-x: Se inserta el resultado del partido, en función de los equipos sorteados, siendo x un numero. \n• /goles: Inicia conversación con el bot para insertar los goles al jugador de la forma 'nombre\_jugador gol'. \n• /parar\_goles: Finaliza la conversación de insercción de goles. \n• /clasificacion: Muestra la clasificación de los jugadores en función de puntos y goles. \n• /clasificacion\_goles: Muestra los goles que lleva cada jugador. \n• /clasificacion\_puntos: Muestra solo los puntos que lleva cada jugador en ese momento."
    bot.send_message(cid, texto, parse_mode="Markdown")



@bot.message_handler(commands=['insertar'])
def command_insertar(m):
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    jugador = m.text[10:20]

    if en_conversacion_seleccion:
        bot.send_message(cid, "Error. Ahora se están seleccionando jugadores, usa /parar_seleccionar para finalizar la selección.")
    elif en_conversacion_goles:
        bot.send_message(cid, "Error. Ahora se están insertando goles, usa /parar_goles para finalizar la inserción.")
    elif len(jugador) == 0:
        bot.send_message(cid, "Error. Debes introducir un nombre.")
    elif ' ' in jugador:
        bot.send_message(cid, "Error. Has introducido espacios en el nombre.")
    elif len(jugador) > 9:
        bot.send_message(cid, "Error. Nombre demasiado largo.")
    else:
        contador = consultas.consulta_por_valor(jugador)
        if contador == 1:
            bot.send_message(cid, "Error. Nombre de jugador ya añadido.")
        elif contador == 0:
            modificaciones.insertar_jugador(jugador)
            bot.send_message(cid, jugador + " introducido.")
        else:
            bot.send_message(cid, "Error inesperado.")



@bot.message_handler(commands=['mostrar'])
def command_mostrar(m):
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    vacio = m.text[8:20]
    cadena = ""

    if en_conversacion_seleccion:
        bot.send_message(cid, "Error. Ahora se están seleccionando jugadores, usa /parar_seleccionar para finalizar la selección.")
    elif en_conversacion_goles:
        bot.send_message(cid, "Error. Ahora se están insertando goles, usa /parar_goles para finalizar la inserción.")
    elif len(vacio) == 0:
        cadena = consultas.consultar()
        bot.send_message(cid, cadena, parse_mode="Markdown")
    else:
        bot.send_message(cid, "Error. Este mensaje no necesita argumentos.")

@bot.message_handler(commands=['clasificacion'])
def command_clasificacion(m):
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    vacio = m.text[14:20]
    cadena = ""

    if en_conversacion_seleccion:
        bot.send_message(cid, "Error. Ahora se están seleccionando jugadores, usa /parar_seleccionar para finalizar la selección.")
    elif en_conversacion_goles:
        bot.send_message(cid, "Error. Ahora se están insertando goles, usa /parar_goles para finalizar la inserción.")
    elif len(vacio) == 0:
        cadena = consultas.clasificacion()
        bot.send_message(cid, cadena, parse_mode="Markdown")
    else:
        bot.send_message(cid, "Error. Este mensaje no necesita argumentos.")

@bot.message_handler(commands=['clasificacion_goles'])
def command_clasificacionGoles(m):
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    vacio = m.text[20:30]
    cadena = ""

    if en_conversacion_seleccion:
        bot.send_message(cid, "Error. Ahora se están seleccionando jugadores, usa /parar_seleccionar para finalizar la selección.")
    elif en_conversacion_goles:
        bot.send_message(cid, "Error. Ahora se están insertando goles, usa /parar_goles para finalizar la inserción.")
    elif len(vacio) == 0:
        cadena = consultas.clasificacion_goles()
        bot.send_message(cid, cadena, parse_mode="Markdown")
    else:
        bot.send_message(cid, "Error. Este mensaje no necesita argumentos.")

@bot.message_handler(commands=['clasificacion_puntos'])
def command_clasificacionPuntos(m):
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    vacio = m.text[21:30]
    cadena = ""

    if en_conversacion_seleccion:
        bot.send_message(cid, "Error. Ahora se están seleccionando jugadores, usa /parar_seleccionar para finalizar la selección.")
    elif en_conversacion_goles:
        bot.send_message(cid, "Error. Ahora se están insertando goles, usa /parar_goles para finalizar la inserción.")
    elif len(vacio) == 0:
        cadena = consultas.clasificacion_puntos()
        bot.send_message(cid, cadena, parse_mode="Markdown")
    else:
        bot.send_message(cid, "Error. Este mensaje no necesita argumentos.")

@bot.message_handler(commands=['borrar'])
def command_borrar(m):
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    identificador = m.text[8:15]

    if en_conversacion_seleccion:
        bot.send_message(cid, "Error. Ahora se están seleccionando jugadores, usa /parar_seleccionar para finalizar la selección.")
    elif en_conversacion_goles:
        bot.send_message(cid, "Error. Ahora se están insertando goles, usa /parar_goles para finalizar la inserción.")
    elif len(identificador) == 0:
        bot.send_message(cid, "Error. El campo del identificador esta vacio.")
    elif not identificador.isnumeric():
        bot.send_message(cid, "Error. Tienes que usar un numero(identificador) para borrar al jugador.")
    else:
        modificaciones.borrar_jugador(identificador)
        bot.send_message(cid, "Usuario con identificador " + identificador + " borrado.")


@bot.message_handler(commands=['sortear'])
def command_sortear(m):
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    sorteo = m.text[9:15]
    lista = []
    lista1 = consultas.getEquipo1()
    lista2 = consultas.getEquipo2()
    if en_conversacion_seleccion:
        bot.send_message(cid, "Error. Ahora se están seleccionando jugadores, usa /parar_seleccionar para finalizar la selección.")
    elif en_conversacion_goles:
        bot.send_message(cid, "Error. Ahora se están insertando goles, usa /parar_goles para finalizar la inserción.")
    elif len(lista1) != 0 or len(lista2) != 0:
        bot.send_message(cid, "Error. Ya hay un equipo sorteado, para cancelar sorteo --> /cancelar_sorteo.")
    elif len(consultas.getListaCompleta()) == 0:
        bot.send_message(cid, "Error. No has seleccionado jugadores.")
    elif len(sorteo) == 0:
        lista = consultas.getListaCompleta()
        modificaciones.random_sorteo(lista)
        equipo1 = "Equipo 1: \n"
        equipo2 = "Equipo 2: \n"
        for i in range(0, (len(lista)/2)):
            consultas.aniadeEquipo1(lista[i])
            consultas.aniadeequipo1Goles(lista[i])
            equipo1 += lista[i]
            equipo1 += "\n"
        bot.send_message(cid, equipo1)
        for i in range((len(lista)/2), len(lista)):
            consultas.aniadeEquipo2(lista[i])
            consultas.aniadeequipo2Goles(lista[i])
            equipo2 += lista[i]
            equipo2 += "\n"
        bot.send_message(cid, equipo2)
    else:
        bot.send_message(cid, "Error. Este mensaje no necesita argumentos.")

@bot.message_handler(commands=['resultado'])
def command_resultado(m):
    global numero1
    global numero2
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    resultado = m.text[11:20]
    lista = []
    if en_conversacion_seleccion:
        bot.send_message(cid, "Error. Ahora se están seleccionando jugadores, usa /parar_seleccionar para finalizar la selección.")
    elif en_conversacion_goles:
        bot.send_message(cid, "Error. Ahora se están insertando goles, usa /parar_goles para finalizar la inserción.")
    elif len(resultado) < 3 or len(resultado) > 5:
        bot.send_message(cid, "Error. El resultado tiene que tener un tamaño de entre 3 y 5 caracteres.")
    elif "-" not in resultado:
        bot.send_message(cid, "Error. El resultado debe ser separado por '-'.")
    else:
        tupla = resultado.partition("-")
        if not tupla[0].isnumeric() or not tupla[2].isnumeric():
            bot.send_message(cid, "Error. A la derecha o a la izquierda de '-' no se ha ingresado un numero.")
        else:
            numero1 = int(float(tupla[0]))
            numero2 = int(float(tupla[2]))
            lista1 = consultas.getEquipo1()
            lista2 = consultas.getEquipo2()
            if len(lista1) == 0 or len(lista2) == 0:
                bot.send_message(cid, "Error. Se debe sortear un equipo antes de añadir los puntos.")
            elif numero1 < 0 or numero2 < 0:
                bot.send_message(cid, "Error. No se pueden añadir numeros negativos.")
            elif numero1 > numero2:
                puntos = 0
                for i in lista1:
                    #i --> nombre del jugador
                    puntos = consultas.puntos_jugador(i)
                    puntos += 3
                    modificaciones.actualizar_puntos(i, puntos)
                    puntos = 0
                consultas.borraEquipo1()
                puntos = 0
                for i in lista2:
                    #i --> nombre del jugador
                    puntos = consultas.puntos_jugador(i)
                    puntos += 1
                    modificaciones.actualizar_puntos(i, puntos)
                    puntos = 0
                consultas.borraEquipo2()
                bot.send_message(cid, "Resultado recibido, añadiendo puntos...\n" + "Pincha aquí para ver la /clasificacion")
            elif numero1 < numero2:
                puntos = 0
                for i in lista1:
                    #i --> nombre del jugador
                    puntos = consultas.puntos_jugador(i)
                    puntos += 1
                    modificaciones.actualizar_puntos(i, puntos)
                    puntos = 0
                consultas.borraEquipo1()
                puntos = 0
                for i in lista2:
                    #i --> nombre del jugador
                    puntos = consultas.puntos_jugador(i)
                    puntos += 3
                    modificaciones.actualizar_puntos(i, puntos)
                    puntos = 0
                consultas.borraEquipo2()
                bot.send_message(cid, "Resultado recibido, añadiendo puntos...\n" + "Pincha aquí para ver la /clasificacion")
            elif numero1 == numero2:
                puntos = 0
                for i in lista1:
                    #i --> nombre del jugador
                    puntos = consultas.puntos_jugador(i)
                    puntos += 2
                    modificaciones.actualizar_puntos(i, puntos)
                    puntos = 0
                consultas.borraEquipo1()
                puntos = 0
                for i in lista2:
                    #i --> nombre del jugador
                    puntos = consultas.puntos_jugador(i)
                    puntos += 2
                    modificaciones.actualizar_puntos(i, puntos)
                    puntos = 0
                consultas.borraEquipo2()
                bot.send_message(cid, "Resultado recibido, añadiendo puntos...\n" + "Pincha aquí para ver la /clasificacion")

@bot.message_handler(commands=['cancelar_sorteo'])
def command_cancelar_sorteo(m):
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    sorteo = m.text[16:20]

    lista1 = consultas.getEquipo1()
    lista2 = consultas.getEquipo2()
    if en_conversacion_seleccion:
        bot.send_message(cid, "Error. Ahora se están seleccionando jugadores, usa /parar_seleccionar para finalizar la selección.")
    elif en_conversacion_goles:
        bot.send_message(cid, "Error. Ahora se están insertando goles, usa /parar_goles para finalizar la inserción.")
    elif len(lista1) == 0 or len(lista2) == 0:
        bot.send_message(cid, "Error. No hay sorteo realizado, para realizar sorteo --> /sortear.")
    elif len(sorteo) == 0:
        consultas.borraEquipo1()
        consultas.borraEquipo2()
        bot.send_message(cid, "Sorteo borrado, para realizar un nuevo sorteo --> /sortear.")
    else:
        bot.send_message(cid, "Error. Este mensaje no necesita argumentos.")

bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.

bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.
