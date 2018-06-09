# --coding:utf-8--

# my_name = 'Zed A. Shaw'
# my_age = 35 # not a lie
# my_height = 74 # inches
# my_weight = 180 # lbs
# my_eyes = 'Blue'
# my_teeth = 'White'
# my_hair = 'Brown'

# print "let's talk about %s." % my_name
# print "he's %d inches tall." % my_height
# print "he's %d pounds heavy." % my_weight
# print "actully that's not too heavy"
# print "he's got %s eyes and %s hair." % (my_eyes,my_hair)
# print "his teeth are usually %s depending on the coffee." % my_teeth

#this line is tricky,try to get it exactly right
# print "if I add %d,%d,and %d I get %d." % (my_age,my_height,my_weight,my_age + my_height + my_weight)

name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'white'
hair = 'Brown'

print "let's talk about %s." % name
print "he's %d inches tall." % height
print "he's %d pounds heavy." % weight
print "actully that's not too heavy"
print "he's got %s eyes and %s hair." % (eyes,hair)
print "his teeth are usually %s depending on the coffee." % teeth

print "if I add %d,%d,and %d I get %d" % (age,height,weight,age+height+weight)

print "----------以下是python格式化符号的笔记和练习题-----------------"
# pyhon格式化字符串
# %% 百分号标记，就是输出一个％
# %s 字符串,调用str函数打印字符串，str函数返回原始字符串
# %r 字符串，调用rper函数打印字符串，repr函数返回的字符串是加上了转义序列，是直接书写的字符串的形式
# %d 有符号整数（十进制）
# %u 无符号整数（十进制）
# %o 无符号整数（八进制）
# %x 无符号整数（十六进制）
# %X 无符号整数（十六进制，大写字符）
# %e 浮点数字（科学计数法）
# %E 浮点数字（科学计数法，用E代替e）
# %f 浮点数字（用小数点符号）
# %g 浮点数字（根据值的大小采用％e或％f）
# %G 浮点数字（类似于％g）
# %p 指针（用十六进制打印值的内存地址）
# %n 存储输出字符的数量放进参数列表的下一个变量中

# ％格式化字符也可用于字典，可用%(name)引用字典中的元素进行格式化输出。

year = 2018
month = 6
day = 9
#格式化日期， ％02d数字转换成两位整型，缺位填0
print "今天是%04d-%02d-%02d"%(year,month,day)


fvalue = 8.126
#保留宽度为6的2位小数浮点型
print '保留宽度为6的2位小数浮点型,8.123输出为%06.2f'%fvalue

value1 = 10
value2 = 1.2888
#输出十进制
print '%d'%value1
#输出八进制
print '%o'%value1
#输出两位十六进制，字母小写空缺补零
print '%02x'%value1
#输出四位十六进制，字母大写空缺补零
print '%04X'%value1
#以科学计数法输出浮点型，保留2位小数
print '%.2e'%value2


#格式化操作符辅助指令
# *定义宽度活着小数点京都
# -用做左对齐
# +在整数前面显示加号
# <sp>在整数前面显示空格
# #在八进制数前面显示零('0'),在十六进制前面显示‘0x’或者‘0X’（取决于用的是'x'还是'X'
# 0显示的数字前面填充‘0’而不是默认的空格
# % '%%'输出一个单一的‘％’
#（var）映射变量（字典参数）
# m.n m是显示的最小总宽度，n是小数点后的位数（如果可用用的话）


# 1英寸（in）＝ 2.54厘米（cm）
# 1磅（lb） ＝ 0.45359237千克（kg）
transfer_height = 2.54 * height #cm
transfer_weight = 0.45359237 * weight #kg
print "he's %d innechess tall,%d cm." % (height,transfer_height)
print "he's %d pounds haeavy,%d kg." % (weight,transfer_weight)
