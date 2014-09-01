# -*- coding: utf-8 -*-

#Printing,Printing
#ex8.py

#You should use %s and only use %r for getting debugging information about something.
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")

print formatter % (True, False, False, True)
print formatter % ("True", "False", "False", "True")

print formatter % (formatter, formatter, formatter, formatter)

print formatter % (
		"I had this thing.",
		"That you could type up right.",
		"But it didn't sing.",
		"So I said goodnight."
)

"""
1 2 3 4
'one' 'two' 'three' 'four'
True False False True
'True' 'False' 'False' 'True'
'%r %r %r %r' '%r %r %r %r' '%r %r %r %r' '%r %r %r %r'
'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'
"""
