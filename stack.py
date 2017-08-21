
stack = []

def push(*varargs):
    for var in varargs:
        stack.append(var)

def last():
    ind = len(stack) - 1
    if ind > -1:
        print stack[ind]

def show():
    for x in stack:
        print x

def pop(size = 1):
    if len(stack) == 0:
        return []
    res = []
    for i in range(size):
        res.append(stack.pop())
    return res

def top(ptr = 1, size = 1):

    if len(stack) == 0:
        return

    #length = len(stack)
    ptr = length() - 1 - ptr
    
    #if ptr < 0 or size < 0 or (ptr + size) >= length:
        #return

    for i in range(size):
        x = stack.pop(ptr)
        stack.append(x)
    
    
