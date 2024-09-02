¡Felicidades!
Aprobaste el curso. Ya puedes acceder a tu diploma digital.
10
Calificación
20 / 20
Aciertos
Curso de Bases de Datos con MySQL y MariaDB
¿Cuál es el RDBMS que creó originalmente Monty y que ahora pertenece a Oracle?
MySQL

1\.
Cuando tengo una relación muchos a muchos, ¿cómo debería relacionar mis tablas?
Creando una tabla pivot que relacione una fila de una tabla con una fila de otra
tabla.

2\.
¿Cuál sentencia SQL me permite crear una nueva base de datos?
CREATE DATABASE

3\.
¿Cómo puedo crear un nuevo usuario en mi base de datos?
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';

4\.
¿Cómo puedo crear una nueva tabla dentro de mi base de datos?
CREATE TABLE

5\.
¿Cuál sentencia SQL me permite modificar una tabla de mi base de datos?

6\.


Ask
ALTER TABLE
¿Es posible insertar múltiples filas con un único INSERT INTO?
Verdadero, simplemente pongo cada nueva fila encerrada en paréntesis después
del VALUES.

7\.
Si dentro de mi tabla "usuarios" tengo un usuario con el id 4 cuyo "username" está escrito
como "RtaxMatser". ¿Qué sentencia SQL me ayudaría a corregir dicho nombre de usuario?
UPDATE \`usuarios\` SET username \= "RetaxMaster" WHERE id \= 4;

8\.
Si necesito borrar todos los registros de una tabla, pero sin reiniciar las llaves primarias ¿cuál
sentencia SQL debería utilizar?
DELETE FROM

9\.
Si necesito borrar una tabla ¿cuál sentencia SQL debería utilizar?
DROP TABLE

10\.
¿Cuál es esa frase que debes repetir ANTES DE BORRAR registros de una tabla?
Nunca hacer un DELETE FROM sin un WHERE.

11\.
¿Es posible hacer operaciones matemáticas en lenguaje SQL?
Verdadero

12\.
¿Es posible renombrar una columna usando la sentencia SELECT ?
Falso

13\.
¿En qué caso nos ayudan las consultas anidadas?

14\.
Ver menos
Cuando necesitamos ejecutar subconsultas antes de ejecutar nuestra consulta
principal para obtener ciertos datos.
¿Cuál de los siguientes sería un ejemplo en el que puedes aplicar las funciones espaciales?
Cuando necesito obtener la lista de restaurantes que estén a menos de 3
kilómetros de distancia de un usuario.

15\.
¿En qué casos es más recomendable usar procedimientos almacenados?
Cuando tenemos una consulta SQL muy larga que estaremos ocupando muchas
veces a lo largo de nuestra aplicación.

16\.
¿Es posible concatenar código SQL dentro de un procedimiento almacenado?
Verdadero. Gracias a los prepared statements y a la función CONCAT es posible
hacer esto.

17\.
¿Cuál es la diferencia entre CHARSET y COLLATE cuando creamos una tabla?
CHARSET define el tipo de caracteres que puedo insertar en mi base de datos y
COLLATE define cómo se hará la comparación de datos al consultarlos.

18\.
Las llaves primarias SIEMPRE deben ser números autoincrementales. Esta afirmación es...
Falsa. Puedo usar números de serie o algún otro dato que identifique un registro
como llave primaria.

19\.
¿Qué es una llave foránea?
Es una columna que nos permite relacionar los registros de una tabla con los
registros de otra tabla.

20\.
Ir a Inicio
Siguiente curso
Cursos que podrían interesarte
Curso de SQL y MySQL
Por Alberto Alcocer (Beco)
Curso de PHP con MySQL
Por Carlos Eduardo Gómez García
Curso de 
Elasticsea
Por Kevin S
