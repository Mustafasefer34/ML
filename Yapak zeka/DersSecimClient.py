# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:54:35 2024

@author: casper
"""
import json
import requests

url='http://127.0.0.1:8000/derssecim'

requests_data=json.dumps({'derssecim1':'Türkçe'})
response=requests.post(url,requests_data)
print(response.text)
