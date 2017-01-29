#VAGRANT:

Una vez que hemos realizado toda la configuración de [Azure](https://github.com/rubenjo7/IV/blob/master/Documentacion/AZURE.md), ya podemos empezar a crear el archivo de configuración Vagrantfile:

    vagrant init

Una vez hacemos este paso nos aparece un archivo Vagrantfile, que tendremos que editar dejandolo con el siguiente [aspecto](https://github.com/rubenjo7/IV/blob/master/Vagrant%20y%20Ansible/Vagrantfile), que explicaremos justo ahora.

###Contenido archivo Vagrantfile:

* config.vm.box = "azure" --> Esto configura qué caja se encargará la máquina.

* config.vm.network "public_network" --> Configura la red en la máquina, en este caso una conexión pública.

* azure.mgmt_certificate = File.expand_path("azure.pem")
		azure.mgmt_endpoint    = "https://management.core.windows.net" --> Ubicación del portal de administración de la máquina.

* azure.subscription_id = ENV['id_azure'] --> Id de la suscripción de Azure. Por supuesto tiene que oculta con variables de entorno.

* azure.vm_name     = "pdeportivasbot" --> Nombre de la máquina virtual.

* azure.cloud_service_name = 'pdeportivasbot' --> Nombre del servicio en la nube.

* azure.vm_image    = "b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04_2-LTS-amd64-server-20150506-en-us-30GB" --> Imagen del sistema operativo que instalamos.

* azure.vm_size     = "Small" --> Tamaño de la máquina virtual.

* config.vm.box_url = "https://github.com/msopentech/vagrant-azure/raw/master/dummy.box" --> Configuración de la caja utilizada.

* azure.vm_user = "ruben" # defaults to 'vagrant' if not provided --> Nombre de usuario de la máquina.

* azure.vm_password = ENV['clave'] --> Clave de acceso para el usuario de la máquina, protegida mediante variables de entorno.

azure.vm_location = "Central US" # e.g., West US --> Ubicación de la máquina virtual.

* config.ssh.username = ENV['usuario_ssh'] --> Usuario para la conexión por ssh, protegido por viables de entorno, más adelante se mostraran usos de los mismos.

* config.ssh.password = ENV['clave'] --> Clave para la conexión por ssh, protegida por viables de entorno, más adelante se mostraran usos de los mismos.

Ahora la configuración de ansible:

* ansible.sudo = true --> Los comandos ejecutados por ansible serán con privilegios de administrador.

* ansible.raw_arguments=["-vvvv"] --> Para que ansible imprima todo lo que ocurre.

* ansible.playbook = "configuracion_ansible.yml" --> Ubicación del archivo de ansible.

###Despliegue, provisionamiento y apagado.

Una vez tenemos configurado todo de manera correcta pasamos a lanzar el despliegue de la máquina y su provisionamiento:

<img src="http://i66.tinypic.com/2s1sk1g.png" border="0" alt="Image and video hosting by TinyPic"></a>

<img src="http://i64.tinypic.com/169q2jk.png" border="0" alt="Image and video hosting by TinyPic"></a>

Si solo queremos realizar el provisionamiento usaremos:

<img src="http://i67.tinypic.com/14w6mom.png" border="0" alt="Image and video hosting by TinyPic"></a>

Por último, en el caso de que queramos que se apague la máquina virtual usamos:

    vagrant halt

<img src="http://i63.tinypic.com/2pqnhy1.png" border="0" alt="Image and video hosting by TinyPic"></a>
