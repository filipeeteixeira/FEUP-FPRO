# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 12:55:03 2019

@author: filip
"""
from functools import reduce

def map_filter_reduce(lst,f1,f2,f3):
    return reduce(f3,list(map(f2,list(filter(f1,lst)))))