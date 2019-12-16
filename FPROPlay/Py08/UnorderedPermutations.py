# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 09:37:35 2019

@author: filip
"""

def permutations(atuple):
    if len(atuple) == 1:
        return {atuple}
    res = set()
    for permutation in permutations(atuple[1:]):
        for i in range(len(atuple)):
            res.add(permutation[:i] + atuple[0:1] + permutation[i:])
    return res
    
print(permutations(('A', 'B', 'C')))

