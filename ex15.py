#--coding:utf-8--

from sys import argv #引用

script,filename = argv #给变量argv赋值
txt = open (filename) #打开命令中输入的文件

print "here's your file %r:" % filename #打印文件名
print txt.read() #读argv中输入的文件，并将文件内容打印出来


print "type the filename again:" #打印
file_again = raw_input("> ") #在终端输入文件名
txt_again = open (file_again) #将终端输入的文件打开
print txt_again.read() #将终端输入的文件内容打印出来
