#!/usr/bin/env python

import os, sys
lib_path = os.path.abspath(os.path.join('ext'))
sys.path.append(lib_path)

import stack
import smath
import readline

ext = {}
running = 1

# commands functions

def help_():
    f = open("readme.txt", "r")
    for line in f.readlines():
        print line[:-1]
    f.close()

def exit_():
    global running
    running = 0

def import_(arg):

    global ext

    try:
        __import__(arg)
        imp = sys.modules[arg]
    except KeyError:
        print "Imported module", arg, "doesn't exist"
        return
        
    vars_ = dir(imp)

    for var in vars_:
        func = getattr(imp, var)
        if callable(func):
            ext[var] = func

# basic commands

cmds = {"exit" : (0, str, exit_),
        "help" : (0, str, help_),
        "import" : (1, str, import_),
	"push" : (-1, float, lambda x: stack.stack.append(x)),
        "ls" : (0, str, stack.ls),
        "last" : (1, int, stack.last),
        "pop" : (1, int, stack.pop),
        "top" : (2, int, stack.top) }

# basic operations

opers = {   "+" : smath.add,
            "-" : smath.minus,
            "*" : smath.mult,
            "/" : smath.div,
            "**" : smath.exp,
            "%" : smath.mod }

ext.update(opers)

def complete(text, state):
    for cmd in cmds.keys():
        if cmd.startswith(text):
            if not state:
                return cmd
            else:
                state -= 1
    for cmd in ext.keys():
        if cmd.startswith(text):
            if not state:
                return cmd
            else:
                state -= 1

readline.parse_and_bind("tab: complete")
readline.set_completer(complete)

def split_args(scan):

    out = []
    tmp = ""
    split = True
    subout = []

    for c in scan:
	if c == ' ' and split:
	    out.append(tmp)
	    tmp = ""
	elif c == '(':
	    split = False
	    if tmp == "":
                subout.append(out.pop())
            else:
                subout.append(tmp)
                tmp = ""
	elif c == ')':
	    split = True
	    subout.append(tmp)
	    out.append(subout)
	    subout = []
	    tmp = ""
        elif c == ',' and not split:
	    subout.append(tmp)
	    tmp = ""
	else:
	    tmp += c

    if tmp != "":
        out.append(tmp)

    return out

def exec_cmd(cmd, *args):
	
    for name, struct in cmds.iteritems():
	if name == cmd:
	    n = struct[0]

	    if n > 0:
		try:
		    args = args[:n]
		except:
		    """ nothing """

	    args = map(struct[1], args)

	    try:
		struct[2](*args)
	    except:
		""" nothing """

	    return 1

    return 0

def exec_ext(cmd):

    for name, func in ext.iteritems():
	if name == cmd:
	    try:
		func(stack.stack)
	    except:
		print "Not able to execute this operation"

	    stack.last()
	    return 1

    print "Undefined operation", cmd
    return 0

def exec_(cmd, *args):
    if exec_cmd(cmd, *args):
	    """ nothing """
    elif exec_ext(cmd):
	    """ just skipping """

def main():

    scan = raw_input(">>> ")

    if scan == "":
        return 
		
    args = split_args(scan)

    for arg in args:
	if type(arg) is str:

            if arg == "":
                continue
            
	    try:
		x = float(arg)
		stack.stack.append(x)
	    except:
		exec_(arg)
	elif type(arg) is list:
	    exec_(arg[0], *arg[1:])


while(running):
    main()
