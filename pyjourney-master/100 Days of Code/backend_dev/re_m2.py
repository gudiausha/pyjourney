from flask import Flask,request,render_template,redirect,jsonify
import json
import os
from werkzeug.utils import secure_filename
import requests
import webbrowser

app = Flask(__name__)

@app.route('/dev/m2/task2',methods=['GET','POST'])
def m2_service():
    # file1 = 'C:/Users/USER/Desktop/python/biden.jpg'
    # file2 = 'C:/Users/USER/Desktop/python/obama.jpg'
    # input = {"file1":file1 , "file2":file2}
    content = requests.get('http://127.0.0.1:5000/dev/m1/task1')
    webbrowser.open('http://127.0.0.1:5000/dev/m1/task1')
    print(content.url)
    # return(render_template('m1.html'))
    return('message from microservice-1 ')

if __name__ == "__main__":
    app.run(port=5002, debug=True)
