# In object oriented programming we can define a class having some functions and then make an object of that class and call the defined functions in method form i.e object.methodName()

# define a class
# class keyword is used to define a new class
# syntax:   class ClassName:
class MyClass:
    # __init__ function is a by default function and will added in every class.it will run automatically when we define a object of the class
    # it is also called constructor of the class.


    # Here we use self keyword in parameter.so when we initialize the object of this class the name of object will automatically comes in the parameter.
    # self is used in every parameter.--- self=object
    def __init__(self):
        # In farrukh object we are initializing name of farrukh i.e self.farrukh
        self.Name='ali'
        # In farrukh object we are initializing class of farrukh i.e Class.farrukh
        self.Class=12
        # In farrukh object we are initializing gender of farrukh i.e gender.farrukh
        self.gender='male'
        print(f'Name: {self.Name} --- Class: {self.Class} --- Gender:{self.gender}')
    

    def display_name(self):
        print(f'Name: {self.Name}')


    def display_class(self):
        print(f'Class: {self.Class}')


    def display_gender(self):
        print(f'Gender: {self.gender}')


    def display_all(self):
        print(f'Name: {self.Name}')
        print(f'Class: {self.Class}')
        print(f'Gender: {self.gender}')

    
    def self(self):
        print(self)


farrukh=MyClass()
print(farrukh.Name)
print(farrukh.Class)
print(farrukh.gender)
farrukh.display_name()
farrukh.display_class()
farrukh.display_gender()
farrukh.display_all()

print(farrukh)





# In python the global variable can accessed in function but can't modified in function or any block of code if we try to  do so python will define a new variable in that block,to get modify the global variable in function first we should use global keyword to tell that teh variable after global keyword is the variable that is defined globally and can be modified.
name='robin'
def fun():
    global name
    name='roooobin'


fun()
print(name)


farrukh.self()