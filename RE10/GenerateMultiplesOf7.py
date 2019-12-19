# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 00:11:29 2019

@author: filip
"""


def multiples_of7(n):
    l = [i for i in range(0,n) if i%7==0]
    for k in l:
        yield k
print(multiples_of7(21))
         
#OU

# =============================================================================
# def multiples_of7(n):
#     l=(mult for mult in range(0, n) if mult%7 ==0)
#     return l
# print(multiples_of7(21))
# =============================================================================
