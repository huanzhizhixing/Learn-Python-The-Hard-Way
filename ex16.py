# -*- coding: utf-8 -*-

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL+C (^C)."
print "If you do want that, hit return."

raw_input("?")

print "Opening the file..."
#注意！里面的w应当是加上''的！否则就会当成变量看待。
target = open(filename,'w')

print "Truncating the file, goodbye!"
target.truncate()

print "Now I will ask you for three lines."

line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "I'm going to write this to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it"
target.close()



