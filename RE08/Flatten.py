#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 18:52:02 2019

@author: filipe
"""

def flatten(alist):
    resultList=[]
    for i in alist:
        if type(i)==list:
            resultList+=flatten(i)
        else:
            resultList.append(i)
    return resultList

print(flatten([['hello', ','], 'how', 'are', [[['you']]], '?']))