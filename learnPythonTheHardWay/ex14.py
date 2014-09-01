# -*- coding: utf-8 -*-

#Prompting and Passing
#ex14.py

from sys import argv

script, user_name = argv
prompt = '>'

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

"""
>python ex14.py zed
Hi zed, I'm the ex14.py script.
I'd like to ask you a few questions.
Do you like me zed?
>yes
Where do you live zed?
>china
What kind of computer do you have?
>orange

Alright, so you said 'yes' about liking me.
You live in 'china'. Not sure where that is.
And you have a 'orange' computer. Nice.
"""


