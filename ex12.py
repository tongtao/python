# -*- coding: utf-8 -*-

#Prompting People
#ex12.py

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy," % (
	age, height, weight)

'''	
How old are you? 38
How tall are you? 6'2"
How much do you weigh? 180lbs
So, you're '38' old, '6\'2"' tall and '180lbs' heavy,
'''

'''
python -m pydoc raw_input (windows)
pydoc raw_input (linux)

Help on built-in function raw_input in module __builtin__:

raw_input(...)
    raw_input([prompt]) -> string

    Read a string from standard input.  The trailing newline is stripped.
    If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError.
    On Unix, GNU readline is used if enabled.  The prompt string, if given,
    is printed without a trailing newline before reading.
'''

'''
C:\Python27\testcode>python -m pydoc -p 7766
pydoc server ready at http://localhost:7766/
可以在浏览器中看到模块说明文档
'''