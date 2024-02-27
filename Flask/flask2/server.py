from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'this is home page.'

@app.route('/register', methods=['POST', 'GET'])
def  register():
    match request.method:
        case 'GET':
            return render_template('serverform.html')
        case 'POST':
            # request.files is used to get the files in a dictionary with same name as given in name of html.
            if request.files['given_file']: # i.e if the dictionary has a file by name 'given_file'.
                given_file = request.files['given_file'] # storing file in a variable
                filename = given_file.filename # storing the filename in a variable using 'filename' keyword.
                # saving the file at folder data present in main directory by name of filename.
                given_file.save('data/'+ filename)
            else:
                return 'no file uploaded.'





match __name__:
    case '__main__':
        app.run(debug=True, port=4040)