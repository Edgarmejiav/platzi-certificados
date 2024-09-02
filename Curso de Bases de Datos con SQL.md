¡Felicidades!
Aprobaste el curso. Ya puedes acceder a tu diploma digital.
10
Calificación
19 / 19
Aciertos
Curso de Bases de Datos con SQL
¿Cuál es la instrucción correcta para seleccionar todas las columnas de una tabla llamada
“empleados”?
SELECT \* FROM empleados

1\.
¿Cuál es la instrucción correcta para seleccionar todas las columnas de una tabla llamada
"empleados"?
SELECT \* FROM empleados

2\.
¿Qué tipo de JOIN se utiliza para retornar todas las filas cuando hay una coincidencia en
ambas tablas?
INNER JOIN

3\.
Cuál es la instrucción correcta para insertar una nueva fila en la tabla "clientes"?
INSERT INTO clientes (nombre, edad) VALUES ('Juan', 30\);

4\.
¿Cuál es la cláusula correcta para seleccionar todos los empleados cuyo salario sea mayor a
50000?
SELECT \* FROM empleados WHERE salario \> 50000;

5\.
¿Cuál es la instrucción para obtener la suma de la columna "salario" de la tabla "empleados"?

6\.
SELECT SUM(salario) FROM empleados;
¿Cuál es la instrucción correcta para agrupar por la columna "departamento" y contar el
número de empleados en cada departamento?
SELECT departamento, COUNT(\*) FROM empleados GROUP BY departamento;

7\.
¿Cuál es la instrucción correcta para filtrar los grupos que tienen más de 10 empleados?
SELECT departamento, COUNT(\*) FROM empleados GROUP BY departamento
HAVING COUNT(\*) \> 10;

8\.
¿Cuál es la instrucción correcta para crear una tabla llamada "productos" con las columnas
"id", "nombre" y "precio"?
CREATE TABLE productos (id INT, nombre VARCHAR(50\), precio DECIMAL(10, 2\));

9\.
¿Cuál es la instrucción correcta para definir "id" en SQL como clave primaria al crear una tabla
"clientes"?
CREATE TABLE clientes (id INT PRIMARY KEY, nombre VARCHAR(50\));

10\.
¿Cuál es la instrucción correcta para crear un procedimiento almacenado llamado
"ActualizarSalario"?
CREATE PROCEDURE ActualizarSalario AS BEGIN UPDATE empleados SET salario \=
salario \* 
1\.1; END;

11\.
¿Cuál es la instrucción correcta para crear un índice en la columna "apellido" de la tabla
"empleados"?
CREATE INDEX idx\_apellido ON empleados(apellido);

12\.
¿Cuál es la diferencia principal entre una vista materializada y una vista temporal?
Una vista materializada almacena físicamente los datos, mientras que una vista
temporal no almacena los datos.

13\.
Ver menos
¿Cuál es la instrucción correcta para realizar un producto cartesiano entre las tablas?
SELECT \* FROM productos CROSS JOIN categorías;

14\.
¿Qué tipo de JOIN devuelve todas las filas de la tabla de la izquierda y las filas coincidentes de
la tabla de la derecha?
LEFT JOIN

15\.
¿Qué tipo de JOIN devuelve todas las filas de la tabla de la derecha y las filas coincidentes de
la tabla de la izquierda?
RIGHT JOIN

16\.
Cuál es la instrucción correcta para seleccionar todos los empleados que trabajan en los
departamentos 'Ventas' o 'Marketing' y cuyo nombre comience con la letra 'A'?
SELECT \* FROM empleados WHERE departamento IN ('Ventas', 'Marketing') AND
nombre LIKE 'A%';

17\.
¿Cuál es la instrucción correcta para actualizar el campo "edad" a 30 para todos los empleados
cuyo nombre sea 'Carlos'?
UPDATE empleados SET edad \= 30 WHERE nombre \= 'Carlos';

18\.
¿Cuál es la diferencia entre DELETE, DROP y TRUNCATE?
DELETE elimina filas específicas de una tabla sin afectar su estructura, DROP
Elimina la tabla , incluyendo su estructura y TUNCARE Elimina todas las filas de una
tabla pero mantiene su estructura

19\.
Cursos que podrían interesarte
Ir a Inicio
Siguiente curso
Curso de Sketch
Por Tomás Nicolini
Curso de Introducción a
Frameworks de PHP
Por Profesor Italo Morales F
Curso de 
Profesion
Por Jesús V
