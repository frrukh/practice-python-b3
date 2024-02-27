# patient='John'
# age=20
# is_new=True
# print(patient)
# print(age)
# print(is_new)


# input function is used to take input from the user
# name=input('What is your Name? ')
# print('Hi '+name)



# 
# name=input('What is your Name? ')
# fav_color=input('What is your favorate color? ')
# print(name+" Likes "+fav_color)



#Calculating age 
# born_in=input('Birth year : ')
# in this piece of code the interpreter is trying to subtract a string into an integer so to fix this we use int() function to convert string into integer 
        # age=2023-born_in
# age=2023-int(born_in)
# print(age)



# type function is used to check the type of any variable
# print(type(born_in))
# print(type(age))



# Getting the weight from the user in pounds and then converting into kilograms
# lb_unit=0.45359237
# weight_lb= input('Enter your age in lbs (pounds) ')
# weight_kg= int(weight_lb) * lb_unit
# print(weight_kg)

# Python comments

# THIS IS A SINGLE LINE COMMENT

'''
THIS IS A MULTI LINE COMMENT
'''

"""
THIS IS ALSO A MULTI LINE COMMENT
"""

# declaring a string
# string1='this is a single line string'

# string2="this is also a single line string"

# string3='''
# This is a multiline string
# with multiple lines
# '''

# string4="""
# This is also a multiline string
# with multiple lines
# """
# print(string1)
# print(string2)
# print(string3)
# print(string4)


# we can target the specific index of the string
# name='Farrukh'
# print(name[0]) #it will show F because it is on index 0
# print(name[1]) #it will show a because it is on index 1

# we can also get index from last
# print(name[-1]) # it will show h as its index is -1 from end
# print(name[-2]) # it will show k as its index is -2 from end

# we can also get a slice from the string
# it do't includes last index i.e 0:3 means 0,1,2    3 is not included
# print(name[1:5])

# if we give index from end it also works
# print(name[-7:-2])

# if we not give the end index it will give total string
# print(name[1:])
# print(name[-6:])

# if we not supply the start index the python interpreter assumes it 0
# print(name[:2])
# print(name[:-2])

# if we not supply any value the python interpreter assumes 0 as a start index and the string length as the end index
# print(name[:])
        # this index is used to copy or clone a string for example
# my_name=name[:]
# print(my_name+'  --- this is clone')




# Concatenation Or Formatting Strings
# inserting something of a different nature into something else
# String formatting refers to the process of creating a string that contains placeholders, which are later replaced by actual values or variables to produce a final formatted string.


# there are two ways to concatenate strings in python

# Method 1 : Using + operator
# first='Farrukh'
# last='Maqsood'
# I want to print : Farrukh [Maqsood] is a coder
# message=first+' ['+last+'] is a coder'
# print(message) 

# Method 2 : Using f (stands for formated string) 
# we just start this with prefix f and then when we have to use variable we use it in curly braces{}
# msg=f'{first} [{last}] is a coder (with f Method)' # there we have 2 place-holders or holes
# print(msg)

# Method 3 : Using str.format() function
# In this function the placeholders are in curly braces and after string we use .format(placeholder1,placeholder2,placeholder3 and so on)
# msge='{} [{}] is a coder with .format()'.format(first,last)
# print(msge)

# Method 4 : Using % --- it is the oldest technique of string formatting
# We just leave a placeholder in string like % and add a suffix with it according to the datatype like for string %s and after closing the strnig we have to define the variable that we want to use in string.
# Using with single placeholder
# messag='%s is a coder (with percentage Method)' % first
# print(messag)
# Using with multi placeholders
# messag='%s [%s] is a coder (with percentage Method)'% (first,last)
# print(messag)





# String Methods
# when a function belongs to a specific type of object we refers it a Method

# 1-- len() ---function
# to get length----it is a general purpose function and can be use on lists not only strings
# name='Farrukh'
# print(len(name))

