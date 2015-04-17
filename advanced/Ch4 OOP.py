# -*- coding: utf-8 -*-


# 第四章 面向对象编程


# 4-1 面向对象编程


# 4-2 定义类并创建实例

#   在Python中，类通过 class 关键字定义。

#   按照 Python 的编程习惯，类名以大写字母开头，紧接着是(object)，
#   表示该类是从哪个类继承下来的。类的继承将在后面的章节讲解，
#   现在我们只需要简单地从object类继承。

class Person(object):
    pass
    
#   有了Person类的定义，就可以创建出具体的xiaoming、xiaohong等实例。
#   创建实例使用 类名+()，类似函数调用的形式创建：
xiaoming = Person()
xiaohong = Person()

# Task: 请练习定义Person类，并创建出两个实例，打印实例，再比较两个实例是否相等。

class People(object):
    name = "default"        # 这句多余了吧  不多余，只是一开始对其理解有问题，看4-6节
    def __init__(self, name):
        self.name = name
        
ming = People('ming')
hong = People('hong')

print ming.name
print hong
print ming == hong


# 4-3 创建实例属性

class People43(object):
    pass
    
p1 = People43()
p1.name = 'Bart'    # 为什么可以直接赋值？ 是因为object?

p2 = People43()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

L1 = [p1, p2, p3]
L2 = sorted(L1, lambda p1, p2: cmp(p1.name, p2.name))

print L2[0].name
print L2[1].name
print L2[2].name


# 4-4 初始化实例属性

#   我们可以自由地给一个实例绑定各种属性，如上节

#   在定义 Person 类时，可以为Person类添加一个特殊的__init__()方法，
#   当创建实例时，__init__()方法被自动调用，我们就能在此为每个实例都统一加上以下属性：
class Person44(object):
    def __init__(self, name, gender, birth):
        self.name = name        #不用额外定义name的语句
        self.gender = gender
        self.birth = birth
#   __init__() 方法的第一个参数必须是 self(勿忘)
#   后续参数则可以自由指定，和定义函数没有任何区别。

#   创建实例时，就必须要提供除 self 以外的参数：
xiaoming = Person44('Xiao Ming', 'Male', '1991-1-1')

#   有了__init__()方法，每个Person实例在创建时，都会有 name、gender 和 birth 这3个属性，
#   并且，被赋予不同的属性值，访问属性使用.操作符
print xiaoming.birth

#   要定义关键字参数，使用 **kw；
#   除了可以直接使用self.name = 'xxx'设置一个属性外，
#   还可以通过 setattr(self, 'name', 'xxx') 设置属性。

class Person44t(object):
    def __init__(self, name, gender, birth, **kw):
        self.name = name
        self.gender = gender
        self.birth = birth
        print kw
        for k, v in kw.iteritems():
            print k, v
            setattr(self, k, v)
            
xiaoming = Person44t('Xiao Ming', 'Male', '1990-1-1', job='Student', age=18)
print xiaoming.name
print xiaoming.job
# {'age': 18, 'job': 'Student'}
# age 18
# job Student
# Xiao Ming
# Student


# 4-5 访问控制

#   Python对属性权限的控制是通过属性名来实现的，
#   如果一个属性由双下划线开头(__)，该属性就无法被外部访问。
class Person45(object):
    def __init__(self, name):
        self.name = name
        self._title = 'Mr'
        self.__job = 'Student'
        
p = Person45('bob')

try:
    print p.__job
except:
    print 'error'
    
#   如果一个属性以"__xxx__"的形式定义，那它又可以被外部访问了，
#   以"__xxx__"定义的属性在Python的类中被称为特殊属性，有很多预定义的特殊属性可以使用，
#   通常我们不要把普通属性用"__xxx__"定义。
#   以单下划线开头的属性"_xxx"虽然也可以被外部访问，但是，按照习惯，他们不应该被外部访问。

class Person45t(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

pt = Person45t('Bob', 59)

print pt.name
try:
    print pt.__score
except:
    print 'error'
    
 
# 4-6 创建类属性

#   注意是类的属性，而不是实例的属性
print People.name   #注意  用类名调用
# default
#   实例属性每个实例各自拥有，互相独立，而类属性有且只有一份。

#   每个实例也可以访问所属类的属性
#   因为类属性只有一份，所以，当类的属性改变时，所有实例访问到的类属性都改变了。

# Task: 请给 Person 类添加一个类属性 count，每创建一个实例，count 属性就加 1，
#       这样就可以统计出一共创建了多少个 Person 的实例。

class Person46(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Person46.count += 1
        # 不应是self.count = self.count + 1

p1 = Person46('Bob')
print Person46.count

p2 = Person46('Alice')
print Person46.count

p3 = Person46('Tim')
print Person46.count


# 4-7 类属性和实例属性名字冲突怎么办

#   上边的People类正好遇到这个问题
#   访问实例p1.name时，优先查找实例属性，若没有，再返回类属性。
#   当实例属性和类属性重名时，实例属性优先级高，它将屏蔽掉对类属性的访问。

#   所以，千万不要在实例上修改类属性，它实际上并没有修改类属性，而是给实例绑定了一个实例属性。

# Task：请把上节的 Person 类属性 count 改为 __count，再试试能否从实例和类访问该属性。
class Person47(object):
    __count = 0
    def __init__(self, name):
        self.name = name
        Person47.__count += 1

p1 = Person47('Bob')
p2 = Person47('Alice')

# print Person47.__count
# print p1.__count
# 均不能访问


# 4-8 定义实例方法

#   虽然私有属性无法从外部访问，但是，从类的内部是可以访问的。
#   除了可以定义实例的属性外，还可以定义实例的方法。
#   实例的方法就是在类中定义的函数，它的第一个参数永远是 self，
#   指向调用该方法的实例本身，其他参数和一个普通函数是完全一样的

class Person48(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_grade(self):
        if self.__score >= 80:
            return 'A'
        if self.__score >= 60:
            return 'B'
        return 'C'

p1 = Person48('Bob', 90)
p2 = Person48('Alice', 65)
p3 = Person48('Tim', 48)

print p1.get_grade()
print p2.get_grade()
print p3.get_grade()


# 4-9 方法也是属性

#   在 class 中定义的实例方法其实也是属性，它实际上是一个函数对象
#   因为方法也是一个属性，所以，它也可以动态地添加到实例上，
#   只是需要用 types.MethodType() 把一个函数变为一个方法
class Person49(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.get_grade = lambda: 'A'
    def grade(self):
        return 'A'

p1 = Person49('Bob', 90)
print p1.get_grade
print p1.grade
print p1.get_grade()
# <function <lambda> at 0x01717FB0>
# <bound method Person49.grade of <__main__.Person49 object at 0x01807430>>
# A


# 4-10 定义类方法

#   和属性类似，方法也分实例方法和类方法。

#   在class中定义的全部是实例方法，实例方法第一个参数 self 是实例本身。

#   要在class中定义类方法，需要这么写：
class Person410(object):
    count = 0
    @classmethod
    def how_many(cls):
        return cls.count
    def __init__(self, name):
        self.name = name
        Person410.count = Person410.count + 1

print Person410.how_many()
p1 = Person410('Bob')
print Person410.how_many()

#   通过标记一个 @classmethod，该方法将绑定到 Person 类上，而非类的实例。
#   类方法的第一个参数将传入类本身，通常将参数名命名为 cls，
#   上面的 cls.count 实际上相当于 Person.count。

#   因为是在类上调用，而非实例上调用，因此类方法无法获得任何实例变量，只能获得类的引用。
