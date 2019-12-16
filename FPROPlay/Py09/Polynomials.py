# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 13:02:55 2019

@author: filip
"""
from functools import reduce

def evaluate(a,x):
    return reduce(lambda n,m: n+m,list(map(lambda p: p*x**a.index(p),a)))