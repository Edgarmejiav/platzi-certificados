¡Felicidades!
Aprobaste el curso. Ya puedes acceder a tu diploma digital.
10
Calificación
26 / 26
Aciertos
Curso de MongoDB: Aggregation Framework
Si necesitas hacer una consulta que solamente fintre los documentos por el valor de un campo
especifico, que alternativa susarias?
MongoDB Query Languaje

1\.
Si deseas agregar una etapa que te conserve los campos existenete, y solo te agregue al
resultado un campo nuevo, que operador usarias?
$set

2\.
Si necesitas transformar completamente la estructura de tus documentos, en el objeto final, el
operador más adecuado sería:
$project

3\.
Qué hace el operador $unwind?
Crea un objeto por cada elemento que existe en el array

4\.
Además de limitar el tamaño del resultado de la consulta, utilizar $limit nos ayuda a
ahorrar consumo de memoria y mejorar performance

5\.
Crear una colección nueva en MongoDB con los resultados de un pipeline es posible con el
operador:

6\.


Ask
$out
Qué es GeoJSON?
Formato para codificar estructuras geográficas utilizando JSON

7\.
Cual es la forma correcta para describir un punto en GeoJSON?
{ "type": "Point", "coordinates": \[
125\.6, 
10\.1] }

8\.
Uniones entre colecciones es posible con:
$lookup

9\.
Los campos requeridos para utilizar $lookup son:
from: localFields: foreignField: as:

10\.
Para obtener datos detallados de los recursos que consume una consulta, debemos usar:
explain("executionStats")

11\.
De que forma se le indica al operador $group, cual es el campo sobre el cual se agruparan los
elementos
\_id: ,

12\.
Indica cual de estas opciones NO corresponde a un operador de acumulación:
$geoNear

13\.
¿Cuál de las siguientes es la forma correcta de calcular el promedio de un campo llamado
"score" en todos los documentos de una colección llamada "tests" usando el operador de
agregación $avg

14\.
(\[{$group: {\_id: null, average: {$avg: "$score"}}}])
¿Cuál es el propósito del operador $lookup en el MongoDB Aggregation Framework?
Realizar operaciones de unión entre dos colecciones

15\.
¿Qué hace el campo as en la operación $lookup?
Crea un nuevo campo en cada documento de entrada que contiene los documentos
coincidentes de la colección de "from"

16\.
¿Cuál es el propósito del operador $bucket?
Para agrupar los documentos en intervalos definidos por el usuario

17\.
¿Cuál es la diferencia principal entre $bucket y $bucketAuto en el Aggregation Framework de
MongoDB?
$bucket requiere que los intervalos se definan manualmente, mientras que
$bucketAuto define automáticamente los intervalos de agrupamiento

18\.
¿Cuáles son los componentes principales de la especificación de $accumulator?
init, accumulate, merge, finalize, lang y accumulateArgs

19\.
¿Qué es el operador $redact en MongoDB Aggregation Framework?
Es un operador que permite limitar el acceso a ciertos datos dentro de los
documentos

20\.
¿Para qué sirve el operador $function en MongoDB Aggregation Framework?
Para permitir la ejecución de una función personalizada de JavaScript en el servidor

21\.
¿Cuál de los siguientes NO es un parámetro de $function?

22\.
Ver menos
filter
¿Qué se debe tener en cuenta al usar $function?
Puede afectar el rendimiento y debe usarse con precaución

23\.
¿Qué sucede con los campos que no se especifican en la etapa $project?
Se omiten del documento de salida

24\.
¿Es posible agregar nuevos campos a los objetos de salida con $project?
Sí, $project puede agregar nuevos campos

25\.
Considera el documento { \_id: 1, tags: \['a', 'b', 'c'] }. ¿Cómo se verían los documentos después
de aplicar { $unwind: "$tags" }?
{ \_id: 1, tags: 'a' }, { \_id: 1, tags: 'b' }, { \_id: 1, tags: 'c' }

26\.
Cursos que podrían interesarte
Fundamentos de Arquitectura de
Software
Por Guido Contreras Woda
Curso de Introducción a los
Patrones de Diseño de Software
Por Daniel Basulto
Curso de A
para Desa
Por Manue
Ir a Inicio
Siguiente curso
