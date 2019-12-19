#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 11:03:36 2019

@author: filipe
"""

def maximum_depth(l):
    if len(l)==0:
        return 1
    maxx=0
    for i in l:
        if type(i)==list:
            tmp=1 + maximum_depth(i)
        if tmp>maxx:
            maxx=tmp
    return maxx

print(maximum_depth([[[], [], [[]]], [[[[]]]]]))
        