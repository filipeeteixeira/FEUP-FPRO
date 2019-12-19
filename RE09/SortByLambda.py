# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 00:21:35 2019

@author: filip
"""

def sort_by_f(alist):
    return sorted(alist, key= lambda x: 5-x if x>=5 else x, reverse=False)

print(sort_by_f([]))