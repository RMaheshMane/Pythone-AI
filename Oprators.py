## Membership Operators in , not in
a=10
b=20

list= [10,20,30,40,50]

if a in list:
    print ("a is in given list")
else:
    print ("a is not in given list")

if b not in list:
    print ("b is given in list")
else:
    print ("b is not given in list")


## Identity operators: is , is not
c=10
d=20
if c is list:
    print ("c is in given list")
else:
    print ("c is not in given list")

if d is not list:
    print ("d is given in list")
else:
    print ("d is not given in list")
