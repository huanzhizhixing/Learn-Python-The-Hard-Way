# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Coping form %s to %s." % (from_file,to_file)

#We could do this thing in one line too, how?
in_file = open(from_file)

#这里挺有意思，是先把infile打开，然后又通过read来赋值。
#或许写成
#indata = from_file.open.read()
#不行啊，没成功，问题出在哪里呢？
indata = in_file.read()

#indata = read(from_data)
#也不行。先往后做，接着看吧。

print "The input file is %s long." % len(indata)

print "Does the output file exist? %r " % exists(to_file)
print "Ready?Hit RETURN to continue, CTRL-c to abort."
raw_input()

out_file = open(to_file,'w')
out_file.write(indata)

print "Allright, all done."

out_file.close()
in_file.close()

#课后的cat命令是什么意思？


