# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 13:10:04 2019

@author: filip
"""

def rearrange(l):
    l1=list(filter(lambda x: x<=0,l))
    l2=list(filter(lambda x: x>0,l))
    listt=l1+l2
    return listt