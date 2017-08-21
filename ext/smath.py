
def add(stack, *args):
    x = stack.pop()
    y = stack.pop()
    stack.append(x + y)

def minus(stack, *args):
    x = stack.pop()
    y = stack.pop()
    stack.append(y - x)

def mult(stack, *args):
    x = stack.pop()
    y = stack.pop()
    stack.append(x * y)

def div(stack, *args):
    x = stack.pop()
    y = stack.pop()
    stack.append(y / x)
