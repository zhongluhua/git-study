#enconding=utf-8

True and True
False and True
1 == 1 and 2 == 1
"test" == "test"
1 == 1 or 2 != 1
True and 1 == 1
False and 0 != 0
True or 1 == 1
"test" == "testing"
"test" == 1
not (True and False)
not (1 == 1 and 0 != 1)
not (10 == 1 or 1000 == 1000)
not (1 != 10 or 3 == 4)
not ("testing" == "testing" and "Zed" == "Cool Guy")
1 == 1 and not ("testing" == 1 or 1 == 0)
"chunky" == "bacon" and not (3 == 4 or 3 == 3)
3 == 3 and not ("testing" == "testing" or "Python" == "Fun")

"""
所有布尔逻辑表达式都可以用下面的简单流程得到结果：
1.找到相等判断的部分(== or !=),将其改为其最终值(True 或 False)
2.找到括号里的and / or，先算出它们的值
3.找到每一个not，算出它们反过来的值
4.找到剩下的and / or，解出它们的值
5.等你做完后，剩下的结果应该就是True 或者 False了
"""
