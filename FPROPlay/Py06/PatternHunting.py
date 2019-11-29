#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 20:55:22 2019

@author: filipe
"""

def pattern_hunting(l1,l2,p):
    alist=[]
    for i in l2:
        for j in l1:
            if j.find(p)!=-1 and l2.index(i)==l1.index(j):
                alist.append(i)
            elif i.find(p)!=-1 and l2.index(i)==l1.index(j):
                alist.append(j)
    alist.sort(reverse=True)
    return alist

print(pattern_hunting(['a string', 'two strings', 'not here'], ['choose me', 'me too', 'but not me'], 'string'))
