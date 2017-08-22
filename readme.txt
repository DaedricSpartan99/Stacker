|----------->>> Stacker <<<-------------|

Syntax:

>>> <n1> <n2> <func>(arg1, arg2, ..., argn)

Variables: 
Writing a number means to push it into the stack

Ex: >>> 5.8

Multiple numbers can be pushed writing only one
line 

Ex: >>> 5.8 7 3 5.8

Functions:
Functions are operations that act onto the stack of 
numbers

Ex:  >>> pop
Ex2: >>> pop()
Ex3: >>> top(3, 2)

Operations are functions called by a symbol:

- + 	: 	plus operator
- -	: 	minus operator
- *	: 	multiplication operator
- /	: 	division operator
- ** 	: 	power operator

Functions are dynamically writtable in a file .py
and placing it in ext/ directory

Built-in functions:

- exit		:  	quits the program

- help  	:  	prints this documentation

- pop(size = 1)	:	pops "size" arguments from the stack

- import(module) :	imports a module in ext/

- push		:	equal to write numbers

- ls		: 	prints all the stack content

- last		:	prints the last number of the stack

- top(pointer = 1, size = 1) : 	moves a pointed block to the top of the stack

