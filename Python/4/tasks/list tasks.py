'''
1-Find the last element of an array without giving a hard-coded index.
2-Check whether the first or the last index of an array has a specified value, let's say 5.
3-Make an array to store the names of students and check whether that array has your own name or not and also return the index of that value.
4-Add the array element at the specified index.
5-Delete the array element from the specified index.
'''

# 1--- Find the last element of an array without giving a hard-coded index.
list=[2,5,3,5,78,20]
l_element=list.pop()
print(f'last element: {l_element}')

# 2--- Check whether the first or the last index of an array has a specified value, let's say 5.
list=[5,2,3,5,7,8,5]
if list[0] == list[-1]:
    print(f'list has same first and last value i.e {list[0]}')
else:
    print(f'list has different first and last values i.e first value: {list[0]} --- last value: {list[-1]}')

# 3--- Make an array to store the names of students and check whether that array has your own name or not and also return the index of that value.
names=['ali','ahmed','talha','farrukh','farhan']
if 'farrukh' in names:
    index=names.index('farrukh')
    print(f'the name is present and the index of name is {index}')
else:
    print('the name is not in list')

# 4--- Add the array element at the specified index.
list=[2,1,3,2,4]
list.insert(2,'added at index 2')
print(list)

# 5--- Delete the array element from the specified index.
list=[1,2,3,4,5]
del list[-2] # --- second one from last i.e  4
print(list)





# create == of javascript in python
a=9
b='9'
if a is b:
    print('data types are same')
else:
    print('data types are not same')

if type(a) == type(b):
    pass
elif type(a)==str:
    a=int(a)
    print(type(a))
elif type(b)==str:
    b=int(b)
    print(type(b))
