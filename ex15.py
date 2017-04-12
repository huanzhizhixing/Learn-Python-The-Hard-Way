# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv
#注意要把后面的格式类型写上
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"

#这里输入另外一个文件，可以再打开一个。
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()


