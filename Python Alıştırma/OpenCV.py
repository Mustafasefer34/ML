# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 09:56:10 2024

@author: casper
"""

import cv2

#yüz tanıma için gerekli haarcascade xml dosyası

cizimxml="haarcascade_frontalface_default.xml"
yuzCascadeClassifier=cv2.CascadeClassifier(cizimxml)

#python kodunu çalıştırmadan önce kamerayı bağla
video_capture=cv2.VideoCapture(0)

#sonsuz loop içinde vşdeoda yakalanan tüm frameler işleniyor
#loop tan cıkmak ıcın q ye bas

while True:
    ret, frame=video_capture.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#SİYAH BEYAZA DÖNER 
    #detectMultiScale bize eger frame icınde yuz varsa onu tespit edip
    #yuzun ozellıklerını barındıran bir tuple tipinde dönüyor
    faceDetected=yuzCascadeClassifier.detectMultiScale(gray,minSize=(35,35))
    
    
    for (x, y, w, h) in faceDetected:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),2)
        cv2.putText(frame, "Face detected", (x+50,y+120), cv2.FONT_HERSHEY_COMPLEX,1, (0,255,0),1)
        
    #başlık yazalım
    cv2.imshow("Python Yüz Tanıma - Image Proccesing", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
       break
   
    video_capture.release()
    cv2.destroyAllWindows()