# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:18:57 2024

@author: casper
"""
import pickle 
import numpy as np
from flask import Flask, request 

app = Flask(__name__)

ml=pickle.load(open('knnmodel.pickle','rb'))
sc=pickle.load(open('sc.pickle','rb'))

#	Pregnancies	Glucose	BloodPressure	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age	
@app.route('/sekerhastaliktahmin',methods=['POST'])

def seker_hastalik_tahmin():
    request_data=request.get_json(force=True)
    pregnancies=request_data['pregnancies']
    glucose=request_data['glucose']
    bloodPressure=request_data['bloodPressure']
    skinThickness=request_data['skinThickness']
    insulin=request_data['insulin']
    bmi=request_data['bmi']
    diabetesPedigreeFunction=request_data['diabetesPedigreeFunction']
    age=request_data['age']
    
    new_prediction=ml.predict(sc.transform(np.array([[pregnancies,glucose,bloodPressure,skinThickness,insulin,bmi,diabetesPedigreeFunction,age]])))
     
    return "Tahmin: {}".format(new_prediction)
 
if __name__ == "__main__":
    app.run(port=8000,debug=True)
