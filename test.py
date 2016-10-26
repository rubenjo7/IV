import unittest
from requests import HTTPError
import time
import consultas
import modificaciones
import telebot
from telebot import types

class p_deportivas(unittest.TestCase):

	#TESTEAR FUNCIONES PROPIAS
	def testing_por_nombre(self):
		lista = consultas.consultar_jugadores_por_nombre()
		for i in range (0, len(lista)):
			if lista[i] == "Ruben":
				self.assertEqual("Ruben", lista[i])

	def testing_por_id(self):
		lista = consultas.consultar_jugadores_por_id()
		for i in range (0, len(lista)):
			if lista[i] == 1:
				self.assertEqual(1, lista[i])

	def testting_consultas(self):
		lista = consultas.consultar()
		if lista[0] == 1 and lista[1] =="Ruben":
			self.assertEqual(1, lista[0])

	def testting_consultas_por_nombre(self):
		numero = consultas.consulta_por_valor("Ruben")
		self.assertEqual(1, numero)

	def testing_rand(self):
		lista = ["yo", "tu", "el"]
		modificaciones.random_sorteo(lista)
		for i in range (0, len(lista)):
			if lista[i] == "yo":
				self.assertEqual("yo", lista[i])

	#TESTEAR TELEBOT
	def test_json_message(self):
	    jsonstring = r'{"message_id":1,"from":{"id":108929734,"first_name":"Ruben","last_name":"Jimenez","username":"rubenjo7"},"chat":{"id":1734,"first_name":"R","type":"private","last_name":"Ji","username":"oir"},"date":1435296025,"text":"HOLA"}'
	    msg = types.Message.de_json(jsonstring)
	    assert msg.text == 'HOLA'

	#PENDIENTE TESTEAR INSERTADO Y BORRADO DE JUGADORES
	"""def testing_insertado(self):
		modificaciones.insertar_jugador("yo")
		lista = consultas.consultar_jugadores_por_nombre()
		for i in range (0, len(lista)):
			if lista[i] == "yo":
				self.assertEqual("yo", lista[i])

	def testing_borrado(self):
		lista = consultas.consulta_para_test("yo")
		modificaciones.borrar_jugador(lista[0])
		self.assertRaises("yo", lista[1])"""


if __name__ == '__main__':
    unittest.main()
