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

# 单独处理list的每个元素
# map()是 Python 内置的高阶函数，它接收一个函数 f 和一个 list，并通过把函数 f 依次作用在 list 的每个元素上，得到一个新的 list 并返回。
def f(x):
    return x*x

print map(f, [1,2,3]) 
# [1, 4, 9] 不改变原有的 list，而是返回一个新的 list。
# map() 不仅仅可以处理只包含数值的 list，事实上它可以处理包含任意类型的 list，只要传入的函数f可以处理这种数据类型。

# Task: 假设用户输入的英文名字不规范，没有按照首字母大写，后续字母小写的规则，请利用map()函数，把一个list（包含若干不规范的英文名字）变成一个包含规范英文名字的list：
# Input:['adam', 'LISA', 'barT']    Output:['Adam', 'Lisa', 'Bart']
def format_name(s):
    return s[0].upper() + s[1:].lower()
    #return s.capitalize()
print map(format_name, ['adam', 'LISA', 'barT'])


# 2-5 reduce()函数

#   把list的元素合成处理
#   reduce()函数也是Python内置的一个高阶函数。reduce()函
#   数接收的参数和 map()类似，一个函数 f，一个list，但行为
#   和 map()不同，reduce()传入的函数 f 必须接收两个参数，
#   reduce()对list的每个元素反复调用函数f，并返回最终结果值。
#       res = f(list[0], list[1])->res = f(res,list[3]) ... 
#   reduce()还可以接收第3个可选参数，作为计算的初始值res。
#   即：res = f(res,list[0])->res = f(res,list[1])->res = f(res,list[2]) ... 遍历完得到最终的res
# Task: Python内置了求和函数sum()，但没有求积的函数，请利用recude()来求积：
# 输入：[2, 4, 5, 7, 12]   输出：2*4*5*7*12的结果
def prod(x, y):
    return x*y 
    
print reduce(prod, [2, 4, 5, 7, 12])
# 3360


# 2-6 filter()函数

#   过滤元素
#   filter()函数是 Python 内置的另一个有用的高阶函数，filter()
#   函数接收一个函数 f 和一个list，这个函数 f 的作用是对每个
#   元素进行判断，返回 True或 False，filter()根据判断结果自
#   动过滤掉不符合条件的元素，返回由符合条件元素组成的新list。

#   利用filter()，可以完成很多有用的功能，例如，删除 None 或者空字符串：
def is_not_empty(s):
    return s and len(s.strip()) > 0
print filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])
# ['test', 'str', 'END']

# Task: 请利用filter()过滤出1~100中平方根是整数的数，即结果应该是：
#       [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# import math
def is_sqr(x):  #判断方法！
    r = int(math.sqrt(x))
    return r*r==x
print filter(is_sqr, range(1, 101))


# 2-7 自定义排序函数

#   Python内置的 sorted()函数可对list进行排序：
print sorted([36, 5, 12, 9, 21])
#   [5, 9, 12, 21, 36]

#   sorted()也是一个高阶函数，它可以接收一个比较函数来实现自定义排序，
#   比较函数的定义是，传入两个待比较的元素 x, y，
#   如果 x 应该排在 y 的前面，返回 -1，
#   如果 x 应该排在 y 的后面，返回 1，
#   如果 x 和 y 相等，返回 0。

# 要实现倒序排序，只需要编写一个reversed_cmp函数：
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
print sorted([36, 5, 12, 9, 21], reversed_cmp)
# [36, 21, 12, 9, 5]

# sorted()也可以对字符串进行排序，字符串默认按照ASCII大小来比较：
print sorted(['bob', 'about', 'Zoo', 'Credit'])
# ['Credit', 'Zoo', 'about', 'bob']

# Task: 对字符串排序时，有时候忽略大小写排序更符合习惯。请利用sorted()高阶函数，实现忽略大小写排序的算法。
#   输入：['bob', 'about', 'Zoo', 'Credit']    输出：['about', 'bob', 'Credit', 'Zoo']
def cmp_ignore_case(s1, s2):
    tmpS1 = s1.lower()
    tmpS2 = s2.lower()
    
    if tmpS1 < tmpS2:
        return -1
    elif tmpS1 > tmpS2:
        return 1
    else:    
        return 0

print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)

# 2-8 返回函数

#   Python的函数不但可以返回int、str、list、dict等数据类型，还可以返回函数！

#   例如，定义一个函数 f()，我们让它返回一个函数 g，可以这样写：
def f():
    print 'call f()...'
    # 定义函数g:
    def g():
        print 'call g()...'
    # 返回函数g:
    return g
x=f()
# call f()...
print x
# <function g at 0x1037bf320>
x()
# call g()...

#   返回函数可以把一些计算延迟执行。例如，如果定义一个普通的求和函数：
#   def calc_sum(lst):
#       return sum(lst)
#   调用calc_sum()函数时，将立刻计算并得到结果
#   但是，如果返回一个函数，就可以“延迟计算”：
def calc_sum(lst):
    def lazy_sum():
        return sum(lst)
    return lazy_sum
f = calc_sum([1, 2, 3, 4])
print f
# <function lazy_sum at 0x016E7D30>
print f()
# 10
#   由于可以返回函数，我们在后续代码里就可以决定到底要不要调用该函数。

# Task:请编写一个函数calc_prod(lst)，它接收一个list，
#       返回一个函数，返回函数可以计算参数的乘积。
def calc_prod(lst):
    def cal_prod_delay():
        return reduce(prod, lst)
        # return reduce(lambda x, y : x * y, lst)
    return cal_prod_delay

f = calc_prod([1, 2, 3, 4])
print f()
# 24


# 2-9 闭包






