#coding=utf-8

#从sys里面调出argv模块
from sys import argv

#将argv解包依次赋值给左边的变量
script,input_file = argv

#定义一个打印文件所有行的函数
def print_all(f):
    print f.read() #函数执行读命令

#定义一个倒置函数，将光标至0，以便操作当前位置
def rewind(f):
    f.seek(0) #把文件光标移至0处，方便接下来的操作

#定义一个打印文件一行的函数
def print_a_line(line_count,f):
    print line_count,f.readline()#变量line_count表示行数，f.readline()表示只读一行指令
    
#将文件打开给变量
current_file = open(input_file)

print "first let's print the whole file:\n"

#调用print_all()函数
print_all(current_file)

print "now let's rewind,kind of like a tape."

#将文件的光标置0
rewind(current_file)

print "let's print three lines:"

#从0光标开始打印第一行
current_line = 1
print_a_line(current_line,current_file)

#行数加1，打印第二行
current_line = current_line + 1
print_a_line(current_line,current_file)

#行数加1，打印第三行
current_line = current_line + 1
print_a_line(current_line,current_file)


print "print is over!"
current_file.close()
