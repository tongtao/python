# -*- coding: utf-8 -*-

#Reading File
#ex15.py

from sys import argv

script, filename = argv

txt = open(filename)

print "Here is your file %r." % filename
print txt.read(10)
print txt.read()

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()

txt.close()
txt_again.close()

"""
>python ex15.py ex15_sample.txt
Here is your file 'ex15_sample.txt'.
This is st               #读10个字节
uff I typed into a file.   #从第11个字节开始读
It is really cool stuff.
Lots and lots of fun to have in here.
Type the filename again:
>ex1.py
# -*- coding: utf-8 -*-

# A Good First Program
#ex1.py


print "Hello World!"
print "Hello Again"
print "I like typing this"
print "this is fun"
print "Yay! Printing."
print "I'd much rathher you 'not'."
print 'I "said" do not touch this.'
"""