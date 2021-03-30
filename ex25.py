#coding=utf-8
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ') #split()通过指定分隔符对字符串进行切片，此处是通过空格切片
    return words

"""sort和sorted区别：sort是应用在list上的方法，sorted可以对所有可迭代的对象进行排序操作
list的sort方法返回的是对已经存在的列表进行操作，而内建函数sorted方法返回的是一个新的list，而不是在原来的基础上进行操作
sorted(iterable,key=None,reverse=False)
iterable:可迭代对象
key:主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序
reverse：排序规则，reverse =True 降序，reverse = False 升序(默认)
#返回值：返回重新排序的列表
"""
def sort_words(words):
    """Sorts the words."""
    return sorted(words) #sorted()函数对所有可迭代对的对象进行排序操作


"""pop()函数用于移除列表中的一个元素(默认最后一个元素)，并且返回该元素的值
list.pop([index=-1])，obj可选参数，要移除列表元素的索引值，不能超过列表总长度，默认为index=-1,删除最后一个列表值
"""

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0) #移除第一个元素
    print word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1) #移除最后一个元素
    print word


#结合break_words和sort_words
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sortedwords."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
