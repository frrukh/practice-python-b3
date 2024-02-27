# Tuples
# tuples are same like lists but they are defined with parentheses and they are immutable so we can't make any change in tuples

# initialization
tup=(1,2,3,4)

# access
print(tup)
print(tup[1])

# check type
print(type(tup))
print(isinstance(tup,tuple))

# delete
# del tup[0] # it does't works as tuples are immutable
del tup
# print(tup)

# tuple Methods
# 1---tupleName.count(value whose repetition count is required)
tupl=(1,2,3,1,1,1)
count=tupl.count(1)
print(f'count: {count}')

# 2---tupleName.index(value whose index is required) works on first occurred value
tupl=(1,2,3,2,1,1,1)
index=tupl.index(2)
print(index)

# dictionary
# the object of Javascript is called the dictionary in python

# initialization
dic={
    'name':'Ali',
    'class':'python',
    'roll_num':12,
    'phone':'03040303033'
}

# access
print(dic)
print(dic['name'])

# updating a key
dic['roll_num']=22
print(dic)

# adding new key
dic['f_name']='Ahmed'
print(dic)

# delete any key form dictionary
del dic['f_name']
print(dic)

# delete the dictionary
del dic 
# print(dic) # --- it will throw error of undefined as dictionary had been deleted 
