#--coding:utf-8--

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#统计车辆总数
print "there are",cars,"cars available"
#统计司机总数
print "there are only",drivers,"drivers available"
#统计今天空着的车辆数
print "there will be",cars_not_driven,"empty cars today"
#统计今天可以运送的人数
print "we can transport",carpool_capacity,"people today"
#统计今天需要运送的人数
print "we have",passengers,"to carpool today"
#统计每辆可用的车可运送的人数
print "we need to put about",average_passengers_per_car,"in each car"
