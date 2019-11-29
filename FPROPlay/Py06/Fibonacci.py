#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 14:30:38 2019

@author: filipe
"""

def fib(n):
    alist=[]
    if n<2:
        alist.append(0)
    else:
        alist.append(0)
        alist.append(1)
    for i in range(2,n):
        alist.append(alist[i-1]+alist[i-2])
    return alist
