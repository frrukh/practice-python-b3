from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def main():
    return 'This is the Main Page!'


@app.route('/shop')
def shop():
    return 'This is the Shop Page'


# getting an argument from the url
@app.route('/name/<n>')
def name(n):
    return f'My name is {n}.'
# getting a float argument from url


@app.route('/num/<float:n>')
def float_num(n):
    return f'the given float number is {n}'
# getting a integer argument from url


@app.route('/num/<int:n>')
def integer(n):
    return f'the given integer number is {n}'


# getting a string argument from url
@app.route('/str/<string:n>')
def string(n):
    return f'the given string is "{n}".'


# redirect() - used to redirect to the specific url.
@app.route('/gotogoogle')
def google():
    return redirect('https://www.google.com')


# url_for() - used to make the link dynamic to redirection so we will use this instead of static url.
# syntax: url_for('functionName of this file')
@app.route('/gotomy/main')
def gotomain():
    return redirect(url_for('main'))


@app.route('/gotomy/shop')
def gotoshop():
    return redirect(url_for('shop'))


# syntax with argument: url_for('functionName',a='farrukh',b='maqsood')
# url_for() function takes single POSITIONAL argument so to pass the argument to the url we should use KEYWORD argument.
@app.route('/gotomy/name')
def my_name():
    return redirect(url_for('name',n='Muhammad.Farrukh.Maqsood'))


# passing the dynamic value in the parameter of targeted url.
@app.route('/gotomy/name/<i>')
def my_dynamic_name(i):
    return redirect(url_for('name',n=i))


match __name__:
    case '__main__':
        app.run(debug=True, port='8080')

# if __name__ == '__main__':
#     app.run(debug=True)
