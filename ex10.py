# -*- coding: utf-8 -*-

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food 
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
 
 
#ture应该改为True
#发现会一直转动的一个图标。根本停不下来，尝试ctrl+z也不行。
#于是就把powershell关闭了。
while True:
  for i in ["/","-","|","\\",""]:
    print "%s\r" % i,
    

