# -*- coding: utf-8 -*-

my_name = 'Zed A. Shaw'
my_age = 35
my_height = 74
my_weight = 180
my_eyes = "Blue"
my_teeth = "White"
my_hair = "Brown"

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are ususlly %s depending on the coffee." % my_teeth

# This line is tricky, try to get it exactly right
#注意，在语句结束后，要在后面加上“%”，不加的话，后面无法引用。
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height,my_weight,my_age+my_height+my_weight)
	
# -*- coding: utf-8 -*-

name = 'Zed A. Shaw'
age = 35
height = 74
weight = 180
eyes = "Blue"
teeth = "White"
hair = "Brown"

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are ususlly %s depending on the coffee." % teeth

# This line is tricky, try to get it exactly right
#注意，在语句结束后，要在后面加上“%”，不加的话，后面无法引用。
print "If I add %d, %d, and %d I get %d." % (
    age, height,weight,age+height+weight)
	
# -*- coding: utf-8 -*-

name = 'Zed A. Shaw'
age = 35
height = 74
weight = 180
eyes = "Blue"
teeth = "White"
hair = "Brown"

print "Let's talk about %r." % name
print "He's %r inches tall." % height
print "He's %r pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %r eyes and %r hair." % (eyes, hair)
print "His teeth are ususlly %r depending on the coffee." % teeth

# This line is tricky, try to get it exactly right
#注意，在语句结束后，要在后面加上“%”，不加的话，后面无法引用。
print "If I add %r, %r, and %r I get %r." % (
    age, height,weight,age+height+weight)
	




