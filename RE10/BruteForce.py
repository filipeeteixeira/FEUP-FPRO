# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 23:41:36 2019

@author: filip
"""

from itertools import permutations as p

def brute_force(f, l):
    l1= [i[0]+i[1]+i[2] for i in p(l,3)]
    return list(filter(f,l1))

print(brute_force(lambda x: x in ('abc', 'bac', 'cab', 'cba'), ['a', 'b', 'c', 'd', 'e']))

#without itertools
# =============================================================================
# 
# def brute_force(f, l):
#     return list(filter(f,[x+y+z for x in l for y in l for z in l]))
# =============================================================================
