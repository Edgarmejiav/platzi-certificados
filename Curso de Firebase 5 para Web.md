¡No te rindas!
Necesitas una calificación mínima de 
9\.0 para aprobar.
Vuelve a intentarlo en:
05 h 55 m 32 s

8\.62
Calificación
25 / 29
Aciertos
Curso de Firebase 5 para Web
Firebase nos brinda servicios para:
El desarrollo de aplicaciones, mejorar la calidad de las aplicaciones y el crecimiento del
negocio

1\.
¿Cuáles de estos servicios de firebase se pueden usar en las aplicaciones Web?
Hosting, storage, base de datos

2\.
Firebase genera el código y permite tener en corto tiempo una aplicación Android con una
arquitectura adecuada:
Falso

3\.
En firebase puedo dar acceso detallado a cada uno de los servicios a los usuarios o miembros del
proyecto:
Verdadero

4\.
Es posible integrar Firebase con algunos servicios como por ejemplo Jira:
Verdadero

5\.
Firebase brinda oficialmente SDKs para:
Android, iOS, javascript y NodeJS

6\.
Firebase nos brinda algunos de estos proveedores de servicios de autenticación:
Email/pass, Facebook, Github

7\.
Desde la consola de firebase de gestión de usuarios podemos ver la contraseña del usuario:
Falso

8\.
Es posible modificar el cuerpo del mensaje de la plantilla del correo de verificación del email:
Falso

9\.
Si se requiere validar que el email dado por el usuario para la creación de la cuenta es válido, ¿qué
debes hacer?
Usar la función “sendEmailVerification”una vez autenticado y luego, preguntar si lo hizo
cuando intenta autenticarse a la aplicación

10\.
Es posible realizar autenticación de usuarios por medio del número de teléfono móvil:
Verdadero

11\.
Firestore tiene habilitado por defecto el almacenamiento offline:
Verdadero

12\.
Se requiere consultar los post por una fecha ordenados por autor y que solo retorne 10:
this.db
.collection('posts')
.where('fecha' , '\=\=', fecha)
.orderBy('autor', 'asc')

13\.
.limit(10\)
.onSnapshot(querySnapshot)
Si tenemos la siguiente consulta, ¿cómo sería el índice compuesto?
this.db
.collection('posts')
.where('fecha' , '\=\=', fecha)
.orderBy('autor', 'asc')
.orderBy('titulo', 'asc')
.limit(10\)
.onSnapshot(querySnapshot \=\>{})
Fecha ASC, Autor ASC, título ASC

14\.
Si queremos que el usuario solo pueda leer sus posts y los de nadie más, ¿qué regla colocamos?
match /posts/{post}/{uid} {
 allow read, delete: if request.auth.uid \=\= uid;
}

15\.
Para esta consulta tendríamos que crear un índice compuesto?
this.db
.collection('posts')
.where('fecha' , '\=\=', fecha)
.where('autor', '\=\=', autor)
.onSnapshot(querySnapshot \=\>{})
Verdadero

16\.
Podemos tener reglas de seguridad en el storage para la consulta o la subida de archivos:
Verdadero

17\.
Si requerimos subir un archivo al directorio del usuario que está dentro del directorio de pruebas y
que a su vez está dentro del directorio de la empresa ¿cómo lo haríamos?
firebase.storage().ref(empresa).child(‘usuario’).child(‘pruebas’)

18\.
Podemos pausar la subida de un archivo al storage desde Javascript con las librerías de Firebase:
Verdadero

19\.
Es posible desplegar una aplicación PHP en el hosting de Firebase:
Falso

20\.
Es posible tener varios sitios web en el mismo proyecto de Firebase:
Verdadero

21\.
Si requerimos asignar un caché a todas las páginas, ¿cómo lo hacemos en Firebase hosting?
Creamos una regla en el archivo de personalización del hosting agregándolo en la
propiedad de headers

22\.
Personalizar el dominio en Firebase Hosting tiene cobro
Falso

23\.
¿Qué cosas podemos personalizar en el hosting de Firebase?
Rewrites, header y redirects

24\.
Para recibir las notificaciones en background o en segundo plano, es necesario tener un Service
Worker:
Verdadero

25\.
¿Cuáles estados son necesarios al momento de recibir mensajes?

26\.
Ir a Inicio
Siguiente curso
Background, foreground
¿Qué tipo de envío de mensajes existen?
Token, grupo, tópico

27\.
Si requerimos enviar una notificación a los usuarios que le dieron un like o me gusta a una categoría
de productos cómo sería la mejor forma:
Creando un tópico por categoría

28\.
El token del usuario podría cambiar en el transcurso del tiempo:
Verdadero

29\.
Cursos que podrían interesarte
Curso de Firebase 5: Cloud
Functions
Por Juan Guillermo Gómez Torres
Curso de PostgreSQL Aplicado a
Ciencia de Datos
Por Israel Vázquez Morales
Curso de 
Por Carlos 
