# In python arrays are called lists.

# creating a new list
li=[1,2,3,4]
# accessing list with index
print(li)
print(li[1])

# update list item or list
li[3]=5
print(li)
li=[5,4,3,2,1]
print(li)

# check type
print(type(li))

# compare type
#       Method-1
# syntax : isinstance(object,type to compare with)
print(isinstance(li,int))
print(isinstance(li,float))
print(isinstance(li,str))
print(isinstance(li,bool))
print(isinstance(li,list)) # true
print(isinstance(li,tuple))
print(isinstance(li,dict))

#       Method-2
# syntax type(object) is type to compare with
if type(li) is list:
    print('li is a list')
else:
    print('li is not a list')

# get the length of list
# syntax : len(object)
list=[1,2,3,4,5,6,7,8,9]
length=len(list)
print(length)

# List Methods

# 1--- listName.append(single value)--- to add a single item in the last of list
list=[1,2,3,4,5]
list.append(2) # it takes only one argument
print(list)

# 2--- listName.extend([always take a single list])--- to add single as well as multiple items in the end of the list
list=[1,2,3,4,5]
list.extend([1,2,3]) # it also takes only one argument but in list form and add the items of this list at the end of the targeted list.
print(list)

# 3--- listName.insert(index,value to insert)--- to add not replace a value at specific index
list=[1,2,3,4]
list.insert(0,'added by insert')
print(list)

# 3--- listName.remove(value to remove)--- to remove the given value that occurred first in the list 
list=[19,2,19,3,4,5]
list.remove(19)
print(list)

# 4--- listName.pop()
#       Use 1: it removes the last value and return the removed value
list=[1,2,3,4,5]
removed=list.pop()
print(list)
print(removed)
#       Use 2: it removes the value of given index and return the removed value
list=[1,2,3,4,5]
removed=list.pop(0) # here 0 is index not value
print(list)
print(removed) # --- 1

# 5--- listName.index(value whose index is required)--- to get the index of first occurred given value
list=[2,2,5,3,4,2,4,6]
index=list.index(2) # targets the first 2
print(index)

# 6--- listName.count(value whose repetition count is required)--- to get how many times the number is occurred in list
list=[1,2,3,4,2,3,2] 
count=list.count(2)
print(count) # --- 3 as 2 is three times in list

# 7--- listName.sort()--- to sort the list
        #   Ascending
list=[2,4,1,3,6,5]
list.sort()
print(list) #--- [1,2,3,4,5,6]
        # Descending
list=[2,4,1,3,6,5]
list.sort(reverse=True) # --- by default it is false
print(list) #--- [6,5,4,3,2,1]

# 8--- listName.reverse()--- not sort just reverse the list
list=[1,2,4,3]
list.reverse()
print(list) #--- [3,4,2,1]

# 9--- listName.copy()--- to make a copy of list
list=[2,1,2]
list_copy=list.copy()
print(list_copy) #--- [2,1,2]

# 10--- listName.clear()--- to make the list empty
list=[1,2,3]
list.clear()
print(list) #--- []



# 'in' keyword to check weather item is present in the list of not
list=[2,'far',4,'farrukh']
if 'farrukh' in list:
    print('present')
else:
    print('not present')



