#FABRIC:

La instalación de fabric es bien sencilla:

    sudo apt-get install fabric

###Contenido del fichero [fabfile.py](https://github.com/rubenjo7/IV/blob/master/fabfile.py):

En este fichero se incluyen las siguientes órenes:

* info_servidor --> Comprueba el nombre de la máquina remota.

* descargar --> Elimina el directorio IV descargado con anterioridad lo descarga de nuevo.

* actualizar --> Actualiza el estado del proyecto.

* borrar --> Borra el directorio del proyecto.

* testear --> Lanza los tests del proyecto, a lo que hay que insertar variables de entorno para que esto sea posible.

* instalar --> Ejecuta el instalador del proyecto.

* consultar_contenido --> Muestra el contenido del directorio del proyecto.

* iniciar --> Inicia el supervisor, que lanza el bot, también son necesarias pasarle las variables de entorno.

* stop --> Detiene el supervisor.

* status --> Muestra el estado del supervisor p_deportivas_bot.

* recargar --> Recarga el supervisor.

* logs --> Muestra el contenido del fichero en el que se almacenan los logs del bot.

###Pruebas:

La primera prueba muestra la salida de los comandos info_servidor y consultar_contenido:

<img src="http://i66.tinypic.com/9iwjo2.png" border="0" alt="Image and video hosting by TinyPic"></a>

Esta, recarga el supervisor, comprueba su estado, lo inicia y vuelve a mostrar el estado:

<img src="http://i63.tinypic.com/2a9b0r7.png" border="0" alt="Image and video hosting by TinyPic"></a>

Vemos que efectivamente el bot funciona:

<img src="http://i67.tinypic.com/s6t7wy.png" border="0" alt="Image and video hosting by TinyPic"></a>

Mostramos los logs:

<img src="http://i67.tinypic.com/2w4k3uq.png" border="0" alt="Image and video hosting by TinyPic"></a>

Ahora pararemos el supervisor y veremos su estado y comprobaremos que efectivamente ya no contesta, al estar parado:

<img src="http://i63.tinypic.com/nqra5i.png" border="0" alt="Image and video hosting by TinyPic"></a>

<img src="http://i66.tinypic.com/2jb5yq8.png" border="0" alt="Image and video hosting by TinyPic"></a>
