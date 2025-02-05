import os
import sys

from train_audio1 import record_train1
from train_audio2 import record_train2
from train_audio3 import record_train3
from train_audio4 import record_train4
from train_audio5 import record_train5
from test_audio import record_test
from flask import jsonify
from flask import Flask,render_template,request
from werkzeug.utils import secure_filename
from sklearn.externals import joblib
sys.path.append('../')
from main import get_id_result


import os
UPLOAD_FOLDER = 'uploads/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')
def hello_world():
    return render_template('default.html')

@app.route('/trainaudiosave1',methods=['GET','POST'])
def trainaudiosave1():
    print("\n\n\nRunning\n\n\n\n")
    record_train1()
    return "done",200

@app.route('/trainaudiosave2',methods=['GET','POST'])
def trainaudiosave2():
    print("\n\n\nRunning\n\n\n\n")
    record_train2()
    return "done",200

@app.route('/trainaudiosave3',methods=['GET','POST'])
def trainaudiosave3():
    print("\n\n\nRunning\n\n\n\n")
    record_train3()
    return "done",200

@app.route('/trainaudiosave4',methods=['GET','POST'])
def trainaudiosave4():
    print("\n\n\nRunning\n\n\n\n")
    record_train4()
    return "done",200

@app.route('/trainaudiosave5',methods=['GET','POST'])
def trainaudiosave5():
    print("\n\n\nRunning\n\n\n\n")
    record_train5()
    return "done",200

@app.route('/testaudiosave',methods=['GET','POST'])
def testaudiosave():
    print("\n\n\nRunning\n\n\n\n")
    record_test()
    return "done",200
    
@app.route('/test',methods=['GET','POST'])
def trainaudio():
    print("\n\n\nRunning\n\n\n\n")
    a = get_id_result()
    print(a)
    data = {'status' : a}
    print(data)
    # response = app.response_class(
    #     response=data,
    #     status=200,
    #     mimetype='application/json'
    # )
    return jsonify(data)
    
if __name__ == '__main__':
    localhost = '127.0.0.1'
    app.run(host = localhost, port = 3000);