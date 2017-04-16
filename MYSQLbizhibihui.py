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
