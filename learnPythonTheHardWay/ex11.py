# -*- coding: utf-8 -*-

#Asking Question
#ex11.py

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you are %r old, %r tall and %r heavy." % (age, height, weight)

#input()函数支持用户输入数字或者表达式,不支持输入字符串.返回的是数字类型的数值.
#raw_input()函数捕获的是用户的原始输入,返回为字符串.
			#如果需要用输入的数字计算,则需要使用int()函数转换一下.
var1 = input("var1:")
var2 = raw_input("var2:")	
print "var1 =",var1
print "var2 =",var2
print "var1 = %r, var2 = %r" % (var1, var2)

'''
How old are you? 38
How tall are you? 6'2"
How much do you weigh? 180lbs
So, you are '38' old, '6\'2"' tall and '180lbs' heavy.
var1:1+2
var2:1+2
var1 = 3
var2 = 1+2
var1 = 3, var2 = '1+2'
'''