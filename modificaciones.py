# -*- coding: utf-8 -*-
import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
import random
import datetime
import urllib3
import sqlite3 as lite

def insertar_jugador(jugador):
    con = lite.connect('jugadores.db')
    cur = con.cursor()
    cur.execute("Insert into jugadores values (?, ?)", (None, jugador))
    con.commit()
    cur.close()
    con.close()

def borrar_jugador(identificador):
    con = lite.connect('jugadores.db')
    cur = con.cursor()
    valores_borrar = (identificador, )
    cur.execute('Delete from jugadores where id=?', valores_borrar)
    con.commit()
    cur.close()
    con.close()

def random_sorteo(lista):
    random.shuffle(lista)
