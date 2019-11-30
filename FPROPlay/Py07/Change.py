# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 19:59:17 2019

@author: filip
"""

def change(money):
    customDic = {2.0:0, 1.0:0, 0.5:0, 0.2:0, 0.1:0, 0.05:0, 0.02:0, 0.01:0}
    for i in customDic.keys():
        while round(money-i,2)>=0:
            customDic[i]+=1
            money=round(money-i,2)
        print(money)
    return customDic

print(change(7.71))