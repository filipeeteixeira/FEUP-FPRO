# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 00:15:14 2019

@author: filip
"""

def odd_range(start,stop,step):
    l = [i for i in range(start,stop+1) if i%2!=0]
    for k in [l[i] for i in range(0,len(l),step)]:
        yield k

print(odd_range(-50, 50, 5))