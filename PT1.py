import random

nice = ["Kelly","Jonathan","Peter","Angie","William","Joseph","Stacey",
"Jamal","Keesha","Michael"]
naughty = []

print
print "The nice list:", nice

count = 0
while count < len(nice):
    name = nice.pop(random.randrange(len(nice)))
    # print name
    # print len(nice)
    naughty.append(name)
    count += 1
    
print
print "The naughty list is:",naughty
print
print "The nice now has: ",nice
