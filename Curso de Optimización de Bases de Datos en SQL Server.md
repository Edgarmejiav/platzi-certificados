¡No te rindas!
Necesitas una calificación mínima de 
9\.0 para aprobar.
Vuelve a intentarlo en:
05 h 39 m 23 s

8\.67
Calificación
26 / 30
Aciertos
Curso de Optimización de Bases de Datos en SQL Server
Cuando estamos desarrollando una aplicación nueva ¿en qué momento debemos comenzar con el
análisis, diseño y optimización de la base de datos?
Al inicio del desarrollo.

1\.
¿Para qué sirve el plan de ejecución?
Nos permite analizar el comportamiento de un query, un procedimiento almacenado, una
vista, una función, etc.

2\.
¿Qué función tienen los índices?
Nos ayuda a mejorar el rendimiento de una consulta o un proceso.

3\.
Si un plan de ejecución nos recomienda crear un índice ¿hay que ejecutarlo inmediatamente?
No, siempre hay que analizar cada caso de forma individual y ver si lo que se necesita es
optimizar el query.

4\.
¿Los índices en las tablas o vistas siempre nos van a ayudar en el rendimiento?
No, siempre debemos de ver el comportamiento de los índices de forma individual.

5\.
¿Qué es Merge?
Merge nos permite en una sola operación realizar insert, update o delete en una o varias
tablas.

6\.
¿En qué momento se ejecuta un trigger?
Un trigger se ejecuta después de realizar un insert, delete o update en una tabla.

7\.
¿Cómo capturamos un error y reversamos una operación en un trigger?
Después de las validaciones, si hay un error ejecutamos ROLLBACK y RETURN

8\.
Si queremos crear una regla en una tabla para que una columna tenga un valor default ¿qué
debemos de utilizar?
Debemos de utilizar un CONSTRAINT.

9\.
¿Cómo podemos controlar que una tabla sea modificada o bien que nos notifique cuando esto
suceda?
Creamos un Trigger ON DATABASE que bloquee o reporte esta acción.

10\.
Si queremos tener control de los cambios en información en una tabla ¿cuál es la mejor opción que
nos brinda SQL Server?
Crear un trigger que capture todos los movimientos y los inserte en una tabla
histórica.
Repasar

11\.
¿Qué función nos brinda un catálogo Full Text Search?
Nos permite realizar búsquedas flexibles y más intéligentes en las tablas que lo integran.

12\.
¿Cuáles tipos de valores puede retornar una función?
Una función puede retornar un valor único o retornar una tabla.

13\.
¿Qué diferencia existe entre función tabla y una vista?
En una función tabla podemos utilizar parámetros para filtrar los datos. Una vista
siempre va a retornar los mismos datos y después aplicamos los filtros.

14\.
¿Cuál es la mejor forma de utilizar una vista?
La mejor forma de utilizar una vista es con WITH SCHEMABINDING y creándole un
índice.

15\.
¿Cómo debe hacerse para retornar un valor de un procedimiento almacenado?
Declarando variables OUTPUT para los valores que queremos retornar.

16\.
¿Qué ventaja nos puede dar retornar XML o JSON en nuestros procedimientos almacenados?
Nos puede generar un ahorro en recursos, ya que no tenemos que convertir los datos en
nuestra aplicación.

17\.
¿Qué es mejor utilizar, tabla temporal de sesión o tabla temporal global?
Lo mejor es utilizar tabla temporal de sesión.

18\.
¿Qué es mejor utilizar, tabla temporal de sesión o tabla variable?
Lo mejor es utilizar una tabla temporal de sesión ya que optimiza mejor los
recursos.
Repasar

19\.
¿El procedimiento EXEC sp\_send\_dbmail en cuál base de datos se debe ejecutar?
Se debe ejecutar en la base de datos msdb.

20\.
¿Cuál es el porcentaje recomendado de una tabla fragmentada para reordenar los índices?
Se recomienda para una tabla con 30% de fragmentación.

21\.
¿Cuál es el principal motivo para tener un adecuado plan de respaldos?

22\.
Poder recuperar una base de datos lo más rápido posible con la menor pérdida de datos.
¿Cuál sería la pérdida de información que eventualmente podríamos tener con una correcta
estrategia de respaldos?
Se perdería la información desde el último backup de transacción log al momento en que
la base de datos dejó de funcionar.

23\.
Si nuestra base de datos deja de funcionar ¿cuál es la forma correcta de recuperar la base de datos
de los backups que hemos realizado con nuestra estrategia de respaldos?
Primero debemos restaurar el último full backup, restaurar el último backup diferencial y
restaurar todos los backups del transaction log desde el último backup diferencial.

24\.
¿En qué momento es que podemos reducir el tamaño del Log de la base de datos?
Lo recomendado es hacer el backup del Transaction Log y después realizar el Shrink del
Log de la base de datos.

25\.
¿Cuántos archivos TempDB se recomienda inicialmente tener para la base de datos?
Se recomienda tener un archivo por núcleo del procesador.
Repasar

26\.
¿Cómo se recomienda tener almacenados los archivos de TempDB?
Se recomienda tener los archivos en un disco único para esta base de datos, exclusivo.

27\.
¿Es necesario eliminar una tabla variable después de utilizarla?
No es necesario.

28\.
En las tablas versionadas, cuando desvinculamos una tabla histórica de la tabla principal, ¿qué
sucede con los datos recuperados?
Los datos quedan almacenado en una tabla independiente histórica, los datos no se
pierden.

29\.
Ir a Inicio
Siguiente curso
Si tengo un disco propio para mi base de datos TempDB ¿de qué tamaño tengo que configurar los
archivos?
Se recomienda que el tamaño de los archivos sea pequeño y crezcan
conforme se van utilizando.
Repasar

30\.
Cursos que podrían interesarte
Curso Práctico de SQL
Por Israel Vázquez Morales
Curso Práctico de Bases de Datos
en AWS
Por Carlos Andrés Zambrano Barrera
Curso de 
con Azure
Por Héctor
