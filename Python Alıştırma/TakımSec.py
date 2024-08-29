# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 16:01:25 2024

@author: casper
"""

from flask import Flask, request

app=Flask(__name__)

@app.route('/takımSec', methods=['POST'])

def takım_sec():
    request_data=request.get_json(force=True)
    takım_sec_2=request_data['takımSec1']
    
    if(takım_sec_2=="Galatasaray"):
        cevap="Galatasaray seçildi".format(takım_sec_2)
    elif(takım_sec_2=="Fenerbahçe"):
        cevap="Fenerbahçe seçildi".format(takım_sec_2)
        
        
    return cevap



if __name__ == "__main__":
    app.run(port=8000,debug=True)