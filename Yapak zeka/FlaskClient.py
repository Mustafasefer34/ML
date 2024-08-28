# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:29:49 2024

@author: casper
"""

import json
import requests

url='http://127.0.0.1:8000/sekerhastaliktahmin'

#	Pregnancies	Glucose	BloodPressure	SkinThickness	Insulin	BMI	DiabetesPedigreeFunction	Age	
requests_data=json.dumps({'pregnancies':1,'glucose':85,'bloodPressure':66,'skinThickness':29,'insulin':0,'bmi':26.6,'diabetesPedigreeFunction':0.351,'age':31})
response=requests.post(url,requests_data)
print(response.text)