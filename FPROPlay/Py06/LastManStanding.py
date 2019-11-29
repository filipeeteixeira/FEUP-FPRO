#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 17:18:39 2019

@author: filipe
"""

def last_man_standing(alist,step):
    posi=0
    while(len(alist)!=1):
        index=(posi+step-1)%len(alist)
        print(index)
        alist.remove(alist[index])
        posi=index
    return alist[0]

print(last_man_standing([6, 3, 8, 2, 1, 8, 5, 2, 2], 10))        