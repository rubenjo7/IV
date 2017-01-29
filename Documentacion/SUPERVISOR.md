#SUPERVISOR:

Como dijimos anteriormente, el supervisor ha sido instalado en el paso de ansible.

###Contenido del fichero [p_deportivas_bot.conf](https://github.com/rubenjo7/IV/blob/master/p_deportivas_bot.conf):

- autostart: El servicio ha de iniciarse automaticamente cuando lanzamos supervisord, en nuestro caso no.
- command: Se refiere al ejecutable, podemos referenciarlo directamente con la ruta absoluta, o bien, si esta en el path, invocarlo sin más.

- user: El usuario con el que el proceso se lanza.

- directory: Especifica desde que directorio se hace la ejecución del comando.

- environment: Valores en la forma VARIABLE=VALOR que se incluiran en el entorno de ejecución del servicio.

- redirect_stderr: Redirigir la salida de los errores al log propio de supervisord en vez de al individual del servicio.

- \*log: opciones de log para su rotado, conservación y clasificación, se autoexplican.

###Pasos para su funcionamiento:

1. Recargar el supervisor.
2. Iniciarlo.
3. Parar si es necesario.
4. Entre paso y paso es recomendable ver el estado en el que se encuentra el supervisor.
5. En caso de error, Recargar. 
