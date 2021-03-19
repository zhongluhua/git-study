#encoding=utf-8
from sys import argv

script,filename = argv

print "We're going to erase %s." % filename
print "If you don't want that,hit CTRL-C."
print "If you do want that,hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename,'w')

#truncate()方法用于截断文件，若指定参数size，则截断文件为size个字符，若没有指定size，则从当前位置起截断
#截断之后，size后面的所有字符被删除
print "Truncating the file.Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally,we close it."
target.close()
