# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 17:09:27 2019

@author: filip
"""

def gcd_rec(a,b):
    if(b==0): 
        return a 
    else: 
        return gcd_rec(b,a%b) 