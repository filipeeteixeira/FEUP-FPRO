# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 23:25:14 2019

@author: filip
"""
import math as m

def comprehensions(i,j):
    l = [i for i in range(i,j+1) if i%10==3 or i%10==8]
    t = tuple([round(m.sqrt(x),2) for x in range(i,j+1)])
    d = {key: chr(key) for key in range(i,j+1)}
    return (l,t,d)

print(comprehensions(65, 90))