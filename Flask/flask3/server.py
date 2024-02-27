from flask import Flask, render_template,request, redirect, url_for, flash
# importing the connect class from connector module to connect with database.
from mysql.connector import connect

app = Flask(__name__)
# making an object of connect class.
# connect class takes four keyword arguments.
# 1-- host  2--user  3--password  4--database
connection = connect(host='localhost',user='root',password='',database='flask-3')
app.secret_key='33e3'

@app.route('/')
def home():
# now we will get data from database and pass it in html to display.
    # making connection with database
    db = connection.cursor()
    # getting data from database.
    # while getting data the data automatically saved in the variable on which the execute function is called i.e in our case d
    db.execute('SELECT * from users')
    # fetching the data from the 'd' in a variable
    # using fetchall() method we can get all the data in the form of 2d list.
    data = db.fetchall()
    # the data variable has a 2d list saved in it like [[1,ali,aslam,ali@gmail.com,admin],[2,..]]
    # return data

    # passing the data of all users to the html page.
    return render_template('home.html',users=data)

@app.route('/signup')
def signup():
    return render_template('form.html')


@app.route('/register',methods=['POST'])
def register():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    if first_name and email and password and confirm_password and password == confirm_password: 
        # running cursor function on object of class 'connect' to make a connection of the object(connection which object of class 'connect') with database.
        # saving this connection(with database) is a variable to make some modification on this function.
        db = connection.cursor() 
        # execute function is used to execute the sql queries in python.
        # inserting data in the connection object using db variable.
        db.execute('INSERT INTO users (first_name,last_name,email,password) VALUES(%s,%s,%s,%s)',(first_name,last_name,email,password))
        # submitting/saving the connection object in database.
        # the data inserted in our connection object is saved in it now we are submitting the connection object in the database.
        connection.commit()
        # as we have done our work now we are destroying the connection to prevent the data from hackers.
        # so the connection is going to close using method close() on db.
        db.close()
        flash('Registered Successfully','success')
        return redirect(url_for('home'))
    else:
        return redirect(url_for('signup'))
    

@app.route('/edit/<id>',methods=['GET','POST'])
def edit(id):
    if request.method == 'GET':
        db = connection.cursor()
        # we used (id,) to prevent our program from ERROR as python interpreter do't assumes tuple with single value as tuple. 
        # db.execute('SELECT first_name,last_name,email,id FROM users WHERE id=%s',(id,))
        db.execute(f'SELECT id,first_name,last_name,email FROM users WHERE id={id}')
        # select query always returns its value and to get it we have to fetch.
        data = db.fetchone()
        connection.commit()
        db.close()
        # we can't display data coming from fetch one as it is.
        return render_template('edit.html',data=data)
    else:
        request.form
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        if first_name and email:
            db = connection.cursor()
            db.execute('UPDATE users SET first_name=%s,last_name=%s ,email=%s WHERE id=%s',(first_name,last_name,email,id))
            connection.commit()
            db.close()
            return redirect(url_for('home'))


@app.route('/delete/<id>')
def delete(id):
    db = connection.cursor()
    # in %s concatenation we have to give a tuple as a second argument but tuple having a single value is not considered as a tuple by python interpreter so it will show an ERROR.
    # to fix this error we play a trick with python interpreter i.e we just add a comma after the value of tuple so the python interpreter becomes happy and do't pass ERROR.  

    # so we write :   (id,)
    db.execute('DELETE FROM users WHERE id=%s',(id,))
    connection.commit()
    db.close()
    return redirect(url_for('home'))


match __name__:
    case '__main__':
        app.run(debug=True,port=8000)