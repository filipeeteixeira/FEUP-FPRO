# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 00:26:31 2019

@author: filip
"""

from functools import reduce

def map_reduce(n1,n2):
    alist=[n**2 for n in range(n1,n2) if n%2!=0]
    return reduce(lambda x,y: x*y if x*y<50 else x+y,alist)

print(map_reduce(100,102))