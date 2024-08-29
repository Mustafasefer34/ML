# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:31:40 2024

@author: casper
"""

import json 
import requests

url='http://127.0.0.1:8000/sarkıtursecimi'

requests_data=json.dumps({'şarkıtursecimi':'Klasik'})
response=requests.post(url, requests_data)
print(response.text)
