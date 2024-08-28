# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:59:17 2024

@author: casper
"""

import pickle 
import numpy as np
from flask import Flask, request 

app = Flask(__name__)

ml=pickle.load(open('randomforest.pickle','rb'))
sc=pickle.load(open('scRandom.pickle','rb'))

#Deneyim Yili	SuanCalisiyor?	Eski Calistigi Firmalar	Egitim Seviyesi	Top10 Universite?	StajBizdeYaptimi?
@app.route('/iseAlim',methods=['POST'])

def seker_hastalik_tahmin():
    request_data=request.get_json(force=True)
    deneyimyili=request_data['deneyimyili']
    suancalisiyor=request_data['suancalisiyor']
    eskicalistigifirmalar=request_data['eskicalistigifirmalar']
    egitimseviyesi=request_data['egitimseviyesi']
    top10universite=request_data['top10universite']
    stajbizdeyaptimi=request_data['stajbizdeyaptimi']
    
    
    new_prediction=ml.predict(sc.transform(np.array([[deneyimyili,suancalisiyor,eskicalistigifirmalar,egitimseviyesi,top10universite,stajbizdeyaptimi]])))
    
     
    return "Tahmin: {}".format(new_prediction)
 
if __name__ == "__main__":
    app.run(port=8000,debug=True)