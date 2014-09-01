# -*- coding: utf-8 -*-

#Parameters, Unpacking, Variables
#ex13.py

from sys import argv

#Take whatever is in argv, unpack it, 
#and assign it to all of these variables on the left in order
# the command line arguments  come in as strings, 
# even if you typed numbers on the command line. 
# Use int() to convert them just like with int(raw_input())
script, first, second, third = argv

print "The script is called", script
print "Your first variable is", first
print "Your second variable is", second
print "Your third variable is", third

'''
>python ex13.py first 2nd 3rd
The script is called ex13.py
Your first variable is first
Your second variable is 2nd
Your third variable is 3rd

>python ex13.py first 2nd
Traceback (most recent call last):
  File "ex13.py", line 3, in <module>
    script, first, second, third = argv
ValueError: need more than 3 values to unpack
'''