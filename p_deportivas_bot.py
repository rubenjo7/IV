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

def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    global en_conversacion_seleccion
    global contador_jugadores
    global esta_seleccionando
    global en_conversacion_goles
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        if m.content_type == 'text': # Filtramos mensajes que sean tipo texto.
            cid = m.chat.id # Almacenaremos el ID de la conversación.
            mensajes = m.text
            if mensajes == '/Seleccionar' and esta_seleccionando == 0:
                en_conversacion_seleccion = True
                bot.send_message(cid, "Vamos a seleccionar jugadores, recuerda que deben estar añadidos.")
                esta_seleccionando = 1
                contador_jugadores = 0
                consultas.borraListaCompleta()
            elif esta_seleccionando == 1 and mensajes == '/Seleccionar':
                bot.send_message(cid, "Error. Ya estas usando esta opción.")
            elif esta_seleccionando == 0 and mensajes == '/Parar_seleccionar':
                bot.send_message(cid, "Error. Tienes que estar seleccionando para poder cancelar la selección.")
            elif contador_jugadores < 2 and mensajes == '/Parar_seleccionar':
                bot.send_message(cid, "Error. Tienes que añadir al menos dos jugadores para poder parar la selección.")
            elif mensajes == '/Parar_seleccionar' and contador_jugadores >= 2:
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
            elif mensajes == '/Goles' and not esta_seleccionando == 1:#len(mensajes.split())
                en_conversacion_goles = True
                bot.send_message(cid, "Vamos a insertar goleadores, recuerda que deben estar añadidos a algun equipo.")
                inserta_goles = 1

            #archivo = open("sucesos.log", "r+")
            #contenido = archivo.read()
            #final_de_archivo = archivo.tell()
            #archivo.write("Fecha y hora: " + time.strftime("%c") + "\n")
            #archivo.write("[" + str(cid) + "]: " + m.text + "\n")
            #archivo.seek(final_de_archivo)
            print "Fecha y hora: " + time.strftime("%c")
            print "[" + str(cid) + "]: " + m.text # Y haremos que imprima algo parecido a esto -> [52033876]: /start


@bot.message_handler(commands=['Insertar'])
def command_insertar(m):
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    jugador = m.text[10:20]

    if en_conversacion_seleccion:
        bot.send_message(cid, "Error. Ahora se están insertando jugadores.")
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



@bot.message_handler(commands=['Mostrar'])
def command_mostrar(m):
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    vacio = m.text[8:20]
    cadena = ""

    if en_conversacion_seleccion:
        bot.send_message(cid, "Error. Ahora se están insertando jugadores.")
    elif len(vacio) == 0:
        cadena = consultas.consultar()
        bot.send_message(cid, cadena)
    else:
        bot.send_message(cid, "Error. Este mensaje no necesita argumentos.")

@bot.message_handler(commands=['Clasificacion'])
def command_clasificacion(m):
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    vacio = m.text[14:20]
    cadena = ""

    if en_conversacion_seleccion:
        bot.send_message(cid, "Error. Ahora se están insertando jugadores.")
    elif len(vacio) == 0:
        cadena = consultas.clasificacion()
        bot.send_message(cid, cadena)
    else:
        bot.send_message(cid, "Error. Este mensaje no necesita argumentos.")


@bot.message_handler(commands=['Borrar'])
def command_borrar(m):
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    identificador = m.text[8:15]

    if en_conversacion_seleccion:
        bot.send_message(cid, "Error. Ahora se están insertando jugadores.")
    elif len(identificador) == 0:
        bot.send_message(cid, "Error. El campo del identificador esta vacio.")
    elif not identificador.isnumeric():
        bot.send_message(cid, "Error. Tienes que usar un numero(identificador) para borrar al jugador.")
    else:
        modificaciones.borrar_jugador(identificador)
        bot.send_message(cid, "Usuario con identificador " + identificador + " borrado.")


@bot.message_handler(commands=['Sortear'])
def command_sortear(m):
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    sorteo = m.text[9:15]
    lista = []
    lista1 = consultas.getEquipo1()
    lista2 = consultas.getEquipo2()
    if en_conversacion_seleccion:
        bot.send_message(cid, "Error. Ahora se están insertando jugadores.")
    elif len(lista1) != 0 or len(lista2) != 0:
        bot.send_message(cid, "Error. Ya hay un equipo sorteado, para cancelar sorteo --> /Cancelar_sorteo.")
    elif len(consultas.getListaCompleta()) == 0:
        bot.send_message(cid, "Error. No has seleccionado jugadores.")
    elif len(sorteo) == 0:
        lista = consultas.getListaCompleta()
        modificaciones.random_sorteo(lista)
        equipo1 = "Equipo 1: \n"
        equipo2 = "Equipo 2: \n"
        for i in range(0, (len(lista)/2)):
            consultas.aniadeEquipo1(lista[i])
            equipo1 += lista[i]
            equipo1 += "\n"
        bot.send_message(cid, equipo1)
        for i in range((len(lista)/2), len(lista)):
            consultas.aniadeEquipo2(lista[i])
            equipo2 += lista[i]
            equipo2 += "\n"
        bot.send_message(cid, equipo2)
        #consultas.borraListaCompleta()
        print consultas.getListaCompleta()
    else:
        bot.send_message(cid, "Error. Este mensaje no necesita argumentos.")

@bot.message_handler(commands=['Resultado'])
def command_resultado(m):
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    resultado = m.text[11:20]
    lista = []
    if en_conversacion_seleccion:
        bot.send_message(cid, "Error. Ahora se están insertando jugadores.")
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
                bot.send_message(cid, "Resultado recibido, añadiendo puntos...\n" + "Pincha aquí para ver la /Clasificacion")
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
                bot.send_message(cid, "Resultado recibido, añadiendo puntos...\n" + "Pincha aquí para ver la /Clasificacion")
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
                bot.send_message(cid, "Resultado recibido, añadiendo puntos...\n" + "Pincha aquí para ver la /Clasificacion")

@bot.message_handler(commands=['Cancelar_sorteo'])
def command_cancelar_sorteo(m):
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    sorteo = m.text[16:20]

    lista1 = consultas.getEquipo1()
    lista2 = consultas.getEquipo2()
    if en_conversacion_seleccion:
        bot.send_message(cid, "Error. Ahora se están insertando jugadores.")
    elif len(lista1) == 0 or len(lista2) == 0:
        bot.send_message(cid, "Error. No hay sorteo realizado, para realizar sorteo --> /Sortear.")
    elif len(sorteo) == 0:
        consultas.borraEquipo1()
        consultas.borraEquipo2()
        bot.send_message(cid, "Sorteo borrado, para realizar un nuevo sorteo --> /Sortear.")
    else:
        bot.send_message(cid, "Error. Este mensaje no necesita argumentos.")

bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.

bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.
