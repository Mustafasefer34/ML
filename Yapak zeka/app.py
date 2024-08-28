# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask, request

app=Flask(__name__)

@app.route('/havadurumu',methods=['POST'])

def hava_durumu():
    request_data=request.get_json(force=True)
    hava_durumu_sehir=request_data['hava_durumu_il']
    
    if(hava_durumu_sehir=="ankara"):
        cevap="İstediğiniz il {0} hava durumu:".format(hava_durumu_sehir)+"14 derece"
    elif(hava_durumu_sehir=="izmir"):
        cevap="İstdeğinizi il {0} hava durumu:".format(hava_durumu_sehir)+"18 derece"
    elif(hava_durumu_sehir=="istanbul"):
        cevap="İstedğiniz il {0} hava durumu:".format(hava_durumu_sehir)+"17 derece"
    
    return cevap


@app.route('/nemdurumu',methods=['POST'])

def nem_durumu():
    request_data=request.get_json(force=True)
    nem_durumu_sehir=request_data['nem_durumu_il']
    
    if(nem_durumu_sehir=="ankara"):
        cevap="İstediğiniz il {0} nem durumu:".format(nem_durumu_sehir)+"%70 nem"
    elif(nem_durumu_sehir=="izmir"):
        cevap="İstdeğinizi il {0} nem durumu:".format(nem_durumu_sehir)+"%60 nem"
    elif(nem_durumu_sehir=="istanbul"):
        cevap="İstedğiniz il {0} nem durumu:".format(nem_durumu_sehir)+"%50 nem"
    
    return cevap





if __name__ == "__main__":
    app.run(port=8000,debug=True)
