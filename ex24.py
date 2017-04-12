# -*- coding: utf-8 -*-

print "Let's practisce everything."
print 'You \'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\t the lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "---------------------"
print poem
print "----------------------"

five = 10 - 2 + 3 -6
print "This should be five: %s " % five

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 500
	crates = jars /100
	return jelly_beans, jars , crates
	
start_point = 10000
beans, jars, crates = secret_formula(start_point)
print "With a start_point of : %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans,jars,crates)

start_point = start_point/10

print "We can also do that this way."
print "We'd have %d beans, %d jars,and %d crates." % secret_formula(start_point)

"""
容易犯的错误：
1.打印错误
2.定义函数不加 ：
3.多利用已有的函数名提示，可以有效的防止函数名的打印错误。还是要认真的提高注意力。
4.对于函数的定义，不行就用tab键吧，至少不会出现四个键提示的错误。
"""


