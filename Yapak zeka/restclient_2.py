# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 11:18:58 2024

@author: casper
"""

import json
import requests

url='http://127.0.0.1:8000/nemdurumu'

requests_data=json.dumps({'nem_durumu_il':'ankara'})
response=requests.post(url,requests_data)
print(response.text)
