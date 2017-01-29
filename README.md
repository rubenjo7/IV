# IV    [![Telegram.me](http://lelb.net/wp-content/uploads/2016/01/telegram-icon-e1453881760594.png)](https://telegram.me/p_deportivas_bot)
[![Build Status](https://travis-ci.org/rubenjo7/IV.svg?branch=master)](https://travis-ci.org/rubenjo7/IV) [![Heroku Deploy](https://www.herokucdn.com/deploy/button.svg)](https://pdeportivasbot.herokuapp.com/) [![Docker](https://camo.githubusercontent.com/8a4737bc02fcfeb36a2d7cfb9d3e886e9baf37ad/687474703a2f2f693632382e70686f746f6275636b65742e636f6d2f616c62756d732f7575362f726f6d696c67696c646f2f646f636b657269636f6e5f7a7073776a3369667772772e706e67)](https://hub.docker.com/r/rubenjo7/iv/) [![Azure](http://azuredeploy.net/deploybutton.png)](http://pdeportivasbot.cloudapp.net/)

Repositorio de la asignatura Infraestructura Virtual

<h3>Aplicación de "Peñas" deportivas:</h3>
####Versión 1.3

Bot para Telegram. Este bot será para llevar las estadísticas de una peña deportiva. Se podrán añadir jugadores, tras estar dentro de la peña una serie de jugadores, se podrán sortear equipos seleccionándolos mediante una conversación y tras finalizar el partido se podrán añadir estadísticas del mismo, como el resultado, o incluir la cantidad de goles que ha marcado cada jugador. Tras introducir el resultado se repartirán los puntos para cada jugador en función del resultado. También se podrán consultar clasificación por puntos o clasificación por goles.
- [Aquí](https://github.com/rubenjo7/IV/blob/master/Documentacion/TAREAS.md#tareas-del-bot) se pueden consultar las tareas ya realizadas.
- [Aquí](https://github.com/rubenjo7/IV/blob/master/Documentacion/FUNCIONAMIENTO.md#funcionamiento-de-peñas-deportivas-) se pueden consultar las funciones de las que dispone el bot.

<h3>Realización:</h3>

Para la realización de la practica, en principio necesitare:

* Tener instalado los paquetes necesarios para que phyton funcione correctamente.
* Una base de datos para almacenar los datos necesarios, PostGreSQL.
* Uso de la API TELEBOT --> pyTelegramBotAPI versión 2.1.7
* pip versión 9.0.1
* pyOpenSSL versión 16.2.0
* Heroku.
* Monitorización.
* TravisCI para realizar test continuos.
* DockerHub, para permitir a los usuarios compartir las imágenes construidas.
* Azure, para desplegar el bot en un IaaS.

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
      cd p_deportivas_bot && python test_p_deportivas_bot.py

    ejecutar:
      cd p_deportivas_bot && python p_deportivas_bot.py

Tras esto, Travis comienza a instalar los paquetes necesarios y a ejecutar el test.

* [Aquí](https://github.com/rubenjo7/IV/blob/master/Documentacion/TRAVIS.md#tercera-versión-de-test-para-travis) se puede ver los resultados de los test en el ordenador personal y en TRAVIS-CI. Mostrando las diferentes etapas de los test.

* [Aquí](https://github.com/rubenjo7/IV/blob/master/Documentacion/TRAVIS.md#varibles-de-entorno-en-travis) se puede consultar como he tenido que crear varias variables de entorno en TRAVIS-CI.

Si nos vamos a [TRAVIS-CI](https://travis-ci.org/rubenjo7/IV) vemos que esta todo correcto porque esta de color verde.

###Despliegue en Heroku:

Para este despliegue, me he tenido que dar de alta en la web, vincular mi cuenta de github a esta nueva y a partir de ahí crear una aplicación con una base de datos. La base de datos que he usado ha sido la propia de Heroku (PostgreSQL).

* Consulta [Aquí](https://github.com/rubenjo7/IV/blob/master/Documentacion/HEROKU.md#creación-base-de-datos) como se creo la base de datos.


Ahora debo acceder a ella desde mi código, para ello uso:

    con = psycopg2.connect(database=database_db,user=usuario_db,password=password_db, host=host_db)

* Es necesario declarar variables de entorno en [Heroku](https://github.com/rubenjo7/IV/blob/master/Documentacion/HEROKU.md#variables-de-entorno-en-heroku)

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

###Entorno de pruebas

- Lo primero ha sido preparar la imagen con el bot y sus dependencias instaladas para que la ejecución de @p_deportivas_bot sea posible. Esto lo he realizado mediante un fichero [Dockerfile](https://github.com/rubenjo7/IV/blob/master/Dockerfile).

- El segundo paso ha sido, una vez creado dicho fichero, unir la cuenta de DockerHub con la de GitHub y la creación del contenedor, este proceso se puede ver [aquí](https://github.com/rubenjo7/IV/tree/Documentacion#entorno-de-pruebas).

- La página de DockerHub con mi imagen se encuentra [aquí](https://hub.docker.com/r/rubenjo7/iv/).

- La instalación del contenedor en nuestro ordenador personal la podemos ver [aquí](https://github.com/rubenjo7/IV/blob/master/Documentacion/DOCKER.md#instalación-del-contenerdor).

###Vagrant y Ansible:

Usaré Vagrant para crear una máquina Virtual y poder lanzarla en una Infraestructura, en mi caso, Azure. A continuación explicaré los pasos por encima, para verlos más detalladamente es recomendable visitar los enlaces disponibles.

1. Descargamos e instalamos Vagrant. En mi caso, la versión que he usado ha sido la 1.8.6, que se puede descargar de [aquí](https://releases.hashicorp.com/vagrant/1.8.6/vagrant_1.8.6_x86_64.deb).
2. Instalo el plugin de Azure para Vagrant:

        vagrant plugin install vagrant-azure

3. Realizamos una serie de [configuraciones de Azure](https://github.com/rubenjo7/IV/blob/master/Documentacion/AZURE.md).
4. Rellenamos el archivo [Vagrantfile](https://github.com/rubenjo7/IV/blob/master/Vagrant%20y%20Ansible/Vagrantfile), cuyo contenido se explica [aquí](https://github.com/rubenjo7/IV/blob/master/Documentacion/VAGRANT.md#vagrant).
5. El Vagrantfile llama al fichero de [Ansible](https://github.com/rubenjo7/IV/blob/master/Vagrant%20y%20Ansible/configuracion_ansible.yml), cuyo contenido se explica [aquí]().
6. Una vez que tenemos todo esto, podremos lanzar el despliegue de la máquina y su provisionamiento con:

        vagrant up --provider=azure

7. En caso de que solo queramos realizar el provisionamiento usaremos:

          vagrant provision

###Fabric:

Fabric es una biblioteca de Python y una herramienta de línea de comandos para agilizar el uso de SSH para el despliegue de aplicaciones o tareas de administración de sistemas.

Su uso es el siguiente:

    fab -p [CONTRASEÑA] -H [USUARIO]@[HOST] [ORDEN]

En el siguiente [enlace]() se pueden ver algunas pruebas realizadas.

El contenido del archivo [Fabric](https://github.com/rubenjo7/IV/blob/master/fabfile.py) se encuentra explicado [aquí]().

###Supervisor:

He tenido que instalar Supervisord para tener controlado el bot sin tener la necesidad  de mantener la terminal abierta en la ejecución del mismo.

El supervisor es instalado desde el fichero de ansible, donde también configuro el programa para supervisor, además de ejecutarlo.

El archivo para la [configuración del supervisor del bot](https://github.com/rubenjo7/IV/blob/master/p_deportivas_bot.conf) se encuentra explicado [aquí]().
