#AZURE: [![Azure](http://azuredeploy.net/deploybutton.png)](http://pdeportivasbot.cloudapp.net/)

Azure es un IaaS creado por Microsoft. Esta infraestructura como servicio (IaaS) es una infraestructura informática inmediata que se aprovisiona y administra a través de Internet. Permite reducir o escalar verticalmente los recursos con rapidez para ajustarlos a la demanda y se paga por uso.

Para poder usarlo, es necesario tener una suscripción. Gracias al código que nos facilito el profesor, ha sido posible la realización de este hito.

Una vez tenemos la suscripción, usaremos el siguiente comando para iniciar sesión en Azure:

    azure login

<img src="http://i65.tinypic.com/5n6x55.png" border="0" alt="Image and video hosting by TinyPic"></a>

Tras esto, tenemos que crear los certificados. Lo haremos con estas órdenes:

    openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout azure.pem -out azure.pem
    openssl x509 -inform pem -in azure.pem -outform der -out azure.cer
    chmod 600 azure.pem

<img src="http://i65.tinypic.com/b46rd2.png" border="0" alt="Image and video hosting by TinyPic"></a>

<img src="http://i63.tinypic.com/qyu05c.png" border="0" alt="Image and video hosting by TinyPic"></a>

Ahora, dentro de azure, nos [logueamos en nuestra cuenta](https://manage.windowsazure.com/). Buscamos el apartado Configuración, Certificados de administración, Cargar, y cargamos el archivo .cer

<img src="http://i63.tinypic.com/e6tyqw.png" border="0" alt="Image and video hosting by TinyPic"></a>

Tras este paso tiene que aparecernos una ventana similar a esta:

<img src="http://i63.tinypic.com/23w1tv7.png" border="0" alt="Image and video hosting by TinyPic"></a>
