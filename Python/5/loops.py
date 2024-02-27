# For loop

    # With static value

# range function is used to give number of iteration we need to run the loop
# range with single parameter (end point)
for i in range(12):
    print(i) # each iteration have a value 0,1,2,3...11.

# range with dual parameters (start point,end point)
for i in range(2,11):
    print(i) # it will start from 2 and end at 11 but not include 11.

# range with triple parameters (startPoint,endPoint,increment)
for i in range(0,11,2):
    print(1) # it prints values like 0,2,4,6,8,10

# range with triple parameters reverse (start,end,decrement)
for i in range(10,0,-1):
    print(i) # it prints like 10,9,8,7,6....1

    # with dynamic value

# Loops on lists

names=['Ali','Bilal','Sultan','Rehan','Farhan','Noman','Haider','Majid','Dilawar']
for name in names:
    print(name) # this will give the value of every index ony by one like Ali  Bilal ...

# the upper syntax will not gives us the index of the value to get index and value we use the enumerate() function 
# enumerate(list name) function provides us the index and value of list in the form of tuple
for ind_and_val in enumerate(names):
    print(ind_and_val) # output : (1,'Ali') (2,'Sultan')....
    print(f'index:{ind_and_val[0]}---vlaue:{ind_and_val[1]}')

# we and store the index and value in two different variables by giving 2 variables in loop
for ind,val in enumerate(names):
    print(f'index:{ind}---value:{val}')


# Loops on dictionaries

dic = {
    'fname' : 'ahmad',
    'lname' : 'ali',
    'course' : 'python',
    'age' : 25,
    'email' : 'ahmadali@gmail.com',
    'phone' : '030012345678'
}

# this function is for lists not for dictionaries
for i in enumerate(dic):
    # print(i) # this will give the self made index and key of dictionary but not give the value of key
    print(f'key:{i[1]} -- value:{dic[i[1]]}')

# we should not use the upper function for dictionaries for dictionaries we have some other methods
# dic.items()
for item in dic.items():
    print(item) # output is in tuple form (key,value)
    print(f'key:{item[0]} -- value:{item[1]}')


# we can also save the  key and value in different variables by giving two variables in loop
for key,value in dic.items():
    print(f'key:{key} -- value:{value}')

# to get only keys of dictionary
for key in dic.keys():
    print(f'key:  {key}')

# to get only values of dictionary
for value in dic.values():
    print(f'value:  {value}')




# break--- this keyword is used to terminate the loop
for i in names:
    if(i is 'Farhan'):
        break
    else:
        print(i)

# continue--- this keyword is used to skip the next code of current iteration
for i in names:
    if i is 'Sultan':
        print('******')
        continue
    print(i) # if i is Sultan the print(i) will not executed




    print('***************')
# for else
# if the loop will run completely without any termination the else block will run
for i in names:
    print(i)
    # if i is 'Farhan': break # using this line the else will not run
    if i is 'Farhan': continue # using this line the else not run
else:
    print('Names are completed')


# While loop
    # with static vlaue
count = 5
while count>0:
    print(count)
    count-=1

    # with dynamic value
count = 5
run=True
while run:
    print('hi')
    count+=1
    if count is 8:
        run=False

