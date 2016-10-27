# IV    
[![Build Status](https://travis-ci.org/rubenjo7/IV.svg?branch=master)](https://travis-ci.org/rubenjo7/IV)

Repositorio de la asignatura Infraestructura Virtual

<h3>Aplicacion de "Peñas" deportivas:</h3>
####Versión 1.0

Se va a intentar desarrollar un bot para Telegram. Este bot sera para llevar las estadísticas de una peña deportiva. Se podrán añadir jugadores, tras estar dentro de la peña una serie de jugadores, se podrán sortear equipos seleccionándolos mediante un teclado y tras finalizar el partido se podrán añadir estadísticas del partido, como el resultado, o incluir la cantidad de goles que ha marcado cada jugador. Tras introducir el resultado se repartirán los puntos para cada jugador en función del resultado. También se podrán consultar clasificación por puntos o clasificación por goles.

###Tareas ya realizadas:

- Inserción de jugadores.
- Borrado de jugadores por ID.
- Mostrar jugadores ya insertados.
- Sortear equipos aleatorios con los jugadores insertados.

###Tareas por realizar:

- Inserción de resultado y goleadores por partido.
- Creación de clasificación de puntos y goleadores.
- Modo selección de jugadores para sorteo.

<h3>Realizacóon:</h3>

Para la realizacion de la practica, en principio necesitare:

* Tener instalado los paquetes necesarios para que phyton funcione correctamente.
* Una base de datos para almacenar los datos necesarios(sqlite).
* Uso de la API TELEBOT --> pyTelegramBotAPI versión 2.1.7
* pip versión 8.1.2
* pyOpenSSL versión 16.2.0
* Desplegar bot en la nube -->  [arubacloud](https://www.arubacloud.es/vps/tipos-virtual-private-server.aspx)
* Monitorización.
* TravisCI para realizar test continuos.

En principio pongo los que creo que voy a utilizar, esta lista se ampliará si necesitase usar algo más.

###Funcionamiento actual:

Actualmente el bot integra 4 funciones, como ya he dicho anteriormente:

  * _/Insertar nombre_ : Inserta a un jugador en la base de datos. Por supuesto, se realiza una comprobación de errores para que no exista ya ese nombre o que se ponga un nombre, entre otros.sta función solo podrá hacerla el administrador de la peña en una versión futura.
  * _/Borrar id_ : Borra a un jugador. Esta función solo podrá hacerla el administrador de la peña en una versión futura. También tiene su comprobación de errores.
  * _/Mostrar_ : Muestra id y nombre de los jugadores que hay en la base de datos actualmente. Esta función la podrá realizar cualquier usuario.
  * _/Sortear_ : Sortea dos equipos de manera aleatoria entre todos los jugadores insertados. Esta función solo puede hacerla el administrador de la peña.

###Integración continua:

Para la integración continua se ha usado Travis-CI para realizar los tests. Para llevarlo a cabo se ha necesitado crear un fichero .travis.yml, el cual tiene el siguiente contenido:

    language: python
    python:
      - "2.7"
    # command to install dependencies
    install: make install
    # command to run tests
    script: make test

El makefile que he creado para hacer las instalaciones automáticamente y los test es:

    install:
    	pip install -r requirements.txt

    test:
    	python test.py

    ejecutar:
    	python p_deportivas_bot.py

Tras esto, Travis comienza a instalar los paquetes necesiarios y a ejecutar el test, que anteriormente probé con el siguiente resultado:

<img src="http://i66.tinypic.com/f9iop0.png" border="0" alt="Image and video hosting by TinyPic">

Si nos vamos a [TRAVIS-CI](https://travis-ci.org/rubenjo7/IV) vemos que esta todo correcto porque esta de color verde:

<img src="http://i65.tinypic.com/2r2btk3.png" border="0" alt="Image and video hosting by TinyPic">
