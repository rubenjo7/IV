# IV    [![Telegram.me](http://lelb.net/wp-content/uploads/2016/01/telegram-icon-e1453881760594.png)](https://telegram.me/p_deportivas_bot)
[![Build Status](https://travis-ci.org/rubenjo7/IV.svg?branch=master)](https://travis-ci.org/rubenjo7/IV)

Repositorio de la asignatura Infraestructura Virtual

<h3>Aplicación de "Peñas" deportivas:</h3>
####Versión 2.0

Se va a intentar desarrollar un bot para Telegram. Este bot sera para llevar las estadísticas de una peña deportiva. Se podrán añadir jugadores, tras estar dentro de la peña una serie de jugadores, se podrán sortear equipos seleccionándolos mediante un teclado y tras finalizar el partido se podrán añadir estadísticas del partido, como el resultado, o incluir la cantidad de goles que ha marcado cada jugador. Tras introducir el resultado se repartirán los puntos para cada jugador en función del resultado. También se podrán consultar clasificación por puntos o clasificación por goles.

###Tareas ya realizadas:

- Inserción de jugadores.
- Borrado de jugadores por ID.
- Mostrar jugadores ya insertados.
- Sortear equipos aleatorios con los jugadores insertados.
- Anular Sorteo.
- Insertar Resultado.
- Consultar la clasificación

###Tareas por realizar:

- Inserción de goleadores por partido.
- Creación de clasificación de goleadores.
- Modo selección de jugadores para sorteo.

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

En principio pongo los que creo que voy a utilizar, esta lista se ampliará si necesitase usar algo más.

###Funcionamiento actual:

Actualmente el bot integra 4 funciones, como ya he dicho anteriormente:

  * _/Insertar nombre_ : Inserta a un jugador en la base de datos. Por supuesto, se realiza una comprobación de errores para que no exista ya ese nombre o que se ponga un nombre, entre otros. Esta función solo podrá hacerla el administrador de la peña en una versión futura.
  * _/Borrar id_ : Borra a un jugador. Esta función solo podrá hacerla el administrador de la peña en una versión futura. También tiene su comprobación de errores.
  * _/Mostrar_ : Muestra id y nombre de los jugadores que hay en la base de datos actualmente. Esta función la podrá realizar cualquier usuario.
  * _/Sortear_ : Sortea dos equipos de manera aleatoria entre todos los jugadores insertados. Esta función solo puede hacerla el administrador de la peña.
  * _/Cancelar_sorteo_ : Cancela el sorteo, en caso de que no haya ninguno, da el aviso de que no existe ninguno.
  * _/Resultado_ : Se inserta un resultado en formato "X-X", siendo X un número, por supuesto, si no sigue ese formato manda un mensaje de error al usuario.
  * _/Clasificacion_ : Muestra la clasificación en función de los puntos que tiene cada jugador, en caso de empate van por orden de lista. En versiones futuras, se añadiran los goles a esta clasificación.

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

####Mejoras:

He ampliado mi proyecto, y como es lógico, he creado más funciones que ha que testear:

1. Test en ordenador personal:

<a href="http://es.tinypic.com?ref=x4jes4" target="_blank"><img src="http://i66.tinypic.com/x4jes4.png" border="0" alt="Image and video hosting by TinyPic"></a>

2. Como mejora, y para tener algo más de seguridad, he tenido que crearme varias variables de entorno, que las inserto del siguiente modo:

<a href="http://es.tinypic.com?ref=d7051" target="_blank"><img src="http://i64.tinypic.com/d7051.png" border="0" alt="Image and video hosting by TinyPic"></a>

3. Y como es lógico los test en [Travis](https://travis-ci.org/rubenjo7/IV/builds/174616898) vuelven a pasarse:

<a href="http://es.tinypic.com?ref=2z8x07t" target="_blank"><img src="http://i63.tinypic.com/2z8x07t.png" border="0" alt="Image and video hosting by TinyPic"></a>

<a href="http://es.tinypic.com?ref=2wdosq9" target="_blank"><img src="http://i64.tinypic.com/2wdosq9.png" border="0" alt="Image and video hosting by TinyPic"></a>

###Despliegue en Heroku:

Para este despliegue, me he tenido que dar de alta en la web, vincular mi cuenta de github a esta nueva y a partir de ahí crear una aplicación con una base de datos. La base de datos que he usado ha sido la propia de Heroku (PostgreSQL).

La base de datos que he creado a sido la siguiente, desde mi terminal:

<a href="http://es.tinypic.com?ref=110x94y" target="_blank"><img src="http://i63.tinypic.com/110x94y.png" border="0" alt="Image and video hosting by TinyPic"></a>

Ahora debo acceder a ella desde mi código, para ello uso:

    con = psycopg2.connect(database=database_db,user=usuario_db,password=password_db, host=host_db)


Como se ve, me he declarado variables locales para la base de datos, host, usuario y contraseña, luego en Heroku, tenemos que declararlas también (Aquí he difuminado los datos por temas de seguridad):

<a href="http://es.tinypic.com?ref=2rrwa34" target="_blank"><img src="http://i65.tinypic.com/2rrwa34.png" border="0" alt="Image and video hosting by TinyPic"></a>

Ahora nos vamos a Heroku y seleccionamos la casilla de despliegue automático, para que una vez se haga push en git, este actualice automáticamente. Además, seleccionamos la opción de esperar a que los test de integración continua estén pasados, lo cual es bastante conveniente tenerlo activo:

<a href="http://es.tinypic.com?ref=20qgpyf" target="_blank"><img src="http://i68.tinypic.com/20qgpyf.png" border="0" alt="Image and video hosting by TinyPic"></a>

Otra manera de hacerlo es de forma manual, porque a veces tarde más de lo esperado:

<a href="http://es.tinypic.com?ref=1zzo006" target="_blank"><img src="http://i63.tinypic.com/1zzo006.png" border="0" alt="Image and video hosting by TinyPic"></a>

Para el despliegue necesitamos un fichero Procfile:

    worker: python p_deportivas_bot.py

Como se trata de un bot de Telegram, necesitamos poner "worker" para que a los 60 segundos sin recibir peticiones no se descative.

Este fichero es el que Heroku ejecuta, por tanto, debemos decirle que ejecute el bot.

A parte, he creado un archivo llamado [runtime.txt](https://github.com/rubenjo7/IV/blob/master/runtime.txt) que contiene la versión de Python que estamos usando.

Una vez que se evaluen los test unitarios de nuestra aplicación en TravisCI en mi caso veremos como nuestra aplicación se despliega en Heroku:

<a href="http://es.tinypic.com?ref=21l0nrp" target="_blank"><img src="http://i66.tinypic.com/21l0nrp.png" border="0" alt="Image and video hosting by TinyPic"></a>

En este momento nuestro bot esta desplegado. Podemos ver los logs introduciendo en la carpeta donde se encuentre nuestro bot el comando:

    heroku logs --tail --ps postgres --app pdeportivasbot

y podemos ver como ejecuta los comandos que queramos sin nigún problema además de estar funcionando el bot:

<a href="http://es.tinypic.com?ref=263ftxk" target="_blank"><img src="http://i63.tinypic.com/263ftxk.png" border="0" alt="Image and video hosting by TinyPic"></a>

Con esto ya tendremos configurado nuestro despliegue atomático y podremos probarlo desde cualquier plataforma de telegram buscando el bot por el nombre de @p_deportivas_bot. Algunas pruebas son:

<a href="http://es.tinypic.com?ref=157ovfd" target="_blank"><img src="http://i68.tinypic.com/157ovfd.png" border="0" alt="Image and video hosting by TinyPic"></a>
