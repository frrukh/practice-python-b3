# list comprehension is a simple way to make the for loops on list in single line

# without list comprehension:
a = [0,1,2,3,4,5,6,7,8,9]
b = []
for i in a:
    b.append(i+1)

print(b)

# with list comprehension
# Flow: in list comprehension first we have to make a list and make what to do with it. like simply write it eg. [x for x....] or sum a value in it eg. [x+3 for x....] then there are two options:

# 1-- first option is to write a for loop:

# without list comprehension
c = [0,1,2,3,4,5]
d = []
for i in c:
    d.append(i+2)

print(d)

# with list comprehension

c = [0,1,2,3,4,5]
d = [i+2 for i in c]

print(d)

# 2-- second option is to write a for loop with if condition:

# without list comprehension
e = [0,1,2,3,4,5,6]
f = []

for i in e:
    if i < 4:
        f.append(i)

print(f)

# with list comprehension
e = [0,1,2,3,4,5,6]
f = [i for i in e if i < 4]
print(f)




# we can also use if condition on the result coming from the loop after this like with x in [x for...]

# for example if we want to duplicate a list with keeping the check that if 3 is in the current iteration it will changed to 0


g = [1,2,3,4,5,3]
h = [x if x != 3 else 0 for x in g]

print(h)