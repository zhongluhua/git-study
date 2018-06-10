#--coding:utf-8---

# raw_input()用来获取控制台的输入，将所有输入作为字符串看待，返回字符串类型
# input()和raw_input()这两个函数均能接收字符串，但raw_input()直接读取控制台的输入（任何
# 类型的输入它都可以接收）。而对于input(),它希望能够读取一个合法的python表达式，即你输入字符
# 串的时候必须使用引号将它括起来，否则它会引发一个SyntaxError

print "how old are you?",
age = raw_input()
print "how tall are you ?",
height = raw_input()
print "how much do you weigh?",
weight = raw_input()
print "so,you're %r old,%r tall and %r heavy." % (age,height,weight)

print "----------使用input()函数----------\n"
print "how old are you?",
age = input()
print "how tall are you ?",
height = input()
print "how much do you weigh?",
wight = input()
print "so,you're %s old,%s tall and %s heavy." %(age,height,weight)
