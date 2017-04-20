# Learn-Python-The-Hard-Way + 利用python进行数据分析 + mysql必知必会
# LPTHW标注为ex，数据分析标注为sj
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

五、
1.发现github的排序不人性化，1后面是11，下次再建项目时，用01、02、03这样。
2.没有找到改项目名称的地方。后续挖掘
3.没有找到编辑备注的地方。后续挖掘



mysql必知必会20170416
一、
1.重要内容 select from where group by having, order by limit.
2.like,union,视图、储存过程，游标，触发器，
3.连接 mysql， mysql -uroot -p
4.SHOW DATABASES； 显示现有的数据库，SHOW TABLES;显示在某一个库中的表。
5.用USE text 就能进入到数据库里面了。使用数据库 USE crashcourse；只有先打开数据库，才能读取里面的数据。
6.命令需要按 ；或者\g结束，不仅是enter。输入quit和exit能够退出命令行实用程序。
7.SHOW COLUMNS FROM customers；要求返回一个表名（表的基本信息，并非表里的内容。）
8.SHOW GRANTS;显示用户的权限。
9.select……from……；
10.where……in……

二、
1.通配符过滤：like，
2.Concat（）函数能够实现两个列之间的拼接。AS可以实现别名。
SELECT Concat（RTrim（vend_name),‘（‘，Rtrim（vend_country），’）’） AS vend_title
FROM vendors
ORDER BY vend_name
3.MYSQL的时间格式必须是 yyyy-mm-dd。如果使用日期，就用Date（）；时间就用Time（）。
4.某一特定年和月，用Year（）和Month（）来确定。
5.聚集函数，AVG(),返回某列平均值；COUNT(),返回某列行数；MAX(),返回某列最大值，MIN(),返回某列最小值，SUM()，返回某列值之和。
6. SELECT AVG(prod_price) AS avg_price FROM products;
7. GROUP BY vend_id;按照vend_id来实施分组。
8.联结，把两个表按照相同的名称连接起来。
SELECT vend_name,prod_name，prod_price
FROM vendors，products
WHERE vendors.vend.id = products.vend_id
ORDER BY vend_name, prod_name;
联结时，实际上是将第一个表中的每一行和第二个表中的每一行配对。WHERE子句作为过滤条件，它只包含哪些匹配给定条件（这里是联结条件）的行。WHERE子句，第一个表中的每个行将与第二个表中的每个行配对，而不管它们逻辑上是否可以配在一起。
9.自联结
SELECT p1.prod_id,p1.prod_name
FROM products AS p1,products AS p2
WHERE p1.vend_id = p2.vend_id
  AND p2.prod_id = 'DTNTR';
同一个表内连接，DTNTR找到同一个厂商的其他产品。
10.外部联结——能够包含没有关联行的数据。
比如有的人没有订购产品，也得在表中体现出来。
SELECT customers.cust_id,order.order_num
FROM customers INNER JOIN orders
 ON customers.cust_id = orders.cust_id
上面是内部连接

外部联结
SELECT customers.cust_id,order.order_num
FROM customers LEFT OUTER JOIN orders
 ON customers.cust_id = orders.cust_id
以左边的为目录，来建立联结。以右边为目录时，是RIGHT。

