# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 16:08:21 2024

@author: casper
"""

import json
import requests

url='http://127.0.0.1:8000/takımSec'

request_data=json.dumps({'takımSec1':'Fenerbahçe'})

response=requests.post(url, request_data)

print(response.text)