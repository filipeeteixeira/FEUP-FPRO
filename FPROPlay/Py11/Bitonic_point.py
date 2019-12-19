# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 09:32:55 2019

@author: filip
"""

def binary_search(alist):
    mid = len(alist)//2
    if alist[mid]>alist[mid-1] and alist[mid]>alist[mid+1]:
            return alist[mid]
    if alist[mid] > alist[mid+1]:
        return binary_search(alist[:mid+1])
    else:
        return binary_search(alist[mid:])

def bitonic_point(f):
    return binary_search(f())
        
print(bitonic_point(lambda: list(range(-1, 7000001)) + list(range(5000002, 2, -1))))
    