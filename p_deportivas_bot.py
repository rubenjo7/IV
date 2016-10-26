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

TOKEN = os.environ['token_bot'] #Nuestro tokken del bot (el que @BotFather nos dió).

bot = telebot.TeleBot(TOKEN) # Creamos el objeto de nuestro bot.

def listener(messages): # Con esto, estamos definiendo una función llamada 'listener', que recibe como parámetro un dato llamado 'messages'.
    for m in messages: # Por cada dato 'm' en el dato 'messages'
        if m.content_type == 'text': # Filtramos mensajes que sean tipo texto.
            cid = m.chat.id # Almacenaremos el ID de la conversación.
            print "[" + str(cid) + "]: " + m.text # Y haremos que imprima algo parecido a esto -> [52033876]: /start


@bot.message_handler(commands=['Insertar'])
def command_insertar(m):
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    jugador = m.text[10:20]

    if len(jugador) == 0:
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

    if len(vacio) == 0:
        cadena = consultas.consultar()
        bot.send_message(cid, cadena)
    else:
        bot.send_message(cid, "Error. Este mensaje no necesita argumentos.")



@bot.message_handler(commands=['Borrar'])
def command_borrar(m):
    cid = m.chat.id # Guardamos el ID de la conversación para poder responder.
    identificador = m.text[8:15]

    if len(identificador) == 0:
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

    if len(sorteo) == 0:
        lista = consultas.consultar_jugadores_por_nombre()
        modificaciones.random_sorteo(lista)
        equipo1 = "Equipo 1: \n"
        equipo2 = "Equipo 2: \n"
        for i in range(0, (len(lista)/2)):
            equipo1 += lista[i]
            equipo1 += "\n"
        bot.send_message(cid, equipo1)
        for i in range((len(lista)/2), len(lista)):
            equipo2 += lista[i]
            equipo2 += "\n"
        bot.send_message(cid, equipo2)

    else:
        bot.send_message(cid, "Error. Este mensaje no necesita argumentos.")

bot.set_update_listener(listener) # Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener' declarada arriba.

bot.polling(none_stop=True) # Con esto, le decimos al bot que siga funcionando incluso si encuentra algún fallo.
