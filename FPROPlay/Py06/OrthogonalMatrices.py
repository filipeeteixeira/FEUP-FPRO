#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 18:36:56 2019

@author: filipe
"""

def is_orthogonal(mx):
    result=[]
    row=[]
    row2=[]
    mult=mx[0][0]*mx[0][0]+mx[0][1]*mx[0][1]
    row.append(mult)
    mult=mx[0][0]*mx[1][0]+mx[0][1]*mx[1][1]
    row.append(mult)
    mult=mx[1][0]*mx[0][0]+mx[1][1]*mx[0][1]
    row2.append(mult)
    mult=mx[1][0]*mx[1][0]+mx[1][1]*mx[1][1]
    row2.append(mult)
    result.append(row)
    result.append(row2)
    if (result==[[1,0],[0,1]]):
        return True
    else:
        return False

print(is_ortogonal([[-1, 0], [0, 1]]))