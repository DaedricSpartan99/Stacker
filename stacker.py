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

# basic commands

cmds = {"exit" : exit_,
        "import" : import_,
        "push" : lambda *args: stack.push(*args),
        "ls" : lambda *args: stack.ls(),
        "last" : lambda *args: stack.last(),
        "pop" : lambda *args: stack.pop(args[0]) if len(args) > 0 else stack.pop(),
        "top" : lambda *args: stack.top(args[0], args[1]) if len(args) > 1 else stack.top(args[0]) if len(args) > 0 else stack.top() }

def main():

    scan = raw_input(">>> ")

    if scan == "":
        return 

    args = scan.split()
    cmd = args.pop(0)

    try:
        args = map(float, args)
    except:
        print "Float values only as arguments"
        return

    retval = 0

    for name, func in cmds.iteritems():
        if name == cmd:
            func(*args)
            return

    for name, func in ext.iteritems():
        if name == cmd:
            try:
                func(stack.stack, *args)
                stack.last()
            except:
                "Not able to execute this operation"
            break

# import standard math module

import_("smath")

while(running):
    main()
