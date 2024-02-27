from flask import Flask, render_template, request, redirect, url_for
from mysql.connector import connect

app = Flask(__name__)
connection = connect(host='localhost',user='root',password='',database='database1')

@app.route('/')
def home():
    db=connection.cursor()
    # db.execute('SELECT * FROM users WHERE id = 1')
    # data = db.fetchone()
    db.execute('SELECT * FROM users')
    data = db.fetchall()
    return render_template('home.html',data=data)


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.form
    first_name=data['first_name']
    last_name=data['last_name']
    email=data['email']
    password=data['password']
    confirm_password=data['confirm_password']
    if first_name and email and password and confirm_password and password == confirm_password:
        db = connection.cursor()
        db.execute('INSERT INTO users (first_name,last_name,email,password) VALUES(%s,%s,%s,%s)',(first_name,last_name,email,password))
        # db.execute(f'INSERT INTO users (first_name,last_name,email,password) VALUES({first_name},{last_name},{email},{password})')
        connection.commit()
        db.close()
        return redirect(url_for('home'))
    else:
        return redirect(url_for('signup'))


if __name__ == '__main__':
    app.run(debug=True,port=3030)