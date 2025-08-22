from flask import Flask,render_template,redirect,request,url_for
import pandas as pd
import numpy as np
import pickle

app=Flask(__name__)

with open("firstModel.pkl", "rb") as file:
    model = pickle.load(file)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method=='POST':
        cgpa=float(request.form.get('cgpa'))
        internships=float(request.form.get('internships'))
        inp_data=np.array([[cgpa,internships]])
        is_placed=model.predict(inp_data)
        if int(is_placed[0]):
            return redirect(url_for('ok_placed'))
        else:
            return redirect(url_for('not_placed'))
    return render_template('index.html')

@app.route('/ok_placed')
def ok_placed():
    return render_template('get_place.html')

@app.route('/not_placed')
def not_placed():
    return render_template('not_placed.html')

if __name__=="__main__":
    app.run(debug=True)