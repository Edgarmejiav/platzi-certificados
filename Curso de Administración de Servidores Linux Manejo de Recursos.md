¡Felicidades!
Aprobaste el curso. Ya puedes acceder a tu diploma digital.
10
Calificación
20 / 20
Aciertos
Curso de Administración de Servidores Linux: Manejo de Recursos
¿Cuál es el primer proceso que se inicia en el arranque del sistema?
init

1\.
¿Qué es el firmware?
Es un software que hace todo el inventario y chequeo de todos los dispositivos
conectados al momento del arranque.

2\.
¿Desde dónde se entra al modo recovery del sistema operativo?
Desde el GRUB

3\.
¿Para qué son útiles los usuarios en Linux?
Nos permiten separar las responsabilidades y permisos de acciones dentro del
sistema.

4\.
¿Para qué sirven los grupos en Linux?
Sirven para agrupar a los usuarios y un conjunto de permisos

5\.
¿Qué campo nos otorga información extra de nuestros usuarios?

6\.
GECOS
¿En qué archivo se guarda la información de nuestros usuarios?
/etc/passwd

7\.
¿Con qué comando puedo crear un usuario de manera interactiva?
adduser

8\.
¿Cómo puedo bloquear a un usuario?
usermod \-\-lock USERNAME

9\.
¿Cómo puedo ver los grupos a los que pertenece el usuario con el que inicie sesión?
groups

10\.
¿Cómo puedo cambiar el nombre de un grupo?
groupmod \-n nuevoNombre nombreActual

11\.
Si quiero que dos usuarios compartan archivos solo entre ellos ¿Qué tendría que hacer?
Crear un grupo, añadir a los usuarios a ese grupo y crear una carpeta compartida
con permisos especiales y el group owner.

12\.
Si creo un archivo usando el comando sudo ¿Quién es el dueño de este archivo?
root

13\.
Cuando se quieren ejecutar acciones a nivel administrador lo mejor es:
Limitar el número de usuarios administrador y ejecutar las acciones usando el
comando sudo.

14\.
Ir a Inicio
Ver menos
¿Cómo creo un usuario de tipo administrador?
Solo basta con agregarlo al grupo sudo o wheel.

15\.
Si quiero modificar el archivo de sudoers ¿Cuál es la mejor práctica para hacerlo?
Se hace con el comando visudo

16\.
¿Con cuál opción dentro de fdisk nos permite crear una nueva partición de un disco?
n

17\.
¿Qué pasa si creamos una tabla de particiones con fdisk en un disco que ya tiene archivos?
Una vez guardemos la tabla perderemos el contenido del disco.

18\.
Si queremos crear una copia exacta de nuestro disco en tiempo real ¿Qué nos conviene hacer?
Crea un arreglo RAID

19\.
Si queremos agrandar o achicar una serie de particiones de disco constantemente ¿Qué nos
conviene implementar?
Crear un grupo LVM

20\.
