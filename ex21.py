# -*- coding: utf-8 -*-

def add(a,b):#这里的冒号经常丢
    print "Adding %d +%d " % (a,b)
	#缩进出现错误。这里好多次了，总是改一下就行，不知怎么回事。以后试试tab
    return a + b
	
def subtruct(a,b):
    print "Subtructing %d - %d" % (a,b)
    return a - b  
	#这个函数一方面是赋值，另一方面是打印！实现了两个功能！

def multiply(a,b):
    print "Multiply %d * %d" % (a,b)
    return a * b
	
def  divide(a,b):
#这里的d前面多打了个乘号。
    print "Dividing %d /%d" %(a,b)
    return a /b
	
print "Let's do some math with just functins!"

age = add(30,5)
#subtruct打成了subtract
height = subtruct(78,4)
#weight的打印错误。
weight = multiply(90,2)
iq = divide(100,2)

print "Age: %d, Subtructing: %d, Multipyl: %d, Dividing: %d." % (age,height,weight,iq)

#A puzzle for the extra credit,type it in anyway.
print "Here is a puzzle."

what = add(age, subtruct(height,multiply(weight,divide(iq,2))))
#subtruct的打印错误。

print "That becomes: ", what, "Can you do it by hand?"


