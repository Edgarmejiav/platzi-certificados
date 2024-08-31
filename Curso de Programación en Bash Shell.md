¡Felicidades!
Aprobaste el curso. Ya puedes acceder a tu diploma digital.

9\.67
Calificación
29 / 30
Aciertos
Curso de Programación en Bash Shell
El kernel es la parte fundamental del Sistema Operativo (núcleo) que permite gestionar y
administrar los recursos de hardware como son la memoria, el tiempo de procesamiento, el
sistema de archivos, las entradas/salidas y es donde se ejecutan las aplicaciones:
Verdadero

1\.
La programación bash tiene como objetivo poder ejecutar múltiples comandos de forma
secuencial para automatizar una tarea en específico:
Verdadero

2\.
¿Una vez creado un script antes de ejecutarlo se tiene que otorgar un permiso de ejecución,
con cuál comando se realiza esta acción?
chmod \+x script.sh

3\.
¿Dentro del alcance de una variable, ésta no puede ocuparse en otro script a menos que sea
visible a nivel del sistema utilizando el comando EXPORT?
Verdadero

4\.
¿Cuáles son los operadores relacionales que se utilizan en la programación bash?
\< \=\= !\=

5\.
¿En el caso de envíe un número de 20 argumentos a mi programa bash y necesita recuperar el
número 14, cuál de las siguientes sentencias utilizaría?
${14}

6\.
¿Si se requiere ejecutar un comando dentro de un script y almacenar su respuesta cuál es la
sentencia correcta para realizarlo?
variable \= $(comando)

7\.
¿Cuál es el comando que se utiliza para realizar un debug de un script y que permita
diferenciar los comandos de la salida estándar?
bash \-x script.sh

8\.
¿Cuál es el comando que se utiliza para capturar información en un programa shell?
read

9\.
Cuando se captura la información ingresada por el usuario y se utiliza validación del tamaño de
campo se puede eliminar la información:
Falso

10\.
¿Cuándo se utiliza la validación de información utilizando expresiones regulares y se requiere
tener 2 ocurrencias de una expresión que sentencia se utiliza para definir la expresión?
^\[0\-9]{2}$

11\.
¿Cuál es la forma correcta de pasar opciones a un programa?
./programa.sh \-opt1 \-opt2

12\.
¿Cuál es el comando que se utiliza para descargar un programa desde internet?
wget http://www.utilidades.com/programa.zip

13\.
En las sentencias de decisión e iteración es necesario respetar los espacios en las condiciones
para evitar errores:
Verdadero

14\.
En una expresión condicional para comparar números, ¿qué expresión se utiliza?
\[ $variable \-eq 10 ]

15\.
La sentencia case puede evaluar un rango de caracteres
Verdadero

16\.
¿Cuál de las siguientes declaraciones es correcta para crear un arreglo?
arregloTmpNumeros\=(1 2 3 4\)

17\.
Cuando se utiliza la sentencia de iteración for loop se puede iterar arreglos directamente:
Verdadero

18\.
¿Cuál es el formato correcto para declarar un while loop? Considerando que todo está en una
línea y que las palabras  y  serán reemplazadas por una condición
lógica y sentencias respectivamente.
while \[  ]; then  done

19\.
¿Para qué se utiliza la sentencia break dentro de un loop?
Parar la iteración y salir del loop

20\.
Para crear un menú de opciones en un programa bash, ¿qué sentencia de iteración se utiliza?
while loop

21\.
¿Qué comando se utiliza para crear un directorio llamado prueba?

22\.
mkdir prueba
¿Con cuál de los siguientes comandos se puede escribir en un archivo llamado prueba.txt sin
utilizar un programa externo?
echo texto \>\> prueba.txt

23\.
¿Cuál sentencia se utiliza para leer el contenido de un archivo llamado prueba.txt dentro de un
programa bash?
cat prueba.txt

24\.
¿Cuál de los siguientes comandos es correcto para copiar todos los archivos de un directorio a
otro estando en otro directorio?
cp \-R directorio1/ directorio2/

25\.
¿Con cuál comando se puede empaquetar solamente un archivo simple y no un conjunto de
archivos?
gzip

26\.
¿Cuál comando para empaquetar soporta poner un password al archivo empaquetado?
Zip

27\.
Se requiere realizar un programa en bash que permite sacar respaldos de información y que
los transfiera de forma empaquetada por la red a otra computadora en la cual se conoce la IP y
el lugar a donde se debe transferir el respaldo. ¿Cuál es la forma más óptima de pasar la
información?
Utilizar un comando de transferencia de información con características de
empaquetamiento de forma remota desde al origen al destino.

28\.
¿Cuál es el formato para declarar una función llamada validarNumeros?
validarNumeros (){ ….}

29\.
Ir a Inicio
Ver menos
Para llamar a una función dentro de un programa bash debe crearse antes de realizar la
llamada:
Verdadero

30\.
