# -*- coding: utf-8 -*-
formatter = "%r %r %r %r"
print formatter %(1,2,3,4)
print formatter %("one","two","three","four")
print formatter %(True,False,False,True)
print formatter %(formatter,formatter,formatter,formatter)
#注意print后用逗号分隔开，即使是长句；
#此外，句子很长时，后面的括号不要忘了。
print formatter %(
    "I had this thing.",#此处的逗号容易忘。
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight.",
	#后面括号容易忘
)

