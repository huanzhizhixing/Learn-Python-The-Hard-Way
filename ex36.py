# -*- coding: utf-8 -*-

#引入函数时不能加括号。
#应当为程序确认出去的门。

from sys import exit

def BeiJing():
	print "Welcome to DiDu! Now you can choose your job or go to another city."
	print "1.Play game with the government."
	print "2.Go to ShangHai."
	print "3.Try to do something big."
	print "4.IT."
	print "5.Buy House."
	print "6.Fight with WuMai."
	print "7.Go to Shenzhen."
	
	bj = raw_input("> ")
	
	if bj == "1" :
		print "You are too young too simple, sometimes naive. You lost everything."
	elif bj == "2" :
		ShangHai()
	elif bj == "3":
		print "It is hard to do something for young people in this environment."
	elif bj == "4":
		print "This job is for young guys who has a dream.Good Job!"
	elif bj =="5":
		print "You become a slave to the house.It goes up and down.Future, Who knows?"
	elif bj =="6":
		print "You are really a hero! But, why not go to other place?"
		start()
	elif bj == "7":
		ShenZhen()
	else:
		print "I don't know what you are saying."
		start()
		
def ShangHai():
	print "Welcome to MoDu! Now ,what will you do?"
	print "1.Be a trader of finance."
	print "2.Trade with other country."
	print "3.Find outer places in the inside of ChangSanJiao."
	print "4.Go to Beijing."
	print "5.Go to Shenzhen."

	
	sh = raw_input("> ")
	
	if sh == "1":
		print "It is a funny job, but needs hard work."
		exit(0)
	elif sh == "2":
		print "Shanghai is really good for trading, good job!"
		exit(0)
	elif sh == "3":
		print "Its inside is really funny and a lot of chances,good job!"
		exit(0)
	elif sh == "4":
		BeiJing()
	elif sh == "5":
		ShenZhen()
	else:
		print "I don't know what you are saying.Do you want to go other city?"
		start()
		
def ShenZhen():
	print "Welcome to ZhaiDu! Here are many young people. What are you going to do?"
	print "1.Be a coder."
	print "2.Go to HongKong."
	print "3.Join the finance and be a quant."
	print "4.Buy a house."
	print "5.Go to BeiJing."
	print "6.Go to ShangHai."
	
	sz = raw_input("> ")
	
	if sz == "1":
		print "Good job! You will find many friends here!"
		exit(0)
	elif sz == "2":
		print "You don't have passport and go back."
		shenzhen()
	elif sz == "3":
		print "Are you sure to find a job of finance? Quant is hard, learn python first."
		exit(0)
	elif sz == "4":
		print "It is too high now, you do not have enough money.Then you choose other city."
		start()
	elif sz == "5":
		BeiJing()
	elif sz == "6":
		ShangHai()
	else:
		print "I don't know what you are saying."
		start()	

def start():
	print "Which city do you want to live?"
	print "1.BeiJing."
	print "2.ShangHai."
	print "3.ShenZhen."
	
	st = raw_input("> ")
	
	if st == "1":
		BeiJing()
	elif st == "2":
		ShangHai()
	elif st == "3":
		ShenZhen()
	else:
		print "You must choose a city!"
		start()


start()


