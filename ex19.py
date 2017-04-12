# -*- coding: utf-8 -*-

#输入两个变量
def cheese_and_crackers(cheese_count, boxes_of_crackers):
#第一个变量
    print "You have %d cheeses!" % cheese_count
	#第二个变量
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanker.\n"
	
print "We can just give the function numbers directly:"
#直接输入数
cheese_and_crackers(20,30)

print "OR, we can use variables from our stript:"
#由形参来做
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
#函数内四则运算
cheese_and_crackers(10 + 20 , 5 + 6)

#形参和实参一起来
print "And we can comine the two ,variables and math:"
#当该提示的字符不提示时，说明用的是中文输入法。此时标点符号不对，应当警觉。
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers +1000)

