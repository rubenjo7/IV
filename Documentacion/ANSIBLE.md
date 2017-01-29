#ANSIBLE:

Ansible es una herramienta que nos permite gestionar configuraciones, aprovisionamiento de recursos, despliegue automático de aplicaciones y muchas otras tareas de TI de una forma limpia y sencilla.

La instalación de ansible es bastante sencilla:

    sudo apt-get install ansible

###Contenido ficher [configuracion_ansible.yml](https://github.com/rubenjo7/IV/blob/master/Vagrant%20y%20Ansible/configuracion_ansible.yml):

Con "vars" añadimos las variables de entorno que necesitamos para el bot.

Tras esto, lo primero que hacemos es actualizar el sistema.

Luego instalamos git y nos descargamos el repositorio de la aplicación.

Otro paso importante es la instalación tanto de pip como del supervisor.

El siguiente paso es copiar la información de nuestro fichero de configuración para el supervisor.

Luego instalo los paquetes que necesita mi bot para su posible ejecución. La mayoría relacionados con python.

Tras esto, se actualiza pip para prevenir problemas a la hora de instalar los requirements, que es el siguiente paso.

Para terminar el contenido de este fichero, he creado un directorio que contiene un fichero logs.txt, el cual almacenará la información que el bot reciba, la conversación y la hora de la misma, para que en caso de caída, podamos saber la causa con mayor facilidad.

Por último, ejecutamos el supervisor.
