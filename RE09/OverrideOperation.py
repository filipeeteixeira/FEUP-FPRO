# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 21:15:46 2019

@author: filip
"""

def override(l1,l2):
    l= list(map(lambda x: x[0],l2))
    i = list(filter(lambda x: x[0] not in l,l1))
    r=l+i
    return sorted(r,key=lambda x: x[0])
        