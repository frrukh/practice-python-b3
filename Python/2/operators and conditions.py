# there are six comparison operators in python
# > , >= , < , <= , == , !=


# conditional statements
# if 
a=15
b=152
if (a<b):
    print('a is smaller than b')
    
# if else
if a>b:
    print('a is grater than b')
else:
    print('b is grater than a')

# elif
if a>b:
    print('a is grater')
elif b>a:
    print('b is grater')
else:
    print('both of a and b are equal')

# Logical operators
# there are three logical operators in python
# and , or , not
if (True)and(True):
    print('and needs all values true')
if (True)or(False):
    print('or needs at least one value true')
if not(False):
    print('not means negation of the expression')
