# -*- coding: utf-8 -*-

#Functions Can Return Something
#ex21.py

def nadd(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b 

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	
print "Let's do some math with just functions"

age = nadd(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age:%d, Height:%d, Weight:%d, IQ:%d" % (age, height, weight, iq)

what = nadd(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes:",what,"Can you do it by hand?"
