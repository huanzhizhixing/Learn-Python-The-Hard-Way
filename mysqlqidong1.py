mysql接入成功
之前安装mysql后总是连接不上，启动不成功。
今晚终于解决了。方案如下：
1.点击右键以管理员身份运行cmd。
2.输入mysqld --install
3.找到mysql下的my.ini文件，在[mysqld]下添加#skip-grant-tables
4.重启mysql，我的电脑，右键，高级，服务，把mysql关掉后再启动。
5.？或者用net start mysql？
6.输入 mysql -uroot -p
7.提示输入密码，输入密码即可

C:\Windows\system32>mysqld --install
Service successfully installed.

C:\Windows\system32>mysql
ERROR 1045 (28000): Access denied for user 'ODBC'@'localhost' (using password: NO)

C:\Windows\system32>net start mysql
MySQL 服务正在启动 .
MySQL 服务无法启动。

服务没有报告任何错误。

请键入 NET HELPMSG 3534 以获得更多的帮助。


C:\Windows\system32>use mysql
'use' 不是内部或外部命令，也不是可运行的程序
或批处理文件。

C:\Windows\system32>mysql -u root mysql
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: NO)

C:\Windows\system32>/etc/init.d/mysqld stop
系统找不到指定的路径。

C:\Windows\system32>mysql
ERROR 1045 (28000): Access denied for user 'ODBC'@'localhost' (using password: NO)

C:\Windows\system32>mysql
ERROR 1045 (28000): Access denied for user 'ODBC'@'localhost' (using password: NO)

C:\Windows\system32>mysql -u root
ERROR 1045 (28000): Access denied for user 'root'@'localhost' (using password: NO)

C:\Windows\system32>mysql -uroot -p
Enter password: ********
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 6
Server version: 5.7.17-log MySQL Community Server (GPL)

Copyright (c) 2000, 2016, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
