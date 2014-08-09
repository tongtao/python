# -*- coding: utf-8 -*-

#While Loops
#ex33.py

numbers = []
numbers2 = []

def print_number(n, inc):
	i = 0
	while i<n:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i + inc
		print "Numbers now:", numbers
		print "At the bottom i is %d" % i

print "The numbers:"

for num in numbers:
	print num
		
		
print_number(10, 2)

def print_number_v2(n, inc):
	for i in range(0, n, inc):
		print "At the top i is %d" % i
		numbers2.append(i)
		print "Numbers now:", numbers2

print_number_v2(10, 2)		
print "The numbers2:"

for num in numbers2:
	print num

print u"汉字"