people = 31
cars = 30
buses = 35

if cars > people and buses > people :
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright,let's just take the buses."
else:
    print "Fine,let's stay home then."
