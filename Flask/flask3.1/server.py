from flask import Flask, render_template, redirect, url_for, request, flash
from mysql.connector import connect

app = Flask(__name__)
connection = connect(host='localhost',user='root',password='',database='flask3.1')
app.secret_key='donno5555'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/quiz_app')
def quiz():
    return render_template('quiz.html')

@app.route('/todo_app')
def todo():
    return render_template('todo.html')

@app.route('/weather_app')
def weather():
    return render_template('weather.html')

@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    else:
        first_name=request.form['first_name']
        last_name=request.form['last_name']
        email=request.form['email']
        password=request.form['password']
        confirm_password=request.form['confirm_password']
        if first_name and email and password and confirm_password and password==confirm_password:
            db = connection.cursor()
            db.execute('INSERT INTO users (first_name,last_name,email,password) VALUES(%s,%s,%s,%s)',(first_name,last_name,email,password))
            connection.commit()
            db.close()
            flash("You have successfully signed up!","success")
            return redirect(url_for('home'))
        else:
            flash("Please fill out all the fields correctly!",'danger')
            return redirect(url_for('signup'))
        
@app.route('/usersdata')
def usersdata():
    db = connection.cursor()
    db.execute("SELECT * from users")
    data = db.fetchall()
    connection.commit()
    db.close()
    return render_template('users.html',users=data)


@app.route('/edit/<id>',methods=['GET','POST'])
def edit(id):
    if request.method == 'GET':
        db = connection.cursor()
        db.execute('SELECT id,first_name,last_name,email FROM users where id=%s',(id,))
        data = db.fetchone()
        connection.commit()
        db.close()
        return render_template('edit.html',data=data)
    else:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        if first_name and email:
            db = connection.cursor()
            db.execute('UPDATE users SET first_name=%s, last_name=%s, email=%s  WHERE id=%s',(first_name,last_name,email,id))
            connection.commit()
            db.close()
            flash(f'User {id} has been Updated successfully!','success')
            return redirect(url_for('usersdata'))
@app.route('/delete/<id>')
def delete(id):
    db = connection.cursor()
    db.execute('DELETE FROM users WHERE id=%s',(id,))
    connection.commit()
    db.close()
    flash(f'User {id} has been deleted!','danger')
    return redirect(url_for('usersdata'))

if __name__ == '__main__':
    app.run(debug=True,port=3030)