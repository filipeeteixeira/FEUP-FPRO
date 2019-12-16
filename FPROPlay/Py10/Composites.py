# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 15:06:40 2019

@author: filip
"""

def is_prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    else:
        return False
    
def get_composites(n):
    for i in range(4,n+1):
        if not is_prime(i):
            yield i


    
    