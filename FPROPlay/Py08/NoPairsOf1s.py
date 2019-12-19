# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 22:14:04 2019

@author: filip
"""

def countStrings(k, last_digit):
    if k==0:
        return 0
    if k==1:
        if last_digit==1:
            return 1
        else:
            return 2
    if last_digit==0:
        return countStrings(k-1,0)+countStrings(k-1,1)
    else:
        return countStrings(k-1,0)

def no_consecutives1(k):
    return countStrings(k,0)

