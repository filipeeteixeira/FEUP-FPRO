#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 17:30:41 2019

@author: filipe
"""

def ackermann(m, n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ackermann(m-1,1)
    else:
        return ackermann(m-1,ackermann(m,n-1))

print(ackermann(3,4))