# Task
#     Check two given numbers and return true if one of the numbers is 50 or if their sum is 50.
#     Check from the given integer, whether it is positive or negative.
#     Check whether a given number is even or odd.
#     Check whether a given positive number is a multiple of 3.
#     All the prior tasks are to be solved with functions.

#     check from the given two numbers, weather the first number is "grater", "lesser" or "equal" to the second number.
#     check from the three sides of triangle. use conditions to determine and display 
#     weather the triangle is "Equilateral" (all sides are equal), "Isosceles" (two sides are equal), or "Scalene" (no sides are equal)
#     check from the given month (1-12) if its "Winter" (December-February), "Spring" (March-May), "Summer" (June-August), or "Autumn" OR "Fall" (September-November).
#     Create a function that takes two numbers as input and returns the largest of the two.
#     create a function that takes two strings as input and returns a new string that concatenates both if them.
#     Write a function that takes a temperature in celsius and converts it to Fahrenheit.
#     Write a program that takes the age and checks if they are eligible for voting (e.g 18 or older)
#     Implement a function that checks if a given number is positive, negative, or zero and return the result.
#     create a function that takes two numbers as input and returns their product  using arithmetic operations. (e.g the product of 2 and 3 is 6)
#     implement a function that takes two strings as input and checks if they are equal.
#     Write a function that takes a number as input and returns the absolute value of the number
#     Determine whether a given year is a leap year.


# SOLUTION
#     Check two given numbers and return true if one of the numbers is 50 or if their sum is 50.
def check_if_50(a,b):
    if a==50 or b==50:
        return 'one of the given numbers is 50'
    elif a+b==50:
        return 'the sum of the given numbers is 50'
    else:
        return 'any of the given number is not 50 and their sum is also not 50'

is_fifty=check_if_50(20,30)
print(is_fifty)

# Check from the given integer, whether it is positive or negative.
def check_sign(num):
    if num>0:
        print('number is positive')
    elif num<0:
        print('number is negative')
    else:
        print('ZERO')
check_sign(0)

#     Check whether a given number is even or odd.
def even_odd(n):
    if n%2==0:
        print('given number is even')
    else:
        print('given number is odd')
even_odd(11)

#     Check whether a given positive number is a multiple of 3.
def check_multiple_of_three(n):
    if n<=0:
        print('plese enter a positive non-zero number')
    elif n%3==0:
        print('the given number is the multiple of three')
    else:
        print('the given number is not the multiple of three')
check_multiple_of_three(12)

#     check from the given two numbers, weather the first number is "grater", "lesser" or "equal" to the second number.
def check_num(a,b):
    if a>b:
        print('first number is grater than second')
    elif a<b:
        print('second number is grater than first')
    else:
        print('both numbers are equal')
check_num(13,12)

#     check from the three sides of triangle. use conditions to determine and display weather the triangle is "Equilateral" (all sides are equal), "Isosceles" (two sides are equal), or "Scalene" (no sides are equal)
def define_triangle(s1,s2,s3):
    if s1==s2 and s2==s3:
        print('it is an equilateral triangle')
    elif s1==s2 or s2==s3 or s3==s1:
        print('it is an isosceles triangle')
    else:
        print('it is a scalene triangle')
define_triangle(2,3,4)

#     check from the given month (1-12) if its "Winter" (December-February), "Spring" (March-May), "Summer" (June-August), or "Autumn" OR "Fall" (September-November).
def check_season(month):
    if month<1 or month>12:
        print('plese enter a valid month (1-12)')
    elif month==12 or month<=2:
        print('Winter')
    elif month<=5:
        print('Spring')
    elif month<=8:
        print('Summer')
    else:
        print('Autumn')
check_season(11)

#     Create a function that takes two numbers as input and returns the largest of the two.
def find_larger(a,b):
    if a>b:
        return "a is grater"
    elif b>a:
        return 'b is grater'
    else:
        return 'both are equal'
print(find_larger(9,9))

#     create a function that takes two strings as input and returns a new string that concatenates both if them.
def concatenation(a,b):
    if not (type(a)==str and type(b)==str):
        print('plese enter string in both parameters')
    else:
        print('{} {}'.format(a,b))
concatenation('1.string','2.string')

#     Write a function that takes a temperature in celsius and converts it to Fahrenheit.
def change_unit(temp,unit,unit_to):
    unit=unit.lower()
    unit_to=unit_to.lower()
    if not((unit=='f' or unit=='c' or unit=='k')and(unit_to=='f' or unit_to=='c' or unit_to=='k')):
        print('please enter a valid unit i.e fahrenheit(f),celsius(c) or kelvi(k)')
    elif unit=='f' and unit_to=='c':
        temp_Celsius=(temp-32)*(5/9)
        print(f'temp in Celsius: {temp_Celsius}')
    elif unit=='c' and unit_to=='f':
        temp_fah=(temp*(9/5))+32
        print(f'temp in Fahrenheit :{temp_fah}')
    elif unit=='c' and unit_to=='k':
        temp_kelvin=temp+273.15
        print(f'temp in Kelvin: {temp_kelvin}')
    elif unit=='k' and unit_to=='c':
        temp_Celsius=temp-273.15
        print(f'Temp in Celsius: {temp_Celsius}')
    elif unit=='f' and unit_to=='k':
        temp_kelvin=(temp-32)*(5/9)+273.15
        print(f'temp in kelvin: {temp_kelvin}')
    elif unit=='k' and unit_to=='f':
        temp_fah=(temp-273.15)*1.8+32
        print(f'temp in fahrenheit: {temp_fah}')
    else:
        print(temp)

change_unit(5,'F','C')
change_unit(32,'C','F')
change_unit(13,'C','K')
change_unit(323,'K','C')
change_unit(20,'F','K')
change_unit(20,'K','F')


#     Write a program that takes the age and checks if they are eligible for voting (e.g 18 or older)
def is_eligible(age):
    if age<0 or age>120:
        print('plese enter a valid age')
    elif age>17:
        print('Eligible for voting')
    else:
        print('Not eligible for voting')
is_eligible(31)

#     Implement a function that checks if a given number is positive, negative, or zero and return the result.
def check(n):
    if n>0:
        return 'Positive'
    elif n<0:
        return 'Negative'
    else:
        return 'ZERO'
print(check(2))

#     create a function that takes two numbers as input and returns their product  using arithmetic operations. (e.g the product of 2 and 3 is 6)
def product(a,b):
    print(f'product of {a} and {b} is: {a*b}')
product(2,3)

#     implement a function that takes two strings as input and checks if they are equal.
def string_check(a,b):
    if a==b:
        print('both strings are equal')
    else: print('both are not equal')
string_check('string','string')

#     implement a function that takes two strings as input and checks the length of both strings are equal.
def string_len(a,b):
    if len(a)==len(b):
        print('Both strings have same length')
    else:
        print("Both strings does't have same length")
string_len('we','ew')

#     Write a function that takes a number as input and returns the absolute value of the number
def abs_val(a):
    if a<0:
        print(f'the absolute value of {a} is {a*-1}')
    else:
        print(f'the absolute value of {a} is {a}')
abs_val(30)

#     Determine whether a given year is a leap year.

def leap_year():
    year=int(input('Enter a year (like 2003): '))
    if year==00:
        return 'program is over'
    elif (year%4==0 and year%100!=0)or year%400==0 :
        print('Given year is a leap year')
    else:
        print('Given year is not a leap year')
    leap_year()
leap_year()