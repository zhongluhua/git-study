open#--coding:utf-8--

from sys import argv #引用

script,filename = argv #给变量argv赋值
txt = open (filename) #从open获得的东西是一个文件，然后赋值给变量txt

print "here's your file %r:" % filename #打印文件名
print txt.read() #读取txt中的内容，并打印出来


print "type the filename again:" #打印
file_again = raw_input("> ") #在终端输入文件名，并文件名赋值给变量file_again
txt_again = open (file_again) #open来获取文件file_again，并赋值给txt_again
print txt_again.read() #读取文件txt_again的内容并打印出来
