#coding=utf-8

animalslist = ['狗熊', '老虎', '狮子', '斑马']



def start():
    print "游戏开始！!"
    print "请输入房间号(1,2,3):"
    roomnum = int(raw_input(">"))

    if roomnum == 1:
        room_one()
    elif roomnum == 2:
        room_two()
    elif roomnum == 3:
        room_three()
    else:
        print "对不起！到火星了~"
        print "游戏结束!"
        exit(0)

def room_one():
    print "欢迎来到第一房间!"
    result = 0

    print "选择一种动物吧:"

    while True:
        if (result >= 0) and (result < 50) :
            animal = raw_input(">>>")
            if animal in animalslist:
                result += 10
            else :
                result -= 10
                if result < 0 :
                    print "抱歉，没有动物%s，扣10分！" % animal
                    result = 0
            print "当前总分数是：",result
            room_one()
        elif result >= 50 :
            room_two()
        else :
            print ("房间1出错啦！")
        return result
        print result
        
                    
    



def room_two():
    print "Welcome!"


def room_three():
    print "Welcome!"

start()
