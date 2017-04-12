# Learn-Python-The-Hard-Way

"""
一点一滴，夯实python基础。
总结错误，失败为成功之母。

宝剑锋从磨砺出，梅花香自苦寒来。

日积月累，千锤百炼

20170406

一、
1.pip list 显示所有安装好的包
2.命令下运行python和ipython都可以，但是只有python可以用ctrl+Z退出。
3.命令下mkdir表示创建当前目录下的文件夹，如 mkdir mystuff；cd 为转到目录下，如cd mystuff；查看路径为dir。
4.在命令里直接输入 g：就可以把目录转到g盘了。
5.powershell不是cmd，是可以打开的
6.搜索如果没了，可以通过在任务栏点右键调出来。
7.命令行里的回家操作是cd ~，注意中间有个空格。
8.pwd查看当前工作目录
9.cd .. 表示返回上级目录，可以连着返回，如 cd ../../../../..,其实cd后面不用空格。
10.列出所有目录的办法是 ls（LS），大写也行。powershell是不区分大小写的。

二、
1.rmdir是删除目录的命令，比如 rmdir stuff。rm是remove的缩写。
2.调整工作目录后，再键入 python ex1.py，python会运行在当前的工作目录上。
3.倒着从最后一行开始，逐个单词检查代码很有用。避免让大脑跟着每一段代码的意思走，可以精确处理每个片段，从而更容易发现代码的错误。
4.python里的‘%’是求余数的，别和‘/’除法混掉。
5.python2.7里，如果是除法时，只返回整数部分，如1/4，返回值是0.如果要计算正确，需要改成浮点数——方法是数字后面加“.”python3里已经改正过来了。
6.# -*- coding: utf-8 -*- 用于可写汉字。
7.注意在有引用时，加上“%”。#注意，在语句结束后，要在后面加上“%”，不加的话，后面无法引用。
print "If I add %d, %d, and %d I get %d." % （my_age, my_height,my_weight,my_age+my_height+my_weight)
8.装linux最好，底线是能跑起 ipython notebook。win-anaconda-notebook-skl
9.print后面加上‘，’再加另外一个print，会中间空一格而不是换行。
print end1 + end2 +end3 +end4+ end5+end6,
print end7 +end8+end9+end10+end11+end12 
cheese Burger
10.注意print后用逗号分隔开，即使是长句；此外，句子很长时，后面的括号不要忘了。
print formatter %(
    "I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight.",
)

20170407
一、
1.不可以用IDLE，应该学习使用命令行。命令行对学习编程很重要，而且是学习编程的绝佳初始环境。
2.%d 数字，%s 字符，%r内部调试
3.print后面加"""可以输入一个长段落。

20170408
一、
1.机器学习定义：以一组输入的训练集为输入，通过指定的模型，计算出模型所对应的最优组合，最优组合使得在这组组合给定的训练集下，这组参数在模型上表现最好。
#获取数据
train_x,train_y,test_x,test_y = getData()
#训练模型，并得出测试集的y
model = somemodel()
model.fit(train_x,train_y)
predictions = model.predict(test_x)
#打分，看预测集和实际值的对应情况。score成绩好，不一定回测成绩好。回测比score要复杂和严密很多。多数情况下，是否定模型的。
score = score_function(test_y,predictions)
2.降维，TSNE，把多维度降到低纬度。y不用降，直接就可以用，可以跑出来多个。Y值可以是任何是穷，不一定是股票的价格。
3.花的类型案例，150个点；手写数字识别，60000个点，mnist，深度学习的数据值之一，压缩到了8*8；
4.sklearn.datasets import make 可以自己造数据，满足某种分布，很方便的做实验的数据。
5.不能在训练集上进行训练集拟合。第4课，41分，讲解sklearn流程。
6.OLS最小二乘——到——高级线性模型
Regression Shrinkage and Selection via the Lasso
7.线性模型 y=x*$,$=(x*x)^x*y,分别去左乘就可以。回去看线性代数。


20170411
一、
1.在shell里运行python是用 python ex11.py
2.在while等条件运算里，True 和 False 的首字母应当大写。
3.注意\r 和%r的区别，前者是换行之类的，而后者是显示打印信息。
4.在print后面加 ， 是为了print不会输出换行符而跑到下一行。
5.raw_input() 表示后面可以输入的字符，比如 age = raw_input(）。raw_input(）和input()有区别，前者输入不用加引号，而input()后面输入必须加引号才行，所以一般就用raw_input()。本质上是，input（）是把输入的内容当成python代码来处理了。
6.避免使用%r来转义——有时会对符号产生影响，可以替换为%s。
7.查看函数作用时，用 pydoc raw_input。这里，pydoc是说明，raw_input不用加函数了。此外，这是在powershell里运行的，而不是在python里。
8.argv是从sys里引入的解包函数，需要在运行前赋值，比如：python ex13.py a b c。其中的script是文件名称，这里就是ex13.py
9.argv是在运行程序前就要输入的，而raw_input()是在运行后需要输入的。
10.在open（）函数中，一定要把格式写上。

二、
1.在命令里退出python可以用ctrl+z，也可以用quit（）命令。ctrl+c是干什么的？
2.python不限制多次打开同一个文件。
3.在打开文件的格式中，以某种方式打开，需要加''。比如，target = open（filename，'w'）.w应当在引号之中。
4.run,call,use对函数的操作是一样的。
5.在函数中，例如print_two(*args).这里的*表示把所有的输入变量都加到args的列表中去。

三、函数注意事项

写函数时的注意事项
1.函数定义是以  def 开始的吗？
2.函数名是以字符和下划线_组成的吗？
3.函数名是不是紧跟(？
4.括号里是否包含参数？参数是否以逗号隔开？
5.参数名称是否重复？不能使用重复的参数名。
6.紧跟着参数的是不是（)?）？
7.函数结束的未知是否取消了缩进？

运行函数时的注意事项
1.调用函数是否使用了函数名？
2.函数名是否紧跟(?
3.括号后是否有参数？多个参数是否以逗号隔开？
4.函数是否以）结尾？

四、
1.当该提示的字符不提示时，说明用的是中文输入法。此时标点符号不对，应当警觉。
2.注意函数的4个空格默认缩进有时会出问题。
3.多利用已有的函数名提示，可以有效的防止函数名的打印错误。还是要认真的提高注意力。
4.对于函数的定义，不行就用tab键吧，至少不会出现四个键提示的错误。
