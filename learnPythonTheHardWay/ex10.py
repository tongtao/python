# -*- coding: utf-8 -*-

#What Was That
#ex10.py

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#%r prints it the way you'd write it in your file, 
#but %s prints it the way you'd like to see it
print "%r, %s" % ("\\\t\'", "\\\t\'")

#print 会自动在行末加上回车,
#如果不需回车,只需在print语句的结尾添加一个逗号
print "%s" % "1234567",

#（windows系统）\r 就是return 回到 本行 行首 这就会把这一行以前的输出 覆盖掉
#\n 是回车＋换行 把光标 先移到 行首 然后换到下一行 也就是 下一行的行首
while True:
	for i in ["/", "-", "|", "\\", "|"]:
		print "%s\r" % i,



"""
        I'm tabbed in.
I'm split
on a line.
I'm \ a \ cat.

I'll do a list:
        * Cat food
        * Fishies
        * Catnip
        * Grass
"""