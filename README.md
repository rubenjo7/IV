# IV    [![Telegram.me](http://lelb.net/wp-content/uploads/2016/01/telegram-icon-e1453881760594.png)](https://telegram.me/p_deportivas_bot)
[![Build Status](https://travis-ci.org/rubenjo7/IV.svg?branch=master)](https://travis-ci.org/rubenjo7/IV) [![Heroku Deploy](https://www.herokucdn.com/deploy/button.svg)](https://pdeportivasbot.herokuapp.com/) [<img src="http://i628.photobucket.com/albums/uu6/romilgildo/dockericon_zpswj3ifwrw.png" alt="Docker" height=32>](https://hub.docker.com/r/rubenjo7/iv/)

Repositorio de la asignatura Infraestructura Virtual

<h3>Aplicación de "Peñas" deportivas:</h3>
####Versión 1.3

Bot para Telegram. Este bot será para llevar las estadísticas de una peña deportiva. Se podrán añadir jugadores, tras estar dentro de la peña una serie de jugadores, se podrán sortear equipos seleccionándolos mediante una conversación y tras finalizar el partido se podrán añadir estadísticas del mismo, como el resultado, o incluir la cantidad de goles que ha marcado cada jugador. Tras introducir el resultado se repartirán los puntos para cada jugador en función del resultado. También se podrán consultar clasificación por puntos o clasificación por goles.
- [Aquí](https://github.com/rubenjo7/IV/blob/master/TAREAS.md) se pueden consultar las tareas ya realizadas.
- [Aquí](https://github.com/rubenjo7/IV/blob/master/FUNCIONAMIENTO.md) se pueden consultar las funciones de las que dispone el bot.

<h3>Realización:</h3>

Para la realización de la practica, en principio necesitare:

* Tener instalado los paquetes necesarios para que phyton funcione correctamente.
* Una base de datos para almacenar los datos necesarios, como en esta practica usaré heroku, para desplegar mi base de datos he usado la que por defecto viene en heroku, PostGreSQL.
* Uso de la API TELEBOT --> pyTelegramBotAPI versión 2.1.7
* pip versión 8.1.2
* pyOpenSSL versión 16.2.0
* Desplegar bot en la nube -->  [arubacloud](https://www.arubacloud.es/vps/tipos-virtual-private-server.aspx).
* Heroku.
* Monitorización.
* TravisCI para realizar test continuos.
* DockerHub, para permitir a los usuarios compartir las imágenes construidas.

En principio pongo los que creo que voy a utilizar, esta lista se ampliará si necesitase usar algo más.


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

Tras esto, Travis comienza a instalar los paquetes necesarios y a ejecutar el test.

* [Aquí](https://github.com/rubenjo7/IV/blob/master/TRAVIS.md) se puede ver los resultados de los test en el ordenador personal y en TRAVIS-CI. Mostrando las diferentes etapas de los test.

* [Aquí](https://github.com/rubenjo7/IV/blob/master/TRAVIS.md) se puede consultar como he tenido que crear varias variables de entorno en TRAVIS-CI.

Si nos vamos a [TRAVIS-CI](https://travis-ci.org/rubenjo7/IV) vemos que esta todo correcto porque esta de color verde.

###Despliegue en Heroku:

Para este despliegue, me he tenido que dar de alta en la web, vincular mi cuenta de github a esta nueva y a partir de ahí crear una aplicación con una base de datos. La base de datos que he usado ha sido la propia de Heroku (PostgreSQL).

* Consulta [Aquí](https://github.com/rubenjo7/IV/blob/master/HEROKU.md) como se creo la base de datos.


Ahora debo acceder a ella desde mi código, para ello uso:

    con = psycopg2.connect(database=database_db,user=usuario_db,password=password_db, host=host_db)

* Es necesario declarar variables de entorno en [Heroku](https://github.com/rubenjo7/IV/blob/master/HEROKU.md)

Ahora nos vamos a Heroku y seleccionamos la casilla de despliegue automático, para que una vez se haga push en git, este actualice automáticamente. Además, seleccionamos la opción de esperar a que los test de integración continua estén pasados, lo cual es bastante conveniente tenerlo activo:

<img src="http://i68.tinypic.com/20qgpyf.png" border="0" alt="Image and video hosting by TinyPic"></a>

Otra manera de hacerlo es de forma manual, porque a veces tarde más de lo esperado:

<img src="http://i63.tinypic.com/1zzo006.png" border="0" alt="Image and video hosting by TinyPic"></a>

Para el despliegue necesitamos un fichero Procfile, cuyo contenido es el siguiente:

    worker: python p_deportivas_bot.py

Como se trata de un bot de Telegram, necesitamos poner "worker" para que a los 60 segundos sin recibir peticiones no se desactive.

Este fichero es el que Heroku ejecuta, por tanto, debemos decirle que ejecute el bot.

A parte, he creado un archivo llamado [runtime.txt](https://github.com/rubenjo7/IV/blob/master/runtime.txt) que contiene la versión de Python que estamos usando.

Una vez que se evaluen los test unitarios de nuestra aplicación en TravisCI en mi caso veremos como nuestra aplicación se despliega en Heroku:

<img src="http://i66.tinypic.com/21l0nrp.png" border="0" alt="Image and video hosting by TinyPic"></a>

En este momento nuestro bot esta desplegado. Podemos ver los logs introduciendo en la carpeta donde se encuentre nuestro bot el comando:

    heroku logs --tail --ps postgres --app pdeportivasbot

y podemos ver como ejecuta los comandos que queramos sin nigún problema además de estar funcionando el bot:

<img src="http://i63.tinypic.com/263ftxk.png" border="0" alt="Image and video hosting by TinyPic"></a>


Con esto ya tendremos configurado nuestro despliegue atomático y podremos probarlo desde cualquier plataforma de telegram buscando el bot por el nombre de @p_deportivas_bot.

###
