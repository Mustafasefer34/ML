# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script fil
"""
from flask import Flask, request

app=Flask(__name__)

@app.route('/derssecim',methods=['POST'])

def ders_secim():
    request_data=request.get_json(force=True)
    ders_secim=request_data['derssecim1']
    
    if(ders_secim=="Matematik"):
        cevap="Matematik dersini seçtiniz".format(ders_secim)
    elif(ders_secim=="Türkçe"):
        cevap="Türkçe dersini seçtiniz".format(ders_secim)
    elif(ders_secim=="Kimya"):
        cevap="Kimya dersini seçtiniz".format(ders_secim)
        
    return cevap


if __name__ == "__main__":
    app.run(port=8000,debug=True)