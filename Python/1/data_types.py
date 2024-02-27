#single line comment
'''Multiline Comment 
     this is multiline comment.
'''


# to print a value on screen
print("hello world!")




# declaration and updating the variables
a='12'
print('initial a : '+a)# we can only concatenate two or more string using this method in python.
a='14'
print('updated a : '+a) # we can only concatenate two or more string using this method in python.


# # data types
number=123
decimal=23.33
string='farrukh'
boolean=False   #in pyhton boolean starts with capital
array=[21,21,32,42,32]

# print(number)
# print(type(number))

# print(decimal)
# print(type(decimal))

# print(string)
# print(type(string))

# print(boolean)
# print(type(boolean))

# print(array)
# print(type(array))

# String formatting

# 1--- simple formatting  --- this mehtod can only formate string with string
print('formatting :'+string)  # it can't formate string + number

# 2--- .formate() formatting
print('formate function formating : {} {} {} {} {}'.format(number,decimal,string,boolean,array))

# 3--- f-string formatting
print(f'formated string with f : {number} {decimal} {string} {boolean} {array}')

# 4--- %-formatting
print('formate with percentage : %d %f %s %s %s '%(number,decimal,string,boolean,array))



# Arithmetic Operators

# +
print(12+32)
# -
print(12-32)
# *
print(12*32)
# /
print(10/3)    # division of two numbers gives a float value it will give 3.333333 as result
# to get the integer part we use // operator
# //
print(10//3)     # it will give 3 as result instead of 3.33333
# **
print(8**3)      # power operator
# % Modulus
print(7%5)       # it will return the remainder of the division i.e 2



# Assignment Operators

num = 10         # Simple assignment
print(num)
num += 5        # Add and assign it means num = num + 5
print(num)
num -= 5        # Subtract and assign means num = num-5
print(num)
num *= 5       # Multiply and assign means num = num X 5
print(num)
num /= 5       # Division and assign means num = num/5
print(num)
num //= 5      # floor division and assign means num = num//5 which is an integer division
               # it will remove the decimal part from the result
print(num)
num %= 5       # Modulus and assign means num = num % 5
print(num)
