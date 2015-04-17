# -*- coding: utf-8 -*-


# 第四章 类的继承


# 5-1 什么是继承


# 5-2 继承了一个类

#   已经定义了Person类，需要定义新的Student和Teacher类时，可以直接从Person类继承
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        
#   定义Student类时，只需要把额外的属性加上，例如score：
class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score       
        
#   一定要用 super(Student, self).__init__(name, gender) 去初始化父类，
#   否则，继承自 Person 的 Student 将没有 name 和 gender。

#   函数super(Student, self)将返回当前类继承的父类，即 Person ，
#   然后调用__init__()方法，注意self参数已在super()中传入，
#   在__init__()中将隐式传递，不需要写出（也不能写）。


# 5-3 判断类型

#   函数isinstance()可以判断一个变量的类型，既可以用在Python内置的数据类型如str、list、dict，
#   也可以用在我们自定义的类，它们本质上都是数据类型。
s = Student('Bob', 'Male', 88)

print isinstance(s, Person)
print isinstance(s, Student)
# True
# True