# 2-3-- .upper() , .lower()
# to convert string into upper case , lower case---it can not change the original string 
# print(name.upper())
# print(name.lower())
# print(name)

# 4-- .title()--- Make the first letter in each word upper case
# sentence='Farrukh is a very good boy'
# print(sentence.title())
# print(sentence)
# 5--- .find() --- to find a single or multiple characters in the string
# returns the first index of substring if found otherwise return -1
# name.find('k')   --returns 5  
# print(name.find('k'))
# name.find('w')  --returns -1
# print(name.find('w'))
# if I find r in name it will give the index of first one --2
# print(name.find('r'))
# if I find rukh in name it will give the index of r --3
# print(name.find('rukh'))
# print(name.find('arukh')) #it goes to -1

# 6--- .replace(,) --- to replace a single or group of characters
# It takes two arguments:
#       a) character/substring which needs to be replaced
#       b) new value /character that will replace old value
# If no new value provided then it replaces with None
# name.replace('a','A')    --It will Replace all 'a' with 'A'
# print(name.replace('r','R')) # --- FaRRukh
# print(name.replace('rrukh','rrukhDon')) # --- FarrukhDon
# print(name.replace('rrukh','')) # --- Fa
# print(name.replace('reukh','mmppoo')) # ---Farrukh (do't works because not find reukh)






# Python Membership Operators--- it answers in boolean value


# In python there are two types of membership operators :

#                        a) "in" operator
# 'in' operator
# it checks whether a given element is present in the sequence or not
# syntax :  element in sequence
# print('Farrukh' in name) # --- True
# print('farrukh' in name) # --- False

#                        b) "not in" operator
# 'not in' operator
# it checks whether a given element is not present in the sequence or not
# syntax :  element not in sequence
# print('r' not in name) # --- False
# print('farrukh' not in name) # --- True









# Arethmetic Operators
# Addition         +
# three=3
# print(three+4)
# Subtraction      -
# print(12-three)
# Multiplication    *
# print(three*10)
# Division          /
# print(10/three)
# Modulus(reminder)           %
# print(10%three)
# exponentiation(power)     **
# print(2**three)
# Floor division (it will gives the floor value i.e without point)      // 
# print(10//three) # --- it gives 3 not 3.33333333




# Math Functions 



# 1--- .round() --- it rounds the number according to some rules i.e 2.94 to 3
#       rule-1  it simply removes all digit after decimal point if first digit after decimal point is less then 5
# print(round(2.4))    # --- 2
# print(round(3.4))    # --- 3
#       rule-2 it add 1 to the value if the first digit after decimal point is grater then 5
# print(round(2.6))    # --- 3
# print(round(3.8))    # --- 4
#       rule-3  if first digit after decimal point is 5 then if the last number before decimal is odd, it will add 1 in it else not.
# print(round(3.5))      # --- 4
# print(round(2.5))      # --- 2
# import math

# 2--- .abs --- it will always give the absolute(positive) value
# print(abs(-24.3))         # --- 24.3





# IF STATEMENTS
'''

hot_day=False
cold_day=True
if hot_day:
    print("It is a hot day")
elif cold_day:
    print('It is a cold day')      
else:
    print('It is a lovely day')
'''

# Example 
'''
good_credit=False
normal_credit=False
house_Amount=1000000
discount=0
off_upto=0
if good_credit:
    final_amount=house_Amount-((house_Amount/100)*10)
    discount=house_Amount-final_amount
    off_upto=10
elif normal_credit:
    final_amount=house_Amount-((house_Amount/100)*20)
    discount=house_Amount-final_amount
    off_upto=20
else:
    final_amount=house_Amount-((house_Amount/100)*30)
    discount=house_Amount-final_amount
    off_upto=30

print(f'Actual amount : ${house_Amount}')
print(f'Discout amount : ${discount}')
print(f'Final_amount : ${final_amount} upto {off_upto}% off')
'''


