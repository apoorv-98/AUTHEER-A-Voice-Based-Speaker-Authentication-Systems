from flask import Flask,render_template,request
from werkzeug.utils import secure_filename

import os
UPLOAD_FOLDER = 'uploads/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')
def hello_world():
    return render_template('default.html');

@app.route('/trainaudiosave',methods=['GET','POST'])
def trainaudiosave():
     if request.method == 'POST':
        file = request.files['train_data']
        filename = secure_filename(file.filename)
        file.save(os.path.join('../', filename))
        f = open("../cfg/enroll_list.csv","w");
        f.write(filename);
        return "done",200

@app.route('/testaudiosave',methods=['GET','POST'])
def testaudiosave():
     if request.method == 'POST':
        file = request.files['test_data']
        filename = secure_filename(file.filename)
        file.save(os.path.join('../', filename))
        f = open("../cfg/test_list.csv","w");
        f.write(filename);
        return "done",200
    
@app.route('/test',methods=['GET','POST'])
def trainaudio():
    f = open("cfg/enroll_list.csv","r");
    print(f.read())
    return "done",200
    
if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 3000);