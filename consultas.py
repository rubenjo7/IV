# -*- coding: utf-8 -*-
import telebot # Librería de la API del bot.
from telebot import types # Tipos para la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
import random
import datetime
import urllib3
import sqlite3 as lite
import psycopg2
import os

usuario_db = os.environ['usuario_db']
password_db = os.environ['password_db']
database_db = os.environ['database_db']
host_db = os.environ['host_db']

lista_completa = []
equipo1 = []
equipo2 = []

def aniadeListaCompleta(jugador):
    lista_completa.append(jugador)

def aniadeEquipo1(jugador):
    equipo1.append(jugador)

def aniadeEquipo2(jugador):
    equipo2.append(jugador)

def borraListaCompleta():
    del lista_completa[:]

def borraEquipo1():
    del equipo1[:]

def borraEquipo2():
    del equipo2[:]

def getListaCompleta():
    return lista_completa

def getEquipo1():
    return equipo1

def getEquipo2():
    return equipo2

def puntos_jugador(jugador):
    con = psycopg2.connect(database=database_db,user=usuario_db,password=password_db, host=host_db)
    cur = con.cursor()
    par = (jugador, )
    cur.execute("SELECT puntos from jugadores where jugador=%s", par)
    for i in cur:
        puntos = i[0]
    cur.close()
    con.close()
    return puntos

def consultar_jugadores_por_nombre():
    lista = []
    con = psycopg2.connect(database=database_db,user=usuario_db,password=password_db, host=host_db)
    cur = con.cursor()
    cur.execute("SELECT * from jugadores")
    for jugador in cur:
        lista.append(jugador[1])
    cur.close()
    con.close()
    return lista

def consultar_jugadores_por_id():
    lista = []
    con = psycopg2.connect(database=database_db,user=usuario_db,password=password_db, host=host_db)
    cur = con.cursor()
    cur.execute("SELECT * from jugadores")
    for jugador in cur:
        lista.append(jugador[0])
    cur.close()
    con.close()
    return lista

def consultar():
    con = psycopg2.connect(database=database_db,user=usuario_db,password=password_db, host=host_db)
    cur = con.cursor()
    cur.execute("SELECT * from jugadores ORDER BY id ASC")
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

def clasificacion():
    con = psycopg2.connect(database=database_db,user=usuario_db,password=password_db, host=host_db)
    cur = con.cursor()
    cur.execute("SELECT * from jugadores ORDER BY puntos DESC, jugador ASC")
    cadena = "------------------------------\n"
    cadena += "NOMBRE | PUNTOS \n"
    cadena += "------------------------------\n"
    for jugador in cur:
        cadena += jugador[1] + " | " + str(jugador[2]) + "\n"
        cadena += "------------------------------\n"

    cur.close()
    con.close()
    return cadena

def consulta_por_valor(jugador):
    contador = 0
    con = psycopg2.connect(database=database_db,user=usuario_db,password=password_db, host=host_db)
    cur = con.cursor()
    par = (jugador, )
    cur.execute("SELECT * from jugadores where jugador=%s", par)
    for i in cur:
        contador += 1
    cur.close()
    con.close()
    return contador
