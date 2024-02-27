'''
Sum all the list elements by using both a loop and a Python built-in function.
Reverse the list by using both a loop and a Python built-in function.
Make a table of the given number with all possible loops.
Find the largest number in a list by using both a loop and a Python built-in function.
Find the smallest number in a list by using both a loop and a Python built-in function.
Add the list element at the specified index.
Delete the list element from the specified index.
Make a normal list to store the name of 5 students and iterate with for and foreach loop.
Make an associative list to store the name of 5 students and iterate with a foreach loop.
Make a normal list of associative Lists(a list that will have associative Lists) to store the information of at least 2 students and access them as hard-coded.
Information to store:
Name, age, registration number, course, favorite programming languages (should be a    normal list), Marks of 5 different subjects (should be an associative list).
The operations to perform:
Display every single value for any student.
Display the first and last favorite programming languages of any student.
Display the marks of any two subjects for any student.
'''


# 1--Sum all the list elements by using both a loop and a Python built-in function.
list=[2,3,4,1,5,6]
sum=0
for i in list:
    sum+=i
else:
    print(sum)


# 2--Reverse the list by using both a loop and a Python built-in function.
# using loop
list=[0,9,8,7,6,5,4,3,2,1]
reversed_list=[]
for i in list:
    reversed_list.insert(0,i)
print(reversed_list)
# using function
list=[0,9,8,7,6,5,4,3,2,1]
list.reverse()
print(list)


# 3--Make a table of the given number with all possible loops.
# with for loop
num=4
mul=[1,2,3,4,5,6,7,8,9,10]
for i in mul:
    print(f'{num} X {i} = {num*i}')

# with while loop
num=4
mul=[1,2,3,4,5,6,7,8,9,10]
i=0
while i < len(mul):
    print(f'{num} X {mul[i]} = {num*mul[i]}')
    i+=1

# 4--Find the largest number in a list by using both a loop and a Python built-in function.
# with loop
list=[2,4,2,4,6,7,4,76,43,6,23]
largest=list[0]
for i in list:
    if largest<i:
        largest=i
print(largest)
# with function
list=[2,4,2,4,6,7,4,76,43,6,23]
largest=list[0]
largest=max(list)
print(largest)


# 5--Find the smallest number in a list by using both a loop and a Python built-in function.
# by for loop
list=[3,4,23,5,56,3,5,456,8,21,34,1,34,34]
smallest=list[0]
for i in list:
    if smallest>i:
        smallest=i

print(smallest)

# by function
smallest_num=min(list)
print(smallest_num)

# 6--Add the list element at the specified index.
list=[1,2,3,4,5]
list.insert(2,2.5)
print(list)


# 7--Delete the list element from the specified index.
list=[1,2,3,4,4,5]
list.pop(4)
print(list)


# 8--Make a normal list to store the name of 5 students and iterate with for and foreach loop.
names=['Ali','Ahmed','Farhan','Husain','Salman']
for i in names:
    print(i)

for ind,val in enumerate(names):
    print(f'index: {ind} --- value: {val}')


