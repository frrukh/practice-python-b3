# decorators are used to decorate the function.
# they allow us to wrap around a function and modify its behavior without changing its source code.
def greet(function):
    def modified():
        print('Good Morning')
        function()  # calling the original function
        print('Good Bye !')
    return modified




@greet
def fun():
    print('hello !')

fun()