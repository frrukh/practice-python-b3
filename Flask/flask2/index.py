from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is home page'

# render_template() - it is used to render our html page on the live browser.
# first we have to make a folder by name 'templates' that will hold your html files.
# then we have to make a route and in the function of route we have to return render_template function with the parameter of html file name that is present in templates.
# render_template function automatically target the templates folder so we do't need to give the path of the templates folder.but if the file is in a subdirectory of templates directory then the path will be needed.
@app.route('/wordlist')
def words():
    return render_template ('wordlist.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/todo')
def todo():
    return render_template('todo app.html')

@app.route('/weather')
def weather():
    return render_template('weather.html')

@app.route('/signup')
def signup():
    return render_template('form.html')


# GETTING INFORMATION FROM FORMS.
# to get the data from the form we have to define the from which method we will get data.
# we can define multi methods to get data.
# 5 https methods : ['GET','POST','PUT','DELETE','HEAD']
@app.route('/formdata',methods=['POST','GET'])
def form_data():
    # request.method is used to get method of request i.e the method is get or post or other.
    match request.method:
        # request.args (i.e arguments) is used to get the values from the from if the method is GET.
        # so in case of 'GET' we use request.args
        case 'GET':
            return request.args
        case 'POST':
            # request.form is used to get the data from form if the https method is 'POST'.
            # so in case of 'POST' we use request.form
            return request.form

@app.route('/form2')
def form2():
    return render_template('form2.html')

# STORING IN VARIABLE AND RESENDING TO HTML PAGE,THE INFORMATION GOT FROM FORM.
@app.route('/save',methods=['POST'])
def save():
    data = request.form
    return render_template('formData.html', data=data)

match __name__:
    case '__main__':
        app.run(debug=True,port=3030)
