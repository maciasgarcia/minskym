# coding: utf8
from pylab import *
from tabulate import tabulate
import re

# TODO Change the commands to a dictionary and also print the explanation for each command.
# TODO Modify editinstruc to give the option to put the new instruction in other position.
# TODO Add new instructions in betweeen?


def enterinitval():
    """This function will prompt for the initial values that will be used in the program. It will transform them into a
    vector"""
    initval = input("Introduce los valores iniciales:")  # Initial values input.
    # Removing parentheses, splitting and turning them into integers.
    initval = initval[1:-1]
    initval = re.split('[^0-9\+\-]+', initval)
    return [int(v) for v in initval]


def enterinstr():
    """This function will prompt for the instructions that will be used in the program. It will transform them into a
    matrix of instructions in which the first one will be made of zeros. The function will stop asking for instructions
    whenever "end" is entered as an instruction"""
    instructions = [[-2, -2, -2, -2]]  # Initial instruction matrix. Starts with -2 to ease on the indices and printing.
    inp = input("Introduce una instrucción: ")
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
                print("La instrucción no es válida.")
            inp = input("Introduce otra instrucción:")

        else:
            print("La instrucción no es válida.")
            inp = input("Introduce otra instrucción:")
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


def regtable(initval, instructions):
    """ This function parameters are a set of initial values and a program for Minsky's machine and returns a vector in
    which are store the sequence of instructions that the machine has gone through and each of the states of the machine
     in those steps. The third member of the vector is a tabulated version of the data."""

    # Calculating the maximum register needed and fill with zeros the initial values vector until completion.
    maxregister = instructions[:, 0].max()
    registers = [initval + [0]*(maxregister - len(initval))]
    currentinst = 1  # Initialize the variable to store S_i states.
    listinstruc = ["S%d" % currentinst]  # String list with S_i to tabulate
    listninstruc = [1]  # Int list of the states.
    # Loop that computes the table of states with the instructions given.
    while currentinst != 0:
        (ins, est) = applyinstr(instructions[currentinst], registers[-1])
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

    return registers, listninstruc, tabuldata


def getstate(instructions, initval, register, stepnum):
    """Given instructions, a set of initial values, a register number and a step number, this function returns
    the value of the register at that step once calculated the register states. If the register number is greater than
    the existing ones, it'll return 0. If the step number is greater than the number of steps needed to reach S0, it'll
    return the register value for S0. Additionally, if the register given is -1, the function will return the complete
    vector of register on that step."""
    (reg, lis, tab) = regtable(initval, instructions)
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
        return "El registro no es válido."


def editinstruc(instructions, nins, newinstruc):
    """This function edits the instruction number nins and replaces it for the newinstruc"""
    newinstruc = newinstruc[1:-1]
    splitinst = re.split('[^0-9\+\-]+', newinstruc)

    if splitinst[1] == "+" and len(splitinst) == 3:
        instructions[nins] = [int(splitinst[0]), 0, int(splitinst[2]), -1]
    elif splitinst[1] == "-" and len(splitinst) == 4:
        instructions[nins] = [int(splitinst[0]), 1, int(splitinst[2]), int(splitinst[3])]


def printinst(instructions):
    for i, instruc in enumerate(instructions):
        if instruc[1] == 0:    # Case in which we need to print a + instruction
            print("S%d  (%d, +, %d)" % (i, instruc[0], instruc[2]))
        elif instruc[1] == 1:  # Case in which we need to print a + instruction
            print("S%d  (%d, -, %d, %d)" % (i, instruc[0], instruc[2], instruc[3]))
        else:  # We use the fact that our matrix always starts with a row of -2, and no other row has other than 0 or 1.
            print("Instrucciones")
            print("=============")


def debugprogram(instructions):
    # Checking for program exit condition (i.e. exists a 0 somewhere in the states)
    if 0 not in instructions[:, 2] and 0 not in instructions[:, 3]:
        print("Su programa no tiene condición de salida.")
        print("Si quiere editar su programa use la instrucción 'Edit instruction'")
    infiniteloop = False
    infloopinst = []
    for i, instruct in enumerate(instructions):
        if i == instruct[2] or i == instruct[3]:
            infiniteloop = True
            infloopinst.append(i)
    if infiniteloop:
        print("Su programa podría no acabar al tener un bucle infinito en las instrucciones", infloopinst)
        print("Si no es su intención, modifique las instrucciones con 'Edit instruction'")



# commands = ['Commands', 'Enter values', 'Enter instructions', 'Register table', 'Edit instruction', 'Get state']
# usr_input = ''
# usr_initval = [0]
# while usr_input != "End":
#     while usr_input not in commands:
#         usr_input = input("¿Qué quiere hacer?: ")
#     if usr_input == commands[0]:
#         print("Los comandos disponibles son:")
#         for comm in commands:
#             print(comm)
#     elif usr_input == commands[1]:
#         val = enterinitval()
#     elif usr_input == commands[2]:
#         instruct = enterinstr()
#         debugprogram(instruct)
#     elif usr_input == commands[3]:
#         (regist, instlist, tabuld) = regtable(val, instruct)
#         print(tabuld)
#
#     usr_input = input("¿Qué quiere hacer?: ")