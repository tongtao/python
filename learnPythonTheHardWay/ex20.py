# -*- coding: utf-8 -*-

#Functions and Files
#ex20.py

from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()

#seek(offset[, whence])
#whence argument is optional and defaults to 
		#os.SEEK_SET or 0 (absolute file positioning); 
		#other values are os.SEEK_CUR or 1 (seek relative to the current position) 
		#and os.SEEK_END or 2 (seek relative to the file’s end). 
		#There is no return value.
		#For example, f.seek(2, os.SEEK_CUR) advances the position by two 
		#and f.seek(-3, os.SEEK_END) sets the position to the third to last.
	
def rewind(f):
	f.seek(0)

def print_a_line(line_count, f):
	print line_count, f.readline()

current_file = open(input_file)

print "First let'print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)


