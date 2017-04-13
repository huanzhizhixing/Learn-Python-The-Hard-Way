# -*- coding: utf-8 -*-

ten_things = "Apples Oranges Crows Telephone Light Suger "

print "Wait there's not 10 things in the list , Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10 :
	next_one = more_stuff.pop(0)
	print "Adding: ", next_one
	stuff.append(next_one)
	print "There's %d items now." % len(stuff)
	
print "There we go:", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]#whoa! fancy!
print stuff.pop()
print ' '.join(stuff) #what?cool!!
print '#'.join(stuff[3:5]) #super stellar!

#join函数的用法挺特别，是加到列表里面。
