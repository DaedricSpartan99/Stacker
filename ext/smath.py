
def add(stack, *args):
    
    if len(stack) < 2:
        raise BufferError
    
    x = stack.pop()
    y = stack.pop()
    stack.append(x + y)

def minus(stack, *args):

    if len(stack) < 2:
        raise BufferError
    
    x = stack.pop()
    y = stack.pop()
    stack.append(y - x)

def mult(stack, *args):

    if len(stack) < 2:
        raise BufferError
    
    x = stack.pop()
    y = stack.pop()
    stack.append(x * y)

def div(stack, *args):

    if len(stack) < 2:
        raise BufferError
    
    x = stack.pop()
    y = stack.pop()
    stack.append(y / x)

def exp(stack, *args):

    if len(stack) < 2:
        raise BufferError
    
    x = stack.pop()
    y = stack.pop()
    stack.append(y**x)

def mod(stack):

    if len(stack) < 2:
        raise BufferError

    x = stack.pop()
    y = stack.pop()
    stack.append(y % x)
