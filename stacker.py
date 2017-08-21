#!/usr/bin/env python

import os, sys
lib_path = os.path.abspath(os.path.join('ext'))
sys.path.append(lib_path)

import stack

ext = {}
running = 1

# commands functions

def exit_(*args):
    global running
    running = 0

def import_(*args):
    
    if len(args) < 1:
        return

    global ext

    try:
        __import__(args[0])
        imp = sys.modules[args[0]]
    except KeyError:
        print "Imported module", args[0], "doesn't exist"
        return
        
    vars_ = dir(imp)

    for var in vars_:
        func = getattr(imp, var)
        if callable(func):
            ext[var] = func

# varargs resolvers

def push_(*args):
    if len(args) > 0:
        stack.push(*args)

def last_(*args):
    stack.last()

def show_(*args):
    stack.show()

def pop_(*args):
    if len(args) > 0:
        stack.pop(args[0])

def top_(*args):
    if len(args) > 1:
        stack.top(args[0], args[1])

# basic commands

cmds = {"exit" : exit_,
        "import" : import_,
        "push" : push_,
        "show" : show_,
        "last" : last_,
        "pop" : pop_,
        "top" : top_}

def main():

    try:
        scan = raw_input(">>> ")
    except:
        print "Something wrong on input"

    if scan == "":
        return 

    args = scan.split()
    cmd = args.pop(0)

    try:
        args = map(float, args)
    except:
        print "Float values only as arguments"

    retval = 0

    for name, func in cmds.iteritems():
        if name == cmd:
            func(*args)
            return

    for name, func in ext.iteritems():
        if name == cmd:
            try:
                func(stack.stack, *args)
            except:
                "Not able to execute this operation"
            break

# import standard math module

import_("smath")

while(running):
    main()
