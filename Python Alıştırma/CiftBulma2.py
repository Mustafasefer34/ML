# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 14:12:05 2024

@author: casper
"""

def asal_mi(sayi):
    if(sayi<=1):
        return False
    for i in range(2,sayi):
        if(sayi%i)==0:
            return False
    return True




for x in range(1,50):
    if(asal_mi(x)):
        print(x,end=" ")
   