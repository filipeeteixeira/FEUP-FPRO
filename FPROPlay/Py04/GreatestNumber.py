#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 12:56:02 2019

@author: filipe
"""

def maximo(n):
    n=str(n)
    maximo=0
    for i in range(0,len(n)):
        if (int(n[i])>=maximo):
            maximo=int(n[i])
    return str(maximo)

def greatest(num):
    result=""
    num=str(num)
    while(num!=""):
        result+=maximo(num)
        num=num[:num.index(maximo(num))]+num[num.index(maximo(num))+1:]
    return int(result)
            
print(greatest(310909))