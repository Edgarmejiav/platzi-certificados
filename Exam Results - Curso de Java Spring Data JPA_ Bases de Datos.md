Rate this course

Close
Now you learned:

Da tus primeros pasos con Spring Data y JPA

Domina los Query Methods y Paginación con Spring Data Repositories

Ejecuta Queries Personalizados, Auditorías y Store Procedures

Sigue los principios ACID en tus transacciones

Content:


Teacher:


Do you recommend this course?

Tell the community what was the best part of this course (optional)

Submit rating
Rate this course

Close
My rating

ExamSummary.modalReviewed.month-NaN NaN, NaN
Content

Teacher

Curso de Java Spring Data JPA: Bases de Datos
Curso de Java Spring Data JPA: Bases de Datos

Don't give up!
You need a minimum score of 9.0 to pass.

Try again in:

05 h 56 m 35 s

7.33

Score

11/ 15

Correct answers

1.
¿Cuál de los siguientes subproyectos NO hace parte de Spring Data?
Spring Data Oracle
2.
¿Cuál es la implementación de JPA que por defecto tiene Spring Data JPA?
Hibernate
3.
Al usar el método save(entity) de CrudRepository, Spring internamente ejecuta un proceso para saber sí debe hacer un INSERT o un UPDATE en la base de datos.
Verdadero
4.
Sí quisiera recuperar una lista de pizzas disponibles ordenadas desde la más costosa a la más barata, ¿Qué query method debería usar?
findAllByAvailableTrueOrderByPriceDesc()
5.
Sí quisiera recuperar la lista de los clientes que en su nombre contengan "Cody" o "Charlotte", ¿Qué query method debería usar?
findAllByNameContainingOrNameContaining(name1, name2)
6.
Sí quisiera recuperar las 5 pizzas veganas más costosas ¿Qué query method debería usar?
findTop5ByVeganTrueOrderByPriceDesc()
7.
¿Qué valor de PageRequest debo usar en una consulta paginada si quiero recuperar 10 elementos de la segunda página?
PageRequest.of(2, 10)

Review
8.
En el proyecto de pizzeria ¿Qué tipo de query es el siguiente? *SELECT o FROM OrderEntity WHERE o.idOrder = ?*
JPQL
9.
¿Qué función cumple el atributo nativeQuery en la anotación @Query?
Permite indicar que el query es un SQL nativo.
10.
¿Qué ventaja tienen las Projections al usarlas como retorno de un @Query?
Permite retornar un solo campo sin necesidad de hacerlo con todo el entity.

Review
11.
¿Qué anotación se debe usar para realizar un INSERT, DELETE o UPDATE dentro de un @Query?
@Modifying
12.
¿Cuándo NO se debería usar la anotación @Transactional?
Cuando no queramos asegurar la atomicidad de nuestra transacción.

Review
13.
¿Cuál de las siguientes NO es una anotación de auditoría de Spring Data JPA?
@ModifiedDate
14.
Sí tengo un SQL que modifica información dentro de un @Query con @Modifying, no será "escuchado" por los @EntityListeners
Verdadero
15.
¿Qué función cumple el atributo outputParameterName en la anotación @Query?
Permite definir un parámetro de salida para enviar al stored procedure.

Review
Courses you might be interested in
Curso de Java Spring Security
Curso de Java Spring Security
Curso de Java Spring Security
By Alejandro Ramírez

Curso de Intro al Despliegue de Aplicaciones
Curso de Intro al Despliegue de Aplicaciones
Curso de Intro al Despliegue de Aplicaciones
By Santiago Bernal

Curso de Introducción a DevOps
Curso de Introducción a DevOps
Curso de Introducción a DevOps
By Jaivic Villegas

Go to Home

Next course