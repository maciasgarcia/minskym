# coding: utf8
from pylab import *
from tabulate import tabulate
import re


def enterinitval():
    """This function will prompt for the initial values that will be used in the program. It will transform them into a
    vector"""
    initval = input("Introduzca los valores iniciales: ")  # Initial values input.
    # Removing parentheses, splitting and turning them into integers.
    initval = initval[1:-1]
    initval = re.split('[^0-9\+\-]+', initval)
    return [int(v) for v in initval]


def enterinstr():
    """This function will prompt for the instructions that will be used in the program. It will transform them into a
    matrix of instructions in which the first one will be made of zeros. The function will stop asking for instructions
    whenever "end" is entered as an instruction"""
    instructions = [[-2, -2, -2, -2]]  # Initial instruction matrix. Starts with -2 to ease on the indices and printing.
    inp = input("Introduzca una instrucción: ")
    # Starting loop to enter instructions. Loop ends once "end" is given as an instruction.
    while inp != "end":
        if (inp[0] == "(") and inp[len(inp) - 1] == ")":
            inp = inp[1:-1]
            inps = re.split('[^0-9\+\-]+', inp)

            if inps[1] == "+" and len(inps) == 3:
                instructions = vstack([instructions, [int(inps[0]), 0, int(inps[2]), -1]])  # Last member is -1 for
                                                                                    # checking loop ending conditions.
            elif inps[1] == "-" and len(inps) == 4:
                instructions = vstack([instructions, [int(inps[0]), 1, int(inps[2]), int(inps[3])]])

            else:
                print("Lo siento, no es una instrucción válida.")
            inp = input("Introduzca otra instrucción: ")

        else:
            print("Lo siento, no es una instrucción válida.")
            inp = input("Introduzca otra instrucción: ")
    return instructions


def applyinstr(inst, state):
    """This function takes as parameters an instruction (in vector form, once transformed from input) and a machine
    state. It applies the instruction to the state given and returns the new machine's state and the number of the
    next instruction to apply."""
    regmodif = inst[0] - 1

    if inst[1] == 0:
        nstate = copy(state)   # Use copy() because when using = we only rename the object, thus modifying the original.
        nstate[regmodif] += 1
        return inst[2], nstate

    elif state[regmodif] != 0:
        nstate = copy(state)
        nstate[regmodif] -= 1
        return inst[2], nstate

    else:
        return inst[3], state


def regtable(initval, instructions, looplim):
    """ This function parameters are a set of initial values and a program for Minsky's machine and returns a vector in
    which are store the sequence of instructions that the machine has gone through and each of the states of the machine
     in those steps. The third member of the vector is a tabulated version of the data."""

    # Calculating the maximum register needed and fill with zeros the initial values vector until completion.
    maxregister = instructions[:, 0].max()
    registers = [initval + [0]*(maxregister - len(initval))]
    currentinst = 1  # Initialize the variable to store S_i states.
    listinstruc = ["S%d" % currentinst]  # String list with S_i to tabulate
    listninstruc = [1]  # Int list of the states.
    loopchecker = 0
    infiniteloop = False
    # Loop that computes the table of states with the instructions given.
    while currentinst != 0:
        (ins, est) = applyinstr(instructions[currentinst], registers[-1])
        if ins == currentinst:
            loopchecker += 1
        else:
            loopchecker = 0
        if loopchecker > looplim:
            infiniteloop = True
            currentinst = 0
        else:
            currentinst = ins
        listinstruc = vstack([listinstruc, ["S%d" % currentinst]])
        listninstruc = vstack([listninstruc, currentinst])
        registers = vstack([registers, est])
    # Header for the tabulated data.
    heade = ["Ins"]
    for i in range(maxregister):
        heade.append("R%d" % (i+1))
    # Table for data printing.
    tabuldata = tabulate(hstack(([listinstruc, registers])), headers=heade, tablefmt='rst')

    return registers, listninstruc, tabuldata, infiniteloop


def getstate(instructions, initval, register, stepnum, looplim):
    """Given instructions, a set of initial values, a register number and a step number, this function returns
    the value of the register at that step once calculated the register states. If the register number is greater than
    the existing ones, it'll return 0. If the step number is greater than the number of steps needed to reach S0, it'll
    return the register value for S0. Additionally, if the register given is -1, the function will return the complete
    vector of register on that step."""
    (reg, lis, tab, loop) = regtable(initval, instructions, looplim)
    numstates = len(reg)
    maxregister = instructions[:, 0].max()

    if register == 0:
        if stepnum > numstates:
            return 0
        else:
            return lis[stepnum - 1][0]
    elif register > 0:
        if register > maxregister:
            return 0
        elif stepnum > numstates:
            return 0
        else:
            return reg[stepnum - 1][register - 1]
    elif register == -1:
        if stepnum > numstates:
            return reg[numstates - 1]
        else:
            return reg[stepnum - 1]
    else:
        return "Lo siento, no es un número de registro válido."


def editinstruc(instructions, nins, newinstruc):
    """This function edits the instruction number nins and replaces it for the newinstruc"""
    newinstruc = newinstruc[1:-1]
    splitinst = re.split('[^0-9\+\-]+', newinstruc)

    if splitinst[1] == "+" and len(splitinst) == 3:
        instructions[nins] = [int(splitinst[0]), 0, int(splitinst[2]), -1]
    elif splitinst[1] == "-" and len(splitinst) == 4:
        instructions[nins] = [int(splitinst[0]), 1, int(splitinst[2]), int(splitinst[3])]


