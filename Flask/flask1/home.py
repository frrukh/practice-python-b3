# from flask import Flask, redirect, url_for

# app = Flask(__name__)


# @app.route('/')
# def main():
#     return 'This is Main Page.'

# @app.route('/home')
# def home():
#     return 'This is Home Page.'

# @app.route('/shop')
# def shop():
#     return 'This is Shop Page.'

# @app.route('/contact')
# def contact():
#     return 'This is Contact Page.'

# @app.route('/signup')
# def signup():
#     return 'This is Sign-up Page'

# @app.route('/google')
# def googlePage():
#     return 'This is Google Page.'

# # we can pass '<n>' in route (here '<>' are reserved keywords) so we can pass anything is the place of n and to use the value of 'n' in function we hove to pass it in the function by giving the parameter n to the function. 
# @app.route('/home/<n>')
# def name(n):
#     return f'My name is: {n}.'

# # we can also specify the type of n so if the user type in another datatype the browser shows page not found error.
# # there are 3 commonly using types:
# # <float:n>  --  <int:n>  --  <string:n>
# @app.route('/<int:n>')
# def int_number(n):
#     return f'the url is 127.0.0.1:3/{n}'


# @app.route('/gotopage')
# def red():
#     # redirect function is used to redirect the page to another page,url_for is used to make the url dynamic so it is better than the static url,in url for we should pass the name of the function of the required route and it takes only one positional argument but if the targeted function requires any argument then we can pass it in url_for function but it will not a POSITIONAL argument it will be KEYWORD argument.
#     return redirect(url_for('name',n='Farrukh Maqsood.'))



# @app.route('/redirect/<n>')
# def redirect_page(n):
#     match n:
#         case 'main':
#             return redirect(url_for('main'))
#         case 'home':
#             return redirect(url_for('home'))
#         case 'shop':
#             return redirect(url_for('shop'))
#         case 'contact':
#             return redirect(url_for('contact'))
#         case 'signup':
#             return redirect(url_for('signup'))
#         case 'google':
#             return redirect(url_for('googlePage'))
#         case 'name':
#             return redirect(url_for('name',n='Muhammad Farrukh Maqsood'))
#         case _:
#             return '<h1 style="color:red;">Please Enter a valid url</h1>'
        




# if __name__ == '__main__':
#     app.run(debug=True,port='3')