'''
# Logical Operators
is_good=True
is_slim=True

# AND-and
if is_good and is_slim:
    print("You are good and slim")


# OR-or
is_good=True
is_slim=False

if is_good or is_slim:
    print('You are good or slim')


#  NOT-not
is_good=True
is_slim=False

if is_good and not is_slim: # here not is changing the false of is_slim into true and as the result the 
    print('You are good but not slim')

if not (is_good and is_slim):
    print('You are good but not slim')



'''

'''
# Comparison Operators

# there are six Comparison operators in python
#   >     <      >==    <=   ==   !=
a="10"
b=10
if a == b:
    print('a and b are equal')
else:
    print('a and b are not equal')

#   exercise
name=input('Enter Your Name:  ')
if len(name)<3:
    print('name must be at least 3 characters')
elif len(name)>50:
    print('name can be maximum of 50 characters')
else:
    print('name looks good!')

# Weight convertor
weight=int(input('Enter Your Weight:  '))
unit=input('Enter Unit (K)g/(L)b :  ')
if unit.upper()=='K':
    weight_in_lbs=round(weight/0.45)
    print(f'Weight : {weight_in_lbs}lbs')
elif unit.upper()=='L':
    weight_in_kgs=round(weight*0.45)
    print(f'Weight : {weight_in_kgs}kg')
else:
    print("Invalid Input")
'''


'''
# Loops

# There are three types of loops in Python
# while loop, for loop , and nested loop


# while loop
"""
syntax:
while condition:
    code
"""
i=1
while i<=5:
    print('*'*i)
    i+=1
print('done ')


# Secrete Number Game
secret_number=9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('You won!')
        break # break statement is used to terminate the loop
# in python we also have the else part in LOOPS which is executed if the loop completes successfully without an immediate break
# in this case if the user guess the right number you break this loop and jump out of it so the else written in else block will not get executed , but if the user can't guess the number the loop will not break and the code written in else block will executed.
else:
    print('sorry, You failed!')
'''


# Car Game
'''
i=1
while i>0:
    inp=input('>')
    if inp=='help':
        print('start ---- to start the car')
        print('stop ---- to stop the car')
        print('end---- to end the process')
    elif inp=='start':
        print('car is started')
    elif inp=='stop':
        print('car is stoped')
    elif inp=='end':
        print('process ended')
        break
    else:
        print("I don't understand that...")
'''

'''
print('write help to get info')
command=''
is_start=False
while True:
    command = input('> ').lower()
    if command =='start' :
        if is_start:
            print('Car has already been started')
        else:
            print('Car has been started.')
            is_start=True
    elif command =='stop':
        if not is_start:
            print('Car has already been stopped')
        else:
            print('Car has been stopped')
            is_start=False
    elif command == 'help':
        print("""
start ---  to start the car
stop --- to stop the car
quit --- to quit
        """)
    elif command == 'quit':
        break
    else:
        print("Sorry, I don't understand that!")
print('process ended')
'''

'''
# For Loop
# in python for loop is just like the for of loop of javascript i.e it continuously gives us the value of string or array etc until it ends.
for val in 'Farrukh':
    print(val)

for val in ['Farrukh','Waqas','Talha','Abdullah','Ali']:
    print(val)

for val in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]:
    print(val)

# range()
# in upper example we write the numbers from 1 to 20 but what happened if we need the more that 20 like 50 or 100 or 1000,we can't write it one by one, to solve this problem there is a builtin function in python i.e range()
# syntax : range(start-value,end-value(not included))----if we give only one value it will take that as end value and assume the start value 0.
# it does not generate a list(array), it generates a special type of object which datatype is range that can be used for iteration in loop.

for val in range(10):
    print(val)
# for val in range(-10):    # not working
    # print(val)

for val in range (-10,10):
    print(val)
for val in range(3,12):
    print(val)

    # the range function can optionally take a third parameter i.e step , so if we pass 2 as the step of this function it will make the object like this : range(0,2,4,6,8,10)
for val in range(0,51,5):
    print(val)
for val in range (-10,10,3):
    print(val)

# Exercise
list_of_prices=[100,120,130,200]
total=0
for price in list_of_prices:
    total+=price
print(f'Total : {total}')
'''
'''

# Nested Loop
# (outer) loop having inside a (Inner) loop is called nested loop
for x in range(3):
    for y in range(4):
        print(f'({x}, {y})')
    
# Challenge
# Printing F Using Nested Loop
numbers=[5,2,5,2,2]
for x_count in numbers:
    output=''
    for x in range(x_count):
        output+='x'
    print(output)
'''


