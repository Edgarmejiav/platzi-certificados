¡Felicidades!
Aprobaste el curso. Ya puedes acceder a tu diploma digital.

9\.33
Calificación
14 / 15
Aciertos
Curso de TypeScript
¿Cuál es comando con el cual pueda habilitar el análisis de código de TypeScript en un archivo
JavaScript?
@ts\-check

1\.
¿Cuál es la opción correcta para decirle al compilador de TS la versión de JavaScript a la cual
debe transpilar?
npx tsc src/\*\* \-\-target es6

2\.
Si se define esta variable  let myProductPrice \= 100; ¿Cuál es el tipo que infiere TS?
number

3\.
¿Cuál es la forma correcta de definir un hexadecimal en TS?
let hex \= 0xfff;

4\.
Una prueba práctica es definir una variable con un valor boolean de esta manera:  const
myBoolean: Boolean \= true;
No, ya que se debe evitar el boolean con Mayúscula

5\.
Teniendo en cuenta esta instrucción \`const rta \= 1 \+ '1';\` ¿Cuál sería el tipo de dato que infiere
TS de rta?

6\.
string
¿Cuál sería la forma correcta de definir un array que solo soporte números y booleanos?
let mixed: (number \| boolean )\[];

7\.
¿Cuál sería la forma correcta de definir una variable que solo soporte números y strings?
let myVar: number \| string;

8\.
Teniendo en cuenta este código: \`type Sizes \= 'S' \| 'M' \| 'L' \| 'XL';  let shirtSize: Sizes; shirtSize \=
'xxl';\` ¿El valor asignado a  shirtSize es válido?
FALSE

9\.
¿Cuál de las siguientes en la manera correcta de definir una parámetro opcional en una
función?
function sum(a?: number) {}

10\.
Si quiero declarar una función que no tiene retorno ¿cuál de las siguientes palabras reservadas
de TS usaría?
void

11\.
¿Cuál de estas formas es la manera correcta de definir un objeto como parámetros de una
función?
function login(data: {email: string, password: string}) { console.log(data.email,
data.password); }

12\.
¿Cuál es la manera correcta de crear un propio tipo para definir los atributos de un Producto?
type Product \= { title: string, createAt: Date, stock: number, shirtSize?: Sizes };

13\.
Cuando hay librerías que no tiene  soporte a tipos por ejemplo en el caso de  lodash podemos
agregar el soporte a tipos usando el comando...

14\.
Ir a Inicio
Siguiente curso
Ver menos
npm i @types/lodash \-\-save\-dev
¿Cuál es el tipado correcto para crear una variable que soporte strings y null?
let myName: (string \|\| null) \= null;
Repasar

15\.
Cursos que podrían interesarte
Curso de TypeScript: Tipos
Avanzados y Funciones
Por Nicolas Molina
Curso de Webpack
Por Oscar Barajas Tavares
Curso de A
Aplicacion
Por Nicolas