def printusrdata(values, instructions):
    valstr = "("
    for ival in values:
        valstr += "%d, " % ival
    valstr = valstr[:-2]
    valstr += ")"
    print("Valores iniciales")
    print("=================")
    print(valstr)
    for i, instruc in enumerate(instructions):
        if instruc[1] == 0:    # Case in which we need to print a + instruction
            print("S%d  (%d, +, %d)" % (i, instruc[0], instruc[2]))
        elif instruc[1] == 1:  # Case in which we need to print a + instruction
            print("S%d  (%d, -, %d, %d)" % (i, instruc[0], instruc[2], instruc[3]))
        else:  # We use the fact that our matrix always starts with a row of -2, and no other row has other than 0 or 1.
            print("Instrucciones")
            print("=============")


def debugprogram(instructions):
    """This function will check in the instruction matrix for 3 things: a program endig condition, if there is a
    possibility of an endless loop and if there are referenced unexisting instructions"""
    programend = True
    infiniteloop = False
    nonexistinst = False
    instrnumber = len(instructions)
    infloopinst = []

    for i, instruct in enumerate(instructions):
        if i == instruct[2] or i == instruct[3]:
            infiniteloop = True
            infloopinst.append(i)
    # Checking for program ending condition (i.e. exists a 0 somewhere in the program).
    if 0 not in instructions[:, 2] and 0 not in instructions[:, 3]:
        programend = False
        print("Su programa no tiene una condición de salida.")
    # Checking for infinite loops in the program.
    if infiniteloop:
        print("Su programa podría no acabar debudi a un bucle infinito localizado en las instrucciones", infloopinst)
    # Checking for instructions referenced that do not exist.
    if (instructions[:, 2].max() > instrnumber) or (instructions[:, 3].max() > instrnumber):
        nonexistinst = True
        print("Su programa hace referencia a una instrucción que no existe.")

    if infiniteloop or not programend or nonexistinst:
        print("Si desea editar su programa, utilice el comando 'Modificar instrucción' o introduzca un nuevo programa"
              " con 'Introducir instrucciones'")


commands = {'Comando': 'Muestra la lista de comandos y sus explicaciones.',
            'Introducir valores': 'Permite al usuario introducir valores iniciales para el programa. Los valores '
                                  'deberán estar entre paréntesis y separados por comas.',
            'Introducir instrucciones': 'Permite al usuario introducir un programa dando sus instrucciones. Cada '
                                        'instrucción deberá ser introducida en el orden deseado y en la forma '
                                        '(j,+,k) o (j,-,k,l).',
            'Tabla registros': 'Muestra una tabla con los registros en cada uno de los pasos del programa.',
            'Mostrar datos': 'Muestra los datos introducidos por el usuario.',
            'Modificar instrucción': 'Permite al usuario modificar una instrucción introducida.',
            'Obtener registro': 'Permite recuperar el contenido de un registro o el número del estado en un paso del '
                                'programa. Cuando se introduce 0 como registro, devolverá la instrucción en la que se '
                                'encuentra en dicho paso. Al introducir -1 devolverá todos los registros.',
            'Depurar': 'Depura el programa actual. Alerta sobre bucles infinitos, la falta de condiciones de salida '
                       'del programa y la referencia a instrucciones inexistentes. Se ejecurará automáticamente cada '
                       'vez que el usuario introduzca un programa por sus instrucciones.',
            'Límite bucle': 'Permite al usuario definir un nuevo máximo de iteraciones en las que el programa parará si'
                            ' cree que se encuentra en un bucle infinito.'}


def main():
    print("Primero introduzca los valores iniciales y después las instrucciones que componen el programa.")
    print("   *Los valores iniciales deberán estar entre paréntesis y separados por comas.")
    print("   *Cada instrucción deberá estar dada en el orden deseado y en la forma (j,+,k) o (j,-,k,l).")
    usr_input = ''
    looplimit = 50
    usr_initval = enterinitval()
    usr_instruc = enterinstr()
    debugprogram(usr_instruc)

    while usr_input != "End":
        while usr_input not in commands.keys():
            usr_input = input("¿Qué quiere hacer ahora?: ").capitalize()

        if usr_input == 'Commands':
            print("Los comandos disponibles son:")
            for icom, comm in enumerate(commands):
                print(icom + 1, "-.", comm, ":", commands[comm])

        elif usr_input == 'Introducir valores':
            usr_initval = enterinitval()

        elif usr_input == 'Introducir instrucciones':
            usr_instruc = enterinstr()
            debugprogram(usr_instruc)

        elif usr_input == 'Tabla registros':
            (regist, instlist, tabuld, loop) = regtable(usr_initval, usr_instruc, looplimit)
            if loop:
                print(tabuld)
                print("Su programa fue detenido debido a un posible bucle infinito.")
            else:
                print(tabuld)

        elif usr_input == 'Mostrar datos':
            printusrdata(usr_initval, usr_instruc)

        elif usr_input == 'Modificar instrucción':
            n = input("¿Qué instrucción quiere modificar?: ")
            insstr = input("Introduzca la nueva instrucción: ")
            editinstruc(usr_instruc, n, insstr)

        elif usr_input == 'Depurar':
            debugprogram(usr_instruc)

        elif usr_input == 'Obtener registro':
            m1 = int(input("Introduzca el número de registro: "))
            m2 = int(input("Introduzca el paso que quiere consultar: "))
            print(getstate(usr_instruc, usr_initval, m1, m2, looplimit))

        elif usr_input == "Loop limit":
            looplimit = int(input("How many iterations do you want to set for the limit?: "))

        usr_input = input("¿Qué quiere hacer ahora?: ").capitalize()

if __name__ == "__main__":
    main()