# # from flask module we are importing class Flask
# from flask import Flask
# # initializing the website
# app = Flask(__name__)
# # providing the route of the main page
# @app.route('/')
# def main():
#     return 'this is main landing page.'
# # providing the route of home page
# @app.route('/home')
# def home():
#     return 'Home'
# # if we import this file as a module the app.run() will also executed to prevent this we are making a check i.e if __name__(the name of executing file)==__main__ i.e if this file is executing run app but if this file is imported in another file the value of __name__ will be the name of the file like (app.py).so in case of importing the file the app will not run.
# if __name__ == "__main__":
#     app.run(debug=True,port='90')