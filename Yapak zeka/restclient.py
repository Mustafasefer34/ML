# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 11:15:02 2024

@author: casper
"""

import json
import requests

url='http://127.0.0.1:8000/havadurumu'

requests_data=json.dumps({'hava_durumu_il':'izmir'})
response=requests.post(url,requests_data)
print(response.text)
