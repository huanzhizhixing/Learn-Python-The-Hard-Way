# -*- coding: utf-8 -*-


"""

>>> stuff = ['a','b','c','d']
>>> print stuff[1]
b
>>> things[1] = 'z'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'things' is not defined
>>> stuff[1] = 'z'
>>> print stuff[1]
z
>>> print things
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'things' is not defined
>>> print stuff
['a', 'z', 'c', 'd']
>>> stuff = {'name':'zed','age':'36','height'='6*12+2'}
  File "<stdin>", line 1
    stuff = {'name':'zed','age':'36','height'='6*12+2'}
                                             ^
SyntaxError: invalid syntax
>>> stuff = {'name':'zed','age':'36','height':'6*12+2'}
>>> print stuff['name']
zed
>>> print stuff['age']
36
>>> print stuff['height']
6*12+2
>>> stuff['city']="San Francisco"
>>> print stuff['city']
San Francisco
>>> stuff[1] = "WoW"
>>> stuff[1]
'WoW'
>>> stuff[2]="Neato"
>>> print stuff[1]
WoW
>>> print stuff[2]
Neato
>>> print stuff
{'city': 'San Francisco', 2: 'Neato', 'name': 'zed', 1: 'WoW', 'age': '36', 'height': '6*12+2'}
>>> del stuff['city']
>>> del stuff['1']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: '1'
>>> del stuff[1]
>>> del stuff[2]
>>> stuff
{'name': 'zed', 'age': '36', 'height': '6*12+2'}
>>>


"""

#Create a mapping of state to abbreviation
states = {
	'Oregon': 'OR',
	'Florida': 'FL',
	'California':'CA',
	'New York':'NY',
	'Michigan':'MI',
}

#create a basic set of states and some cities in them
cities = {
	'CA':'San Francisco',
	'MI':'Detroit',
	'FL':'Jacksonville'
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#Print out some cities
print '-' * 10
print "NY state has: ", cities['NY']
print "OR state has: ", cities['OR']

#print some states
print '-' * 10 
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

#do it by using the state then cities dict
print '-' * 10
print "Michigan has :", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

#print every state abbreviation
print '-' * 10
#itens是什么函数？
for state, abbrev in states.items():
	print "%s is abbreviation %s " % (state,abbrev)
	
print '-' * 10
for abbrev, city in cities.items():
	print "%s has the city %s " % (abbrev, city)
	
#now do both at the same time
print '-' * 10 
for state, abbrev in states.items():
	print "%s state is abbreviated %s and has city %s " % (
		state, abbrev,cities[abbrev])
		
print '-' * 10
#safely get a abbreviation by state that might not be there
state = states.get('Texas',None)

#get a city with a default values
city = cities.get('TX','Does Not Exit')
print "The city for the state 'TX' is: %s" % city

