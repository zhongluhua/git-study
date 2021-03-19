#coding=utf-8

#导入import进来的功能称作模组，可以这样说：把sys模组import进来，也有人称作库
from sys import argv


#argv是所谓的参数变量argument variable，是一个非常标准的编程术语
#将argv解包，将所有参数放到同一个变量下面，我们将每个参数赋予一个变量名script,first,second,third
#含义很简单：把argv中的东西解包，将所有的参数依次赋予左边的变量名
script,first,second,third,fourth = argv

print "The script is called:",script
print "Your first variable is:",first
print "Your second variable is:",second
print "Your third variable is:",third
print "Your fourth variable is:",fourth

