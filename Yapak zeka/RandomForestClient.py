# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 14:24:44 2024

@author: casper
"""

import json
import requests

url='http://127.0.0.1:8000/iseAlim'

#Deneyim Yili	SuanCalisiyor?	Eski Calistigi Firmalar	Egitim Seviyesi	Top10 Universite?	StajBizdeYaptimi?
requests_data=json.dumps({'deneyimyili':0,'suancalisiyor':0,'eskicalistigifirmalar':0,'egitimseviyesi':0,'top10universite':0,'stajbizdeyaptimi':0})
response=requests.post(url,requests_data)
print(response.text)