三、
1.如果是连接，就不用WHERE来表示了，用ON来表示。
2.UNION可以把多个SELECT语句合成一个结果集。如果有ORDER BY，那最后一个起作用。
3.全文搜索可以用LIKE(),也可以用 Match()   Against()
SELECT note_text
FROM productnotes
WHERE Match(note_text) Against('rabbit');
用where的话只给有rabbit的行，如果在select里面，则给出所有的行。
4.布尔文本搜索
SELECT note_text
FROM productnotes
WHERE Match(note_text) Against('heavy'IN BOOLEAN MODE);
5.搜索时，忽略词中的单引号。例如，don't，所因为dont
6.插入数值。INSERT INTO customers(……） VALUES(……）
7.更新数据，UPDATE。注意，随后是 E 不是A. UPDATE ……SET……
更新某一个数据 
UPDATE customers
SET cust_email = 'elmer@fudd.com'
WHERE cust_id = 10005;
8.删除数据
DELETE FROM customers
WHERE cust_id = 10006;
9.创建表 
CREATE TABLE,新标的名字，在关键字CREATE TABLE 之后给出
mysql> CREATE TABLE mystuff
    -> (
    ->  cust_id      int   NOT NULL   AUTO_INCREMENT,
    ->  cust_name    char(50)  NOT NULL,
    ->  PRIMARY KEY(cust_id)
    -> )ENGINE=InnoDB;
Query OK, 0 rows affected (0.04 sec)
可以给定两个主键，如 PRIMARY KEY (order_num，order_item）
10.MYSQL可以有多个引擎，InnoDB是事务处理引擎，不支持全文搜索。
M有ISAM是性能高的引擎，支持全文本搜索，但是不支持事务处理。事务处理是全都执行或者全都不执行，更稳定一些。因此，一般来说，用InnoDB更适合。

四、

1.更新表：ALTER TABLE，使得表结构改变。这个会常用，比如金融数据里用机器学习时会添加新的列。
ALTER TABLE vendors
ADD vend_phone CHAR(20)
添加一个叫vend_phone的列，并给出了数据类型。

2.ALTER TABLE来定义外键。
ALTER TABLE orderitems
ADD CONSTRAINT fk_orderitems_orders
FOREIGN KEY(order_num) REFERENCES orders (order_num)

3.删除表 DROP TABLE customers2；
4.重命名表 RENAME TABLE customers2 TO customers;
5.视图：虚拟的表，只包含使用时动态检索数据的索引。可以很好的利用重复SQL语句。
6.CREATE VIEW,创建视图；SHOW CREATE VIEW viewname，查看创建视图语句；DROP删除试图，DROP VIEW viewname；更新视图时，可以直接用CREATE OR REPLACE VIEW 来。
7.视图可以用来简化复杂的联结。
8.存储过程，利用多条SQL语句封装。可以接受输入和输出变量。
CALL productpricing(@pricelow,@pricehigh,@priceaverage);
9.创建存储过程
CREATE PROCEDURE productpricing()
BEGIN
   SELECT Avg(prod_price) AS priceaverage
   FROM products;(这里有一个分号)
END;（这里也有一个分号）
10.所有MYSQL变量都必须以@开始，传递到mysql的存储过程中的参数个数必须严格相等。显示参数可以用 select来，eg：select @pricehigh

五、
1.检查存储过程用 SHOW CREATE PROCEDURE
2.游标：游标是一个存储在MYSQL服务器上的数据库查询，它不是一条SELECT语句，而死被该语句检索出来的结果集。在存储了游标之后，应用程序可以根据需要滚动或浏览器中的数据。
3.创建游标
CREATE PROCEDURE processorders()
BEGIN
    DECLARE ordernumbers CURSOR
    FOR
    SELECT order_num FROM orders;
END;
4.打开游标 OPEN CURSOR
5.触发器，是mysql相应DELETE\INSERT\UPDATE语句时自动执行的一条MYSQL语句。使用触发器，把更改（如果需要，甚至还有之前和之后的状态）记录到另一个表非常容易。
6.事务处理：transaction processing.t事务ransaction,一组SQL语句；回退（rollback）撤销指定SQL语句过程；提交（commit）将未存储的SQL语句结果写入数据库表；保留点（savepoint）事务处理中设置的临时占位符（placeholder），可以对它发布回退。
7.每个保留点都有唯一的名字，eg：SAVEPOINT delete1；，ROLLBACK TO delete1；
8.在工作中不要随意使用root，应该创建一系列的帐号，有的用于管理，有的供用户使用，有的供开发人员使用。
9.创建用户。CREATE USER ben IDENTIFIED BY 'p@$$w0rd';显示用户权限，SHOW GRANTS FOR ben；授予搜索权限：GRANT SELECT ON text.* TO ben;更改用户密码; SET PASSWORD FOR ben = Password('n3w p@$$w0rd');
10.备份数据 命令行 mysqldump转储。

六、
1.维护：ANALYZE TABLE;诊断启动服务；查看日志文件；
2.改善性能，存储过程比一条一条执行的快；select用union语句代替；用FULLTEXT而不是LIKE;