'''
# List(array)
# define
list=[21,32,4523,53,53,21,15,'farrukh',True]
print(list)
# change
list[0]=15
print(list)
# following can not make any chang in original list.
# access
print(list[0])
# access from end
print(list[-1]) # it gives True
print(list[-2]) # it gives Farrukh
print(list[-3]) # it gives 15
# access multi values   i.e list[startIndex:EndIndex(not included)]
print(list[1:7])
    # access multi values with first parameter empty --- it assumed it 0
print(list[:7])
    # access multi values with second parameter empty --- it assumed it to the end of the list
print(list[1:])





list=[21,32,43,54,65,75,43,32,54,24,98,32,32,4]
largest=list[0]
for item in list:
    if largest<item:
        largest=item
print(f'Largest Number in the list is : {largest}')

'''
'''
# 2D Lists


# Declaration
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# access
print(matrix[0][1])
# modification
matrix[0][1]=20
print(matrix[0][1])

# using in loop
for row in matrix:
    for val in row:
        print(val)

# List Methods
# 1---listName.append(value to append)---this is used to append the value at the last of the list
array=[2,4,6,8,10,12,14]
array.append(16)
print(array)

# 2---listName.insert(index,value to append)---this is used to append the value at the specific index of the list
array=[2,4,6,8,10,12,14]
array.insert(2,5)
print(array)

#  3---listName.remove(value to remove not the index)---this is used to remove the value from array
array=[2,4,6,8,103,12,14]
array.remove(103)
# array.remove(1030) # if we pass a value that is not present in list it will show error
print(array)

# 4---listName.clear()---it is used to remove all the values present in the list
# it does't take any parameter
array=[2,4,6,8,10,12,14]
array.clear()
print(array)

# 5---listName.pop()---it is used to remove the single item from the end of the list
# it also have no parameters
array=[2,4,6,8,10,12,14]
array.pop()
print(array)

# 6---listName.index(value whose index is needed)---this method is used to get the index of the value
array=[2,2,4,6,8,10,2,12,14]
print(array.index(2))# it will give the index of first occurred value i.e there are three twos but it jusr give the index of first one.
# if the given number does't exist in the list we will get an error. 
# print(array.index(20))

# to check the existence of a character is string or existence of a value in string can also be done with 'in' membership operator
print(50 in array)


# 7--- arrayName.count(value to count)---this will give the number of repetition of the value in the array 
# i.e array=[2,2,4,6,8,10,2,12,14]  print(array.count(2)) ---- 3 as there are three tows
array=[2,2,4,6,8,10,2,'as',12,14]
print(array.count('as')) # ---1

# 8---arrayName.sort()---this is used to sort the list
array1=[4,5,3,2,7,1,6,8,9,0]
array1.sort() # now array1=[0,1,2,3,4,5,6,7,8,9]
print(array1)

# 9---arrayName.reverse()---this will reverse your list
array2=[0,1,2,3,4,5,6,7,8,9]
array2.reverse()
print(array2)

# 10---arrayName.copy()---this is used to take a copy  of the list
array3=array2.copy()
print(array3)

# exercise  problem: write a program to remove the duplicates in a list
array_of_duplicates=[1,4,2,4,5,6,4,8,5,2,5]
def remove_duplicates():
    for item in array_of_duplicates:
        if array_of_duplicates.count(item) > 1:
            while array_of_duplicates.count(item)!=1:
                array_of_duplicates.remove(item)
    else:
        return array_of_duplicates
    
print(remove_duplicates())


# exercise  problem: write a program to remove the duplicates in a list
array_duplicates=[2,2,5,3,4,5,4,7]
unique_num=[]
for item in array_duplicates:
    if item not in unique_num:
        unique_num.append(item)
print(unique_num)

'''
'''

# Tuples
# Tuples are just like lists but unlike lists we can't modify the tuples as TUPLES are Immutable
# lists are defined by square brackets where tuples are defined by parentheses
tuple1=(1,2,3,4,5,2,2,2)
# access single item
print(tuple1[2])
# tuple1[1]=2 # it will give error as tuples are immutable
# There are only two basic methods of tuples in python
# 1---tupleName.count()---	Returns the number of times a specified value occurs in a tuple
print(tuple1.count(2))
# 2---tupleName.index()---Searches the tuple for a specified value and returns the position of the first occurrence where it was found
print(tuple1.index(2)) # --- 1 as first 2 is on index 1

'''
'''

# Unpacking --- can be used for strings and tuples.
# this is a short method to assign the each value of list or tuple to a variable
let=(1,2,3,4)
a=let[0]
b=let[1]
c=let[2]
d=let[3]
print(b)
# we can do the same thing using unpacking like given below
leet=(1,2,3,4)
a,b,c,d=leet
print(d)
# can also do this for arrays
arr=[1,2,3,4,5]
(a,b,c,d,e)=arr
print(e)

# in unpacking the use of * followed by the variable name will give all the next values to the variables in array formate.
tuplee=('apple','mango','Orange','banana','kiwi')
red,yellow,*fruits=tuplee
print(red) #---apple
print(yellow) #---mango
print(fruits) #---['Orange','banana','kiwi']

# if there is an other variable after variable with static sign it will assign the all rest(remaining) values except last one and assign last one to that variable

# tuplee=['apple','mango','Orange','banana','kiwi'] # also works on array
# tuplee-{'apple':12,'mango':13,'orange':14,'banana':15,'kiwi':16} # Not works on dictionary
tuplee=('apple','mango','Orange','banana','kiwi')
red,yellow,*fruits,green=tuplee
print(red)
print(yellow)
print(fruits)
print(green)

'''
'''

# Dictionary
# syntax : { 'key':value,'key':value,'key':value,'key':value }
# initialization
dictionary={
    'name':'Farrukh',
    'Course':'Python',
    'Batch':3,
    'age':19
}

# access
print(dictionary)
print(dictionary['Batch'])
    # here if we give a key which is not present in dictionary it will through error, to fix it we use get method
    # syntax:dictionaryName.get(keyName,default value(optional))
print(dictionary.get('address'))  # if key is not present it will return None
# but if you provide a default value then it will return that value
print(dictionary.get('address','lahore')) #---Not effect the original dectionary

# update existing key
dictionary['age']=20
print(dictionary)

# adding new key
dictionary['fullName']='Muhammad Farrukh Maqsood'
print(dictionary)

# exercise problem:Translate the given number into words (1234 to one two three four)

def convert_num_to_words():
    phone=input('Phone: ')
    if phone is 'stop':
        return 
    final=''
    for num in phone:
        array=['zero ','one ','two ','three ','four ','five ','six ','seven ','eight ','nine ']
        
        final+=array[int(num)]
    print(final)
        # print(num)
    convert_num_to_words()
convert_num_to_words()

# easy and simple way
phone=input('Phone: ')
digits={
    "0":"zero",
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine'
}
output=''
for ch in phone:
    output+=digits.get(ch,'!')+' '
print(output)
'''

