# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 10:34:41 2019

@author: filip
"""

def first_zero(alist,left,right):
    mid = left+int(right-left)//2
    if alist[mid]==0 and alist[mid-1]==1:
        return mid
    if alist[mid]==1: #se o mid não for zero
        return first_zero(alist,mid+1,right)
    else:
        return first_zero(alist,left,mid-1)
        
def count_zeros(f):
    size=len(f())
    first=first_zero(f(),0,size)
    return size-first

print(count_zeros(lambda: [1]*8 + [0]*6))