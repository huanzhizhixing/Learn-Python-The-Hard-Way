# -*- coding: utf-8 -*-

class Song(object):
	
	def __init__(self,lyrics,hahaha):
		self.lyrics = lyrics
		self.hahaha = hahaha
		
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
			
	def laugh(self):
		print self.hahaha
happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right there"],233)
					
bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"],666)
						

print"\n"						
happy_bday.sing_me_a_song()
print "\n"
bulls_on_parade.sing_me_a_song()
print "\n"

print happy_bday.hahaha
print bulls_on_parade.hahaha

happy_bday.laugh()
bulls_on_parade.laugh()