'''
# change char to emoji
message=input('>')
words=message.split()#--this method is used to split a sentence like from 'I am farrukh' to ['I','am','farrukh'] it gives a string.---it also have a parameter if we add then it will split from the given parameter and remove the parameter from the string i.e string='my name is farrukh' string.split('a') it will give ['my n','me is f','rrukh']
print(words)
emoji={
    ":)" : '😀',
    ":(" : '😌'
}
output=''
for word in words:
    output+=emoji.get(word,word)+' '
print(output)
'''

'''
# Functions
# syntax: def functionName(parameters):
# initialization
def print_ok():
    print('I am OK! 😶')


# calling
print_ok()

# Parameters and arguments
# parameters
# parameters are like variables that hold the values passed into a function
# arguments
# arguments are what we actually pass into the parentheses when we call a function
def add(x,y): # here x and y are parameters
    print(x+y)



add(12,21) # here 12 and 21 are arguments

'''

'''
# types of arguments and parameters
# there are five major types of arguments and parameters in python

# 1--Positional arguments
# In this, the arguments are assigned to the parameters according to position 
# Example
def positional_arguments(a,b,c):
    print(f'a: {a} --- b: {b} --- c: {c} ')


positional_arguments(1,2,3) #according to the position - a=1,b=2,c=3

# 2--Keyword arguments
# In this,we can assign the arguments by the name of parameters 
# keyword arguments are always placed at the end of the other arguments
# Example
def keyword_arguments(a,b,c):
    print(f'a: {a} --- b: {b} --- c: {c} ')



keyword_arguments(b=2,c=3,a=1)

# 3---Default parameters
# In this,if an argument is not provided while calling the function then it will take its default value instead of throwing error
# Example 1
def default_parameter(a,b=2,c=3):# always use keyword arguments in last
    print(f'a: {a} --- b: {b} --- c: {c} ')


default_parameter(1)

# Example 2
def fun(a,b):
    print(f'a: {a} b: {b}')


fun(23,2) #---error fun got multiple values of 'a'

# Arbitrary parameters (arbitrary means without meaning or without any principle)
# In this,If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
# Example 1
def arbitrary_argument_1(a,*b):
    print(f'a: {a}')
    print(f'b: {b}') # it will print a tuple of arguments like (2,3,4)


arbitrary_argument_1(12,2,3,4)

# Example 2
def arbitrary_argument_2(a,*b,c):
    print(f'a: {a}')
    print(f'b: {b}')
    print(f'c: {c}')

#-- it is not giving the last value to c and throwing error
#-- to fix this we can assign value of c using keyword argument or by making 'c' a default parameter
# arbitrary_argument_2(12,2,3,4,3,4)

arbitrary_argument_2(12,2,3,4,3,c=4)

# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly
# Example
def arbitrary_keyword_argument(a,**b): # they can only be written in the end
    print(f'a: {a}')
    print(f'b: {b}')


arbitrary_keyword_argument(21,key1=12,key2='string',key3=True)



# Return statement--- used to return the value from where it is called
def sum():
    return 12*2


sum=sum()
print(f'sum: {sum}')


# Function Final Example
# Emoji converter
emoji={
    ':)':'😀',
    ':(':'😑',
}
def emoji_fun(message):
    words=message.split()
    output=''
    for word in words:
        output+=emoji.get(word,word)+' '
    return output


mes=input('>')
print(emoji_fun(mes))

'''
'''

# Exception

try:
    age=int(input('age> '))
    print(age)
except ValueError:
    print('invalid input')
'''
'''
# Classes
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y


    def move(self):
        print('move')


    def draw(self):
        print('draw')

    
p=Point(y=2,x=32)
print(p.y)

class Person:
    def __init__(self,name):
        self.name=name


    def talk(self):
        print(f'Hi {self.name},I am generated by Farrukh!')


e=Person('Abdullah')

print(e.name)
e.talk()
        
'''