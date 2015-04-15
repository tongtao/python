# -*- coding: utf-8 -*-

# 第二章 函数式编程

# 2-1 函数式编程简介

#     Python不是纯函数式编程：允许有变量
#     支持高阶函数：函数也可以作为变量传入
#     支持闭包：有了闭包就能返回函数
#     有限度的支持匿名函数

# 2-2 高阶函数

#     变量可以指向函数
print abs(-10)
print abs
f = abs
print f(-20)

#     函数名其实就是指向函数的变量
bakup = abs
abs = len
print abs([1, 2, 3])

abs = bakup

#     高阶函数：能接收函数做参数的函数
#       变量可以指向函数
#       函数的参数可以接收变量
#       一个函数可以接收另一个函数作为参数
#       DEMO:接收abs的函数       
#           定义一个函数，接受x,y,f三个参数，其中x,y是数值，f是函数
def add(x, y, f):
    return f(x) + f(y)

print add(-5, 9, abs)
# 14

# 2-3 把函数作为参数

#   利用add(x,y,f)函数，计算：x开二次方+y开二次方
import math
print add(25, 9, math.sqrt)
# 8.0

# 2-4 map()函数

# map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。
def f(x):
    return x*x

print map(f, [1,2,3]) 
# [1, 4, 9] 不改变原有的 list，而是返回一个新的 list。
# map() 不仅仅可以处理只包含数值的 list，事实上它可以处理包含任意类型的 list，只要传入的函数f可以处理这种数据类型。
