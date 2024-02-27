from flask import Flask, render_template, redirect, url_for, request, flash, session
from mysql import connector
import json

app = Flask(__name__)
connection = connector.connect(host='localhost',user='root',password='',database='flask4')
app.secret_key = 'fasdiofklsdanvqwe'
@app.route('/')
def home():
    user_name = session.get('user_name',None)
    is_admin = session.get('is_admin',0)
    return render_template('home.html',user_name=user_name, is_admin = is_admin)

@app.route('/quiz')
def quiz():
    user_name=session.get('user_name',None)
    is_admin = session.get('is_admin',0)
    if user_name is not None:
        db = connection.cursor()
        db.execute('SELECT title,options,correctAnswer FROM questions')
        questions = db.fetchall()
        db.close()
        quiz_questions=[]
        for question in questions:
            current_question={
                'title' : question[0],
                'options' : json.loads(question[1]),
                'correctAnswer' : question[2]
            }
            quiz_questions.append(current_question)
        
        return render_template('quiz.html',user_name=user_name,questions = quiz_questions, is_admin = is_admin)
    else:
        flash('please login first!','warning')
        return redirect(url_for('login'))

@app.route('/todo')
def todo():
    user_name=session.get('user_name',None)
    is_admin = session.get('is_admin',0)
    if user_name is not None:
        return render_template('todo.html',user_name=user_name, is_admin = is_admin)
    else:
        flash('please login first!','warning')
        return redirect(url_for('login'))


@app.route('/weather')
def weather():
    user_name=session.get('user_name',None)
    is_admin = session.get('is_admin',0)
    if user_name is not None:
        return render_template('weather.html',user_name=user_name ,is_admin = is_admin)
    else:
        flash('please login first!','warning')
        return redirect(url_for('login'))


@app.route('/signup',methods=['GET','POST'])
def signup():
    adminCode='1234567890'
    error = False
    if request.method == 'GET':
        user_name = session.get('user_name',None)
        is_admin = session.get('is_admin',0)
        return render_template('signup.html',user_name = user_name ,is_admin = is_admin)
    else:
        # return request.form
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        admin = request.form.get('is_admin',0)
        admin_code = request.form.get('admin_code','')
        if not first_name:
            flash('First name is required!','danger')
            error = True
        if not email:
            flash('email is required!','danger')
            error = True
        
        if not password:
            flash('Password is required!','danger')
            error = True
        if not confirm_password:
            flash('Confirm password is required!','danger')
            error = True
        if password != confirm_password:
            flash('Password does\'t match!','danger')
            error = True
        if admin=='1':
            if admin_code == '':
                flash('Admin code required!','danger')
                error = True
            elif admin_code == adminCode:
                session['is_admin']= 1
            else:
                flash('please enter a valid admin code!','danger')
                error=True

        if error == True:
            return redirect(url_for('signup'))
        else:
            email = request.form['email']
            db = connection.cursor()
            db.execute('SELECT * FROM users WHERE email=%s',(email,))
            is_exist = db.fetchall() 
            # is_exist = db.fetchone() 
            db.close()
            if is_exist:
                flash('email already exist!','warning')
                return redirect(url_for('signup')) 
            db = connection.cursor()
            db.execute('INSERT INTO users (first_name,last_name,email,password,is_admin) VALUES(%s,%s,%s,%s,%s)',(first_name,last_name,email,password,session.get('is_admin',0)))
            connection.commit()
            db.close()
            db = connection.cursor()
            db.execute('SELECT id FROM users WHERE email=%s',(email,))
            id_obj = db.fetchall()
            id=id_obj[0][0]
            db.close()
            session['id'] = id
            session['user_name'] = f'{first_name} {last_name}'
            flash('The Signup process has been completed successfully!','success')
            return redirect(url_for('home'))


