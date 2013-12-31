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

Funciones implementadas
-----------------------
En curso.