# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 14:38:30 2019

@author: filip
"""

def biggest_member(atuple):
    for i in atuple:
        if type(i)==tuple:
            x=biggest_member(i)
            if len(x)>len(atuple):
                return x
    return atuple
    
print(biggest_member(('abc', 'jkl', ('abc', 'z', 'def', ('123', 'jkl')))))