#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 21:49:06 2019

@author: filipe
"""

n = float(input())

a=0
b=n/2

def square_root(a,b,n):
    midpoint=(a+b)/2
    while(round(a,5)!=round(b,5)):
        midpoint=(a+b)/2
        
        if(midpoint*midpoint>n):
            b=midpoint
        else:
            a=midpoint
    return round(midpoint,5)
print(square_root(a,b,n))