# python Functions
# syntax: def functionName(parameters(arguments)(arguments)):
    # code of function

# define a function
a=12
b=13
def sum():
    print(f'a + b: {a+b}')

    # calling the function
sum()

# function with     (arguments)
def display(a,b):
    print(f'a is {a}---b is {b}')
display(12,11)


# this formula will give us the sum of the all numbers from 0 to n i.e if given number is 5 it will give (1+2+3+4+5)
# formula= (n*(n+1))/2
# function example
def sum1(n):
    result=(n*(n+1))/2
    print(result)
sum1(5)

# function with default parameter value
# in this function we initialize the value of the parameter's value while defining the function and then while calling the function if we do't give the parameter the default value will be used and if we give the value the default value will be over written
# it is essential to give the default parameters(arguments) in the end,if there are multi parameters(arguments).
def sum2(n=10):
    result=(n*(n+1))/2
    print(result)
sum2()
sum2(11)

# default parameter example
def circle_area(r,pi=3.1415):
    area=pi*(r**2)
    print(area)
circle_area(12)
circle_area(12,3.14)

# assigning the parameters(arguments) while calling the function.
def find(a,b,c,d):
    print(a,b,c,d)
find(1,2,3,4) # now by default these parameters(arguments) are assigned one by one i.e a=1 b=2 c=3 d=4
find(c=3,a=1,d=4,b=2) # using this method we can assign the value on any place to the any parameter

# returning function
# returning functions returns any value to the calling place
def circle_area1(r,pi=3.14):
    area=pi*(r**2)
    return area   # return statement terminates the function i.e the code after the return statement will never run
    print('this is after return statement')
returned_value=circle_area1(12)
print(f'area of circle: {returned_value}')

# recursive function
# the function that call itself in its body is called recursive function
# this is an alternate of loops
def recursive():
    print(f'A is: {a}---B is: {b}')
    # recursive() # due to this statement it is a never ending recursive function
recursive()

# finding factorial of 5 i.e 1*2*3*4*5 using recursive function
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5))


# lambda functions
# A lambda function is a small anonymous function
# Lambda function can take a number of arguments(parameters),but can only have one expression
# the lambda functions returns the value by default

# Syntax: lambda arguments : expression

add = lambda a,b,d : a+b+d
print(add(1,2,3))