@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        user_name = session.get('user_name',None)
        is_admin = session.get('is_admin',0)
        return render_template('login.html',user_name=user_name ,is_admin = is_admin)
    else:
        email = request.form['email']
        password = request.form['password']
        if email and password:
            db = connection.cursor()
            db.execute('SELECT * FROM users WHERE email=%s and password=%s',(email,password))
            user = db.fetchall()
            # user = db.fetchone()
            db.close()
            
            # if user is not None:
            if len(user) > 0:
                session['id'] = user[0][0]
                session['user_name'] = f'{user[0][1]} {user[0][2]}'
                session['is_admin']= user[0][5]
                flash('login process completed successfully!','success',)
                return redirect(url_for('home'))
            else:
                flash('user not found','danger')
                return redirect(url_for('login'))
        else:
            flash('invalid entries','danger')
            return redirect(url_for('login'))
    

@app.route('/logout')
def logout():
    if session.get('user_name',None):
        flash('user logged out successfully!','success')
    else:
        flash('please login first!','warning')

    session.pop('id',None)
    session.pop('user_name',None)
    session.pop('is_admin',0)
    return redirect(url_for('login'))


@app.route('/addquestion',methods=['GET','POST'])
def addquestion():
    user_name = session.get('user_name',None)
    is_admin = session.get('is_admin',0)
    if user_name is None:
        flash('Kindly login first!','warning')
        return redirect(url_for('login'))
    elif is_admin:
        if request.method == 'GET':
            return render_template('addques.html',user_name = user_name ,is_admin = is_admin)
        else:
            error = False
            option_error = False
            title = request.form['title']
            options = request.form.getlist('option')
            answer = request.form['answer']
            if not title:
                flash('Title is required!','danger')
                error = True

            for option in options:
                if not option:
                    if not option_error:
                        flash('All options are required!','danger')
                        option_error = True
                        error=True
                        break
            if not answer:
                flash('Correct answer is required!','danger')
                error = True
            if error:
                return redirect(request.url)
            else:
                options = json.dumps(options)
                db = connection.cursor()
                db.execute('INSERT INTO questions (title,options,correctAnswer) VALUES(%s,%s,%s)',(title,options,answer))
                connection.commit()
                db.close()
                flash("Question added Successfully","success")
                return redirect(url_for('questions'))
    else:
        flash("Access prevision prohibited!",'danger')
        return redirect(url_for('home'))

@app.route('/questions')
def questions():
    user_name = session.get('user_name',None)
    is_admin = session.get('is_admin',0)
    if user_name is None:
        flash('please login first','warning')
        return redirect(url_for('login'))
    elif is_admin:
        db = connection.cursor()
        db.execute('SELECT * FROM questions')
        all_questions = db.fetchall()
        db.close()
        user_name = session.get('user_name',None)
        is_admin = session.get('is_admin',0)
        return render_template('questions.html',user_name = user_name ,is_admin = is_admin ,questions = all_questions)
    else:
        flash('Access prevision prohibited!','danger')
        return redirect(url_for('home'))
    

@app.route('/question/edit/<int:id>', methods=['GET','POST'])
def edit(id):
    user_name = session.get('user_name',None)
    is_admin = session.get('is_admin',0)
    if user_name is None:
        flash('please login first','warning')
        return redirect(url_for('login'))
    elif is_admin:
        if request.method == 'GET':
            db = connection.cursor()
            db.execute(f'SELECT * FROM questions WHERE id = {id}')
            # data = db.fetchone()
            # the data is in this form : [(0,title,[options],answer...)]
            # so it is on index 0 i.e is a tuple 
            data_tuple = db.fetchall()
            db.close()
            # now we have to convert the options array in array form using json.
            # as it is placed in a tuple and we can't make any change directly in tuple so first we have change it into an array.
            data = list(data_tuple[0])
            data[2] = json.loads(data[2])
            user_name = session.get('user_name',None)
            is_admin = session.get('is_admin',0)
            return render_template('editQuestion.html', user_name = user_name,is_admin=is_admin , data = data)
        else:
            error = False
            option_error = False
            title = request.form['title']
            options = request.form.getlist('option')
            answer = request.form['answer']
            if not title:
                flash('Title is required!','danger')
                error = True

            for option in options:
                if not option:
                    if option_error is True:
                        break
                    flash('All options are required!','danger')
                    option_error = True
                    error = True

            if not answer:
                flash('Correct Answer is required!','danger')
                error = True
        if error:
            return redirect(request.url)
        else:
            options = json.dumps(options)
            db = connection.cursor()
            db.execute('UPDATE questions SET title = %s ,options = %s, correctAnswer = %s WHERE id = %s',(title,options,answer,id))
            connection.commit()
            db.close()
            flash('Question updated successfully!','success')
            return redirect(url_for('questions'))
    else:
        flash('Access prevision prohibited!','danger')
        return redirect(url_for('home'))


