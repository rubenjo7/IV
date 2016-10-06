# IV

Repositorio de la asignatura Infraestructura Virtual


<h1>Practica 0: Git y Github.</h1>
<h2>*Ruben Jimenez Ortega*</h2>

<h3>Prerrequisitos</h3>

<ol> 
	<li> Haber rellenado en la hoja de cálculo correspondiente la equivalencia entre nombre real y nick en GitHub. </li>
    <li> Haber cumplimentado los objetivos de la primera sesión </li>
</ol>

<h3>Realizacion</h3>

<h4>Edicion de datos del usuario</h4>

Es un paso bastante sencillo, basta con ingresar con nuestra cuenta de Github, tras esto, en la parte izquierda nos aparece un boton: "Edit Profile", pulsamos y podemos editar toda nuestra informacion facilmente.

<h4>Creacion de par de llaves e importacion a Github</h4>

Lo primero que tenemos que hacer es usar el siguiente comando:

	ssh-keygen -t rsa -C "rubenjo7412@gmail.com"

Tras esto tenemos que copiar la clave privada que se genera:

	cat /home/ruben/.ssh/id_rsa.pub

Lo que se muestra por pantalla es lo que tenemos que copiar. Esto debe copiarse en la parte del perfil que trata los temas de ssh.

<h4>Creacion nombre de usuario y correo para commits</h4>

	git config --global user.name "Ruben Jimenez Ortega"
    git config --global user.email "rubenjo7412@gmail.com"

<h4>Creacion de repositorio propio</h4>

Paso bastante sencillo. Solo tenemos que irnos a la parte superior de la interfaz de Github y le damos a "New Repository". Aqu podemos utilizar el nombre que queramos, en mi caso "IV".

<h4>Creacion de nuevo branch o rama</h4>

Un paso tambien bastante simple. Una vez dentro del repositorio creado, buscamos el desplegable donde pone "Branch" y añadimos uno nuevo. Yo lo he llamado "BranchP0".

<h4>Licencia, readme y P0</h4>

Una vez creado el repositorio, pasamos a añadir una licencia y un fichero readme. Una vez creado nos vamos a la rama branchP0 en mi caso y editamos el archivo readme.

Por ultimo tengo que añadir el fichero P0.md, esto se hace de manera muy sencilla:

	git fetch
    git add .
    git commit -m "descripcion"
    git push origin branchP0

<h4>Fork Repositorio de la asignatura</h4>

Buscamos el repositorio al cual queremos hacerle un fork, y tan solo tenemos que darle al botn que pone fork.

<h4>Pull request</h4>

Una vez finalizada la edicion del archivo, debemos hacer un pull request para que se actualicen nuestros cambios.

# DOCUMENTACION PRACTICA IV

<h3>Prerrequisitos:</h3>

- [x] Tener aprobado el hito 0 de proyecto.
- [x] Haber alcanzado el 80% de los objetivos del tema introductorio. 
- [x] Haber realizado los ejercicios propuestos. 

<h3>Aplicacion de "Peñas" deportivas:</h3>

Se va a intentar desarrollar un bot para Telegram. Este bot sera para llevar las estadisticas de una peña deportiva. Se podran añadir jugadores, tras estar dentro de la peña una serie de jugadores, se podran sortear equipos y tras finalizar el partido se podran añadir estadisticas del partido, como el resultado, o incluir la cantidad de goles que ha marcado cada jugador. Tras introducir el resultado se repartiran los puntos para cada jugador en funcion del resultado. Tambien se podran consultar clasificacion por puntos o clasificacion por goles.

<h3>Realizacion:</h3>

Para la realizacion de la practica, en principio necesitare:

* Tener instalado los paquetes necesarios para que phyton funcione correctamente.
* Una base de datos para almacenar los datos necesarios.
* API de bots para Telegram.

En principio pongo los que creo que voy a utilizar, esta lista se ampliara si necesitase usar algo mas.
