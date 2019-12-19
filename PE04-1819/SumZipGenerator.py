#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 11:22:16 2019

@author: filipe
"""

def sum_zip(functions,arguments):
    l=[]
    result=[]
    for i in arguments:
        for j in functions:
            l.append(j(i))
        yield (l,sum(l))
        l.clear()

print(sum_zip([lambda x: x*2,
lambda x: x**2,
lambda x: -x],
[-5, 10, 3]))
