
def my_function(height,age):
    print "my height is:%r" % height
    print "my age is:%s" % age


print "round 1:"
my_function(50,20)

print "round 2:"
x1 = 10
x2 = 20

my_function(x1,x2)

print "round 3:"
my_function(10+11,20+33)

print "round 4:"
my_function(x1+10,x2+11)

print "round 5:"
sign = '>'
x01 = input(sign+'your height(a number):')
x02 = input(sign+'your age(a number):')
my_function(x01,x02)

print "round 6:"
sign = '>'
x01 = raw_input(sign+'your height(a string):')
x02 = raw_input(sign+'your age(a string):')
my_function(x01,x02)

print "round 7:"
x01 = input("input a number:")
x02 = input("input a number:")
my_function(x01,x02)

print "round 8:"
x01 = raw_input("input a string:")
x02 = raw_input("input a string:")
my_function(x01,x02)
