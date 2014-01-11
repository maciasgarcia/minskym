Introducción
============
Este programa es un editor de programas para la *máquina de Minsky* (también conocida como máquina de registros)
programada en Python 3 por Juan Antonio Macías ([@JuanMtg](http://www.twitter.com/JuanMtg)).
Este editor de programas trata de emular a la máquina de Minsky, una máquina teórica equivalente a la máquina de Turing.
Fue formalizada por Marvin Minsky en 1961.

Características de la máquina
-----------------------------
La máquina de registros consta de una sucesión infinita de registros R<sub>1</sub>,R<sub>2</sub>,... en los cuales se
puede almacenar un número natural arbitrario.
Un programa para la máquina de registros consiste de un conjunto finito de estados {S<sub>0</sub>, S<sub>1</sub>,...,
S<sub>n</sub>} tales que, para cada i, hay una instrucción a ejecutar por la máquina cuando alcance el estado
S<sub>i</sub>. El estado S<sub>0</sub> es un estado reservado para indicar al programa que debe parar

Existen dos tipos de instrucciones:
> 1. Sumar 1 al registro R<sub>j</sub> y proceder al estado S<sub>k</sub>.
>    Esta instrucción se representará por (j, +, k).
> 2. Examinar el registro R<sub>j</sub>. Si hay un 0 en dicho registro, pasamos al estado S<sub>l</sub>. En otro caso
>    restar 1 y proceder al estado S<sub>k</sub>.
>    Este tipo de insrucción se representa por (j, -, k, l).

Consideraremos que el estado S<sub>1</sub> es el estado inicial de la máquina.

Uso del editor
==============
Este editor está programado en Python 3.3.2 y los módulos necesarios para hacer uso de él son la suite
[SciPy](http://scipy.org/) para hacer uso de los arrays N-dimensionales y el módulo
[tabulate](https://pypi.python.org/pypi/tabulate) para mostrar correctamente tabulados los datos de los registros.

Funcionamiento
--------------
Una vez ejecutado el programa, indicará que deben introducirse primero un conjunto de valores iniciales para el programa
y las instrucciones que compondrán el mismo. Se detalla la forma de introducción (entre paréntesis y separadas por comas
para los valores, y como representados anteriormente y en orden para las instrucciones), y una vez terminado, se
preguntará al usuario qué desea hacer a continuación. Los comandos disponibles son:
> 1. **Comandos**: Muestra la lista de los comandos con su explicación.
> 2. **Introducir valores**: Comando para introducir nuevos valores iniciales.
> 3. **Introducir instrucciones**: Comando para introducir un nuevo programa mediante sus instrucciones.
> 4. **Tabla registros**: Muestra una tabla con el programa una vez evaluado, en el que se tienen los contenidos de los
>                         registros en cada paso.
> 5. **Mostrar datos**: Muestra los datos introducidos por el usuario, esto es, los valores iniciales y las
>                       instrucciones.
> 6. **Modificar instrucción**: Permite modificar una única instrucción de un programa introducido.
> 7. **Obtener registro**: Este comando permite recuperar el contenido de un registro en un paso determinado del
>                          programa. También permite recuperar la instrucción en dicho paso o el vector de registros
>                          completos en un paso.
> 8. **Depurar**: El comando depurar indica si existen problemas con el programa introducido, como bucles infinitos,
>                 que el programa no tenga condición para terminar o que haya referencias a instrucciones que no
>                 existen.
> 9. **Limite bucle**: En caso de que el usuario necesite un máximo de iteraciones mayor que el establecido, este
>                      comando permite cambiarlo.

Para terminar la ejecución del programa, bastará con introducir "End" como comando. No es precisa la correcta
capitalización de los comandos anteriores al introducirlos.
