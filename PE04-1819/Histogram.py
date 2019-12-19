#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 10:47:40 2019

@author: filipe
"""

def histogram(alist,bins):
    l=[]
    for i in range(1,len(bins)):
        tmp=list(filter(lambda x: x<bins[i] and x>=bins[i-1],alist))
        l.append(len(tmp))
    return l

print(histogram([3, 0, 1, 5, 3, 2], (0, 3, 6)))
    