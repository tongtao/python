# -*- coding: utf-8 -*-

#Loops and lists
#ex32.py

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'orangs', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quaters']

#this first kind if for-loop goes though a list
for number in the_count:
	print "this is count %d" % number
	
#same as above
for fruit in fruits:
	print "A fruit of type:%s" % fruit
	
#also we can go through mixed lists too
#notice we have to use %r since we don't konw what's in it
for i in change:
	print "I got %r" % i

#we can also bulid lists, first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0, 6):
	print "Adding %d to the list." % i
	#append is a function that lists understand
	elements.append(i)
	
#now we can print them out too
for i in elements:
	print "Elememt was:%d" % i