@app.route('/question/delete/<int:id>')
def delete(id):
    user_name = session.get('user_name',None)
    is_admin = session.get('is_admin',0)
    if user_name is None:
        flash('please login first','warning')
        return redirect(url_for('login'))
    elif is_admin:
        db = connection.cursor()
        db.execute(f'DELETE FROM questions WHERE id={id}')
        connection.commit()
        db.close()
        flash('Question has been deleted successfully!','success')
        return redirect(url_for('questions'))
    else:
        flash('Access prevision prohibited!','danger')
        return redirect(url_for('home'))

@app.route('/users')
def users():
    user_name = session.get('user_name',None)
    is_admin = session.get('is_admin',0)
    if user_name is None:
        flash('please login first','warning')
        return redirect(url_for('login'))
    elif is_admin:
        db = connection.cursor()
        db.execute('SELECT * FROM users')
        users = db.fetchall()
        db.close()
        user_name = session.get('user_name',None)
        is_admin = session.get('is_admin',0)
        return render_template('users.html',users=users ,user_name=user_name ,is_admin = is_admin)
    else:
        flash('Access prevision prohibited!','danger')
        return redirect(url_for('home'))

@app.route('/user/edit/<int:id>',methods={'GET','POST'})
def edit_user(id):
    adminCode='1234567890'
    if request.method == 'GET':    
        user_name = session.get('user_name',None)
        is_admin = session.get('is_admin',0)
        if user_name is None:
            flash('please login first','warning')
            return redirect(url_for('login'))
        elif is_admin:
            db = connection.cursor()
            db.execute('SELECT * FROM users WHERE id = %s',(id,))
            data = db.fetchall()
            db.close()
            user_name = session.get('user_name',None)
            is_admin = session.get('is_admin',0)
            return render_template("edit_user.html" ,user_name = user_name ,is_admin = is_admin ,data = data[0],adminCode=adminCode)
        else:
            flash('Access prevision prohibited!','danger')
            return redirect(url_for('home'))
    else:
        error=False
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        is_admin = request.form.get('is_admin',0)
        admin_code = request.form.get('admin_code','')
        if not first_name:
            flash('First name is required!','danger')
            error = True
        if not email:
            flash('email is required!','danger')
            error = True
        if not password:
            flash('Password is required!','danger')
            error = True
        if is_admin=='1':
            if admin_code == '':
                flash('Admin code required!','danger')
                error = True
            elif admin_code == adminCode:
                pass
            else:
                flash('please enter a valid admin code!','danger')
                error=True

        if error == True:
            return redirect(request.url)
        else:
            db = connection.cursor()
            db.execute('UPDATE users SET first_name=%s ,last_name=%s ,email=%s ,password=%s ,is_admin=%s WHERE id=%s',(first_name,last_name,email,password,is_admin,id))
            connection.commit() 
            db.close()
            flash('User successfully updated!','success')
            return redirect(url_for('users'))


@app.route('/user/delete/<int:id>')
def delete_user(id):
    user_name = session.get('user_name',None)
    is_admin = session.get('is_admin',0)
    if user_name is None:
        flash('please login first','warning')
        return redirect(url_for('login'))
    elif is_admin:
        db = connection.cursor()
        db.execute('DELETE FROM users WHERE id=%s',(id,))
        connection.commit()
        db.close()
        flash(f'user {id} has been deleted successfully!','success')
        return redirect(url_for('users'))
    else:
        flash('Access prevision prohibited!','danger')
        return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True,port=8080)
