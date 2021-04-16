#encoding=utf-8

#使用def命令创建函数，也就是定define的意思，参数必须放在圆括号()中才能正常工作
def print_two(*args):
    #用冒号结束上一行，开始下一行缩进。下面是将参数解包，跟脚本参数解包差不多原理
    arg1,arg2 = args
    print "arg1:%r,arg2:%r" % (arg1,arg2)

#其实，函数中可以跳过参数解包的过程，()中直接使用变量名
def print_two_again(arg1,arg2):
    print "arg1:%r,arg2:%r" % (arg1,arg2)

#函数可接收单个参数
def print_one(arg1):
    print "arg1:%r" % arg1

    
#函数可不接收任何参数
def print_none():
    print"I got nothin'."

print_two("zed","shaw")
print_two_again("zed","shaw")
print_one("first")
print_none()
