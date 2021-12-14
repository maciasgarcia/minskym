Introduction
============
This is a *Minsky Machine* program editor (also known as the counter machine) coded in Python 3 by Juan Antonio Macías
([@juamacgar](http://www.twitter.com/juamacgar)).
This program editor tries to emulate the Minsky machine, an abstract machine which is Turing complete. It was formalized
by Marvin Minsky in 1961.

Machine features
----------------
This machine consists of an infinite sequence of registers, R<sub>1</sub>,R<sub>2</sub>,... in which we can store an
arbitrary natural number.
A program for the counter machine consists of a finite set of states {S<sub>0</sub>, S<sub>1</sub>,...,S<sub>n</sub>}
so that, for each i, there is an instruction to be executed by the machine whenever it reaches the state S<sub>i</sub>.
The state S<sub>0</sub> is reserved to indicate the program to stop.

There are two types of instructions:
> 1. Add 1 to the register R<sub>j</sub> and proceed to the state S<sub>k</sub>.
>    This instruction will be represented as (j, +, k).
> 2. Examine the register R<sub>j</sub>. If there is a 0 in it, proceed to state S<sub>l</sub>. In other case,
>    subtract 1 and then proceed to the state S<sub>k</sub>.
>    This type of instruction is represented as (j, -, k, l)

We will assume that S<sub>1</sub> is the initial state of the machine.

Usage of the editor
===================
This editor is coded in Python 3.3.2 and the modules used are the [SciPy](http://scipy.org/) suite to make use of
N-dimensional array functions and the module [tabulate](https://pypi.python.org/pypi/tabulate) to properly print some
parts of the program.

Functions implemented
---------------------
Work in progress.
