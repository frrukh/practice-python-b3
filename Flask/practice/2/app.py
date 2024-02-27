from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is home page.'

@app.route('/weather')
def weather_app():
    return render_template('weather.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/save',methods=['POST','GET'])
def save():
    if request.method=='GET':
        data = request.args
        return render_template('formdata.html',info=data)
    else:
        data = request.form
        return render_template('formdata.html',info=data)
    
# getting files from form.
@app.route('/uploadfiles')
def files():
    return render_template('fileform.html')

@app.route('/savefile', methods=['POST'])
def davefile():
    if request.files['file']:
        file = request.files['file']
        file_name = file.filename
        file.save('data/'+ 'file1.jpg')
        return 'the file has been saved.'
    else:
        return 'file not found.'

match __name__:
    case '__main__':
        app.run(debug=True,port=3232)