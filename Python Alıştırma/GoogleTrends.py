# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 10:54:11 2024
 GOOGLE TRENDS ANALİZ-1
@author: casper
"""

import pandas as pd
import matplotlib.pyplot as plt
from pytrends.request import TrendReq

pytrends= TrendReq()

#keyword listesi oluştururuz
kw_list=["python","java","javascript","visual basic"]

#payload build
pytrends.build_payload(kw_list, cat=None, timeframe='2010-01-01 2024-09-01', geo='TR')

#zamana göre dağılım
df=pytrends.interest_over_time()

#Dataframe excel dosyasına kaydedelim
df.to_excel("us_prog_lang.xlsx")

#Çizim
plt.figure(figsize=(10,8))
plt.plot(df.index, df.python, 'k*')
plt.plot(df.index, df.java, 'r*')
plt.plot(df.index, df.javascript, 'b*')
plt.plot(df.index, df["visual basic"], 'g*')

plt.show()




