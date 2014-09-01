# -*- coding: utf-8 -*-

#More Variables And Printing
#ex5.py

my_name = 'Xed A. Shaw'
my_age =  35
my_height_inches = 74
my_height_cm = my_height_inches * 2.54

my_weight_lbs = 180
my_weight_kg = my_weight_lbs * 0.4532
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches (%.3f cm) tall." % (my_height_inches, my_height_cm)
print "He's %d pounds (%.3f kg) heavy." % (my_weight_lbs, my_weight_kg)
print "Actually that is not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height_inches, 
	my_weight_lbs, my_age + my_height_inches + my_weight_lbs)
	
print " %%r my_name=%r, my_age=%r." % (my_name, my_age)
	
# %% 百分号标记 
# %c 字符及其ASCII码 
# %s 字符串 
# %d 有符号整数(十进制) 
# %u 无符号整数(十进制) 
# %o 无符号整数(八进制) 
# %x 无符号整数(十六进制) 
# %X 无符号整数(十六进制大写字符) 
# %e 浮点数字(科学计数法) 
# %E 浮点数字(科学计数法，用E代替e) 
# %f 浮点数字(用小数点符号) 
# %g 浮点数字(根据值的大小采用%e或%f) 
# %G 浮点数字(类似于%g) 
# %p 指针(用十六进制打印值的内存地址) 
# %n 存储输出字符的数量放进参数列表的下一个变量中 
