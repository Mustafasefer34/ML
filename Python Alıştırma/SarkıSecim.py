# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 14:25:15 2024

@author: casper
"""

from flask import Flask, request

app=Flask(__name__)

@app.route('/sarkıtursecimi',methods=['POST'])

def sarki_secim():
    request_data=request.get_json(force=True)
    sarki_secim_sonuc=request_data['şarkıtursecimi']
    
    if(sarki_secim_sonuc=="Pop"):
        cevap="Pop türünü seçtiniz".format(sarki_secim_sonuc)
    elif(sarki_secim_sonuc=="Rock"):
        cevap="Rock türünü seçtiniz".format(sarki_secim_sonuc)
    elif(sarki_secim_sonuc=="Klasik"):
        cevap="Klasik türünü seçtiniz".format(sarki_secim_sonuc)
        
    return cevap

if __name__ == "__main__":
    app.run(port=8000,debug=True)
