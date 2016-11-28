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


def insertar_jugador(jugador):
    con = psycopg2.connect(database=database_db,user=usuario_db,password=password_db, host=host_db)
    cur = con.cursor()
    cur.execute("Insert into jugadores(jugador, puntos, goles) values (%s, %s, %s)", (jugador, 0, 0))
    con.commit()
    cur.close()
    con.close()

def borrar_jugador(identificador):
    con = psycopg2.connect(database=database_db,user=usuario_db,password=password_db, host=host_db)
    cur = con.cursor()
    valores_borrar = (identificador, )
    cur.execute('Delete from jugadores where id=%s', valores_borrar)
    con.commit()
    cur.close()
    con.close()

def actualizar_puntos(nombre, puntos):
    con = psycopg2.connect(database=database_db,user=usuario_db,password=password_db, host=host_db)
    cur = con.cursor()
    cur.execute('Update jugadores set puntos=%s where jugador=%s', (puntos, nombre))
    con.commit()
    cur.close()
    con.close()

def actualizar_goles(nombre, goles):
    con = psycopg2.connect(database=database_db,user=usuario_db,password=password_db, host=host_db)
    cur = con.cursor()
    cur.execute('Update jugadores set goles=%s where jugador=%s', (goles, nombre))
    con.commit()
    cur.close()
    con.close()

def random_sorteo(lista):
    random.shuffle(lista)
