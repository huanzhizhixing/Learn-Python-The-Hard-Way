# -*- coding: utf-8 -*-

i = 0
numbers = []
numa = []
j=0
while i<len("happy"):
	print "At the top i is %d" % i
	numbers.append(i)
	
	i = i + 1
	print "Numbers now :" ,numbers
	print "At the bottom i is %d " % i
	while j < len ("good"):
		numa.append(j)
		j = j + 1
		print"numa now:" , numa
		print "At the bottom j is %d" % j
	
print "The numbers: "

for num in numbers:
	print num

