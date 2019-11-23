#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 19:24:12 2019

@author: filipe
"""
def operation(tup):
    if tup[1]=='*':
        return tup[0]*tup[2]
    elif tup[1]=='-':
        return tup[0]-tup[2]
    elif tup[1]=='+':
        return tup[0]+tup[2]

def calculator(expr):
    result=0
    tup1=()
    for i in expr:
        if type(i)==tuple:
            result=calculator(i)
            tup1+=(result,)
        else:
            tup1+=(i,)
    return operation(tup1)

print(calculator((6, '-', ((3, '+', 1), '*', (9, '-', 2)))))
    