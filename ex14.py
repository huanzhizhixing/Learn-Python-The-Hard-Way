# -*- coding: utf-8 -*-

from sys import argv

script, user_name = argv
#发现prompt不能输入中文
prompt = 'put in '

#发现这里的输入也不能录入中文。
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "How old are you?"
age = raw_input(prompt)

print"""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer .
And you are %r year old. Nice.
""" % (likes, lives,computer,age)






















