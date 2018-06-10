# --coding:utf-8--

formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True,False,False,True)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (
    "i had this thing.",
    "that you could type up right.",
    "but it didn't sing.",
    "so i said goodnight."
)

print "-" * 20

formatter = "%s %s %s %s"

print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True,False,False,True)
print formatter % (formatter,formatter,formatter,formatter)
print formatter % (
    "i had this thing.",
    "that it didn't sing.",
    "but it didn't sing.",
    "so i said goodnight."
)

# 为什么％r有时候打印出来的是单引号，而我实际用的是双引号？
# python会用最有效的方式打印出字符串，而不是完全按照你写方式来打印。这样做对于％r来说是可以
# 接受的，因为它是用作debug和排错，没必要非要打印出多好看的格式。
