¡Felicidades!
Aprobaste el curso. Ya puedes acceder a tu diploma digital.
10
Calificación
15 / 15
Aciertos
Curso de Modelado de Datos en MongoDB
¿Qué es el formato BSON en MongoDB?
BSON es un formato creado por MongoDB que se encarga de almacenar los
documentos en un formato binario que tengan mayor rendimiento y nuevos tipos de
datos.

1\.
¿Cuál es el orden correcto de los 3 pasos de la metodología vista en el curso para modelar una
base de datos en MongoDB?

1\. Identificar los requerimientos 
2\. Identificar las entidades y relaciones 
3\.
Identificar y aplicar patrones

2\.
¿Qué es Mongo Atlas?
Es un servicio directo de los creadores de MongoDB en donde se pueden
administrar y escalar una base de datos en MongoDB

3\.
¿Cuál es el objetivo del documento de Workload?
Nos ayuda a identificar la carga de la base de datos tanto de lectura de escritura,
las entidades, actores y observaciones encontradas en el caso de negocio.

4\.
¿Cuál es la función del comando \`docker\-compose up \-d mongodb\`?

5\.
Levantar un contenedor que corre MongoDB 
¿Cuál de las siguientes es la manera correcta de validar que en una colección el campo name
sea un string?
db.createCollection("users", { validator: { $jsonSchema: { bsonType: "object",
properties: { name: { bsonType: "string", }, }, }, }, });

6\.
¿Cuál de las siguientes es la manera correcta de validar que en una colección el campo age
tenga un minimo y maximo?
db.createCollection("users", { validator: { $jsonSchema: { bsonType: "object"
properties: { age: { bsonType: "number", minimum: 18, maximum: 99 } }, }, }, });

7\.
¿Cuál de las siguientes es la manera correcta de validar que en una colección el campo sizes
sea un array con minimo un elemento?
db.createCollection("products", { validator: { $jsonSchema: { bsonType: "object",
properties: { sizes: { bsonType: "array", minItems: 1, }, }, }, }, });

8\.
¿Cuándo tienes una relación 1\-1 el 90% de los casos se expresa como una relación embebida?
TRUE

9\.
¿Cuál es el caso más común en donde una relación 1\-1 puede ir de forma referenciada?
Cuando el documento está pasando el límite de los 16 MB en peso.

10\.
Cuándo tenemos una relación de uno a pocos: ¿esta relación se expresa de forma embebida o
referenciada?
Se expresa de forma embebida

11\.
Cuándo tenemos una relación de uno a muchos: ¿esta relación se expresa de forma embebida
o referenciada?
Se expresa de forma referenciada

12\.
Ir a Inicio
Siguiente curso
Ver menos
Cuándo tenemos una relación de muchos a muchos: ¿esta relación se expresa de forma
embebida o referenciada?
Se expresa de forma referenciada

13\.
¿Qué es la Desnormalización en MongoDB?
Es una técnica utilizada para almacenar datos redundantes en un documento para
evitar tener que realizar múltiples consultas.

14\.
¿Qué es el Computed Pattern en MongoDB?
Es un patrón que se basa en hacer precálculos a medida que se ingresan valores a
la DB con el fin de evitar consultar un gran volumen de documentos para obtener
un resultado.

15\.
Cursos que podrían interesarte
Curso de MongoDB: Aggregation
Framework
Por Carlos Olivera Terrazas
Curso de Introducción a MongoDB
Por Nicolas Molina
Curso de 
Fundame
Por Enriqu
