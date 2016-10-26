# -*- coding: utf-8 -*-
import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
import random
import datetime
import urllib3
import sqlite3 as lite

def consultar_jugadores_por_nombre():
    lista = []
    con = lite.connect('jugadores.db')
    cur = con.cursor()
    cur.execute("SELECT * from jugadores")
    for jugador in cur:
        lista.append(jugador[1])
    cur.close()
    con.close()
    return lista

def consultar_jugadores_por_id():
    lista = []
    con = lite.connect('jugadores.db')
    cur = con.cursor()
    cur.execute("SELECT * from jugadores")
    for jugador in cur:
        lista.append(jugador[0])
    cur.close()
    con.close()
    return lista

def consultar():
    con = lite.connect('jugadores.db')
    cur = con.cursor()
    cur.execute("SELECT * from jugadores")
    cadena = "----------------------\n"
    cadena += " ID |  NOMBRE  \n"
    cadena += "----------------------\n"
    for jugador in cur:
        if len(str(jugador[0])) == 1:
            cadena += str(jugador[0]) + "   | " + jugador[1] + "\n"
            cadena += "----------------------\n"
        elif len(str(jugador[0])) == 2:
            cadena += str(jugador[0]) + "  | " + jugador[1] + "\n"
            cadena += "----------------------\n"
        elif len(str(jugador[0])) == 3:
            cadena += str(jugador[0]) + " | " + jugador[1] + "\n"
            cadena += "----------------------\n"
        else:
            cadena += str(jugador[0]) + "| " + jugador[1] + "\n"
            cadena += "----------------------\n"
    cur.close()
    con.close()
    return cadena

def consulta_por_valor(jugador):
    contador = 0
    con = lite.connect('jugadores.db')
    cur = con.cursor()
    par = (jugador, )
    cur.execute("SELECT * from jugadores where nombre=?", par)
    for i in cur:
        contador += 1
    cur.close()
    con.close()
    return contador

def consulta_para_test(jugador):
    lista = []
    con = lite.connect('jugadores.db')
    cur = con.cursor()
    par = (jugador, )
    cur.execute("SELECT * from jugadores where nombre=?", par)
    for i in cur:
        lista += i
    cur.close()
    con.close()
    return lista
